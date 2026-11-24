# Kijut-e a robot bármelyik útvesztőből? – tesztelés és hibakeresés
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 3. Robotika

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/09-labirintus.md

  A blokkok felirata a „… blokk” kulcsokból jön; a # a paraméter helye (szám, irány, feltétel).
  A „Tippelj!” lépésekben (3., 7.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A pályák, a programok és a futások eredményei (kijutott / falnak ment / körbe jár, a lépések
  száma) a kódban készülnek – kézzel nincsenek kiírva.
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
- kitalált bélyeg: kitalált pályák
- blokknyelv bélyeg: a lecke saját blokkjai
- program felirat: A PROGRAM
- útvesztő felirat: AZ ÚTVESZTŐ FELÜLRŐL
- indításkor blokk: indításkor
- indításkor vége: program vége
- lépj blokk: lépj előre # mezőt
- lépj egyet blokk: lépj egy mezőt
- fordulj blokk: fordulj #
- jobbra opció: jobbra
- balra opció: balra
- amíg blokk: ismételd, amíg #
- amíg vége: ismétlés vége
- ha-különben blokk: ha # akkor
- ha-különben közép: különben
- ha-különben vége: elágazás vége
- bent? blokk: bent van
- jobbra szabad? blokk: jobbra szabad
- előre szabad? blokk: előre szabad
- igaz felirat: IGAZ
- hamis felirat: HAMIS
- kör felirat: #. kör
- korlát felirat: végtelen ciklus?
- ütközés hiba: falnak ment!
- futtatás gomb: Futtatás
- egy lépés gomb: Egy lépés
- alaphelyzet gomb: Alaphelyzet
- sebesség csúszka: Sebesség
- lassú felirat: lassú
- normál felirat: normál
- gyors felirat: gyors
- azonnal felirat: azonnal
- kijárat felirat: KIJÁRAT
- kijutott felirat: kijutott · # lépés
- falnak felirat: falnak ment
- körbe felirat: körbe jár
- fal jel felirat: fal
- szabad jel felirat: szabad
- pálya felirat: #. pálya
- teszt felirat: TESZT
- várt felirat: várt: kijut
- történt felirat: történt: #

## 1. A cél: ki az útvesztőből
A robot nem látja az útvesztőt. Csak azt **érzékeli**, van-e fal **előtte**, **jobbra** és **balra**. Lépni és fordulni tud. ==Vezesd ki a gombokkal!== Minden gombnyomásod egy utasítás lesz.

> megjegyzés: A robot modell: mezőről mezőre lép, pontosan fordul. Csúszás, akkumulátor nincs benne.

### Feliratok
- lépj gomb: Lépj egy mezőt
- jobbra gomb: Fordulj jobbra
- balra gomb: Fordulj balra
- újra gomb: Kezdd újra
- gombokból felirat: A PROGRAM – A GOMBJAIDBÓL
- vezesd felirat: Vezesd ki a robotot!
- fal előtte felirat: Előtte fal van!
- túl hosszú felirat: Túl hosszú lett – kezdd újra!
- utasítás felirat: # utasítás
- érzékel felirat: a robot ennyit érzékel:

## 2. Kézzel megírt út
Ez a program pontosan leírja az utat: hány mezőt lépjen, merre forduljon. Lefuttattuk, és kijutott. Ez egy **teszt**: kipróbáljuk, és összevetjük, amit vártunk, azzal, ami történt. ==Változtass egy számot! Mi lesz?==

### Feliratok
- kattints felirat: kattints a számra: − bal fele, + jobb fele

## 3. Másik pályán?
Ugyanez a program egy másik útvesztőben. ==Mi történik? Tippelj!==

**Falnak megy.** A program csak az első pályára jó: az utat írtuk le, nem azt, hogyan kell utat találni. Egyszer működött – ettől még nincs kész.

### Feliratok
- pálya kérdés felirat: Ugyanez a program a 2. pályán. Mi lesz?
- kijut tipp: kijut
- elakad tipp: elakad a falnál
- másik kijárat tipp: másik kijáraton megy ki
- csak egy pályára felirat: az út az 1. pályáé volt

## 4. Általános szabály: jobb kéz a falon
Képzeld el, hogy a jobb kezed végig a falon csúszik. ==Ha jobbra szabad, fordulj jobbra és lépj; különben ha előre szabad, lépj; különben fordulj balra.== Ez a program nem az utat írja le, hanem egy **szabályt**. Próbáld ki mindhárom pályán!

### Feliratok
- pálya gomb: Másik pálya
- jobb kéz felirat: a jobb kéz a falon
- egyszer felirat: egyszer járt itt
- kétszer felirat: zsákutcából vissza

## 5. Lépésenként: hibakeresés
**Hibakereséskor** lépésenként futtatjuk a programot. A **töréspont** (piros pötty) megállítja a futást. Miért itt állt meg? Nézd a robot állapotát: elöl és jobbra is fal van. ==Léptesd tovább!== Töréspontot a blokk bal szélére kattintva tehetsz.

### Feliratok
- állapot felirat: A ROBOT ÁLLAPOTA – EZT LÁTJA A PROGRAM
- hely felirat: hely: #. oszlop, #. sor
- arra néz felirat: arra néz:
- töréspont felirat: itt megállt
- sávra felirat: töréspont: kattints a blokk bal szélére
- lépésszám felirat: eddig # utasítás

## 6. Hol a hiba?
Ebben a programban egy irány hibás. A robot falnak ment, és a „lépj” blokknál állt meg. ==Ott a hiba?== Tegyél töréspontot, léptesd, és kattints a hibás irányra! Egyszerre csak egy dolgot változtass, aztán teszteld újra.

### Feliratok
- itt akadt felirat: itt akadt el
- itt kezdődött felirat: itt fordult rossz irányba
- javítva felirat: Javítva – újra teszteltük!
- változtatás felirat: változtatás: #

## 7. Teszteljük minden pályán!
A 4. pályán a robot egy különálló fal, a „sziget” mellől indul. ==Kijut a jobbkéz-szabállyal? Tippelj!==

**Körbe-körbe megy:** a jobb keze a szigeten marad. Ha ugyanoda ér, ugyanarra nézve, minden ismétlődik: ez **végtelen ciklus**. Ha minden fal összefügg a külső fallal, a szabály mindig kivezet.

### Feliratok
- sziget kérdés felirat: A 4. pályán a robot a sziget mellől indul. Kijut?
- kijut 4 tipp: kijut
- körbe tipp: körbe-körbe megy
- megáll tipp: megáll
- teszttábla felirat: TESZTTÁBLA – UGYANAZ A PROGRAM, NÉGY PÁLYA
- sziget felirat: sziget
- ismétlődik felirat: ugyanitt, ugyanarra: #. kör
- véletlen felirat: #. pálya – véletlen
- új pálya gomb: Új véletlen pálya

### Adatok
- lépéskorlát: 500 utasítás
<!-- forrás: a lecke beállítása – ennyi végrehajtott blokk után a futás megáll („végtelen ciklus?”) -->

## 8. Összefoglalás
- Egy pályán működött? Kevés: **teszteld** sok pályán, nehéz esetekben is.
- A **hibakereső** lépésenként mutatja a programot és a robot állapotát.
- A hiba gyakran előbb van, mint ahol a robot elakad. ==Egyszerre egy dolgot javíts, és tesztelj újra.==

> megjegyzés: Rajzoljatok egymásnak pályát, és teszteljétek rajta a szabályt!

### Feliratok
- tervezés kártya: TERVEZÉS
- kódolás kártya: KÓDOLÁS
- tesztelés kártya: TESZTELÉS
- javítás kártya: JAVÍTÁS
- tervezés példa: szabály: jobb kéz a falon
- kódolás példa: blokkokból program
- tesztelés példa: sok pálya, nehéz esetek is
- javítás példa: egy változtatás, újra teszt
- kör felirat közép: amíg minden teszt jó nem lesz

### Adatok
- robot sebessége: 2,5 mező/s (modell)
<!-- forrás: modell – a lecke saját robotja; a vásznon ennyi mezőt tesz meg másodpercenként (normál sebességnél) -->
- fordulás sebessége: 270 °/s (modell)
<!-- forrás: modell – helyben fordulás -->

<!-- Tanári megjegyzések és források:
  - A négy pálya kitalált, a kódban készül: az 1–3. pálya „tökéletes” útvesztő (minden mező elérhető, kör
    nincs benne), mélységi bejárással, rögzített véletlenmaggal generálva – minden betöltéskor ugyanaz. Az
    „Új véletlen pálya” gomb ugyanígy, egy következő maggal készít új pályát. A 4. pálya generált útvesztő,
    amelynek közepén egy 3 × 3 mezős terem van, benne egy oszloppal (a „sziget”): az oszlop falai sehol nem
    érnek más falhoz.
  - A robot modell: mezőről mezőre lép, pontosan 90°-ot fordul, három érzékelője van (fal elöl / jobbra /
    balra – a lecke blokkjaiban „előre szabad”, „jobbra szabad”). Ütközéskor a lecke modelljében a program
    megáll („falnak ment!”). Súrlódás, kerékcsúszás, akkumulátor nincs benne.
  - A 6. lépés hibás programja: az első ágban („ha jobbra szabad”) a „fordulj jobbra” helyett „fordulj
    balra” áll. A 2. pályán a robot az első ilyen elágazásban (a felső sorban) rossz irányba fordul,
    végigmegy a felső folyosón, majd egy későbbi elágazásban falnak megy – a hiba helye és az elakadás
    helye különbözik. Javítás: a „balra” szóra kattintva „jobbra” lesz. Ha a diák a harmadik ág
    „fordulj balra” blokkját írja át, a robot már az első sarokban falnak megy – a próba megmutatja, hogy
    nem ott volt a hiba (ezt is érdemes megbeszélni).
  - A jobbkéz-szabály (falkövetés) állítása: ha egy útvesztő minden fala összefügg egymással és a külső
    fallal („egyszeresen összefüggő” útvesztő), a falat követő robot nem téved el, és eljut egy másik
    kijárathoz, ha van ilyen; ha nincs, visszaér a kiindulási helyére. Rövid indoklás: a robot végig
    ugyanazt az összefüggő falcsoportot követi, mintha egy tárgy körvonalát járná körbe; a körvonal véges,
    és rajta van a külső fal minden nyílása, így a kijárathoz előbb-utóbb odaér. Ha viszont a robot egy
    különálló falcsoport („sziget”) mellől indul, annak a körvonalát járja körbe vég nélkül.
    Forrás: Wikipedia, „Maze-solving algorithm” szócikk, „Hand-on-wall rule” szakasz (angol nyelvű,
    letöltve 2026-11-24). A lecke kódja ellenőrzi: sok száz véletlen tökéletes útvesztőben a szabály
    mindig kijut, a 4. pályán körbe jár.
  - A végtelen ciklus felismerése: a programban nincs változó, ezért a robot következő lépése csak attól
    függ, melyik mezőn áll és merre néz. Ha a ciklus elején ugyanoda ér, ugyanarra nézve, onnan minden
    pontosan ismétlődik. A lépéskorlát ({lépéskorlát}) csak biztonsági fék.
  - A gráfbejárás és a szélességi keresés (a legrövidebb út megkeresése) 9–10. osztályos anyag – itt
    nem kerül elő.
  - A lecke blokknyelve saját: az órán használt környezetben a blokkok másképp néznek ki, a töréspont és
    a lépésenkénti futtatás is máshol (vagy nem minden környezetben) érhető el.
-->
