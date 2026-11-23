# Leckék

Interaktív, animált leckék tanórai kivetítésre (16:9). Megnyitás: dupla kattintás a
`.html` fájlra – internet nem kell.

| Lecke | Tantárgy, sáv | Kerettantervi témakör |
|---|---|---|
| [`fizika-7-8/01-suruseg.html`](fizika-7-8/01-suruseg.html) – Miért úszik a jég? – a sűrűség | Fizika 7–8. | 1. Bevezetés a fizikába |

**Kezelés:** ← → (vagy Szóköz) léptetés · R a lépés újrajátszása · F teljes képernyő ·
számbillentyűk: ugrás · **K** review mód (lásd lent).

## Minden lecke három fájl

```
01-suruseg.md          ← A SZÖVEG. Ezt szerkeszti a tanár.
01-suruseg.html        ← a rajz, a mozgás, a geometria (kód)
01-suruseg.content.js  ← a .md-ből generált fájl – kézzel ne szerkeszd
```

## Tanároknak: a szöveg javítása

1. Nyisd meg a `.md` fájlt egy egyszerű szövegszerkesztővel (Jegyzettömb, VS Code…).
2. Csak a **kettőspont utáni** részt írd át. A kettőspont előtti *kulcs* köti a szöveget a
   lecke kódjához – azt ne változtasd.
3. Mentés után futtasd (a projekt gyökeréből):
   ```bash
   python3 tools/build_lesson.py leckek/fizika-7-8/01-suruseg.md
   ```
   Ha valami nem stimmel (elírt szám, túl hosszú felirat, hiányzó sor), a szkript a
   **sor számával** megmondja, és nem írja felül a leckét.
4. Frissítsd a böngészőt.

A számok (pl. sűrűségek) az animációt is vezérlik: ha a `.md`-ben átírod a jég sűrűségét,
a grafikon, a merülési mélység és a százalékok is ehhez igazodnak.

### Review mód

Nyisd meg a leckét `?review` végződéssel (pl. `01-suruseg.html?review`), vagy nyomd meg a
**K** billentyűt. Ha az egeret egy feliratra vagy bekezdésre viszed, kiírja, hogy a `.md`
melyik kulcsából és hányadik sorából jön. Pirossal keretezett felirat: kódban rögzített
szöveg (pl. tengelyszámok, képletjelek) – ezt a tanár jelezni tudja, javítani nem.

## A `.md` formátuma

```markdown
# Miért úszik a jég? – a sűrűség
tantárgy: Fizika · évfolyam: 7–8. · témakör: 1. Bevezetés a fizikába

## Közös                               ← a lecke egészére érvényes feliratok/adatok
### Feliratok
- jég: jég
### Adatok
- jég sűrűsége: 0,92 g/cm³

## 1. Nehéz = elsüllyed?               ← lépés: sorszám + cím (a panel címe)
Egy jéghegy **több millió tonna**, mégis úszik.      ← bekezdések (üres sor választja el)

Tehát nem a tömeg dönt. ==Akkor mi?==

képlet: ρ = m / V                      ← kiemelt, nagy képlet
- felsorolás eleme                     ← felsorolás
> megjegyzés: Kérdezd meg az osztályt!   ← kiemelt megjegyzésdoboz

### Feliratok                          ← a vásznon megjelenő szövegek
- kérdés: Mi dönti el, hogy mi úszik?
### Adatok                             ← tényadatok, amelyek az animációt vezérlik
- csavar tömege: 10 g
```

Szabályok:

- Jelölések a szövegben: `**félkövér**`, `*dőlt*`, `==színnel kiemelt==`, `F_fel` (alsó index), `{adat kulcsa}` →
  az adat értéke egységgel (pl. `{csavar tömege}` → „10 g”).
- `<!-- … -->` közé írt szöveg megjegyzés, nem jelenik meg.
- Számok magyarosan: tizedes**vessző** (`0,92`), valódi mínuszjel (`−4 °C`), ezres tagolás
  szóközzel (`12 000 cm³`). A mértékegységet a lecke előírja – a build szól, ha más.
- Egy kulcs csak egyszer szerepelhet a fájlban; mindegy, melyik `##` alatt áll.
- Lépésenként legfeljebb kb. 55 szó panelszöveg (a build figyelmeztet; a lecke ezt szigoríthatja,
  a történelemleckékben 45 szó).
- Feliratban a `#` jel helyére a lecke számot ír (pl. `≈ # felnőtt tömege`).

### Évszám, dátum, koordináta, tartomány, becslés

Történelemleckékben az `### Adatok` alatt ilyen értékek is állhatnak. Hogy melyik kulcs milyen
fajta, azt a lecke előírja; a build szól, ha a formátum nem stimmel.

| fajta | így írd | megjegyzés |
|---|---|---|
| évszám | `Kr. e. 753` · `Kr. u. 476` · `1241` · `i. e. 490` | 0. év nincs (Kr. e. 1 után Kr. u. 1 jön); mínuszjelet ne írj |
| dátum | `1848. március 15.` · `1849. április` · `Kr. e. 44. március 15.` | hónap kisbetűvel, kiírva; a nap létezzen |
| koordináta | `47,50° É, 19,04° K` · `38° 9′ É, 23° 58′ K` | É/D és K/Ny; ha a pont kiesik a lecke térképéről, a build szól |
| tartomány | `50–70 ezer fő` · `25–28` | nagygondolatjel (–); `ezer`, `millió` megengedett |
| becslés | `kb. 25 ezer fő` · `~ 3000 km` · `Kr. e. 2560 körül` · `50–70 ezer fő (becslés)` | a lecke „kb.”-t vagy „becslés” bélyeget mutat |

A számolás a leckében helyes lesz: Kr. e. 776 és Kr. e. 753 között 23 év telt el, Kr. e. 1 és
Kr. u. 1 között 1. A `{kulcs}` hivatkozás a szövegben így jelenik meg: „Kr. e. 753”,
„1848. március 15.”, „kb. 50–70 ezer fő”. Bizonytalan számnál a forrást és a bizonytalanságot
egy `<!-- -->` megjegyzésben írd mellé.

### Képlet, tört, kitevő, kémiai képlet

Ugyanaz a jelölés minden tantárgyban, a panelen és a feliratokban is. A build kiírja, mit
alakított át, és szól, ha valami gyanús (pl. `3.14`, `5 - 3`).

| mit | így írd | így jelenik meg |
|---|---|---|
| kitevő | `x^2` · `10^-3` · `2^(n+1)` | x², 10⁻³, 2ⁿ⁺¹ (felső index) |
| alsó index | `F_fel` · `x_1` · `v_(max)` | F<sub>fel</sub>, x<sub>1</sub> |
| képlet | `` `x^2 - 4x + 3 = 0` `` (két fordított aposztróf közt) | *x*² − 4*x* + 3 = 0: dőlt betűk, valódi mínusz; 1 szónak számít |
| … a képletben | `*` · `<=` `>=` `!=` `~=` · `->` `\|->` `=>` `<=>` · `+-` · `pi` `inf` · `NN` `ZZ` `QQ` `RR` · `√(x + 1)` vagy `gyök(x + 1)` | · ≤ ≥ ≠ ≈ → ↦ ⇒ ⇔ ± π ∞ ℕ ℤ ℚ ℝ √ |
| álló tört | `[[x/2]]` · `[[a + b/2]]` | emeletes tört (a felső és alsó rész a `/` két oldala) |
| halmaz | `{1; 2; 3}` · `{ }` | {1; 2; 3} – pontosvesszővel (a `{kulcs}` adat-hivatkozásban nincs `;`) |
| kémiai képlet (kémialecke) | `H2O` · `CO2` · `Ca(OH)2` · `Na^+` · `SO4^2-` · `->` | H₂O, CO₂, Ca(OH)₂, Na⁺, SO₄²⁻, → (Unicode-dal is írhatod: `H₂O`) |
| jel szó szerint | `\{` `\}` `\^` `\_` `` \` `` `\/` | { } ^ _ ` / |

Matematikaleckében ezen felül: `3/4` magától álló tört, `2 1/3` vegyes szám, a `képlet:` sor
egésze képlet, benne `(−b ± √(b^2 − 4ac)) / (2a)` emeletes tört lesz. Egyenlőtlenséggel ne kezdj
sort – a `>` megjegyzésdobozt nyit –, írd képletbe: `` `x > 3` ``.

**Az eredményt ne írd át kézzel – a lecke kiszámolja.** Ha egy eredmény a szövegben is
szerepel (`{összeg}`), és nem egyezik a lecke számolásával, a lecke piros sávval jelez.

### További adatfajták

| fajta | így írd | megjegyzés |
|---|---|---|
| nagy szám | `480 millió` · `4,5 millió/µl` · `38 billió` | **billió = 10¹²** (az angol *billion* = milliárd!) |
| arány / ütem | `3 : 4 : 5` · `70/perc` · `60–100/perc` | |
| szög | `45° 30′` | szögperc: ′, nem aposztróf |
| tört | `3/4` · `2 1/3` · `−5/8` | ha a lecke egyszerűsített törtet kér, `6/8` hiba |
| pont | `A(2; −3)` · `(2; −1,5)` | pontosvessző, mert a vessző tizedesvessző |
| számsor | `2; 3; 5; 5; 5` · `−1,2; 0,9; 5,4 °C` | pontosvesszővel; az egység a végén |
| értékpárok | `0 °C: 13,3 · 20 °C: 31,6` | x: y párok, középponttal elválasztva |
| kifejezés | `x^2 − 4x + 3` · `3x + 4 = 19` | a lecke kiszámolja és ábrázolja |
| kémiai képlet | `H₂O` · `SO4^2-` | |
| reakcióegyenlet | `CH₄ + 2 O₂ → CO₂ + 2 H₂O` | a build ellenőrzi, hogy ki van-e egyenlítve |
| mély idő | `3,8 milliárd éve` · `7–6 millió éve` | |
| időzóna | `UTC+5:30` · `UTC−5` | |
| az adat éve | `8,2 milliárd fő (2025, frissítendő)` · `(előrejelzés)` · `(modell)` | a lecke jelzi; `--stale` listázza az elavultakat |
| adatkészlet | `ENSZ WPP 2024` | a nagy táblázat a `shared/foldrajz/` alatt van; az évszám egyezzen a táblázat verziójával |

Ha a lecke kéri (földrajz), minden adat mellé forrás kell: `<!-- forrás: …, lekérdezve: ÉÉÉÉ-HH-NN -->`
ugyanabban vagy a következő sorban, vagy a szakasz elején egyszer
`<!-- forrás (az alábbiakra): … -->`. Elsősegély-leckében a szakmai lektor egy
`<!-- Szakmai ellenőrzés: <szerep>, <dátum>, <ajánlás verziója> -->` blokkot ír a végére (név nélkül).

## Fejlesztőknek

```bash
python3 tools/build_lesson.py --all                       # minden lecke újragenerálása
python3 tools/build_lesson.py --selftest                  # a build öntesztje (tools/tests/)
python3 tools/build_lesson.py --stale                     # elavuló („frissítendő”) adatok
python3 tools/qa_lesson.py leckek/fizika-7-8/01-suruseg.html --back --review 6
python3 tools/qa_lesson.py … --det --data                 # determinizmus-próba, adatlista
```

A QA képernyőképet készít minden lépésről (`build/qa/<lecke>/`), és kilistázza a JS-hibákat,
a túlcsorduló panelszöveget, a panel alá lógó, 22 px-nél kisebb vagy egymást átfedő
feliratokat. Új lecke írásához: [`SZERZODES.md`](SZERZODES.md).
