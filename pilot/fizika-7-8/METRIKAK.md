# Pilot: Fizika 7–8. – gyártási metrikák

A pilot célja (CLAUDE.md, 1. fázis): valódi számok a becslések helyett – gyártási idő,
tokenfogyasztás, hibaarány, tanári review-idő.

Szabály: egyszerre legfeljebb 3 al-ügynök fut.

## Al-ügynökök

| # | Feladat | Kezdés | Időtartam | Token (al-ügynök) | Eredmény |
|---|---|---|---|---|---|
| A | Közös motor, tartalomformátum + build, QA-eszköz, 01-suruseg lecke | 1. hullám | 26 p 30 mp | 253 336 (kimenet 142 388; cache-írás 372 159; cache-olvasás 9 457 676) | kész: 9 lépés, QA hibátlan |
| B | Leckesor terve (terv.md) | 1. hullám | 9 p 15 mp | 106 401 (kimenet 54 407; cache-írás 151 246; cache-olvasás 499 275) | kész: 16 lecke, 6 köteg |
| C | 05-inga lecke | 2. hullám | 20 p 12 mp | 259 895 (kimenet 100 478; cache-írás 339 735; cache-olvasás 5 650 608) | kész: 8 lépés, QA hibátlan |
| D | 07-felhajtoero lecke (Arkhimédész) | 2. hullám | 28 p 34 mp | 298 313 (kimenet 124 720; cache-írás 290 054; cache-olvasás 10 430 756) | kész: 8 lépés, QA hibátlan |
| E | 10-arnyek-tukor lecke | 2. hullám | 34 p 10 mp | 348 181 (kimenet 139 022; cache-írás 451 644; cache-olvasás 12 425 969) | kész: 9 lépés, QA hibátlan |
| F | 08-aramkor lecke | 3. hullám | 28 p 27 mp | 322 243 (kimenet 131 304; cache-írás 592 903; cache-olvasás 8 523 458) | kész: 9 lépés, QA hibátlan |
| G | 02-energia lecke | 3. hullám | 34 p 46 mp | 360 501 (kimenet 145 801; cache-írás 508 804; cache-olvasás 11 995 273) | kész: 9 lépés, QA hibátlan |
| H | 11-lencse-szem lecke | 3. hullám | 36 p 40 mp | 334 590 (kimenet 157 945; cache-írás 415 751; cache-olvasás 13 184 665) | kész: 9 lépés, QA hibátlan |

A token-oszlop az al-ügynök saját fogyasztása (a koordináló fő munkamenet nélkül).
Az első szám a Claude Code által jelentett al-ügynök-tokenszám; zárójelben az API-hívások
összesített bontása (a cache-olvasás többszörösen számolódik, de ~10%-os áron).

## Koordináló fő munkamenet

A fő munkamenet (0. fázis + pilot-koordináció, ellenőrzés) az 1. hullám végéig:
kimenet ~60 ezer, cache-írás ~169 ezer token (cache-olvasás ~6,8 millió).

## Leckék

| Lecke | Lépések | Gyártás (al-ügynök) | QA | Kézi ellenőrzés | Javítások |
|---|---|---|---|---|---|
| 01-suruseg | 9 | az A feladat része (motor + eszközök is) | 0 JS-hiba, 0 túlcsordulás | 2 hiba: 7. lépés ok-okozati ugrás (befagyás); 8. lépés a hajó 30 px-szel mélyebben látszik (két eltérő tartálygeometria) | mindkettő javítva a fő munkamenetben, kis költséggel |
| 05-inga | 8 | 20 perc, ~260 ezer token | 0 JS-hiba, 0 túlcsordulás | – | build: „15°” nem volt elfogadva → javítva a build-szkriptben (fő munkamenet) |
| 07-felhajtoero | 8 | 28,5 perc, ~298 ezer token | 0 JS-hiba, 0 túlcsordulás | 4. lépés számai ellenőrizve (p = ρgh, 9,81 N) | alsó index a panelen lokálisan megoldva (a szerződésből hiányzott) |
| 10-arnyek-tukor | 9 | 34 perc, ~348 ezer token | 0 JS-hiba, 0 túlcsordulás | 7. lépés geometriája ellenőrizve (tükör 70–130 cm, szem ~150 cm → 0–112 cm látszik) | húzás (drag) lokálisan; szélső húzásnál felirat–sugár átfedés |
| 08-aramkor | 9 | 28,5 perc, ~322 ezer token | 0 JS-hiba, 0 túlcsordulás | 6. lépés: Ohm/Kirchhoff számok és elektron- vs. technikai áramirány ellenőrizve | `L.pill` nem veszi figyelembe a `max`-ot (motor-hiány); árammérő-húzás lokálisan |
| 02-energia | 9 | 35 perc, ~361 ezer token | 0 JS-hiba, 0 túlcsordulás | 7. lépés: energiamérleg ellenőrizve (1 kg, 1,6 m → 15,7 J = 6,7 + 0,7 + 8,3) | golyóhúzás lokálisan (a 3. lecke, ami saját drag-et ír) |
| 11-lencse-szem | 9 | 37 perc, ~335 ezer token | 0 JS-hiba, 0 túlcsordulás | 7. lépés (rövidlátás) átnézve | drag a 10-es leckéből másolva; egyszerűsített szemmodell (1 mm ≈ 3,5 D, valóságban ≈ 2,7 D) |
