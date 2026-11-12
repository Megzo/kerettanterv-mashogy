# Kerettanterv – másképp

Szemléletes, interaktív, animált leckék a magyar **NAT 2020 kerettantervek** témaköreihez –
tanórai kivetítésre (16:9) és egyéni használatra.

A projekt lépésenként halad; jelenleg a **0. fázisnál** tart: a hivatalos kerettantervek
összegyűjtése és géppel olvasható, egységes Markdownra alakítása.

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
