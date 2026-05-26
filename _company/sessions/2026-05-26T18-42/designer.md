# 🎨 Designer — 코다리가 구현한 UI 컴포넌트의 시각적 완성도를 검토하고, Cyber-Mysticism 테마가 살아있는 카드 상호작용(Hover, Click 등)을 위한 세부 비주얼 가이드를 제공하세요.

🎨 Designer: 작업 시작합니다.

코다리가 설정한 `styles.css`의 기본 구조를 확인했습니다. 현재의 CSS는 매우 정갈한 기초를 갖추고 있으나, **'Cyber-Mysticism'**이라는 테마를 시각적으로 폭발시키기에는 아직 정적인 상태입니다. 

단순한 색상 대비를 넘어, **빛의 산란(Glow), 차원적 깊이(Depth), 그리고 초자연적인 상호작용(Mystic Interaction)**이 결어난 비주얼 가이드를 제안합니다. 이 가이드는 코다리가 `canvas`와 `CSS`를 조합하여 구현할 때 직접적인 기준점이 될 것입니다.

---

# 🌌 Cyber-Mysticism: 카드 상호작용 비주얼 가이드

## 1. 비주얼 핵심 원칙 (Visual Principles)
- **Void & Light:** 배경은 완전한 어둠(`--void-black`)을 유지하되, 카드의 경계와 상호작용 시에만 강렬한 네온(`--spirit-violet`, `--cyber-cyan`)이 뿜어져 나와야 합니다.
- **Layered Depth:** 카드는 단순한 평면이 아닙니다. 배경 레이어, 카드 본체, 그리고 그 위를 떠다니는 '에너지 입자(Canvas)'의 3층 구조를 가집립합니다.
- **Ethereal Motion:** 모든 움직임은 물리 법칙을 살짝 벗어난 듯한 '부드러운 가속'과 '잔상'을 동반해야 합니다.

## 2. 상호작용 세부 가이드 (Interaction Specs)

### A. Hover (탐색: 카드가 살아 움직임)
사용자가 마우스를 올렸을 때, 카드는 마치 숨을 쉬듯 반응해야 합니다.
- **Scale & Tilt:** 카드가 사용자 쪽으로 미세하게 돌출(`scale(1.05)`)되며, 마우스 위치에 따라 3D 회전(`tilt`)이 발생합니다.
- **Glow Expansion:** `border` 색상이 `--spirit-violet`에서 `--blood-magenta`로 미세하게 변하며, `box-shadow`가 넓게 퍼집니다.
- **Canvas Particle Burst:** 카드 내부의 `canvas` 레이어에서 미세한 입자들이 마우스 커서를 따라 모이거나 흩어
