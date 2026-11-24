# Hogyan marad a robot a vonalon? – fényszenzor és visszacsatolás
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 3. Robotika

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/08-vonalkoveto.md

  A blokkok felirata a „… blokk” kulcsokból jön; a # a paraméter helye (szám, szenzor, feltétel).
  A „Tippelj!” lépésekben (3., 5.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A számolt értékek (két mérés között megtett út, mérések száma másodpercenként, a kétszeres
  sebesség, a fényprofil, a termosztát görbéje) a kódban készülnek az alábbi adatokból.
  A robot mozgása valódi (determinisztikus) szimuláció: ha egy adatot átírsz, a robot
  másképp mozoghat – ilyenkor a QA-ellenőrzések jelzik, ha egy lépés állítása már nem igaz.
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
- lassítva bélyeg: lassítva
- blokknyelv bélyeg: a lecke saját blokkjai
- program felirat: A PROGRAM
- pálya felirat: A PÁLYA FELÜLRŐL
- indításkor blokk: indításkor
- indításkor vége: program vége
- mindig blokk: ismételd mindig
- mindig vége: ismétlés vége
- ha-különben blokk: ha # akkor
- ha-különben közép: különben
- ha-különben vége: elágazás vége
- < blokk: # < #
- − blokk: # − #
- motorok blokk: motorok: bal # %, jobb # %
- fény opció: fény
- bal fény opció: bal fény
- jobb fény opció: jobb fény
- igaz felirat: IGAZ
- hamis felirat: HAMIS
- kör felirat: #. kör
- futtatás gomb: Futtatás
- mért felirat: #
- küszöb felirat: küszöb: #
- idő tengely: idő (s)
- fény tengely: mért fény
- fekete felirat: fekete
- fehér felirat: fehér
- balra felirat: balra
- jobbra felirat: jobbra
- előre felirat: előre
- mér felirat: MÉR
- dönt felirat: DÖNT
- mozdul felirat: MOZDUL

### Adatok
- fehér padló értéke: 90 (modell)
<!-- forrás: modell – a fényszenzor 0–100-as skáláján (mint a 07-szenzor leckében); a valódi érték szenzoronként, padlónként és megvilágításonként más -->
- fekete vonal értéke: 10 (modell)
<!-- forrás: modell – mint fent -->
- küszöb: 50 (modell)
<!-- forrás: modell – a fehér és a fekete érték közepe; valódi robotnál a két mért érték átlagát szokás küszöbnek venni (kalibrálás) -->
- vonal szélessége: 2 cm (becslés)
<!-- forrás: becslés – vonalkövető pályákhoz gyakran kb. 2 cm széles fekete szigetelőszalagot vagy nyomtatott vonalat használnak; a pontos érték pályánként más -->
- robot sugara: 6 cm (modell)
<!-- forrás: modell – egy kis iskolai padlórobot mérete nagyságrendileg (ugyanaz, mint a 07-szenzor leckében) -->
- robot sebessége: 20 cm/s (modell)
<!-- forrás: modell – nagyságrendileg egy kis iskolai robot haladási sebessége (mint a 07-szenzor leckében); ennél a kétszeres sebességnél (40 cm/s) repül le a 3. lépés éles kanyarjában -->
- vezérlési ütem: 100 ms (modell)
<!-- forrás: modell – ennyi időnként mér és dönt a lecke robotja (10-szer másodpercenként). Szándékosan lassú, hogy a cikázás és a „vakon megtett út” látsszon; a valódi robotok ennél sűrűbben, másodpercenként több tucatszor mérnek (becslés). A terv 20 ms-ot írt – azzal a 2 cm-es vonalon a cikázás szemmel nem látszott. -->
- átállási idő: 0,05 s (modell)
<!-- forrás: modell – a motorok nem azonnal veszik fel az új sebességet; ennyi idő alatt állnak át nagyjából -->
- szenzor előretolása: 5 cm (modell)
<!-- forrás: modell – a fényszenzor a robot közepe előtt, a padló fölött ül -->
- két szenzor távolsága: 6 cm (modell)
<!-- forrás: modell – a két szenzor a 2 cm-es vonal két oldalán, attól 2–2 cm-re -->
- mérőfolt átmérője: 2 cm (modell)
<!-- forrás: modell – a szenzor egy kis foltot lát a padlón, és annak átlagos világosságát méri; ezért ad a vonal szélén köztes értéket -->
- éles kanyar sugara: 4 cm (modell)
<!-- forrás: modell – a 3. lépés pályájának derékszögű, éles kanyarja -->
- futás hossza: 24 s
<!-- forrás: a lecke beállítása – ennyi ideig fut egy szimuláció a 2., 4–7. lépésben -->

## 1. Fehér vagy fekete?
A robot nem *látja* a vonalat. Alul egy **fényszenzor** méri, mennyi fény verődik vissza: fehér padlón {fehér padló értéke}, fekete vonalon {fekete vonal értéke}. ==Húzd át a robotot a vonalon!== A szélén köztes érték jön. A program **küszöbbel** dönt: {küszöb} alatt „fekete”.

### Feliratok
- közelkép felirat: FELÜLRŐL, NAGYÍTVA
- vonal felirat: fekete vonal, # széles
- folt felirat: ezt a foltot méri
- húzd felirat: Húzd a robotot!
- ennyit lát felirat: A ROBOT CSAK EZT A SZÁMOT KAPJA
- kérdés felirat: # < #? #
- hely tengely: a szenzor helye a vonal közepétől (cm)
- szenzor csúszka: a szenzor helye

## 2. Egy szenzor, két szabály: cikázás
A legegyszerűbb program két szabályból áll: ha **sötétet** mér, balra kanyarodik, ha **világosat**, jobbra. Így a vonal **szélén** halad, és ==cikázik==: a mért érték újra és újra átbillen a küszöbön. Nézd a grafikont!

> megjegyzés: A robot modell: kerékcsúszás, súrlódás, árnyékok és a fény ingadozása nincs benne.

## 3. Gyorsabban?
A robot {robot sebessége} sebességgel beveszi az éles kanyart. ==Mi lesz, ha kétszer olyan gyorsan megy? Tippelj!==

**Lerepül a vonalról.** A robot csak {vezérlési ütem}-onként mér, közben vakon halad. Gyorsabban nagyobb utat tesz meg két mérés között, és a kanyarnál már későn fordul. Próbáld ki a csúszkával!

### Feliratok
- gyors kérdés felirat: Most kétszer olyan gyorsan megy: #. Mi lesz a kanyarban?
- simán tipp: simán beveszi
- lassabban tipp: lassabban ér célba
- lerepül tipp: lerepül a vonalról
- lerepült felirat: lerepült a vonalról!
- bevette felirat: bevette a kanyart
- sebesség felirat: sebesség: #
- ütem felirat: mér: #-onként
- vakon felirat: két mérés között vakon: #
- sötét pötty felirat: itt sötétet mért
- világos pötty felirat: itt világosat mért
- sebesség csúszka: sebesség

## 4. A visszacsatolás köre
Minden ütemben ugyanaz történik: a szenzor **mér**, a program **dönt**, a motorok **mozdulnak**. A mozgás megváltoztatja a következő mérést – ez a ==visszacsatolás==. Itt {lassítás}-szörös lassítással látod, a robot mögül.

### Feliratok
- robot mögött felirat: A ROBOT MÖGÖTT, NAGYÍTVA
- mér most felirat: fény = #
- dönt most felirat: # < #? #
- gyakoriság felirat: # kör másodpercenként

### Adatok
- lassítás: 5
<!-- forrás: a lecke beállítása – a 4. lépés ötödakkora sebességgel játssza le a futást -->

## 5. Két szenzor, négy eset
Most **két szenzor** van, a vonal két oldalán. ==Mindkettő fehéret mér. Merre menjen a robot? Tippelj!==

**Előre** – a vonal épp a két szenzor között van. Ha a **bal** lát feketét, balra kell fordulni, ha a **jobb**, jobbra. Így kevesebbet cikázik, és gyorsabban halad.

### Feliratok
- két kérdés felirat: Mindkét szenzor fehéret mér. Merre menjen?
- előre tipp: előre
- megáll tipp: álljon meg
- fordul tipp: forduljon
- bal mért felirat: bal: #
- jobb mért felirat: jobb: #
- kérdőjel felirat: ?
- jobb fekete felirat: jobb: fekete
- jobb fehér felirat: jobb: fehér
- bal fekete felirat: bal: fekete
- bal fehér felirat: bal: fehér

## 6. Mi lesz a 8-asnál?
A 8-as közepén a vonal keresztezi önmagát. Ott **mindkét szenzor feketét** mér. A program ilyenkor balra fordul, és a robot ==körbe-körbe jár== a bal hurokban. Kell egy **negyedik szabály**: mindkettő fekete → előre. Kapcsold be!

### Feliratok
- kereszteződés felirat: kereszteződés
- szabályok felirat: A SZABÁLYOK
- mindkét hurok felirat: bejárja mindkét hurkot
- csak bal hurok felirat: csak a bal hurokban kering
- három szabály felirat: Mindkettő fekete? Akkor a bal szabály dönt: balra.
- négy szabály felirat: Új szabály: mindkettő fekete → előre.
- három gomb: 3 szabály
- négy gomb: 4 szabály

## 7. Arányos kormányzás
Ügyesebb, ha a robot azt is eldönti, **mennyire** forduljon. Az **arányos** szabály: bal motor = mért fény, jobb motor = 100 − mért fény. A vonal szélén alig fordul, ezért ==nem cikázik==. Lassabban halad, de simán.

### Feliratok
- bal kerék felirat: bal
- jobb kerék felirat: jobb
- két szabály felirat: két szabály: cikázik
- arányos felirat: arányos: sima
- szaggatott felirat: szaggatott: a másik program
- két szabály gomb: két szabály
- arányos gomb: arányos

## 8. Hol van még visszacsatolás?
Visszacsatolás ott van, ahol valami **mér, dönt és beavatkozik**. A termosztát hidegben bekapcsolja a fűtést, melegben kikapcsolja – a hőmérséklet ezért {termosztát beállítása} körül ==ingadozik==. Te is így egyensúlyozol a biciklin.

### Feliratok
- termosztát felirat: EGY TERMOSZTÁT ÉS A SZOBA HŐMÉRSÉKLETE (KITALÁLT PÉLDA)
- beállítás felirat: beállítva: #
- fűtés be felirat: fűtés be
- perc tengely: idő (perc)
- hőmérséklet tengely: hőmérséklet (°C)
- termosztát kártya: Termosztát
- termosztát mér: a szoba hőmérsékletét
- termosztát dönt: hidegebb, mint kéne?
- termosztát mozdul: be- vagy kikapcsolja a fűtést
- kerékpár kártya: Biciklizés
- kerékpár mér: a tested érzi, hogy dőlsz
- kerékpár dönt: merre dőlök?
- kerékpár mozdul: arra kormányzol
- zuhany kártya: Zuhanyozás
- zuhany mér: a bőröd a víz melegét
- zuhany dönt: túl hideg vagy túl meleg?
- zuhany mozdul: tekersz a csapon

### Adatok
- termosztát beállítása: 21 °C (modell)
<!-- forrás: kitalált példa – szokásos szobahőmérséklet-beállítás -->
- kapcsolási sáv: 0,5 °C (modell)
<!-- forrás: kitalált példa – a termosztát a beállítás alatt 0,5 °C-kal kapcsol be, fölötte 0,5 °C-kal ki; valódi készülékeknél ez típusonként más -->
- fűtés melegítése: 0,3 °C/perc (modell)
<!-- forrás: kitalált példa – a görbe alakjához; egy valódi szoba melegedése a fűtéstől, a szoba méretétől és a kinti hidegtől függ -->
- szoba hűlése: 0,15 °C/perc (modell)
<!-- forrás: kitalált példa – mint fent -->
- kezdő hőmérséklet: 19 °C (modell)
<!-- forrás: kitalált példa -->

## 9. Összefoglalás
A vonalkövető robot **egy számot** mér, és ==újra meg újra== dönt: ez a visszacsatolás. Egy szenzorral cikázik, túl gyorsan lerepül. Két szenzorral simábban halad – de minden esetre kell szabály. Az arányos szabály még simább.

### Feliratok
- összegzés felirat: AMIT MEGTANULTUNK
- egy szám kártya: Egy szám, nem kép
- egy szám szöveg: A fényszenzor csak azt méri, mennyire világos a padló. A küszöb dönt: fekete vagy fehér.
- kör kártya: Mér – dönt – mozdul, újra és újra
- kör szöveg: A mozgás megváltoztatja a következő mérést: ez a visszacsatolás.
- gyors kártya: Két mérés között vakon megy
- gyors szöveg: Gyorsabban nagyobb utat tesz meg vakon – az éles kanyarban lerepül.
- két szenzor kártya: Két szenzor, négy eset
- két szenzor szöveg: Simább és gyorsabb, de minden esetre kell szabály – a 8-as kereszteződésére is.

<!-- Tanári megjegyzések és források:
  - A lecke a 07-szenzor folytatása: ott a szenzor fogalma (mit mér, mikor téved), itt a visszacsatolás:
    egy szenzor → cikázás; sebesség és kanyar; két szenzor és az esetek; az arányos szabály ötlete.
  - Tévhitek, amelyekre a lecke épít: „a robot látja a vonalat” (1.); „a robot egyenesen megy a vonalon” (2.);
    „gyorsabb = jobb” (3.); „két szenzor kétszer jobb” – új szabály is kell (5–6.); „visszacsatolás csak
    robotban van” (8.).
  - A robot mozgása a DigRobot modul determinisztikus szimulációja (kéttengelyű kocsi, a kerekek rövid
    átállási idővel). A vezérlési ütem (100 ms) szándékosan lassabb a valódinál, hogy a cikázás látsszon;
    ettől a „lerepül” határsebesség is kisebb, mint egy valódi robotnál. A lényeg (gyorsabban → nagyobb vakon
    megtett út → lerepül) valódi robotokra is igaz.
  - A „lerepült” felirat akkor jelenik meg, ha a szenzor legalább fél másodpercig folyamatosan fehéret lát.
  - A 3. lépésben a lerepülés a kezdőhelytől is függ (a mérések ütemétől a kanyarhoz képest). A lecke
    kezdőhelyén 10–25 cm/s-mal beveszi a kanyart, 30 cm/s-tól lerepül; más kezdőhelyről a határ 20 és
    40 cm/s között bárhol lehet (a 4 cm-es kanyar 20 cm/s-nál már a határon van). Az irány – gyorsabban könnyebben
    lerepül – minden kezdőhelyről igaz.
  - A terv sorrendjétől eltérően a „Két szenzor” a 8-as előtt van (5–6.): a 8-as kereszteződésének gondja
    (mindkét szenzor fekete) csak két szenzorral értelmezhető; egy szenzorral a modellben a robot átjut rajta.
  - Az arányos szabály itt a legegyszerűbb alak (bal = fény, jobb = 100 − fény); a valódi P-szabályozó
    alapsebességgel és erősítéssel dolgozik – ezt nem tanítjuk, csak az ötletet: „mennyire forduljon”.
  - A termosztát görbéje kitalált példa (be/ki kapcsolás egy sáv két szélén) – a számok nem mérésből valók.
-->
