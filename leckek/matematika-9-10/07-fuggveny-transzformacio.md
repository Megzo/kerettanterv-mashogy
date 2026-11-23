# Merre mozdul a parabola? – függvények és transzformációik
tantárgy: Matematika · évfolyam: 9–10. · témakör: 10. A függvény fogalma, függvénytulajdonságok (+ 7. Arányosság)

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/07-fuggveny-transzformacio.md
  Feliratban a # jel helyére a lecke számot ír.
  Képlet a szövegben `…` között (x^2 → x², * → ·, - → −, >= → ≥, +- → ±, √(…)).
  A panelszöveg képleteiben (pl. `f(x + 3)`) a számok szó szerint állnak: ha egy adatot átírsz,
  a hozzá tartozó szöveget is írd át. Az „eredmény” jellegű adatokat (zérushely, minimum,
  helyi maximum, megoldás) a lecke kiszámolja, és eltérésnél piros hibasávot mutat.
-->

## Közös

### Feliratok
- alap x: x
- alap x2: x²
- alap gyök: √x
- alap 1/x: 1/x
- alap abs: |x|
- a csúszka: a (nyújtás, tükrözés)
- u csúszka: u (vízszintes eltolás)
- v csúszka: v (függőleges eltolás)
- abs gomb: |·| felhajtás
- eredeti: eredeti
- új görbe: új

## 1. A függvénygép
A függvény egy gép: beteszel egy *x*-et, kijön egy szám, az `f(x)`. Az `(x; f(x))` párok pontként esnek a koordináta-rendszerbe, és sok pontból összeáll a **grafikon**. ==Minden x-hez pontosan egy y tartozik.== A kör ezért nem függvénygrafikon: egy *x*-hez két *y*-t ad.

> megjegyzés: Húzd a csúszkát: hány pontban metszi a függőleges egyenes a görbét?

### Feliratok
- gép: FÜGGVÉNYGÉP
- bemenet: be: x
- kimenet: ki: f(x)
- kör cím: kör – nem függvény
- két y: egy x-hez két y
- egy y: egy x-hez egy y
- gép csúszka: x (bemenet)

### Adatok
- gép szabálya: x^2
- gép bemenetei: −3; −2; −1; 0; 1; 2; 3

## 2. Mit árul el a grafikon?
**Értelmezési tartomány** (`D_f`): mely *x*-ekre van értelmezve. **Értékkészlet** (`R_f`): mely *y*-okat veszi fel – ==nem az egész y tengely!== **Zérushely**: ahol `f(x) = 0`, itt {zérushely 1} és {zérushely 2}. **Minimum**: a legkisebb érték, {minimum értéke}. Hol csökken, hol nő?

> megjegyzés: Húzd a pontot a görbén!

### Feliratok
- ÉT felirat: értelmezési tartomány
- ÉK felirat: értékkészlet
- nem az egész: nem az egész y tengely!
- zérushely felirat: zérushely
- minimum felirat: minimum
- csökken: csökken
- nő: nő
- pont csúszka: x (a pont helye)

### Adatok
- vizsgált függvény: x^2 − 2x − 3
- ÉT eleje: −2
- ÉT vége: 4
- zérushely 1: −1
- zérushely 2: 3
- minimum helye: 1
- minimum értéke: −4
- ÉK felső határa: 5
<!-- A zérushelyeket, a minimumot és az értékkészlet felső határát a lecke kiszámolja a „vizsgált függvény”
     és az értelmezési tartomány adataiból, és összeveti az itteni értékekkel. -->

## 3. Az alapfüggvények
Ezekből az **elemi függvényekből** építkezünk. Nézd meg, hol vannak értelmezve! A `√x` csak `x >= 0`-ra, az `1/x` az `x = 0`-ban nincs értelmezve: a két ága ==sosem ér össze==. Az `y = 12/x` **fordított arányosság**: a téglalapok területe mind `x · y = 12`.

### Feliratok
- lineáris: lineáris
- másodfokú: másodfokú
- abszolút: abszolútérték
- négyzetgyök: négyzetgyök
- reciprok: fordított arányosság
- ÉT mind: minden x
- ÉT gyök: `x >= 0`
- ÉT reciprok: `x != 0`
- téglalap cím: mind ugyanakkora területű
- szélesség csúszka: x (a téglalap szélessége)

### Adatok
- téglalap területe: 12
- téglalap szélessége: 3

## 4. `f(x) + v`: fel és le
Adj minden függvényértékhez 3-at: `g(x) = f(x) + 3`. Minden pont pontosan 3 egységgel **feljebb** kerül, a görbe alakja nem változik. ==Pozitív v fel, negatív v le tolja.== Húzd a csúcsot, vagy próbáld ki más alapfüggvénnyel!

### Feliratok
- fel: minden pont # egységgel feljebb
- le: minden pont # egységgel lejjebb

### Adatok
- függőleges eltolás: 3

## 5. `f(x + u)`: miért balra?
A „+ 3” miatt sokan jobbra tolnák. Ha `f(x_0) = y_0`, akkor `g(x_0 - 3) = f(x_0 - 3 + 3) = y_0`. ==Az f minden pontja 3-mal balra kerül:== a g ugyanazt az értéket 3-mal kisebb *x*-nél veszi fel. ∎

### Feliratok
- tipp: tipp: jobbra?
- nem jobbra: nem jobbra – balra!
- bizonyítás: bizonyítás

### Adatok
- vízszintes eltolás: 3

## 6. `a · f(x)`: nyújtás és tükrözés
A `2 · f(x)` minden *y*-értéket a kétszeresére növel, az *x* marad. A parabola ezért **keskenyebbnek** látszik – nem lett „kétszer szélesebb”, csak magasabb. Az *x* tengely pontjai helyben maradnak. ==Negatív szorzó az x tengelyre tükröz.==

### Feliratok
- keskenyebb: keskenyebb? Nem: magasabb!
- tükrözés felirat: tükrözés az x tengelyre

### Adatok
- nyújtás: 2
- tükrözés: −1

## 7. `|f(x)|`: felhajtás
Az abszolútérték a negatív értékeket ellentettjükre váltja: a grafikon tengely alatti része ==felhajlik, az x tengelyre tükrözve.== Az `|x^2 - 4|` zérushelyei maradnak `+-2`, és az `x = 0`-ban **helyi maximuma** lett: {helyi maximum}. Vigyázz: az `f(|x|)` egészen mást jelent!

### Feliratok
- felhajtott rész: a tengely alatti rész felhajlik
- helyi max: helyi maximum
- f abs x gomb: f(|x|) mutatása
- nem ugyanaz: f(|x|) ≠ |f(x)|

### Adatok
- süllyesztés: −4
- helyi maximum: 4

## 8. `f(x) = c` és a megfordítás
Melyik *x*-hez tartozik az 5? Az `x^2 = 5` egyenletnek két megoldása van: `x = +-√5 ~= +-`{megoldás közelítőleg}. Két *x* ugyanahhoz az *y*-hoz: így az `x^2` ==nem fordítható meg==. Az `x >= 0` rész már **kölcsönösen egyértelmű**: tükrözzük az `y = x` egyenesre – ez a `√x`.

### Feliratok
- megoldás db: # megoldás
- nincs megoldás: nincs megoldás
- nem fordítható: két x → nem fordítható meg
- fordítható: egy x → megfordítható
- csak pozitív: csak az x ≥ 0 rész
- tükör: y = x
- megfordítva: megfordítva:
- parabola példa: x² (x ≥ 0) ↔ √x
- egyenes példa gomb: 2x + 1 ↔ (x − 1)/2
- újra tükröz: Tükrözés újra
- c csúszka: c (vízszintes egyenes)

### Adatok
- c érték: 5
- megoldás közelítőleg: 2,24
- egyenes példa: 2x + 1

## 9. Találd el! – összefoglalás
Válaszd ki az alapfüggvényt, és állítsd be a csúszkákat úgy, hogy a görbéd ==fedje a célgörbét==! A szabályok a vásznon.

### Feliratok
- célgörbe: célgörbe
- talált: Talált!
- még nem: még nem fedi
- új cél: Új célgörbe
- szabályok: A négy lépés
- össz v: függőleges eltolás (v > 0: fel)
- össz u: vízszintes eltolás (u > 0: balra!)
- össz a: nyújtás, a < 0: tükrözés
- össz abs: a negatív rész felhajlik

### Adatok
- célgörbe magja: 7

<!-- Matematikai ellenőrzés (Python és a lecke L.checks() önellenőrzése, 2026-11-23):
  - (x + 3)² csúcsa (−3; 0); x² + 3 csúcsa (0; 3); 2x² és −x²: az x tengely pontjai (0; 0) helyben maradnak.
  - Bizonyítás (5. lépés): g(x) = f(x + 3); ha f(x₀) = y₀, akkor g(x₀ − 3) = f(x₀) = y₀, tehát az f grafikonjának
    minden (x₀; y₀) pontja a (x₀ − 3; y₀) pontba kerül – ez minden pontra igaz, nem csak a rajzoltakra.
  - x² − 2x − 3 = (x + 1)(x − 3) = (x − 1)² − 4 a [−2; 4] intervallumon: zérushelyek −1 és 3, minimum −4 az x = 1-ben,
    f(−2) = f(4) = 5, értékkészlet [−4; 5]; a [−2; 1]-en csökken, az [1; 4]-en nő.
  - |x² − 4|: zérushelyek ±2, helyi maximum 4 az x = 0-ban (a [−2; 2] szakasz felhajtva).
  - x² = 5 → x = ±√5 ≈ ±2,236 → két tizedesre ±2,24.
  - √x: értelmezési tartomány x ≥ 0, értékkészlet y ≥ 0; 1/x: x ≠ 0, y ≠ 0.
  - 2x + 1 megfordítása x ↦ (x − 1)/2; az x² (x ≥ 0) megfordítása a √x (x ≥ 0).
  - Fordított arányosság: 1 · 12 = 2 · 6 = 3 · 4 = 4 · 3 = 6 · 2 = 12, a csúcsok a 12/x hiperbolán.
  - A „Találd el!” célgörbéje a magból (U.rng) számolódik; az egyezést a lecke a két függvény értékeinek
    összevetésével dönti el (nem a paraméterekével), így pl. |x|-nél a = −1 és a = 1 egyaránt „talált”.
  Jelölés: D_f értelmezési tartomány, R_f értékkészlet (a tankönyvek egy része ÉT/ÉK rövidítést használ).
  Az f(x + u) eltolást a lecke u > 0-ra „balra” szabállyal mondja ki; egyes tankönyvek f(x − u) alakban
  tanítják (u > 0: jobbra) – a kettő ugyanaz a szabály.
-->
