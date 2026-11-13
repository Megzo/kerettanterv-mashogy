# Kerettanterv – másképp

Szemléletes, interaktív, animált leckék a magyar **NAT 2020 kerettantervek** témaköreihez –
tanórai kivetítésre (16:9) és egyéni használatra.

**Nyitóoldal:** [`index.html`](index.html) – tantárgyak × évfolyamok, a kész leckékkel
(a többi „hamarosan”). Letöltés után dupla kattintással is megnyílik, internet nélkül.

Állapot: a kerettantervek feldolgozva (0. fázis); a pilot – **Fizika 7–8.**, 15 lecke –
elkészült ([`leckek/fizika-7-8/`](leckek/fizika-7-8/), terv és gyártási számok:
[`pilot/fizika-7-8/`](pilot/fizika-7-8/)).

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
