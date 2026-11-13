# Pilot: Történelem 5–6. – gyártási metrikák

Szabály: egyszerre legfeljebb 3 al-ügynök fut. A token-oszlop az al-ügynök saját fogyasztása
(a koordináló fő munkamenet nélkül); zárójelben az API-hívások bontása.

## Al-ügynökök

| # | Feladat | Kör | Időtartam | Token (al-ügynök) | Eredmény |
|---|---|---|---|---|---|
| T1 | Leckesor terve (terv.md) | tervezés | 20 p 54 mp | 205 750 (kimenet 118 346; cache-írás 351 818; cache-olvasás 1 724 783) | 18 lecke (+2 a felhasználó döntésével), 7 modul, szerkesztői elvek |
| T2 | Előkészítés: Natural Earth térképadatok (`shared/tort/`), build-bővítés (évszám, dátum, koordináta, tartomány, becslés), szerződés 11. § | 0. kör | 22 p 30 mp | 245 066 (kimenet 111 037; cache-írás 243 494; cache-olvasás 10 544 803) | kész; a fizika-leckék tartalma változatlan, selftest hibátlan |
| T3 | 08-vandorlas – az `iskola` leckéjének átültetése (világos téma, .md) | 0. kör | 23 p 46 mp | 286 033 (kimenet 97 329; cache-írás 438 914; cache-olvasás 10 045 266) | kész: 10 lépés, QA hibátlan |
| T4 | 06-var-uradalom (+ jelenet-metszet modul: TortScene) | 1. kör | 37 p 51 mp | 79 336 a jelentés szerint – valószínűleg tömörítés miatt alacsony (a naplóból: kimenet 193 928; cache-írás 707 669; cache-olvasás 13 798 179) | kész: 9 lépés, QA hibátlan |
| T5 | 01-idoszamitas (+ idővonal és forráskártya modul: TortTimeline, TortSource) | 1. kör | 38 p 7 mp | 92 495 a jelentés szerint – valószínűleg tömörítés miatt alacsony (a naplóból: kimenet 184 386; cache-írás 536 878; cache-olvasás 6 417 273) | kész: 9 lépés, QA hibátlan |

## Leckék

| Lecke | Lépések | Gyártás | QA | Kézi ellenőrzés | Megjegyzés |
|---|---|---|---|---|---|
| 08-vandorlas | 10 | 24 perc, ~286 ezer token (átültetés) | 0 JS-hiba, 0 túlcsordulás | 6. lépés (Etelköz) képernyőképe átnézve | a törzsek helye Etelközön belül szemléltető (nem ismert) – tanári review; a záró, teljes útvonalas nézet zsúfolt |
| 06-var-uradalom | 9 | 38 perc, kimenet ~194 ezer (a legdrágább eddig) | 0 JS-hiba, 0 túlcsordulás | adatok és „vitatott pontok” átolvasva: kilenced 1351, robot 1514 (heti 1 nap = 52) és 1767 (52 igás / 104 gyalog), Visegrád 1247 / 1323 / 1335 | a 14. századi robot (kb. 3–12 nap) ellenőrizendő; a 9. lépés képe hasonlít az 1.-re |
| 01-idoszamitas | 9 | 38 perc, kimenet ~184 ezer | 0 JS-hiba, 0 túlcsordulás | 5. lépés képernyőképe: Kr. e. 776 → 753 = 23 év, „monda” jelölés a hagyományos dátumokon | a „most” évszámot (2026) évente frissíteni kell |
