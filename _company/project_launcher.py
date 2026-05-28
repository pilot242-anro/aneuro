#!/usr/bin/env python3
"""아느로 프로젝트 런처 서버 — localhost:5999"""
import http.server, json, os, shutil, subprocess, urllib.parse
from datetime import datetime
from pathlib import Path

PORT = 5999
PROJECTS_BASE = Path.home() / "Desktop/kks/_company/projects"

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        self.send_header('Access-Control-Allow-Origin', '*')

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
            subprocess.Popen(['open', '-a', 'Antigravity IDE', str(folder)])
            self._ok({'ok': True, 'path': str(folder)})

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
