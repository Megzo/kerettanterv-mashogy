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
| tartomány | `50–70 ezer fő` · `25–28` · `10–30 µm` | nagygondolatjel (–); `ezer`, `millió` megengedett; ha a lecke mértékegység-családot kér (hosszúság, térfogat…), bármely egysége írható |
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
| képlet | `` `x^2 - 4x + 3 = 0` `` (két fordított aposztróf közt) | *x*² − 4*x* + 3 = 0: dőlt betűk, valódi mínusz; 1 szónak számít; a panelen egyben marad (csak `=`, `<`, `≤` … után törhet sort) |
| mértékegység a képletben | `` `9,81 m/s^2` `` · `` `5 cm` `` · `` `20 °C` `` · `` `"max"` `` | álló betű (m/s², cm, °C), a változó dőlt marad. Csak **szám után** egység: `` `F = m * a` `` – itt *m* tömeg (dőlt); `` `5 m` `` = 5 méter, `` `5m` `` = 5 · *m*. `"…"` közé írt szöveg mindig álló. A *t* (tonna) és az *a* (ár) nem egység. |
| … a képletben | `*` · `<=` `>=` `!=` `~=` · `->` `\|->` `=>` `<=>` · `+-` · `pi` `inf` · `NN` `ZZ` `QQ` `RR` · `√(x + 1)` vagy `gyök(x + 1)` | · ≤ ≥ ≠ ≈ → ↦ ⇒ ⇔ ± π ∞ ℕ ℤ ℚ ℝ √ |
| álló tört | `[[x/2]]` · `[[a + b/2]]` | emeletes tört (a felső és alsó rész a `/` két oldala) |
| halmaz | `{1; 2; 3}` · `{ }` | {1; 2; 3} – pontosvesszővel (a `{kulcs}` adat-hivatkozásban nincs `;`) |
| kémiai képlet (kémialecke) | `H2O` · `CO2` · `Ca(OH)2` · `Na^+` · `SO4^2-` · `->` | H₂O, CO₂, Ca(OH)₂, Na⁺, SO₄²⁻, → (Unicode-dal is írhatod: `H₂O`) |
| jel szó szerint | `\{` `\}` `\^` `\_` `` \` `` `\/` | { } ^ _ ` / |

A lecke **címében** (`#` sor) is működik: ott Unicode-jellé alakul (`` `x^2 - 1` `` → x² − 1,
`Na^+` → Na⁺, kémialeckében `H2O` → H₂O); ami így nem írható (`F_fel`), az jelöléssel marad.
Kémialecke feliratában a töltés is Unicode lesz: `Na^+` → Na⁺, `OH^-` → OH⁻.
A `képlet:` sor (nagy, kiemelt képlet) a panelen egyben marad; ha nem fér ki egy sorba, csak
relációjel (`=`, `<`, `≤`, `⇒` …) után törik.

Matematikaleckében ezen felül: `3/4` magától álló tört, `2 1/3` vegyes szám, a `képlet:` sor
egésze képlet, benne `(−b ± √(b^2 − 4ac)) / (2a)` emeletes tört lesz. Egyenlőtlenséggel ne kezdj
sort – a `>` megjegyzésdobozt nyit –, írd képletbe: `` `x > 3` ``.

**Az eredményt ne írd át kézzel – a lecke kiszámolja.** Ha egy eredmény a szövegben is
szerepel (`{összeg}`), és nem egyezik a lecke számolásával, a lecke piros sávval jelez.

### További adatfajták

| fajta | így írd | megjegyzés |
|---|---|---|
| nagy szám | `480 millió` · `4,5 millió/µl` · `38 billió` | **billió = 10¹²** (az angol *billion* = milliárd!) |
| terület, hosszúság… szorzószóval | `530 ezer ha` · `93 ezer km²` · `1,2 millió ha` | ha a lecke mértékegység-családot kér (terület, hosszúság, tömeg…): a család bármely egysége elé írható `ezer`, `millió`, `milliárd` |
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

### Magyar nyelv és irodalom: idézet, verssor, szóelem

**Idézett szöveg** (vers, prózarészlet) egy külön `### Idézet` blokkba kerül, soronként egy
kulccsal. A blokk előtt mindig ott áll, honnan való a szöveg – enélkül a build nem fogadja el:

```markdown
<!-- idézet: Petőfi Sándor: János vitéz (1844), 1. fejezet 1–4. sor · szöveg: MEK 01010 · szerző † 1849 · közkincs -->
### Idézet
- jv 1/1: Tüzesen süt le a | nyári nap sugára
- jv 1/2: Az ég tetejéről | a juhászbojtárra.
```

- A szöveget **betűhűen**, a megadott kiadás írásmódjával írd (régi írásmód is marad).
- A `|` a **sormetszet** helye; a leckében nem látszik, de a lecke tudja, hol áll meg a sor.
- A build megszámolja a szótagokat (= a magánhangzók száma), és szól, ha egy sor nem annyi, amennyit a
  lecke vár (pl. tizenkettő). Ha a forrásban is eltér, írd a sor végére:
  `<!-- szótagszám: 11, a forrásban is -->` – így csak figyelmeztet.
- A † utáni évszám a szerző (népköltészetnél a gyűjtő, fordításnál a fordító) halálának éve. Ha
  azóta még nem telt el 70 év, a szöveg védett: a build nem engedi idézni.

| fajta | így írd (az `### Adatok` alatt) | megjegyzés |
|---|---|---|
| rímképlet | `aabb` · `abab` · `abcb` | a lecke tudja, melyik idézet sorairól szól; x = rímtelen sor. Szól, ha a „rímelő” sorok vége nem cseng össze. Ha csak kiejtve rímel (*Sire* [szír] – *sír*), írd a sor végére vagy alá: `<!-- rím-kivétel: 5 – indoklás -->` (5. versszak; `5/2`: az 5. versszak 2. sora; `5–7`, `5, 9` is) – azt nem ellenőrzi |
| időmérték | `— ∪ ∪ \| — ∪ ∪ \| — ×` | `—` (vagy `-`) hosszú, `∪` (vagy `u`) rövid, `×` (vagy `x`) bármelyik; `\|` versláb, `\|\|` metszet. Szól, ha a jelek száma nem egyezik a sor szótagszámával, vagy hosszú magánhangzó rövid helyen áll |
| szóelemek | `kert + ész (képző) + ek (jel) + nek (rag)` · `virág (tő) + cserép (tő) + ben (rag)` · `-ban/-ben (rag)` · `lát + j (jel) + a (rag) = lássa` | fajta: tő, képző, jel, rag, kötőhangzó, előtag. Szól, ha rag után jel vagy képző jön, vagy ha a toldalék hangrendje nem illik a tőhöz – kivételnél (pl. *célba*) írd a sor végére: `<!-- ingadozó -->`. Ha a szó írva más, mint a szóelemek egymás után (*lát + j + a* → *lássa*), az `=` után írd az írott alakot; a leckében és a `{kulcs}` helyén ez jelenik meg. Ha a kulcs maga a szó (`lássa: …`), egyeznie kell vele |
| ejtés | `kútba [kúdba]` | a kiejtés szögletes zárójelben, a betűk szerint |
| szereplőkapcsolat | `Gergely – Éva: szerelem (I–V)` | barát, ellenség, család, szerelem, szolgál, vezet; zárójelben a részek (fejezetek), amelyekben a kapcsolat áll |

**Értelmezés:** ami nem tény, hanem egy lehetséges olvasat, az külön dobozba kerül:
`> értelmezés: A tűző nap talán a juhász szerelmének képe.` – a panelen „Egy lehetséges olvasat”
felirattal jelenik meg.

## Fejlesztőknek

```bash
python3 tools/build_lesson.py --all                       # minden lecke újragenerálása
python3 tools/build_lesson.py --selftest                  # a build öntesztje (tools/tests/)
python3 tools/build_lesson.py --stale                     # elavuló („frissítendő”) adatok
python3 tools/qa_lesson.py leckek/fizika-7-8/01-suruseg.html --back --review 6
python3 tools/qa_lesson.py … --det --data                 # determinizmus-próba, adatlista
python3 tools/qa_lesson.py … --jump-only                  # csak az ugrópróba (alapból is fut; --no-jump kihagyja)
python3 tools/qa_lesson.py … --states --at 1.5,settle      # + a lecke __qaStates-állapotai, köztes és nyugalmi kép
python3 tools/qa_lesson.py tools/tests/qa-kor3.html --states --at 1.5,settle   # a QA és a motor próbaoldala (0 hiba)
```

- `--at 1.5`: a köztes kép nem várja meg a lecke `idle()`-jét (az a mozgás közbeni pillanat fotója); csak a nyugalmi
  (`settle`) és a visszalépés-kép vár rá.
- `--states`: egy állapotnak elég az `st`-je (`{name: 'korai', st: 1.5}`, `set` nélkül) – akkor csak az időt állítja.
- Motor: `U.mix(a, b, t)` a `#rrggbb` mellett `rgb()`/`rgba()` színt is elfogad, így egymásba ágyazható
  (`U.mix(U.mix(a, b, t), c, s)`); a kimenet `rgb(r,g,b)` marad (átlátszó `rgba()` bemenetnél `rgba(…)`).

A QA képernyőképet készít minden lépésről (`build/qa/<lecke>/`), és kilistázza a JS-hibákat,
a túlcsorduló panelszöveget, a panel alá lógó, 22 px-nél kisebb vagy egymást átfedő
(forgatottnál a forgatott téglalap szerint, `L.pill` dobozánál a doboz szerint) feliratokat, és
ugrópróbát futtat (1. → utolsó, vissza, véletlen ugrások, betöltés `#N`-re) JS-hiba-figyeléssel. Figyelmeztet, ha egy
jel nincs a lecke fontjaiban (magyarleckében külön glifpróba: ő ű „ ” ‚ ’ – — ∪ ×), és hibát ad, ha a lecke
kattintás nélkül szólal meg. Új lecke írásához: [`SZERZODES.md`](SZERZODES.md).
