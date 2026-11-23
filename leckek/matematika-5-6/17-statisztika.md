# Mit mutat az átlag? – diagramok, átlag, módusz, medián
tantárgy: Matematika · évfolyam: 5–6. · témakör: 17. Leíró statisztika

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/17-statisztika.md
  Feliratban a # jel helyére a lecke számot ír (pl. „az osztály # diákja” → „az osztály 24 diákja”).
  Minden adat KITALÁLT példa (osztályfelmérés, hőmérséklet, könyvek); a vásznon „kitalált adat” bélyeg jelzi.
  Az eredményeket (diákok száma, szögek, átlag, medián, módusz) a lecke kiszámolja, és piros sávval jelez,
  ha a .md-ben írt érték nem egyezik a számolásával.
-->

## Közös

### Feliratok
- gyalog: gyalog
- busz: busz
- autó: autó
- bicikli: bicikli
- kitalált adat: kitalált adat
- átlag: átlag
- medián: medián
- módusz: módusz
- diák felirat: # diák
- diákok tengely: diákok száma
- kérdés 1: Hogyan jöttök iskolába?
- tippelj: Tippelj előbb!
- a tipped: a te tipped

### Adatok
- közlekedés: 9; 6; 6; 3
- diákok száma: 24
<!-- kitalált osztályfelmérés. A „közlekedés” négy száma sorban: gyalog; busz; autó; bicikli.
     A „diákok száma” a négy szám összege – a lecke kiszámolja és összeveti. -->

## 1. Hogyan jöttök iskolába?
Megkérdeztük az osztály mind a {diákok száma} diákját: hogyan jön iskolába? Minden válasz egy **strigula** a táblázatban. Ötösével csoportosítunk, így könnyű megszámolni. A strigulák száma a **gyakoriság**. ==A táblázat rendet tesz az adatokban.==

> megjegyzés: Végezzétek el a felmérést a saját osztályotokban is!

### Feliratok
- osztály: az osztály # diákja
- fej mód: hogyan?
- fej strigula: strigulák
- fej gyakoriság: gyakoriság
- összesen: összesen

## 2. Oszlopdiagram
Minden diák egy kis tégla. A téglák oszlopokba rakódnak: az oszlop **magassága** a gyakoriság. ==Az oszlopdiagramon egy pillantásra látszik, melyik csoport nagyobb.== A függőleges tengely 0-tól indul, különben az oszlopok aránya becsapna.

> megjegyzés: Kattints egy oszlopra!

### Feliratok
- egy tégla: 1 tégla = 1 diák

## 3. Ugyanez kördiagramon
==Tippelj előbb!== Mekkora körcikk jut a busznak? Az oszlopok lefekszenek, szalaggá állnak össze, a szalag körré görbül. Az egész kör a {diákok száma} diák, így **1 diák = {1 diák szöge}**. A **kördiagram** azt mutatja, mekkora rész jut az egészből.

### Feliratok
- kérdés 3: Mekkora körcikk jut a busznak?
- tipp negyed: negyed kör
- tipp harmad: harmad kör
- tipp fél: fél kör
- váltó gomb: oszlop ↔ kör
- negyed kör: pontosan negyed kör
- egy diák: 1 diák

### Adatok
- 1 diák szöge: 15°
- busz szöge: 90°
<!-- 360° : 24 = 15°; busz: 6 · 15° = 90° (6/24 = 1/4: negyed kör). Gyalog 135°, autó 90°, bicikli 45°.
     Mindkettőt a lecke kiszámolja és összeveti. -->

## 4. Melyiket mikor?
Az **oszlopdiagram** összehasonlít. A **kördiagram** azt mutatja, mekkora rész jut az egészből. A **vonaldiagram** az időbeli változást mutatja. Tévhit: a kördiagram bármihez jó. ==De mi lenne a heti hőmérsékletek „egésze”? Ilyen nincs.==

### Feliratok
- oszlopdiagram: oszlopdiagram
- kördiagram: kördiagram
- vonaldiagram: vonaldiagram
- sor hőmérséklet: Reggeli hőmérséklet (°C)
- hétfő: H
- kedd: K
- szerda: Sze
- csütörtök: Cs
- péntek: P
- jó összehasonlít: összehasonlít
- jó rész-egész: rész az egészből
- rossz átmenet: nincs köztük átmenet
- rossz egész: nincs „egész”
- jó idő: változás időben

### Adatok
- hőmérséklet: 4; 6; 9; 7; 3 °C
<!-- kitalált példa: reggeli hőmérséklet hétfőtől péntekig. A hőmérsékletek összege nem jelent semmit,
     ezért nincs „egész”, aminek a részeit kördiagram mutathatná. -->

## 5. Az átlag: kiegyenlítjük a tornyokat
Négy torony: {tornyok} kocka. A magasabbakról kockák vándorolnak az alacsonyabbakra, amíg mind egyforma magas nem lesz. Ez a magasság az **átlag**: ==összeadjuk az adatokat, és elosztjuk a darabszámukkal.== Húzd a csúszkát: az átlag nem mindig egész szám!

### Feliratok
- torony cím: Rakjuk egyforma magasra!
- torony csúszka: a 4. torony magassága
- maradék: a maradék # kockát # szeletre vágjuk
- eredeti: eredetileg

### Adatok
- tornyok: 3; 5; 4; 8
- tornyok átlaga: 5
<!-- (3 + 5 + 4 + 8) : 4 = 20 : 4 = 5. A csúszka a 4. tornyot 1 és 10 között állítja; pl. 9-nél 21 : 4 = 5,25
     (a maradék 1 kocka 4 negyed-szeletre vágva). A „tornyok átlaga” eredményt a lecke összeveti. -->

## 6. Módusz és medián
Kilenc diák elmondta, hány könyvet olvasott a nyáron. A **módusz** a leggyakoribb adat. A **medián** a középső, de csak **sorba rendezve**! ==Az átlag ≈ {könyvek átlaga}, pedig senki sem olvasott ennyit.==

> megjegyzés: Húzd a pöttyöket: a vonalak követik!

### Feliratok
- könyvek cím: Hány könyvet olvastál a nyáron?
- középső kérdés: a középső?
- rendezetlen: rendezetlen sor!
- sorba rendezve: sorba rendezve
- könyvek tengely: könyvek száma
- nincs módusz: nincs módusz
- alaphelyzet gomb: Eredeti adatok

### Adatok
- könyvek: 2; 4; 1; 0; 3; 2; 4; 1; 2
- könyvek átlaga: 2,1
- könyvek mediánja: 2
- könyvek módusza: 2
<!-- kitalált példa, a válaszok sorrendjében. Sorba rendezve: 0; 1; 1; 2; 2; 2; 3; 4; 4.
     Átlag: 19 : 9 = 2,111… ≈ 2,1; medián (az 5. adat): 2; módusz: 2 (háromszor). A rendezetlen sor közepe 3 – ez a tévhit.
     A három eredményt a lecke kiszámolja és összeveti (az átlagot ±0,05 eltéréssel, mert kerekített). -->

## 7. Egy kiugró adat
==Tippelj előbb!== Egy diák nem {lecserélt érték}, hanem {kiugró érték} könyvet olvasott. Mi mozdul el jobban: az átlag vagy a medián? Egy **kiugró adat** az átlagot elhúzza, a mediánt alig. Most a legtöbben az átlag alatt vannak: ==az átlag itt nem a „tipikus” érték.==

### Feliratok
- kérdés 7: Mi mozdul el jobban?
- tipp átlag: az átlag
- tipp medián: a medián
- tipp egyik sem: egyik sem
- kiugró gomb: kiugró adat be / ki
- átlag alatt: az átlag alatt: # diák a #-ből
- előtte: előtte
- utána: utána

### Adatok
- lecserélt érték: 4
- kiugró érték: 12
- kiugró átlag: 3
- kiugró medián: 2
<!-- A „könyvek” sor utolsó 4-ese 12 lesz: 0; 1; 1; 2; 2; 2; 3; 4; 12 → átlag 27 : 9 = 3, medián 2, módusz 2.
     Az átlag alatt 6 diák van (0; 1; 1; 2; 2; 2), egy pontosan az átlagon (3). A két eredményt a lecke összeveti. -->

## 8. Összefoglalás
- **Oszlopdiagram:** összehasonlít. **Kördiagram:** rész az egészből. **Vonaldiagram:** változás időben.
- **Átlag:** összeadjuk, elosztjuk a darabszámmal – a kiegyenlített érték.
- **Medián:** a sorba rendezett adatok közepe.
- **Módusz:** a leggyakoribb adat.
- ==Kiugró adat: az átlag elmozdul, a medián alig.==

### Feliratok
- össz oszlop: összehasonlít
- össz kör: rész az egészből
- össz vonal: változás időben
- össz átlag: kiegyenlítés
- össz medián: középső, sorba rendezve
- össz módusz: a leggyakoribb

<!-- Tanári megjegyzések:
  - Minden adat kitalált didaktikai példa (osztályfelmérés, hőmérséklet, könyvek); a vásznon „kitalált adat” bélyeg.
  - A terv briefje a 0; 1; 1; 2; 2; 2; 3; 4; 12 sort adja; itt az alapsor 0; 1; 1; 2; 2; 2; 3; 4; 4, és a „kiugró adat”
    lépés az utolsó 4-est cseréli 12-re – így a briefbeli sor áll elő. Az adatok száma mindig 9 (a pöttyök húzása nem
    változtat rajta), ezért a medián mindig egyetlen középső adat: a sorba rendezett sor 5. eleme.
  - Módusz: ha minden adat különböző, a lecke „nincs módusz” feliratot ír; ha több érték egyformán a leggyakoribb, mindet
    jelöli. Tankönyvenként eltér, hogy ilyenkor „nincs módusz” vagy „több módusz” a szóhasználat.
  - Az 5. lépés a „kiegyenlítés” (PhET „Mean: Share and Balance” jellegű) modellje; nem egész átlagnál a maradék kockákat
    a lecke egyenlő szeletekre vágja.
  - A 3. lépésben az oszlopok előbb szalagdiagrammá (rész–egész szalag) állnak össze; a szalag hossza a kör kerülete,
    ezért görbítve pontosan zár.
  - A vonaldiagram a kategóriák (gyalog, busz…) között azért félrevezető, mert a vonal köztes értékeket és sorrendet sugall.
-->
