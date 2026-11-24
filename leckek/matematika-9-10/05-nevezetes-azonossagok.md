# Miért nem `a^2 + b^2`? – nevezetes azonosságok négyzetekkel
tantárgy: Matematika · évfolyam: 9–10. · témakör: 6. Betűs kifejezések alkalmazása egyenletmegoldás, függvényábrázolás során

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/05-nevezetes-azonossagok.md
  Képlet a szövegben `…` között (x^2 → x², * → ·, - → −, != → ≠).
  A vásznon megjelenő számolásokat (területek, kifejtések, fejszámolás) a lecke számolja ki az
  alábbi adatokból. A panelszöveg képleteiben a számok szó szerint állnak: ha egy adatot átírsz,
  a hozzá tartozó szöveget is írd át. Az „eredmény” jellegű adatokat (pl. 47² értéke) a lecke
  ellenőrzi, és eltérésnél piros hibasávot mutat.
  Színek a vásznon (minden lépésben ugyanígy): a² cinóber, a · b kékeszöld, b² okker.
-->

## Közös

### Feliratok
- bizonyítás: bizonyítás
- vázlat: vázlat
- pozitív bélyeg: területtel: csak pozitív a, b

## 1. Mekkora a (3 + 5)²?
Tippelj! Sokan rávágják: `(3 + 5)^2 = 3^2 + 5^2 = 34`. Pedig `3 + 5 = 8`, és `8^2 = 64`. Rajzoljuk le! A 8 oldalú négyzetben elfér egy `3^2`-es és egy `5^2`-es négyzet, de ==kimarad két `3 · 5`-ös téglalap: ez a hiányzó 30.== Tehát `(a + b)^2 != a^2 + b^2`.

> megjegyzés: Kérdezd meg az osztályt, ki tippelt 34-et!

### Feliratok
- tippelj: Tippelj!
- sokan így: Sokan így számolnak:
- valójában: Valójában:
- a hiány: A különbség:
- két téglalap: a két téglalap
- hiányzik: kimaradt!

### Adatok
- első a: 3
- első b: 5

## 2. Négy darab: a², 2ab, b²
Az `a + b` oldalú négyzet négy darabra esik: egy `a^2`-es és egy `b^2`-es négyzetre, meg **két** `a · b`-s téglalapra. ==`(a + b)^2 = a^2 + 2ab + b^2`.== Húzd a csúszkákat: a darabok és a számok együtt változnak. A `2ab` a két téglalap – éppen ez hiányzott a tévhitből.

> megjegyzés: Ez a rajz csak pozitív *a*-ra és *b*-re bizonyít: oldalhossz nem lehet negatív.

### Feliratok
- a csúszka: a (az egyik oldal)
- b csúszka: b (a másik oldal)
- tévhit 2: a tévhitből hiányzik:
- együtt: összesen:

### Adatok
- kezdő a: 5
- kezdő b: 3

## 3. Minden számra: szorzás tagonként
Negatív számhoz nincs ilyen négyzet. A szorzás viszont **tagonként** mindig elvégezhető (disztributivitás): minden tagot minden taggal szorzunk. A táblázat négy cellája ugyanaz a négy darab. ==Így `(a + b)^2 = a^2 + 2ab + b^2` minden valós *a*, *b* számra igaz.== Próbáld ki negatív számmal is!

### Feliratok
- a csúszka 3: a (negatív is lehet)
- b csúszka 3: b (negatív is lehet)
- példa cím 3: Próba számokkal:
- tévhit 3: a tévhit:
- tagonként: minden tagot minden taggal

### Adatok
- példa a: 7
- példa b: −3

## 4. (a − b)²: levágunk
Az *a* oldalú négyzetből vágj le egy *b* széles csíkot jobbról, majd egyet felülről: mindkettő `a · b`. De a jobb felső `b^2`-es sarkot ==kétszer vontuk le, ezért egyszer vissza kell adni==: `(a − b)^2 = a^2 − 2ab + b^2`. Tehát `(a − b)^2 != a^2 − b^2`!

> megjegyzés: Ha *b* nagyobb, a rajz tükröződik, de a képlet ugyanaz: `(a − b)^2 = (b − a)^2`.

### Feliratok
- a csúszka 4: a
- b csúszka 4: b (amennyit levágunk)
- jobb csík: jobb oldali csík
- felső csík: felső csík (sarokkal)
- kétszer: kétszer levonva!
- visszaadjuk: visszaadjuk
- tükör: b nagyobb: tükrözött ábra
- tévhit 4: tévhit:
- marad: ez marad:

### Adatok
- levágás a: 6
- levágás b: 2

## 5. a² − b²: átdarabolás téglalappá
Vágd ki az `a^2`-es négyzet sarkából a `b^2`-es négyzetet! A maradék L alak felső csíkját fordítsd át a jobb oldalra: ==egy `a + b` hosszú, `a − b` magas téglalap lesz.== Tehát `a^2 − b^2 = (a + b)(a − b)`. Jobbról balra olvasva: **szorzattá alakítás**, `x^2 − 9 = (x + 3)(x − 3)`.

### Feliratok
- a csúszka 5: a
- b csúszka 5: b (a kivágott négyzet oldala)
- kivágjuk: kivágjuk
- átfordítjuk: átfordítjuk
- szorzattá: jobbról balra: szorzattá alakítás
- példa 5: Számokkal:

### Adatok
- különbség a: 7
- különbség b: 3
- szorzattá példa: 9

## 6. Fejszámolás azonosságokkal
==Keress egy kerek számot a közelben!== `47^2 = (50 − 3)^2 = 2500 − 300 + 9 = 2209`. Ha két szám egy kerek szám körül egyformán messze áll: `49 · 51 = 50^2 − 1^2 = 2499`, és `99 · 101 = 9999`. Válassz egy példát, vagy húzd a csúszkát!

> megjegyzés: Versenyezzen valaki számológéppel!

### Feliratok
- saját szám: a te számod (négyzetre emeljük)
- kerek: kerek szám a közelben:
- négyzet bal: Négyzetre emelés
- szorzat bal: Szorzat, kerek szám körül

### Adatok
- négyzet 1: 47
- négyzet 2: 103
- szorzat 1: 49; 51
- szorzat 2: 99; 101
- négyzet 1 értéke: 2209
- szorzat 1 értéke: 2499
- szorzat 2 értéke: 9999

## 7. Gondolj egy számra!
Gondolj egy pozitív egészre! Szorozd meg a nála 2-vel nagyobbal, adj hozzá 1-et, vonj belőle négyzetgyököt, és vond ki a gondolt számot. ==Mindig 1 jön ki.== Miért? A csempék megmutatják: `x(x + 2) + 1 = x^2 + 2x + 1 = (x + 1)^2`, és ennek gyöke `x + 1`.

> megjegyzés: Egy diák gondoljon számot, a többiek számoljanak vele!

### Feliratok
- gondolt csúszka: a gondolt szám
- újra 7: Még egyszer!
- utasítás 1: Gondolj egy számra!
- utasítás 2: Szorozd a nála 2-vel nagyobbal!
- utasítás 3: Adj hozzá 1-et!
- utasítás 4: Vonj négyzetgyököt!
- utasítás 5: Vond ki a gondolt számot!
- négyzet lett: négyzet lett!

### Adatok
- gondolt szám: 7

## 8. Két páratlan szám négyzete
Két szomszédos páratlan szám: `2k − 1` és `2k + 1`. A négyzetük különbsége a rajzon egy 1 széles keret. ==A keret mindig 8 egyforma, *k* hosszú darabra vágható==, tehát a különbség osztható 8-cal. Algebrával: `(2k + 1)^2 − (2k − 1)^2 = 4k · 2 = 8k`. Például `9^2 − 7^2 = 32`.

### Feliratok
- k csúszka: k (a nagyobb szám: 2k + 1)
- keret: a keret
- nyolc sor: 8 sor, mindegyikben k cella
- algebrával: Algebrával, minden k-ra:

### Adatok
- páratlan példa: 9
- páratlan különbség: 32

## 9. Összefoglaló
Három **nevezetes azonosság**, mindhárom minden valós számra igaz. ==A négyzetre emelés nem megy tagonként: a `2ab` mindig ott van.== Mire jók?

- fejszámolás: `47^2`, `49 · 51`
- szorzattá alakítás: `x^2 − 9 = (x + 3)(x − 3)`
- oszthatóság: `(2k + 1)^2 − (2k − 1)^2 = 8k`

> megjegyzés: A másodfokú egyenleteknél a teljes négyzetté kiegészítés is ezekre épül.

### Feliratok
- össz 1: összeg négyzete
- össz 2: különbség négyzete
- össz 3: két négyzet különbsége
- össz 4: Vigyázz!

<!-- Matematikai ellenőrzés (Python, 2026-11-24):
  (3 + 5)² = 64, 3² + 5² = 34, a különbség 30 = 2 · 3 · 5.
  (a + b)² = a² + 2ab + b² a csúszkák minden állásában (a 1–8, b 1–6, 0,5-ös lépés) a rajzolt darabok
  területének összegével is ellenőrizve (L.checks).
  Negatív példa: a = 7, b = −3: (7 + (−3))² = 16 = 49 − 42 + 9; a² + b² = 58.
  (6 − 2)² = 16 = 36 − 24 + 4; 6² − 2² = 32.
  7² − 3² = 40 = 10 · 4; x² − 9 = (x + 3)(x − 3).
  47² = (50 − 3)² = 2500 − 300 + 9 = 2209; 103² = 10 000 + 600 + 9 = 10 609;
  49 · 51 = 50² − 1² = 2499; 99 · 101 = 100² − 1² = 9999.
  Bűvésztrükk: x(x + 2) + 1 = (x + 1)², √((x + 1)²) = x + 1 (x ≥ 0-ra, mert x + 1 > 0), x + 1 − x = 1;
  pl. 7 · 9 + 1 = 64, √64 = 8, 8 − 7 = 1.
  (2k + 1)² − (2k − 1)² = 8k; 9² − 7² = 81 − 49 = 32 = 8 · 4 (k = 4); a keret 4 · 2k = 8k egységnégyzet.
  Eltérés a terv briefjétől: a bűvésztrükk a lineáris „(2(x + 3) − 4)/2 − x = 1” helyett
  az x(x + 2) + 1 = (x + 1)² azonosságra épül (ez a lecke témája, és csempékkel kirakható).
-->
