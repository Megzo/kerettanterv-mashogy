# Pilot: Fizika 7–8. – gyártási metrikák

A pilot célja (CLAUDE.md, 1. fázis): valódi számok a becslések helyett – gyártási idő,
tokenfogyasztás, hibaarány, tanári review-idő.

Szabály: egyszerre legfeljebb 3 al-ügynök fut.

## Al-ügynökök

| # | Feladat | Kezdés | Időtartam | Token (al-ügynök) | Eredmény |
|---|---|---|---|---|---|
| A | Közös motor, tartalomformátum + build, QA-eszköz, 01-suruseg lecke | 1. hullám | 26 p 30 mp | 253 336 (kimenet 142 388; cache-írás 372 159; cache-olvasás 9 457 676) | kész: 9 lépés, QA hibátlan |
| B | Leckesor terve (terv.md) | 1. hullám | 9 p 15 mp | 106 401 (kimenet 54 407; cache-írás 151 246; cache-olvasás 499 275) | kész: 16 lecke, 6 köteg |

A token-oszlop az al-ügynök saját fogyasztása (a koordináló fő munkamenet nélkül).
Az első szám a Claude Code által jelentett al-ügynök-tokenszám; zárójelben az API-hívások
összesített bontása (a cache-olvasás többszörösen számolódik, de ~10%-os áron).

## Koordináló fő munkamenet

A fő munkamenet (0. fázis + pilot-koordináció, ellenőrzés) az 1. hullám végéig:
kimenet ~60 ezer, cache-írás ~169 ezer token (cache-olvasás ~6,8 millió).

## Leckék

| Lecke | Lépések | Gyártás (al-ügynök) | QA | Kézi ellenőrzés | Javítások |
|---|---|---|---|---|---|
| 01-suruseg | 9 | az A feladat része (motor + eszközök is) | 0 JS-hiba, 0 túlcsordulás | 8. lépés: a hajó merülése gyanús | – |
