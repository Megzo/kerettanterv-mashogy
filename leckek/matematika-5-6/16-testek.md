# Melyik hálóból lesz kocka? – testek, háló, felszín, térfogat
tantárgy: Matematika · évfolyam: 5–6. · témakör: 16. Térgeometria (+ 13. Mérés és mértékegységek)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/16-testek.md
  Feliratban a # jel helyére a lecke számot ír (pl. „az építmény: # kocka” → „az építmény: 7 kocka”).
  Az eredményeket (csúcsok, élek, lapok, átlók száma, a kockahálók száma, felszín, térfogat) a lecke
  kiszámolja a rajzolt testből, és piros sávval jelez, ha a .md-ben írt érték nem egyezik a számolásával.
-->

## Közös

### Feliratok
- tippelj: Tippelj előbb!
- a tipped: a te tipped
- jó tipp: jó tipp!
- rossz tipp: nem talált
- forgasd: Forgasd egérrel!
- csúcs: csúcs
- él: él
- lap: lap
- a csúszka: a (hosszúság)
- b csúszka: b (szélesség)
- c csúszka: c (magasság)
- felszín: felszín
- térfogat: térfogat

## 1. Csúcsok, élek, lapok, átlók
==Tippelj előbb!== Hány éle van a kockának? Aztán megszámoljuk. Két lap egy **élben**, három él egy **csúcsban** találkozik. A **lapátló** egy lap két szemközti csúcsát köti össze, a **testátló** két csúcsot a test belsején át.

> megjegyzés: Forgasd egérrel! A takart élek szaggatottak.

### Feliratok
- kérdés 1: Hány éle van a kockának?
- tipp 6: 6 él
- tipp 8: 8 él
- tipp 12: 12 él
- lapátló: lapátló
- testátló: testátló
- takart él: takart él

### Adatok
- csúcsok száma: 8
- élek száma: 12
- lapok száma: 6
- lapátlók száma: 12
- testátlók száma: 4
<!-- Laponként 2 lapátló: 6 · 2 = 12. Testátló: két olyan csúcs között, amelyek nincsenek egy lapon: 4.
     Mind az öt számot a lecke a rajzolt kockából számolja, és összeveti. -->

## 2. Nézetek: elölről, felülről, oldalról
Ugyanaz az építmény elölről, felülről és oldalról: ezek a **nézetek**. ==Egy nézetből nem derül ki, hány kocka van.== Ha a felülnézet mezőibe beírjuk, hány kocka áll egymáson, megkapjuk az **alaprajzot**: ebből újraépíthető az egész.

> megjegyzés: Nyomd meg a gombokat, vagy forgasd egérrel!

### Feliratok
- nézetek cím: Nézd meg több oldalról!
- elölnézet: elölnézet
- felülnézet: felülnézet
- oldalnézet: oldalnézet (jobbról)
- alaprajz: alaprajz
- gomb elölről: elölről
- gomb felülről: felülről
- gomb jobbról: jobbról
- gomb térben: térben
- építmény: az építmény: # kocka

### Adatok
- építmény kockái: 7
<!-- Az építmény alakja a kódban van (3 + 2 kocka a földön, a hátsó bal sarokban 3 magas torony).
     Az elölnézet és a felülnézet is 5 négyzet, az oldalnézet 4 – egyikből sem olvasható ki a 7. -->

## 3. Kiterítjük: a háló
Vágd fel a kockát néhány éle mentén, és hajtsd szét a lapjait! A síkba kiterített felület a **háló**. ==A háló lapjai pontosan a test lapjai.== Az egyenes **hasáb** két egybevágó alaplapját téglalapok kötik össze, a **gúla** oldallapjai háromszögek.

### Feliratok
- háló kocka: A kocka hálója
- háló téglatest: A téglatest hálója
- háló hasáb: A háromszög alapú hasáb hálója
- háló gúla: A négyzet alapú gúla hálója
- gomb kocka: kocka
- gomb téglatest: téglatest
- gomb hasáb: hasáb
- gomb gúla: gúla
- lapok kocka: 6 egybevágó négyzet
- lapok téglatest: 6 téglalap, páronként egyformák
- lapok hasáb: 2 háromszög és 3 téglalap
- lapok gúla: 1 négyzet és 4 háromszög
- összehajtás: összehajtás

## 4. Melyikből lesz kocka?
==Tippelj előbb!== Válassz egy hat négyzetből álló alakzatot: kocka lesz belőle? Aztán hajtsd össze! Nem mindegyik háló: két lap ütközhet, és egy hely üres marad. A {hexominók száma} ilyen alakzatból csak **{kockahálók száma}** kockaháló.

### Feliratok
- kérdés 4: Kocka lesz belőle?
- válassz: Kattints egy alakzatra!
- gomb lesz: Kocka lesz!
- gomb nem lesz: Nem lesz kocka
- gomb következő: következő alakzat
- kocka lett: Kocka lett!
- nem lett: Nem lett kocka
- ütközik: két lap ugyanoda kerül
- nyitva: egy lap helye üres

### Adatok
- hexominók száma: 35
- kockahálók száma: 11
<!-- A 35 a hat egybevágó négyzetből álló, egymástól (forgatás és tükrözés után is) különböző alakzatok száma.
     A lecke mind a 35-öt előállítja és gépben „összehajtja”: pontosan 11-ből lesz kocka. Mindkét számot összeveti. -->

## 5. Felszín: a háló területe
A test **felszíne** a lapjai területének összege, vagyis a háló területe. A téglatest szemközti lapjai egyformák:

képlet: A = 2 · (ab + ac + bc)

==A {téglatest a}, {téglatest b} és {téglatest c} élű téglatest felszíne {téglatest felszíne}.==

### Feliratok
- felszín cím: Mennyi papír kell a dobozhoz?
- háló területe: a háló területe

### Adatok
- téglatest a: 3 cm
- téglatest b: 4 cm
- téglatest c: 5 cm
- téglatest felszíne: 94 cm²
<!-- 2 · (3 · 4 + 3 · 5 + 4 · 5) = 2 · (12 + 15 + 20) = 2 · 47 = 94 cm². Az élek egész centiméterek (1–5 cm),
     mert a háló rácsán 1 négyzet = 1 cm². A felszínt a lecke kiszámolja és összeveti. -->

## 6. Megtöltjük: térfogat
Hány 1 cm élű kis kocka fér a dobozba? Egy rétegben a · b, és c réteg van:

képlet: V = a · b · c

A **térfogat** azt mutatja, hány **egységkocka** fér bele: most {téglatest térfogata}. ==A felszín és a térfogat nem ugyanaz: cm² és cm³!==

### Feliratok
- térfogat cím: Hány kis kocka fér a dobozba?
- egy réteg: egy réteg: # · # = # kocka
- rétegek: # réteg: # · # = # kocka
- egységkocka: = 1 cm³ (1 cm élű kocka)
- kockák: # kocka
- nem ugyanaz: más mennyiség, más mértékegység

### Adatok
- téglatest térfogata: 60 cm³
<!-- 3 · 4 · 5 = 60 cm³ (ugyanaz a téglatest, mint az 5. lépésben). A lecke kiszámolja és összeveti. -->

## 7. 1 liter = 1 dm³
„Nem hiszem!” játék: belefér-e {tej} tej egy {kocka éle} élű kocka alakú edénybe? {kocka éle} = 10 cm, ezért az edénybe 10 · 10 · 10 kis kocka fér. ==1 dm³ = 1000 cm³ = 1 liter.==

> megjegyzés: Öntsd bele a tejet!

### Feliratok
- állítás cím: „Nem hiszem!”
- állítás 1: „# liter tej belefér
- állítás 2: egy # dm élű kockába?”
- öntés gomb: Öntsük bele!
- beöntve: beöntve: # l
- kifolyt: kifolyt: # l
- nem fér: Nem fér bele!
- belefér: Belefér!
- réteg 1: 1 réteg: # · # = # cm³
- réteg 10: # réteg: # · # = # cm³
- liter egyenlőség: 1 dm³ = 1000 cm³ = 1 liter
- él felirat: # dm = # cm

### Adatok
- kocka éle: 1 dm
- edény térfogata: 1000 cm³
- tej: 2 l
- kifolyó tej: 1 l
<!-- (10 cm)³ = 1000 cm³ = 1 dm³ = 1 l. A kerettanterv „Nem hiszem” játékának példája (4. témakör):
     „két liter tej belefér egy 1 dm élű kocka alakú edénybe” – hamis, 1 liter kifolyik.
     Az edény térfogatát és a kifolyó mennyiséget a lecke kiszámolja és összeveti. -->

## 8. Kétszer akkora kocka
==Tippelj előbb!== Ha a kocka éle kétszeres, hányszoros a térfogata? Rakjuk ki a nagy kockát kicsikből: hosszában, széltében és magasságban is kétszer annyi fér el. ==A felszín és a térfogat nem kétszeres lesz!==

> megjegyzés: Tipp után a csúszkával 3- és 4-szeres élt is kipróbálhatsz.

### Feliratok
- kérdés 8: Kétszeres él – hányszoros térfogat?
- tipp 2x: 2-szeres
- tipp 4x: 4-szeres
- tipp 8x: 8-szoros
- nagyítás: hányszoros az él?
- kis kocka: kis kocka
- nagy kocka: nagy kocka

### Adatok
- kis kocka éle: 2 cm
- kis felszín: 24 cm²
- kis térfogat: 8 cm³
- nagy felszín: 96 cm²
- nagy térfogat: 64 cm³
- felszín szorzó: 4
- térfogat szorzó: 8
<!-- 2 cm élű kocka: A = 6 · 2 · 2 = 24 cm², V = 2 · 2 · 2 = 8 cm³. 4 cm élű: A = 6 · 4 · 4 = 96 cm² (4-szeres),
     V = 4 · 4 · 4 = 64 cm³ (8-szoros). A lecke mindet kiszámolja és összeveti. -->

## 9. Összefoglalás
- A kockának {csúcsok száma} csúcsa, {élek száma} éle, {lapok száma} lapja van.
- **Háló:** a kiterített felület – a kockának {kockahálók száma} hálója van.
- **Felszín:** a háló területe (cm²).
- **Térfogat:** hány egységkocka fér bele (cm³). ==1 dm³ = 1 liter.==
- Kétszeres él: {felszín szorzó}-szeres felszín, {térfogat szorzó}-szoros térfogat.

### Feliratok
- össz kocka: kocka
- össz háló: háló
- össz felszín: felszín
- össz térfogat: térfogat
- össz liter: 1 liter
- össz kétszeres: kétszeres él
- össz hálók: # különböző kockaháló
- össz felszín sor: a háló területe
- össz térfogat sor: hány kis kocka fér bele
- össz szorzók: felszín #-szeres, térfogat #-szoros

<!-- Tanári megjegyzések:
  - A testek rajza ortografikus (párhuzamos) vetítés: a párhuzamos élek a rajzon is párhuzamosak,
    mint a füzetben rajzolt testeknél. A takart élek szaggatottak.
  - Az „alaprajz” itt a felülnézet, a mezőkben a rájuk épített kockák számával (tankönyvenként
    a „felülnézet” és az „alaprajz” szóhasználata eltérhet). Az oldalnézet jobbról nézett.
  - A 4. lépés tíz alakzata: hat kockaháló (kereszt, „lépcső”, 3 + 3, 2 + 3 + 1 és két 1 + 4 + 1)
    és négy nem-háló (hat egy sorban, 2 · 3-as téglalap, 5 + 1 és a 4 + 2 „fésű”). A „Kocka lett/nem lett”
    ítéletet a lecke a hajtogatás eredményéből számolja, nem táblázatból.
  - Az 5–6. lépés csúszkái 1–5 cm-ig mennek (a brief 1–6-ot írt): 5 cm-nél a háló 20 rácsnégyzet magas,
    és így fér el 1 cm = 1 füzetkocka méretben.
  - A 8. lépés a szorzószót (-szeres/-szoros) a számhoz illesztve írja: 2-szeres, 4-szeres, 8-szoros,
    9-szeres, 16-szoros, 27-szeres, 64-szeres.
  - Tej helyett víz is lehet: 1 liter víz tömege kb. 1 kg (ez nincs a leckében).
-->
