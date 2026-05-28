# 🎨 Designer — 코다리가 작성한 3D 회전 및 입자 효과 코드를 검토하고, Cyber-Mysticism 테마의 미학을 극대화할 수 있는 색상 대비, 입자 밀도, 애니메이션 타이밍에 대한 세부 비주얼 가이드를 제공하세요.

🎨 Designer: 작업 시작합니다.

코다리가 구현한 3D 회전 및 입자 폭발(Particle Burst) 로직을 바탕으로, **'Cyber-Mysticism'** 테마의 정수를 담은 비주얼 스펙을 확정합니다. 이 가이드는 단순한 미적 제안을 넘어, 개발자가 CSS 변수와 Canvas API의 파라미터로 즉시 치환할 수 있는 **수치적 가이드**입니다.

---

# 🌌 Cyber-Mysticism: Visual Specification Guide (v1.0)

## 1. Color Contrast & Depth (색상 대비와 심도)
'Cyber-Mysticism'은 초자연적인 신비로움과 차가운 미래 기술의 충돌입니다. 딥 톤의 배경 위에서 네온 컬러가 '빛을 뚫고 나오는' 느낌을 주어야 합니다.

| Element | Color Hex | Role | Visual Logic |
| :--- | :--- | :--- | :--- |
| **Void Base** | `#05050A` | Background | 완전한 Black보다는 미세한 Deep Navy가 섞인 심연 |
| **Mystic Neon** | `#00F5FF` | Primary Accent | 카드의 엣지 및 주요 상호작용 입자 (Cyan) |
| **Ethereal Gold** | `#FFD700` | Secondary Accent | 신비로운 문양 및 2차 입자 (Gold/Amber) |
| **Shadow Void** | `#1A1A2E` | Depth Layer | 카드 뒷면 또는 3D 회전 시 생기는 그림자 영역 |

- **Contrast Rule:** 배경(`Void Base`)과 네온(`Mystic Neon`)의 대비를 극대화하기 위해, 카드 본체에는 미세한 `Glassmorphism` (Backdrop-filter: blur)을 적용하여 배경의 어둠이 투과되도록 합니다.

## 2. Particle Burst Specification (입자 폭발 스펙)
코다리의 70:30(Point:Line) 비율을 바탕으로 한 정밀 제어 가이드입니다.

### A. Density & Distribution (밀도와 분포)
- **Burst Trigger:** 카드가 멈추는 시점(Settling) 혹은 클릭 시점에 찰나의 폭발 발생.
- **Primary
