# Hány tyúk és hány nyúl? – egyenletek, egyenlőtlenségek, egyenletrendszerek
tantárgy: Matematika · évfolyam: 9–10. · témakör: 8. Elsőfokú egyenletek, egyenlőtlenségek, egyenletrendszerek

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/06-egyenletrendszer.md
  Képlet a szövegben `…` között (* → ·, - → −, <= → ≤, != → ≠).
  A vásznon megjelenő levezetéseket (mérleg, taxi, metszéspont) a lecke számolja ki az Adatokból.
  A panelszöveg képleteiben a számok szó szerint állnak: ha egy adatot átírsz (pl. a fejek vagy a lábak
  számát), a hozzá tartozó panelszöveget is írd át. Az „eredmény” jellegű adatokat (mérleg megoldása,
  egyenlőtlenség határa, kiegyenlítés, tyúkok, nyulak) a lecke kiszámolja, és eltérésnél piros hibasávot mutat.
  A feliratokban a # jel helyére a lecke számot ír.
-->

## Közös

### Feliratok
- bizonyítás: bizonyítás
- mérés: mérés
- kitalált adat: kitalált adat
- ellenőrzés: Ellenőrzés:
- fejek: fejek
- lábak: lábak
- tyúk tengely: x (tyúk)
- nyúl tengely: y (nyúl)

### Adatok
- fejek száma: 35
- lábak száma: 94

## 1. A mérleg: mindkét oldalon ugyanazt
A mérleg egyensúlyban van: `3x + 5 = x + 13`. Vegyünk le **mindkét** tányérról egy dobozt, aztán öt golyót, végül osszuk két egyenlő részre. ==Ha mindkét oldallal ugyanazt tesszük, az egyensúly megmarad==: `x = 4`.

> megjegyzés: Vegyél le csak az egyik oldalról: billen!

### Feliratok
- doboz jelentése: = ismeretlen súly
- golyó jelentése: = 1 egység
- lépések cím: Mérlegelv, lépésenként
- csak bal: csak bal oldalon!
- billen: Billen! Ez már nem egyenlőség.
- egy doboz: 1 doboz ugyanannyi, mint 4 golyó
- billen tipp: A mérleg billen – kezdd újra!
- kész tipp: Kész: egy dobozt kaptunk meg.
- osztás tipp: Osztani akkor lehet, ha az egyik oldalon csak doboz van.
- üres tipp: Ebből már nincs mindkét oldalon.
- doboz gomb: −1 doboz mindkét oldalról
- golyó gomb: −1 golyó mindkét oldalról
- oszt gomb: Oszd egyenlő részekre
- csak bal gomb: −1 golyó csak balról
- újra gomb: Újra, magad!

### Adatok
- mérleg egyenlet: 3x + 5 = x + 13
- mérleg megoldás: 4

## 2. Egyenlőtlenség: mikor fordul a jel?
`2 < 3`. Szorozzuk mindkét oldalt mínusz eggyel! Ez a számegyenest a nullára tükrözi, ezért a két pont helyet cserél: `−2 > −3`. ==Negatív számmal szorozva vagy osztva a reláció megfordul.== Így `−2x < 6`-ból nem `x < −3`, hanem `x > −3` lesz.

> megjegyzés: Húzd a szorzót! Pozitív számnál a jel marad, negatívnál fordul.

### Feliratok
- fordul: a jel megfordul!
- marad: a jel marad
- nulla: mindkettő 0
- biz cím: Miért fordul meg?
- biz magyarázat: mindkét oldalból ugyanazt vontuk ki: ez is mérlegelv
- tévhit 2: Gyakori hiba:
- rossz: rossz
- jó: jó
- megoldáshalmaz: megoldáshalmaz
- rossz irány: a rossz irány
- szorzó csúszka: szorzó (k)

### Adatok
- pontpár: 2; 3
- hibás egyenlőtlenség: −2x < 6
- egyenlőtlenség határa: −3
- próbapontok: 0; −4

## 3. Két taxi: melyik éri meg?
Az A taxi {A alapdíj}-tal indul, és {A km-díj}; a B {B alapdíj}-tal, de csak {B km-díj}. Mindkét ár egy egyenes. ==Ahol metszik egymást, ott egyenlő az ár==: {kiegyenlítés távolsága}-nél {kiegyenlítés ára}. A leolvasott értéket **behelyettesítéssel ellenőrizzük** – így a grafikus megoldás is pontos. Hosszabb úton a B olcsóbb.

> megjegyzés: Húzd a csúszkát: melyik taxi olcsóbb 3 km-en? És 9 km-en?

### Feliratok
- A taxi: A taxi
- B taxi: B taxi
- A olcsóbb: A olcsóbb
- B olcsóbb: B olcsóbb
- egyforma: egyforma
- számolás cím: Számolással: mikor egyenlő?
- útnál: útnál
- út tengely: út (km)
- ár tengely: ár (Ft)
- út csúszka: út (km)

### Adatok
<!-- kitalált példa: a tarifák nem valódi taxitársaságok árai -->
- A alapdíj: 700 Ft
- A km-díj: 400 Ft/km
- B alapdíj: 1000 Ft
- B km-díj: 350 Ft/km
- kiegyenlítés távolsága: 6 km
- kiegyenlítés ára: 3100 Ft

## 4. Tyúkok és nyulak: két egyenlet
Egy udvaron tyúkok és nyulak vannak: összesen 35 fej és 94 láb. Hány tyúk és hány nyúl? Legyen *x* a tyúkok, *y* a nyulak száma. ==Két feltétel, két egyenlet==: `x + y = 35` (fejek) és `2x + 4y = 94` (lábak). Próbálgass: minden nyúl két lábbal többet ad!

> megjegyzés: Ősi feladat: egy kínai számtankönyvben már szerepel, legalább 1500 éve.

### Feliratok
- feladat: 35 fej, 94 láb. Hány tyúk, hány nyúl?
- forrás 4: Kínai feladat, Sunzi suanjing (kb. 3–5. század)
- jelölés cím: Jelöljük:
- tyúk: a tyúkok száma
- nyúl: a nyulak száma
- próbálgatás: Próbálgatás:
- fej: fej
- láb: láb
- pont annyi: pont 94 láb!
- hiányzik láb: még # láb hiányzik
- sok láb: # lábbal több
- nyúl ad: Ha egy tyúk helyére nyúl kerül, a fejek száma marad, a lábaké 2-vel nő.
- nyúl csúszka: nyulak száma (y)

### Adatok
- nyulak: 12
<!-- Sunzi suanjing (孫子算經), 3. kötet, 31. feladat: „雉兔同籠” – fácánok és nyulak egy ketrecben, 35 fej,
     94 láb; megoldás 23 fácán, 12 nyúl. A keletkezés ideje bizonytalan (kb. Kr. u. 3–5. század). A leckében a
     fácán helyett tyúk áll (a hazai tankönyvi hagyomány). Ellenőrizendő: Wikipédia „Sunzi Suanjing” és
     „Chickens and rabbits problem”, MacTutor „Sun Zi”. A „legalább 1500 éve” a legkésőbbi (5. századi) keltezéssel is igaz. -->

## 5. Egy egyenlet = egy egyenes
Az `x + y = 35` egyenletnek sok megoldása van: `(0; 35)`, `(1; 34)`, … `(35; 0)`. Ábrázolva ==a megoldások egy egyenesen vannak==, és az egyenes minden pontja megoldás. Az udvarhoz csak a nemnegatív egész pontok illenek. A fejek száma mindenhol 35, a lábaké nem!

> megjegyzés: Húzd a pontot az egyenesen, és figyeld a lábak számát.

### Feliratok
- megoldások cím: A pont koordinátái:
- lábak most: és a lábak száma:
- egyenes: Minden ilyen pont egy egyenesen van.
- tyúk csúszka: tyúkok száma (x)

## 6. A metszéspont a megoldás
A lábak egyenlete is egy egyenes. ==A két egyenes metszéspontja mindkét egyenletet kielégíti==: `M(23; 12)`. Számolva: a fejek egyenletét 2-vel szorozzuk, `2x + 2y = 70`, és ezt a lábakéból kivonjuk: `2y = 24`, tehát `y = 12`, `x = 23`. Ez az **egyenlő együtthatók** módszere.

> megjegyzés: Behelyettesítéssel is megy: `y = 35 − x` a második egyenletbe.

### Feliratok
- módszer cím: Egyenlő együtthatók módszere
- kivonva: kivonva
- mindkettő igaz: mindkét egyenlet igaz
- csak az egyik: csak a fejek stimmelnek
- húzd a pontot: Húzd a pontot a metszéspontba!
- tyúk csúszka 6: tyúkok száma (x)

### Adatok
- tyúkok: 23

## 7. Fél nyúl? Ellenőrzés
95 lábnál a metszéspont `(22,5; 12,5)` – fél nyúl nincs! 150 lábnál `x = −5`: negatív tyúk sincs. ==Az egyenletrendszernek van megoldása, a feladatnak mégsincs.== Ezért a kapott számokat mindig visszahelyettesítjük a szövegbe, és megnézzük: egész-e, nemnegatív-e?

> megjegyzés: Húzd a lábak számát! Melyik lábszámnál jó a megoldás?

### Feliratok
- értelmes: itt értelmes
- egész: egész szám?
- nemnegatív: nemnegatív?
- jó megoldás: jó megoldás
- fél nyúl: fél állat – nincs ilyen udvar
- negatív tyúk: negatív tyúk – nincs ilyen udvar
- negatív nyúl: negatív nyúl – nincs ilyen udvar
- van megoldás: Az egyenletrendszernek van megoldása, a feladatnak nincs.
- láb csúszka: lábak száma

### Adatok
- fél nyúl lábszám: 95
- negatív tyúk lábszám: 150

## 8. Párhuzamos és egybeeső egyenesek
Ha minden állat kétlábú: `2x + 2y = 94`, azaz `x + y = 47`. Ez párhuzamos a fejekével: ==nincs metszéspont, nincs megoldás==. 70 lábnál a két egyenes egybeesik: végtelen sok megoldás, a második adat nem mond újat.

> megjegyzés: Kapcsold vissza a nyulakat!

### Feliratok
- kétlábú cím: Minden állat kétlábú
- négylábú cím: Tyúkok és nyulak
- ugyanaz: ugyanaz az egyenlet!
- ellentmondás: ellentmondás
- egy megoldás: egy megoldás
- nincs megoldás: nincs megoldás
- végtelen sok: végtelen sok megoldás
- egyértelmű: Két metsző egyenes: pontosan egy közös pont.
- ellentmondó: Ellentmondó adatok: a két feltétel nem teljesülhet egyszerre.
- hiányos: Hiányos adat: a második egyenlet nem mond újat.
- három eset: Két egyenes – három eset
- metsző: metsző
- párhuzamos: párhuzamos
- egybeeső: egybeeső
- kétlábú gomb: Minden állat kétlábú
- négylábú gomb: Nyulak vissza
- láb csúszka 8: lábak száma

## 9. Összefoglalás
**Mérlegelv:** mindkét oldallal ugyanazt tesszük. **Egyenlőtlenség:** negatív számmal szorozva vagy osztva megfordul a jel. **Egyenletrendszer:** két egyenes – ==a megoldás a metszéspont==; egy, egy sem vagy végtelen sok lehet. A végén **ellenőrizz** a szövegben: értelmes-e a válasz?

### Feliratok
- össz 1 cím: Mérlegelv
- össz 1: mindkét oldallal ugyanazt
- össz 2 cím: Egyenlőtlenség
- össz 2: Negatív számmal szorozva vagy osztva a reláció megfordul.
- össz 3 cím: Egyenletrendszer
- össz 3: A megoldás a két egyenes metszéspontja: egy, egy sem vagy végtelen sok.
- össz 4 cím: Ellenőrizz!
- össz 4: Fél nyúl nincs: helyettesíts vissza a szövegbe!

<!-- Matematikai ellenőrzés (2026-11-24, kézzel + Pythonnal + a lecke L.checks() kampója):
     Mérleg: 3x + 5 = x + 13 | −x → 2x + 5 = 13 | −5 → 2x = 8 | :2 → x = 4; ellenőrzés 3 · 4 + 5 = 17 = 4 + 13.
       A súlyok (x = 4): bal 3 · 4 + 5 = 17, jobb 4 + 13 = 17; minden mérlegelv-lépés után egyenlő (2 · 4 + 5 = 13, 8 = 8).
     Egyenlőtlenség: 2 < 3 → (−1)-gyel szorozva −2 > −3. Bizonyítás: a < b | −a − b → −b < −a.
       −2x < 6 | :(−2) → x > −3; próba: x = 0 → 0 < 6 igaz; x = −4 → 8 < 6 hamis (az „x < −3” rossz irány).
     Taxi (kitalált adat): 700 + 400x = 1000 + 350x → 50x = 300 → x = 6; 700 + 2400 = 3100 = 1000 + 2100.
       3 km: A 1900 Ft, B 2050 Ft (A olcsóbb); 9 km: A 4300 Ft, B 4150 Ft (B olcsóbb).
     Tyúk–nyúl: x + y = 35, 2x + 4y = 94 → (·2 és kivonás) 2y = 24 → y = 12, x = 23; 23 + 12 = 35, 46 + 48 = 94.
       Sunzi módszere (érdekesség): 94 : 2 = 47, 47 − 35 = 12 nyúl.
       Általánosan L lábnál: y = (L − 70)/2, x = 35 − y = (140 − L)/2. 95 láb: (22,5; 12,5); 150 láb: (−5; 40);
       60 láb: (40; −5); 70 láb: (35; 0) – minden tyúk; 140 láb: (0; 35) – minden nyúl. Értelmes megoldás pontosan
       a páros L-re, 70 ≤ L ≤ 140 között.
     Kétlábú: 2x + 2y = 94 ⇔ x + y = 47 ∥ x + y = 35 (nincs megoldás); 2x + 2y = 70 ⇔ x + y = 35 (egybeesik).
     A lecke a vásznon minden levezetést az Adatokból számol; az eredményadatokat ellenőrzi (eltérésnél piros hibasáv). -->
