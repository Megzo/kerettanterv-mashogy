# Hogyan fedi le a csempe a síkot? – tükrözés, forgatás, eltolás, parketta
tantárgy: Matematika · évfolyam: 9–10. · témakör: 15. Transzformációk, szerkesztések (+ 13. Négyszögek, sokszögek)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/12-egybevagosag-parketta.md
  A pontok és alakzatok betűi (A, B, C, A′, F, F′, F″, O, P, t₁, t₂, n) és a szögek betűi (α, β, γ, δ, φ)
  a vásznon kódban rögzítettek. Színek: az eredeti alakzat (F) tinta, az első kép (F′) kékeszöld, a második kép (F″) cinóber (az 1. lépésben a tükörkép cinóber);
  a 6. lépésben α kékeszöld, β okker, γ cinóber, δ zöld.
  A mintázatok (F betű, saját csempe, „lény” a csempén) saját, kóddal rajzolt ábrák – nem Escher- vagy
  Vasarely-művek (jogvédettek, a lecke csak a módszert mutatja).
-->

## Közös

### Feliratok
- mérés: mérés
- bizonyítás: bizonyítás
- szemléltetés: szemléltetés
- újra gomb: Újra
- pozitív: pozitív körüljárás
- negatív: negatív körüljárás
- igen: igen
- nem: nem

## 1. Tükrözés: mi marad meg, mi fordul meg?
Tükrözzük az F-et a t tengelyre! Minden pont és a képe egyforma messze van a tengelytől. A távolságok és a szögek **megmaradnak**, a **körüljárás** viszont megfordul. ==A tükörkép a síkban csúsztatva, forgatva nem vihető rá az eredetire== – mint a jobb kesztyű a balra. Húzd a tengely pontjait!

### Feliratok
- cím 1: Mi marad meg a tükrözésnél?
- húzd a tengelyt: húzd a tengelyt!
- tükrözés: tengelyes tükrözés
- távolság marad: a távolság megmarad
- szög marad: a szög megmarad
- körüljárás: a körüljárás megfordul
- ráforgatás: A-t és B-t ráforgatjuk A′-re és B′-re…
- nem fedi: …de C nem kerül C′-re!
- tévhit tükör: A tükörkép ugyanaz az alakzat.
- cáfolat tükör: Nem vihető rá: fordított körüljárás!

## 2. Két párhuzamos tükör = eltolás
Tükrözzük F-et a `t_1`, majd a `t_2` tengelyre! A második tükrözés visszafordítja a körüljárást, így F″ már nem tükörkép: ==F″ az F eltoltja, a tengelyek távolságának kétszeresével.== Minden pont ugyanazzal a nyíllal mozdul el – ez az eltolás **vektora**. Fordított sorrendben a vektor is megfordul.

### Feliratok
- cím 2: Két párhuzamos tükör
- vektor: eltolásvektor
- tévhit két tükör: Két tükrözés = egy tükrözés.
- cáfolat két tükör: F″ körüljárása pozitív: eltolás!
- biz p1: `PP′ = 2a`, `P′P″ = 2b`
- biz p2: `a + b = d` (a tengelyek távolsága)
- biz p3: így `PP″ = 2d`, és `PP″ ⊥ t_1`
- távolság csúszka: a tengelyek távolsága
- sorrend gomb: Fordított sorrend
- sorrend 1: előbb `t_1`, aztán `t_2`
- sorrend 2: előbb `t_2`, aztán `t_1`

### Adatok
<!-- A kezdő helyzet: d = 3,5 cm → az eltolás 7 cm (a lecke számolja és ellenőrzi). -->
- tengelyek távolsága: 3,5 cm
- eltolás hossza: 7 cm

## 3. Két metsző tükör = forgatás
Ha a tengelyek O-ban, φ szögben metszik egymást, a két tükrözés eredménye **O körüli forgatás**. O helyben marad, és `OP = OP′ = OP″`. A tükrözések a szögeket megkettőzik: 2α és 2β, ahol `α + β = φ` – ==a forgásszög `2φ`.== Ha `φ = 90°`, a forgatás 180°-os: ez a **középpontos tükrözés**.

### Feliratok
- cím 3: Két metsző tükör
- forgásszög: forgásszög
- biz r1: O mindkét tengelyen rajta van.
- biz r2: `OP = OP′ = OP″`
- biz r3: `POP′` szög `= 2α`, `P′OP″` szög `= 2β`
- biz r4: `α + β = φ`, a forgásszög `2φ`
- szög csúszka: a tengelyek szöge
- 90 gomb: 90°: középpontos tükrözés
- középpontos: 180°-os forgatás = középpontos tükrözés
- húzd a t2-t: húzd a második tengelyt!

### Adatok
<!-- A kezdő helyzet: φ = 60° → a forgásszög 120° (a lecke a rajzolt pontokból méri és ellenőrzi). -->
- tükrök szöge: 60°
- forgatás szöge: 120°

## 4. A sokszög szögeinek összege
A konvex n-szög egy csúcsából húzzunk átlókat: a sokszög `n − 2` háromszögre esik szét, és ezek szögei együtt éppen a sokszög szögeit adják. ==A belső szögek összege `(n − 2) · 180°`.== Minden csúcsnál belső + külső szög = 180°, ezért a **külső szögek összege** mindig 360°.

> megjegyzés: Feladat: miért `n(n − 3)/2` az n-szög átlóinak száma?

### Feliratok
- cím 4: Hány fok a szögek összege?
- n csúszka: a csúcsok száma (n)
- másik alak gomb: Másik alak
- húzd a csúcsokat: húzd a csúcsokat!
- biz s1: Egy csúcsból `n − 3` átló,
- biz s2: így `n − 2` háromszög keletkezik.
- biz s3: Szögeik együtt a sokszög szögei:
- képlet szögösszeg: `(n − 2) · 180°`
- belső összeg: belső szögek összege:
- külső összeg: külső szögek összege:
- külső szögek: külső szögek

## 5. Melyik szabályos sokszög parkettáz?
**Parketta**: egybevágó lapok hézag és átfedés nélkül fedik le a síkot. Egy csúcs körül a szögek összege 360°, ezért a belső szögnek a 360° osztójának kell lennie. ==Szabályos sokszögből csak a háromszög, a négyzet és a hatszög parkettáz.== Az ötszögből három fér el ({ötszög belső szöge} mindegyik), {ötszög rése} rés marad.

### Feliratok
- cím 5: Melyik szabályos sokszög parkettáz?
- n csúszka 5: oldalak száma (n)
- belső szög: belső szög
- rés: rés
- átfedne: a következő átfedne
- pontos: pontosan 360°: parkettáz!
- nem parkettáz: nem parkettáz
- fej oldalak: n
- fej szög: belső szög
- fej hányados: hányados
- fej parketta: parketta?
- tévhit ötszög: Szabályos ötszög is jó – lásd a focilabdát!
- cáfolat ötszög: A labda gömb, hatszögek is vannak rajta.

### Adatok
<!-- (5 − 2) · 180° : 5 = 108°; 360° − 3 · 108° = 36° (a lecke számolja és ellenőrzi). -->
- ötszög belső szöge: 108°
- ötszög rése: 36°

## 6. Bármely háromszög és négyszög parkettáz
Forgassuk el a négyszöget 180°-kal egy oldal felezőpontja körül: a két lap ennél az oldalnál pontosan illeszkedik. Ezt ismételve hézag nélkül lefedjük a síkot, és minden csúcsban mind a négy szög találkozik: ==`α + β + γ + δ = 360°`.== Homorú négyszögre is működik! A háromszögnél hat szög, kétszer `α + β + γ`.

### Feliratok
- cím 6: Bármely háromszög és négyszög?
- háromszög gomb: Háromszög
- négyszög gomb: Négyszög
- homorú gomb: Homorú négyszög
- húzd a csúcsokat 6: húzd a csúcsokat!
- forgatás 180: 180°-os forgatás egy oldal felezőpontja körül
- egy csúcsban: egy csúcsban találkozó szögek:
- oldalak illeszkednek: Az oldalak párban illeszkednek.
- tévhit szabályos: Csak szabályos sokszög parkettázhat.
- cáfolat szabályos: Bármely háromszög és négyszög is jó!

## 7. Rajzolj saját csempét!
Húzd az alsó él pontjait: a görbe eltolva a felső élre is átkerül. Ami kiáll, annyi be is horpad, így ==a csempe területe nem változik, és a lapok hézag nélkül illeszkednek.== A bal él eltolással vagy **csúsztatva tükrözéssel** (tükrözés, majd eltolás a tengely mentén) kerülhet át. Ez M. C. Escher módszere, a minta saját.

### Feliratok
- cím 7: Rajzolj saját csempét!
- eltolás gomb: Eltolással
- csúsztatott gomb: Csúsztatva tükrözéssel
- kezdő gomb: Kezdő minta
- húzd a pontokat: húzd a pontokat!
- alsó felső: alsó él → felső él: eltolás
- bal jobb eltolás: bal él → jobb él: eltolás
- bal jobb csúsztatott: bal él → jobb él: csúsztatva tükrözés
- csúsztatott def: tükrözés, majd eltolás a tengely mentén
- terület: a csempe területe
- tükrözött lapok: minden második oszlop tükörkép

### Adatok
<!-- A kiinduló négyzet oldala; a csempe területe = a négyzeté (a lecke a rajzolt csempéből számolja). -->
- csempe oldala: 4 cm
- csempe területe: 16 cm²

## 8. Kitekintés: csempe, amely sosem ismétlődik
Eddigi parkettáink **periodikusak**: van olyan eltolás, amely az egész mintát önmagára viszi. Húzd a nyilat, és keress ilyet! {kalap éve}-ban egy 13 oldalú lapot találtak, a „kalapot”: ==lefedi a síkot, de csak nem periodikusan== – sehogy sem tolható el önmagára. Ilyen lapot évtizedekig kerestek.

> megjegyzés: Érdekesség: a konvex ötszögeknek {ötszögtípusok} parkettázó típusa ismert; a listát 2017-ben számítógéppel igazolták.

### Feliratok
- cím 8: Csempe, amely sosem ismétlődik
- húzd a nyilat: húzd a nyíl végét!
- fedi: fedi önmagát: periodikus!
- nem fedi 8: nem fedi önmagát
- a te csempéd: a te csempéd a 7. lépésből
- kalap cím: a „kalap”
- kalap 1: 13 oldalú, 8 egyforma „sárkányból”
- kalap 2: lefedi a síkot, de sosem periodikusan
- kalap 3: a tükörképe is kell hozzá
- tükörkép: tükörkép

### Adatok
<!-- Forrás: D. Smith, J. S. Myers, C. S. Kaplan, C. Goodman-Strauss: An aperiodic monotile,
     arXiv:2303.10798 (2023. március), Combinatorial Theory 4(1) (2024). A „kalap” 8 „sárkányból”
     (a szabályos hatszögrács hatszögeit a középpontból az oldalfelezőkhöz húzott szakaszok 6 deltoidra
     bontják) álló, 13 oldalú sokszög; a lefedéshez tükrözött példány is kell (a tükrözés nélküli
     „spectre” ugyanazon szerzők 2023. májusi cikkében). Ellenőrizendő tankönyvi/ismeretterjesztő forrással. -->
- kalap éve: 2023
- kalap oldalai: 13
<!-- Konvex ötszögek: 15 parkettázó típus; a 15. típust 2015-ben találták (C. Mann, J. McLoud-Mann,
     D. Von Derau), a lista teljességét M. Rao 2017-ben számítógépes bizonyítással igazolta. Ellenőrizendő. -->
- ötszögtípusok: 15

## 9. Összefoglaló
- a tükrözés megtartja a távolságot és a szöget, de megfordítja a körüljárást
- két tükrözés: párhuzamos tengelyeknél eltolás (`2d`), metszőknél forgatás (`2φ`)
- a konvex n-szög belső szögeinek összege `(n − 2) · 180°`, a külsőké 360°
- szabályos sokszögből a háromszög, a négyzet és a hatszög parkettáz, de bármely háromszög és négyszög is

==Parketta = egy csúcs körül pontosan 360°.==

### Feliratok
- össz tükör cím: Tengelyes tükrözés
- össz tükör 1: távolság, szög: marad
- össz tükör 2: körüljárás: megfordul
- össz két cím: Két tükrözés egymás után
- össz két 1: párhuzamos tengelyek: eltolás `2d`
- össz két 2: metsző tengelyek: forgatás `2φ`
- össz csúszt cím: Csúsztatva tükrözés
- össz csúszt 1: tükrözés + eltolás a tengely mentén
- össz szög cím: Szögösszeg
- össz szög 1: belső: `(n − 2) · 180°`
- össz szög 2: külső: 360°
- össz park cím: Parketta
- össz park 1: szabályos: 3-, 4- és 6-szög
- össz park 2: bármely háromszög, négyszög
- össz saját cím: Saját csempe
- össz saját 1: élpárok: eltolás vagy csúsztatott tükrözés

<!-- Matematikai ellenőrzés (Python 3 és a lecke L.checks()-e, 2026-11-24):
  - Tengelyes tükrözés (1. lépés): a lecke a rajzolt pontokból méri, hogy AC = A′C′, ABC∢ = A′B′C′∢,
    a PP′ szakasz felezőpontja a tengelyen van és PP′ ⊥ t; az előjeles terület (körüljárás) előjele megfordul.
    Az F betű ABC háromszögénél AC = √(2,4² + 4²) ≈ 4,66 cm, ABC∢ ≈ 111,8°. A „ráforgatás”: az az irányítástartó
    mozgás, amely A-t A′-be, B-t B′-be viszi, C-t a C′ A′B′-re vett tükörképébe viszi (≠ C′).
  - Két párhuzamos tengely (2. lépés): P a t₁-től a, P′ a t₂-től b távolságra; ha P, P′ a rajz szerinti oldalon
    van, PP′ = 2a, P′P″ = 2b, a + b = d ⇒ PP″ = 2d (általában előjeles távolságokkal ugyanez). d = 3,5 cm → 7 cm.
    A lecke ellenőrzi, hogy F″ = F + 2d·n (n a t₁-ről a t₂ felé mutató normális), és hogy fordított sorrendben −2d·n.
  - Két metsző tengely (3. lépés): O mindkét tengelyen van ⇒ fixpont; OP = OP′ = OP″; ha P a t₁-től α, P′ a t₂-től
    β szögre van (a rajz elrendezésében), akkor POP′∢ = 2α, P′OP″∢ = 2β, α + β = φ ⇒ 2φ. φ = 60° → 120°;
    φ = 90° → 180° (középpontos tükrözés). A lecke a rajzolt P, P″ pontokból méri a forgásszöget.
  - Szögösszeg (4. lépés): konvex n-szög, egy csúcsból n − 3 átló, n − 2 háromszög ⇒ (n − 2) · 180°;
    n = 3…8: 180°, 360°, 540°, 720°, 900°, 1080°. Külső szögek: n · 180° − (n − 2) · 180° = 360°.
    Átlók: n(n − 3)/2 → 5 → 5, 6 → 9, 10 → 35. A lecke a rajzolt (húzható, konvexnek tartott) sokszög szögeit
    összegzi.
  - Szabályos sokszögek (5. lépés): belső szög (n − 2) · 180°/n: 60°, 90°, 108°, 120°, ≈ 128,57°, 135°;
    360° : szög = 6; 4; ≈ 3,33; 3; 2,8; ≈ 2,67 – egész csak n = 3, 4, 6 esetén. Ötszög: 3 · 108° = 324°, rés 36°.
    Nem él-él illeszkedésnél (egy csúcs egy másik lap oldalán) a csúcsnál 180°-nak kellene kijönnie – ez sem
    sikerül az 5, 7, 8 oldalúval (108°, 128,57°, 135° egyike sem osztója a 180°-nak), így az állítás általában is igaz.
  - Négyszög-parketta (6. lépés): az oldalfelező pontok körüli középpontos tükrözések közül kettő egymásutánja
    eltolás a két átló vektorával (u = C − A, v = D − B), ezért a lapok: Q + i·u + j·v és (B + C − Q) + i·u + j·v.
    Minden rácscsúcsban a négy szög (egy-egy példányban) találkozik, összegük 360°. Háromszögnél u = B − A,
    v = C − A, hat szög: 2 · 180°. A lecke a rajzolt lapokból ellenőrzi, hogy a kiemelt csúcsban a szögek
    összege 360°.
  - Saját csempe (7. lépés): az alsó és a felső él egymás eltoltja, ezért a kiálló és a behorpadó rész egybevágó:
    a terület = 4² = 16 cm² (cipőfűző-képlettel a lecke számolja). Csúsztatott tükrözésnél a jobb él a bal él
    képe a vízszintes középvonalra tükrözve és 4 cm-rel eltolva; minden második oszlop tükörkép. A lecke
    ellenőrzi, hogy a szomszédos lapok közös élei pontosan egybeesnek.
  - Kalap (8. lépés): a csúcsok hatszögrács-koordinátái a szerzők nyilvános „hatviz” programjának
    kalap-körvonalát követik (ellenőrizendő a cikk 1. ábrájával); a lecke ellenőrzi: 13 csúcs, a terület
    = 8 deltoid (8 · √3 egység², a rács hatszögeinek oldala 2 egység), a körvonal nem metszi önmagát.
-->
