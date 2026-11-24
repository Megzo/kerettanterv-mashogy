# Kinek hazudik az átlag? – középértékek, szóródás, diagramtrükkök
tantárgy: Matematika · évfolyam: 9–10. · témakör: 16. Leíró statisztika

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/14-statisztika.md
  Ahol egy feliratban # áll, oda a lecke számot ír.
  A tengelyszámok és a σ, Q₁, Q₃ jelek a vásznon kódban rögzítettek.
  Az eredményeket (átlag, medián, terjedelem, szórás, kvartilisek, látszólagos arány) a lecke kiszámolja,
  és piros sávval jelez, ha a .md-ben írt érték nem egyezik a számolásával.
  Kapcsolat: a Matematika 5–6. „Mit mutat az átlag?” leckéje (kiegyenlítés, medián, módusz, kiugró adat,
  oszlop ↔ kör) erre a leckére az előzmény – ezeket itt nem ismételjük, hanem továbbvisszük.
-->

## Közös

### Feliratok
- kitalált adat: kitalált adat
- valós adat: valós adat
- modell bélyeg: modell – csak az alak szemléltetés
- kitekintés: kitekintés – 11–12. évfolyam
- átlag: átlag
- medián: medián
- módusz: módusz
- ezer Ft: ezer Ft

## 1. Az átlag: az egyensúly pontja
Egy kis cég kilenc dolgozójának bére egy deszkán: minden bér egy egyforma súly. Hol kell alátámasztani, hogy ne billenjen? ==Pontosan az átlagnál.== Ott a bal oldali eltérések összege egyenlő a jobb oldaliakéval: {eltérések összege} ezer Ft mindkét oldalon. Húzz el egy súlyt: a deszka megbillen, az alátámasztás utánacsúszik.

> megjegyzés: Bizonyítsd: az átlagtól való eltérések összege mindig 0.

### Feliratok
- bérek cím: Havi bér egy kilencfős cégnél
- bal oldal: bal oldali eltérések: #
- jobb oldal: jobb oldali eltérések: #
- egyensúly: egyensúlyban
- billen: billen…
- bér tengely: bér (ezer Ft)
- alaphelyzet 1: Eredeti bérek

### Adatok
- bérek: 400; 420; 450; 450; 480; 500; 520; 550; 600
- bérek átlaga: 485,6
- bérek mediánja: 480
- eltérések összege: 227,8
<!-- kitalált példa (a terv számpéldája), havi bruttó bér ezer forintban. Összeg 4370, átlag 4370 : 9 = 485,55… ≈ 485,6;
     medián (az 5. adat) 480; módusz 450. Bal oldali eltérések: 85,6 + 65,6 + 35,6 + 35,6 + 5,6 ≈ 227,8;
     jobb oldaliak: 14,4 + 34,4 + 64,4 + 114,4 ≈ 227,8 (pontosan 2050/9). A lecke kiszámolja és összeveti. -->

## 2. Megérkezik a tulajdonos
==Tippelj előbb!== Belép a tulajdonos is, havi {tulajdonos bére} ezer forinttal. Az átlag {új átlag} ezer Ft lesz – több, mint amennyit a kilenc dolgozó bármelyike keres. A medián csak {új medián} ezer Ft. ==Egy kiugró adat az átlagot elrántja, a mediánt alig mozdítja.== Húzd a csúszkát!

> megjegyzés: Melyik számot írná egy álláshirdetés? Melyiket a szakszervezet?

### Feliratok
- kérdés 2: Mennyi lesz most az átlag?
- tippelj: Tippelj előbb!
- tipp 2a: kb. 500
- tipp 2b: kb. 700
- tipp 2c: 1000 fölött
- a tipped: a te tipped
- tulajdonos csúszka: a tulajdonos bére (ezer Ft)
- tulajdonos: tulajdonos
- dolgozók az átlag alatt: az átlag alatt: # dolgozó a #-ből

### Adatok
- tulajdonos bére: 6000
- új átlag: 1037
- új medián: 490
<!-- kitalált példa: 4370 + 6000 = 10 370, 10 370 : 10 = 1037; páros elemszám → medián (480 + 500) : 2 = 490.
     A csúszka a tulajdonos bérét 300 és 8000 ezer Ft között állítja (mindig egész ezer Ft, 100-asával). -->

## 3. Valódi adat: átlagkereset és mediánkereset
A KSH szerint ({ksh hónap}) a teljes munkaidőben dolgozók bruttó **átlagkeresete** {ksh átlag}, **mediánkeresete** csak {ksh medián} volt. Az eloszlás **jobbra elnyúló**: kevés nagyon magas kereset húzza fel az átlagot. ==Mivel a medián kisebb az átlagnál, a dolgozók legalább fele az átlag alatt keres.==

> megjegyzés: A görbe csak az eloszlás alakját mutatja (modell), a két jelölt érték valódi.

### Feliratok
- ksh cím: Bruttó havi kereset Magyarországon
- dolgozók fele: a dolgozók fele
- forrás ksh: Forrás: KSH, Keresetek gyorstájékoztató, #
- kereset tengely: bruttó kereset (ezer Ft)
- gyakoriság tengely: dolgozók aránya
- különbség: az átlag # %-kal több a mediánnál

### Adatok
- ksh hónap: 2024. október
- ksh átlag: 637 200 Ft (2024, frissítendő)
- ksh medián: 529 000 Ft (2024, frissítendő)
<!-- forrás: KSH gyorstájékoztató, Keresetek, 2024. október (megjelent: 2024-12-20),
     https://www.ksh.hu/en/first-releases/ker/eker2410.html, lekérdezve: 2026-11-24.
     „Full-time employees' average gross earnings were HUF 637,200 … Median gross earnings were HUF 529,000.”
     Azért október, mert a decemberi adatot a jutalmak, prémiumok torzítják (2024. december: átlag 727 700 Ft,
     medián 560 900 Ft). Teljes évi mediánt a gyorstájékoztató nem közöl (a teljes évi átlag 646 800 Ft).
     FRISSÍTENDŐ: évente cserélhető egy újabb hónap adatára (a hónapot a „ksh hónap” és a forrássor is mutatja).
     A görbe MODELL: lognormális eloszlás, amelynek mediánja 529 és átlaga 637,2 ezer Ft
     (σ = √(2 · ln(637,2/529)) ≈ 0,61) – a valódi eloszlás alakját a KSH nem ebben a formában közli.
     „Legalább fele”: ha a medián < átlag, akkor a medián alatt vagy azon lévők (legalább 50 %) mind az átlag alatt vannak. -->

## 4. Melyik jegy jár? – mikor melyik középérték
Jegyeid: {jegyek}. Az átlag {jegyek átlaga}, a medián és a módusz {jegyek mediánja}. ==Ugyanaz az adatsor, három „igazság”== – érvelj az ötösért! Húzd a jegyeket: mikor ad a három mutató különböző jegyet? Ökölszabály: torz, kiugró adatoknál a **medián**, ha az összeg számít, az **átlag**, kategóriáknál a **módusz** a beszédes.

### Feliratok
- jegyek cím: Év végi jegyek matekból
- jegy tengely: érdemjegy
- jegy szerint: → jegy: #
- alaphelyzet 4: Eredeti jegyek
- mikor medián: bérek, lakásárak: kiugró adatok
- mikor átlag: összeg számít: költség, termés
- mikor módusz: kategória: cipőméret, kedvenc szín
- ökölszabály: ökölszabály

### Adatok
- jegyek: 2; 3; 5; 5; 5
- jegyek átlaga: 4
- jegyek mediánja: 5
<!-- a terv számpéldája: (2 + 3 + 5 + 5 + 5) : 5 = 20 : 5 = 4; rendezve 2; 3; 5; 5; 5 → medián 5; módusz 5.
     A „jegy szerint” sor az átlagot a szokásos módon kerekíti (x,5-től fölfelé); az iskolai gyakorlat
     ennél bonyolultabb (súlyozás, tanári mérlegelés) – a lecke ezt nem modellezi. -->

## 5. Ugyanaz az átlag, mégis más: a szóródás
Két kosaras hat meccse: átlag, medián, módusz egyaránt {pontátlag} pont. Mégis más a kettő! A **terjedelem**: legnagyobb adat − legkisebb adat. A **szórás** az átlagtól való `d` eltérések tipikus mérete: ==az eltérésnégyzetek átlagának négyzetgyöke== (piros négyzet).

képlet: σ = √([[d_1^2 + … + d_n^2 / n]])

### Feliratok
- játékos A: Andi
- játékos B: Bori
- játékos gomb: Andi ↔ Bori
- pont tengely: pont meccsenként
- terjedelem: terjedelem: #
- szórás: szórás: σ #
- átlagos négyzet: az eltérésnégyzetek átlaga
- alaphelyzet 5: Eredeti pontok

### Adatok
- Andi pontjai: 14; 15; 16; 16; 17; 18
- Bori pontjai: 9; 11; 16; 16; 21; 23
- pontátlag: 16
- Andi terjedelme: 4
- Bori terjedelme: 14
- Andi szórása: 1,29
- Bori szórása: 4,97
<!-- kitalált példa. Mindkét sor összege 96, átlag 16; rendezve a 3. és 4. adat 16 → medián 16; módusz 16.
     Andi: eltérések −2; −1; 0; 0; 1; 2, négyzetösszeg 10, 10 : 6 ≈ 1,667, σ ≈ 1,29; terjedelem 18 − 14 = 4.
     Bori: eltérések −7; −5; 0; 0; 5; 7, négyzetösszeg 148, 148 : 6 ≈ 24,67, σ ≈ 4,97; terjedelem 23 − 9 = 14.
     A szórás itt n-nel osztott (a középiskolai definíció). A szórás és a terjedelem a kerettantervben a 11–12.
     évfolyam fogalma – a lecke „kitekintés” bélyeggel előzetesként mutatja; a tanár kihagyhatja. -->

## 6. Kvartilisek és dobozábra
Rendezd sorba a tizenegy adatot! A medián kettévágja a sort, a két fél mediánja az **alsó** és a **felső kvartilis** (`Q_1`, `Q_3`). A **dobozábra** öt számot mutat: legkisebb, `Q_1`, medián, `Q_3`, legnagyobb. ==A dobozban van az adatok középső fele.== Húzd a pöttyöket: melyik szám mozdul?

### Feliratok
- képernyő cím: Napi képernyőidő (perc), 11 diák
- perc tengely: perc
- alsó fél: alsó fél
- felső fél: felső fél
- legkisebb: legkisebb
- legnagyobb: legnagyobb
- Q1 felirat: alsó kvartilis
- Q3 felirat: felső kvartilis
- középső fele: az adatok középső fele
- alaphelyzet 6: Eredeti adatok

### Adatok
- képernyőidő: 40; 50; 70; 90; 100; 110; 120; 140; 160; 190; 240
- alsó kvartilis: 70
- képernyő medián: 110
- felső kvartilis: 160
<!-- kitalált példa. 11 adat, rendezve; medián a 6. (110); alsó fél az első 5 (medián nélkül) → Q₁ = 70 (3. adat);
     felső fél a 7–11. → Q₃ = 160 (9. adat). Terjedelem 240 − 40 = 200, interkvartilis terjedelem 160 − 70 = 90.
     A lecke a kártyákat először összekeverve mutatja, majd sorba rendezi.
     Kvartilis-módszer: a medián nélküli két fél mediánja (több tankönyv így tanítja; más módszerek – pl. a
     táblázatkezelők QUARTILE függvénye – páratlan elemszámnál eltérhetnek). A kvartilis és a dobozábra a kerettantervben
     a 11–12. évfolyam fogalma („sodrófa (box-plot) diagram”) – itt kitekintés. -->

## 7. A levágott tengely
Két jelölt: {szavazat A} és {szavazat B}. Húzd a csúszkát: honnan induljon a függőleges tengely? Ha {tengely kezdete}-nál kezdődik, az egyik oszlop {látszólagos arány}-szer olyan magas, mint a másik – pedig a valódi arány csak kb. 1,08. ==Oszlopdiagramon a tengely 0-tól induljon, különben az oszlopok magassága hazudik.==

> megjegyzés: Keress a hírekben levágott tengelyű diagramot, és rajzold újra 0-tól!

### Feliratok
- szavazás cím: Ki nyeri a szavazást?
- jelölt A: A jelölt
- jelölt B: B jelölt
- tengely csúszka: a tengely kezdete (%)
- látszik: látszólag ennyiszer magasabb:
- valójában: valójában ennyiszer több:
- levágva: levágott tengely!
- becsületes: a tengely 0-tól indul

### Adatok
- szavazat A: 52 %
- szavazat B: 48 %
- tengely kezdete: 45 %
- látszólagos arány: 2,33
<!-- kitalált példa (a terv számpéldája). Tengely 45 %-tól: az oszlopok látható magassága 52 − 45 = 7 és 48 − 45 = 3,
     7 : 3 ≈ 2,33. Valódi arány 52 : 48 ≈ 1,083. A lecke kiszámolja és összeveti. -->

## 8. Együtt mozog – de oka-e?
Húsz nyári nap: amikor több fagyi fogyott, többen égtek le. ==Okozza a fagyi a leégést?== Nem: mindkettőt egy **harmadik tényező**, a napos meleg növeli. Hasonló hőmérsékletű napokon az összefüggés eltűnik. ==Az együttmozgás (korreláció) nem bizonyít ok-okozatot.==

> megjegyzés: Cipőméret és helyesírás alsósoknál – mi a harmadik tényező?

### Feliratok
- fagyi cím: Fagylalt és leégés – 20 nyári nap
- fagyi tengely: eladott gombóc
- leégés tengely: leégés miatt orvosnál
- háttér gomb: Mi van a háttérben?
- sáv csúszka: csak ezek a napok
- mind: minden nap
- hőség: meleg, napos idő
- fagyi ok: több fagyi
- leégés ok: több leégés
- okoz: okozza?
- hőmérséklet jelmagyarázat: hűvösebb → melegebb nap
- nincs összefüggés: itt nincs összefüggés

### Adatok
- napi hőmérséklet: 19; 19; 20; 20; 21; 23; 24; 23; 25; 24; 27; 27; 28; 28; 29; 33; 32; 32; 31; 31 °C
- fagyi eladás: 51; 38; 68; 80; 63; 116; 123; 93; 106; 87; 148; 129; 170; 159; 144; 184; 197; 178; 202; 214
- leégés: 4; 2; 1; 3; 5; 4; 8; 7; 5; 6; 6; 9; 10; 8; 12; 15; 10; 10; 13; 12
<!-- kitalált adat, a didaktikai cél szerint szerkesztve: négy hőmérséklet-csoport (19–21, 23–25, 27–29, 31–33 °C),
     csoportonként öt nap. A fagyi és a leégés is a csoport melegével nő, de egy csoporton belül a két szám egymástól
     gyakorlatilag független (a csoporton belüli korrelációs együttható |r| < 0,04) – ezért a sávra szűrve „eltűnik”
     az összefüggés. A korrelációs együttható (r) nem tananyag, a lecke nem írja ki; az összes napra r ≈ 0,86.
     A csoportokat a lecke a hőmérsékletekből képezi (ahol két szomszédos érték közt legalább 2 °C a rés). -->

## 9. Összefoglalás
- **Átlag:** egyensúlyi pont; a kiugró adat elrántja. **Medián:** középső adat; kiugró adatnál beszédesebb. **Módusz:** a leggyakoribb.
- **Szóródás:** terjedelem, szórás, kvartilisek – dobozábra.
- ==Diagramon a tengely 0-tól induljon.==
- ==Az együttmozgás nem ok-okozat.==

### Feliratok
- össz középérték: középérték: hol a közép?
- össz szóródás: szóródás: mennyire szórt?
- össz tengely: tengely 0-tól
- össz korreláció: korreláció ≠ ok-okozat

<!-- Matematikai ellenőrzés (Python, 2026-11-24):
  - 1. bérek: összeg 4370, átlag 485,55… ≈ 485,6; medián 480; módusz 450; az eltérések összege bal/jobb 2050/9 ≈ 227,8.
  - 2. tulajdonossal: 10 370 : 10 = 1037; medián (480 + 500) : 2 = 490; mind a 9 dolgozó az átlag alatt.
  - 3. KSH 2024. október: 637 200 / 529 000 ≈ 1,205 → az átlag kb. 20 %-kal több a mediánnál.
  - 4. jegyek: átlag 4, medián 5, módusz 5.
  - 5. Andi σ = √(10/6) ≈ 1,291; Bori σ = √(148/6) ≈ 4,967; terjedelem 4 és 14.
  - 6. Q₁ = 70, medián 110, Q₃ = 160; terjedelem 200.
  - 7. (52 − 45) : (48 − 45) = 7 : 3 ≈ 2,33; 52 : 48 ≈ 1,083.
  - 8. összes nap r ≈ 0,862; csoportonként r ≈ 0,03; 0,01; −0,01; 0,03 (a lecke ellenőrzi: |r| < 0,1 a sávokban, > 0,8 összesen).
  Tételek: Σ(xᵢ − átlag) = 0 (a panel feladatként kéri a bizonyítást, a lecke nem bizonyítja).
-->
