# Miért kék az ég? – a fény és a színek
tantárgy: Fizika · évfolyam: 7–8. · témakör: 8. Hullámok (+ 7. Világítás, fény, optikai eszközök)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/13-szinek.md

  Előzmény: 10-arnyek-tukor (hogyan látunk, visszaverődés), 11-lencse-szem (fénytörés).

  Modell és egyszerűsítések:
  - Prizma, esőcsepp: a sugarak útját a Snellius–Descartes-törvény adja, a törésmutató
    hullámhosszfüggése Cauchy-képlet (n = A + B/λ²), amelyet a lecke a lent megadott két
    értékből (vörös, ibolya) számol. Egyetlen vékony fénysugár; a visszavert részt nem rajzoljuk.
  - Prizma: F2 flintüveg (Schott-katalógus: n = 1,6126 @ 700 nm, 1,6522 @ 400 nm). Ablaküvegnél
    (koronaüveg, BK7: 1,513 / 1,531) a színes legyező kb. feleakkora.
  - Víz: n_C = 1,3312 (656 nm), n_F = 1,3371 (486 nm) 20 °C-on → Cauchy-képlettel 700 nm-en 1,330,
    400 nm-en 1,343. A szivárvány szöge a kilépési szög maximuma (Descartes): 42,5° (700 nm),
    40,6° (400 nm). Csak az elsődleges ív (egy belső visszaverődés).
  - Színek: a CIE 1931 színillesztő függvények analitikus közelítésével (Wyman–Sloan–Shirley, 2013)
    a lecke a spektrumból számolja a látott színt, a megvilágító fény fehérjéhez hangolva.
    A tárgyak, lámpák és festékek színképe kitalált, de jellegében valósághű (sima görbék).
  - Ég: csak a levegő molekuláin való Rayleigh-szórás (∝ 1/λ⁴), por és pára nélkül.
    A napfény a légkörön függőlegesen átmenve 550 nm-en kb. 9 %-ot veszít (Rayleigh-féle optikai
    mélység ≈ 0,097). A ferde út relatív hossza: Kasten–Young-képlet (a horizonton ≈ 38×).
    Az égbolt színátmenete szemléltető közelítés (egyszeres szórás, ózon nélkül), a számok
    (szórásarány, úthossz, a Nap átjutó fénye) pontosak.
  - Miért nem ibolya az ég? A napfényben kevesebb az ibolya, és a szemünk arra kevésbé érzékeny.
  - A felhő cseppjei sokkal nagyobbak a hullámhossznál: minden színt kb. egyformán szórnak → fehér.
-->

## Közös

### Feliratok
- húzd: húzd!
- vörös: vörös
- ibolya: ibolya
- kék: kék
- zöld: zöld
- sárga: sárga
- narancs: narancs
- cián: cián
- bíbor: bíbor
- fehér: fehér
- fekete: majdnem fekete
- fehér fény: fehér fény
- napfény: napfény
- szem: szem

### Adatok
- vörös hullámhossza: 700 nm
- ibolya hullámhossza: 400 nm
- kék hullámhossza: 450 nm

## 1. A prizma szétbontja a fehér fényt
A 11. leckében láttad: az üveg határán a fény **megtörik**. A prizmában a fehér fény ==színekre bomlik==!

Az ibolya jobban törik, mint a vörös: az üveg törésmutatója színenként kicsit más. Forgasd a fénysugarat!

> megjegyzés: Hol a legkisebb az irányváltozás? Keresd meg!

### Feliratok
- ernyő: ernyő
- prizma: prizma
- beesési merőleges: beesési merőleges
- törésmutató felirat: törésmutató:
- eltérülés felirat: irányváltozás:
- nagyítás nélkül: flintüveg, valódi szögek – nem nagyítva
- n grafikon: törésmutató – hullámhossz
- szög csúszka: A beesési szög

### Adatok
<!-- F2 flintüveg (Schott). Ablaküveg (BK7): 1,513 és 1,531. -->
- üveg törésmutatója vörösre: 1,613
- üveg törésmutatója ibolyára: 1,652
- kezdő beesési szög: 55°

## 2. Nem a prizma festi
**Tévhit:** a prizma „megfesti” a fényt. Newton egy résen át csak egy színt engedett tovább, egy második prizmára. Az ==megtörte, de a színét nem változtatta meg==.

A prizma tehát csak szétválogat. Minden színhez egy **hullámhossz** tartozik: a vörösé a leghosszabb, az ibolyáé a legrövidebb.

### Feliratok
- rés: rés
- második prizma: 2. prizma
- nem bomlik: ugyanaz a szín marad!
- hullámhossz felirat: hullámhossz:
- hullám: a hullám rajza nagyítva
- egy hullámhossz: 1 hullámhossz
- hullámhossz csúszka: A rés helye (hullámhossz)

### Adatok
<!-- A színtartományok határai kerekítve; a szakirodalomban pár nm-rel eltérnek. -->
- látható tartomány alja: 380 nm
- ibolya–kék határ: 450 nm
- kék–zöld határ: 495 nm
- zöld–sárga határ: 570 nm
- sárga–narancs határ: 590 nm
- narancs–vörös határ: 620 nm
- látható tartomány teteje: 750 nm
- kezdő hullámhossz: 530 nm

## 3. Szivárvány
Az esőcsepp is bont: a napfény belépéskor megtörik, a csepp hátfalán visszaverődik, kilépéskor újra megtörik. A fény ==zöme kb. 42°-ban jön ki==.

Vöröset azok a cseppek küldenek a szemedbe, amelyek a fejed árnyékától 42°-ra látszanak: ezek egy kört alkotnak. Az ibolya 40°-nál van, belül.

### Feliratok
- esőcsepp: esőcsepp
- szög tengely: kilépési szög
- hely tengely: hol éri a fény a cseppet?
- középen: közép
- szélén: szél
- legtöbb fény: itt a legtöbb fény
- fejed árnyéka: a fejed árnyéka: a kör közepe
- Nap mögötted: a Nap mögötted van, # magasan
- sugár csúszka: A sugár helye a cseppen

### Adatok
<!-- Víz 20 °C-on, a Fraunhofer C- és F-vonal mért törésmutatójából Cauchy-képlettel. -->
- víz törésmutatója vörösre: 1,330
- víz törésmutatója ibolyára: 1,343
- Nap magassága szivárványkor: 20°

## 4. A tárgy színe: visszavert fény
A 10. leckében láttad: azt látjuk, amiből fény jut a szemünkbe. A lámpa fehér fénye minden színt tartalmaz.

Az alma ==csak a vöröset veri vissza==, a többit elnyeli. A levél főleg a zöldet, a papír mindet.

**Tévhit:** a piros alma sötétben is piros. Kapcsold le a lámpát!

### Feliratok
- lámpa fénye: a lámpa fénye
- visszavert fény: visszavert fény
- alma: alma
- levél: levél
- papír: papír
- sötétben: sötétben nincs mit visszaverni
- lámpa gomb: Lámpa le / fel

### Adatok
- alma ennél hosszabbat ver vissza: 600 nm
- levél legjobban visszavert: 550 nm

## 5. Más fényben más szín
A tárgy nem „gyárt” színt: csak abból ver vissza, ami ráesik. Vörös fényben a levélnek ==nincs mit visszavernie==: majdnem feketének látszik. A fehér papír olyan színű, mint a fény.

Kapcsolgasd a lámpákat!

> megjegyzés: A levél klorofillja a vöröset és a kéket nyeli el.

### Feliratok
- vörös lámpa: Vörös lámpa
- zöld lámpa: Zöld lámpa
- kék lámpa: Kék lámpa

### Adatok
<!-- Színes LED-ek jellemző hullámhosszai -->
- vörös lámpa hullámhossza: 630 nm
- zöld lámpa hullámhossza: 530 nm
- kék lámpa hullámhossza: 460 nm

## 6. A fények összeadódnak
Színes fények keverésekor ==a fények összeadódnak==: vörös + zöld = sárga, mind a három együtt **fehér**.

**Tévhit:** minden szín együtt barna. A képernyőd is így kever, apró vörös, zöld és kék pontokból. Húzd a foltokat!

### Feliratok
- képernyő: a képernyőd közelről
- messziről: messziről nézve
<!-- A csapok érzékenységi görbéi a rajzon egyszerű haranggörbék (csúcs kb. 440, 535, 565 nm). -->
- csapok: a szem háromféle csapja
- kiegészítő: Kiegészítő színpárok
- pár vörös: vörös + cián
- pár zöld: zöld + bíbor
- pár kék: kék + sárga
- fény plusz fény: fény + fény = világosabb
- vörös csúszka: Vörös fény
- zöld csúszka: Zöld fény
- kék csúszka: Kék fény

## 7. A festékek elnyelnek
A festék nem fényt ad, hanem ==elnyel== a fehér fényből. A cián elnyeli a vöröset, a sárga a kéket: együtt csak a zöld marad.

Minél több festék, annál kevesebb fény: a három együtt majdnem fekete. Innen ered az előző tévhit!

### Feliratok
- festék elnyeli: Mit nyel el a festék?
- cián elnyeli: a cián a vöröset nyeli el
- bíbor elnyeli: a bíbor a zöldet nyeli el
- sárga elnyeli: a sárga a kéket nyeli el
- festék mínusz: festék + festék = sötétebb
- papír felirat: fehér papír fehér fényben
- cián csúszka: Cián festék
- bíbor csúszka: Bíbor festék
- sárga csúszka: Sárga festék

## 8. Miért kék az ég?
A levegő molekulái a napfényt minden irányba szórják, a rövid hullámhosszút sokkal jobban (∝ 1/λ⁴). A szórt kék fény ==az ég minden részéről== a szemedbe jut.

Lemenő Napnál a fény hosszú utat tesz meg a levegőben: a kék kiszóródik, a vörös marad.

**Tévhit:** az ég a tengert tükrözi.

### Feliratok
- szórás cím: Mennyire szórja a levegő?
- arány felirat: kék : vörös szórása ≈ # : 1
- eljut: ami a Napból egyenesen eljut
- út felirat: a napfény útja a levegőben
- Nap fent: Nap a fejed fölött
- Nap most: most: #
- nem méretarányos: nem méretarányos
- felhő: felhő: minden színt egyformán szór
- tenger tükröz: a tenger tükrözi az eget!
- sivatag kék: sivatag fölött is kék az ég!
- nap csúszka: A Nap magassága
- talaj gomb: Tenger / sivatag
- levegő: levegő
- Föld: Föld
- te: te

### Adatok
<!-- Rayleigh-féle optikai mélység 550 nm-en, tengerszinten ≈ 0,097 → e^(−0,097) ≈ 0,908, azaz kb. 9 % szóródik ki. -->
- szórt hányad függőlegesen: 9,2 %
- kezdő napmagasság: 45°

## 9. Összefoglalás
- A fehér fény **színek keveréke**; a prizma szétválogatja, nem festi.
- Az ibolya jobban törik, mint a vörös: ebből lesz a **szivárvány** is.
- A tárgy színe a ==visszavert fény== színe – más fényben más.
- A fények összeadódnak (fehér), a festékek elnyelnek (fekete).
- Az ég kék, mert a levegő a kéket jobban **szórja**.

### Feliratok
- össz prizma: a fehér fény színekre bomlik
- össz newton: egy szín: nem bomlik tovább
- össz szivárvány: szivárvány: 42° és 40°
- össz tárgy: a tárgy színe: visszavert fény
- össz fény: fény: összead · festék: elnyel
- össz ég: kék ég, vörös naplemente
