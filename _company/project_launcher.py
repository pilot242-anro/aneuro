#!/usr/bin/env python3
"""아느로 프로젝트 런처 서버 — localhost:5999"""
import http.server, json, os, shutil, subprocess, urllib.parse
from datetime import datetime
from pathlib import Path

PORT = 5999
PROJECTS_BASE = Path.home() / "Desktop/kks/_company/projects"
GLOBAL_COMPANY = Path.home() / "Desktop/kks/_company"
# 프로젝트 간 공유 (글로벌로 심볼릭 링크) — 나머지 작업 상태는 프로젝트별 격리
SHARED_CONFIG_FILES = ["agent_models.json", "identity.md", "_system.md"]


def scaffold_project_company(folder):
    """프로젝트 폴더 안에 격리된 _company 생성.
    에이전트 팀 + 공유 설정은 글로벌 심볼릭 링크(공유),
    roadmap·sessions·reports 등 작업 상태는 빈 상태(프로젝트별 격리)."""
    proj_company = folder / "_company"
    for sub in ("_shared", "sessions", "approvals/pending",
                "approvals/history", "00_Raw/conversations"):
        (proj_company / sub).mkdir(parents=True, exist_ok=True)
    # 에이전트 팀 → 글로벌 심볼릭 링크 (한 번 고치면 전 프로젝트 반영)
    agents_link = proj_company / "_agents"
    if not agents_link.exists():
        try:
            agents_link.symlink_to(GLOBAL_COMPANY / "_agents")
        except OSError:
            pass
    # 공유 설정 파일 → 심볼릭 링크
    for fname in SHARED_CONFIG_FILES:
        src = GLOBAL_COMPANY / "_shared" / fname
        dst = proj_company / "_shared" / fname
        if src.exists() and not dst.exists():
            try:
                dst.symlink_to(src)
            except OSError:
                pass
    return proj_company


def write_workspace_settings(folder, company_dir):
    """프로젝트 폴더에 .vscode/settings.json — connectAiLab.companyDir 지정.
    이게 있어야 확장이 글로벌이 아닌 이 프로젝트 전용 _company를 사용한다."""
    vscode_dir = folder / ".vscode"
    vscode_dir.mkdir(exist_ok=True)
    sp = vscode_dir / "settings.json"
    settings = {}
    if sp.exists():
        try:
            settings = json.loads(sp.read_text(encoding="utf-8"))
        except Exception:
            settings = {}
    settings["connectAiLab.companyDir"] = str(company_dir)
    sp.write_text(json.dumps(settings, ensure_ascii=False, indent=2), encoding="utf-8")

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        # 주의: send_header는 send_response 이후에만 호출해야 함.
        # CORS 헤더는 _ok/_err 안에서 처리한다 (여기서 부르면 응답이 깨짐).

        if parsed.path == '/ping':
            self._ok('pong')

        elif parsed.path == '/open':
            name = params.get('name', [''])[0]
            if not name:
                self._err('name required'); return
            folder = PROJECTS_BASE / name
            folder.mkdir(parents=True, exist_ok=True)
            brief = folder / "BRIEF.md"
            if not brief.exists():
                brief.write_text(f"# {name}\n\n## 목표\n\n## 주요 작업\n\n## 메모\n")
            # 프로젝트별 격리된 _company 스캐폴딩 + companyDir 설정 주입
            proj_company = scaffold_project_company(folder)
            write_workspace_settings(folder, proj_company)
            subprocess.Popen(['open', '-a', 'Antigravity IDE', str(folder)])
            self._ok({'ok': True, 'path': str(folder), 'company': str(proj_company)})

        elif parsed.path == '/list':
            # 실제 폴더 목록 반환 — localStorage와 동기화용
            projects = []
            if PROJECTS_BASE.exists():
                for d in sorted(PROJECTS_BASE.iterdir()):
                    if d.is_dir() and not d.name.startswith('.'):
                        mtime = d.stat().st_mtime
                        brief_path = d / "BRIEF.md"
                        has_brief = brief_path.exists()
                        has_result = (d / "결과.html").exists() or (d / "index.html").exists()
                        projects.append({
                            'name': d.name,
                            'path': str(d),
                            'mtime': mtime,
                            'has_brief': has_brief,
                            'has_result': has_result,
                        })
            # 최신 수정 순으로 정렬
            projects.sort(key=lambda x: x['mtime'], reverse=True)
            self._ok({'projects': projects})

        else:
            self.send_response(404); self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/delete':
            length = int(self.headers.get('Content-Length', 0))
            try:
                body = json.loads(self.rfile.read(length).decode()) if length else {}
            except Exception:
                self._err('invalid json'); return
            name = body.get('name', '').strip()
            if not name or '/' in name or '..' in name:
                self._err('invalid name'); return
            folder = PROJECTS_BASE / name
            if not folder.exists() or not folder.is_dir():
                self._err('not found'); return
            # 안전을 위해 _trash 폴더로 이동 (즉시 삭제 X)
            trash = PROJECTS_BASE.parent / '_trash'
            trash.mkdir(exist_ok=True)
            stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            shutil.move(str(folder), str(trash / f"{name}_{stamp}"))
            self._ok({'ok': True, 'moved_to': str(trash / f"{name}_{stamp}")})
        else:
            self.send_response(404); self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def _ok(self, body):
        data = json.dumps(body).encode() if not isinstance(body, bytes) else body
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(data if isinstance(body, dict) else body.encode() if isinstance(body, str) else data)

    def _err(self, msg):
        self.send_response(400)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({'error': msg}).encode())

    def log_message(self, *_): pass  # 로그 끄기

if __name__ == '__main__':
    PROJECTS_BASE.mkdir(parents=True, exist_ok=True)
    print(f"아느로 런처 서버 실행 중: http://localhost:{PORT}")
    with http.server.HTTPServer(('127.0.0.1', PORT), Handler) as s:
        s.serve_forever()
