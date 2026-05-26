#!/usr/bin/env python3
"""아느로 프로젝트 런처 서버 — localhost:5999"""
import http.server, json, os, subprocess, urllib.parse
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

        else:
            self.send_response(404); self.end_headers()

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
