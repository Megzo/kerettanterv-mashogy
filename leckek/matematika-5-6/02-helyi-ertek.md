# Mennyit ér egy számjegy? – helyi érték, nagy számok, kerekítés
tantárgy: Matematika · évfolyam: 5–6. · témakör: 3. Természetes számok halmaza, számelméleti ismeretek

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/02-helyi-ertek.md
  Feliratban a # jel helyére a lecke számot ír (pl. „kb. #” → „kb. 350”).
  A nagy számokban (5 jegytől) a tagoló szóköz nem törő szóköz, hogy a szám ne törjön két sorba;
  a build a sima szóközt is elfogadja.
  Az eredményeket (valódi érték, a nulla nélküli szám, a kerekítések, a római és a kettes alak, egy év
  másodpercben) a lecke maga számolja, és piros sávval jelez, ha a .md-ben írt érték nem egyezik.
-->

## Közös

### Feliratok
- tippelj: Tippelj előbb!
- a tipped: a te tipped
- jó tipp: jó tipp!
- rossz tipp: nem talált
- forgasd: Forgasd egérrel!
- mutasd: Mutasd!
- újra: Újra
- egyes: egyes
- tízes: tízes
- százas: százas
- ezres: ezres
- ezer: ezer
- millió: millió
- milliárd: milliárd
- billió: billió

## 1. Tízesével csoportosítunk
Hány pálcika van az asztalon? ==Tippelj előbb!== Egyenként számolni lassú. Kössünk inkább **tízes kötegeket**, aztán tíz kötegből egy **százas köteget**! A számjegyek ezt mondják meg: hány százas köteg, hány tízes köteg és hány szál maradt.

> megjegyzés: Tegyél hozzá szálakat! Mi történik, ha tíz szál összegyűlik?

### Feliratok
- kérdés 1: Hány pálcika van az asztalon?
- tipp pálcika: kb. #
- kötegeld: Kötegeld!
- plusz egy: +1 szál
- plusz tíz: +10 szál
- százas köteg: százas köteg
- tízes köteg: tízes köteg
- szál: szál
- tíz szál: 10 szál = 1 köteg
- tíz köteg: 10 köteg = 1 százas köteg
- tele: Ennél több már nem fér el ebben a játékban.

### Adatok
- pálcikák száma: 347
<!-- kitalált példa. A lecke a pálcikákat a szám jegyei szerint köti össze (3 százas köteg, 4 tízes köteg,
     7 szál); a tipp-gombok a számból készülnek (kb. 200 / 350 / 500). Legfeljebb 999 (9 százas köteg). -->

## 2. Kocka, rúd, lap, nagy kocka
Tíz kis **kocka** egy **rúd**. Tíz rúd egy **lap**. Tíz lap egy **nagy kocka**. ==Minden lépésben tízszer annyi.== Ezért elég tíz számjegy, a 0-tól a 9-ig: egy helyen sosem kell kilencnél többet számolnunk.

> megjegyzés: Forgasd meg! Hány kis kocka van a nagy kockában?

### Feliratok
- kérdés 2: Mi lesz tíz egyformából?
- kis kocka: kis kocka
- rúd: rúd
- lap: lap
- nagy kocka: nagy kocka
- tízszer: tízszer annyi

## 3. Mennyit ér egy számjegy?
A {vizsgált szám} első jegyének **alaki értéke** {alaki érték}, **helyi értéke** a százas, **valódi értéke** {valódi érték}. A 0 nem semmi: ==helyet tart.== Ha elhagyod, a többi jegy jobbra csúszik, és {nulla nélkül} lesz belőle.

> megjegyzés: Kattints egy számjegyre! Mit ér a 0?

### Feliratok
- kérdés 3: Mennyit ér egy számjegy?
- alaki érték felirat: alaki érték
- helyi érték felirat: helyi érték
- valódi érték felirat: valódi érték
- hagyd el: Hagyd el a 0-t!
- tedd vissza: Tedd vissza a 0-t!
- helyet tart: a 0 helyet tart
- üres hely: üres
- kattints jegyre: Kattints egy számjegyre!
- nem ugyanaz: nem ugyanannyi!

### Adatok
- vizsgált szám: 305
- alaki érték: 3
- valódi érték: 300
- nulla nélkül: 35
<!-- kitalált példa. 305 = 3 · 100 + 0 · 10 + 5; a 0 nélkül 35 = 3 · 10 + 5. A lecke a jegyeket a „vizsgált szám”
     adatból veszi, az alaki és a valódi értéket, valamint a nulla nélküli számot kiszámolja és összeveti.
     Háromjegyű szám legyen, benne legalább egy 0-val (pl. 507, 480). A „helyi értéke a százas” az első
     jegyre mindig igaz. Ha a szám 5-tel kezdődik, a panelen „Az” névelő kell („Az 507 első jegyének…”). -->

## 4. Millió és milliárd
Legyen a kis kocka éle {kis kocka éle}! A nagy kocka éle {ezres kocka éle}. **Ezer** ilyen nagy kocka már **egymillió** kis kocka: egy {milliós kocka éle} élű kocka. Ezer ilyenből lesz az **egymilliárd**: ==egy {milliárdos kocka éle} élű kocka, magas, mint egy ház.==

> megjegyzés: Válts a gombokkal! Hol állnál te?

### Feliratok
- kérdés 4: Mekkora egy millió? És egy milliárd?
- ezerszer: ezerszer annyi
- él sablon: él: #
- te: te
- darab sablon: # kis kocka

### Adatok
- kis kocka éle: 1 cm
- ezres kocka éle: 10 cm
- milliós kocka éle: 1 m
- milliárdos kocka éle: 10 m
- gyerek magassága: kb. 1,5 m
<!-- 10 · 10 · 10 = 1000 kis kocka → 10 cm-es él; 1000 · 1000 = 1 000 000 → 100 cm = 1 m; 1000 · 1 000 000 =
     1 000 000 000 → 10 m. Ezerszer annyi kocka = tízszer hosszabb él (10 · 10 · 10 = 1000). A lecke az éleket a
     kis kocka éléből számolja és összeveti. A 10 m kb. egy háromemeletes ház magassága (egy szint kb. 3 m) –
     szemléltetés. A gyerek magassága kerekített, szemléltető érték (10–12 évesek: kb. 1,4–1,5 m). -->

## 5. Hármasával tagolunk
Ki tudod olvasni egyben? Nehéz! ==Jobbról hármasával tagolj!== Az első hármas az egyeseké, aztán jön az **ezer**, a **millió**, a **milliárd**. Minden hármast háromjegyű számként olvasol, utána mondod a nevét.

> megjegyzés: Az angol *billion* a magyar milliárd. A magyar **billió** ezer milliárd!

### Feliratok
- kérdés 5: Ki tudod olvasni ezt a számot?
- jobbról: jobbról hármasával!
- fény: ennyi métert tesz meg a fény 1 másodperc alatt
- föld nap: ennyi méter a Föld és a Nap távolsága
- év: ennyi másodperc egy év (365 nap)
- fény gomb: Fény
- föld nap gomb: Föld–Nap
- év gomb: Egy év
- olvasd: Így olvasd:

### Adatok
- fény útja 1 másodperc alatt: 299 792 458 m
- Föld–Nap távolság: 149 597 870 700 m
- napok egy évben: 365
- másodpercek egy napban: 86 400
- egy év másodpercben: 31 536 000
<!-- A fény sebessége vákuumban pontosan 299 792 458 m/s (az SI a métert ezzel definiálja, 1983 óta).
     A csillagászati egység pontosan 149 597 870 700 m (IAU 2012, B2 határozat) – ez a Föld és a Nap
     közepes távolsága; a valódi távolság az év során kb. 147,1 és 152,1 millió km között változik.
     Egy nap 24 · 60 · 60 = 86 400 s; 365 nap = 31 536 000 s (a lecke kiszámolja és összeveti; szökőév: 31 622 400 s).
     A magyar (hosszú skála) elnevezés: ezer = 10^3, millió = 10^6, milliárd = 10^9, billió = 10^12;
     az angol (rövid skála) „billion” = 10^9. -->

## 6. Kerekítés a számegyenesen
Mennyi a {kerekítendő szám} százasra kerekítve? ==Tippelj előbb!== A számegyenes megmutatja, melyik kerek szám van **közelebb**. Ha pont középen áll, felfelé kerekítünk. Lépésenként kerekíteni hiba: úgy {lépcsős kerekítés} jönne ki!

> megjegyzés: Húzd a pontot! Kerekíts tízesre és ezresre is!

### Feliratok
- kérdés 6: Mennyi a # százasra kerekítve?
- tipp szám: #
- tízesre: tízesre
- százasra: százasra
- ezresre: ezresre
- közelebb: ez van közelebb
- fele: a fele: #
- középen: pont középen: felfelé!
- lépcsős: lépésenként: # → # → #
- nem így: nem így!
- egyből: egyből: # ≈ #
- szám csúszka: a szám

### Adatok
- kerekítendő szám: 4449
- százasra kerekítve: 4400
- lépcsős kerekítés: 4500
<!-- kitalált példa. 4449 a 4400 és a 4500 között van; a fele 4450. 4449 − 4400 = 49 < 51 = 4500 − 4449, tehát
     4449 ≈ 4400. Lépésenként (tévesen): tízesre 4450, ebből százasra 4500. A lecke mindhármat kiszámolja és
     összeveti. A csúszka 1000 és 9999 között mozog (négyjegyű számok: a számegyenesen nincs ezres tagolás). -->

## 7. Római számok: a jel dönt, nem a hely
A rómaiak jeleket adtak össze: I = 1, V = 5, X = 10, **L** = 50, **C** = 100, **D** = 500, **M** = 1000. ==Az X mindig 10-et ér==, akárhol áll. A kisebb jel a nagyobb előtt kivonást jelent: XL = 40. Nulla nincs.

> megjegyzés: Melyik évszám a leghosszabb?

### Feliratok
- kérdés 7: Hogyan írták volna a rómaiak?
- római alak: MDCCCXLVIII
- jelek száma: # jel
- számjegyek száma: # számjegy
- évszám csúszka: évszám
- római sor: rómaiul: a jel dönt
- helyi sor: helyi értékkel: a hely dönt
- kivonás: kivonás

### Adatok
- évszám: 1848
<!-- 1848 = M (1000) + DCCC (800) + XL (40) + VIII (8) = MDCCCXLVIII. A lecke a „római alak” feliratot
     összeveti a saját átírásával. A csúszka 1–3999 (a hagyományos jelekkel írható tartomány).
     Az ókorban a kivonásos alak (IV, IX, XL…) nem volt egységes; a mai iskolai szabályt követjük:
     I csak V és X, X csak L és C, C csak D és M előtt állhat. -->

## 8. Kitekintés: a kettes számrendszer
Mi lenne, ha **kettesével** csoportosítanánk? Két egyforma érméből egy kétszer akkora lesz. Így a {kettes példa} kettes számrendszerben {kettes alak}. ==Itt a „10” kettőt jelent!== A számítógép is így tárol mindent.

> megjegyzés: Állítsd az alapot 3-ra vagy 10-re! Ugyanaz a gép.

### Feliratok
- kérdés 8: Mi lenne, ha kettesével csoportosítanánk?
- alap csúszka: csoportosítás (alap)
- plusz egy érme: +1 érme
- nullázd: Nullázd
- alap sablon: # számrendszerben
- váltás: # egyforma → 1 nagyobb
- a tíz: itt a „10” = #

### Adatok
- kettes példa: 13
- kettes alak: 1101
<!-- 13 = 1 · 8 + 1 · 4 + 0 · 2 + 1 · 1 → 1101. A lecke kiszámolja és összeveti. Az érmék értéke a kettes
     gépen 1, 2, 4, 8, 16…, a hármason 1, 3, 9, 27… (a kerettanterv „fabatka” játéka), a tízesen 1, 10, 100… -->

## 9. Összefoglalás
- **Helyi érték:** tízesével csoportosítunk; a jegy értékét a helye adja.
- A **0** helyet tart.
- Nagy számot jobbról **hármasával** tagolunk: ezer, millió, milliárd.
- **Kerekítés:** a közelebbi kerek szám; középről felfelé.
- ==A római szám nem helyi értékes.==

### Feliratok
- kérdés 9: Egy szám, sokféleképpen
- táblázat: helyiérték-táblázat
- kerekítve: kerekítve
- rómaiul: rómaiul
- kettesben: kettes számrendszerben
- összefoglaló csúszka: a szám

### Adatok
- összefoglaló szám: 2026

<!-- Tanári megjegyzések:
  - Kitalált példák: a pálcikák száma (347), a vizsgált szám (305), a kerekítendő szám (4449), a kettes példa (13).
    Valós adatok: a fény útja 1 s alatt és a csillagászati egység (definíció szerint pontos értékek, lásd az
    5. lépés megjegyzését), egy év másodpercben (számolt).
  - A helyiérték-táblázat oszlopneveit (egyes, tízes, százas, ezres) a tankönyvek rövidítve is írják (E, T, Sz,
    E); a lecke kiírja őket, mert az „E” kétszer szerepelne.
  - A 2. lépés kockái a Dienes-készlet (kocka, rúd, lap, nagy kocka) mintájára készültek.
  - Egyszerűsítés: a 4. lépés kockái csak szemléltetik a nagyságrendet (a milliós és a milliárdos kockát
    1000 nagyobb kockából rakjuk össze, a kis kockákat nem rajzoljuk ki egyenként).
  - Ezres tagolás 5 jegytől (4449, de 31 536 000), a magyar helyesírási szabályzat (AkH. 12., a számok írásáról szóló rész; review: pontszám) és a tankönyvek gyakorlata szerint.
  - A kerekítésnél a „pont középen: felfelé” az iskolai szabály (a 4450 százasra 4500).
  - A brief „tökéletes pénztárgépét” az 1. lépés (+1 szál, tíz szál → köteg) és a 8. lépés (alapcsúszka 2–10,
    a hármas a „fabatka”) valósítja meg; az írásbeli összeadás és a tizedek („apró fiókok”) kimaradt
    (a 08-tizedes-tortek lecke foglalkozik a tizedes helyi értékkel).
-->
