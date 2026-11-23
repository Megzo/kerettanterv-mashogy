# shared/fonts – a leckék webfontjai

Offline WOFF2 részhalmazok; a `shared/lesson.css` `@font-face` szabályai töltik be őket.
Licenc: mind SIL Open Font License 1.1 (`OFL.txt`).

A leckék három családnevet használnak (DOM-ban és a vásznon, `ctx.font`-ban is):
**Fraunces** (cím, kiemelés, képletjel), **Bricolage Grotesque** (szöveg, felirat),
**JetBrains Mono** (szám, mértékegység). Minden családnév mögött több fájl van, `unicode-range`
szerint szétosztva – a böngésző mindig csak azt tölti le, amelyik jel a lapon tényleg előfordul.

## 1. Alap: latin + latin-ext (Google Fonts részhalmazai, kézzel nem módosítjuk)

| fájl | font | tengely |
|---|---|---|
| `fraunces-latin[-ext][-italic].woff2` | Fraunces 1.000 | wght 100–900 (opsz 14) |
| `bricolage-grotesque-latin[-ext].woff2` | Bricolage Grotesque 1.001 | wght 200–800 (opsz 14, wdth 100) |
| `jetbrains-mono-latin[-ext].woff2` | JetBrains Mono 2.211 | wght 100–800 |

## 2. Matematikai / természettudományos jelek (generált: `tools/build_fonts.py`)

Lefedett jelek mindhárom családban (normál és Fraunces dőlt):
≤ ≥ ≠ ≈ ≡ ≅ ∼ ∝ ± ∓ × · ⋅ ÷ − ∶ ∘ · √ ∛ ∜ π ∞ ∑ ∏ ∫ ∂ ∇ ∆ ‰ ‱ ° ′ ″ ‴ ℃ ℉ µ Ω Å ‖ ·
∠ ∡ ∢ ⊥ ∥ △ □ ■ ○ ● ⌀ ⟂ · görög kis- és nagybetűk (α–ω, Α–Ω, ϑ ϕ ϵ) · ∈ ∉ ⊂ ⊆ ⊃ ⊇ ∪ ∩ ∅ ∖
∀ ∃ ℕ ℤ ℚ ℝ ℂ · a teljes Arrows blokk (→ ← ↔ ⇌ ⇒ ⇔ ↦ ↑ ↓ ⇄ …) és a hosszú nyilak (⟶ ⟹ …) ·
a teljes Mathematical Operators blokk (U+2200–22FF) · felső és alsó indexek (⁰–⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ,
₀–₉ ₊ ₋ ₌ ₍ ₎, ₐ ₑ ₒ ₓ …) · törtek (½ ⅓ ⅔ ¼ ¾ ⅕ … ⅞ ⅐ ⅑ ⅒ ↉ és ⁄) · ⌈ ⌉ ⌊ ⌋.
A pontos kódpontlista: `TARGET_RANGES` a szkriptben.

Rétegek (egy jel az első rétegből jön, amelyikben megvan):

| család | 1. réteg | 2. réteg | 3. réteg |
|---|---|---|---|
| Fraunces (+ dőlt) | `fraunces-math[-italic]` – a teljes upstream Fraunces (≤ ≥ ≠ ≈ ‰ ∙) | `stix-two-text-ext[-italic]` – STIX Two Text 2.13: görög, **összes** felső/alsó index, törtek, ℕ ℝ … | `noto-sans-math` – műveleti jelek, nyilak, halmazjelek; utolsó: `noto-sans-ext` (betű-alsóindexek, ⅐ ⅑ ⅒) |
| Bricolage Grotesque | `bricolage-grotesque-math` – upstream Bricolage (π √ ∞ ∑ ∫ ≤ ≥ → ⁰–⁹ ₀–₉ …) | `noto-sans-ext` – Noto Sans: görög, ℃, törtek … | `noto-sans-math` |
| JetBrains Mono | `jetbrains-mono-math` – upstream JetBrains Mono (görög, sok műveleti jel, nyíl, index) | `noto-sans-ext` | `noto-sans-math` |

Döntések:

- **Ugyanaz a családnév**, további `@font-face` szabályokkal: a leckék kódja nem változik.
  A szabályok a CSS-ben az alapfájlok után állnak; ahol két szabály tartománya átfed (pl. U+2212,
  vagy a Fraunces ¹ ² ³), a böngésző a később megadottat nézi először.
- **A tartalékfontok `size-adjust`-ot kapnak**: a betűk (görög, indexek) az x-magassághoz, a
  műveleti jelek a nagybetű-magassághoz igazodnak.
- **Súly:** a Fraunces, Bricolage, JetBrains Mono, STIX Two Text (400–700) és Noto Sans rétegek
  változtatható vastagságúak; a Noto Sans Math csak Regular – félkövér szövegben az általa adott
  ritkább jelek (∈ ⊂ ⇒ ∠ …) vékonyabbak maradnak (szándékosan nincs műfélkövér).
- **Fraunces indexek mind a STIX-ből**: a Fraunces-ben csak ⁰¹²³⁴ van, a vegyes forrás feltűnő
  volt (10⁻³). Ezért a Fraunces ¹ ² ³ is a STIX-é lett.
- **Index-előjelek kicsinyítve (Bricolage, JetBrains Mono)**: a ⁺ ⁻ ⁼ ⁽ ⁾ ₊ ₋ ₌ ₍ ₎ a font saját
  + − = ( ) jeléből készül összetett glifaként, a ⁴ / ₄ ↔ 4 arányával és helyzetével (a Bricolage-ből
  hiányoznak, a JetBrains Mono ⁺-ja pedig mélyen a számjegyek alatt ült: Na⁺).
- **JetBrains Mono mínuszjel**: az eredeti U+2212 rajza azonos a kötőjelével (−5 ≈ -5). Itt a
  nagykötőjel (–) rajzát kapja, ami majdnem olyan széles, mint a + vízszintes szára.
- Fraunces: opsz 14, SOFT 0, WONK 0 rögzítve; Bricolage: opsz 14, wdth 100 – ugyanígy rögzítette a
  Google Fonts az alapfájlokat (glifaösszevetéssel ellenőrizve).

## Újragenerálás

Forrás: a `google/fonts` repó `ofl/` mappája, rögzített commit (`tools/build_fonts.py`: `COMMIT`);
URL + SHA-256: `sources/fonts/manifest.json`. A letöltött TTF-ek (`sources/fonts/*/`) gitignore-on.

```bash
python3 -m venv /tmp/fontvenv && /tmp/fontvenv/bin/pip install fonttools brotli
/tmp/fontvenv/bin/python -I tools/build_fonts.py --download   # első alkalommal: letöltés + manifest
/tmp/fontvenv/bin/python -I tools/build_fonts.py              # hash-ellenőrzés, részhalmazok, lesson.css blokk
```

A szkript felülírja a `*-math*.woff2`, `stix-two-text-ext*.woff2`, `noto-sans-*.woff2` fájlokat és
a `shared/lesson.css` „BEGIN generált … END generált” blokkját. Új jel: `TARGET_RANGES` bővítése.
