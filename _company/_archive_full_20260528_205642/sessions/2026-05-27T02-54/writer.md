# ✍️ Writer — 디지털 타로카드 의미 데이터 파일 (/Users/kks/Desktop/kks/_company/my-mobile-app/src/data/tarot_cards/meaning/011-020.json) 수정: 중복 제거, 의미 텍스트 간결화, 사용자 친화적 문장으로 재작성. 작업 후 roadmap.md에서 '🔄 진행 중' 항목을 '✅ 완료'로 변경해 주세요.

✍️ Writer: 작업 시작합니다.

<read_file path="/Users/kks/Desktop/kks/_company/_shared/roadmap.md"/>

<read_file path="/Users/kks/Desktop/kks/_company/my-mobile-app/src/data/tarot_cards/meaning/011-020.json"/>

<edit_file path="/Users/kks/Desktop/kks/_company/my-mobile-app/src/data/tarot_cards/meaning/011-020.json"><find>[]</find><replace>[
  {
    "id": 11,
    "name_en": "Justice",
    "name_ko": "정의",
    "number": "11",
    "suit": "major",
    "keywords": ["균형", "결정", "공정", "책임"],
    "meaning_upright": "객관적인 판단과 균형이 필요한 시기예요. 옳은 결정을 내리고 자신의 행동에 책임을 지게 될 거예요.",
    "meaning_reversed": "불공정함이나 편향된 판단을 주의해야 해요. 감정에 치우친 결정이 문제를 일으킬 수 있어요.",
    "description": "저울과 칼을 든 모습. 감정에 휘둘리지 않는 냉철한 이성과 정의를 상징합니다."
  },
  {
    "id": 12,
    "name_en": "The Hanged Man",
    "name_ko": "매달린 사람",
    "number": "12",
    "suit": "major",
    "keywords": ["인내", "관점의 전환", "정지", "희생"],
    "meaning_upright": "지금은 움직일 때가 아니라 관점을 바꿔야 할 때예요. 인내하며 새로운 시각을 찾는 과정이 필요합니다.",
    "meaning_reversed": "무의미한 희생이나 정체 상태를 의미해요. 헛된 고집을 버리고 현실을 직시해야 합니다.",
    "description": "나무에 거꾸로 매달린 사람. 멈춰 있는 듯 보이지만 내면의 깨달음을 얻는 과정입니다."
  },
  {
    "id": 13,


---
## 📁 파일 액션 결과

📖 읽기: ~/Desktop/kks/_company/_shared/roadmap.md (38줄, 2.0KB)
```
 1	# 🗺️ 프로젝트 로드맵
 2	
 3	_여기엔 **각 프로젝트별 작업**만 적습니다._
 4	_회사 운영·인프라·매출 같은 회사 전체 일은 `goals.md`에._
 5	_에이전트가 작업 끝낼 때마다 자동 업데이트._
 6	
 7	---
 8	
 9	## 🔮 디지털 타로카드 & 사주앱
10	
...
```
⚠️ 읽기 실패: /Users/kks/Desktop/kks/_company/my-mobile-app/src/data/tarot_cards/meaning/011-020.json — 파일이 존재하지 않습니다.

[시스템: read_file 결과]
파일: ~/Desktop/kks/_company/_shared/roadmap.md (38줄)
```
 1	# 🗺️ 프로젝트 로드맵
 2	
 3	_여기엔 **각 프로젝트별 작업**만 적습니다._
 4	_회사 운영·인프라·매출 같은 회사 전체 일은 `goals.md`에._
 5	_에이전트가 작업 끝낼 때마다 자동 업데이트._
 6	
 7	---
 8	
 9	## 🔮 디지털 타로카드 & 사주앱
10	
11	### ✅ 완료
12	- 프로젝트 폴더 + 기본 구조 생성
13	- 디자이너 — UI/UX 디자인 시스템 확정 (Cyber-Mysticism 테마)
14	- 디자이너 — 컬러 팔레트 + 타이포그래피 + 컴포넌트 가이드
15	- 디자이너 — 썸네일 + 브랜드 비주얼 3안 제시
16	- 디자이너 — 카드 상호작용(Hover/Click) 비주얼 가이드
17	- 디자이너 — 입자 폭발(Particle Burst) 시각 스펙 확정 (70:30)
18	- 코다리 — 네온서바이버 PayPal 결제 템플릿 통합
19	- 코다리 — CSS 변수 + 3층 레이어 구조 설계
20	- 코다리 — HTML5 Canvas 카드 렌더링 엔진 구현
21	- 코다리 — 3D 회전(Tilt) 효과 코드 작성
22	- 코다리 — 입자 폭발(Particle Burst) 렌더링 엔진 코드
23	
24	### 🔄 진행 중
25	- 카드 셔플 애니메이션 디테일 조정
26	- 입자 밀도·타이밍 최적화
27	- 코드 통합 및 첫 작동 데모 만들기
28	
29	### 📋 예정
30	- ✍️ Writer — 타로 메이저 0~10번 데이터 작성 (바보/마법사/여사제/여황제/황제/교황/연인/전차/힘/은둔자/운명의수레바퀴) → `/Users/kks/Desktop/kks/_company/my-mobile-app/src/data/tarot_major_00-10.json` 신규 create_file
31	- ✍️ Writer — 타로 메이저 11~21번 데이터 작성 (정의/매달린사람/죽음/절제/악마/탑/별/달/태양/심판/세계) → `/Users/kks/Desktop/kks/_company/my-mobile-app/src/data/tarot_major_11-21.json` 신규 create_file
32	- 사주 계산 로직 구현 (생년월일·생시 → 사주 8자)
33	- 카드 뽑기 → 해석 → 결과 페이지 플로우
34	- 메인 랜딩 페이지 완성
35	- 결제 시스템 실제 연동 (PayPal/토스)
36	- 베타 사용자 10명 테스트
37	- 정식 서비스 배포 (Vercel/Cloudflare Pages)
38	
```
