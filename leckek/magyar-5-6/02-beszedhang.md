# Hogyan lesz a levegőből „á”? – beszédszervek, magánhangzók, zönge
tantárgy: Magyar nyelv és irodalom · évfolyam: 5–6. · témakör: 4. A nyelvi szintek: a beszédhang, a fonéma, a szóelemek, a szavak, az összetett szavak

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/magyar-5-6/02-beszedhang.md

  A magánhangzók csoportosítása (a „… lista” feliratok) vezérli a négyszöget: ahová egy betűt
  írsz (magas/mély, felső/középső/alsó, kerek/réses), oda kerül a rajzon, és a 6. lépés kérdéseinek
  megoldását is ebből számolja a lecke. Mind a 14 magánhangzó pontosan egyszer szerepeljen
  mindhárom csoportosításban – ha nem, a lecke piros sávval jelez.
  A formánsok (az „… formánsai” adatok) a gépi hangot és a 3. lépés rajzát vezérlik.
  A hang szintetizált (Web Audio), csak gombra kattintva szól; a lecke hang nélkül is teljes.
  Feliratban a # jel helyére a lecke számot vagy betűt ír.
-->

## Közös

### Feliratok
- modell bélyeg: modell – egyszerűsített rajz
- gépi hang bélyeg: gépi hang – egyszerűsített
- adathiba felirat: Ellenőrizd a .md-t: #
- szólaltasd gomb: Szólaltasd meg!
- tüdő név: tüdő
- légcső név: légcső
- gége név: gége (hangszalagok)
- garat név: garat
- szájüreg név: szájüreg
- orrüreg név: orrüreg
- nyelv név: nyelv
- ajak név: ajak
- fogak név: fogak
- szájpadlás név: szájpadlás
- lágy szájpadlás név: lágy szájpadlás
- magas lista: e, é, i, í, ö, ő, ü, ű
- mély lista: a, á, o, ó, u, ú
- kerek lista: a, o, ó, u, ú, ö, ő, ü, ű
- réses lista: á, e, é, i, í
- felső lista: i, í, u, ú, ü, ű
- középső lista: é, o, ó, ö, ő
- alsó lista: a, á, e
- elöl felirat: elöl képzett = magas
- hátul felirat: hátul képzett = mély
- felső felirat: felső
- középső felirat: középső
- alsó felirat: alsó
- kerek felirat: ajakkerekítéses
- réses felirat: ajakréses
- legközelebbi felirat: a legközelebbi: #
- húzd felirat: Húzd a nyelvet!
- alaphang csúszka: A zönge rezgésszáma

### Adatok
<!-- A magyar köznyelvi magánhangzók formánsainak tájékoztató adatai, Hz-ben (F1; F2; F3):
     Gósy Mária: Fonetika, a beszéd tudománya. Osiris, Budapest, 2004, 116. o., 20. táblázat.
     A könyv szerint „a szemléltetést szolgálják”, határértékek nélkül; a beszélő neme nincs megadva
     (a mellette lévő hangszínkép férfi bemondóé). Nők és gyerekek formánsai magasabbak (rövidebb a
     hangcsatornájuk). A rövid és hosszú párt a táblázat külön méri; a lecke a négyszögben egy helyre
     teszi őket (a tankönyvi rendszer szerint), a hangjuk az itt megadott értékekből szól. -->
- i formánsai: 280; 2400; 3000 Hz
- í formánsai: 260; 2500; 2850 Hz
- é formánsai: 420; 2100; 2800 Hz
- e formánsai: 550; 1900; 2500 Hz
- ü formánsai: 280; 1750; 2200 Hz
- ű formánsai: 260; 1800; 2150 Hz
- ö formánsai: 380; 1600; 2400 Hz
- ő formánsai: 400; 1550; 2500 Hz
- á formánsai: 800; 1400; 2500 Hz
- a formánsai: 600; 1100; 2400 Hz
- o formánsai: 450; 900; 2300 Hz
- ó formánsai: 400; 950; 2300 Hz
- u formánsai: 300; 650; 2300 Hz
- ú formánsai: 280; 600; 2100 Hz
<!-- A formánsok sávszélessége (a gépi hang „élessége”): Gósy 2004, 5. fejezet: B1 = 50–98 Hz,
     B2 = 62–106 Hz, B3 = 96–255 Hz; a lecke ezekből egy-egy értéket választ. -->
- sávszélességek: 80; 90; 150 Hz
<!-- A gépi hang alaphangja (a zönge rezgésszáma): egy felnőtt férfihang tartományában. -->
- gépi alaphang: 120 Hz
<!-- Felnőtt férfi és nő: Gósy 2004 (idézi: Deme Andrea: Óvodások magánhangzóinak akusztikai jellemzői,
     in: Beszédtudomány, 2014, 77–99., 1. táblázat); 6–7 éves gyerekek átlaga (4 fiú, 4 lány): ugyanott,
     280 Hz. 10–12 évesekre nem találtunk magyar mérést. -->
- férfi alaphang: 80–148 Hz
- női alaphang: 166–240 Hz
- gyerek alaphang: kb. 280 Hz

## 1. Honnan jön a hang?
Tedd a kezed a torkodra, és mondd: *ááá*! Érzed a rezgést? A hang útja: a **tüdő** levegőt fúj, a **gégében** rezegnek a hangszalagok, a **szájüreg** és az **orrüreg** formálja a hangot. ==A hang nem a szájban születik==, a száj csak alakítja.

### Feliratok
- kövesd gomb: Kövesd a levegőt!
- á gomb: Szólaltasd meg: á
- út felirat: a levegő útja

## 2. A hangszalag rezeg: zönge
A gégében két izmos redő ül: a **hangszalagok**. Ha összezárnak, a levegő szétfeszíti őket, aztán visszacsapódnak. Így rezegnek, másodpercenként több százszor is. Ez a **zönge**. ==Gyorsabb rezgés = magasabb hang.== De a zönge még nem *á*, csak zümmögés.

### Feliratok
- zönge gomb: Szólaltasd meg a zöngét!
- suttog gomb: Zönge ki: suttogás
- zönge be gomb: Zönge be
- felülnézet felirat: a hangszalagok felülről
- hangrés felirat: hangrés
- lassítva felirat: lassítva
- rezgés felirat: másodpercenként # rezgés
- férfi felirat: felnőtt férfi
- nő felirat: felnőtt nő
- gyerek felirat: 6–7 éves gyerek
- suttogás felirat: nyitott hangrés: nincs zönge
- zümm felirat: zönge: zümmögés

## 3. A száj mint szűrő
Ugyanaz a zönge szól, csak a száj alakja más, és mégis más hangot hallasz! A száj **szűrő**: egyes hangmagasságokat felerősít, másokat elnyel. A felerősített sávok a „hegyek”. ==A hegyek helye dönti el, melyik magánhangzót halljuk.==

> megjegyzés: A szakkönyvek a hegyeket **formánsoknak** hívják.

### Feliratok
- á3 gomb: á
- i3 gomb: i
- u3 gomb: u
- zönge sor felirat: 1. a zönge: sok egyforma lépcső
- szűrő sor felirat: 2. a száj szűrője
- eredmény sor felirat: 3. ami kijön: #
- hegy felirat: hegy
- frekvencia felirat: hangmagasság (Hz)

## 4. Elöl vagy hátul?
Húzd a nyelvet előre és hátra! Ha a nyelv **elöl** emelkedik, **magas** magánhangzó szól (*i, é, ü*), ha **hátul**, **mély** (*u, o, a*). ==A „magas” itt a nyelv helyét jelenti, nem a hangmagasságot:== az *i* mély hangon is *i*.

### Feliratok
- csúszás gomb: Csúsztasd: i → u
- húzás hang gomb: Hang húzás közben
- húzás hang ki gomb: Hang ki

## 5. Kerek vagy réses ajak?
Mondd: *i*! Most kerekítsd az ajkad, de a nyelved maradjon: *ü* lesz belőle! Az ajak lehet **kerek** (*o, u, ö, ü*) vagy **réses** (*i, é, e*). Az *a* kerek, az *á* réses és nyíltabb. ==Az *á* nem a hosszú *a*:== más a hangszíne.

### Feliratok
- kerekítsd gomb: Kerekítsd az ajkad!
- réses gomb: Réses ajak
- a5 gomb: a
- á5 gomb: á
- elölnézet felirat: az ajak elölről
- nem hosszú felirat: más a helye, más a hangja

## 6. Fent, középen, lent
A nyelv lehet **felső**, **középső** vagy **alsó** helyzetben: minél lejjebb van, annál nyitottabb a száj. Az *i–í*, *o–ó* párok tagjai csak **hosszúságban** különböznek. ==Kattints a négyszög betűire!==

> megjegyzés: Más tankönyvben ezt másképp is csoportosíthatják.

### Feliratok
- kérdés 1: Melyik felső nyelvállású és kerek?
- kérdés 2: Melyik alsó nyelvállású?
- kérdés 3: Melyik magas és középső?
- kérdés 4: Melyik mély és réses?
- másik kérdés gomb: Másik kérdés
- megoldás gomb: Mutasd a megoldást!
- jó felirat: Jó! Még # hiányzik.
- kész felirat: Megvan mind: #
- rossz felirat: A(z) # nem ilyen.
- hosszú pár felirat: rövid – hosszú: ugyanott, csak tovább tart

## 7. Zöngés vagy zöngétlen?
A **mássalhangzónál** a levegő akadályba ütközik: résen súrlódik, és **zörej** keletkezik. Ha közben a hangszalag is rezeg, a hang **zöngés** (*z, v, zs*), ha nem, **zöngétlen** (*sz, f, s*). ==Tedd a kezed a torkodra: zzz – szsz!==

### Feliratok
- sz-z gomb: sz – z
- f-v gomb: f – v
- s-zs gomb: s – zs
- zönge kapcsoló gomb: Zönge be / ki
- zörej felirat: zörej
- zöngés felirat: zöngés: #
- zöngétlen felirat: zöngétlen: #
- rezeg felirat: a hangszalag rezeg
- nem rezeg felirat: a hangszalag nem rezeg
- párok cím: zöngés – zöngétlen párok
- párok lista: b–p, d–t, g–k, gy–ty, v–f, z–sz, zs–s, dz–c, dzs–cs
- pár nélküli felirat: pár nélküli zöngés: j, l, m, n, ny, r · zöngétlen: h
- szópárok cím: a zönge szót választ el
- szópárok lista: zár – szár, vér – fér, zsír – sír, gép – kép
<!-- A zörej sávja Gósy 2004 (5. fejezet, réshangok) szerint: sz, z: 4000–5000 Hz fölött intenzív,
     8000 Hz-ig; s, zs: 2000–4000 Hz; f: szinte a teljes sávban (1000–8000 Hz), gyengén. -->

### Adatok
- sz zörejsávja: 4000–8000 Hz
- s zörejsávja: 2000–4000 Hz
- f zörejsávja: 1000–8000 Hz

## 8. Összefoglaló
A **tüdő** levegőt ad. A **gégében** a hangszalagok rezgése a **zönge**. A **szájüreg** a szűrő: a nyelv **elöl vagy hátul**, **fent vagy lent** áll, az ajak **kerek vagy réses**. A mássalhangzónál akadály van: ==zörej, zöngével vagy anélkül.==

### Feliratok
- össz levegő: levegő
- össz zönge: zönge (vagy nincs)
- össz szűrő: szájüreg: a szűrő
- össz magánhangzó: magánhangzó: szabad út
- össz mássalhangzó: mássalhangzó: akadály, zörej

<!-- Vitatott / bizonytalan pontok (tanári review):
  - Tankönyvi rendszer: a csoportosítás a terv szerinti 5. osztályos rendszer (magas: e é i í ö ő ü ű;
    mély: a á o ó u ú; ajakkerekítéses: a o ó u ú ö ő ü ű; ajakréses: á e é i í; alsó: a á e; középső:
    é o ó ö ő; felső: i í u ú ü ű). Az á-t egyes tankönyvek „középső helyzetű” (elöl és hátul között
    képzett) hangnak veszik; a mérések szerint (Gósy 2004, 20. táblázat: F2 = 1400 Hz) valóban előrébb
    képzett, mint az a (1100 Hz). Ha a választott tankönyv másképp csoportosít, a fenti listákat
    kell átírni – a négyszög és a kérdések ehhez igazodnak. A 6. lépés megjegyzése kimondja, hogy más
    tankönyv másképp is csoportosíthat.
  - A négyszög a tankönyvi (képzési) rendszert rajzolja, nem a mért formánsokat: a pötty helye a
    nyelv modellbeli helye. A formánsok csak a gépi hangot és a 3. lépés görbéit vezérlik.
  - A fejmetszet saját, egyszerűsített rajz („modell” bélyeg): a nyelv egy görbe, az állkapocs egy pont
    körül fordul, a hangszalagok felülnézete vázlat. A hangszalagok rezgése a rajzon lassított.
  - A gépi hang forrás–szűrő modell: fűrészfog-zönge és három (+ egy rögzített) rezonátor. A rövid–hosszú
    párokat a lecke nem nyújtja meg külön (a hang hossza a gombtól függ).
  - Zöngés–zöngétlen párok (9) és pár nélküliek: a terv szerinti tankönyvi besorolás; a h-t a lecke
    zöngétlennek mondja (két magánhangzó között zöngésen is ejthető – ezt a lecke nem tárgyalja).
  - A szópárok (zár – szár, vér – fér, zsír – sír, gép – kép) saját példák.
  - Alaphang: a 10–12 évesekre magyar mérést nem találtunk; a lecke a 6–7 évesek átlagát (Deme 2014) és
    a felnőtt tartományokat (Gósy 2004) mutatja.
-->
