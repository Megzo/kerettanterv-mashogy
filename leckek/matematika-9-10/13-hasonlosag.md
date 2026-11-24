# Milyen magas a torony? – nagyítás, hasonlóság, terület és térfogat
tantárgy: Matematika · évfolyam: 9–10. · témakör: 15. Transzformációk, szerkesztések (+ 7. Arányosság)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/13-hasonlosag.md
  A pontok betűi (O, A, B, C, A′, B′, C′, A″…), a λ, a H, T, b, t, a, m jel és a tengelyszámok a vásznon
  kódban rögzítettek. A vektort a vásznon a betűk fölötti nyíl jelöli: a feliratokban „→OA” alakban
  írd (a nyíl a betűpár elé kerül, a lecke a betűk fölé rajzolja).
  Színek: az eredeti alakzat tinta, a kép cinóber, a második kép kékeszöld.
  Ahol egy feliratban # áll, oda a lecke számot ír.
-->

## Közös

### Feliratok
- mérés: mérés
- bizonyítás: bizonyítás
- kitalált adat: kitalált adat
- vázlat: vázlat, nem méretarányos
- hagyomány: a hagyomány szerint
- újra gomb: Újra

## 1. Nagyítás egy pontból
Válassz egy **O** pontot és egy λ számot! Minden P pont képe az OP félegyenesen van, és `OP′ = λ · OP`. Ez a **középpontos hasonlóság**, λ az **aránya**. Ha `λ > 1`, nagyít; ha `λ < 1`, kicsinyít – ==a kicsinyítés is hasonlóság==. Húzd az O pontot, és állítsd a λ-t!

> megjegyzés: Kérdezd meg: hol van a kép, ha O a háromszög belsejében van?

### Feliratok
- cím 1: Nagyítás egy O pontból
- húzd az O-t: húzd az O pontot!
- arány csúszka: a hasonlóság aránya (λ)
- nagyít: `λ > 1`: nagyítás
- kicsinyít: `λ < 1`: kicsinyítés
- helyben: `λ = 1`: minden pont helyben marad
- arányok cím: a képpont és a pont távolsága O-tól
- definíció: P′ az OP félegyenesen, `OP′ = λ · OP`

### Adatok
<!-- A kezdő arány; az 1–2. lépés ezzel indul. -->
- arány: 2

## 2. Mi marad meg?
Vektorokkal: ha `OA′ = λ · OA` és `OB′ = λ · OB`, akkor kivonva `A′B′ = λ · AB`. ==Minden szakasz képe párhuzamos az eredetivel, és λ-szor olyan hosszú==, ezért a szögek sem változnak. Ha a képet még el is mozgatjuk, az eredmény **hasonló** az eredetihez: `ABC ∼ A″B″C″`.

> megjegyzés: A szögek a párhuzamos szárú szögek miatt egyenlők.

### Feliratok
- cím 2: Mi marad meg a nagyításnál?
- biz cím: Miért párhuzamos és λ-szoros?
- biz 1: →OA′ = λ · →OA
- biz 2: →OB′ = λ · →OB
- biz 3: →A′B′ = →OB′ − →OA′
- biz 4: = λ · (→OB − →OA) = λ · →AB
- következmény: `A′B′ ∥ AB` és `A′B′ = λ · AB`
- szögek: a szögek is egyenlők
- húzd a csúcsokat: húzd a csúcsokat!
- mozgatás: …majd elforgatjuk, eltoljuk
- hasonló def: `ABC ∼ A″B″C″`: hasonló alakzatok

## 3. Kétszeres oldal – hányszoros terület?
Tippelj: ha minden oldal kétszeresére nő, hányszoros lesz a terület? A nagy háromszöget ==`λ^2` darab kis háromszög tölti ki==. Az alap is, a magasság is λ-szoros, így a terület `λ · λ = λ^2`-szeres, a kerület csak λ-szoros. A térképen is: {térkép méretaránya} mellett 1 cm → {1 cm a valóságban}, de 1 cm² → {1 cm² a valóságban}.

### Feliratok
- cím 3: Kétszeres oldal – hányszoros terület?
- kis háromszög: 1 kis háromszög
- darab: # kis háromszög
- lambda csúszka: a nagyítás aránya (λ)
- oldal: oldal
- kerület: kerület
- terület: terület
- tévhit terület: Kétszeres oldal → kétszeres terület.
- cáfolat terület: Nem: négyszeres terület!
- biz t1: alap: `λ · a`, magasság: `λ · m`
- biz t2: `T′ = λa · λm : 2 = λ^2 · T`
- térkép cím: Térkép
- a térképen: a térképen
- a valóságban: a valóságban

### Adatok
<!-- 1 : 50 000 → 1 cm a térképen 50 000 cm = 500 m; 1 cm² → 500 m · 500 m = 250 000 m² = 0,25 km².
     4 cm → 2 km (a terv számpéldája). A lecke számolja és ellenőrzi. -->
- térkép méretaránya: 1 : 50 000
- 1 cm a valóságban: 500 m
- 1 cm² a valóságban: 0,25 km²

## 4. Egy nagy vagy két kicsi pizza?
Egy {nagy pizza átmérője}-es vagy két {kis pizza átmérője}-es pizza a több? Sokan a kettőre szavaznak: `2 · 22 = 44 > 32`. De a **terület** számít, és az az átmérő négyzetével nő: `32^2 = 1024`, de `2 · 22^2 = 968`. ==Az egy nagy kb. {nagy pizza többlete}-kal több.== Állítsd be az átmérőket!

> megjegyzés: Mikor egyforma? Ha `d_1 = √2 · d_2`.

### Feliratok
- cím 4: Egy nagy vagy két kicsi?
- tippelj: Tippelj: melyikben van több pizza?
- egy nagy: 1 db
- két kicsi: 2 db
- nagy csúszka: a nagy pizza átmérője
- kis csúszka: a kis pizzák átmérője
- tévhit pizza: Két kicsi: dupla átmérő, tehát több!
- cáfolat pizza: A terület számít: `d^2`-tel nő!
- terület sor: terület
- nagy a több: az egy nagy ≈ # %-kal több
- kicsi a több: a két kicsi ≈ # %-kal több
- egyforma: egyforma!
- egyenlőség: egyforma, ha `d_1 = √2 · d_2`
- két kicsi helye: ennyi a két kicsi együtt
- többlet: többlet

### Adatok
<!-- π · 16² ≈ 804,25 cm², 2 · π · 11² ≈ 760,27 cm²; 1024 : 968 ≈ 1,0579 → kb. 5,8 %-kal több.
     A számok kitaláltak (tipikus pizzaméretek). A lecke számolja és ellenőrzi. -->
- nagy pizza átmérője: 32 cm
- kis pizza átmérője: 22 cm
- nagy pizza többlete: 5,8 %

## 5. Miért nincs 10 méteres hangya?
Kétszeres élű kockába ==`2^3 = 8` kis kocka fér==: a térfogat – és vele a tömeg – `λ^3`-szeres, a lapok területe csak `λ^2`-szeres. Nagyítsunk egy {hangya hossza}-es hangyát {óriáshangya hossza}-esre (λ = 1000)! Tömege milliárdszoros, a lába keresztmetszete csak milliószoros: ==minden cm²-re ezerszer több teher jut==.

> megjegyzés: Galilei 1638-ban így érvelt: az óriások csontja nem bírná a súlyukat.

### Feliratok
- cím 5: Miért nincs 10 méteres hangya?
- kis kocka: 1 kis kocka
- kocka darab: # kis kocka
- forgasd: forgasd a kockát!
- lambda csúszka 5: a kocka éle (λ)
- él: él
- lap: lapok területe
- térfogat: térfogat, tömeg
- hangya cím: Hangya: # → #
- tömeg sor: tömeg
- keresztmetszet sor: a láb keresztmetszete
- teher sor: teher a láb 1 cm²-én
- hangya kicsi: 1 cm-es hangya
- hangya nagy: 10 m-es hangya ugyanígy

### Adatok
<!-- Kerek, kitalált méretek (egy nagyobb hangyafaj kb. 1 cm). λ = 10 m : 1 cm = 1000;
     λ³ = 10⁹ (milliárd), λ² = 10⁶ (millió), λ = 1000. A lecke számolja és ellenőrzi. -->
- hangya hossza: 1 cm
- óriáshangya hossza: 10 m
- tömeg szorzója: 1 milliárd
- keresztmetszet szorzója: 1 millió
- teher szorzója: 1000

## 6. Milyen magas a torony?
Egy {bot magassága}-es bot árnyéka {bot árnyéka}, a toronyé {torony árnyéka}. A napsugarak párhuzamosak, ezért a bot és a torony háromszögének szögei egyenlők: a két háromszög **hasonló**. Így `H : 48 = 1 : 1,6`, vagyis ==a torony {torony magassága} magas==. Mozgasd a Napot: az árnyékok változnak, az eredmény nem!

> megjegyzés: Csoportmunka: mérjétek meg így az iskola melletti tornyot!

### Feliratok
- cím 6: Milyen magas a torony?
- torony: torony
- Nap: Nap
- nap csúszka: a Nap magassága
- napsugarak: párhuzamos napsugarak
- bot nagyítva: a bot (nagyítva)
- hasonló háromszögek: ugyanaz a szög: hasonló háromszögek
- arány sor: `H : T = b : t`
- eredmény cím: a torony magassága

### Adatok
<!-- Kitalált adat (a terv számpéldája): 48 · 1 : 1,6 = 30 m. A lecke számolja és ellenőrzi. -->
- bot magassága: 1 m
- bot árnyéka: 1,6 m
- torony árnyéka: 48 m
- torony magassága: 30 m

## 7. Thalész és a piramis
A hagyomány szerint Thalész megvárta, amikor a bot árnyéka épp olyan hosszú, mint a bot ({Thalész napmagassága}). Ekkor a piramis magassága is az árnyékával egyenlő – csakhogy ==az árnyék a piramis közepétől számít==, és egy része az épület alatt rejtőzik: {látható árnyék} + {fél alapél} = {piramis magassága}.

> megjegyzés: A történetet Diogenész Laertiosz és Plutarkhosz írta le, jóval később.

### Feliratok
- cím 7: Thalész és a piramis
- piramis: Kheopsz-piramis
- rejtett: rejtett rész: a/2
- látható: látható árnyék
- csúcs árnyéka: a csúcs árnyéka
- nap csúszka 7: a Nap magassága
- bot 45: 45°-nál a bot árnyéka = a bot
- magasság képlet: `H =` látható árnyék `+ a/2`
- forrás sor: Diogenész Laertiosz, Plutarkhosz (jóval később)

### Adatok
<!-- Kheopsz-piramis eredeti magassága kb. 146,6 m, alapéle kb. 230,3 m (ugyanaz, mint a történelem 5–6
     02-nilus leckéjében; forrás: Wikipédia „Kheopsz-piramis”, Lehner: The Complete Pyramids, 1997).
     Fél alapél 115,15 m; 45°-nál a csúcs árnyéka 146,6 m-re van a középponttól, ebből 146,6 − 115,15 = 31,45 m
     látszik. A lecke számolja és ellenőrzi. (A modell egyszerűsít: a Nap az egyik oldallapra merőleges
     irányból süt.) -->
- piramis magassága: 146,6 m
- piramis alapéle: 230,3 m
- fél alapél: 115,15 m
- látható árnyék: 31,45 m
- Thalész napmagassága: 45°

## 8. Az A4-es lap családja
Félbehajtva az A4-ből A5 lesz – és pontosan hasonló az eredetihez! Minden téglalap ilyen? ==Csak az `a : b = √2` oldalarányú==: a fele akkor hasonló, ha `a : b = b : (a/2)`, azaz `a^2 = 2b^2`. Az A0 területe {A0 területe}, minden következő lap az előző fele, az arány `λ = 1/√2`.

### Feliratok
- cím 8: Az A4-es lap családja
- arány csúszka 8: a téglalap oldalaránya
- gyök 2 gomb: √2-es oldalarány
- tévhit téglalap: Minden téglalap hasonló.
- cáfolat téglalap: Csak az egyforma oldalarányúak!
- eredeti: eredeti
- fele: a fele, felnagyítva
- fele hasonló: a fele hasonló az egészhez!
- fele nem: a fele nem hasonló
- biz a1: `a : b = b : (a/2)`
- biz a2: `a^2 = 2b^2`
- biz a3: `a : b = √2 ≈ 1,414`
- spirál: minden lap az előző 90°-kal elforgatva, 1/√2-szeresre kicsinyítve

### Adatok
<!-- ISO 216: A0 841 × 1189 mm (területe 0,999949 m² ≈ 1 m²), A4 210 × 297 mm; 1189 : 841 ≈ 1,4138,
     297 : 210 ≈ 1,4143, √2 ≈ 1,4142. A lecke számolja és ellenőrzi. -->
- A0 mérete: 841; 1189 mm
- A4 mérete: 210; 297 mm
- A0 területe: kb. 1 m²

## 9. Összefoglalás
A középpontos hasonlóság minden távolságot λ-szorosára változtat, a szögeket megtartja; a hasonló alakzatok egymás nagyított (és elmozgatott) képei. ==A hosszak aránya λ, a területeké `λ^2`, a térfogatoké `λ^3`.== Ezért mérhető egy torony a bot árnyékából, ezért éri meg a nagy pizza, és ezért nincs óriáshangya.

### Feliratok
- össz 1 cím: Középpontos hasonlóság
- össz 1 sor: `OP′ = λ · OP`
- össz 2 cím: Mi marad meg?
- össz 2 sor: szögek, párhuzamosság, arányok
- össz 3 cím: Kerület és terület
- össz 3 sor: kerület: λ-szoros, terület: λ²-szeres
- össz 4 cím: Térfogat
- össz 4 sor: λ³-szeres – ezért nincs óriáshangya
- össz 5 cím: Árnyékmérés
- össz 5 sor: `H : T = b : t`
- össz 6 cím: A-papír
- össz 6 sor: `a : b = √2`, a fele hasonló

<!-- Matematikai ellenőrzés (Python 3 és a lecke L.checks()-e, 2026-11-24):
  - Középpontos hasonlóság (1. lépés): P′ = O + λ(P − O); a lecke a rajzolt pontokból méri OP′ : OP = λ-t mind a három
    csúcsra, és hogy P′ az OP félegyenesen van (a vektoriális szorzat 0, a skaláris szorzat > 0).
  - 2. lépés: A′B′ = OB′ − OA′ = λ(OB − OA) = λ·AB (vektorok) ⇒ A′B′ ∥ AB, |A′B′| = λ|AB|; a szögek a párhuzamos
    szárú szögek miatt egyenlők. A lecke minden húzott helyzetben ellenőrzi: párhuzamosság (1e−9), arány λ, mindhárom szög
    egyenlő; a mozgatott A″B″C″ egybevágó A′B′C′-vel, és a MatTrans.classify a teljes leképezést „forgatva nyújtás”-nak
    (spiral, k = 2) ismeri fel.
  - Terület (3. lépés): λ² egybevágó kis háromszög (λ(λ + 1)/2 eltolt + λ(λ − 1)/2 középpontosan tükrözött); λ = 2 → 4,
    3 → 9, 4 → 16; a lapok területösszege = a nagy háromszög területe (cipőfűző-képlet). Kerület λ-szoros.
    Térkép 1 : 50 000: 1 cm → 500 m, 4 cm → 2 km, 1 cm² → 0,25 km².
  - Pizza (4. lépés): 32² = 1024, 2 · 22² = 968; π · 16² ≈ 804,25 cm², 2π · 11² ≈ 760,27 cm²; 1024 : 968 ≈ 1,0579
    (≈ 5,8 %-kal több); a két kicsi a nagy ≈ 94,53 %-a. Egyenlőség: d₁ = √2 · d₂ (22 cm-nél ≈ 31,11 cm).
  - Térfogat (5. lépés): λ = 2 → 8, 3 → 27, 4 → 64 egységkocka; lapok 4, 9, 16-szoros. Hangya 1 cm → 10 m: λ = 1000,
    λ³ = 10⁹, λ² = 10⁶, a keresztmetszet egységére jutó teher λ³ : λ² = λ = 1000-szeres. (Egyszerűsítés: a test
    sűrűsége és alakja változatlan, a teher a lábak keresztmetszetén oszlik el.) Galilei érve: Discorsi e dimostrazioni
    matematiche intorno a due nuove scienze, 1638 (második nap) – közismert, a négyzet–köb törvény.
  - Torony (6. lépés): H = T · b : t = 48 · 1 : 1,6 = 30 m; a Nap magassága kezdetben arctg(1 : 1,6) ≈ 32,0°.
    A csúszkával (28°–65°) t = b : tg α, T = H : tg α változik, a hányados nem. Kitalált adat.
  - Piramis (7. lépés): Kheopsz-piramis eredetileg ≈ 146,6 m magas, alapéle ≈ 230,3 m (Wikipédia, Lehner 1997;
    ugyanaz, mint a történelem 02-ben). 45°-nál a csúcs árnyéka a középponttól H távolságra van; az alapél fele
    115,15 m, a látható rész 31,45 m. Az oldallap hajlásszöge arctg(146,6 : 115,15) ≈ 51,85° – ennél magasabb Napnál
    az árnyék nem ér ki (a csúszka 30°–50°). A Thalész-történet: Diogenész Laertiosz I. 27 (Hierónümoszra hivatkozva:
    „amikor az árnyékunk akkora, mint mi”), Plutarkhosz, A hét bölcs lakomája 147A (bot és arány) – mindkettő
    évszázadokkal későbbi forrás, ezért „a hagyomány szerint”.
  - A-papír (8. lépés): ISO 216; A0 841 × 1189 mm, 999 949 mm² ≈ 1 m²; A4 210 × 297 mm. A fele (b × a/2) akkor hasonló
    az egészhez, ha a : b = b : (a/2) ⇔ a² = 2b² ⇔ a : b = √2 ≈ 1,4142. A lecke a csúszkával vizsgált téglalapnál a
    két oldalarányt méri; a lapok spirálját egyetlen hasonlóság (90° + 1/√2) adja, a MatTrans.classify középpontját
    (a spirál középpontja) rajzolja ki.
-->
