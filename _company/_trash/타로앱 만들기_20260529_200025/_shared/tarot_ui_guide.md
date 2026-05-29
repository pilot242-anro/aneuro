# 🔮 타로앱 UI/UX 스타일 가이드

> **버전:** v1.0  
> **작성자:** Designer (aneuro)  
> **적용 대상:** 타로 카드 선택 화면, 카드 리딩 결과 화면, 전체 앱 비주얼 시스템  
> **참고 데이터:** `data/cards.json` (78장 카드 데이터)

---

## 1. 브랜드 컬러 시스템

### 1.1 Primary Palette

| 용도 | 색상명 | HEX | CSS 변수 | 비고 |
|------|--------|-----|----------|------|
| 배경 (다크) | Deep Void | `#0A0A0F` | `--bg-primary` | 앱 전체 배경 |
| 배경 (카드) | Card Surface | `#1A1A24` | `--bg-card` | 카드·모달 배경 |
| 주요 강조 | Mystic Violet | `#8B5CF6` | `--accent-primary` | 버튼·강조 텍스트·액티브 상태 |
| 보조 강조 | Cosmic Pink | `#EC4899` | `--accent-secondary` | 리버스(역방향) 표시·포인트 |
| 텍스트 (주) | Starlight White | `#F1F1F6` | `--text-primary` | 본문·제목 |
| 텍스트 (보조) | Nebula Gray | `#9CA3AF` | `--text-secondary` | 설명·레이블·작은 글씨 |
| 경계선 | Star Dust | `#2D2D3A` | `--border-subtle` | 카드 테두리·구분선 |
| 성공/긍정 | Fortune Gold | `#F59E0B` | `--accent-gold` | 정방향 표시·특별 보상 |
| 그림자 | Void Shadow | `rgba(0,0,0,0.6)` | `--shadow-heavy` | 모달·카드 그림자 |

### 1.2 Gradient (주요 3종)

```css
/* 카드 리딩 배경 그라데이션 */
--grad-card-surface: linear-gradient(135deg, #1A1A24 0%, #2D1B69 100%);

/* 버튼 호버/액티브 */
--grad-accent: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%);

/* 결과 화면 배경 (긍정) */
--grad-result-positive: linear-gradient(180deg, #0A0A0F 0%, #1A0A2E 100%);

/* 결과 화면 배경 (도전/역방향) */
--grad-result-challenge: linear-gradient(180deg, #0A0A0F 0%, #2E0A0A 100%);
```

### 1.3 색상 사용 원칙

| 요소 | 색상 적용 규칙 |
|------|---------------|
| 화면 배경 | `--bg-primary` 고정. 그라데이션 X (콘텐츠 집중) |
| 카드 배경 | `--bg-card` + 얇은 `--border-subtle` 테두리 |
| 버튼 Primary | `--accent-primary` 배경, 흰색 텍스트 |
| 버튼 Secondary | 투명 배경, `--accent-primary` 테두리+텍스트 |
| 카드명 | `--text-primary`, bold |
| 설명 텍스트 | `--text-secondary`, regular weight |
| 역방향 표시 | `--accent-secondary` (Cosmic Pink) 배지 + "역방향" 텍스트 |
| 정방향 표시 | `--accent-gold` (Fortune Gold) 배지 + "정방향" 텍스트 |

---

## 2. 타이포그래피

### 2.1 Font Stack

```css
/* 제목·카드명 — 세리프, 신비로운 분위기 */
--font-display: 'Playfair Display', 'Noto Serif KR', Georgia, serif;

/* 본문·설명 — 가독성 중심 산세리프 */
--font-body: 'Inter', 'Noto Sans KR', -apple-system, sans-serif;

/* 숫자·코드 — 모노스페이스 */
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

### 2.2 Type Scale

| 구분 | 크기 | Weight | Line Height | 폰트 | 용도 |
|------|------|--------|-------------|------|------|
| H1 | 32px | Bold (700) | 1.2 | display | 화면 제목 |
| H2 | 24px | SemiBold (600) | 1.3 | display | 섹션 제목 |
| H3 | 20px | SemiBold (600) | 1.3 | display | 카드 이름 |
| Body L | 17px | Regular (400) | 1.6 | body | 카드 의미 본문 |
| Body M | 15px | Regular (400) | 1.5 | body | 설명·부가 텍스트 |
| Body S | 13px | Regular (400) | 1.4 | body | 레이블·작은 메모 |
| Caption | 11px | Medium (500) | 1.3 | body | 태그·배지·시간 |
| Mono | 14px | Regular (400) | 1.4 | mono | 퍼센트·수치 |

### 2.3 타이포 적용 규칙

- **카드명 (H3):** `Playfair Display Bold 20px`, `--text-primary`, 가운데 정렬
- **카드 의미 본문 (Body L):** `Inter/Noto Sans KR Regular 17px`, `--text-secondary`, 좌측 정렬, 1.6 line-height
- **버튼 텍스트:** `Inter SemiBold 15px`, letter-spacing 0.5px, 대문자 없음
- **배지 (정방향/역방향):** `Inter Medium 11px`, letter-spacing 1px, 대문자

---

## 3. 카드 선택 UI (Card Selection Screen)

### 3.1 레이아웃

```
┌─────────────────────────────────┐
│  🔮 오늘의 타로         ← back  │  ← 상단 바 (H1 타이틀)
├─────────────────────────────────┤
│                                 │
│     ┌───┐  ┌───┐  ┌───┐       │
│     │ 1 │  │ 2 │  │ 3 │       │  ← 카드 3장 (뒷면 상태)
│     │ ? │  │ ? │  │ ? │       │
│     └───┘  └───┘  └───┘       │
│                                 │
│     "가장 끌리는 카드를        │
│      선택하세요"               │  ← Body L, text-secondary
│                                 │
│     [ 카드 한 장 뽑기 ]        │  ← Primary 버튼
│                                 │
└─────────────────────────────────┘
```

### 3.2 카드 뒷면 디자인 (선택 전)

| 속성 | 값 |
|------|-----|
| 크기 | 100w × 160h (px), 모서리 12px radius |
| 배경 | `--bg-card` + `--grad-card-surface` |
| 테두리 | `--border-subtle` 1px solid |
| 그림자 | `--shadow-heavy` 0 8px 32px |
| 중앙 패턴 | 육망성(hexagram) 아이콘, `--accent-primary` 40% 투명도 |
| 호버 시 | transform: translateY(-8px), box-shadow 증가, transition 0.3s ease |
| 탭/클릭 시 | scale(0.95) 후 앞면으로 플립 |

### 3.3 카드 앞면 디자인 (선택 후)

```
┌───────────┐
│  ☽        │  ← 왼쪽 상단: 문양 아이콘 (마이너=슈트 심볼, 메이저=별)
│           │
│  The Moon │  ← H3, card name
│           │
│  ───────  │  1px solid --border-subtle
│           │
│  환상과   │  ← Body L, 의미 키워드 1줄
│  직관의   │
│  카드     │
│           │
│   정방향  │  ← 배지 (gold / pink)
└───────────┘
```

- **전환 애니메이션:** 3D Y-axis flip, 0.6s, `transform-style: preserve-3d`
- **뒷면→앞면 시:** 뒷면이 먼저 fade 0.3s, 앞면이 scale(0.8→1) + fade 0.3s

### 3.4 "카드 한 장 뽑기" 버튼

| 속성 | 값 |
|------|-----|
| 위치 | 화면 하단, 가운데 정렬, margin-top: 32px |
| 크기 | min-width 200px, height 52px |
| 배경 | `--grad-accent` (violet→pink) |
| 텍스트 | `--text-primary` white, SemiBold 15px |
| 테두리 반경 | 26px (fully rounded) |
| 그림자 | `0 4px 20px rgba(139,92,246,0.4)` |
| 호버 시 | brightness 1.1, transform scale(1.02) |
| 탭 시 | scale(0.98), 그림자 축소 |
| Disabled | opacity 0.4, pointer-events none (카드 이미 선택됨) |

---

## 4. 결과 화면 (Reading Result Screen)

### 4.1 레이아웃

```
┌─────────────────────────────────┐
│  🔮 당신의 카드        ← back  │  ← 상단 바
├─────────────────────────────────┘
│
│  ┌─────────────────────────┐
│  │                         │
│  │    (카드 앞면 전체)     │  ← 카드 앞면, 화면 중앙, 크기 140w×220h
│  │    The Moon             │
│  │                         │
│  └─────────────────────────┘
│
│  ┌─────────────────────────┐
│  │  🟡 정방향              │  ← 배지 (gold bg, white text)
│  └─────────────────────────┘
│
│  ┌─────────────────────────┐
│  │  환상과 직관의 카드     │  ← H2, 카드명
│  │                         │
│  │  달의 카드는...         │  ← Body L, 정방향 의미 전문 (80-120자)
│  │  (정방향 의미 전체)     │
│  │                         │
│  │  키워드: 환상, 직관,    │  ← Body M, keywords
│  │  불안, 숨겨진 진실      │
│  └─────────────────────────┘
│
│  ┌─────────────────────────┐
│  │ [ 한 번 더 보기 ]       │  ← Secondary 버튼
│  │ [ 처음으로 ]            │  ← Primary 버튼
│  └─────────────────────────┘
│
└─────────────────────────────────┘
```

### 4.2 카드 표시 영역

| 속성 | 값 |
|------|-----|
| 카드 크기 | 140w × 220h px (선택 화면보다 큼) |
| 모서리 | 16px radius |
| 배경 | `--bg-card` + 카드별 색상 약간 반영 (선택) |
| 그림자 | `0 12px 48px rgba(0,0,0,0.6)` + `0 0 60px rgba(139,92,246,0.15)` 글로우 |
| 진입 애니메이션 | 아래에서 위로 슬라이드 (translateY(60px) → 0, 0.5s, ease-out) |
| 지속 효과 | 미세한 floating 애니메이션 (translateY(-3px) → 0, 4s infinite, ease-in-out) |

### 4.3 결과 텍스트 영역

| 요소 | 속성 |
|------|------|
| 배경 | `--bg-card` + border-radius 16px + padding 24px |
| 카드명 (H2) | `--font-display`, `--text-primary`, margin-bottom 8px |
| 의미 본문 | `--font-body`, `--text-secondary`, Body L, line-height 1.6 |
| 키워드 | Inline-flex chips, `--border-subtle` 1px solid, `--text-secondary`, padding 4px 12px, border-radius 99px |
| 키워드 배경 | `rgba(139,92,246,0.1)` |
| 진입 딜레이 | 카드 0.3s 후, 텍스트 영역 fade-in 0.4s |
| 방향 배지 | 우측 상단 고정, `--accent-gold`(정방향) / `--accent-secondary`(역방향) |

### 4.4 액션 버튼 (하단)

| 버튼 | 스타일 | 위치 | 동작 |
|------|--------|------|------|
| "한 번 더 보기" | Secondary: 투명 배경, `--accent-primary` 1px solid 테두리, `--accent-primary` 텍스트 | 왼쪽 | 같은 카드 다시 표시 (랜덤 재선택) |
| "처음으로" | Primary: `--grad-accent` 배경, 흰색 텍스트 | 오른쪽 | 카드 선택 화면으로 이동 |

모바일에서는 버튼을 세로로 배치 (위/아래), 데스크톱에서는 가로 배치 (좌/우)

---

## 5. 공통 UI 컴포넌트

### 5.1 네비게이션 바 (Top Bar)

| 속성 | 값 |
|------|-----|
| 배경 | `--bg-primary` + `rgba(10,10,15,0.8)` 백드롭 블러(blur 12px) |
| 높이 | 56px |
| 하단 테두리 | `--border-subtle` 0.5px solid |
| 제목 | H1 (32px → 모바일 24px) |
| 뒤로 가기 | 왼쪽, chevron-left 아이콘, `--text-secondary` |
| z-index | 100 |

### 5.2 로딩 상태

```css
/* 카드 선택 후 로딩 */
--loader-color: var(--accent-primary);
--loader-size: 40px;
--loader-border: 3px solid var(--border-subtle);
```

- 중앙 원형 스피너, 2초 이상 시 "카드의 에너지를 읽는 중..." Body M 텍스트 표시
- 스피너가 끝나면 결과 화면으로 fade 전환 (0.3s)

### 5.3 에러 상태

- 카드 데이터 로드 실패 시: 아이콘(⚠️) + "카드를 불러오지 못했습니다" Body L + [다시 시도] 버튼
- 배경: `--bg-primary`, 텍스트: `--text-secondary`
- "다시 시도": Primary 버튼 스타일

### 5.4 빈 상태/첫 진입

- "아직 뽑은 카드가 없습니다. 아래 버튼을 눌러 시작하세요." Body L, `--text-secondary`
- 부드러운 페이드인 + 버튼 pulsing 애니메이션 (opacity 1→0.7→1, 2s)

---

## 6. 모바일 반응형 기준

| 디바이스 | 기준 너비 | 카드 크기 | 폰트 스케일 | 레이아웃 변경 |
|----------|-----------|-----------|-------------|---------------|
| 모바일 | < 480px | 80w×130h (선택), 120w×190h (결과) | H1→24px, H2→20px, Body L→15px | 버튼 세로 배치, 카드 3장 1열 |
| 태블릿 | 481~1024px | 100w×160h, 140w×220h | 기준 유지 | 카드 3장 가로 배치 |
| 데스크톱 | > 1024px | 120w×190h, 160w×250h | 기준 유지 | 카드 3장 가로 배치, 최대 폭 600px 중앙 정렬 |

---

## 7. 애니메이션 & 트랜지션 요약

| 구분 | 지속시간 | 타이밍 함수 | 설명 |
|------|----------|-------------|------|
| 카드 호버 | 0.3s | ease | translateY(-8px) + box-shadow 증가 |
| 카드 선택 (탭) | 0.15s | ease | scale(0.95) |
| 카드 플립 | 0.6s | ease-in-out | 3D Y축 회전, 뒷면→앞면 |
| 카드 슬라이드인 | 0.5s | ease-out | translateY(60px) → 0 |
| 텍스트 페이드인 | 0.4s | ease | opacity 0→1, delay 0.3s |
| 페이지 전환 | 0.3s | ease | opacity+scale cross-fade |
| 버튼 호버 | 0.2s | ease | brightness/scale 변화 |
| 로딩 스피너 | infinite | linear | rotate 360deg |
| 카드 플로팅 | 4s | ease-in-out | translateY(-3px↔0) |

---

## 8. 구현 시 주의사항 (Developer 전달)

### 8.1 접근성
- 모든 인터랙티브 요소에 `min 44×44px` 터치 영역 확보
- 색상 대비: 텍스트(`--text-primary` on `--bg-primary`) = #F1F1F6 on #0A0A0F → contrast ratio **17.7:1** (WCAG AAA 통과)
- 보조 텍스트(`--text-secondary` on `--bg-primary`) = #9CA3AF on #0A0A0F → contrast ratio **7.3:1** (WCAG AAA 통과)
- 배지는 색상 외에도 "정방향/역방향" 텍스트로 식별 가능
- 모든 애니메이션은 `prefers-reduced-motion` 미디어쿼리 시 `transition: none`, `animation: none`

### 8.2 성능
- CSS 변수로 컬러 시스템 정의 → 테마 전환·유지보수 용이
- 카드 이미지는 SVG 또는 CSS-only 패턴 (외부 이미지 로딩 최소화)
- 애니메이션은 `transform` + `opacity`만 사용 (GPU 가속, 레이아웃 리플로우 없음)
- 카드 3장 이미지 프리로드 (선택 화면 진입 시)

### 8.3 데이터 연결
- 카드 선택 시 `data/cards.json`에서 랜덤 1장 추출
- 정방향/역방향은 50% 확률로 결정
- 결과 화면에서 해당 카드의 `upright` 또는 `reversed` 의미 텍스트 표시
- 키워드는 `keywords` 배열에서 쉼표로 연결

### 8.4 에지 케이스
- 네트워크 오프라인: 캐시된 마지막 결과라도 표시 (있는 경우)
- 카드 데이터 로드 실패: 에러 화면 표시 (5.3 참고)
- 화면 회전: 레이아웃 유지, orientationchange 이벤트 시 카드 위치 재계산 없음 (CSS Grid/Flexbox 사용)
- 매우 긴 카드 의미 텍스트: max-height 300px + 내부 스크롤 (선택 화면), 결과 화면은 전체 표시

### 8.5 CSS 변수 완전 목록 (index.css / global.css에 정의)

```css
:root {
  /* 배경 */
  --bg-primary: #0A0A0F;
  --bg-card: #1A1A24;
  
  /* 강조 */
  --accent-primary: #8B5CF6;
  --accent-secondary: #EC4899;
  --accent-gold: #F59E0B;
  
  /* 텍스트 */
  --text-primary: #F1F1F6;
  --text-secondary: #9CA3AF;
  
  /* 보더 */
  --border-subtle: #2D2D3A;
  
  /* 섀도우 */
  --shadow-heavy: rgba(0,0,0,0.6);
  
  /* 그라데이션 */
  --grad-card-surface: linear-gradient(135deg, #1A1A24 0%, #2D1B69 100%);
  --grad-accent: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%);
  --grad-result-positive: linear-gradient(180deg, #0A0A0F 0%, #1A0A2E 100%);
  --grad-result-challenge: linear-gradient(180deg, #0A0A0F 0%, #2E0A0A 100%);
  
  /* 타이포 */
  --font-display: 'Playfair Display', 'Noto Serif KR', Georgia, serif;
  --font-body: 'Inter', 'Noto Sans KR', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
}
```