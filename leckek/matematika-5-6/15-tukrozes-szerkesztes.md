# Honnan tudja a körző, hol a közép? – tengelyes tükrözés, szerkesztések
tantárgy: Matematika · évfolyam: 5–6. · témakör: 15. Transzformációk, szerkesztések

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-5-6/15-tukrozes-szerkesztes.md
  A pontok koordinátái a vászon négyzetrácsán értendők: 1 egység = 1 rácsnégyzet = 1 cm
  (x: balról jobbra 1…22, y: alulról fölfelé 2…25). A pontok betűi (P, P′, A, B, C, O, X…) a kódban vannak.
-->

## Közös

### Feliratok
- tippelj: Tippelj előbb!
- tengely betű: t

## 1. Hajtsd össze!
Festékkel rajzoltunk a lap bal felére, a festék még nedves. **Tippelj előbb!** Ha a lapot a vonal mentén összehajtjuk, milyen lenyomat lesz a jobb oldalon: A vagy B? ==A lenyomat a rajz tükörképe: megfordul.==

> megjegyzés: Próbáljátok ki tintapacával, félbehajtott lapon!

### Feliratok
- tipp kérdés: Milyen lesz a lenyomat?
- hajtásvonal: hajtásvonal
- A kép: A
- B kép: B
- A leírás: ugyanígy áll
- B leírás: megfordul
- A gomb: A: ugyanígy áll
- B gomb: B: megfordul
- festék: nedves festék
- lenyomat: lenyomat
- tipp jó: Jól tippeltél!
- tipp rossz: Nem talált – nézd meg újra!
- eredmény 1: A lenyomat megfordult: ez a tükörkép.
- eredmény 2: Minden pont és lenyomata egyenlő távol van a hajtásvonaltól.

## 2. A tükrözés szabálya
A hajtásvonal a **tükörtengely** (`t`). Húzd a P pontot! A képe, P′, a tengely túloldalán van. ==`PP′` merőleges a tengelyre, és P meg P′ egyenlő távol van tőle.== Ez a **tengelyes tükrözés**. A tengely pontjai helyben maradnak.

> megjegyzés: Négyzetrácson számold a kockákat!

### Feliratok
- tükörtengely: tükörtengely
- húzd a P-t: húzd a P-t vagy a P′-t!
- szabály cím: A tükrözés szabálya
- szabály 1: `PP′ ⊥ t`
- szabály 2: a tengelytől egyenlő távol
- P távolsága: P a tengelytől
- P′ távolsága: P′ a tengelytől
- tengelyen: P a tengelyen van: P′ = P
- rácsnégyzet: 1 rácsnégyzet = 1 cm

### Adatok
- P kiinduló helye: P(6; 17)

## 3. Ferde tengely, fordított körüljárás
Gyakori hiba: ferde tengelynél **vízszintesen** átvinni a pontot. ==A `PP′` szakasz mindig merőleges a tengelyre.== Körzővel: két tengelypontból kört húzunk P-n át; a két kör másik metszéspontja P′. A körüljárás (`A -> B -> C`) megfordul!

> megjegyzés: Miért jó a körző? Lásd az 5. lépést.

### Feliratok
- tévhit vízszintes: Ferde tengelynél vízszintesen tükrözünk?
- cáfolat vízszintes: Nem! Mindig merőlegesen.
- hibás kép: vízszintesen: hibás
- egybeesik: Függőleges tengelynél a kettő egybeesik.
- körüljárás: körüljárás
- megfordul: megfordul!
- tengely csúszka: A tengely dőlésszöge
- hibás gomb: Mutasd a hibás módszert
- hibás gomb ki: Rejtsd el a hibásat
- húzd a tengelyt: forgasd a tengelyt!
- körzős lépés: Körző a tengely egy pontjában, nyílás a csúcsig – két ilyen ív metszi ki a képet.

### Adatok
<!-- A háromszög csúcsai pozitív (az óramutatóval ellentétes) körüljárásúak legyenek: A → B → C. -->
- A csúcs: A(2; 14)
- B csúcs: B(4; 10)
- C csúcs: C(5; 18)
- tengely szöge: 60°

## 4. Szimmetrikus alakzatok
Ha egy alakzatot egy egyenes mentén összehajtunk, és a két fele **fedi egymást**, az egyenes **szimmetriatengely**. ==A tengelyesen szimmetrikus alakzat önmaga tükörképe.== Válassz alakzatot! Tippelj: a téglalap átlója is szimmetriatengely?

> megjegyzés: Keressetek szimmetrikus formát a teremben!

### Feliratok
- téglalap: téglalap
- négyzet: négyzet
- egyenlő szárú: egyenlő szárú háromszög
- szabályos: szabályos háromszög
- téglalap gomb: téglalap
- négyzet gomb: négyzet
- egyenlő szárú gomb: egyenlő szárú △
- szabályos gomb: szabályos △
- tengelyek száma: szimmetriatengely:
- fedi: A két fele fedi egymást.
- nem fedi: nem fedi!
- tévhit átló: A téglalap átlója is szimmetriatengely?
- cáfolat átló: Nem: a két fele nem fedi egymást.

## 5. Egyenlő távol A-tól és B-től
Hol vannak azok a pontok, amelyek **egyenlő távol** vannak A-tól és B-től? Húzd a P pontot! Ha `PA = PB`, P pirosra vált, és nyomot hagy. ==A nyomok egy egyenest adnak: az AB **szakaszfelező merőlegesét**.== B éppen A tükörképe erre az egyenesre.

### Feliratok
- húzd P-t 5: húzd a P-t!
- nyom: Ez a nyom egy egyenes!
- felezőmerőleges: szakaszfelező merőleges
- egyenlő igen: P egyenlő távol van A-tól és B-től.
- egyenlő nem: P nincs egyenlő távol.
- nyom törlése: Töröld a nyomot!

### Adatok
- A pont: A(8; 9)
- B pont: B(14; 17)

## 6. A körző trükkje: szakaszfelező merőleges
A körző **egyenlő távolságot** rajzol. Ugyanakkora nyílással A-ból és B-ből ívet húzunk. A két ív metszéspontja A-tól és B-től egyenlő távol van, tehát a szakaszfelező merőlegesen. Két pont kijelöli az egyenest. ==A körzőnyílás legyen nagyobb AB felénél!==

> megjegyzés: Itt `AB` = {AB hossza}, ezért `r` > {fél AB} kell.

### Feliratok
- szerkesztés cím: Szakaszfelező merőleges
- szerkesztés 1: 1. Körző A-ban: ív fölé és alá
- szerkesztés 2: 2. Ugyanígy B-ből: X₁, X₂
- szerkesztés 3: 3. Vonalzóval X₁X₂ – mérni nem kell!
- tévhit nyílás: A körző nyílása mindegy?
- cáfolat nyílás: Nem! Nagyobb legyen AB felénél.
- túl kicsi: Túl kicsi: az ívek nem metszik egymást!
- körzőnyílás csúszka: Körzőnyílás (r)
- újra gomb: Szerkeszd újra!
- a nyom: az 5. lépés nyoma

### Adatok
- AB hossza: 10 cm
- fél AB: 5 cm
- körzőnyílás: 7 cm
<!-- A lépés eleje egy túl kicsi nyílást mutat (tévhit), utána a jót. -->
- kicsi körzőnyílás: 4 cm

## 7. Szögfelező
A **szögfelező** a szöget két egyenlő részre vágja. Körző a csúcsban: ív a két szárra (P_1, P_2). Ugyanakkora nyílással P_1-ből és P_2-ből ív: X. ==OX a szög szimmetriatengelye.== Miért? O és X is egyenlő távol van P_1-től és P_2-től.

> megjegyzés: Próbáld ki a szögmásolást is!

### Feliratok
- szögfelező cím: Szögfelező
- szögfelező 1: 1. Körző O-ban: ív a két szárra
- szögfelező 2: 2. P₁-ből és P₂-ből egyforma ív: X
- szögfelező 3: 3. Vonalzóval OX
- másolás cím: Szögmásolás
- másolás 1: 1. Ugyanaz az ív O-ból és O′-ből
- másolás 2: 2. A körző átveszi a P₁P₂ nyílást
- másolás 3: 3. Q₁-ből ív: Q₂, vonalzóval O′Q₂
- egyforma fél: a két fél egyforma
- tükör: P₁ és P₂ egymás tükörképe OX-re
- másolat egyforma: a másolat ugyanakkora
- szögfelező gomb: Szögfelező
- másolás gomb: Szögmásolás
- szög csúszka: A szög nagysága
- húzd a szárat: húzd a szárat!

### Adatok
- szög nagysága: 70°

## 8. Merőleges és párhuzamos
Előbb **vázlat**: kézzel, nagyjából, hogy lássuk a tervet. Merőleges P-ből: körív P körül, majd az `e`-n kapott két pont felezőmerőlegese. ==Párhuzamos: merőleges a merőlegesre.== Vonalzóval csak egyenest húzunk, nem mérünk.

> megjegyzés: Ha `e ⊥ m` és `f ⊥ m`, akkor `e ∥ f`.

### Feliratok
- terv: terv
- vázlat: vázlat
- merőleges terv: Merőleges P-ből e-re
- merőleges terv 1: 1. Körív P körül: két pont e-n
- merőleges terv 2: 2. A két pont felezőmerőlegese
- párhuzamos terv: Párhuzamos P-n át
- párhuzamos terv 1: 1. Merőleges P-ből e-re: m
- párhuzamos terv 2: 2. Merőleges m-re P-ben: f
- merőleges gomb: Merőleges
- párhuzamos gomb: Párhuzamos
- e merőleges: `PT ⊥ e`
- e párhuzamos: `f ∥ e`
- egyenlő d: mindenütt egyenlő távol

### Adatok
- P pont: P(9; 18)

## 9. Összefoglalás
**Tengelyes tükrözés:** a pont és a képe egyenlő távol van a tengelytől, összekötő szakaszuk merőleges rá; a körüljárás megfordul. A **szakaszfelező merőleges** pontjai a szakasz két végétől egyenlő távol vannak. ==Szerkesztéshez: vázlat, körző, egyélű vonalzó.==

> megjegyzés: Dinamikus geometria: GeoGebra (ingyenes, magyarul is).

### Feliratok
- össz 1 cím: Tükrözés
- össz 1: PP′ merőleges a tengelyre, a két pont egyenlő távol van tőle.
- össz 2 cím: Körüljárás
- össz 2: A tükörkép körüljárása fordított.
- össz 3 cím: Szimmetria
- össz 3: A szimmetrikus alakzat önmaga tükörképe.
- össz 4 cím: Szakaszfelező merőleges
- össz 4: Pontjai A-tól és B-től egyenlő távol vannak.
- össz 5 cím: Szögfelező
- össz 5: A szög szimmetriatengelye.
- össz 6 cím: Merőleges, párhuzamos
- össz 6: Körzővel és egyélű vonalzóval, mérés nélkül.

<!-- Tanári megjegyzések:
  - Kerettanterv (5–6., 15. Transzformációk, szerkesztések): tengelyes tükrözés és tükörkép szerkesztése,
    tengelyesen szimmetrikus alakzatok, alapszerkesztések (szakaszfelező merőleges, szögfelező, merőleges,
    párhuzamos, szögmásolás), „a szerkesztéshez tervet, előzetes ábrát készít”. A középpontos tükrözés és a
    kicsinyítés/nagyítás a 7–8. évfolyam anyaga, itt nem szerepel.
  - A rajzon 1 rácsnégyzet = 1 cm (a kivetítésen nem méretarányos). A kiírt hosszak a rajzolt geometriából
    számolódnak; a 2. lépésben a pont rácspontra ugrik, ezért a távolság egész cm.
  - A 3. lépés körzős tükrözése: a tengely bármely K pontja egyenlő távol van P-től és P′-től (a tengely a
    PP′ szakaszfelező merőlegese), ezért a K középpontú, P-n átmenő kör átmegy P′-n is. Két ilyen kör két
    pontban metszi egymást: P-ben és P′-ben. A diákoknak ezt az 5. lépés után érdemes visszamondani.
  - Szögfelezés: OP₁ = OP₂ (első ív), XP₁ = XP₂ (egyforma nyílás) → O és X is a P₁P₂ szakaszfelező
    merőlegesén van, így OX az. Erre tükrözve P₁ és P₂ helyet cserél, a két szár egymásba megy: OX a szög
    szimmetriatengelye, ezért a két fél egyenlő.
  - Párhuzamos szerkesztése itt két merőlegessel (körzővel, egyélű vonalzóval). Sok tankönyv két
    vonalzóval (derékszögű vonalzó eltolásával) is tanítja – a kerettanterv „saját eszközök (körző,
    egyélű vonalzó)” kifejezése miatt választottuk a körzős változatot.
  - A téglalap átlója mentén hajtva a két fele nem fedi egymást (csak a négyzetnél). A tévhit gyakori.
  - Jelölés: tükörkép P′ (vessző), tengely t, egyenes e, f, m; a merőleges talppontja T. Tankönyvenként
    eltérhet (pl. tengely betűje „t” vagy „e”).
  - GeoGebra: ingyenes, magyar felülettel is elérhető dinamikus geometriai program (saját ismeret, a lecke
    készítésekor nem ellenőrizve). A kerettanterv kéri: „ismer és használ dinamikus geometriai szoftvereket”.
  - Billentyűzet: Tab – következő húzható pont, W/A/S/D – mozgatás.
-->
