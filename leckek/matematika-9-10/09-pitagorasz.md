# Miért éppen `a^2 + b^2 = c^2`? – a Pitagorasz-tétel bizonyításai
tantárgy: Matematika · évfolyam: 9–10. · témakör: 12. Háromszögek

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/09-pitagorasz.md
  A betűk (a, b, c, α, β, γ, A, B, C) és a képletjelek a vásznon kódban rögzítettek.
  A színek: a² cinóber, b² kékeszöld, c² okker – a lecke minden lépésében ugyanígy.
-->

## Közös

### Feliratok
- mérés: mérés
- bizonyítás: bizonyítás
- átfogó: átfogó
- befogó: befogó
- újra gomb: Újra

### Adatok
<!-- Az első példa (1., 3. és 6. lépés) befogói; a 4. lépés a kétszeresükkel rajzol. A lecke ellenőrzi,
     hogy az átfogó a két befogóból számolva egész szám (különben piros sáv jelez). -->
- befogó a: 3
- befogó b: 4
- átfogó c: 5

## 1. Három négyzet egy háromszögön
Egy derékszögű háromszög mindhárom oldalára négyzetet rajzolunk. A derékszöggel szemközti oldal az **átfogó** (`c`), a másik kettő a **befogó** (`a`, `b`). Számold meg a kis négyzeteket! ==Az átfogóra rajzolt négyzet pontosan akkora, mint a másik kettő együtt.== Az oldalakra ez nem igaz: {befogó a} + {befogó b} ≠ {átfogó c}.

### Feliratok
- cím 1: Három négyzet egy derékszögű háromszögön
- számoljuk: Számoljuk meg a kis négyzeteket!
- tévhit összeg: A két befogó összege az átfogó.
- c az átfogó: `c` = a derékszöggel szemközti oldal

## 2. Mérjük meg! (sejtés)
Húzd a C csúcsot a félkörön! A C-nél mindig derékszög van (Thalész-tétel). A kis négyzetek változnak, összegük mégis annyi, mint a nagy. ==Ez csak mérés:== néhány eset, kerekítve. Sok egyező mérés sem bizonyít.

> megjegyzés: A diákok jegyezzenek fel 3–4 helyzetet, és adják össze!

### Feliratok
- cím 2: Mérjük meg: mindig egyezik?
- húzd a C-t: húzd a C-t!
- thalész: félkör: itt mindig derékszög van
- napló cím: Mérési napló
- feljegyzem gomb: Feljegyzem
- C csúszka: C helye a félkörön
- sejtés: Sejtés: `a^2 + b^2 = c^2`
- nem bizonyíték: Sok egyező mérés sem bizonyíték.

## 3. Négy háromszög két keretben (bizonyítás)
Két `a + b` oldalú keretbe 4-4 egybevágó derékszögű háromszöget teszünk. Balra a maradék négyzet, mert `α + β = 90°`. Jobbra a háromszögek csak eltolódnak: a maradék `a^2` és `b^2`. Ugyanannyit vettünk el: ==`a^2 + b^2 = c^2`, minden derékszögű háromszögre.==

### Feliratok
- cím 3: Négy háromszög két keretben
- maradék bal: maradék: `c^2`
- maradék jobb: maradék: `a^2 + b^2`
- biz 1: Mindkét keret oldala `a + b`.
- biz 2: Mindkettőben 4 egybevágó háromszög.
- biz 3: A bal maradék négyzet, mert
- biz 4: `180° - (α + β) = 90°`
- biz 5: Ugyanannyit vettünk el, tehát
- biz 6: `a^2 + b^2 = c^2`
- a csúszka: az a befogó

## 4. Eukleidész nyírása
Eukleidész ({Elemek kora}) másképp bizonyított. A **nyírás** egy oldalt helyben hagy, a szemközti oldalt vele párhuzamosan csúsztatja: az alap és a magasság marad, így a terület is. Az `a^2` négyzetből nyírás, 90°-os forgatás és újabb nyírás után az átfogó-négyzet egyik téglalapja lesz, `b^2`-ből a másik. ==A két téglalap együtt `c^2`.==

### Feliratok
- cím 4: Eukleidész nyírása
- fázis 0: a két befogó-négyzet
- fázis 1: 1. nyírás: ugyanaz az alap és a magasság
- fázis 2: 2. forgatás 90°-kal a csúcs körül
- fázis 3: 3. nyírás a magasságvonal mentén
- terület: terület
- végig: a terület végig ugyanannyi
- eredmény 4: `a^2 + b^2 = c^2`
- menet csúszka: A nyírás menete
- lejátszás gomb: Lejátszás
- elemek: Eukleidész: Elemek, I. könyv, 47. tétel

### Adatok
<!-- Eukleidész Elemek című műve: kb. Kr. e. 300 (a pontos év nem ismert); az I. könyv 47. tétele a
     Pitagorasz-tétel, a bizonyítás a nyírásos (háromszög-egybevágóságos) „szélmalom-ábra”. -->
- Elemek kora: kb. Kr. e. 300

## 5. Ha nem derékszög?
Állítsd a γ szöget! Az `a` és a `b` oldal marad, a `c` változik. Hegyesszögnél `c^2 < a^2 + b^2` (γ = {hegyes szög}: `c^2` = {c négyzet hegyesnél}), tompaszögnél `c^2 > a^2 + b^2` (γ = {tompa szög}: `c^2` = {c négyzet tompánál}). ==Egyenlőség csak `γ = 90°`-nál van.== A mérleg mutatja, melyik oldal nagyobb. Ezt itt csak mérjük.

### Feliratok
- cím 5: Mi van, ha nem derékszög?
- tévhit minden: A tétel minden háromszögre igaz.
- cáfolat minden: Csak a derékszögűre!
- hegyesszögű: hegyesszögű
- derékszögű: derékszögű
- tompaszögű: tompaszögű
- gamma csúszka: a γ szög
- hegyes gomb: hegyesszög
- derék gomb: derékszög
- tompa gomb: tompaszög

### Adatok
- hegyes szög: 60°
- tompa szög: 120°
- c négyzet hegyesnél: 13
- c négyzet tompánál: 37

## 6. A megfordítás
Fordítva is igaz: ha `a^2 + b^2 = c^2`, a háromszög derékszögű. Miért? Rajzolunk egy derékszögű segédháromszöget `a` és `b` befogóval. Átfogójára `c′^2 = a^2 + b^2 = c^2`, így `c′ = c`. A két háromszög oldalai páronként egyenlők, tehát **egybevágók**: ==a γ is 90°.== Állítsd a `c`-t!

> megjegyzés: Kőművesfogás: 60 cm és 80 cm mellé 100 cm-es átló – akkor derékszögű a sarok.

### Feliratok
- cím 6: A megfordítás
- c csúszka: a c oldal hossza
- szerkesztés: körzővel: `b` sugár A-ból, `a` sugár B-ből
- segéd: segédháromszög (derékszögű)
- ráillik: Pontosan ráillik – egybevágók!
- nem illik: Nem illik rá: `c^2 != a^2 + b^2`
- biz m1: 1. Segédháromszög: befogói `a` és `b`.
- biz m2: 2. `c′^2 = a^2 + b^2 = c^2`
- biz m3: 3. Így `c′ = c`: három oldal egyenlő,
- biz m4: tehát egybevágók: `γ = 90°`.
- c ötös gomb: legyen c² = a² + b²

## 7. Egész számhármasok
Ha `a`, `b` és `c` is egész: **pitagoraszi számhármas** (3–4–5, 5–12–13, 8–15–17). Húzd a pontot a rácson! A legtöbb párnál `c` nem egész – a tétel akkor is igaz. ==Jóval Pitagorasz előtt ismerték:== babiloni agyagtáblán ({Plimpton 322 kora}) is szerepelnek.

> megjegyzés: Pitagorasztól magától bizonyítás nem maradt fenn.

### Feliratok
- cím 7: Egész számhármasok
- húzd a pontot: húzd a pontot!
- egész: egész – számhármas!
- nem egész: nem egész, de a tétel igaz
- többszörös: többszöröse ennek:
- tévhit egész: Csak egész számokra igaz.
- cáfolat egész: `1^2 + 2^2 = (√5)^2` is igaz
- tévhit pitagorasz: Pitagorasz fedezte fel.
- cáfolat pitagorasz: kb. # évvel előtte is ismerték
- plimpton cím: Plimpton 322 – babiloni agyagtábla
- plimpton sor: egyik sora (mai jelöléssel):
- következő gomb: Következő számhármas
- nem egész gomb: Nem egész példa

### Adatok
<!-- Plimpton 322: óbabiloni agyagtábla (Columbia Egyetem), kb. Kr. e. 1800 (a szakirodalom Kr. e. 1822–1762
     közé teszi). A tábla a rövidebb oldalt és az átlót sorolja fel; az első sor 119 és 169, a hiányzó oldal 120.
     Hogy a táblát mire használták, vitatott (Robson 2001; Mansfield–Wildberger 2017). -->
- Plimpton 322 kora: kb. Kr. e. 1800
- Plimpton-hármas: 119; 120; 169
<!-- Pitagorasz születése a hagyomány szerint kb. Kr. e. 570 (bizonytalan, a források Kr. e. 580–570 közé teszik). -->
- Pitagorasz születése: kb. Kr. e. 570

## 8. Mekkora az 55 colos tévé?
A tévé méretét az **átlójával** adják meg: 1 col = {col}. Itt az átló {tévé átló} = {átló centiméterben}. A 16 : 9-es képnél a szélesség `16x`, a magasság `9x`, és Pitagorasz szerint `(16x)^2 + (9x)^2 = d^2`, vagyis `x = d / √337`. ==Szélesség ≈ {tévé szélessége}, magasság ≈ {tévé magassága}.== Húzd a csúszkát!

> megjegyzés: Ugyanakkora átlónál a régi 4 : 3-as kép területe nagyobb, mint a 16 : 9-esé.

### Feliratok
- cím 8: Mekkora a # colos tévé?
- átló: átló
- szélesség: szélesség
- magasság: magasság
- átló csúszka: képátló
- régi gomb: régi 4 : 3-as kép
- tévhit col: A # col a tévé szélessége.
- cáfolat col: Nem: az átlója!
- számolás: Pitagorasszal:
- képterület: képterület
- egy méter: 1 m

### Adatok
- col: 2,54 cm
- tévé átló: 55 col
- átló centiméterben: 139,7 cm
- képarány: 16 : 9
- régi képarány: 4 : 3
- tévé szélessége: 121,8 cm
- tévé magassága: 68,5 cm

## 9. Összefoglaló
- derékszögű háromszögben: `a^2 + b^2 = c^2`, ahol `c` az átfogó
- bizonyítás: átdarabolás – a mérés nem bizonyít
- megfordítás: ha `a^2 + b^2 = c^2`, a háromszög derékszögű
- hegyesszögnél `c^2` kisebb, tompaszögnél nagyobb

==Egy oldal ismeretlen? Pitagorasz kiszámolja.==

### Feliratok
- össz tétel cím: A tétel
- össz tétel 1: csak derékszögű háromszögben
- össz tétel 2: `c` az átfogó: a derékszöggel szemközti oldal
- össz biz cím: Bizonyítás
- össz biz 1: négy háromszög két keretben
- össz biz 2: a mérés csak sejtést ad
- össz meg cím: Megfordítás
- össz meg 1: ha `a^2 + b^2 = c^2`, akkor `γ = 90°`
- össz meg 2: hegyesszög: `c^2 < a^2 + b^2`
- össz meg 3: tompaszög: `c^2 > a^2 + b^2`
- össz alk cím: Alkalmazás
- össz alk 1: 55 colos tévé, 16 : 9
- össz alk 2: 3–4–5: így ellenőrizhető a derékszög

<!-- Matematikai ellenőrzés (Python 3, 2026-11-24):
  - 3² + 4² = 9 + 16 = 25 = 5²; 3 + 4 = 7 ≠ 5. 6–8–10 (a 4. lépés rajza) a 3–4–5 kétszerese.
  - Számhármasok: 5² + 12² = 169 = 13²; 8² + 15² = 289 = 17²; 20² + 21² = 841 = 29²; 7–24–25, 9–40–41,
    11–60–61, 12–35–37, 28–45–53, 33–56–65, 48–55–73. a ≤ b ≤ 60 között 34 számhármas van, ebből 11 primitív.
    Plimpton 322: 119² + 120² = 14 161 + 14 400 = 28 561 = 169².
  - Nem derékszög (a = 3, b = 4): γ = 60° → c² = 25 − 24 · cos 60° = 13; γ = 120° → c² = 37; γ = 150° → c² ≈ 45,78.
    A lecke a koszinusztételt nem nevezi meg: a c²-et a rajzolt csúcsok távolságából méri.
  - Bizonyítások: (1) két (a + b) oldalú keret, négy egybevágó háromszög; a háromszögek tisztán eltolással
    rendeződnek át (bal felső: (a; −b), bal alsó: (0; a), jobb felső: (−b; 0), jobb alsó: helyben). (2) Eukleidész
    (Elemek I. 47.) nyírásos változata: a befogó-négyzet nyírása az AC egyenessel párhuzamosan (a csúszó oldal
    a C-ből az A-ba kerül), forgatás 90°-kal a B körül, nyírás a magasságvonallal párhuzamosan; az átfogó-négyzet
    BH · c területű téglalapja = a² (mert BH = a²/c). A lecke minden képkockánál ellenőrzi, hogy a darab
    területe a² (ill. b²), és a végén pontosan a téglalap.
    (3) Megfordítás: segédháromszög + oldal-oldal-oldal egybevágóság (a lecke ezt az egybevágósági alapesetet
    ismertnek veszi).
  - Tévé: 55″ · 2,54 cm = 139,7 cm; √(16² + 9²) = √337 ≈ 18,358; szélesség 139,7 · 16/√337 ≈ 121,76 cm,
    magasság 139,7 · 9/√337 ≈ 68,49 cm; képterület ≈ 8339 cm². 4 : 3 és 55″: 111,76 cm × 83,82 cm ≈ 9368 cm².
    1 col = 2,54 cm pontosan (1959 óta definíció szerint).
  - Történeti adatok (kitekintés, nem tananyag): Plimpton 322 kb. Kr. e. 1800 – értelmezése vitatott (Robson,
    E.: Neither Sherlock Holmes nor Babylon, Historia Mathematica 28, 2001); Pitagorasz kb. Kr. e. 570–495
    (hagyomány, bizonytalan); Eukleidész Elemek kb. Kr. e. 300. A „kb. 1200 évvel előtte” a két évszámból
    számolva, százasra kerekítve. Ellenőrizendő: a fenti évszámok tankönyvi forrással.
  - Tankönyvi jelölés: a befogók a és b, az átfogó c, a derékszög a C csúcsnál (γ) – ettől eltérő jelölésnél a
    panelszöveget és a Feliratokat kell átírni; a vásznon a betűk kódban vannak.
-->
