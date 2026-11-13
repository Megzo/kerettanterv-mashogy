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
| T6 | 04-pannonia (+ térképmotor: TortMap) | 1. kör | 44 p 55 mp | 112 798 a jelentés szerint – valószínűleg tömörítés miatt alacsony (a naplóból: kimenet 211 628; cache-írás 797 182; cache-olvasás 12 272 778) | kész: 9 lépés, QA hibátlan |
| T7 | 07-kozepkori-varos (+ kártyajáték-modul: TortCards) | 2. kör | 34 p 58 mp | 115 831 a jelentés szerint (a naplóból: kimenet 166 465; cache-írás 626 866; cache-olvasás 11 825 220) | kész: 9 lépés, QA hibátlan; 3 modult változtatás nélkül vett át |
| T8 | 18-gozgep | 2. kör | 41 p 48 mp | 186 241 (kimenet 195 348; cache-írás 1 165 947; cache-olvasás 11 702 786) | kész: 9 lépés, QA hibátlan; párhuzamosan saját TortCards-t írt (a 07-esé a referencia) |

## Leckék

| Lecke | Lépések | Gyártás | QA | Kézi ellenőrzés | Megjegyzés |
|---|---|---|---|---|---|
| 08-vandorlas | 10 | 24 perc, ~286 ezer token (átültetés) | 0 JS-hiba, 0 túlcsordulás | 6. lépés (Etelköz) képernyőképe átnézve | a törzsek helye Etelközön belül szemléltető (nem ismert) – tanári review; a záró, teljes útvonalas nézet zsúfolt |
| 06-var-uradalom | 9 | 38 perc, kimenet ~194 ezer (a legdrágább eddig) | 0 JS-hiba, 0 túlcsordulás | adatok és „vitatott pontok” átolvasva: kilenced 1351, robot 1514 (heti 1 nap = 52) és 1767 (52 igás / 104 gyalog), Visegrád 1247 / 1323 / 1335 | a 14. századi robot (kb. 3–12 nap) ellenőrizendő; a 9. lépés képe hasonlít az 1.-re |
| 01-idoszamitas | 9 | 38 perc, kimenet ~184 ezer | 0 JS-hiba, 0 túlcsordulás | 5. lépés képernyőképe: Kr. e. 776 → 753 = 23 év, „monda” jelölés a hagyományos dátumokon | a „most” évszámot (2026) évente frissíteni kell |
| 04-pannonia | 9 | 45 perc, kimenet ~212 ezer (a legdrágább: térképmotor) | 0 JS-hiba, 0 túlcsordulás | 4. lépés (limes, Duna-határ, mai nevek) képernyőképe átnézve | a provinciahatárok „vázlatos” kézi közelítések, atlasszal nincs egybevetve; a hun idősávon a 451/452/453 címkék összeérnek |
| 07-kozepkori-varos | 9 | 35 perc, kimenet ~166 ezer | 0 JS-hiba, 0 túlcsordulás | adatok: Pest 1244, Buda 1247 k., Budai jogkönyv 1405–1421, népesség-becslések; 7. lépés képernyőképe átnézve | Buda alaprajza sematikus; Kassa 1307 (első céhlevél) és a kapu-/piacidők ellenőrizendők |
| 18-gozgep | 9 | 42 perc, kimenet ~195 ezer | 0 JS-hiba, 0 túlcsordulás | évszámok: Newcomen 1712, Watt 1769/1781, jenny 1764 k., mule 1779, gyári törvény 1833 (9 év alatt tilos, 9–13: 9 óra + 2 óra iskola), Pest–Vác 1846. júl. 15.; 2. lépés képe átnézve | Watt gépe egyszerűsített rajz; a tanú (Bentley) adatai ellenőrizendők |
