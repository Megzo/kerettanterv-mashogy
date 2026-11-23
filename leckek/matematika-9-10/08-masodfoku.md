# Hol metszi a parabola a tengelyt? – teljes négyzet, megoldóképlet, diszkrimináns
tantárgy: Matematika · évfolyam: 9–10. · témakör: 9. Másodfokú egyenletek, egyenlőtlenségek (+ 6. Betűs kifejezések, 10. Függvények)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/08-masodfoku.md
  Képlet a szövegben `…` között (x^2 → x², * → ·, - → −, < → <, <= → ≤, +- → ±, √(…)).
  A vásznon megjelenő levezetéseket, megoldásokat, csúcsokat a lecke számolja ki az alábbi adatokból.
  A panelszöveg képleteiben a számok szó szerint állnak: ha egy adatot átírsz, a hozzá tartozó
  szöveget is írd át. Az „eredmény” jellegű adatokat (megoldás, csúcs, zérushelyek, gyökök,
  legnagyobb terület) a lecke kiszámolja, és eltérésnél piros hibasávot mutat.
-->

## Közös

### Feliratok
- bizonyítás: bizonyítás
- mérés: mérés
- csúcs felirat: csúcs
- vagy: vagy

## 1. Al-Hvárizmi négyzete
Al-Hvárizmi bagdadi tudós könyvének feladata: `x^2 + 10x = 39`. Rajzoljuk le! Az `x^2` egy négyzet, a `10x` két `5x`-es csík a két oldalán. A sarokból hiányzik egy `5 · 5`-ös négyzet – tegyük be! ==Így egy `x + 5` oldalú, 64 területű négyzet lesz==: az oldala 8, tehát `x = 3`.

> megjegyzés: Ő csak a pozitív megoldást kereste. Van másik is – a 4. lépésben kiderül.

### Feliratok
- forrás 1: al-Hvárizmi, Bagdad, kb. 820
- algebra szó: a könyv címéből (al-dzsabr) lett az „algebra” szó
- terület 1: területük együtt:
- hiányzik: hiányzik:
- kész négyzet: teljes négyzet
- pozitív: al-Hvárizmi: csak pozitív
- újra 1 gomb: Rakd össze újra!

### Adatok
- hvárizmi b: 10
- hvárizmi c: 39
- hvárizmi megoldás: 3
<!-- A feladat (x² + 10x = 39, „egy négyzet és tíz gyöke 39 dirhemmel egyenlő”) al-Hvárizmi algebrakönyvéből
     való; a könyv kb. 820–830 körül készült Bagdadban. Az átírás (al-Hvárizmi, al-dzsabr) és a dátum
     ellenőrizendő (MacTutor History of Mathematics: „al-Khwarizmi”; magyar Wikipédia: „Al-Hvárizmi”). -->

## 2. Teljes négyzet a betűkkel
Ugyanez minden *b*-re: az `x^2 + bx` mellé két `b/2 · x`-es csík kerül, a sarokból `(b/2)^2` hiányzik. Hozzáadjuk, és ugyanannyit le is vonunk: ==`x^2 + bx = (x + b/2)^2 − (b/2)^2`.== Negatív *b*-re a rajz nem működik, a számolás igen.

> megjegyzés: Húzd a *b* csúszkát! A példa a következő lépés függvénye.

### Feliratok
- b csúszka: b (az x-es tag szorzója)
- x bármi: x bármilyen pozitív szám
- ennyi hiányzik: ennyi hiányzik
- általános: általában:
- példa cím: Példa (negatív b):

## 3. A parabola csúcsa
A teljes négyzetes alakból leolvasható a grafikon: `(x − 2)^2 − 1` az `x^2` parabolája **2-vel jobbra és 1-gyel lefelé** tolva. Mivel `(x − 2)^2 >= 0`, a függvény ==legkisebb értéke −1, az `x = 2` helyen==: ez a csúcs. A parabola az `x = 2` egyenesre szimmetrikus.

> megjegyzés: Húzd a pontot: a magassága a csúcs fölött éppen `(x − 2)^2`.

### Feliratok
- jobbra: jobbra
- lefelé: lefelé
- szimmetriatengely: szimmetriatengely
- pont csúszka: x (a pont helye)
- csúcs fölött: a csúcs fölött:

### Adatok
- példa függvény: x^2 − 4x + 3
- példa csúcs: (2; −1)

## 4. Hol metszi a tengelyt?
A zérushelyen `f(x) = 0`, azaz `(x − 2)^2 = 1`. Melyik szám négyzete 1? Az 1-é **és a −1-é** is! Tehát `x − 2 = 1` vagy `x − 2 = −1`, így ==`x = 3` vagy `x = 1`== – a csúcstól egyformán messze. Az `x^2 = 9`-nek is két megoldása van: 3 és −3.

> megjegyzés: Al-Hvárizmi egyenlete: `x + 5 = −8` is lehet, tehát `x = −13`.

### Feliratok
- tévhit 4: Csak egy megoldás?
- négyzet 1: melyik szám négyzete 1?
- egyforma: egyformán messze

### Adatok
- példa zérushelyek: 1; 3
- négyzet példa: 9

## 5. A diszkrimináns
A parabola **metszi, érinti vagy elkerüli** a tengelyt. Melyik? Egyetlen szám dönti el, a **diszkrimináns**: `D = b^2 − 4ac`. ==`D > 0`: két megoldás, `D = 0`: egy, `D < 0`: nincs valós megoldás.==

### Feliratok
- a csúszka: a (az x² szorzója)
- b csúszka 5: b (az x szorzója)
- c csúszka: c (a konstans tag)
- mérő cím: diszkrimináns
- két megoldás: 2 megoldás
- egy megoldás: 1 megoldás
- nincs megoldás: nincs valós megoldás
- nem hiba: nem hiba: a parabola nem éri el a tengelyt
- nem másodfokú: a = 0: ez már nem másodfokú
- alaphelyzet 5: Alaphelyzet

## 6. Megoldóképlet és gyöktényezős alak
A teljes négyzetté kiegészítés betűkkel adja a **megoldóképletet**:

képlet: x = (−b ± √(b^2 − 4ac)) / (2a)

Példa: `2x^2 + 3x − 2 = 0`, `D = 25`, `x = (−3 +- 5)/4`, ==így `x_1 = 0,5` és `x_2 = −2`.== A **gyöktényezős alak**, `2(x − 0,5)(x + 2)`, a zérushelyeket mutatja. Negatív *D*-nél nincs valós gyök: negatív számnak nincs négyzetgyöke.

### Feliratok
- levezetés cím: Honnan jön? Teljes négyzet betűkkel
- szoroz: szorozzuk 4a-val
- teljes négyzet: teljes négyzet!
- ha D: ha `D >= 0`
- behelyettesítés: behelyettesítve:
- gyöktényezős cím: gyöktényezős alak:
- nem bontható: nincs valós gyök – nem bontható
- egy gyök: egy (kétszeres) gyök

### Adatok
- példa 6a: 2x^2 + 3x − 2
- példa 6b: x^2 − 6x + 9
- példa 6c: x^2 + 2x + 5
- 6a gyökei: −2; 0,5

## 7. Ne ossz x-szel!
Csábító: `x^2 = 3x`, osszunk *x*-szel, és kész: `x = 3`. De a grafikonok **két** pontban metszik egymást! *x*-szel osztani csak `x != 0` esetén szabad: ==az `x = 0` megoldás elveszett.== Helyesen: `x^2 − 3x = 0`, kiemelve `x(x − 3) = 0`. Egy szorzat akkor 0, ha valamelyik tényezője 0.

### Feliratok
- rossz út: osztunk x-szel:
- elveszett: elveszett megoldás!
- nem oszthatsz: ha x = 0, nem oszthatsz vele
- jó út: kiemelünk:
- szorzat nulla: a szorzat 0, ha egy tényezője 0
- k csúszka: k (az egyenlet: x² = k · x)

### Adatok
- osztás k: 3

## 8. Mikor negatív? (egyenlőtlenség)
Sokan így oldják meg: `x^2 − x − 6 < 0`, tehát `x < 3`. Próbáld ki az `x = −3`-at: `9 + 3 − 6 = 6`, ez nem negatív! A zérushelyek −2 és 3, és ==a parabola csak a kettő között van a tengely alatt==: `−2 < x < 3`, vagyis `x ∈ ]−2; 3[`.

> megjegyzés: Próbáld a többi relációt is!

### Feliratok
- sokan így: Sokan így:
- ellenpélda: ellenpélda:
- nem negatív: nem negatív!
- itt negatív: itt negatív
- itt pozitív: itt pozitív
- megoldás 8: megoldás:
- próbapont csúszka: próbapont x
- igaz: igaz
- hamis: hamis
- nincs megoldás 8: nincs megoldás
- minden x: minden x megoldás
- kisebb gomb: < 0
- nagyobb gomb: > 0
- legfeljebb gomb: ≤ 0
- legalább gomb: ≥ 0

### Adatok
- egyenlőtlenség: x^2 − x − 6
- ellenpélda x: −3
- egyenlőtlenség határai: −2; 3

## 9. A legnagyobb kert – összefoglalás
{spárga hossza} spárgával téglalap alakú kertet kerítünk. Ha az egyik oldal *x*, a másik `10 − x`, a terület `T(x) = x(10 − x)`. Húzd a sarkot! Teljes négyzettel: `T(x) = 25 − (x − 5)^2 <= 25`. ==A legnagyobb kert az `5 · 5`-ös négyzet, 25 m².==

### Feliratok
- spárga: spárga:
- kert: kert
- oldal csúszka: x (a kert egyik oldala, m)
- terület tengely: T (m²)
- oldal tengely: x (m)
- maximum: maximum!
- össz 1 cím: Teljes négyzet
- össz 2 cím: Csúcs
- össz 3 cím: Hány megoldás?
- össz 4 cím: Egyenlőtlenség
- össz 3: D > 0: 2 · D = 0: 1 · D < 0: 0
- össz 4: a grafikonról olvasd le!

### Adatok
- spárga hossza: 20 m
- legnagyobb terület: 25 m²

<!-- Matematikai ellenőrzés (2026-11-24, kézzel + Pythonnal + a lecke L.checks() kampója):
     x² + 10x = 39 ⇔ (x + 5)² = 64 ⇔ x = 3 vagy x = −13 (3² + 30 = 39); a négy darab területe 9 + 15 + 15 + 25 = 64 = 8².
     x² + bx = (x + b/2)² − (b/2)², b = 6: (x + 3)² = x² + 3x + 3x + 9.
     x² − 4x + 3 = (x − 2)² − 1 = (x − 1)(x − 3); csúcs (2; −1), zérushelyek 1 és 3, D = 16 − 12 = 4.
     x² = 9 ⇔ x = 3 vagy x = −3.
     Megoldóképlet: ax² + bx + c = 0 | ·4a → (2ax + b)² = b² − 4ac (a ≠ 0).
     2x² + 3x − 2: D = 9 + 16 = 25, x = (−3 ± 5)/4 → 0,5 és −2; 2(x − 0,5)(x + 2) = 2x² + 3x − 2.
     x² − 6x + 9: D = 0, x = 3 (kétszeres), (x − 3)². x² + 2x + 5: D = 4 − 20 = −16, nincs valós gyök.
     x² = 3x ⇔ x(x − 3) = 0 ⇔ x = 0 vagy x = 3.
     x² − x − 6 = (x + 2)(x − 3) < 0 ⇔ −2 < x < 3; f(−3) = 9 + 3 − 6 = 6 ≥ 0 (ellenpélda az „x < 3”-ra).
     Kert: kerület 2x + 2(10 − x) = 20; T(x) = x(10 − x) = 25 − (x − 5)² ≤ 25, egyenlőség x = 5-nél; 4 · 6 = 24, 3 · 7 = 21.
     A lecke a vásznon minden levezetést az Adatok-ból számol; az eredményadatokat (megoldás, csúcs, zérushelyek,
     gyökök, határok, legnagyobb terület) ellenőrzi, eltérésnél piros hibasáv (kipróbálva). -->
