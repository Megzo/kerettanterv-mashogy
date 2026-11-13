# Pilot: Történelem 5–6. – gyártási metrikák

Szabály: egyszerre legfeljebb 3 al-ügynök fut. A token-oszlop az al-ügynök saját fogyasztása
(a koordináló fő munkamenet nélkül); zárójelben az API-hívások bontása.

## Al-ügynökök

| # | Feladat | Kör | Időtartam | Token (al-ügynök) | Eredmény |
|---|---|---|---|---|---|
| T1 | Leckesor terve (terv.md) | tervezés | 20 p 54 mp | 205 750 (kimenet 118 346; cache-írás 351 818; cache-olvasás 1 724 783) | 18 lecke (+2 a felhasználó döntésével), 7 modul, szerkesztői elvek |
| T2 | Előkészítés: Natural Earth térképadatok (`shared/tort/`), build-bővítés (évszám, dátum, koordináta, tartomány, becslés), szerződés 11. § | 0. kör | 22 p 30 mp | 245 066 (kimenet 111 037; cache-írás 243 494; cache-olvasás 10 544 803) | kész; a fizika-leckék tartalma változatlan, selftest hibátlan |
| T3 | 08-vandorlas – az `iskola` leckéjének átültetése (világos téma, .md) | 0. kör | 23 p 46 mp | 286 033 (kimenet 97 329; cache-írás 438 914; cache-olvasás 10 045 266) | kész: 10 lépés, QA hibátlan |

## Leckék

| Lecke | Lépések | Gyártás | QA | Kézi ellenőrzés | Megjegyzés |
|---|---|---|---|---|---|
| 08-vandorlas | 10 | 24 perc, ~286 ezer token (átültetés) | 0 JS-hiba, 0 túlcsordulás | 6. lépés (Etelköz) képernyőképe átnézve | a törzsek helye Etelközön belül szemléltető (nem ismert) – tanári review; a záró, teljes útvonalas nézet zsúfolt |
