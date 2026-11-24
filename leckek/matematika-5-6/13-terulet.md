# Miért fele a háromszög a paralelogrammának? – kerület, terület, átdarabolás
tantárgy: Matematika · évfolyam: 5–6. · témakör: 13. Mérés és mértékegységek (+ 9. Arányosság, százalékszámítás)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/13-terulet.md
  Feliratban a # jel helyére a lecke egy számot ír (sorban, ha több # van).
  A hosszúság- és területadatok bármely egységben írhatók (m, dm, cm, mm; m², dm², cm², mm²) –
  a lecke átváltja őket. Az eredményeket (kerület, terület) a lecke maga is kiszámolja;
  ha egy itt írt eredmény nem egyezik, piros hibasáv jelenik meg.
-->

## Közös

### Feliratok
- kerület szó: kerület
- terület szó: terület

## 1. Kerítés vagy kert?
Egy kertet bekerítünk, és befüvesítünk. A kerítés hossza a **kerület**: a határ hossza, méterben. A füves rész a **terület**: hány 1 m²-es négyzet fedi le. ==A kerület vonal, a terület felület.==

> megjegyzés: Mihez kell kerület, mihez terület? Szegély, csempe, festés…

### Feliratok
- kerítés gomb: Építsd a kerítést!
- fű gomb: Vesd el a füvet!
- kerület kártya: a határ hossza
- terület kártya: a lefedett rész
- egy méter: 1 m
- egy négyzetméter ikon: 1 m²

### Adatok
<!-- kitalált példa -->
- kert hossza: 6 m
- kert szélessége: 4 m
<!-- Eredmények – a lecke kiszámolja és ellenőrzi: 2 · (6 + 4) = 20 m; 6 · 4 = 24 m². -->
- kert kerülete: 20 m
- kert területe: 24 m²

## 2. Számold a négyzeteket!
A terület azt mutatja, hány **egységnégyzet** fedi le az alakzatot. A téglalapban `b` sor van, minden sorban `a` négyzet: ==`T = a * b`.== A kerület `K = 2 * (a + b)`. Húzd a sarkot! Mikor ugyanaz a két szám?

### Feliratok
- húzd a sarkot: húzd a sarkot!
- téglalap terület képlet: `T = a · b`
- téglalap kerület képlet: `K = 2 · (a + b)`
- sorok: # sor, soronként # négyzet
- ugyanaz a szám: Ugyanaz a szám, más mennyiség!

### Adatok
<!-- A kiinduló téglalap oldalai (a húzható sarok kezdőhelye). -->
- téglalap a: 5 cm
- téglalap b: 3 cm

## 3. Ugyanannyi kerítés, más kert
**Tippelj előbb!** {kerítés hossza} kerítéssel melyik téglalap alakú kert a legnagyobb? A kerület mindig ugyanannyi, a terület mégis változik. ==A négyzet alakú kert a legnagyobb: {legnagyobb kert}.== Húzd a sarkot! A nagyobb kerülethez sem biztos, hogy nagyobb terület tartozik.

### Feliratok
- tippelj 3: Tippelj előbb! Melyik kert a legnagyobb?
- kerítés felirat: kerítés: #
- kert felirat: kert: #
- oldal tengely: a kert egyik oldala (m)
- terület tengely: terület (m²)
- négyzet a legnagyobb: négyzet: # – a legnagyobb!
- tévhit kerület: Nagyobb kerület → nagyobb terület?
- cáfolat kerület: Nem! # m kerítés, mégis csak # m².
- ellenpélda kert: # kert: K = #, T = #

### Adatok
<!-- A kerítés hossza 4-gyel osztható legyen (különben a négyzet oldala nem egész). -->
- kerítés hossza: 24 m
<!-- Eredmény – a lecke kiszámolja: (24 : 4) · (24 : 4) = 6 · 6 = 36 m². -->
- legnagyobb kert: 36 m²

## 4. 1 m² hány cm²?
**Tippelj előbb!** Hány cm² az 1 m²? Az 1 m-es négyzet oldala 10 dm, ezért `10 * 10` = 100 darab 1 dm²-re bontható. Minden 1 dm² újabb `10 * 10` = 100 cm². ==1 m² = 100 · 100 cm² = {egy négyzetméter}.==

### Feliratok
- tippelj 4: Tippelj előbb! Hány cm² az 1 m²?
- oldal m: 1 m
- tipped: A tipped: #
- tévhit m2: 1 m² = 100 cm²?
- cáfolat m2: Nem! A 100 cm² csak ekkora:

### Adatok
<!-- Szomszédos területegységek váltószáma: 10 · 10 = 100 (a lecke ellenőrzi). -->
- váltószám: 100
- egy négyzetméter: 10 000 cm²
<!-- A tippgombok (cm²-ben). -->
- tippek: 100; 1000; 10 000

## 5. Váltsd át!
A szomszédos területegységek között a **váltószám 100**. Ezért a helyiérték-táblázatban minden egységnek két hely jut. ==Egy egységnyi váltásnál a vessző két helyet lép.== Az osztályterem {osztályterem területe}, egy A4-es lap {A4 területe}. Válts egységet!

> megjegyzés: Nagyobb egységek: 1 a (ár) = 100 m², 1 ha (hektár) = 100 a.

### Feliratok
- terem név: osztályterem
- A4 név: A4-es papírlap
- nagyobb egység: ← nagyobb egység, kisebb szám
- kisebb egység: kisebb egység, nagyobb szám →
- váltás szabály: 1 m² = 100 dm², 1 dm² = 100 cm², 1 cm² = 100 mm²

### Adatok
<!-- kitalált példa (a kerettanterv javasolt tevékenysége: az osztályterem adatainak mérése) -->
- osztályterem hossza: 8 m
- osztályterem szélessége: 6 m
- osztályterem területe: 48 m²
<!-- Az A4-es lap mérete 210 mm × 297 mm (ISO 216 szabvány); 21 · 29,7 = 623,7 cm². -->
- A4 rövidebb oldala: 21 cm
- A4 hosszabb oldala: 29,7 cm
- A4 területe: 623,7 cm²

## 6. A ferde téglalap: paralelogramma
Told el a téglalap felső oldalát: **paralelogramma** lesz. Vágd le a sarkát, és told át a túloldalra: újra téglalap! A **magasság** a két párhuzamos oldal távolsága. ==`T = a * m`: alap · magasság, nem alap · oldal.== Húzd a felső oldalt!

### Feliratok
- húzd a felső oldalt: húzd a felső oldalt!
- ferde oldal felirat: ferde oldal: #
- kerület felirat: kerület: #
- terület felirat: terület: #
- tévhit oldal: Terület = alap · ferde oldal = #?
- cáfolat oldal: Nem! alap · magasság = #

### Adatok
<!-- 3–4–5: ha az eltolás 3 cm és a magasság 4 cm, a ferde oldal pontosan 5 cm. -->
- paralelogramma alapja: 8 cm
- paralelogramma magassága: 4 cm
- paralelogramma eltolása: 3 cm
<!-- Eredmények – a lecke kiszámolja: ferde oldal √(3² + 4²) = 5 cm; 8 · 4 = 32 cm²; a tévhit 8 · 5 = 40 cm². -->
- paralelogramma ferde oldala: 5 cm
- paralelogramma területe: 32 cm²
- tévhit szorzat: 40 cm²

## 7. A háromszög: fél paralelogramma
Fordítsd fejjel lefelé a háromszög másolatát, és illeszd mellé: paralelogramma lesz! Ennek területe alap · magasság. ==A háromszög ennek a fele: `T = a * m : 2`.== Húzd a csúcsot! Az alap és a magasság nem változik, így a terület sem.

> megjegyzés: Tompaszögű háromszögnél a magasság talppontja az alap meghosszabbítására esik.

### Feliratok
- húzd a csúcsot: húzd a csúcsot!
- paralelogramma felirat: paralelogramma: #
- háromszög felirat: háromszög: #

### Adatok
- háromszög alapja: 8 cm
- háromszög magassága: 4 cm
<!-- Eredmény – a lecke kiszámolja: 8 · 4 : 2 = 16 cm². -->
- háromszög területe: 16 cm²

## 8. Darabold szét!
Az L alakú kert területe nem egy szorzás. Vágd téglalapokra! ==A darabok területének összege az egész területe.== Bármelyik vágás jó, ki is egészítheted. Más alakú, mégis ugyanakkora, mint a {legnagyobb kert}-es négyzet alakú kert!

> megjegyzés: Vágjatok ki papírból sokszögeket, daraboljátok át, és hasonlítsátok össze a megoldásokat!

### Feliratok
- vízszintes gomb: Vágd el vízszintesen!
- függőleges gomb: Vágd el függőlegesen!
- kiegészítés gomb: Egészítsd ki!
- L kert: L alakú kert
- négyzet kert: négyzet alakú kert
- kerület kiírás: kerület: #
- tévhit alak: Más alak → más terület?
- cáfolat alak: Nem! Mindkettő #.

### Adatok
<!-- kitalált példa: 9 m × 5 m-es telek, a jobb felső sarkából hiányzik egy 3 m × 3 m-es négyzet. -->
- L-kert hossza: 9 m
- L-kert szélessége: 5 m
- hiányzó sarok: 3 m
<!-- Eredmények – a lecke kiszámolja: 9 · 2 + 6 · 3 = 6 · 5 + 3 · 2 = 9 · 5 − 3 · 3 = 36 m²; kerület 2 · (9 + 5) = 28 m.
     A lépés szövege szerint ugyanakkora, mint a 3. lépés négyzet alakú kertje – ha átírod, a lecke ezt is ellenőrzi. -->
- L-kert területe: 36 m²
- L-kert kerülete: 28 m

## 9. Összefoglalás
- A **kerület** a határ hossza, a **terület** a lefedett egységnégyzetek száma.
- 1 m² = 100 dm² = 10 000 cm².
- Téglalap: `T = a * b`. Paralelogramma: `T = a * m`. Háromszög: `T = a * m : 2`.

==Átdarabolva a terület nem változik.==

### Feliratok
- paralelogramma képlet: `T = a · m`
- háromszög képlet: `T = a · m : 2`
- összegzés 1: A kerület a határ hossza, a terület a lefedett rész.
- összegzés 2: Téglalap:
- összegzés 3: Ugyanakkora kerület, más terület: a négyzet a legnagyobb.
- összegzés 4: A területegységek váltószáma 100.
- összegzés 5: Paralelogramma: alap · magasság.
- összegzés 6: Háromszög: a paralelogramma fele.

<!-- Tanári megjegyzések:
  - Kitalált számok: a kertek (6 m × 4 m, 24 m kerítés, 9 m × 5 m-es L), az osztályterem (8 m × 6 m),
    a téglalap, a paralelogramma és a háromszög méretei. Valós adat: az A4-es lap 210 mm × 297 mm (ISO 216).
  - Egyszerűsítések: a 2. és 3. lépésben csak egész oldalhosszú téglalapok vannak (a fogantyú rácsra ugrik);
    a 6–7. lépésben a csúcs egész centiméterekre ugrik. A 3. lépés „a négyzet a legnagyobb” állítását a lecke
    csak egész oldalú kertekre mutatja meg (bizonyítás nincs).
  - Jelölés: a terület T, a kerület K, az alap a, a magasság m. Egyes tankönyvek a magasságot m_a-val, a
    háromszög területét (a · m_a) / 2 alakban írják; 5–6. évfolyamon „alap · magasság : 2” is szokásos.
  - A 7. lépés „fejjel lefelé fordított másolata” középpontos tükrözés (180°-os elforgatás); ezt a szót a lecke
    nem használja, mert a középpontos tükrözés 7–8. évfolyamos anyag.
  - A trapéz, a rombusz és a deltoid területe (speciális négyszögek) 7–8. évfolyamos anyag, ezért kimaradt.
-->
