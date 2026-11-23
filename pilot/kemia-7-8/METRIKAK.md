# Pilot: Kémia 7–8. – gyártási metrikák

Az 5 sorozatos éjszakai gyártás része (2026-11-23, Matek 5–6, Kémia 7–8, Biológia 7–8,
Földrajz 9–10, Matek 9–10). Szabály: egyszerre legfeljebb 5 al-ügynök fut (a sorozatok között
megosztva). A felhasználó nem volt gépnél: a terveket a koordinátor hagyta jóvá. A token-oszlop
az al-ügynök saját, Claude Code által jelentett fogyasztása.

## Al-ügynökök

| # | Feladat | Kör | Időtartam | Token (al-ügynök) | Eredmény |
|---|---|---|---|---|---|
| K1 | Leckesor terve (terv.md) | tervezés | 18 p 56 mp | 239 117 | 14 lecke, 9 modul (A–H, Tx) |
| – | Közös előkészítés (font, build, szerződés) | 0. kör | lásd `pilot/matematika-5-6/METRIKAK.md` | – | kémiai jelölés (`"chem": true`), `formula`/`equation` |
| K2 | 01-reszecskemodell (+ részecskemotor `Reszecske`, labor + nagyító `KemLab`) | 1. kör | 42 p 26 mp | 175 636 | kész: 9 lépés, QA hibátlan |

## Leckék

| Lecke | Lépések | Gyártás | QA | Kézi ellenőrzés (al-ügynök) | Megjegyzés, tanári review |
|---|---|---|---|---|---|
| 01-reszecskemodell | 9 | 42 perc, ~176 ezer token | 0 JS-hiba, `--det` ✓ | átlagsebesség N₂ 470,7 / O₂ 440,4 / H₂ 1754,6 m/s (20 °C); szabad úthossz 66 nm; 30 N 3 cm²-en = 1 bar (Boyle: fele térfogat); víz 0,005 %/bar; 50 + 50 cm³ alkohol–víz ≈ 96,5 cm³; szárazjég −78,5 °C | BIZONYTALAN: a melegedés 5 °C (mérve 3–6, számolva 6–8); „kristályosodás” vs. „deszublimáció”; borsó–mák csak szemléltetés; a hisztogram −20 → 100 °C eltolódása kicsi (≈ 21 %), nincs felnagyítva. Modulok: `Reszecske` (86–407. sor), `KemLab` (409–593. sor). `KemTx` nem készült (Unicode-indexek a fontokkal). Motorjavaslat: a vászonállapot visszaállítása képkockánként; a QA elforgatott feliratoknál téves átfedést jelez. |
