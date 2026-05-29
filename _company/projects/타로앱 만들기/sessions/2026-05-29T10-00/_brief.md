# 📋 작업 브리프

**원 명령:** [자율 사이클 — 2026-05-29] 너는 CEO다. 작업 완료 후 자동 호출된다.

⚠️ 반드시 이 순서로:
1. /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/_shared/last_report.md 읽기
   - 결과물 경로 있으면 → read_file로 실제 파일 존재 확인
   - 파일 존재 확인됨 → roadmap에서 해당 항목 ✅ 완료로 이동
   - 파일 없거나 실패 → 🔄 진행 중에서 📋 예정으로 복귀
2. /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/_shared/roadmap.md 읽기
   - 🔄 진행 중 항목 있으면 → 위에서 처리 완료된 것 제외하고 모두 📋 예정으로 복귀
   - 📋 예정이 비어있으면 → 임의로 채우지 마라. 5번 판단으로 이동
3. /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/_shared/goals.md 읽기 (방향 파악)
4. /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/_shared/decisions.md 확인 (1시간 내 중복 방지)
5. 판단:
   - 📋 예정 있음 → 1개 골라 적합한 에이전트에게 구체적으로 지시 (무엇을/어디에/어떻게)
   - 📋 예정 없고 🔄 진행 중도 없음 → Secretary에게 "모든 작업 완료, 사용자에게 최종 결과 보고" 지시

🚫 금지:
- "다음 단계를 진행하시겠습니까?" 질문 X — 네가 결정해라
- "보고합니다" "검토했습니다" 메타 답변 X — 결과물을 만들어라
- 같은 작업 1시간 안에 두 번 X
- 작업 크다 싶으면 더 작게 쪼개서 지시

## 요약
타로앱 사이트 구현 — 데이터 및 디자인 완료, developer가 구현 시작

## 분배
- **💻 코다리**: 타로 점 사이트를 /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/site/ 에 HTML/CSS/JS로 구현하세요. 데이터: /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/data/cards.json (카드 78장, id/name/upright/reversed/keywords). 디자인: /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/_shared/tarot_ui_guide.md 참고. 배경 #0A0A0F, 악센트 #8B5CF6, 버튼 호버 linear-gradient(135deg, #8B5CF6, #EC4899). 폰트: 제목 Playfair Display, 본문 Inter (Google Fonts CDN). 기능: 클릭 시 랜덤 카드 1장 표시 (정방향/역방향 랜덤 선택), 카드 이름·의미·키워드 디스플레이. 간결한 싱글 페이지로 구현. 모든 파일은 /Users/kks/Desktop/kks/_company/projects/타로앱 만들기/site/ 안에 생성 (index.html, style.css, script.js).
