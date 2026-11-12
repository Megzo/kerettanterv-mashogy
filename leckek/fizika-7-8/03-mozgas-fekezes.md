# Miért kell bekötni az övet? – sebesség, tehetetlenség, fékezés
tantárgy: Fizika · évfolyam: 7–8. · témakör: 3. Mozgások

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/03-mozgas-fekezes.md

  A modell egyszerűsítései (a panel is kimondja):
  - a sebesség szakaszonként állandó, a gyorsítást/lassítást a 2. lépésben nem számoljuk;
  - fékezéskor egyenletes lassulással számolunk; a fékrendszer felfutási idejét
    (kb. 0,2 s) a reakcióidőbe értjük; légellenállás nincs;
  - ütközésnél egyenletes lassulással, becsült megállási utakkal számolunk (átlagos erő).

  Források, tájékoztató értékek (kerekítve):
  - reakcióidő: figyelő sofőrnél kb. 0,7–1,5 s, a KRESZ-oktatásban 1 s a szokásos érték;
    telefonálás / üzenetírás közben ennél jóval több (a 2 s becslés, lehet több is);
  - lassulás: száraz aszfalton 7–8 m/s², vizesen kb. 5 m/s², jégen kb. 1 m/s²
    (gépjárművezető-képzési tananyagok, a fékút = v² / (2 · a) szokásos számpéldái);
  - önvezető / vészfékező rendszer késése: tizedmásodperces nagyságrend – becslés,
    típusonként eltér;
  - súrlódási együtthatók (fahasáb): becsült, tájékoztató értékek;
  - ütközés: gyűrődési zóna kb. 0,5 m, az öv + légzsák további kb. 0,2 m-t enged
    előre; öv nélkül a test a kormányon / műszerfalon néhány cm alatt áll meg – becslés.
  - 50 km/h-s ütközés ≈ 9,8 m-es zuhanás (h = v² / (2 · g)).
-->

## Közös

### Feliratok
- száraz gomb: száraz aszfalt
- vizes gomb: vizes aszfalt
- jeges gomb: jeges út
- sebesség csúszka: Sebesség
- reakcióidő csúszka: Reakcióidő
- gyorsítva: gyorsítva
- lassítva: lassítva
- valós idő: valós idő
- reakcióút: reakcióút
- fékút: fékút
- megállási út: megállási út
- idő tengely: idő (s)
- út tengely: út (m)
- sebesség tengely: sebesség (km/h)
- zebra: zebra
- megállt: megállt
- lassulás: lassulás
- mozgási energia: mozgási energia
- belső energia: belső energia
- zebránál még: a zebránál még
- megáll előtte: megáll a zebra előtt

### Adatok
- városi sebesség: 50 km/h
- reakcióidő: 1,0 s
- lassulás száraz úton: 7 m/s²
- lassulás vizes úton: 5 m/s²
- lassulás jeges úton: 1 m/s²
- autó tömege: 1300 kg
- nehézségi gyorsulás: 9,81 m/s²
- zebra távolsága: 30 m

## 1. Út és elmozdulás
Reggel autóval mész iskolába. A kocsi az utcákon kanyarog: a **megtett út** a teljes útvonal hossza.

Az **elmozdulás** csak azt mutatja meg, ==honnan hová jutottál==: légvonalban, iránnyal együtt.

> megjegyzés: Nyomd meg a „Vissza haza!” gombot! Mennyi lesz a megtett út, és mennyi az elmozdulás?

### Feliratok
- otthon: otthon
- iskola: iskola
- megtett út: megtett út
- elmozdulás: elmozdulás
- az utcákon: az utcákon mérve
- légvonalban: légvonalban
- vissza gomb: Vissza haza!
- elmozdulás nulla: elmozdulás = 0
- park: park

### Adatok
- első szakasz hossza: 1,2 km
- második szakasz hossza: 0,9 km

## 2. Átlagsebesség
Az első szakaszon {első szakasz sebessége}, a másodikon {második szakasz sebessége} a sebesség. Akkor az átlag a kettő átlaga? **Nem!**

képlet: átlagsebesség = összes út / összes idő

A lassú szakaszon több időt töltesz, és a piros lámpánál is telik az idő: ==a megállás is számít==.

> megjegyzés: Egyszerűsítés: szakaszonként állandó sebesség.

### Feliratok
- lámpa csúszka: Várakozás a piros lámpánál
- piros lámpa: piros lámpa
- áll: áll
- út tengely km: út (km)
- sebességek átlaga: a két sebesség átlaga
- átlagsebesség: átlagsebesség
- összes út per idő: összes út / összes idő
- eltelt idő: eltelt idő
- eddig: eddig
- nem átlagsebesség: ≠ átlagsebesség
- átváltás: 1 m/s = 3,6 km/h

### Adatok
- első szakasz sebessége: 30 km/h
- második szakasz sebessége: 50 km/h
- várakozás a lámpánál: 60 s
- időgyorsítás: 40

## 3. Kell erő a mozgáshoz?
Sokan gondolják: ==ami mozog, azt valaminek tolnia kell==. Lökd meg a hasábot! Elengedés után csak a **súrlódás** hat rá, és az lassítja.

Kisebb súrlódással tovább csúszik. Súrlódás nélkül ==örökké egyenletesen haladna==: ez a **tehetetlenség**.

> megjegyzés: Newton I. törvénye: erő nélkül a test megtartja a mozgásállapotát.

### Feliratok
- tévhit erő: A mozgáshoz erő kell?
- igazság erő: Erő a mozgás megváltoztatásához kell!
- szőnyeg gomb: szőnyeg
- parketta gomb: parketta
- jég gomb: jég
- súrlódásmentes gomb: súrlódás nélkül
- kezed tolja: a kezed tolja
- súrlódási erő: súrlódási erő
- nincs erő: nincs erő – egyenletesen halad
- csúszás: csúszás
- sebesség tengely ms: sebesség (m/s)

### Adatok
- hasáb kezdősebessége: 3 m/s
- súrlódás szőnyegen: 0,4
- súrlódás parkettán: 0,25
- súrlódás jégen: 0,05

## 4. Mi állítja meg az autót?
Fékezéskor az **út súrlódási ereje** hátrafelé hat a kerekekre, és lassítja az autót.

képlet: a = F / m

Jégen az út csak kis erővel tud fékezni, ezért ==sokkal tovább tart a megállás==.

> megjegyzés: Közben a mozgási energia belső energiává alakul: a fék felmelegszik.

### Feliratok
- fékerő: az út fékező ereje
- fékidő: fékidő
- fék melegszik: a fék, a gumi, az út melegszik
- tömeg: tömeg
- erő: fékezőerő

## 5. Reakcióút + fékút
Amíg észreveszed a veszélyt és fékre lépsz, az autó **teljes sebességgel** halad: ez a ==reakcióút==. Utána jön a **fékút**.

képlet: s = v · t_r + v² / (2 · a)

> megjegyzés: Próbáld ki 60 km/h-val! (Egyenletes lassulással számolunk.)

### Feliratok
- terület: terület = megtett út

## 6. Kétszer gyorsabb – négyszer hosszabb fékút
Két autó ugyanott kezd fékezni, az egyik kétszer olyan gyors. A fékútja ==négyszer olyan hosszú==!

Miért? A mozgási energia (½ · m · v²) a sebesség **négyzetével** nő. A fékezőerő méterenként ugyanannyit alakít belső energiává, így négyszer annyi út kell.

> megjegyzés: Lásd: „Hová lesz az energia?” lecke.

### Feliratok
- lassabb csúszka: A lassabb autó sebessége
- itt még: itt még
- fékút tengely: fékút (m)
- négyszer: kétszer gyorsabb → négyszer hosszabb fékút
- lassabb: lassabb
- gyorsabb: kétszer gyorsabb
- fékezés kezdete: itt kezdenek fékezni

### Adatok
- lassabb autó sebessége: 45 km/h

## 7. Önvezető autó
Az önvezető autó **radarral és kamerával** folyamatosan figyeli az utat, és ==tizedmásodpercek alatt fékez==. Nem néz a telefonjára.

A fékútja viszont ugyanakkora: azt a gumik és az út szabják meg.

> megjegyzés: Az önvezető autó reakcióideje becslés, típusonként eltér.

### Feliratok
- telefonozó: telefonozó sofőr
- figyelő: figyelő sofőr
- önvezető: önvezető autó
- érzékelők: radar + kamera
- zebránál: a zebránál
- reakcióidő oszlop: reakcióidő
- ugyanannyi: a fékút mindhárom autónál ugyanannyi:

### Adatok
- telefonozó reakcióideje: 2,0 s
- önvezető reakcióideje: 0,3 s

## 8. Öv és légzsák
Ütközéskor az autó hirtelen megáll. Téged ==semmi sem lök előre==: a tested **tovább halad**, amíg valami meg nem állítja.

Az öv és a légzsák **hosszabb úton** állít meg, ezért sokkal kisebb erővel.

> megjegyzés: Egy {városi sebesség}-s ütközés olyan, mint egy zuhanás a 3. emeletről. (Becsült megállási utakkal számoltunk.)

### Feliratok
- ütközés csúszka: Ütközési sebesség
- újra gomb: Ütközés újra
- bekötve: bekötve: öv + légzsák
- bekötetlen: bekötetlen
- tovább halad: a test tovább halad
- sebesség: sebesség
- autó: autó
- test: test
- átlagos erő: átlagos erő a testen
- súlya: ≈ ennyi teher súlya:
- arány: öv nélkül ennyiszer nagyobb erő:
- képlet erő: erő × út = mozgási energia
- zuhanás: ugyanaz, mint zuhanás ennyi magasról:
- légzsák: légzsák
- öv: öv

### Adatok
- utas tömege: 70 kg
- gyűrődési zóna: 0,5 m
- test megállási útja övvel: 0,7 m
- távolság a kormányig: 0,6 m
- test megállási útja öv nélkül: 0,05 m
- ütközési lassítás: 20

## 9. Összefoglalás
- **Út**: a megtett pálya hossza. **Elmozdulás**: honnan hová jutottál.
- Átlagsebesség = összes út / összes idő, a megállásokkal együtt.
- Erő ==a mozgás megváltoztatásához== kell, nem a fenntartásához.
- Megállási út = reakcióút + fékút. ==Kétszer gyorsabban négyszer hosszabb a fékút.==
- Az öv hosszabb úton, kisebb erővel állít meg.

### Feliratok
- összefoglaló cím: Megállási út száraz úton, {reakcióidő} reakcióidővel
- tanulság: Lassíts, figyelj, és kösd be az öved!
- városban: városban
- országúton: országúton
- autópályán: autópályán

### Adatok
- országúti sebesség: 90 km/h
- autópálya sebesség: 130 km/h
