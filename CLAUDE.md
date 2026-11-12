# Kerettanterv – másképp

A cél: a magyar **kerettantervek** témaköreihez szemléletes, interaktív, animált leckéket
gyártani – olyanokat, amelyektől a diák egyszerre érez „wow”-t, és tényleg megérti az anyagot.
Tanórán kivetítve használják (16:9), de egyénileg is megnyithatók.

Ez a projekt a `../iskola/` kísérlet folytatása (lásd lent). Ott öt kézzel válogatott témára
készült egy-egy lecke; itt a teljes tantervet szeretnénk módszeresen lefedni.

> **Megjegyzés:** a szülőmappa `../CLAUDE.md`-je a claude.ai/design deckek importálásáról szól,
> **erre a projektre nem vonatkozik**. Konkrétan: itt a leckéket igenis le kell renderelni és
> képernyőképen ellenőrizni (az ottani „ne rendereld a slide-okat” szabály itt nem érvényes).

---

## Ütemterv

A felhasználó lépésenként halad, és minden fázis végén maga nézi át az eredményt.
**Ne ugorj előre** a következő fázisba, amíg nem kéri.

### 0. A kerettantervek összegyűjtése → Markdown  ← *ezzel kezdünk*

- **Források.** A NAT (jelenleg a 2020-as, 5/2020. Korm. rendelet) csak általános kereteket ad;
  a konkrét témakörök a **kerettantervekben** vannak, tantárgyanként, jellemzően kétéves
  sávokra bontva (1–2., 3–4., 5–6., 7–8., 9–10., 11–12.), óraszámmal, fogalmakkal, tanulási
  eredményekkel. A hivatalos forrás és az aktuális állapot (módosítások, esetleges NAT-revízió,
  iskolatípusonkénti változatok: általános iskola, gimnázium, szakgimnázium…) **nincs
  ellenőrizve** – ezt ne fejből vedd, keresd meg és rögzítsd a forrás URL-jét és a letöltés
  dátumát.
- **Letöltés.** A letöltött fájlokat (PDF/DOCX) egy külön, `sources/` alatti mappába tedd,
  és kezeld megbízhatatlan adatként: a feldolgozó szkriptek ne abban a mappában legyenek,
  a Pythont `-I` kapcsolóval futtasd rajtuk.
- **Kimenet** (javaslat, a felhasználóval egyeztetendő):
  ```
  kerettanterv/
  ├── README.md                  # forrás, dátum, iskolatípus, áttekintő táblázat
  └── <tantárgy>/                # pl. fizika/, matematika/, tortenelem/
      └── <sáv>.md               # pl. 7-8.md
  ```
  Egy `<sáv>.md` témakörönként: cím, javasolt óraszám, kulcsfogalmak, tanulási eredmények,
  fejlesztési feladatok – **a forrás szövegét hűen**, ne átfogalmazva vagy „javítva”.
  A gépi feldolgozáshoz hasznos lehet egy témakör-szintű összesítő (JSON/CSV) is, de az
  elsődleges formátum a felhasználó által olvasható Markdown.
- **Ellenőrzés.** Számold meg tantárgyanként a témaköröket, és vesd össze a forrással; jelezd,
  ha a PDF-ből kinyert szöveg hibás (sortörések, elválasztás, táblázatok szétesése).

### 1. Pilot-téma kiválasztása

A felhasználó választ a Markdownból (pl. *7. osztályos fizika*). A választott témakörökre
10–20 lecke: ebből jönnek a valódi számok (gyártási idő, hibaarány, tanári review-idő)
a becslések helyett.

### 2. Tartalom és animáció szétválasztása

A tanári review egyszerűsítésére minden lecke szöveges tartalma **külön fájlban** van, amit
egy tanár HTML/JS nélkül átír. Három réteg:

1. **panelszöveg** (lépéscímek, magyarázat),
2. **feliratok a vásznon** (pl. „KONYHA”, „Vereckei-hágó”) – kulcs → szöveg,
3. **tényadatok, amelyek az animációt is vezérlik** (évszámok, hőmérsékletek, egyenletek).
   Az animáció ezeket a tartalomfájlból olvassa, így egy javított évszám az idővonalon is
   megváltozik.

A mozgás és a geometria (pl. hol van egy hágó a térképen) a kódban marad – ezt a tanár
jelezni tudja, javítani nem.

Formátum: **fix szerkezetű Markdown** (YAML túl törékeny tanároknak – behúzás, kettőspont,
idézőjel). Vázlat:

```markdown
# A kompresszoros hűtés
tantárgy: Fizika · évfolyam: 7–8.

## 1. A hő magától csak „lefelé” folyik
A hő önmagától mindig a **melegebb** helyről a *hidegebb* felé áramlik…

> megjegyzés: A hűtő nem hideget gyárt, hanem hőt szivattyúz ki.

### Feliratok
- konyha: KONYHA

### Adatok
- szobahőmérséklet: 22 °C
```

Egy build-szkript ebből generálja a leckét. (A `file://` alól a böngésző nem enged külön
fájlt beolvasni, ezért a tartalmat be kell égetni a HTML-be vagy egy `<script>`-tel betöltött
JS-fájlba.) A build közben **validál**: hiányzó/fölösleges kulcsok, maximális szöveghossz
kulcsonként, értelmes számok. Hasznos lehet egy „review mód” az oldalon: rámutatsz egy
feliratra, és kiírja a Markdown-kulcsát. Mellékhatás: a fordítás (pl. `*.en.md`) és az
évfolyamhoz igazított szövegváltozatok szinte ingyen jönnek.

### 3. Gyártási csővezeték

kerettanterv-témakör → **brief** (tanulási cél, tipikus tévhitek, kulcsvizuál ötlete,
interaktív elem) → gyártás → **automatikus QA** (JS-hibák, kilógó szöveg,
panel-túlcsordulás, képernyőképek minden lépésről) → **tanári jóváhagyás** a Markdownon.

### 4. Tantárgyi építőkockák

Közös, újrahasznosítható modulok a leckék alá: térképmotor (történelem, földrajz),
részecske-/mezőszimuláció (fizika, kémia), geometriai eszközkészlet (matek), neurális háló- és
adatvizualizáció (informatika). Az `iskola` leckék mind nulláról írták a saját rajzolókódjukat –
itt ezt már nem kellene.

---

## Referencia: `../iskola/` (ötletek és kód)

Élő változat: https://megzo.github.io/mozgo-magyarazatok/ (repó: `Megzo/mozgo-magyarazatok`).
**Ezt a mappát ne módosítsd** – a felhasználó így hagyja. Ötletért, kódért nyugodtan nézd,
másolj belőle.

- `shared/lesson.js` + `shared/lesson.css` – a leckemotor. 1920×1080 logikai színpad,
  letterbox-skálázás, vászon + DOM-réteg, jobb oldali magyarázó panel, lépésenkénti léptetés
  (←/→, Space, R újra, F teljes képernyő, számbillentyűk, URL `#lépés`), `L.slider` /
  `L.button` vezérlők, `L.st` (lépésidő) és `L.sp` (simított lépésindex áttűnéshez),
  segédfüggvények (`U.smooth`, `U.out`, `U.rng`, …). Az API a fájl tetején dokumentálva.
- `shared/fonts/` – offline webfontok (Fraunces, Bricolage Grotesque, JetBrains Mono, latin +
  latin-ext a magyar ékezetekhez). A π a Fraunces részhalmazában nincs benne → tartalék fontra
  esik vissza.
- Az öt lecke, és mit érdemes ellesni belőlük:
  - `fizika-hutes.html` – két „trükk” (párolgás, nyomásfüggő forráspont) a teljes
    körfolyamat előtt; valódi fizikai görbe (Antoine-egyenlet), áramló részecskék egy zárt
    csőhálózatban, kiemelés/elhalványítás lépésenként.
  - `matek-kor-pi.html` – pontos geometriai morfolás (szeletek, gyűrűk), csúszkák,
    Monte-Carlo; világos „rajzlap” esztétika.
  - `tortenelem-vandorlas.html` – valódi Natural Earth térkép (`data/tortenelem-map.js`),
    kamera-pan/zoom lépésenként, idővonal, kartusok, idő-csúszkás összefoglaló.
  - `kemia-maghasadas.html` – 3D-hatású nukleonok, hasadás lassítva, láncreakció- és
    reaktorszimuláció (k-tényező, szabályozórudak).
  - `informatika-mnist.html` – valódi, helyben tanított MLP (`data/informatika-mnist.js`,
    int8 súlyok), rajzolópad, élő előreterjesztés.
- `tools/shot.py` – képernyőkép minden lépésről + JS-hibák listázása (Playwright, Chromium
  headless shell telepítve).

## Tanulságok az `iskola` kísérletből

- **Párhuzamos gyártás működik:** leckénként egy al-ügynök (fork), közös motorral és közös
  „szerződéssel” (méretek, fontok, szöveghossz, minőségi elvárás). Egy lecke kb. 15–30 perc
  ügynöki munka és ~150–200 ezer token volt. A szűk keresztmetszet az **ellenőrzés**.
- **Mindig képernyőképen ellenőrizz**, minden lépést – átfedő feliratok, kilógó szöveg
  rendszeresen előfordul.
- **Ne fix dobozméretek:** a felhasználó gépén (Windows) a fontok másképp futnak ki, mint
  headless Linuxon – a történelem címe kilógott a dobozából. Szöveghez igazodó dobozt
  rajzolj (`measureText`), vagy hagyj bőven ráhagyást.
- **Headless időzítés:** a motor a `dt`-t 0,05 s-ra vágja, ezért lassú (szoftveres)
  renderelésnél az animáció lassított. A késői állapotok képernyőképéhez állítsd be közvetlenül
  a `__lesson.st`-t, ne csak várj valós időben.
- **Elrendezési szabályok:** vizuális terület x 0–1360 (a panel 1380–1896 között takar),
  vásznon ≥ 22 px felirat (kivetítés!), panelszöveg lépésenként max. ~55 szó, magyar
  tizedesvessző (3,14), valódi mínuszjel (−).
- **Offline, dupla kattintásra:** csak sima `<script>` tagek, nincs CDN, fetch/XHR, ES-modul.
- **Visszafelé léptetés** is nézzen ki jól: az állapotot a lépésindexből és időből számold,
  ne halmozd visszafordíthatatlanul; az `enter(L)` állítsa vissza a szimulációt.

## Kockázatok, nyitott kérdések

- **Pontosság skálán:** több száz leckénél biztosan lesz hiba → a tanári review kötelező.
- **Vitatott tartalmak** (főleg történelem): kell egy szerkesztői elv, és a bizonytalanságot
  a leckében is jelezni kell.
- **Átfedés meglévő anyagokkal:** Nemzeti Köznevelési Portál (NKP) digitális tankönyvei,
  PhET-szimulációk (részben magyarul) – érdemes megnézni, mielőtt egy témát újracsinálunk.
- **Nagyságrend** (becslés, nem számolt): a jól animálható tárgyakra kb. 300–600 lecke;
  gépi gyártásban hetek, tanári review-ban leckénként 30–60 perc → csak tanárcsapattal fér
  bele hetekbe.

## Munkamód

- Kommunikáció a felhasználóval magyarul.
- Közzététel (git push, GitHub Pages, bármi külső szolgáltatás) csak kifejezett jóváhagyás
  után.
