# Miért nem melegszik tovább a forrásban lévő víz? – halmazállapot-változások
tantárgy: Fizika · évfolyam: 7–8. · témakör: 5. Víz és levegő a háztartásban és a környezetünkben

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/06-halmazallapot.md

  A modell egyszerűsítései:
  - a főzőlap minden energiája a fazék tartalmába jut (nincs hőveszteség, a fazék
    melegedését sem számoljuk), és a tartalom hőmérséklete mindenütt ugyanannyi;
  - a gőz melegítése (az összefoglaló szaggatott szakasza) csak zárt edényben lehetséges,
    nyitott fazékból a gőz elszáll;
  - a forráshőt 100 °C-on vett értékkel számoljuk a Kékesen is (96,7 °C-on kb. 0,4 %-kal nagyobb);
  - a részecskerajz szemléltetés: síkbeli, a mozgás lassított, a hőmérséklettel való élénkülése
    felnagyított; a buborékban valójában még sokkal ritkábbak a részecskék;
  - a párolgás ütemének kiírt aránya a telített vízgőz nyomásából jön (Antoine-egyenlet),
    a rajzon a kiszökő részecskék gyakorisága ennek csak a négyzetgyökével nő.
  Források: fajhők, olvadáshő, forráshő: standard táblázati értékek (pl. Engineering Toolbox,
  Négyjegyű függvénytáblázatok). A Kékes-tető (1014 m) légnyomása normál légkörben ≈ 900 hPa,
  ehhez a víz forráspontja ≈ 96,7 °C. 1 kg vízből 100 °C-on, 1013 hPa-on ≈ 1,67 m³ gőz lesz.
-->

## Közös

### Feliratok
- hőmérséklet: hőmérséklet
- idő: eltelt idő
- felvett energia: felvett energia
- szilárd: szilárd (jég)
- olvad: olvad
- folyékony: folyékony (víz)
- forr: forr
- légnemű: légnemű (vízgőz)
- nagyítás: nagyítás · szemléltetés
- főzőlap: főzőlap: {főzőlap teljesítménye}
- kikapcsolva: kikapcsolva
- idő tengely: idő (perc)
- hőmérséklet tengely: hőmérséklet (°C)
- áll a hőmérő: áll a hőmérő
- elforrt: elforrt

### Adatok
- kezdő hőmérséklet: −20 °C
- olvadáspont: 0 °C
- forráspont: 100 °C
- jég fajhője: 2,1 kJ/(kg·°C)
- víz fajhője: 4,18 kJ/(kg·°C)
- gőz fajhője: 2,0 kJ/(kg·°C)
- olvadáshő: 334 kJ/kg
- forráshő: 2256 kJ/kg
- főzőlap teljesítménye: 2000 W
- víz tömege: 1 kg

## 1. Szilárd: rácsban rezegnek
A fazékban {víz tömege} **jég** van, {kezdő hőmérséklet}-os. Nagyítsunk bele!

A vízrészecskék szabályos **rácsba** rendeződnek, a kötések a helyükön tartják őket. Mégsem állnak: ==a helyükön rezegnek==.

> megjegyzés: Tippeljetek! Egyenletesen melegítjük, amíg minden el nem forr. Hogyan változik közben a hőmérséklet? Rajzoljátok le!

### Feliratok
- kötés: kötés
- rezeg: rezeg a helyén

## 2. Melegítés: hevesebb rezgés
Bekapcsoljuk a főzőlapot. A jég **belső energiája** nő: a részecskék egyre hevesebben rezegnek. ==Ezt mutatja a hőmérő.==

Tévhit, hogy a részecskék közben megnőnek vagy megolvadnak. Ugyanazok maradnak, csak gyorsabban mozognak.

> megjegyzés: A belső energia a részecskék mozgásából és a köztük lévő kötésekből adódik (lásd: „Hová lesz az energia?”).

### Feliratok
- tévhit megnő: Megnőnek a részecskék?
- nem nő: Nem: csak hevesebben rezegnek
- ugyanakkora: ugyanakkora

## 3. Olvadás: áll a hőmérő
{olvadáspont}-on a hőmérő megáll, pedig a főzőlap ugyanúgy melegít! A felvett energia most ==a kötések bontására megy==: a rács szétesik.

Energiát adunk, a hőmérséklet mégsem nő: a **hő** és a **hőmérséklet** nem ugyanaz.

> megjegyzés: Az olvadáshő {olvadáshő}: ennyi energia olvaszt meg 1 kg {olvadáspont}-os jeget.

### Feliratok
- kötések bomlanak: kötések bomlanak

## 4. A víz melegszik – lassabban
Elolvadt a jég. A hőmérséklet újra nő, a részecskék ==elcsúsznak egymáson==, és egyre gyorsabban mozognak.

Nézd a meredekséget! A víz kb. fele olyan gyorsan melegszik, mint a jég. A **fajhő** megmutatja, mennyi energia melegít 1 kg anyagot 1 °C-kal: víznél {víz fajhője}, jégnél csak {jég fajhője}.

### Feliratok
- elcsúsznak: elcsúsznak
- jég meredekség: jég: {jég fajhője}
- víz meredekség: víz: {víz fajhője}

## 5. Forrás: a buborék vízgőz
{forráspont}-on a víz forr, és ==a hőmérő megint áll==. A buborékok **nem levegőből** állnak: vízgőzből, kiszabadult vízrészecskékből.

Ehhez minden kötést szét kell szakítani: a forráshő ({forráshő}) majdnem hétszerese az olvadáshőnek.

> megjegyzés: 1 liter vízből kb. {gőz térfogata} vízgőz lesz: a gőzben nagyon ritkák a részecskék.

### Feliratok
- tévhit levegő: Levegő van a buborékban?
- nem levegő: Nem: vízgőz, vízrészecskék
- vízgőz: vízgőz
- hányszor: kb. #-szor tovább tart, mint az olvadás

### Adatok
- gőz térfogata: 1700 L

## 6. Mitől gyorsabb a melegítés?
Állítsd a főzőlap teljesítményét és a víz tömegét! A platók ==hossza változik, a magassága nem==: erősebb lánggal sem lesz forróbb a forrásban lévő víz, csak hamarabb elforr.

A forráspontot a **légnyomás** változtatja meg: a Kékesen a víz már {forráspont a Kékesen}-on forr.

### Feliratok
- teljesítmény csúszka: A főzőlap teljesítménye
- tömeg csúszka: A jég (víz) tömege
- tengerszint gomb: tengerszint
- Kékes gomb: Kékes-tető
- tengerszint: tengerszint, {normál légnyomás}
- Kékes: Kékes-tető, ≈ {légnyomás a Kékesen}
- tévhit láng: Erősebb lánggal forróbb lesz?
- nem forróbb: Nem: csak hamarabb elforr
- olvadás ideje: olvadás
- melegítés ideje: víz melegítése
- forrás ideje: forrás (elforralás)
- forráspont felirat: forráspont
- most: most
- alap: alap
- összehasonlítás: szaggatott: {víz tömege}, {főzőlap teljesítménye}
- folytatódik: folytatódik →

### Adatok
- forráspont a Kékesen: 96,7 °C
- légnyomás a Kékesen: 900 hPa
- normál légnyomás: 1013 hPa

## 7. Párolgás és lecsapódás
A víz **bármely hőmérsékleten** párolog: a felszínről ==a leggyorsabb részecskék kiszöknek==. Melegebb víz gyorsabban párolog.

**Forrás** csak a forrásponton van: ekkor az egész folyadékban gőzbuborékok keletkeznek.

A hideg fedőn a gőz **lecsapódik**: újra víz lesz.

> megjegyzés: A fazék fölötti fehér „gőz” már apró vízcsepp. A vízgőz láthatatlan!

### Feliratok
- hőmérséklet csúszka: A víz hőmérséklete
- hideg fedő: hideg fedő
- lecsapódik: lecsapódik
- víz: víz
- vízrészecske: vízrészecske
- levegőrészecske: levegőrészecske
- gőzbuborék: gőzbuborék
- párolgás: párolgás
- forrás: forrás
- lecsapódás: lecsapódás
- párolgás hol: a felszínen
- párolgás mikor: bármely hőmérsékleten
- forrás hol: az egész folyadékban
- forrás mikor: csak a forrásponton
- lecsapódás leírás: hideg felületen újra víz lesz
- párolgás üteme: párolgás a {szobahőmérséklet}-oshoz képest
- kiszökik: kiszökik
- most forr: most forr!
- most nem forr: most nem forr

### Adatok
- szobahőmérséklet: 20 °C

## 8. Összefoglalás
- Szilárd: rácsban **rezegnek**; folyékony: **elcsúsznak** egymáson; légnemű: szabadon **repülnek**.
- Melegítéskor a részecskék gyorsabban mozognak – nem nőnek meg.
- Olvadás és forrás közben ==a hőmérséklet áll==: az energia a kötéseket bontja.
- Erősebb láng: rövidebb plató, nem magasabb.
- Párolgás: bármikor, a felszínen. Forrás: a forrásponton, az egészben.

### Feliratok
- energia tengely: felvett energia 1 kg-ra (kJ)
- jég melegszik: jég melegszik
- olvadás: olvadás
- víz melegszik: víz melegszik
- gőz melegszik: gőz (zárt edényben)
- rácsban rezegnek: rácsban rezegnek
- elcsúsznak egymáson: elcsúsznak egymáson
- szabadon repülnek: szabadon repülnek
- fagyás: fagyás
- tanulság: Olvadás és forrás közben a hőmérséklet áll: az energia a kötéseket bontja.

### Adatok
- gőz végső hőmérséklete: 130 °C
