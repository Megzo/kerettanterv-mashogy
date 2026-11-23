# Hol legyen a mentőállomás? – a háromszög nevezetes pontjai és körei
tantárgy: Matematika · évfolyam: 9–10. · témakör: 12. Háromszögek (+ 11. Geometriai alapismeretek)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/10-nevezetes-pontok.md
  A csúcsok (A, B, C), a segédpontok (P, X₁, X₂, D, F) és a ρ betűje a kódban vannak.
  A nevezetes pontok betűi (K, O, S, M) itt állíthatók – tankönyvenként eltérnek. Ha átírod őket,
  a bizonyítás soraiban és a panelszövegben is írd át!
-->

## Közös

### Feliratok
- város A: Budapest
- város B: Debrecen
- város C: Szeged
- Szolnok név: Szolnok
- K betű: K
- O betű: O
- S betű: S
- M betű: M
- mérés: mérés
- bizonyítás: bizonyítás
- vázlatos: vázlatos térkép · mai határok
- egy egyenesen: A három pont egy egyenesen van – nincs háromszög.
- f AB: `f_AB`
- f BC: `f_BC`
- f AC: `f_AC`
- általános gomb: általános
- tompaszögű gomb: tompaszögű

### Adatok
<!-- Koordináták: a városközpontok szokásos (Wikipédia-) koordinátái, 2 tizedesre kerekítve; 2026-11-23. -->
- Budapest: 47,50° É, 19,04° K
- Debrecen: 47,53° É, 21,63° K
- Szeged: 46,25° É, 20,14° K
- Szolnok: 47,17° É, 20,20° K
<!-- A lecke a koordinátákból számolja (Lambert-féle kúpvetület, a térkép vetülete). Python-ellenőrzés
     (2026-11-23): a sík vetületen 104,4 km, gömbi (haversine) távolsággal 104,5 km; az eltérés < 0,1 %.
     Ha a fenti koordinátákat átírod, ezt is ellenőrizd – a lecke piros sávval jelez, ha 0,5 km-nél többel eltér. -->
- körülírt kör sugara: kb. 104 km
- súlypont aránya: 2 : 1
- Euler-arány: 1 : 2

## 1. Hol legyen a mentőállomás?
Mentőállomást tervezünk, amely **Budapesttől, Debrecentől és Szegedtől egyformán messze** van. Húzd a piros keresztet! Két távolságot könnyű kiegyenlíteni, a harmadik mindig elszökik. ==Próbálgatással csak közelítünk – kell egy módszer.==

> megjegyzés: Légvonalban mérünk. Próbáld ki a „középre” gombot is!

### Feliratok
- cél: Egyformán messze mindhárom várostól?
- húzd az állomást: húzd az állomást!
- távolságok: Távolság légvonalban
- eltérés: legnagyobb − legkisebb:
- egyforma: Egyforma messze!
- középre gomb: Tedd „középre” (átlag)
- vissza gomb: Vissza a kezdőhelyre

## 2. Szerkesszünk: szakaszfelező merőleges
Kezdjük két várossal! Körzővel **ugyanakkora** sugarú ívet húzunk A-ból és B-ből. A két metszéspont mindkét várostól r távolságra van. A rajtuk átmenő egyenes az AB **szakaszfelező merőlegese**: ==felezi a szakaszt, és merőleges rá.== Mikor nem metszik egymást az ívek?

### Feliratok
- szerkesztés cím: Szakaszfelező merőleges
- szerkesztés 1: 1. Körív A középponttal, r sugárral
- szerkesztés 2: 2. Ugyanilyen körív B-ből
- szerkesztés 3: 3. A két metszésponton át egyenes
- túl kicsi: r ≤ AB/2: nincs metszéspont!
- körzőnyílás csúszka: Körzőnyílás (r)
- újra gomb: Szerkeszd újra!

## 3. Egyenlő távolság = ponthalmaz
Húzd a P pontot! Ha a merőlegesen van, `PA = PB`. Ha lelép róla, az egyik város közelebb kerül. ==A szakaszfelező merőleges azoknak a pontoknak a halmaza, amelyek A-tól és B-től egyenlő távolságra vannak.== Miért? Az egyenesre tükrözve A és B helyet cserél, P helyben marad.

> megjegyzés: Ez mérés. A tükrözéses érv minden pontra igaz.

### Feliratok
- közelebb A: Budapesthez közelebb
- közelebb B: Debrecenhez közelebb
- húzd a P-t: húzd a P-t!
- rajta van: P az egyenesen van.
- nincs rajta: P nincs az egyenesen.
- ponthalmaz: `P ∈ f_AB <=> PA = PB`
- P csúszka: P helye a merőlegesen
- lépj le gomb: Lépj le a vonalról!
- vissza a vonalra gomb: Vissza a vonalra

## 4. Miért metszik egymást egy pontban?
Szerkesszük meg BC felezőmerőlegesét is! A két egyenes metszéspontja K. Ez a pont az elsőn rajta van, ezért `KA = KB`; a másodikon is, ezért `KB = KC`. Így `KA = KC`, tehát K a harmadik merőlegesen is rajta van. ==K mindhárom várostól {körülírt kör sugara} távolságra van: ez a körülírt kör középpontja.==

### Feliratok
- bizonyítás 1: `K ∈ f_AB => KA = KB`
- bizonyítás 2: `K ∈ f_BC => KB = KC`
- bizonyítás 3: `=> KA = KC`
- bizonyítás 4: `=> K ∈ f_AC`
- sugár: `r = KA = KB = KC`
- állomás: mentőállomás
<!-- A K Szolnoktól kb. 11 km-re keletre van, Tiszapüspöki és Törökszentmiklós közelében (Python, a koordinátákból;
     a kisebb települések koordinátái nincsenek a leckében – ellenőrizendő, ha a szöveg pontosabb helyet mond). -->
- szolnok szöveg: Szolnoktól kb. 11 km-re keletre

## 5. Tompa- és derékszög: hová kerül a K?
Húzd a csúcsokat, vagy válassz gombot! Hegyesszögű háromszögben K belül van. **Derékszögűben** az átfogó felezőpontjára esik, **tompaszögűben** kilép a háromszögből. ==A körülírt kör középpontja nem mindig a háromszögben van.== A derékszögű eset a Thalész-tétel – erről szól a 11. lecke.

### Feliratok
- húzd a csúcsot: húzd a csúcsokat!
- tévhit K: A K mindig a háromszögön belül van.
- cáfolat K: Tompaszögnél kívül esik!
- hol a K: Hol van a K?
- K belül: hegyesszögű: K belül
- K átfogón: derékszögű: K az átfogón
- K kívül: tompaszögű: K kívül
- legnagyobb szög: legnagyobb szög
- thalész: Az átfogó felezőpontja! Thalész-tétel → 11. lecke
- hegyesszögű gomb: hegyesszögű
- derékszögű gomb: derékszögű

## 6. Szögfelezők és a beírt kör
A **szögfelező** pontjai a két szögszártól egyenlő távolságra vannak. Ezért a három belső szögfelező is egy pontban metszi egymást: O-ban. A bizonyítás ugyanaz, mint a K-nál. O mindhárom oldaltól ugyanannyira van: ez a **beírt kör** középpontja. ==A szögfelező általában nem felezi a szemközti oldalt!==

### Feliratok
- tévhit szögfelező: A szögfelező felezi a szemközti oldalt.
- cáfolat szögfelező: Általában nem: D ≠ F
- beírt kör cím: Beírt kör
- szögfelező lépés: Szögfelező körzővel: ív a csúcsból, majd a két metszéspontból egyforma ívek.
- egyenlő távol: O mindhárom oldaltól ρ távolságra van.
- egyenlő szárú gomb: egyenlő szárú (AB = AC)

## 7. Súlyvonal és súlypont
A **súlyvonal** a csúcsot a szemközti oldal felezőpontjával köti össze. A három súlyvonal egy pontban, a **súlypontban** (S) metszi egymást. Húzd a tűt! A kartonlap csak az S-en egyensúlyoz. ==S mindegyik súlyvonalat {súlypont aránya} arányban osztja.== Ezt itt csak mérjük, nem bizonyítjuk.

### Feliratok
- tű: tű
- billen: billen
- egyensúlyban: egyensúlyban!
- húzd a tűt: húzd a tűt!
- súlyvonal cím: Súlyvonalak
- tábla fej: csúcs–S és S–felezőpont
- arány szöveg: mindhárom súlyvonalon csúcs–S : S–F =
- tű gomb: Tű a súlypontra
- másik gomb: Másik háromszög

## 8. Magasságpont és az Euler-egyenes
A **magasságvonal** a csúcsból merőleges a szemközti oldal egyenesére; a három metszéspontja a **magasságpont** (M). Tompaszögnél kívül esik. Kapcsold ki-be a pontokat! Általában négy különböző pont, de K, S és M mindig egy egyenesen van (**Euler-egyenes**). ==`KS : SM = 1 : 2`== – ezt is csak mérjük.

### Feliratok
- tévhit egybe: A nevezetes pontok egybeesnek.
- cáfolat egybe: Csak a szabályos háromszögben!
- pontok cím: Nevezetes pontok
- K jelentés: körülírt kör középpontja
- O jelentés: beírt kör középpontja
- S jelentés: súlypont
- M jelentés: magasságpont
- Euler-egyenes: Euler-egyenes
- Euler gomb: Euler-egyenes
- szabályos gomb: szabályos
- egybeesnek: Szabályos háromszög: mind a négy pont egybeesik.

## 9. Összefoglaló
- oldalfelező merőlegesek → K, a **körülírt kör** középpontja
- szögfelezők → O, a **beírt kör** középpontja
- súlyvonalak → S, `2 : 1` arány
- magasságvonalak → M
- K, S, M: Euler-egyenes

==A mentőállomás helye: K.==

### Feliratok
- össz K név: körülírt kör középpontja
- össz K 1: az oldalfelező merőlegesek metszéspontja
- össz K 2: mindhárom csúcstól egyforma messze
- össz O név: beírt kör középpontja
- össz O 1: a belső szögfelezők metszéspontja
- össz O 2: mindhárom oldaltól egyforma messze
- össz S név: súlypont
- össz S 1: a súlyvonalak metszéspontja
- össz S 2: a súlyvonalakat 2 : 1 arányban osztja
- össz M név: magasságpont
- össz M 1: a magasságvonalak metszéspontja
- össz M 2: tompaszögnél a háromszögön kívül

<!-- Matematikai ellenőrzés (Python 3, 2026-11-23):
  - Körülírt kör a három városra: a lecke vetületén (Lambert-féle szögtartó kúpvetület, lon0 = 19,5°, álló
    szélességek 45° és 49°) középpont ≈ 47,18° É, 20,34° K; sugár 104,4 km (a .md 2 tizedesre kerekített
    koordinátáival), gömbi távolsággal 104,5 km. A pontosabb (4 tizedes) koordinátákkal 104,3 km.
    Oldalak: Budapest–Debrecen ≈ 194 km, Debrecen–Szeged ≈ 182 km, Szeged–Budapest ≈ 162 km; a háromszög
    szögei ≈ 60,5°, 50,9°, 68,6° (hegyesszögű, ezért K belül van). A középpont Szolnoktól ≈ 11 km-re keletre.
    A terv „kb. 105 km, Törökszentmiklós mellett” értéke ezzel egyezik (Tiszapüspöki ≈ 4,5 km, Törökszentmiklós
    ≈ 5,6 km a mi koordinátáinkkal – a két kis település koordinátája nincs forrással ellenőrizve).
  - A lecke minden kiírt hossza, szöge és aránya a rajzolt geometriából számolódik; az L.checks ellenőrzi:
    KA = KB = KC; K az f_AC-n; O mindhárom oldaltól ρ; O a három szögfelezőn; BD : DC = AB : AC
    (szögfelezőtétel – a lecke nem mondja ki); csúcs–S : S–felezőpont = 2 : 1 mindhárom súlyvonalon;
    M mindhárom magasságvonalon; K, S, M egy egyenesen, KS : SM = 1 : 2; derékszögnél K = az átfogó
    felezőpontja; X₁A = X₁B = r a szerkesztésben.
  - Tételek: szakaszfelező merőleges és szögfelező mint ponthalmaz; a felezőmerőlegesek és a belső
    szögfelezők egy pontban metszik egymást (a lecke bizonyítja – a szögfelezőkét a panel csak utalással);
    a súlypont 2 : 1 aránya és az Euler-egyenes: a lecke NEM bizonyítja, „mérés” bélyeggel mutatja.
  - Tankönyvi jelölés: a körülírt kör középpontja sok tankönyvben O vagy K, a beírt köré O vagy K, a beírt
    kör sugara ρ vagy r – a betűk a Feliratok alatt átírhatók.
  - Térkép: Natural Earth (közkincs), „Made with Natural Earth”; mai határok, vázlatos.
-->
