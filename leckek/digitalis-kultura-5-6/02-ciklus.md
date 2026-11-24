# Hányszor írjam le ugyanazt? – szekvencia és ciklus
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 1. Algoritmizálás és blokkprogramozás

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/02-ciklus.md

  A blokkok felirata a „… blokk” kulcsokból jön; a # a paraméter helye (szám, irány, feltétel).
  A szám után álló „-szor” toldalékot a program a számhoz igazítja (4-szer, 5-ször, 3-szor).
  A „Tippelj!” lépésekben (3., 6.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A fordulás szöge mindig számolt érték (teljes fordulat / oldalszám) – nem itt van megadva.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- modell bélyeg: modell
- blokknyelv bélyeg: a lecke saját blokkjai
- program felirat: A PROGRAM
- asztal felirat: AZ ASZTAL FELÜLRŐL
- utasítás felirat: # utasítás
- indításkor blokk: indításkor
- indításkor vége: program vége
- lépj blokk: lépj előre # lépést
- fordulj blokk: fordulj # # fokot
- jobbra opció: jobbra
- balra opció: balra
- ismételd blokk: ismételd #-szor
- ismételd vége: ismétlés vége
- amíg blokk: ismételd, amíg #
- amíg vége: ismétlés vége
- mindig blokk: ismételd mindig
- mindig vége: ismétlés vége
- nem blokk: nem #
- ütközik? blokk: ütközik
- igaz felirat: IGAZ
- hamis felirat: HAMIS
- kör felirat: #. kör
- korlát felirat: végtelen ciklus?
- stop felirat: vége
- futtatás gomb: Futtatás
- egy lépés gomb: Egy lépés
- alaphelyzet gomb: Alaphelyzet
- sebesség csúszka: Sebesség
- lassú felirat: lassú
- normál felirat: normál
- gyors felirat: gyors
- azonnal felirat: azonnal
- fordulásmérő felirat: a robot fordulása
- összesen felirat: összesen #
- szorzat felirat: # · # = #
- fordulat felirat: = # teljes fordulat

### Adatok
- egy lépés hossza: 5 mm (modell)
<!-- forrás: modell – a lecke saját robotjának lépése (a blokkprogramozó környezetekben a „lépés” rendszerint képpont vagy a robot saját egysége) -->
- robot sebessége: 25 cm/s (modell)
<!-- forrás: modell – nagyságrendileg egy kis iskolai robot haladási sebessége; a futás a Sebesség csúszkával gyorsítható -->
- fordulás sebessége: 180 °/s (modell)
<!-- forrás: modell – helyben fordulás, a két kerék ellentétes irányban forog -->
- teljes fordulat: 360°
<!-- forrás: definíció (egy teljes fordulat 360 fok) -->
- négyzet oldala: 100 lépés
<!-- forrás: a lecke példaprogramja -->
- négyzet fordulása: 90°
<!-- forrás: a négyzet külső szöge: 360° / 4 = 90° (a kód ellenőrzi) -->

## 1. Rajzolj négyzetet!
A robot pontosan azt teszi, amit a program mond: **sorban, egymás után**. Ez a **szekvencia**. Kattints egy számra, és nézd meg, mi változik!

A robot modell: a súrlódást, az akkumulátort és a kerékcsúszást elhagyja.

> megjegyzés: Régi ötlet: az 1960-as évek végén is így tanultak gyerekek („teknőcgrafika”).

## 2. Négyszer ugyanaz: a ciklus
Ugyanaz a két utasítás négyszer ismétlődik. Tegyük **ciklusba**! Ami ismétlődik, az a **ciklusmag**. A program rövidebb, és egy helyen javítható. Kattintással állítsd a 4-et 6-ra, és a fordulást 60-ra!

### Feliratok
- pár felirat: #. pár
- ciklusmag felirat: ciklusmag
- rövidebb felirat: # utasítás helyett #
- osztás gomb: fordulás = 360° / ismétlés

## 3. Tippelj: mit rajzol?
A robot ötször ismétli: lép, majd 72°-ot fordul jobbra. ==Mit rajzol? Tippelj!==

**Ötszöget.** A robot végül visszaér a helyére, és összesen {teljes fordulat}-ot fordult: egy teljes fordulatot. Minden szabályos sokszögnél így van.

> megjegyzés: Ezért egy fordulás = 360° / oldalszám. A belső szög ezt egészíti ki 180°-ra.

### Feliratok
- ötszög kérdés felirat: Mit rajzol ez a program?
- ötszög tipp: ötszöget
- csillag tipp: csillagot
- nyitott tipp: nyitott vonalat

### Adatok
- ötszög oldalszáma: 5
<!-- forrás: a lecke példaprogramja (a fordulás a kódban: 360° / 5 = 72°) -->

## 4. Háromszög: 60 vagy 120?
Sokan gondolják: a háromszög szögei 60°-osak, tehát 60°-ot kell fordulni. Futtasd mindkettőt! A robot a **menetirányához képest** fordul: 120°-ot, és így a belső szög 60°. Összesen `3 * 120° = 360°`.

> megjegyzés: Próbáld ki az A programban a 90°-ot és a 100°-ot is!

### Feliratok
- a program felirat: A PROGRAM
- b program felirat: B PROGRAM
- fordulás ív felirat: fordulás #
- belső szög felirat: belső szög #
- zárt felirat: visszaért: zárt alakzat
- nyitott felirat: nem ért vissza

### Adatok
- tévhit fordulása: 60°
<!-- forrás: a tévhit (a szabályos háromszög belső szöge 60°; a robotnak a külső szöggel, 180° − 60° = 120°-kal kell fordulnia) -->

## 5. Sokszögből kör
Húzd a csúszkát! A program mindig ugyanaz: n-szer lép és fordul, a fordulás 360° / n. Sok apró oldalnál a szem már **körnek** látja – pedig a robot most is egyenes szakaszokat rajzol.

### Feliratok
- oldalszám csúszka: Oldalak száma
- valódi kör felirat: szaggatott: valódi kör
- oldalszám felirat: # oldal
- kerület felirat: # · # lépés = # lépés
- oldal hossza felirat: egy oldal: # cm

### Adatok
- kör kerülete: 360 lépés
<!-- forrás: a lecke példája (a kerület minden oldalszámnál ugyanannyi, így az alakzatok egyforma nagyok) -->

## 6. Csillag: kétszer körbe
Ugyanaz az ötszög-program, de a robot 72° helyett {csillag fordulása}-ot fordul. ==Mit rajzol? Tippelj!==

**Ötágú csillagot.** A robot összesen `5 * 144° = 720°`-ot fordul: **kétszer** fordul körbe, mire visszaér. Zárt útnál a fordulás mindig egész fordulat: 360°, 720°, 1080°…

### Feliratok
- csillag kérdés felirat: És ha 72° helyett 144°-ot fordul?
- ötszög 144 tipp: ötszöget
- csillag 144 tipp: csillagot
- két kör tipp: két kört

### Adatok
- csillag fordulása: 144°
<!-- forrás: az ötágú csillag (pentagramma) csúcsainál a fordulás 144°; 5 · 144° = 720° = 2 · 360° (a kód ellenőrzi) -->

## 7. Ciklus a ciklusban
A belső ciklus négyzetet rajzol. A külső ezt ismétli – {virág ismétlése} körben –, és minden kör végén {virág fordulása}-ot fordul. Ciklusba **ciklus** is tehető. Húzd a {virág fordulása}-os fordulást a belső ciklusba, vagy egészen ki!

> megjegyzés: Számold meg: a program néhány utasítása 108 mozdulatot vezérel.

### Feliratok
- mozdulat felirat: végrehajtott mozdulat: #
- húzd felirat: fogd meg, és húzd máshová!

### Adatok
- virág ismétlése: 12
<!-- forrás: a lecke példaprogramja; 12 · 30° = 360° (a kód ellenőrzi) -->
- virág fordulása: 30°
<!-- forrás: a lecke példaprogramja -->

## 8. Meddig ismételjen?
A **számlálós** ciklus adott számszor ismétel, a **feltételes** addig, amíg a feltétel igaz – itt: amíg nem ütközik. A **végtelen** sosem áll meg: egy robotnál ez szándékos, figyel, amíg ki nem kapcsolják. Helyezd át a falat!

> megjegyzés: A szimulátor a végtelen ciklust egy idő után megállítja.

### Feliratok
- számlálós felirat: számlálós: adott számszor
- feltételes felirat: feltételes: amíg nem ütközik
- végtelen felirat: végtelen: amíg ki nem kapcsolod
- kikapcsolva felirat: kikapcsolva
- leállítva felirat: # utasítás után leállítva
- fal gomb: Fal áthelyezése
- kikapcsolás gomb: Kikapcsolás

### Adatok
- lépéskorlát: 120 utasítás
<!-- forrás: a lecke szimulátorának beállítása (lépéskorlát, hogy a végtelen ciklus ne fagyassza le az oldalt) -->

## 9. Összefoglalás
A **szekvencia** utasítások sora. A **ciklus** ismétel; ami ismétlődik, a **ciklusmag**. Fajtái: számlálós, feltételes, végtelen. Ciklusba ciklus tehető. Zárt sokszögnél a robot összesen 360°-ot fordul, ezért egy fordulás 360° / oldalszám.

### Feliratok
- négyzet galéria: négyzet
- hatszög galéria: hatszög
- ötszög galéria: ötszög
- csillag galéria: ötágú csillag
- kör galéria: majdnem kör
- virág galéria: virág
- beágyazott galéria: ciklus a ciklusban
- folyamatábra felirat: UGYANEZ FOLYAMATÁBRÁN
- szekvencia kártya: szekvencia: utasítások sorban, egymás után
- ciklus kártya: ciklus: ismétlés – a ciklusmag többször fut
- fajták kártya: számlálós · feltételes · végtelen – és ciklus a ciklusban

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a robot, az asztal, a fal és minden program a lecke saját példája.
  - Modell-egyszerűsítések: a robot pontosan annyit lép és fordul, amennyit a program mond; nincs súrlódás,
    akkumulátor, kerékcsúszás, gyorsulás. A „lépés” itt 5 mm (modell); a sebességek (25 cm/s, 180 °/s)
    nagyságrendi modellértékek, a futás a Sebesség csúszkával gyorsítható.
  - A falnál a robot megáll (az ütköző jelez), semmi nem törik. A végtelen ciklust a szimulátor lépéskorlátja
    állítja meg („végtelen ciklus?”) – valódi robotnál a „mindig” ciklus szándékos (pl. figyel), és a
    kikapcsolásig fut.
  - A blokknyelv a lecke saját nyelve (papír blokk, bal oldali kategóriasáv, behúzott ciklusmag, „ismétlés
    vége” záró sáv). Az órán használt blokkprogramozó környezetben a blokkok színe, alakja és felirata
    eltér (pl. ott a „lépés” rendszerint képpont, a fordulás iránya lehet „balra/jobbra” helyett jelölt
    nyíl), a szerkezet (szekvencia, ciklus, ciklusmag, beágyazás) ugyanaz.
  - Teknőcgrafika: a Logo nyelv (Seymour Papert és munkatársai, 1967 körül; a teknős-robot az 1960-as évek
    végétől) – az évszám ellenőrizendő; a magyar iskolákban a Comenius Logo és az Imagine is ezt a hagyományt
    vitte tovább (nincs ellenőrizve).
  - A panelszövegben a 72°, a 144° és az 5 · 144° = 720° kézzel írt szám (a vásznon a kód számolja az adatokból):
    ha az ötszög oldalszámát vagy a csillag fordulását átírod, ezeket is írd át.
  - Matematika: a szabályos n-szög külső szöge 360° / n, belső szöge 180° − 360° / n; az ötágú csillag
    csúcsainál a fordulás 144° (5 · 144° = 720°). A 4. lépés tévhite: 3 · 60° = 180° – a 60°-os program
    félhatszöget (nyitott vonalat) rajzol.
-->
