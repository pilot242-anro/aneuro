# 🌌 Cyber-Mysticism: 메이저 타로카드 디자인 가이드 (14-21번)

본 가이드는 `Cyber-Mysticism` 테마를 기반으로, 14-21번 메이저 타로카드의 시각적 정체성을 확립하고 개발자가 CSS/Canvas/WebGL로 즉시 구현할 수 있는 정밀한 스펙을 제공합니다.

## 1. 디자인 컨셉: "Digital Frost & Ethereal Rotation"
- **핵심 키워드:** 서리꽃(Frost Flower), 회전하는 기하학(Rotating Geometry), 파스텔 네온(Pastel Neon), 디지털 신비주의.
- **비주얼 스토리:** 차갑고 정적인 '서리'의 미학과 역동적인 '회전' 요소가 결합되어, 정해진 운명의 궤적을 시각화합니다.

## 2. 컬러 팔레트 (Color Palette)
전체적으로 어두운 배경(Deep Space) 위에서 부드럽게 빛나는 파스텔 톤의 네온 컬러를 사용합니다.

| 요소 | 색상 코드 (HEX) | 설명 |
| :--- | :--- | :--- |
| **Base Background** | `#0A0B10` | 심연의 우주, 카드 배경의 기본 색상 |
| **Frost White** | `#E0F7FA` | 서리꽃의 결정체, 메인 라인 및 하이라이트 |
| **Mystic Lavender** | `#B39DDB` | 신비로운 분위기를 더하는 보조 색상 |
| **Ethereal Gold** | `#FFD54F` | 중요한 상징물(태양, 별 등)의 미세한 광원 |
| **Cyan Frost** | `#80DEEA` | 차가운 에너지와 디지털 느낌의 강조색 |

## 3. 시각적 요소 및 구현 스펙 (Visual Elements & Specs)

### A. 서리꽃 결정체 (Frost Patterns)
- **설명:** 카드 테두리나 특정 문양 주위에 생성되는 정교한 결정체 패턴.
- **구현 방법:** 
  - `SVG Filter` 또는 `Canvas API`를 사용하여 미세한 선(Line)들이 얽힌 형태.
  - `Opacity: 0.4~0.6`을 적용하여 너무 과하지 않게 배경과 어우러지도록 설정.
  - `Filter: blur(0.5px)`를 주어 부드러운 결정체 느낌 강조.

### B. 회전하는 기하학 요소 (Rotating Elements)
- **설명:** 카드의 중심 혹은 특정 문양 주위를 도는 고리(Ring) 또는 입자(Particle).
- **구현 방법:**
  - `CSS Animation (transform: rotate)` 또는 `Three.js`를 활용한 부드러운 회전.
  - `Ease-in-out` 타이밍 함수를 사용하여 회전 속도가 자연스럽게 변하도록 설정.
  - 중심축을 기준으로 서로 다른 속도로 회전하는 2~3개의 동심원 레이어 구성.

### C. 입자 폭발 효과 (Particle Burst)
- **설명:** 카드를 선택하거나 결과가 나타날 때 발생하는 시각적 피드백.
- **구현 방법:**
  - `Canvas` 기반의 입자 시스템.
  - `Particle Life-cycle`: 생성(Spawn) → 확장(Expand) → 서서히 사라짐(Fade-out).
  - 색상은 `Frost White`와 `Cyan Frost`를 주력으로 사용.

## 4. 타이포그래피 (Typography)
- **Main Title (Card Name):** `Montserrat` 또는 `Cinzel` (Serif 계열의 우아하고 고전적인 느낌).
- **Sub Text (Meaning):** `Inter` 또는 `Noto Sans KR` (가독성을 위한 Sans-serif 계열).
- **Style:** `Letter-spacing: 0.1em`을 적용하여 여백의 미 확보.

## 5. 개발자를 위한 레이아웃 가이드 (Layout Guide)
- **Aspect Ratio:** `2:3` (표준 타로카드 비율).
- **Safe Zone:** 카드 테두리에서 `5%` 안쪽 영역에 핵심 문양 배치.
- **Layering:**
  1. `Layer 0 (Bottom)`: Background (`#0A0B10`)
  2. `Layer 1`: Frost Patterns (Static/Slow motion)
  3. `Layer 2`: Main Card Symbol (Centerpiece)
  4. `Layer 3`: Rotating Elements (Dynamic)
  5. `Layer 4 (Top)`: Typography & UI Overlay