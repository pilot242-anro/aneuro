# 🌌 Cyber-Mysticism: Major Arcana (14-21) Design Guide

본 가이드는 `Writer`가 생성한 14-21번 메이저 타로 데이터의 의미를 시각화하기 위한 **Cyber-Mysticism** 테마의 정밀 디자인 스펙입니다. 개발자는 이 수치와 속성을 기반으로 CSS 애니메이션, Canvas 입자 효과, WebGL 셰이더를 구성합니다.

## 🎨 1. Core Visual System (공통 시스템)

### [Color Palette: Neon-Ethereal]
- **Primary (Void):** `#0A0A0F` (깊은 우주적 블랙, 배경 및 카드 베이스)
- **Secondary (Mystic Gold):** `#FFD700` → `#B8860B` (신비로운 황금빛, 주요 광원/텍스트)
- **Accent (Cyber Blue):** `#00F5FF` (디지털 정체성, 입자/회전 효과)
- **Accent (Ethereal Pink):** `#FF00FF` (운명적/강렬한 감정, 특정 카드 강조)

### [Typography: Future-Classic]
- **Heading:** `Cinzel` (Serif, 고전적/신비적 느낌) - 카드 번호 및 이름
- **Body:** `Inter` (Sans-serif, 가독성 중심) - 카드 의미/설명
- **Scale:** Title `2.5rem`, Subtitle `1.2rem`, Body `1rem`

### [Visual Elements: The "Frost-Rotation" Effect]
- **Frost (서리꽃):** 카드 가장자리에 미세한 `white/cyan` 입자가 결정체처럼 맺히는 효과 (`filter: blur()`와 `opacity` 애니메이션 활용).
- **Rotation (회전):** 카드가 정면을 향할 때, 배경의 기하학적 문양이 미세하게 역방향으로 회전하여 입체감을 부여 (`transform: rotateZ()`).
- **Particle (입자):** 카드가 선택되거나 의미가 강조될 때, 중심에서 외곽으로 퍼지는 `radial-gradient` 기반의 입자 폭발.

---

## 🃏 2. Card-Specific Design Elements (14-21번)

각 카드의 의미적 정체성을 시각적 속성(Color/Effect/Particle)으로 매핑합니다.

| No | Card Name | Key Concept | Primary Color | Visual Effect/Particle |
|:---|:---|:---|:---|:---|
| **14** | **Temperance** | Balance/Flow | `#E0F7FA` (Cyan) | 부드러운 물결(Wave) 애니메이션, 수평 이동 입자 |
| **15** | **The Devil** | Temptation/Bond | `#FF4500` (Red-Orange) | 붉은 안개(Fog), 쇠사슬 느낌의 날카로운 선(Line) |
| **16** | **The Tower** | Sudden Change | `#FFA500` (Amber) | 폭발적인 수직 낙하 입자, 균열(Crack) 시각화 |
| **17** | **The Star** | Hope/Inspiration | `#F0FFFF` (Azure) | 반짝이는 별(Twinkle), 부드러운 광원 확산 |
| **18** | **The Moon** | Illusion/Intuition | `#483D8B` (Dark Slate) | 일렁이는 물결, 어두운 보라색 안개 |
| **19** | **The Sun** | Vitality/Success | `#FFFF00` (Yellow) | 강렬한 방사형 광원(Radial Glow), 황금빛 입자 폭발 |
| **20** | **Judgement** | Awakening/Call | `#F5F5F5` (Silver) | 천사의 날개 느낌의 대칭적 입자 상승 |
| **21** | **The World** | Completion/Unity | `#DA70D6` (Orchid) | 완벽한 원형(Circle) 회전, 통합된 빛의 고리 |

---

## 🛠 3. Technical Implementation Guide (개발 가이드)

### [A. CSS/Canvas Layering Strategy]
1. **Layer 0 (Background):** `#0A0A0F` Solid Background.
2. **Layer 1 (Card Base):** `clip-path`를 활용한 정교한 카드 프레임. `box-shadow: 0 0 20px rgba(0,0,0,0.5)`.
3. **Layer 2 (Visual Elements):** `Canvas API`를 사용하여 `Frost`와 `Particle` 효과를 독립적으로 렌더링.
4. **Layer 3 (Overlay/Text):** `z-index: 10`. `mix-blend-mode: screen`을 사용하여 빛 효과가 카드 베이스와 어우러지게 설정.

### [B. Animation Specs]
- **Idle State:** `scale(1.0)` + 미세한 `floating` (y-axis: `+/- 5px`).
- **Hover/Focus:** `scale(1.05)` + `drop-shadow: 0 0 15px [Card_Primary_Color]`.
- **Trigger (Pick/Shuffle):** `Particle Burst` (입자 폭발) + `Rotation` (회전).

### [C. Responsive Design]
- **Mobile-First:** 카드는 화면 너비의 `85%`를 차지하되, `aspect-ratio: 2/3`를 유지.
- **Touch Interaction:** `Framer Motion` 또는 `GSAP`을 사용하여 부드러운 `Spring` 물리 엔진 적용.