# 📝 CEO 종합 보고서

🎨 Designer: 작업 시작합니다.

CEO의 지시에 따라 'Cyber-Mysticism' 테마를 관통하는 인터랙션 시각 스펙을 확정하고, 개발자가 즉시 엔진에 이식할 수 있는 수준의 기술적 디자인 가이드를 작성합니다. 이 문서는 `001-010.md` 데이터가 렌더링될 때의 물리적/시각적 기준점이 됩니다.

<create_file path="/Users/kks/Desktop/kks/_company/projects/테스트/_shared/design_specs/cyber_mysticism_tarot_v1.md">
# 🌌 Cyber-Mysticism: Digital Tarot Interaction Spec (v1.0)

**Project:** Digital Tarot & Saju App
**Theme:** Cyber-Mysticism (Deep Space + Neon Occultism)
**Target:** High-fidelity Canvas/CSS-based interaction for 78 cards.

---

## 1. Color Palette & Lighting (The Void & The Glow)

The foundation is a "Deep Void" base with high-contrast "Neon Occult" accents.

### 🌑 Base Layer (The Void)
- **Background:** `#05050A` (Deepest Midnight Blue-Black)
- **Card Surface:** `#0A0A12` (Slightly lighter than BG to provide depth)
- **Shadow/Glow Spread:** `rgba(0, 0, 0, 0.8)`

### ✨ Accent Colors (The Mystical Energy)
- **Primary Neon (Cyan/Soul):** `#00F5FF` (Used for card edges and subtle UI highlights)
- **Secondary Gold (Divine/Fate):** `#FFD700` (Used for specific card symbols or 'Jack/Queen/King' highlights)
- **Tertiary Magenta (Chaos/Emotion):** `#FF007F` (Used for interaction-triggered bursts)

### 💡 Lighting Logic
- **Global Ambient:** Low-intensity dark blue.
- **Local Glow (Card-Centric):** Every card must have a `box-shadow` or Canvas-driven `shadowBlur` of `15px-25px` using its primary accent color.
- **Edge Highlight:** A sharp `1px` line of `#00F5FF` on the leading edges during rotation.
