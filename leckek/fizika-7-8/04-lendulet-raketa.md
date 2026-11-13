# Hogyan repül a rakéta? – lendület és kölcsönhatás
tantárgy: Fizika · évfolyam: 7–8. · témakör: 4. Lendület és egyensúly

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/04-lendulet-raketa.md

  A modell egyszerűsítései:
  - a kocsik és a korcsolyázók súrlódás és légellenállás nélkül mozognak (egyenes vonalú,
    egydimenziós mozgás), a kerekek forgását nem számoljuk;
  - a rugós ütköző ideális rugó: az ütközés teljesen rugalmas, az érintkezés ideje
    a tömegektől és a sebességektől függetlenül „ütközés ideje” (a rugó merevségét így
    választjuk). Az erő nagysága ettől az időtől függ (rövidebb ütközés → nagyobb erő),
    a két erő egyenlősége és a lendület megmaradása nem;
  - a gyurmás ütközőben az erő az érintkezés alatt simán nő, majd csökken, a végén a
    kocsik együtt mozognak; a hiányzó mozgási energia a gyurma alakváltozására és
    melegedésére fordítódik. Képletek: rugalmas: v1' = ((m1 − m2)·v1 + 2·m2·v2) / (m1 + m2),
    v2' = ((m2 − m1)·v2 + 2·m1·v1) / (m1 + m2); összetapadó: v' = (m1·v1 + m2·v2) / (m1 + m2);
  - a korcsolyázók lökése félszinusz alakú erő a lökés ideje alatt; a jég súrlódását
    elhanyagoljuk;
  - léggömbrakéta: becsült, egyszerűsített modell. Állandó tolóerő a kiáramlás ideje alatt,
    állandó tömeg (a kiáramló levegő tömegét nem vonjuk le), négyzetes légellenállás
    F = k · v² (k = ½ · ρ · C · A ≈ ½ · 1,2 kg/m³ · 0,5 · 0,03 m² ≈ 0,01 kg/m), a zsinór
    súrlódása nincs. A „légüres tér” gondolatkísérlet: a valóságban a léggömb vákuumban
    jobban felfúvódna (vagy kidurranna); itt csak azt mutatjuk, hogy a külső levegő nem kell
    a gyorsuláshoz. Levegő nélkül nincs légellenállás, ezért gyorsabb lesz;
  - rakéta: ideális rakéta (Ciolkovszkij-egyenlet, Δv = u · ln(m0 / m1)), gravitáció és
    légellenállás nélkül, állandó kiáramlási sebességgel. A valódi pályára állításhoz a
    gravitáció és a légellenállás miatt kb. 9–10 km/s sebességváltozás kell.
  Források / tájékoztató értékek: teniszlabda tömege 56–59,4 g (ITF), erős adogatás
  50–60 m/s; bowlinggolyó legfeljebb 7,26 kg; rakétahajtóművek effektív kiáramlási
  sebessége kb. 2,5–4,5 km/s (szilárd hajtóanyag ≈ 2,5, kerozin–oxigén ≈ 3, hidrogén–oxigén
  ≈ 4,4 km/s); első kozmikus sebesség (körpálya a Föld felszínén) ≈ 7,9 km/s.
-->

## Közös

### Feliratok
- 1. kocsi: 1. kocsi
- 2. kocsi: 2. kocsi
- összes lendület: összes lendület
- lendület tengely: lendület (kg·m/s)
- idő tengely: idő (s)
- lassítva: lassítva
- áll: áll

### Adatok
- 1. kocsi tömege: 2 kg
- 1. kocsi sebessége: 3 m/s
- 2. kocsi tömege: 2 kg
- ütközés ideje: 0,1 s

## 1. Mi a lendület?
Melyiket nehezebb megállítani: a száguldó teniszlabdát vagy a lassan guruló bowlinggolyót? A mozgás „mennyiségét” a **lendület** méri:

képlet: p = m · v

Mértékegysége kg·m/s. A lendületnek ==iránya is van==: ellentétes irányban negatív.

> megjegyzés: Milyen gyors legyen a teniszlabda, hogy akkora legyen a lendülete, mint a golyóé?

### Feliratok
- teniszlabda: teniszlabda
- bowlinggolyó: bowlinggolyó
- teniszlabda csúszka: A teniszlabda sebessége
- egyenlő: legalább akkora, mint a golyóé!
- képlet szöveg: lendület = tömeg × sebesség

### Adatok
- teniszlabda tömege: 58 g
- teniszlabda sebessége: 50 m/s
- bowlinggolyó tömege: 7 kg
- bowlinggolyó sebessége: 8 m/s

## 2. Ütközés: a lendület átadódik
Az 1. kocsi rugós ütközővel nekimegy az álló 2. kocsinak. A tömegük egyforma.

Az 1. kocsi ==megáll==, a 2. pedig ugyanakkora sebességgel indul tovább: a lendület **átadódott**.

> megjegyzés: Nézd a grafikont! Amennyivel az egyik lendülete csökken, annyival nő a másiké. (Súrlódással nem számolunk.)

### Feliratok
- rugós ütköző: rugós ütköző

## 3. Az összeg állandó
Állítsd be a 2. kocsit: lehet nehezebb, és szembe is jöhet!

A két lendület külön-külön változik, de ==az összegük ütközés előtt, közben és után is ugyanannyi==. Ez a **lendület megmaradása**.

> megjegyzés: A balra mutató lendület negatív, összeadáskor levonódik.

### Feliratok
- 2. kocsi tömege csúszka: A 2. kocsi tömege
- 2. kocsi sebessége csúszka: A 2. kocsi sebessége

## 4. Ki nyom erősebben?
Tévhit: a nehezebb, gyorsabb kocsi ==nagyobb erővel nyom==. Nézd lassítva!

Az érintkezés minden pillanatában a két erő **egyenlő nagyságú és ellentétes irányú** (Newton III. törvénye). Ugyanannyi ideig hatnak, így a lendületváltozások is egyenlők és ellentétesek.

> megjegyzés: A könnyebb kocsi sebessége mégis jobban változik. Miért?

### Feliratok
- 1. kocsi tömege csúszka: Az 1. kocsi tömege
- erő az 1. kocsira: erő az 1. kocsira
- erő a 2. kocsira: erő a 2. kocsira
- erő tengely: erő (N)
- idő tengely ms: idő (ms)
- lendületváltozás: lendületváltozás
- sebességváltozás: sebességváltozás
- legnagyobb erő: legnagyobb erő

### Adatok
- nehéz kocsi tömege: 5 kg

## 5. Összetapadó kocsik
Most gyurma van az ütközőn: a kocsik összetapadnak, és együtt gurulnak tovább.

Az összes lendület ==most is ugyanannyi==. A **mozgási energia** viszont csökken: egy része a gyurma alakváltozására és melegítésére fordítódik.

> megjegyzés: Rugalmas ütközésnél a mozgási energia is megmarad.

### Feliratok
- rugalmas gomb: rugalmas
- összetapad gomb: összetapad
- mozgási energia: mozgási energia
- belső energia: gyurma: alakváltozás, melegedés
- megmarad: megmarad
- csökken: csökken
- gyurma: gyurma
- előtte: előtte
- utána: utána

## 6. Két korcsolyázó ellöki egymást
Két korcsolyázó áll a jégen, majd ellökik egymást. Előtte az összes lendület **nulla**, és ==utána is nulla marad==: ugyanakkora lendülettel, ellentétes irányba csúsznak szét.

Ezért a könnyebb gyorsabb: fele akkora tömeg, kétszer akkora sebesség.

> megjegyzés: Mennyi lesz a sebességek aránya, ha egyforma a tömegük?

### Feliratok
- bal név: Bence
- jobb név: Anna
- jobb tömeg csúszka: Anna tömege
- sebességek aránya: sebességek aránya
- tömegek aránya: tömegek aránya
- összeg nulla: összes lendület = 0
- lökés: ellökik egymást

### Adatok
- bal korcsolyázó tömege: 60 kg
- jobb korcsolyázó tömege: 40 kg
- átadott lendület: 60 kg·m/s
- lökés ideje: 0,4 s

## 7. Léggömbrakéta
A léggömb gumija ==hátralöki a levegőt==, a kiáramló levegő pedig ugyanakkora erővel előrelöki a léggömböt.

Tévhit: a rakéta a külső levegőtől rugaszkodik el. Szívd ki a levegőt: a léggömb **így is gyorsul**, sőt jobban, mert nincs légellenállás!

> megjegyzés: Gondolatkísérlet, egyszerűsített modell.

### Feliratok
- levegőben: levegőben
- légüres térben: légüres térben
- szivattyú gomb: Szívd ki a levegőt!
- levegő vissza gomb: Engedd vissza a levegőt
- erő a léggömbre: a levegő előrelöki a léggömböt
- erő a levegőre: a léggömb hátralöki a levegőt
- sebesség tengely: sebesség (m/s)
- szivattyú: szivattyú
- zsinór: zsinór
- gondolatkísérlet: gondolatkísérlet

### Adatok
- léggömb tömege: 15 g
- tolóerő: 0,2 N
- kiáramlás ideje: 0,6 s
- légellenállási tényező: 0,01 kg/m
- zsinór hossza: 4 m

## 8. Rakéta a légüres térben
A rakéta nagy sebességgel lövi hátra a gázt, és ==ettől gyorsul előre==. Elrugaszkodnia nem kell.

Az ideális rakéta modellje:

képlet: Δv = u · ln(m_0 / m_1)

> megjegyzés: u: a gáz sebessége, m_0 és m_1: a tömeg indításkor és a végén. Gravitációval, légellenállással nem számolunk.

### Feliratok
- kiáramlás csúszka: A gáz kiáramlási sebessége
- üzemanyag csúszka: Üzemanyag a kezdeti tömegből
- erő a rakétára: a gáz előrelöki a rakétát
- erő a gázra: a rakéta hátralöki a gázt
- rakéta sebessége: sebesség
- üzemanyag: üzemanyag
- elégetett tengely: elégetett üzemanyag (a kezdeti tömeg %-a)
- sebességváltozás tengely: sebességváltozás (km/s)
- körpálya: Föld körüli pályán: {első kozmikus sebesség}
- világűr: légüres tér

### Adatok
- kiáramlási sebesség: 3 km/s
- legkisebb kiáramlási sebesség: 2,5 km/s
- legnagyobb kiáramlási sebesség: 4,5 km/s
- üzemanyag aránya: 90 %
- első kozmikus sebesség: 7,9 km/s

## 9. Összefoglalás
- **Lendület**: p = m · v, iránya is van.
- Ütközéskor a lendület átadódik, de ==az összes lendület nem változik==.
- Az erők **párban** lépnek fel: egyenlő nagyságúak, ellentétes irányúak.
- A rakéta ==hátralöki a gázt==, a gáz előrelöki a rakétát. Levegő nem kell hozzá.

### Feliratok
- össz lendület cím: lendület = tömeg × sebesség
- össz megmaradás cím: az összes lendület állandó
- össz erőpár cím: az erők párban lépnek fel
- össz rakéta cím: a rakéta a gázt löki hátra
- össz megmaradás: ütközésben, ellökésnél is
- össz erőpár: egyenlő nagyok, ellentétes irányúak
- össz rakéta: levegő nélkül is működik
- össz lendület: a lassú golyónak is lehet nagyobb
