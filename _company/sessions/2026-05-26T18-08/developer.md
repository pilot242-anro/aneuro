# 💻 코다리 — designer가 제안한 디자인 시스템을 바탕으로, 네온서바이버 템플릿(HTML/Canvas/JS) 환경에서 즉시 적용 가능한 CSS 변수 및 기본 UI 컴포넌트 구조를 코드로 구현하세요.

💻 코다리: 작업 시작합니다.

디자이너가 제안한 네온서바이버 템플릿과 타로카드 디자인 시스템을 바탕으로 CSS 변수와 기본 UI 컴포넌트 구조를 구현합니다.

먼저, `web_init` 도구를 사용하여 프로젝트를 초기화합니다.

<run_command>cd "/Users/kks/Desktop/kks/_company/_agents/developer/tools" && python3 web_init.py --kit vanilla --output_dir ~/connect-ai-projects/mystic-neon-tarot</run_command>

프로젝트 초기화 후, CSS 변수와 기본 UI 컴포넌트를 구현합니다.

<create_file path="~/connect-ai-projects/mystic-neon-tarot/index.html">
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mystic Neon Tarot</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>Mystic Neon Tarot</h1>
        </header>
        <main class="main">
            <section class="card-display">
                <div class="card">
                    <div class="card-front">
                        <canvas id="cardCanvas" width="200" height="300"></canvas>
                    </div>
                    <div class="card-back">
                        <p>🔮 미래를 예지하는 신비한 카드</p>
                    </div>
                </div>
            </section>
            <section class="controls">
                <button class="draw-button">카드 뽑기</button>
            </section>
        </main>
        <footer class="footer">
            <p>&copy; 2026 aneuro</p>
        </footer>
    </div>
    <script src="script.js"></script>
</body>
</html>
</create_file>

<create_file path="~/connect-ai-projects/mystic-neon-tarot/styles.css">
:root {
    --surface-background: #0A0A0F;
    --primary-neon: #8A2BE2;
    --secondary

---
## 🛠️ 도구 실행 결과 (시스템 자동 실행)

### 🔧 실행: `cd "/Users/kks/Desktop/kks/_company/_agents/developer/tools" && python3 web_init.py --kit vanilla --`
```
❌ 이미 존재: /Users/kks/connect-ai-projects/my-app — 다른 이름 쓰거나 폴더 지우세요
```
_❌ exit 1_

---
## 📁 파일 액션 결과

✅ 생성: ~/connect-ai-projects/mystic-neon-tarot/index.html
