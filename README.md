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
- **Természettudomány 5–6.**, 17 lecke – [`leckek/termeszettudomany-5-6/`](leckek/termeszettudomany-5-6/),
  [`pilot/termeszettudomany-5-6/`](pilot/termeszettudomany-5-6/)
- **Magyar nyelv és irodalom 5–6.**, 17 lecke – [`leckek/magyar-5-6/`](leckek/magyar-5-6/),
  [`pilot/magyar-5-6/`](pilot/magyar-5-6/)
- **Digitális kultúra 5–6.**, 17 lecke – [`leckek/digitalis-kultura-5-6/`](leckek/digitalis-kultura-5-6/),
  [`pilot/digitalis-kultura-5-6/`](pilot/digitalis-kultura-5-6/) – saját, offline blokkprogramozóval
  és robotszimulátorral
- **Történelem 7–8.**, 17 lecke – [`leckek/tortenelem-7-8/`](leckek/tortenelem-7-8/),
  [`pilot/tortenelem-7-8/`](pilot/tortenelem-7-8/) – a nemzetállamoktól az uniós csatlakozásig; saját, vázlatos történeti
  határok adatfájlja ([`shared/tort/`](shared/tort/README.md)), és új modulok a leckékben: történeti
  területek és frontok (TortTerr), vázlatos Budapest (TortCity), parlamenti patkó és mandátumszámító
  (TortParl), intézményséma (TortState)

Ezzel a nyitóoldal 5–6. évfolyamos oszlopának mind az öt tárgya (matematika, magyar, történelem,
természettudomány, digitális kultúra) kapott egy-egy sorozatot.

Az utóbbi kilenc sorozat párhuzamos gépi gyártásban készült (öt egy éjszaka alatt – összefoglaló,
számok, kerethasználat: [`pilot/EJSZAKAI-GYARTAS.md`](pilot/EJSZAKAI-GYARTAS.md) –, a
természettudomány, a magyar és a digitális kultúra a következő napon, a Történelem 7–8. az azutáni
napon). **Tanári review még nem volt** – a review-pontok sorozatonként a `METRIKAK.md`-ben vannak.
Szakmai lektorálás nélkül nem használható: három biológialecke (újraélesztés, járvány, magzat), a
természettudományból a tűz (tűzvédelem) és az emberi test (egészség), a digitális kultúrából a
jelszó, a digitális lábnyom és az álhír (online biztonság), a Történelem 7–8. sorozatból a holokauszt
(történész és emlékezetpedagógus) és további hét lecke: Trianon, a diktatúrák, a második
világháború, a szovjetizálás, 1956, a rendszerváltoztatás és a határon túli magyarok (történész) –
így a sorozat 20. századi leckéinek többsége lektort kér.

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
