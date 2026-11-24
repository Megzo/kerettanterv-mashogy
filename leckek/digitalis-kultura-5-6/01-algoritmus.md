# Hogyan kenjen zsíros kenyeret a robot? – az algoritmus
tantárgy: Digitális kultúra · évfolyam: 5–6. · témakör: 1. Algoritmizálás és blokkprogramozás

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/digitalis-kultura-5-6/01-algoritmus.md

  A blokkok felirata a „… blokk” kulcsokból jön; a # a paraméter helye („a kenyéren” / „a szeleten”).
  A recept átírható más ételre: a blokkok száma és a robot mozdulatai a kódban vannak, a feliratuk itt.
  A „Tippelj!” lépésekben (2., 4.) a panel első bekezdése a kérdés; a többi bekezdés elmosódva
  látszik, és csak a tipp után válik olvashatóvá.
-->

## Közös

### Feliratok
- tippelj felirat: Tippelj!
- kísérlet felirat: kipróbálom
- magyarázat felirat: magyarázat
- a te tipped felirat: a te tipped
- jó tipp felirat: Jó tipp! Nézzük meg!
- rossz tipp felirat: Sokan gondolják így – nézzük meg!
- sematikus bélyeg: sematikus rajz
- kitalált bélyeg: kitalált példák
- blokknyelv bélyeg: a lecke saját blokkjai
- program felirat: A PROGRAM
- asztal felirat: A KONYHAPULT FELÜLRŐL
- kenyér felirat: KENYÉR
- zsír felirat: ZSÍR
- kés felirat: KÉS
- só felirat: SÓ
- hagyma felirat: LILAHAGYMA
- tányér felirat: TÁNYÉR
- indításkor blokk: indításkor
- indításkor vége: program vége
- fogd meg a kést blokk: fogd meg a kést
- vágj le blokk: vágj le egy szeletet
- merítsd blokk: merítsd a kést a zsírba
- húzd végig blokk: húzd végig a kést #
- kenyéren opció: a kenyéren
- szeleten opció: a szeleten
- tedd le a kést blokk: tedd le a kést
- tányérra blokk: tedd a szeletet a tányérra
- sózd blokk: szórj sót a szeletre
- hagymát blokk: tegyél hagymát a szeletre
- vágj szeletet blokk: vágj egy szelet kenyeret
- kend meg blokk: kend meg a szeletet zsírral
- ha blokk: ha # akkor
- ha vége: elágazás vége
- van hagyma? blokk: van hagyma
- igaz felirat: IGAZ
- hamis felirat: HAMIS
- futtatás gomb: Futtatás
- egy lépés gomb: Egy lépés
- nincs szelet hiba: hiba: nincs még szelet
- nincs szelet buborék: Nincs szelet!
- metszet felirat: A SZELET OLDALRÓL
- kenyér réteg: kenyér
- zsír réteg: zsír
- só réteg: só
- hagyma réteg: hagyma
- jó eredmény felirat: kész: zsíros kenyér!
- só alatt felirat: más lett: a só a zsír alatt
- hagyma alatt felirat: más lett: a hagyma a zsír alatt

## 1. Mi az algoritmus?
Ez a robotkar zsíros kenyeret készít – ha pontosan leírjuk, mit tegyen. Az **algoritmus** véges sok, pontos lépés, amely megold egy feladatot. ==Nem csak a gépeké:== a recept, az útbaigazítás és a tűzriadó rendje is algoritmus.

> megjegyzés: Végrehajtó lehet ember, robot vagy számítógép.

### Feliratok
- példák felirat: HÉTKÖZNAPI ALGORITMUSOK
- recept kártya: Recept
- recept 1: Vágj egy szelet kenyeret.
- recept 2: Kend meg zsírral.
- recept 3: Sózd meg, tegyél rá hagymát.
- út kártya: Útbaigazítás
- út 1: A kapuból fordulj balra.
- út 2: A második saroknál fordulj jobbra.
- út 3: A harmadik ház a miénk.
- tűz kártya: Tűzriadó
- tűz 1: Hagyd abba, amit csinálsz.
- tűz 2: Állj sorba a tanár mögött.
- tűz 3: A kijelölt úton menj ki az udvarra.
- közös felirat: MI KÖZÖS BENNÜK?
- lépések felirat: lépésekből áll
- sorrend felirat: számít a sorrend
- vége felirat: véges: egyszer vége van
- végrehajtó felirat: a végrehajtó
- cél felirat: A CÉL

## 2. Tippelj: mit csinál a robot?
Egyetlen utasítás: „Kend meg a kenyeret zsírral.” ==Mit csinál a robot?==

**Megáll.** A robot nem találgat, csak végrehajtja, amit leírtunk. A mondat nem **egyértelmű**: mivel kenje? Az egész veknit? Melyik oldalát?

> megjegyzés: Tévhit: „a gép kitalálja, mire gondolok”.

### Feliratok
- kend meg a kenyeret blokk: kend meg a kenyeret zsírral
- kenés kérdés felirat: Mit csinál a robot ezzel a programmal?
- jól megkeni tipp: jól megkeni
- megáll tipp: megáll: nincs megadva, mivel
- vekni tipp: az egész veknit bekeni
- nem elemi hiba: nem elemi: nincs a robot lépései között
- nem elemi buborék: Mivel? Melyik oldalát?

## 3. Elemi lépések
Most kisebb lépéseket írtunk. Az **elemi lépés** olyan kicsi, hogy a robot közvetlenül végre tudja hajtani. De figyeld meg: „a kenyéren” – melyiken? A robot az egész veknit keni meg! ==Kattints rá, és javítsd ki!==

> megjegyzés: Amit „mindenki tud”, azt is le kell írni.

### Feliratok
- szótár felirat: A ROBOT ELEMI LÉPÉSEI
- kattints felirat: kattints rá, és javítsd ki!
- vekni zsíros felirat: az egész vekni zsíros lett!
- szelet zsíros felirat: kész: zsíros a szelet

## 4. Tippelj: számít a sorrend?
Ugyanazok a lépések, de felcseréltük a sózást és a kenést. ==Mi lesz? Tippelj!==

**A só a zsír alá kerül.** A **sorrend** számít: a robot abban a sorrendben dolgozik, ahogy leírtuk. Húzd a blokkokat! A só és a hagyma sorrendje mindegy: ==több jó algoritmus is lehet.==

### Feliratok
- sorrend kérdés felirat: Felcseréltük a sózást és a kenést. Mi lesz?
- ugyanolyan tipp: ugyanolyan lesz
- só alá tipp: a só a zsír alá kerül
- leáll tipp: a robot leáll
- csere felirat: felcserélve
- húzd felirat: fogd meg, és húzd máshová!
- ez is jó felirat: ez is jó: más sorrend, jó kenyér

## 5. Lépésenkénti finomítás
A nagy feladatot nagy lépésekre bontjuk, a nagy lépést kisebbekre – amíg minden lépés elemi nem lesz. Ez a **lépésenkénti finomítás**. A fa levelei sorban kiadják a robot programját. ==Kattints egy nagy lépésre!==

> megjegyzés: A legrövidebb leírás nem mindig a legjobb.

### Feliratok
- készíts blokk: készíts zsíros kenyeret
- feladat felirat: A FELADAT
- nagy lépések felirat: NAGY LÉPÉSEK
- elemi lépések felirat: ELEMI LÉPÉSEK
- nyisd felirat: kattints rá: kinyílik, becsukódik
- levelek felirat: a robot programja: # elemi lépés

## 6. Bemenet és kimenet
A **bemenet** az, amiből az algoritmus dolgozik: a hozzávalók. A **kimenet** az eredmény: a zsíros kenyér. ==Vedd el a hagymát!== A robot megáll. Egy „ha” blokkal kihagyhatja ezt a lépést.

> megjegyzés: Az elágazásról a következő leckékben lesz szó.

### Feliratok
- bemenet felirat: BEMENET
- kimenet felirat: KIMENET
- kenyér bemenet: kenyér
- zsír bemenet: zsír
- só bemenet: só
- hagyma bemenet: lilahagyma
- teljes kimenet: zsíros kenyér lilahagymával
- hagyma nélküli kimenet: zsíros kenyér hagyma nélkül
- nincs kimenet: nincs kész étel: a robot megállt
- nincs hagyma hiba: hiba: nincs hagyma
- nincs hagyma buborék: Nincs hagyma!
- hagyma gomb: Hagyma: elveszem / visszateszem
- feltétel gomb: „ha” blokk: be / ki

## 7. Háromféle leírás
Ugyanazt az algoritmust leírhatjuk **szöveggel**, **folyamatábrával** és **blokkokkal**. Futtasd! A futó lépés mindhárom leírásban ugyanott világít. A folyamatábrán a rombusz a döntés: ott ágazik el az út.

### Feliratok
- szöveg felirat: SZÖVEGGEL
- folyamatábra felirat: FOLYAMATÁBRÁN
- blokk felirat: BLOKKOKKAL
- stop felirat: vége

## 8. Összefoglalás
Az **algoritmus** véges sok, pontos, egyértelmű lépés. A végrehajtó **elemi** lépéseket hajt végre, betű szerint. A **sorrend** számít. A nagy lépést **finomítjuk**. A bemenetből kimenet lesz. Leírhatjuk szöveggel, folyamatábrával, blokkokkal.

### Feliratok
- összegzés felirat: AMIT MEGTANULTUNK
- algoritmus kártya: algoritmus: véges sok, pontos, egyértelmű lépés
- elemi kártya: elemi lépés: a végrehajtó közvetlenül megteszi
- sorrend kártya: a sorrend számít – de több jó sorrend is lehet
- finomítás kártya: finomítás: nagy lépés, benne kisebbek
- bemenet kártya: bemenetből (hozzávalók) kimenet (étel)
- leírás kártya: leírás: szöveg · folyamatábra · blokk

<!-- Tanári megjegyzések és források:
  - Kitalált példák: a konyha, a robotkar, a recept, az útbaigazítás és a tűzriadó lépései a lecke saját,
    szemléltető példái. A tűzriadó valódi rendjét az iskola tűzriadó-terve írja elő – a három sor csak
    szemléltetés, nem a terv kivonata.
  - A „robotkar” sematikus, felülnézeti rajz (nincs arca). A mozdulatai a lecke saját modellje: a kés, a só,
    a hagyma helye rögzített; a robot csak a „### Feliratok” blokkjaiban felsorolt elemi lépéseket hajtja végre.
    A buborék („Mivel? Melyik oldalát?”, „Nincs szelet!”) a robot hibaüzenete, nem gondolat.
  - A „kend meg a szeletet zsírral” és a „vágj egy szelet kenyeret” blokk a 4., 6. és 7. lépésben nagy lépés:
    mögötte az 5. lépés fájának elemi lépései futnak (a kód ugyanazokat a mozdulatokat hajtja végre). Ezt a
    „saját blokkot” 7. osztályban eljárásnak hívják – itt csak finomításként szerepel.
  - Az 5. lépés fája a „lépésenkénti finomítás” (felülről lefelé tervezés). A kerettanterv az „alulról
    felfelé építkezést” is említi: ugyanez a fa jobbról balra olvasva (az elemi lépésekből nagy lépés lesz).
  - A 6. lépés „ha” blokkja előzetes: a feltétel és az elágazás a 3. leckében (03-elagazas) jön.
  - A lecke blokknyelve saját nyelv (papír blokk, bal oldali kategóriasáv, „… vége” záró sáv). Az órán használt
    blokkprogramozó környezetben a blokkok színe, alakja és felirata eltér; a fogalmak (lépés, sorrend,
    elemi lépés, bemenet, kimenet) ugyanazok.
  - Javasolt tevékenység (kerettanterv: „az algoritmus eljátszása”): egy tanuló a „robot”, aki betű szerint
    hajtja végre a társai által írt receptet (pl. vajas kenyér papírmakettel, kés nélkül).
  - Adatok: a leckében nincs mért adat; minden szám (mozdulatok ideje) a rajz modellje.
-->
