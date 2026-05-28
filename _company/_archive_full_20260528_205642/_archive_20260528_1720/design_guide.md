# 🌌 Cyber-Mysticism Design Guide: Major Arcana (14-21)

본 가이드는 `14-21번 메이저 타로카드`의 시각적 정체성을 확립하고, 개발자가 CSS/Canvas/WebGL을 통해 즉시 구현할 수 있는 정밀한 시각 스펙을 정의합니다. `Cyber-Mysticism` 테마(신비로운 고전미 + 미래적 디지털 미학)를 핵심으로 합니다.

---

## 🎨 1. Core Visual Concept: Cyber-Mysticism
- **Concept Definition:** 고전적인 타로의 상징물(서리꽃, 천체, 신화적 요소)이 디지털 입자(Particle), 광원(Glow), 그리고 정밀한 기하학적 회전(Rotation)과 결합된 형태.
- **Visual Mood:** 정적이면서도 미세하게 움직이는(Micro-interaction), 신비롭고 차가운 듯 따뜻한(Pastel-Neon) 분위기.

---

## 💎 2. Key Design Elements (14-21 적용 스펙)

### A. 서리꽃 & 결정체 (Frost/Crystal Patterns)
- **Description:** 카드의 테두리나 특정 상징물 주변에 생성되는 정밀한 결정체 패턴.
- **Implementation Guide:**
  - **SVG/Canvas:** `stroke-dasharray`를 활용한 미세한 선형 패턴 또는 `Canvas API`를 이용한 정육각형(Hexagon) 기반의 결정체 생성.
  - **Visual:** `opacity: 0.6` 정도의 반투명한 화이트/파스텔 블루 계열.
  - **Interaction:** 마우스 호버 시 결정체가 미세하게 확장되거나 빛을 발산(Bloom effect).

### B. 회전 요소 (Orbital/Rotational Elements)
- **Description:** 카드 중심의 핵심 상징물 주위를 도는 궤도(Orbit) 혹은 회전하는 기하학적 고리.
- **Implementation Guide:**
  - **CSS Animation:** `transform: rotate()`를 활용하되, 각 요소의 회전 속도를 다르게 설정 (`ease-in-out` 적용).
  - **Z-index Layering:** 배경 궤도(느린 회전) -> 중간 상징(중간 회전) -> 전경 입자(빠른 회전) 순으로 레이어를 쌓아 입체감 확보.

### C. 파스텔 톤 & 네온 광원 (Pastel-Neon Palette)
- **Description:** 너무 강렬한 원색보다는 부드러운 파스텔 톤에 디지털적인 광원(Glow)을 결합.
- **Color Palette:**
  - `Primary (Mystic Blue): #A2D2FF`
  - `Secondary (Ethereal Pink): #FFC8DD`
  - `Accent (Cosmic Gold): #FFD670`
  - `Background (Deep Void): #1A1A2E` (카드 배경은 어둡게 유지하여 광원 강조)
- **Effect:** `filter: drop-shadow()` 또는 `box-shadow`를 사용하여 색상이 공중에 떠 있는 듯한 느낌 부여.

---

## 🛠 3. Technical Implementation Guide (for Developers)

### 🌌 Layered Architecture (Z-index Strategy)
1. **Layer 0 (Base):** 카드 배경 (`#1A1A2E`), 미세한 그라데이션 (`radial-gradient`).
2. **Layer 1 (Pattern):** 서리꽃/결정체 패턴 (`opacity: 0.3`, `mix-blend-mode: screen`).
3. **Layer 2 (Main Symbol):** 카드 고유의 메인 그래픽 (SVG/Image).
4. **Layer 3 (Orbital):** 회전하는 고리 및 궤도 (`animation: rotate-loop`).
5. **Layer 4 (Particles):** 마우스/클릭 시 발생하는 입자 폭발 (`Canvas/WebGL`).

### ⚡ Interaction Specs
- **Hover (Discovery):** 카드가 부드럽게 앞으로 돌출 (`transform: scale(1.02)`) + 서리꽃 패턴의 광도 증가 (`filter: brightness(1.2)`).
- **Click/Pick (Manifestation):** 선택 시 `Particle Burst` 발생. 선택된 카드의 색상 테마가 화면 전체에 미세하게 확산.
- **Transition:** 카드 셔플 시 `Ease-in-out`을 통한 부드러운 회전 및 이동.

---

## 📝 4. 14-21번 카드별 시각적 변주 (Quick Reference)
*각 카드의 의미에 따라 위 요소들의 비중을 조절합니다.*

| 번호 | 카드명 | 핵심 시각 요소 | 추천 색상 조합 |
| :--- | :--- | :--- | :--- |
| 14 | 절제 (Temperance) | 물의 흐름 + 순환하는 고리 | `Cyan + Gold` |
| 15 | 악마 (Devil) | 대칭적인 뿔 + 어두운 입자 | `Deep Red + Dark Purple` |
| 16 | 탑 (Tower) | 수직적 균열 + 폭발하는 광원 | `Electric Orange + Dark Grey` |
| 17 | 별 (Star) | 수많은 미세 입자 + 수직적 빛 | `Pale Blue + White` |
| 18 | 달 (Moon) | 층층이 쌓인 구름 + 일렁이는 궤도 | `Silver + Indigo` |
| 19 | 태양 (Sun) | 중심부 폭발적 광원 + 회전하는 광륜 | `Bright Gold + Warm Orange` |
| 20 | 심판 (Judgement) | 나팔 소리를 시각화한 파동 + 상승하는 입자 | `Pure White + Gold` |
| 21 | 세계 (World) | 완전한 원형 궤도 + 정밀한 결정체 통합 | `Iridescent/Holographic` |