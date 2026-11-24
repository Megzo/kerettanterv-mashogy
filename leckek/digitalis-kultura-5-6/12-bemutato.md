# Mit lát a hátsó sor? – a jó diakocka
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 5. Bemutatókészítés

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/12-bemutato.md

  A „Tippelj!” lépésekben (1., 2.) a panel első bekezdése a kérdés; a többi bekezdés
  elmosódva látszik, és csak a tipp után válik olvashatóvá.
  A számolt értékeket (látószög, olvasható-e, kontrasztarány, hány szó fér el, mekkora betű)
  a lecke az alábbi adatokból számolja – kézzel ne írd be őket.
  A „#” jel helyére a lecke számot ír.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- modell bélyeg: modell – egyszerűsítve
- kitalált bélyeg: kitalált kiselőadás
- sematikus bélyeg: sematikus rajz – nem a te programod
- dia cím: A méhek
- dia pont 1: Virágport gyűjtenek
- dia pont 2: Viaszból lépet építenek
- dia pont 3: Tánccal mutatják az utat
- kulcsszó 1: virágpor
- kulcsszó 2: lép
- kulcsszó 3: tánc
- dia bekezdés: A mézelő méhek nagy családokban élnek, kaptárban vagy faodúban. Egy családban egy anya és sok ezer dolgozó él, nyáron herék is. A dolgozók virágról virágra repülnek, nektárt és virágport gyűjtenek. A nektárból mézet készítenek, a virágporral a fiatal méheket etetik. Közben beporozzák a virágokat, ezért sok gyümölcs és zöldség az ő munkájuk nyomán terem. A lépet a dolgozók a testükben termelt viaszból építik, hatszög alakú sejtekből. Ha egy méh jó virágos helyet talál, a kaptárban táncol: a tánc iránya és hossza megmutatja a többieknek, merre és milyen messze van az élelem.
- kényelmes felirat: kényelmesen olvasható
- alig felirat: csak erőlködve
- nem felirat: nem olvasható

### Adatok
- vászon szélessége: 2 m
<!-- forrás: kitalált példa – egy kisebb tanterem vetített képe (16 : 9, kb. 90 hüvelykes átló). Nagyobb vásznon minden betű arányosan nagyobb. -->
- dia szélessége: 338,67 mm
<!-- forrás: a szélesvásznú (16 : 9) dia gyakori alapmérete 13,333 × 7,5 hüvelyk = 338,67 × 190,5 mm. A pontban megadott betűméret ehhez a lapmérethez képest számít; más diaméretnél ugyanaz a pontszám más arányt jelent (a DigDoc modul is ezt a méretet használja). -->
- első sor távolsága: 2 m
<!-- forrás: kitalált példa – egy 9 m mély tanterem első padsora. -->
- középső sor távolsága: 5 m
<!-- forrás: kitalált példa – a terem közepe. -->
- hátsó sor távolsága: 9 m
<!-- forrás: kitalált példa – a terem hátsó padsora. -->
- szem felbontása: kb. 1 szögperc
<!-- forrás: a „normál” látásélesség (Snellen 6/6, 20/20) definíciója: a betű egy vonása 1 szögperc, a betű 5 szögperc magas. Sok fiatal ennél élesebben lát – a modell a szokásos viszonyítási értéket használja. -->
- olvashatóság határa: 5 szögperc
<!-- forrás: Snellen-tábla (a 6/6-os betű 5 szögperc), illetve Sloan M-egysége (1 M: a kisbetű magassága 1 m-ről 5 szögperc); folyó szöveghez a kisbetű (x) magassága számít. A lecke a kisbetű magasságát a betűtípusból méri. -->
- kényelmes olvasás: kb. 10 szögperc (becslés)
<!-- forrás: becslés – folyékony olvasáshoz a határméretnél nagyobb betű kell („olvasási tartalék”, acuity reserve: Whittaker és Lovie-Kitchin 1993, Optometry and Vision Science 70: 54–65; gyakori klinikai érték kb. 2-szeres, 0,3 log-egység: Cheong, Lovie-Kitchin és Bowers 2002). Gyengénlátóknál ennél sokkal több is kellhet. -->
- kontraszthatár: 4,5 : 1
<!-- forrás: W3C WCAG 2.2, 1.4.3 Kontraszt (minimum), AA szint: normál méretű szövegnél legalább 4,5 : 1 (nagy betűnél 3 : 1). A kontrasztarány képlete és a relatív világosság (sRGB) definíciója a WCAG fogalomtárában (w3.org/TR/WCAG22, megtekintve: 2026. 11. 24.). -->

## 1. Mire való a dia?
==Tippelj! Melyik diáról emlékszel többre az előadás után?==

A **prezentáció** a beszédedet segíti. Sok szövegnél a közönség egyszerre olvas és hallgat: két szöveg tolong. ==Kép és kevés szó: a kép külön úton jut be.==

> megjegyzés: A lecke is ilyen: kép a vásznon, kevés szöveg a panelen.

### Feliratok
- emlékezet kérdés felirat: Melyik diáról emlékszel többre az előadás után?
- sok szöveg tipp: sok szöveg
- kép tipp: kép + három szó
- egyforma tipp: egyforma
- beszéd felirat: a te hangod
- fül felirat: fül
- szem felirat: szem
- szavak útja felirat: szavak útja
- képek útja felirat: képek útja
- emlékezet felirat: emlékezet
- hallott szó felirat: hallott szó
- olvasott szó felirat: olvasott szó
- kép jel felirat: kép
- tolongás felirat: két szövegfolyam egy úton – sok elvész
- külön út felirat: a kép külön úton jut be

<!-- forrás (a modellhez): R. E. Mayer: Multimedia Learning (3. kiadás, Cambridge University Press, 2021) – két csatorna (szavak és képek) korlátozott befogadóképességgel; a redundancia-elv: kép + beszéd mellett a teljes szöveg kiírása többnyire nem segít; a koherencia-elv: a fölösleges szöveg elhagyása segít. A lecke modellje erősen egyszerűsít (nincs benne szám, csak az irány). A panel óvatosan fogalmaz: az eredmény átlagos hatás, nem mindenkire igaz. -->

## 2. Mit lát a hátsó sor?
==Tippelj! Elolvasható-e {hátsó sor távolsága} távolságból a {tipp betűmérete} méretű betű?==

Messzebbről a betű **kisebbnek látszik**: kisebb a **látószöge**. A szem felbontása {szem felbontása} (a fok 60-ad része). ==A kisbetűnek legalább {olvashatóság határa} kell, kényelmesen {kényelmes olvasás}.== Húzd a betűméretet!

### Feliratok
- olvasható kérdés felirat: Elolvasható-e # m-ről a # pontos betű?
- igen tipp: igen
- alig tipp: alig
- nem tipp: nem
- vászon felirat: vászon
- sor felirat: # m
- nézet felirat: # m-ről így látod
- takarás felirat: Előbb tippelj!
- betűméret sor: a dia betűmérete: # pont
- határ sor: határ (# szögperc) # m-ről: # mm
- kisbetű sor: kisbetű a vásznon: # mm
- látószög sor: látószöge: # szögperc
- nagyítás felirat: a vászon # cm-es darabja, felnagyítva
- betűméret csúszka: A dia betűmérete
- nézet szöveg: A mézelő méhek virágport és nektárt gyűjtenek. Egy kaptárban sok ezer méh él, és mind dolgozik.

### Adatok
- tipp betűmérete: 14 pont
<!-- forrás: kitalált példa – a tipp kérdése. -->
- nézet szélessége: 80 mm
<!-- forrás: kitalált példa – a nagyított nézet a dia ekkora darabját mutatja (a vásznon arányosan nagyobb). -->

## 3. Kontraszt
A **kontraszt** a szöveg és a háttér világosságának aránya. Szöveghez legalább {kontraszthatár} kell. ==Világoskék a fehéren: szép, de halvány.== Kivetítve a teremfény még fakít is: húzd a csúszkát!

> megjegyzés: A határ a nemzetközi akadálymentességi ajánlásból (WCAG) való.

### Feliratok
- kontraszt cím felirat: kontraszt
- pár 1 gomb: sötét a világoson
- pár 2 gomb: világoskék a fehéren
- pár 3 gomb: sárga a fehéren
- pár 4 gomb: világos a sötéten
- teremfény csúszka: Teremfény a vásznon
- teremfény sor: teremfény a vásznon: # lux
- arány felirat: # : 1
- határ felirat: határ: # : 1
- képlet cím: így számoljuk
- világosság sor: világosság: fekete 0, fehér 1
- képlet sor: arány = (világosabb + 0,05) : (sötétebb + 0,05)
- minta szó: Méhek
- sötétített felirat: sötétített terem
- világos terem felirat: világos terem
- tévhit kék: Világoskék szöveg fehér alapon szép.
- válasz kék: Szép, de csak # : 1 – halvány.

### Adatok
- vetítő fénye a vásznon: kb. 1000 lux (becslés)
<!-- forrás: becslés – egy 3000 lumenes vetítő kb. 2,25 m²-es képen legfeljebb kb. 1300 lux; a lámpa öregedése és a veszteségek miatt kevesebb. A lecke ehhez méri a teremfényt (a vászon mindkettőt ugyanúgy veri vissza). -->
- sötétített terem: kb. 20 lux (becslés)
<!-- forrás: becslés – behúzott sötétítővel, lekapcsolt lámpákkal néhányszor tíz lux jut a vászonra. -->
- világos terem: kb. 300 lux (becslés)
<!-- forrás: becslés – a tantermek előírt megvilágítása a padok síkján néhány száz lux (MSZ EN 12464-1); a függőleges vászonra általában kevesebb jut. Behúzott sötétítővel néhányszor tíz lux. -->

## 4. Mit nézel először?
A **vizuális hierarchia** megmutatja, mit nézz először: a nagy, erős színű, üres térrel körülvett elemet. ==Ha minden egyforma, a szem összevissza ugrál.== Válts a két dia között, és kérj új nézőt!

> megjegyzés: A pöttyök modellt mutatnak, nem valódi szemmozgás-mérést.

### Feliratok
- rendezett gomb: Rendezett dia
- rendezetlen gomb: Rendezetlen dia
- új néző gomb: Új néző
- vonz cím: Mi vonzza a szemet?
- vonz 1: a nagy méret
- vonz 2: az erős szín, a kontraszt
- vonz 3: a hely: fent, balra
- vonz 4: az üres tér körülötte
- sorban felirat: a szem sorban halad
- ugrál felirat: a szem összevissza ugrál
- matrica felirat: Szuper téma!
- lábléc felirat: kiselőadás – 5. b
- szemugrás felirat: szemugrás
- cím helye felirat: a cím: #. pillantás
- cím kimaradt felirat: a címet meg sem nézte

### Adatok
- szemugrások: 6 (modell)
<!-- forrás: modell – ennyi „pillantást” mutat a lecke. A szem minden lépésben a legfeltűnőbb, még kevéssé nézett elemre ugrik (feltűnőség: a betűméret és a kép mérete, a hely; plusz egy kis seedelt véletlen). Valódi szemmozgás-mérés eredményét nem állítja. -->

## 5. Lényegkiemelés: kevesebb szöveg
A **lényegkiemelés**: a bekezdésből felsorolás, abból néhány kulcsszó és egy kép. A többit te mondod el. ==Kevesebb szó: nagyobb betű fér el – a hátsó sor is olvassa.== Váltogasd a változatokat!

> megjegyzés: A bekezdés a füzetbe való, a diára a kulcsszavak.

### Feliratok
- bekezdés gomb: bekezdés
- felsorolás gomb: felsorolás
- kulcsszavak gomb: 3 szó + kép
- dia pont 4: Egy családban sok ezer méh él
- szavak sor: szavak a dián: #
- betű sor: a legnagyobb betű, ami elfér: # pont
- hátsó sor sor: a # m-es sorból: # szögperc
- olvasási idő sor: elolvasni: kb. # mp
- tévhit szöveg: Minél több szöveg, annál többet tanul a közönség.
- válasz szöveg: Olvasni és hallgatni egyszerre nehéz.

### Adatok
- legnagyobb szövegméret: 40 pont
<!-- forrás: kitalált példa – a szöveg ennél nem nő tovább (a cím 44 pontos). -->
- olvasási sebesség: kb. 120 szó/perc (becslés)
<!-- forrás: becslés – angol nyelvű olvasásfolyamatossági normák szerint 5–6. osztályban a hangos olvasás mediánja kb. 140–150 szó/perc (Hasbrouck és Tindal 2017, ORF-normák); a magyar szavak átlagosan hosszabbak, és a vetített szöveget messzebbről, idegen tagolásban olvassuk, ezért a lecke kevesebbel számol. Csak nagyságrendi becslés. -->

## 6. Animáció mértékkel
Az **animáció** mozgás a dián. Akkor segít, ha azt mutatja meg, amiről éppen beszélsz. ==Ha minden ugrál, a szem a mozgást követi, nem téged.== Kapcsolj a kettő között!

> megjegyzés: Az órán használt programban az animációt elemenként, sorrendben lehet beállítani.

### Feliratok
- ugrál gomb: Minden ugrál
- egyenként gomb: Egyszerre egy
- beszéd sáv felirat: amiről most beszélsz:
- bevezetés felirat: bevezetés
- figyel felirat: a szem ott van, amiről beszélsz
- elkalandozik felirat: a szem máshol jár
- arány sor: a beszéd # %-ában néz oda
- tévhit animáció: Minél több animáció, annál érdekesebb.
- válasz animáció: Csak az mozogjon, amiről beszélsz.

## 7. Forrás, formátum, közös munka
A kép és az adat **forrása** a dián is ott van. A **dokumentumformátum** döntés: közös munkához **szerkeszthető fájl**, továbbküldéshez nem szerkeszthető, pl. PDF. ==A PDF mindenhol ugyanúgy néz ki.== Válassz helyzetet!

> megjegyzés: Közösen egy felhőben tárolt fájlon is dolgozhattok.

### Feliratok
- kép forrása: Kép: saját rajz (Kiss Panna)
- adat forrása: Adat: Méhes Anna: A méhek élete, 2021
- forrás cédula: a dia alján, kicsiben
- közös gomb: Hárman készítitek együtt
- küldés gomb: Elküldöd, más gépen vetítik
- javítás gomb: A tanár javítást kér
- szerkeszthető cédula: szerkeszthető fájl
- szerk sor 1: többen is szerkeszthetitek
- szerk sor 2: javítható, bővíthető
- szerk sor 3: másik gépen szétcsúszhat
- pdf cédula: nem szerkeszthető, pl. PDF
- pdf sor 1: mindenhol ugyanúgy néz ki
- pdf sor 2: nem írható át könnyen
- pdf sor 3: továbbküldésre, nyomtatásra
- saját gép felirat: a te gépeden
- másik gép szerk felirat: szerkeszthető – másik gépen
- másik gép pdf felirat: PDF – másik gépen
- nincs betű felirat: nincs meg a betűtípus: szétcsúszott
- válassz felirat: Válassz helyzetet!
- ez kell felirat: ez kell

## 8. Összefoglalás
- Egy dia, egy gondolat: kép és kevés szó.
- Nagy betű: a hátsó sorra gondolj!
- Kontraszt legalább {kontraszthatár}.
- Hierarchia: mi a legfontosabb?
- Animáció csak ahhoz, amiről beszélsz.
- Forrás a dián is.

==A dia segít – az előadó te vagy.==

### Feliratok
- összefoglaló cím: A jó diakocka
- tévhit 1: Minél több szöveg, annál jobb.
- válasz 1: Kép és kevés szó – a többit mondd el!
- tévhit 2: A felolvasott dia jó előadás.
- válasz 2: A dia segít, te mesélsz.
- tévhit 3: Ami a monitoron látszik, az a vásznon is.
- válasz 3: A hátsó sornak nagy betű kell.
- tévhit 4: Világoskék a fehéren is olvasható.
- válasz 4: Legalább 4,5 : 1 kontraszt kell.
- tévhit 5: Minél több animáció, annál jobb.
- válasz 5: Csak az mozogjon, amiről beszélsz.
- lecke cédula: Ez a lecke is kivetítve fut
- lecke sor 0: ha a vetített kép # m széles:
- lecke sor 1: legkisebb felirata (# képpont): # m-ig olvasható
- lecke sor 2: ez a cím (# képpont): # m-ig olvasható

### Adatok
- legkisebb felirat: 22 képpont
<!-- forrás: a sorozat szerződése (leckek/SZERZODES.md, 7. fejezet): vásznon legalább 22 képpontos felirat. -->
- cím mérete: 52 képpont
<!-- forrás: ennek a lépésnek a vásznon látható címe. -->
- színpad szélessége: 1920 képpont
<!-- forrás: a lecke 1920 × 1080 képpontos színpadra rajzol (shared/lesson.js); a vetítő ezt a teljes vászonszélességre nagyítja. -->

<!--
  Tanári megjegyzések és források:
  - Kitalált: a „méhes” kiselőadás, a diák neve (Kiss Panna), a könyv (Méhes Anna: A méhek élete, 2021)
    – „kitalált” bélyeggel. A méhekről szóló mondatok a mézelő méhről (Apis mellifera) általánosan ismert
    tények (család: anya, dolgozók, nyáron herék; nektár → méz, virágpor → a fiasítás etetése; beporzás;
    viasz a dolgozók viaszmirigyeiből; táncnyelv: a tánc iránya és hossza – Karl von Frisch).
  - Látásmodell (2. lépés): a betű „látszó mérete” a látószöge: szög = arctg(kisbetű-magasság / távolság).
    A kisbetű magasságát a lecke a betűtípusból méri (a talpatlan betű „x”-e), és a dia → vászon
    nagyítással (vászon szélessége / dia szélessége) számolja át. Határ: 5 szögperc (Snellen, Sloan
    M-egység); kényelmes: kb. 10 szögperc (becslés). Az elmosott nézet modell: a dia képét annyi
    képpontra kicsinyíti, ahány 1 szögperces részletet a szem az adott távolságból megkülönböztet,
    majd simítva felnagyítja. A valódi látás ennél bonyolultabb (kontraszt, fényerő, szemüveg).
    9 m-ről az 5 szögperces kisbetű magassága 9000 mm · tg(5′) ≈ 13,1 mm (a lecke számolja).
  - Kontraszt (3. lépés): WCAG 2.2 relatív világosság (sRGB → lineáris, 0,2126 R + 0,7152 G + 0,0722 B) és
    arány: (L1 + 0,05) : (L2 + 0,05); határ 4,5 : 1 (AA, normál szöveg). A teremfény modellje: a vászon a
    vetítő fényét és a teremfényt is visszaveri; a teremfény minden pontot egyformán világosít, ezért a
    fekete sem fekete: a világosság (L · vetítő + terem) / (vetítő + terem). Erre a vetített világosságra
    alkalmazza a WCAG-képletet – ez a lecke saját, egyszerűsített modellje (a WCAG képernyőre készült).
  - Szemmozgás (4. és 6. lépés): modell, nem mérés („modell” bélyeg). A valódi szemkövetéses vizsgálatok
    is azt találják, hogy a nagy, kontrasztos elemek és az arcok vonzzák először a tekintetet, és a
    mozgó elem elvonja a figyelmet – számszerű állítást a lecke ebből nem tesz.
  - Lényegkiemelés (5. lépés): mindhárom változat ugyanaz a diaelrendezés (balra szöveg, jobbra kép).
    A lecke a DigDoc tördelésével megkeresi a legnagyobb betűméretet, amellyel a szöveg még a diára
    fér (legfeljebb 40 pont), és ebből számolja a hátsó sor látószögét. A szavak számát
    a .md szövegéből számolja; az olvasási idő = szavak / kb. 120 szó/perc (becslés).
  - Formátum (7. lépés): a „szétcsúszás” oka, hogy a szerkeszthető fájl a betűtípust a gépen keresi; ha
    nincs meg, a program másikat használ, más szélességekkel (vö. 10. lecke). A PDF a betűket is magában
    hordozhatja, ezért ugyanúgy néz ki. Valódi program vagy fájlformátum neve a vásznon nincs, csak a
    „PDF”, mint a kerettantervi példa.
  - 8. lépés: a lecke legkisebb, 22 képpontos felirata a 2 m-es vásznon kb. 11–12 mm-es kisbetű – az
    5 szögperces határ szerint kb. 8 m-ig olvasható. Nagyobb teremben nagyobb vászon kell, vagy üljenek
    előrébb – ez beszélgetésindító is lehet.
  - Tévhitek, amelyeket a lecke cáfol: „Minél több szöveg van a dián, annál többet tanul a közönség.”
    „A felolvasott dia jó előadás.” „Minden betű látszik, ha a monitoron látszik.” „Világoskék szöveg fehér
    alapon szép.” „Minél több animáció, annál érdekesebb.”
  - Kapcsolódás: a 10. és a 11. lecke (karakter, bekezdés, kép, forrásjelölés) ugyanezt a „lapot”
    (DigDoc) használja; a dia ugyanaz a tördelés 16 : 9-es lapon.
  - Az órán használt bemutatókészítő program másképp néz ki: a lecke a fogalmakat mutatja, a kezelést
    a tanár a valódi programban tanítja.
-->
