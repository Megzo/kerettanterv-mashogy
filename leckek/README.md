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

## Fejlesztőknek

```bash
python3 tools/build_lesson.py --all                       # minden lecke újragenerálása
python3 tools/build_lesson.py --selftest                  # a build öntesztje (tools/tests/)
python3 tools/qa_lesson.py leckek/fizika-7-8/01-suruseg.html --back --review 6
```

A QA képernyőképet készít minden lépésről (`build/qa/<lecke>/`), és kilistázza a JS-hibákat,
a túlcsorduló panelszöveget, a panel alá lógó, 22 px-nél kisebb vagy egymást átfedő
feliratokat. Új lecke írásához: [`SZERZODES.md`](SZERZODES.md).
