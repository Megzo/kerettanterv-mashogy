# Kerettanterv – másképp

Szemléletes, interaktív, animált leckék a magyar **NAT 2020 kerettantervek** témaköreihez –
tanórai kivetítésre (16:9) és egyéni használatra.

## ▶ [A leckék megnyitása: megzo.github.io/kerettanterv-mashogy](https://megzo.github.io/kerettanterv-mashogy/)

A nyitóoldal tantárgyak × évfolyamok szerint mutatja a kész leckéket (a többi „hamarosan”).
Letöltés után a repó [`index.html`](index.html)-je dupla kattintással is megnyílik, internet nélkül.

Állapot: a kerettantervek feldolgozva (0. fázis). Kész sorozatok:

- **Fizika 7–8.**, 16 lecke – [`leckek/fizika-7-8/`](leckek/fizika-7-8/), terv és gyártási
  számok: [`pilot/fizika-7-8/`](pilot/fizika-7-8/)
- **Történelem 5–6.**, 20 lecke – [`leckek/tortenelem-5-6/`](leckek/tortenelem-5-6/), terv és
  gyártási számok: [`pilot/tortenelem-5-6/`](pilot/tortenelem-5-6/)
- **Matematika 5–6.**, 18 lecke – [`leckek/matematika-5-6/`](leckek/matematika-5-6/),
  [`pilot/matematika-5-6/`](pilot/matematika-5-6/)
- **Kémia 7–8.**, 14 lecke – [`leckek/kemia-7-8/`](leckek/kemia-7-8/),
  [`pilot/kemia-7-8/`](pilot/kemia-7-8/)
- **Biológia 7–8.**, 17 lecke – [`leckek/biologia-7-8/`](leckek/biologia-7-8/),
  [`pilot/biologia-7-8/`](pilot/biologia-7-8/)
- **Földrajz 9–10.** (gimnázium), 15 lecke – [`leckek/foldrajz-9-10/`](leckek/foldrajz-9-10/),
  [`pilot/foldrajz-9-10/`](pilot/foldrajz-9-10/)
- **Matematika 9–10.** (gimnázium), 15 lecke – [`leckek/matematika-9-10/`](leckek/matematika-9-10/),
  [`pilot/matematika-9-10/`](pilot/matematika-9-10/)

Az utóbbi öt sorozat egy éjszakai, párhuzamos gépi gyártásban készült (összefoglaló, számok,
kerethasználat: [`pilot/EJSZAKAI-GYARTAS.md`](pilot/EJSZAKAI-GYARTAS.md)). **Tanári review még
nem volt** – a review-pontok sorozatonként a `METRIKAK.md`-ben vannak; három biológialecke
(újraélesztés, járvány, magzat) szakmai lektorálás nélkül nem használható.

- [`leckek/`](leckek/README.md) – a leckék; mindegyik szövege egy tanár által is
  szerkeszthető `.md`-fájlban van, a `tools/build_lesson.py` égeti be a leckébe.
- `index.html` – generált: `python3 tools/build_index.py`.

- [`kerettanterv/`](kerettanterv/README.md) – a kerettantervek tantárgyanként és kétéves
  sávonként (pl. [`fizika/7-8.md`](kerettanterv/fizika/7-8.md)), összesítő táblázat,
  témakör-lista CSV/JSON-ban.
- [`tools/`](tools/) – letöltő (`download_kerettanterv.py`) és konvertáló
  (`build_kerettanterv.py`, pandoc kell hozzá) szkript.
- `sources/` – a letöltött eredeti dokumentumok helye; a repóban csak a
  [`manifest.json`](sources/oktatas.hu_2020_nat/manifest.json) van (URL + SHA-256),
  a fájlok újra letölthetők.

Előzmény: [Mozgó magyarázatok](https://megzo.github.io/mozgo-magyarazatok/) – öt kísérleti lecke.

## Forrás

A kerettantervek szövege az Oktatási Hivatal által közzétett hivatalos dokumentumokból
származik: <https://www.oktatas.hu/kozneveles/kerettantervek/2020_nat>. A Markdown gépi
konverzió – a szöveg a forrásé, csak a tagolás egységesített; eltérés esetén az eredeti
dokumentum az irányadó.

## Újragenerálás

```bash
python3 -I tools/download_kerettanterv.py   # → sources/oktatas.hu_2020_nat/
python3 -I tools/build_kerettanterv.py      # → kerettanterv/
```
