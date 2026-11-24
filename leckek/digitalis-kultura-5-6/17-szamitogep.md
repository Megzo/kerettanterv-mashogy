# Mi történik, ha lenyomod az „A” betűt? – a gép részei, bit, bájt, fájl, mappa
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 8. A digitális eszközök használata

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/17-szamitogep.md

  A „Tippelj!” lépésekben (3. és 6.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
  A ## Közös feliratai: a „Tippelj! → kísérlet → magyarázat” sáv, a tipp-visszajelzés és a bélyegek
  (szerződés 17. és 19.) – a sorozat minden leckéjében ugyanígy szerepelnek.
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
- kitalált bélyeg: kitalált példa
- sematikus bélyeg: sematikus rajz
- nagyítás bélyeg: nagyítás · szemléltetés
- billentyűzet felirat: billentyűzet
- processzor felirat: processzor
- memória felirat: memória
- háttértár felirat: háttértár
- képernyő felirat: képernyő
- gépház felirat: a gépház belülről
- bájt egység felirat: bájt

### Adatok
- az A kódja: 65
<!-- forrás: ASCII (ISO/IEC 646, ANSI X3.4-1968) – a nagy A kódja 65 (hexadecimálisan 41); a Unicode első 128 jele ugyanez (U+0041) -->
- a B kódja: 66
<!-- forrás: ASCII / Unicode U+0042 -->
- egy bájt bitjei: 8 bit
<!-- forrás: IEC 80000-13:2008 (1 bájt = 8 bit; ma ez az általános jelentés) -->

## 1. Egy gombnyomás útja
Lenyomod az „A” billentyűt, és ==egy szempillantás alatt== ott a betű a képernyőn. Közben a gépben négy állomáson fut végig. Kövesd lassítva!

> megjegyzés: A billentyűzet csak azt jelzi, melyik gombot nyomtad. Hogy az „A” betű, azt a gép programja dönti el.

<!-- „egy szempillantás alatt”: becslés – a billentyűleütéstől a kijelzésig tipikusan néhány tíz ezredmásodperc
     telik el, a pislogás kb. 100–400 ms. A lecke ezt nem számszerűsíti. -->

### Feliratok
- állomás 1 felirat: 1. A billentyű jelet küld a kábelen.
- állomás 2 felirat: 2. A processzor kikeresi a kódját: #.
- állomás 3 felirat: 3. A kód a memóriába kerül: 8 bit.
- állomás 4 felirat: 4. A képernyőn kigyulladnak a pixelek.
- a gomb: Nyomd le az „A”-t!
- b gomb: Nyomd le a „B”-t!
- a kódja felirat: „#” = #
- pixelek felirat: a betű pixelei – nagyítva
- kattints billentyű felirat: kattints az A vagy a B billentyűre!

## 2. Bemenet, feldolgozás, kimenet
A gép a **bemeneti** eszközökön át kap adatot. A **processzor** feldolgozza, a **kimeneti** eszköz megmutatja, a **háttértár** megőrzi. A gépházon kívüli eszközök a **perifériák**. ==Húzd a kártyákat a helyükre!==

> megjegyzés: Kérdezd meg: mi lehet bemenet és kimenet egyszerre?

### Feliratok
- periféria kérdés felirat: Melyik csoportba tartozik?
- bemenet zóna felirat: bemenet
- bemenet alcím felirat: adatot ad a gépnek
- kimenet zóna felirat: kimenet
- kimenet alcím felirat: megmutatja az eredményt
- mindkettő zóna felirat: mindkettő
- mindkettő alcím felirat: be és ki is
- háttértár zóna felirat: háttértár
- háttértár alcím felirat: megőrzi az adatot
- billentyűzet kártya: billentyűzet
- egér kártya: egér
- mikrofon kártya: mikrofon
- szkenner kártya: szkenner
- monitor kártya: monitor
- hangszóró kártya: hangszóró
- nyomtató kártya: nyomtató
- érintőképernyő kártya: érintőképernyő
- okostábla kártya: okostábla
- pendrive kártya: pendrive
- merevlemez kártya: merevlemez
- memóriakártya kártya: memóriakártya
- megoldás gomb: Mutasd a megoldást!
- jó helyen felirat: jó helyen: # / #
- monitor tévhit felirat: A monitor maga a számítógép?
- monitor válasz felirat: Nem: csak kimenet. A gép a gépházban számol.
- memóriakártya tévhit felirat: A memóriakártya memória?
- memóriakártya válasz felirat: Nem: háttértár – kikapcsolva is megőriz.
- bemenet nyíl felirat: bemenet
- feldolgozás nyíl felirat: feldolgozás
- kimenet nyíl felirat: kimenet

## 3. Bit és bájt
A gépben minden **bit**: 0 vagy 1, mint egy kapcsoló. Nyolc bit egy **bájt**. ==Hány különböző értéket tud 8 kapcsoló? Tippelj!==

Minden új kapcsoló ==megkétszerezi== a lehetőségeket: `2^8 = 256`. Kattints a lámpákra! A szám, a betű és a szürke árnyalat együtt változik.

### Feliratok
- kapcsoló kérdés felirat: Hány különböző értéket tud 8 kapcsoló?
- nyolc tipp: 8
- tizenhat tipp: 16
- kétszázötvenhat tipp: 256
- egy bájt felirat: 8 bit = 1 bájt
- érték felirat: szám
- betű felirat: betű
- szürke felirat: szürke árnyalat
- nem betű felirat: nem betű
- szóköz felirat: szóköz
- lehetőség felirat: # bit
- számlál felirat: a gép végigszámol: 0, 1, 2 … #
- kattints lámpa felirat: Kattints a lámpákra!
- lehetőségek felirat: 8 bit: # különböző érték

### Adatok
- egy bájt értékei: 256
<!-- forrás: számolt – 2^8 = 256 (0-tól 255-ig); a lecke L.checks()-e ellenőrzi -->

## 4. A betű is szám
A gép nem betűt tárol, hanem **számot**. Egy **kódtábla** mondja meg, melyik szám melyik betű: „A” = {az A kódja}. ==Az ékezetes betű viszont két bájt!== Válassz egy szót, és számold meg a bájtjait!

> megjegyzés: A ma használt kódtábla a Unicode. Az első 128 jele a régi ASCII.

### Feliratok
- kódtábla felirat: kódtábla
- szia gomb: Szia!
- kőfal gomb: kőfal
- tűz gomb: tűz
- kód felirat: kód
- bájtok felirat: bájtok
- két bájt felirat: 2 bájt
- számlálás felirat: # betű → # bájt
- ékezet tévhit felirat: Az „ő” is egy bájt?
- ékezet válasz felirat: Nem: két bájt.
- betű tévhit felirat: A gép betűket tárol?
- betű válasz felirat: Nem: számokat – a kódtábla tesz betűt belőlük.

## 5. Mennyi az a gigabájt?
A bájtokból nagyobb egységek lesznek, ==mindig ezres lépcsőkkel==: 1 **kB** (kilobájt) = 1000 bájt, mint a kilométerben. Aztán MB, GB, TB. Húzd a csúszkát: mennyi fér el?

> megjegyzés: Egyes gépek 1024-gyel váltanak (ennek pontos neve kibibájt, KiB), ezért kevesebbet írnak ki.

### Feliratok
- létra cím felirat: Ezres lépcsők
- szorzó felirat: × 1000
- egy betű példa felirat: 1 betű
- egy oldal példa felirat: 1 oldal szöveg
- egy fotó példa felirat: 1 telefonfotó
- egy film példa felirat: 1 film
- sok fotó példa felirat: # fotó
- tárhely csúszka: Mekkora a tárhely?
- elfér felirat: Ennyi fér el # tárhelyen:
- betű darab felirat: betű
- oldal darab felirat: oldal szöveg
- fotó darab felirat: telefonfotó
- film darab felirat: film (2 óra)
- egy sem felirat: egy sem

### Adatok
- egy oldal szöveg mérete: kb. 2 kB
<!-- forrás: becslés – egy gépelt oldal kb. 1800–2000 karakter (a „szerzői ív” 40 000 karakter = 22 oldal × 1800),
     karakterenként 1 bájt (az ékezetes betű 2 bájt) → kb. 2 kB; formázás nélküli szövegfájl -->
- egy telefonfotó mérete: kb. 3 MB
<!-- forrás: becslés – egy 12 megapixeles telefonfotó JPEG-ben tipikusan 2–5 MB (a terv 13-pixel és 05-csomagok
     leckéjével azonos konstans) -->
- egy film mérete: kb. 4 GB
<!-- forrás: becslés – egy 2 órás Full HD film tömörítve kb. 2–5 GB (pl. 4,5 Mbit/s · 7200 s ≈ 4 GB) -->

## 6. Memória és háttértár
Írsz egy fogalmazást, és mentés nélkül elmegy az áram. ==Mi marad meg az új szövegből? Tippelj!==

A **memória** gyors, de kikapcsoláskor kiürül. A **háttértár** megőrzi, amit **mentettél**.

> megjegyzés: Neumann János {Neumann-jelentés éve}-ös leírása szerint a program is a memóriában van.

### Feliratok
- áram kérdés felirat: Mentés nélkül elmegy az áram. Mi marad meg az új szövegből?
- minden tipp: minden
- semmi tipp: semmi
- fele tipp: a fele
- gépelj gomb: Gépelj tovább!
- mentés gomb: Mentés
- áramszünet gomb: Áramszünet
- mentett szöveg felirat: Nyári élményeim.
- új szöveg felirat: A Balatonnál voltunk, és minden nap úsztunk egy nagyot.
- fájl neve felirat: fogalmazas.txt
- gyors felirat: gyors, munka közben tárol
- megőriz felirat: kikapcsolva is megőriz
- áram van felirat: áram: van
- áram nincs felirat: áramszünet!
- mentetlen felirat: nincs mentve: # karakter
- minden mentve felirat: minden mentve
- mentés nyíl felirat: mentés
- üres felirat: üres
- melyik felirat: „Van 8 GB-om.” – De melyikből?
- példagép felirat: egy példagép: memória #, háttértár #

### Adatok
- példagép memóriája: 8 GB
<!-- forrás: kitalált példa (egy mai átlagos laptop nagyságrendje) -->
- példagép háttértára: 512 GB
<!-- forrás: kitalált példa -->
- Neumann-jelentés éve: 1945
<!-- forrás: J. von Neumann: First Draft of a Report on the EDVAC, Moore School, University of Pennsylvania, 1945. június 30.
     A tárolt program elvét a jelentés írja le; a gondolatban J. P. Eckert és J. W. Mauchly is részt vett – ezért a
     panel „leírása szerint”, nem „feltalálta”. -->

## 7. Fájl, mappa, elérési út
A **fájl** névvel ellátott adat. A **mappák** fába rendezik. Az **elérési út** a fa egy ága: ==a pirosan kiemelt út==. Próbáld ki a fájlműveleteket! A **felhő** ugyanilyen fa, csak egy másik gépen.

> megjegyzés: A törölt fájl először a Lomtárba kerül – onnan még visszahozható.

### Feliratok
- dokumentumok mappa felirat: Dokumentumok
- iskola mappa felirat: Iskola
- szabadidő mappa felirat: Szabadidő
- digitális kultúra mappa felirat: Digitális kultúra
- rajz mappa felirat: Rajz
- fotók mappa felirat: Fotók
- plakát fájl felirat: plakat.docx
- jegyzet fájl felirat: jegyzet.txt
- nyaralás fájl felirat: nyaralas.jpg
- tó fájl felirat: to.jpg
- üres mappa felirat: (üres mappa)
- elérési út felirat: elérési út:
- lomtár felirat: Lomtár
- lomtár üres felirat: üres
- lomtár alcím felirat: innen még visszahozható
- felhő felirat: Felhő – egy másik gépen
- közös mappa felirat: Közös projekt
- megosztás felirat: Bence: megtekintheti
- háttértár blokkok felirat: a háttértár (blokkok)
- szabad blokk felirat: szabad
- másolás gomb: Másolás a Rajz mappába
- áthelyezés gomb: Áthelyezés
- törlés gomb: Törlés
- ürítés gomb: Lomtár ürítése
- alaphelyzet gomb: Alaphelyzet
- másolás hír felirat: Másolás: új bájtok, új hely a háttértáron.
- áthelyezés hír felirat: Áthelyezés: a bájtok maradtak, csak a fa változott.
- törlés hír felirat: Törlés: a Lomtárba került, a bájtok még ott vannak.
- ürítés hír felirat: Ürítés: a hely felszabadult.
- doboz tévhit felirat: A fájl a mappában „dobozban” van?
- doboz válasz felirat: Nem: a mappa csak a fa egy ága.

## 8. A gép és a tested
Figyelj a testedre a gép előtt! A képernyő legyen kb. **karnyújtásnyira**, a teteje ==szemmagasságban vagy kicsit lejjebb==. A lábad érje a földet. Óránként tarts **szünetet**: állj fel, nézz a távolba! Húzd a csúszkákat!

> megjegyzés: Ezt hívják **ergonómiának**.

### Feliratok
- távolság csúszka: A képernyő távolsága
- magasság csúszka: A képernyő teteje a szemedhez képest
- távolság jó felirat: távolság: # – jó
- távolság közel felirat: távolság: # – túl közel
- távolság messze felirat: távolság: # – túl messze
- magasság jó felirat: magasság: jó
- magasság magas felirat: túl magasan: hátrahajlik a fejed
- magasság alacsony felirat: túl alacsonyan: előregörnyedsz
- láb felirat: talp a földön
- szünet felirat: óránként # szünet: állj fel, nézz a távolba!
- karnyújtás felirat: karnyújtásnyira

### Adatok
- képernyő legkisebb távolsága: 50 cm
<!-- forrás: OSHA eTools, Computer Workstations – Monitors: a képernyő kb. 20–40 hüvelyk (51–102 cm) távolságra
     a szemtől, „legalább karnyújtásnyira”; kerekítve 50–100 cm (gyerekeknél a karnyújtás rövidebb: a lecke a
     tartomány alját is jónak veszi) -->
- képernyő legnagyobb távolsága: 100 cm
<!-- forrás: OSHA eTools, Computer Workstations – Monitors (20–40 hüvelyk ≈ 51–102 cm) -->
- képernyő teteje legfeljebb a szem alatt: 15 cm (modell)
<!-- forrás: OSHA eTools – „a képernyő teteje szemmagasságban vagy kicsit alatta”; a 15 cm a lecke modellje
     (nem szabványszám) -->
- szünet óránként: 10 perc
<!-- forrás: 50/1999. (XI. 3.) EüM rendelet a képernyő előtti munkavégzés minimális egészségügyi és biztonsági
     követelményeiről, 4. § (1): óránként legalább tízperces szünet – felnőtt munkavállalókra vonatkozik; a lecke
     ajánlásként veszi át -->

## 9. Összefoglalás
A **bemenet** adatot ad, a **processzor** feldolgozza, a **memória** munka közben tárol, a **háttértár** megőriz, a **kimenet** megmutat. Minden adat **bit**: 8 bit = 1 bájt. A fájlok mappák fájában élnek. ==Ments gyakran!==

### Feliratok
- összefoglaló cím felirat: Ami a gépben történik
- összegzés bájt felirat: 8 bit = 1 bájt = # érték
- összegzés A felirat: „A” = # = #
- összegzés kilo felirat: 1 kB = 1000 bájt
- összegzés mentés felirat: mentés: memória → háttértár
- összegzés út felirat: elérési út: a mappafa egy ága

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a példagép (8 GB memória, 512 GB háttértár), a fogalmazás szövege, a mappafa és a fájlnevek,
    Bence (megosztás a felhőben). A vásznon „kitalált példa” bélyeg.
  - Modell-egyszerűsítések: az 1. lépés útja (billentyű → processzor → memória → képernyő) erősen egyszerűsített és
    lassított. A valóságban a billentyűzet csak a lenyomott gomb helyének kódját küldi; az operációs rendszer a
    beállított kiosztás (magyar, angol) és a Shift szerint rendeli hozzá a betűt; a betű képét a program a betűtípusból
    rajzolja a képernyő memóriájába. A képernyőn a pixelek a nagyított betű 5 × 7-es rácsa (sematikus).
  - A 3. lépésben a „szürke árnyalat”: ha a bájt egy kép pixelének világossága, 0 = fekete, 255 = fehér. Ugyanaz a
    bájt lehet szám, betű vagy szín – a program dönti el, minek veszi.
  - A kettes számrendszer a matematika-5-6/02-helyi-ertek 8. lépésében (13 = 1101) is szerepel; itt a kapcsoló és a
    kód felől közelítünk, a helyiérték-táblát nem ismételjük.
  - Kódtábla: a vásznon „kódtábla”; a mai szabvány a Unicode, a fájlokban leggyakrabban UTF-8 kódolással. Az „A” =
    65 (U+0041), az „ő” = 337 (U+0151) → UTF-8-ban két bájt: C5 91 (11000101 10010001), az „ű” U+0171 → C5 B1. Régi
    (egybájtos, pl. Latin-2) kódtáblákban az „ő” egy bájt volt – innen a régi levelekben látott „Å‘”-féle
    betűhibák.
  - Mértékegységek: 1 kB = 1000 bájt, 1 MB = 1000 kB… (SI-előtagok, IEC 80000-13). Az 1024-es lépcső neve kibibájt
    (KiB), mebibájt (MiB), gibibájt (GiB). Egyes operációs rendszerek a 1024-es értéket „KB”, „GB” jellel írják ki –
    ezért mutat egy 64 GB-os pendrive kb. 59,6 „GB”-ot (64 · 10⁹ / 2³⁰ ≈ 59,6). A „B” a bájt, a „b” a bit jele.
  - A létra példái becslések (egy oldal szöveg kb. 2 kB, egy telefonfotó kb. 3 MB, egy 2 órás film kb. 4 GB); a
    darabszámokat a lecke ezekből számolja, ezért „kb.”.
  - Neumann János (1903–1957): az 1945-ös EDVAC-jelentés írja le a tárolt programú gépet (a program és az adat
    ugyanabban a memóriában); a gondolat kidolgozásában Eckert és Mauchly is részt vett.
  - Fájlműveletek: az áthelyezés ugyanazon a háttértáron belül csak a mappafát írja át (a bájtok helyben maradnak);
    másik meghajtóra áthelyezve valójában másolás + törlés történik. A végleges törlés után a hely „szabad” lesz – az
    adat addig a háttértáron maradhat, amíg felül nem írják (ezért nem „semmisül meg” azonnal). A Lomtár neve
    rendszerenként eltér (Kuka). Az elérési út elválasztójele rendszerenként más (/ vagy \); a lecke „/”-t mutat.
  - Felhő: a megosztásnál a jogosultság (megtekintés, szerkesztés) dönti el, ki mit tehet; részletesen a
    05-csomagok lecke.
  - Ergonómia: OSHA eTools (Computer Workstations – Monitors): a képernyő kb. 50–100 cm-re, a teteje szemmagasságban
    vagy kicsit alatta. A szünet: 50/1999. (XI. 3.) EüM rendelet 4. § (1) – óránként legalább 10 perc (felnőtt
    munkavállalókra kötelező; gyerekeknek ajánlásként). A „20-20-20” szabályt a lecke nem használja.
  - Az órán használt gépen a mappák, a Lomtár és a felhő a fájlkezelőben máshogy néz ki; a lecke a fogalmat mutatja.
-->
