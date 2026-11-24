# Build és QA – 3. javítókör

A Természettudomány 5–6 és a Magyar 5–6 sorozat gyártásából összegyűlt hat igény. Érintett fájlok:
`tools/build_lesson.py`, `tools/qa_lesson.py`, `shared/lesson.js`, `leckek/README.md`, új próbafájlok a
`tools/tests/` alatt (`kor3-adatok.*`, `kor3-hibak.*`, `qa-kor3.html`). Leckét nem írtam át.

## 1. Build – `morph`: írott (felületi) alak

**Igény:** ha az írott alak eltér a szóelemek összefűzésétől (`lát + j + a` → *lássa*), meg lehessen adni.

**Szintaxis:** `- lássa: lát + j (jel) + a (rag) = lássa` – az `=` után egyetlen szó, csak betűk.

**Kimenet:** `{"t": "morph", "parts": [lát, j, a], "surface": "lássa", "s": "lássa"}`. A `parts` változatlan
(a csempék a szóelemeket mutatják), az `s` – és így a panel `{kulcs}` hivatkozása és az `L.val(k)` – az írott
alak. `surface` csak akkor van, ha a `.md` megadja (a régi kimenet bájtra azonos).

**Ellenőrzés:**
- ha a kulcs egyetlen szó, és az első két betűje a szóé (`lássa`, `láttam`), akkor egyeznie kell az összefűzéssel
  vagy az írott alakkal – különben **hiba** (`lássa: lát + j (jel) + a (rag)` → „írd mögé: … = lássa”;
  `lássák: … = lássa` → „Elírás?”). Ha a kulcs nem a szó (`felszólító példa`, `kijelentő példa`), nincs
  ellenőrzés. (Az összes meglévő morph-kulcsot átnéztem: egyik sem ütközik.)
- `=` után nem egy szó (`= láss a`) → hiba; írott alak egy szóelemnél (`lát = lássa`) → hiba;
  az írott alak = az összefűzés → figyelmeztetés („elhagyható”).

**A `08-ige` kerülőútja:** a lecke ma a JS-ben számolja az alapalak és az írott alak eltérését
(`Ige.diff(látja, lássa)`), és a *lássa* csak felirat. Az új szintaxissal ez adatként is megadható –
ideiglenes másolaton kipróbálva: `- lássa: lát + j (jel) + a (rag) = lássa` hiba nélkül épül. A leckét nem írtam
át (a feladat szerint).

## 2. Build – `rhyme`: rím-kivétel

**Igény:** egy kiejtés szerinti rím (walesi bárdok, 5. vsz.: *Sire* [szír] – *sir*) miatt ne kelljen a
`"lines"` listában 120 kulcsot felsorolni.

**Szintaxis** – a meglévő `<!-- ingadozó -->` / `<!-- szótagszám: … -->` mintájára a `.md`-ben (a tanár látja és
javíthatja), a sor végén vagy közvetlenül alatta:

```markdown
- wb rímképlet: xaxa
<!-- rím-kivétel: 5 – Sire [szír] – sir: kiejtve rímel -->
```

Lista: versszak (`5`), tartomány (`5–7`), versszak/sor (`5/2`), vesszővel; az első ` – ` vagy `:` után indoklás.
A spec-ben ugyanez: `"except": [5, "5/2", "wb 5/2"]` (idézetkulcs is). A versszakot a rímképlet sorai közt
számolja (a képlet hossza = egy versszak); `"quotes": "wb"` csoportnál ez a vers versszaka.

**Kimenet:** a kivett sorok a `keys`/`p`-ben maradnak (a lecke ugyanúgy színezheti őket), csak a rímpróba hagyja ki
őket; + `"ex": [sorindexek]`, csak ha van kivétel. Hiba: nem létező versszak/sor, értelmezhetetlen lista.
Figyelmeztetés: fölösleges kivétel (a versszak betű szerint is rímel).

**Kipróbálva** a `14-walesi-bardok` ideiglenes másolatán (`"quotes": "wb"` + a fenti megjegyzés): 124 sor,
`ex` = a 17–20. sor, nincs rím-figyelmeztetés; a megjegyzés nélkül a build jelzi a *Sire – sir* eltérést.
A leckét nem írtam át.

## 3. Build – `dim`: szorzószó az egység előtt

`{"dim": "terület"}` (és a többi család) számadata most `530 ezer ha`, `93 ezer km²`, `1,2 millió ha` is lehet:
`v` = 530 000, `u` = `ha`, `base` (m²) = `v` × 10⁴, `s` = „530 ezer ha” (nem törő szóközzel). Az `"int"` a `v`-re
(hektárban) vonatkozik. A tartomány (`range` + `dim`) eddig is elfogadta (`50–70 ezer ha`), erre most teszt van.
Rossz egységnél az üzenet megemlíti, hogy szorzószó írható.

## 4. QA – `--states`: állapot `set` nélkül

`{name: 'korai', st: 1.5}` (csak idő) eddig „S.set is not a function” kivétellel leállította a QA-t. Most csak
az időt állítja. A „hatott-e” próba ilyenkor a lépés settle-képéhez hasonlít (ha az `st` = settle, jogosan
figyelmeztet).

## 5. QA – `--at` és a lecke `idle()`-je

Eddig minden `--at` kép előtt várt a lecke `idle()`-jére (max. 5 mp), így a `--at 1.5` kép valójában a nyugalmi
állapotot mutatta. Most csak a `settle` kép (és a visszalépés-kép) vár; a számmal megadott időpont és az
állapotképek nem. Alapbeállítással (`--at` nélkül) a viselkedés változatlan.

## 6. Motor – `U.mix` egymásba ágyazva

`U.mix(a, b, t)` a `#rrggbb` mellett `rgb(r,g,b)` és `rgba(r,g,b,a)` bemenetet is elfogad, így
`U.mix(U.mix(a, b, t), c, s)` helyes. Két `#…` bemenetnél a régi kódsor fut (bitre azonos). A kimenet
`rgb(r,g,b)` marad (több lecke `.replace('rgb(', 'rgba(')`-val épít rá); `rgba(…)` csak akkor, ha a kevert alfa
< 1, azaz átlátszó `rgba()` bemenetnél – ez eddig is hibás eredményt adott.

## Tesztek

| mit | hol | futtatás |
|---|---|---|
| morph írott alak, rím-kivétel (megjegyzés, spec, sor, idézetkulcs), dim szorzószóval (szám és tartomány) | `tools/tests/kor3-adatok.md/.html` (hibátlan, értékek), `kor3-hibak.md/.html` (8 várt hiba, 3 figyelmeztetés) | `python3 tools/build_lesson.py --selftest` |
| `--states` set nélkül, `--at 1.5` idle nélkül, `U.mix` 9 eset | `tools/tests/qa-kor3.html` (próbaoldal, mint az `mtext.html`) | `python3 tools/qa_lesson.py tools/tests/qa-kor3.html --states --at 1.5,settle` → 0 hiba |

A próbaoldal a régi eszközökkel bizonyítottan elbukik: a régi QA „S.set is not a function” kivétellel leáll,
`--states` nélkül a `--at 1.5` képnél 12 konzolhibát ad (az `idle()` a köztes képnél is lekérdezve), a régi
motorral pedig HIBASÁV jelzi az 5 eltérő `U.mix`-eredményt.

## Visszafelé kompatibilitás

- **Build:** a változtatás előtti `build_lesson.py`-vel és az újjal is lebuildeltem mind a 149 leckét (minden
  `NN-*.md`, amelynek van `.html` párja) egy-egy ideiglenes mappába: a `.content.js`-ek **és** a hiba-/figyelmeztetés-
  listák bájtra azonosak, és egyeznek a repóban lévőkkel. A helyben futtatott `--all` után a `git status`
  egyetlen `.content.js`-t sem mutat módosítottnak. Az új mezők (`surface`, `ex`) csak az új szintaxisnál jelennek
  meg; a dim-szám szorzószó nélkül ugyanazt adja, mint eddig. `--selftest`: minden rendben.
- **QA:** `--at` nélkül és állapotoknál a viselkedés változatlan; csak a számmal megadott `--at` képek nem várnak
  az `idle()`-re, és a `set` nélküli állapot nem dob kivételt.
- **Motor (`U.mix`):** két `#…` bemenetnél ugyanaz a kódsor fut. Mind a 149 leckét végigléptettem (minden lépés
  0,5 / 1,5 / 3 mp-nél és nyugalomban) úgy, hogy a nem `#…` bemenetű `U.mix`-hívásokat naplóztam: **egy lecke**
  érintett, a `matematika-9-10/03-fa-diagram` 4. lépése („Dobogó”). Ott a fa csomópontjainak színe
  `dark(MEDAL[…])` = már kevert `rgb()` szín, amit a modul `lite()`/`dark()` újra kever – a régi motor ezt
  feketének olvasta, ezért a csomópontok szürkék, a keretük fekete volt. Most a szándékolt arany árnyalatúak
  (régi/új képernyőkép összevetve; a lecke QA-ja 0 hiba). Ez **hibajavítás**, a lecke kódja nem változott.
- **Mintavételes QA** (új eszközökkel, `--states`): `magyar-5-6/08-ige`, `14-walesi-bardok`, `09-nepmese`,
  `termeszettudomany-5-6/14-energia`, `matematika-5-6/13-terulet`, `foldrajz-9-10/08-folyo` – mind **0 hiba**;
  `--at 1.5,settle --states` mellett is 0 hiba a `09-nepmese`, a `08-ige` és az `idle()`-t használó
  `tortenelem-5-6/09-honfoglalas` leckén. A `qa-kor3.html` próbaoldal: 0 hiba.
- A `termeszettudomany-5-6/16-folyo` fájljait nem írtam (a párhuzamos szerkesztés miatt).
