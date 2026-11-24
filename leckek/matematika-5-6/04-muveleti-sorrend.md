# Mennyi 2 + 3 · 4? – műveleti sorrend és műveleti tulajdonságok
tantárgy: Matematika · évfolyam: 5–6. · témakör: 4. Alapműveletek természetes számokkal

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/04-muveleti-sorrend.md
  Feliratban a # jel helyére a lecke számot ír (pl. „# zacskó” → „3 zacskó”).
  A kifejezéseket (példa, változatok, szorzat …) a lecke maga bontja fára és számolja ki; az „… eredmény”,
  „… értéke” adatokat összeveti a saját számolásával, és piros sávval jelez, ha nem egyeznek.
-->

## Közös

### Feliratok
- tippelj: Tippelj előbb!
- a tipped: a te tipped
- újra: Újra

### Adatok
- példa: 2 + 3 · 4
- helyes eredmény: 14
- balról jobbra eredmény: 20
<!-- 2 + 3 · 4 = 2 + 12 = 14 (műveleti sorrend); balról jobbra: 2 + 3 = 5, 5 · 4 = 20.
     A 2. lépés almás képe ebből a kifejezésből készül: 2 alma + 3 zacskó, mindegyikben 4 alma.
     Ezért a „példa” alakja maradjon „a + b · c” (kis egész számokkal: a ≤ 6, b ≤ 5, c ≤ 6, a + b ≤ 7). -->

## 1. Mennyi 2 + 3 · 4?
==Tippelj előbb!== Mennyi `2 + 3 · 4`? Két diák ugyanazt számolta ki. Az egyik **balról jobbra** haladt, a másik előbb szorzott. Ugyanazok a számok, mégis más eredmény jött ki. ==Melyik a jó?==

> megjegyzés: Szavazzatok, mielőtt megnézitek!

### Feliratok
- tipp gomb: Szerintem #
- válassz: Tippelj a panelen!
- út balról: balról jobbra
- út szorzás: előbb a szorzás
- így helyes: így helyes
- nem így: nem így számolunk
- más eredmény: Ugyanazok a számok, más eredmény!

## 2. A megállapodás
A számolás sorrendjét **megállapodás** rögzíti: 1. zárójel, 2. szorzás és osztás, 3. összeadás és kivonás. Azonos szinten balról jobbra haladunk. ==Miért előbb a szorzás?== A `3 · 4` egy csoport: 3 zacskó, mindegyikben 4 alma. Ha mást akarsz, tegyél zárójelet!

### Feliratok
- sorrend cím: A műveleti sorrend
- szint 1: zárójel
- szint 2: szorzás, osztás
- szint 3: összeadás, kivonás
- azonos szint: azonos szinten: balról jobbra
- zárójel jelentése: A zárójel: „ezt számold előbb!”
- zacskó felirat: # zacskó, mindegyikben # alma
- alma felirat: # alma

## 3. A kifejezésfa
A **kifejezésfa** megmutatja, mit kell előbb kiszámolni. Alul a számok, fölöttük a műveletek. ==Alulról felfelé haladunk==: a részeredmény felszáll, a kifejezés rövidül. Válassz zárójelezést a gombokkal: a fa átrendeződik, és az eredmény is változik!

### Feliratok
- alulról: alulról felfelé
- változatok cím: Ugyanazok a számok
- csoport 1: 1. csoport
- csoport 2: 2. csoport

### Adatok
- 1. változat: 8 − 4 : 2
- 2. változat: (8 − 4) : 2
- 3. változat: 8 : 4 − 2
- 4. változat: 8 : (4 − 2)
- 1. eredmény: 6
- 2. eredmény: 2
- 3. eredmény: 0
- 4. eredmény: 4
<!-- A kerettanterv javasolt tevékenysége: „ugyanazokat a számokat tartalmazó, csoportonként más-más zárójeles és
     zárójel nélküli műveletsorok elvégzése, majd az egyes csoportok eredményeinek összehasonlítása”.
     8 − 4 : 2 = 8 − 2 = 6; (8 − 4) : 2 = 4 : 2 = 2; 8 : 4 − 2 = 2 − 2 = 0; 8 : (4 − 2) = 8 : 2 = 4. -->

## 4. A számológép-csapda
Üsd be ugyanazt két gépbe! A **sorban számoló** gép minden műveleti gombnál azonnal számol, ezért =={balról jobbra eredmény} lesz az eredmény==. A **tudományos** gép ismeri a sorrendet: {helyes eredmény}.

> megjegyzés: Sok egyszerű zsebszámológép sorban számol. Próbáld ki a tiédet!

### Feliratok
- gép sorban: sorban számoló
- gép tudományos: tudományos
- már számolt: már kiszámolta: #
- ítélet sorban: balról jobbra számolt
- ítélet tudományos: betartja a sorrendet
- tipp sorban: Sorban számoló géppel előbb a szorzást üsd be!
- újra beütöm: Újra beütöm
<!-- A „sorban számoló” (azonnali végrehajtású, angolul „immediate execution”) logika: a műveleti gomb lenyomásakor
     a gép elvégzi az előző műveletet, ezért 2 + 3 × 4 = 20. A tudományos (algebrai logikájú) gépek 14-et adnak.
     Ellenőrizendő: legalább két konkrét, iskolában használt típuson kipróbálni (márkanevet a lecke nem ír). -->

## 5. Cseréld fel, csoportosítsd!
Összeadásnál és szorzásnál a számok **felcserélhetők** és **csoportosíthatók**: az eredmény nem változik. ==Ez fejszámolási trükk==: keresd a kerek párokat! `25 · 4 = 100`, így `25 · 7 · 4 = 7 · 100`. Hasonlóan: `48 · 25 = 12 · 4 · 25`.

### Feliratok
- csere felirat: felcserélem és csoportosítom
- balról cím: balról jobbra:
- ügyesen cím: ügyesen:
- nehéz: nehéz
- fejben: fejben is megy!
- bontás: bontsd fel:

### Adatok
- szorzat: 25 · 7 · 4
- átrendezve: 7 · (25 · 4)
- szorzat értéke: 700
- második szorzat: 48 · 25
- felbontva: 12 · (4 · 25)
- második eredmény: 1200
<!-- 25 · 7 = 175, 175 · 4 = 700; 25 · 4 = 100, 7 · 100 = 700. 48 = 12 · 4, 4 · 25 = 100, 12 · 100 = 1200.
     A lecke ellenőrzi, hogy az „átrendezve” és a „felbontva” értéke egyezik-e az eredetivel. -->

## 6. Ami nem cserélhető
Melyik művelet **cserélhető fel**? Próbáld ki mind a négyet a gombokkal! Összeadásnál és szorzásnál mindegy a sorrend. ==A kivonás és az osztás nem cserélhető fel:== `12 − 4 = 8`, de `4 − 12 = −8`; `12 : 4 = 3`, de `4 : 12 = 1/3`.

### Feliratok
- op összeadás: összeadás
- op kivonás: kivonás
- op szorzás: szorzás
- op osztás: osztás
- felcserélhető kérdés: felcserélhető?
- osztás magyarázat: # egység # egyenlő részre: egy rész #
- négyzetek: # négyzet
- forgatás: elforgatva

### Adatok
- első szám: 12
- második szám: 4
- különbség: 8
- fordított különbség: −8
- hányados: 3
- fordított hányados: 1/3
<!-- 12 + 4 = 4 + 12 = 16; 12 · 4 = 4 · 12 = 48; 12 − 4 = 8, 4 − 12 = −8; 12 : 4 = 3, 4 : 12 = 1/3.
     A négy eredményt a lecke kiszámolja és összeveti. A negatív szám (−8) az 5. témakör (egész számok) anyaga. -->

## 7. Széttagolás: a téglalap kettévágása
A `7 · 13` egy 7 sorból és 13 oszlopból álló téglalap. Vágd ketté: `7 · 10 + 7 · 3 = 70 + 21 = 91`. ==Mindkét darabot szorozni kell!== A `7 · 10 + 3` csak egy 3 kockás csíkot adna hozzá. Húzd a vágást: az összeg mindig ugyanannyi.

### Feliratok
- vágás csúszka: a vágás helye
- tévhit cím: Tévhit:
- hiányzik: hiányzik: # kocka
- mindig: az összeg mindig #

### Adatok
- sorok: 7
- oszlopok: 13
- vágás helye: 10
- terület: 91
- rossz eredmény: 73
<!-- 7 · 13 = 7 · (10 + 3) = 7 · 10 + 7 · 3 = 70 + 21 = 91. A tévhit: 7 · 10 + 3 = 73, ebből hiányzik 6 · 3 = 18 kocka.
     A csúszka a vágást 1 és 12 oszlop között állítja; az összeg mindig 91. -->

## 8. Becsülj, aztán számolj!
==Tippelj előbb!== Mennyi lehet `38 · 52`? Kerekíts: `40 · 50 = 2000`. A pontos érték {pontos érték}, közel van. Ha a gép {elütés eredménye}-et írna, a becslés rögtön szól: ==elütöttél valamit!==

### Feliratok
- kérdés 8: Mennyi lehet #?
- tipp kb: kb. #
- majdnem: majdnem ugyanakkora terület
- pontos: pontosan:
- közel: közel van
- elütés felirat: elütés (#):
- messze: messze van – elütötted!

### Adatok
- becsült szorzat: 38 · 52
- kerekítve: 40 · 50
- becslés: 2000
- pontos érték: 1976
- elütés: 38 · 5
- elütés eredménye: 190
<!-- 38 · 52 = 1976 (38 · 50 = 1900, 38 · 2 = 76); 40 · 50 = 2000; 38 · 5 = 190.
     A három tipp a becslés tizede, maga és tízszerese (200, 2000, 20 000). -->

## 9. Összefoglalás
- **Sorrend:** zárójel, aztán szorzás és osztás, végül összeadás és kivonás; azonos szinten balról jobbra.
- **Kifejezésfa:** alulról felfelé számolunk.
- Az összeadás és a szorzás **felcserélhető** és **csoportosítható**, a kivonás és az osztás nem.
- **Széttagolás:** `7 · (10 + 3) = 7 · 10 + 7 · 3`.
- ==Előbb becsülj, aztán számolj!==

### Feliratok
- próba: Most már menni fog: a fa mutatja az utat.
- össz sorrend: műveleti sorrend
- össz sorrend képlet: ( )  →  · :  →  + −
- össz csere: felcserélhető, csoportosítható: + és ·
- össz nem: nem cserélhető: − és :
- össz szét: széttagolható
- össz becsül: előbb becsülj!

### Adatok
- nagy példa: 5 + 2 · (9 − 3) : 4
- nagy példa értéke: 8
<!-- 5 + 2 · (9 − 3) : 4 = 5 + 2 · 6 : 4 = 5 + 12 : 4 = 5 + 3 = 8. -->

<!-- Tanári megjegyzések:
  - A „megállapodás” szó szándékos: a műveleti sorrend konvenció, nem természeti törvény. A 2. lépés almás képe
    azt mutatja, miért kényelmes ez a megállapodás (a szorzat egy „csoport”, az összeg zárójel nélkül leírható).
  - Az alma- és zacskós példa kitalált didaktikai példa.
  - A kifejezésfa jelölése (a műveleti jel a csúcsban, a számok a levelekben, alul a kifejezés szövege) nem
    tankönyvi szabvány; a tankönyvek egy része „műveleti fát” vagy „számolási sorrend-ívet” rajzol helyette.
  - A számológép-gombokon × és ÷ jel van (ahogy a valódi gépeken); a lecke szövegében · és : áll.
  - A 6. lépésben a 4 : 12 = 1/3 tört eredmény, a 4 − 12 = −8 negatív szám: mindkettő túlmegy a 4. témakör
    (természetes számok) keretein; a 6. (törtek) és az 5. (egész számok) témakörre utal előre.
  - A 7. lépés téglalapja a széttagolhatóság területmodellje (7 · 13 = 7 · 10 + 7 · 3).
  - A 8. lépés téglalapjai méretarányosak (1 egység = 7 px): a 38 · 52 és a 40 · 50 területe majdnem egyforma.
-->
