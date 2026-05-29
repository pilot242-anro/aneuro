#!/usr/bin/env python3
"""아느로 프로젝트 런처 — localhost:5999
프로젝트마다 완전히 격리된 폴더 생성:
  kks/_company/projects/<이름>/
    ├── _shared/      ← 이 프로젝트만의 roadmap, last_report 등
    ├── sessions/     ← 이 프로젝트만의 작업 기록
    ├── _agents →     ← 글로벌 에이전트 팀 (심볼릭 공유)
    └── .vscode/settings.json  ← connectAiLab.companyDir = 이 폴더
"""
import http.server, json, os, shutil, subprocess, urllib.parse
from datetime import datetime
from pathlib import Path

PORT = 5999
BASE = Path.home() / "Desktop/kks/_company"
PROJECTS = BASE / "projects"
GLOBAL_AGENTS = BASE / "_agents"
# 공유 설정 파일 (심볼릭 링크)
SHARED_FILES = ["agent_models.json", "identity.md", "_system.md"]


def make_project(folder: Path):
    """프로젝트 폴더 구조 생성 — 모든 작업 데이터는 여기에만 쌓인다."""
    for sub in ["_shared", "sessions", "approvals/pending", "approvals/history", "00_Raw/conversations"]:
        (folder / sub).mkdir(parents=True, exist_ok=True)

    # _agents → 글로벌 심볼릭 (에이전트 설정은 공유)
    link = folder / "_agents"
    if not link.exists() and GLOBAL_AGENTS.exists():
        link.symlink_to(GLOBAL_AGENTS)

    # 공유 설정 파일 심볼릭
    for fname in SHARED_FILES:
        src = BASE / "_shared" / fname
        dst = folder / "_shared" / fname
        if src.exists() and not dst.exists():
            try: dst.symlink_to(src)
            except: pass

    # .vscode/settings.json — companyDir을 이 프로젝트로 고정
    vs = folder / ".vscode"
    vs.mkdir(exist_ok=True)
    sp = vs / "settings.json"
    s = {}
    if sp.exists():
        try: s = json.loads(sp.read_text())
        except: pass
    s["connectAiLab.companyDir"] = str(folder)
    sp.write_text(json.dumps(s, ensure_ascii=False, indent=2))


class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        p = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(p.query)

        if p.path == "/ping":
            return self._ok("pong")

        if p.path == "/open":
            name = q.get("name", [""])[0].strip()
            if not name: return self._err("name required")
            folder = PROJECTS / name
            folder.mkdir(parents=True, exist_ok=True)
            brief = folder / "BRIEF.md"
            if not brief.exists():
                brief.write_text(f"# {name}\n\n## 목표\n\n## 메모\n")
            make_project(folder)
            subprocess.Popen(["open", "-a", "Antigravity IDE", str(folder)])
            return self._ok({"ok": True, "path": str(folder)})

        if p.path == "/list":
            result = []
            if PROJECTS.exists():
                for d in sorted(PROJECTS.iterdir()):
                    if d.is_dir() and not d.name.startswith("."):
                        result.append({
                            "name": d.name,
                            "path": str(d),
                            "mtime": d.stat().st_mtime,
                            "has_brief": (d / "BRIEF.md").exists(),
                        })
            result.sort(key=lambda x: x["mtime"], reverse=True)
            return self._ok({"projects": result})

        self.send_response(404); self.end_headers()

    def do_POST(self):
        p = urllib.parse.urlparse(self.path)
        if p.path == "/delete":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            name = body.get("name", "").strip()
            if not name or "/" in name or ".." in name:
                return self._err("invalid name")
            folder = PROJECTS / name
            if not folder.exists(): return self._err("not found")
            trash = BASE / "_trash"
            trash.mkdir(exist_ok=True)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            shutil.move(str(folder), str(trash / f"{name}_{stamp}"))
            return self._ok({"ok": True})
        self.send_response(404); self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _ok(self, body):
        data = json.dumps(body).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def _err(self, msg):
        self.send_response(400)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({"error": msg}).encode())

    def log_message(self, *_): pass


if __name__ == "__main__":
    PROJECTS.mkdir(parents=True, exist_ok=True)
    print(f"런처 시작: http://localhost:{PORT}")
    print(f"프로젝트 경로: {PROJECTS}")
    with http.server.HTTPServer(("127.0.0.1", PORT), H) as s:
        s.serve_forever()
