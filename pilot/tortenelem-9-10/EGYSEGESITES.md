# Történelem 9–10. – modul-egységesítő kör (2026-11-25)

Cél (a `pilot/tortenelem-7-8/EGYSEGESITES.md` mintájára): a sorozat 17, párhuzamosan gyártott leckéjének közös
moduljait egyeztetni a 7–8-as referenciával, a 15. lecke címét a tartalomhoz igazítani, a metrikasorokban jelzett
modulhibákat és kerülőutakat összegyűjteni (a közös modulokhoz ez a kör **nem nyúlt** – más sorozatok is
használják őket), és egy gyors vizuális egységesség-ellenőrzést végezni.

Az md5 a blokkra vonatkozik: a `/* ── MODUL: …` sortól az első utána következő `/* ── MODUL VÉGE…` sor végéig,
záró újsor nélkül.

## 1. Modulleltár

**Minden modulpéldány bájtra azonos a 7–8-as referenciával** (a 7–8 egységesítő kör utáni változatokkal); eltérő,
módosított példány nem volt, csere nem kellett. 17 lecke, 107 modulblokk (minden `MODUL:` sornak megvan a
`MODUL VÉGE` párja).

| modul | változat | md5 | példány | leckék | = 7–8 ref. |
|---|---|---|---|---|---|
| TtTipp | – | `fa839199626ca8aa31f3693a24150d81` | 17 | mind | ✓ |
| TortTimeline | – | `9c5cebae791ce43f3d93b5f2785e6dfd` | 17 | mind | ✓ |
| TortSource | – | `a59b107413f4949197b9d51f1c5a174e` | 17 | mind | ✓ |
| TortMap | v1.1 | `05bd08a1c2d32bdd050cba4c4fdbc2e2` | 15 | 01–14, 17 | ✓ |
| TortCards | – | `2c411077c00d1ba0d984102651b64c44` | 11 | 02, 03, 04, 05, 06, 07, 10, 13, 14, 15, 16 | ✓ |
| FoldChart | – | `92a03151ff1c93037ec9a611e70c9e91` | 8 | 02, 03, 04, 05, 10, 12, 14, 15 | ✓ |
| TortState | v1.1 | `5c74bd23baebc49fc0345746b1c4ab47` | 8 | 01, 02, 05, 11, 12, 13, 16, 17 | ✓ |
| MatChart | v1.1 | `02e3710065229ffbf2fd7f1ac155933a` | 7 | 01, 07, 08, 12, 14, 15, 16 | ✓ |
| TortTerr | v1.0 | `d7e8dcc3e82e93db533ecaef134c4a26` | 5 | 08, 09, 12, 14, 17 | ✓ |
| TortParl | v1.1 | `875d1496e5cd038b159ec13c96dde51f` | 2 | 02, 16 | ✓ |

Nem használja a sorozat: FoldChoro, TortCity, TortGlobe, TortScene. Új közös modul nem született (minden lecke
leckén belüli kóddal pótolta, ami hiányzott – lásd 4. fejezet).

A metrikasorok néhol „13-rendszervaltas”-t vagy „12-kadar-rendszer”-t adnak meg forrásnak (a TortTerr referenciája
a `07-masodik-vilaghaboru`) – az md5 azonos, a forrásmegjelölés így is helyes.

## 2. A 15. lecke címe

A régi cím („Mitől lett tízszer olcsóbb egy autó?”) nem egyezett a tartalommal: a T-modell ára 1909 → 1925 között
dollárban kb. 3,2× (825 → 260 dollár), egy gyári munkás órabérével mérve kb. 9× lett kevesebb (4342 → 481 óra).

- **Új cím:** „Mitől kellett kilencszer kevesebbet dolgozni egy autóért? – az ipari forradalmak és az új eszmék”
  (`.md` `#` sora, a `.html` `<title>`-je, a terv tervezőtáblája, lecketáblája és brief-címe).
- **3. lépés címe:** „Tízszer olcsóbb?” → „Harmadára vagy kilencedére?” (dollárban harmadára, munkaórában kilencedére
  – ezt mutatja a lépés dollár ↔ munkaóra kapcsolója). A `.md` végi vitatott-pont megjegyzés kiegészítve a régi
  címmel.
- **Mellékhatás:** a hosszabb cím a panel fejlécében 3 sorra tör (a régi 2 sor volt; böngészőben mérve: 52 → 79 px).
  Ettől a 8. lépés panelszövege 12 px-szel túlcsordult (462 > 450). Rövidebb, 2 soros változat csak a pontatlan
  „kilencszer olcsóbb” lett volna, ezért a 8. lépés első mondata rövidült: „A gyárak és a forradalmak új eszméket
  szültek.” → „Négy új eszme született.” A többi lépés a 3 soros fejléccel is elfér.
- QA (`--back --states --det --at 1.5,settle`, ugrópróba): **0 hiba**.
- A gyökér `index.html` már az új címet mutatja (újragenerálva).

## 3. Modulhibák és kerülőutak a metrikasorokból (NEM javítva – sorozatközi modulok)

| lecke | modul | mi | kerülőút a leckében | javaslat a következő közös körre |
|---|---|---|---|---|
| 10 | **TortMap v1.1** | equalEarth-ön, ha a térkép kisebb a színpadnál, a `frame()` a nézetdobozt (vb) a **teljes színpad** képernyőpontjainak inverzéből számolja; a pontok nagy része a peremen kívül esik (null) → a vb elfajul, Eurázsia, Afrika, Ausztrália kimarad (csak Amerika rajzolódik) | `frame()` után `MAPW.vb = [−190, −90, 190, 90]` | a vb a `rect`-en belül mintavételezzen; equalEarth-nél (vagy ha a minták > x %-a null) essen vissza a teljes világra. **Látható hiba más sorozatban is lehet** (minden kis, világtérképes TortMap) |
| 10 | TortMap.line | a ±180°-os varraton átlépő nyitott vonalat nem bontja (vízszintes csík) | kézi bontás (`wline`: Magellán, Manila-gálya) | a `line` bontsa a varratnál (mint a sokszögeknél) |
| 04 | TortMap | a `map-vilag` és a `map-mediterran` réteg kivágat-határán halvány egyenes varrat a szárazföldön (Kaszpi-tengertől É-ra, Szahara) – kis nagyításon látszik | nincs | rétegváltáskor átfedő sáv / a durvább réteg kivágása a finomabbal (adat- vagy modulkör) |
| 06 | adat | `map-europa` 60° K-nél véget ér → halvány varrat a 4. lépés térképén (a 7–8 10-es leckéje is jelezte) | nincs | `shared/tort/` adatkör: a map-europa kelet felé bővítése az Urálig |
| 09 | **TortTerr v1.0** | a `{land: true}` vágás csak a legfinomabb térképréteg (map-karpat, 42–51° É) bbox-án belül működik – délebbre (Balkán) a kitöltés eltűnik | saját szárazföld-maszk (`MAPK.base` fekete szárazfölddel, offscreen) + `destination-in` | a TortTerr v1.1 (7–8 EGYSEGESITES 5. fejezet) kapja meg: land-clip a vilag/mediterran rétegre is |
| 12 | TortTerr.fill | elemenként külön alfa → egymást átfedő félig átlátszó foltok sötétednek | offscreen kompozit (egyszer átlátszósított politikai réteg) | `T.fill(…, {flat: true})` – egy rétegre rajzol, egyszer alfáz |
| 05 | TortTimeline.cards | nincs kártya-igazítás: két, 2 évre eső eseménynél a vezetővonal átvágja a szomszéd kártyát | 1075/1077 kézzel (`tl.card` + saját vonal) | már a 7–8 nyitott 8. pontjában (vízszintes rétegezés, vezetővonal-sorrend) |
| 05, 15 | FoldChart.vspan | a sáv felirata a sáv szélességéhez zsugorodik (22 px alá is) | saját felirat | `o.labelMin` (alatta a felirat a sáv fölé/mellé kerül) |
| 15 | FoldChart.cursor | a kurzorcímke (y − 22) ütközik az y-tengely címével (y − 18), ha a kurzor a bal szélen van | saját címke | = 7–8 nyitott 5. pont (most két sorozatból) |
| 04 | FoldChart.endLabels | a vezetővonalat mindig a rajzterület jobb széléről húzza, akkor is, ha a görbe korábban véget ér | – (a hunok görbéjénél látszik) | a vonal a görbe utolsó pontjából induljon |
| 05 | TortSource | a mini-idővonal `Y.label` tört évre „1348.4563”-at ír | egész évet ad át | `Y.label` kerekítsen |
| 09, 12, 14 | TortSource.card | keskeny (≤ 420 px) kártyán a cím 22 px alá zsugorodik; a mini-idővonal kb. 150 px-szel megnyújtja a kártyát (két kártya nem fér egymás alá) | saját kártya / „Mikor?” sor | kompakt mód: `o.compact` (keskenyebb címkeoszlop, kisebb értékfont, idővonal nélkül) – a 7–8 nyitott 4. pontjával együtt |
| 08 | TortSource.stamp | nincs „vitatott” fajta | `TtTipp.stamp` | = 7–8 nyitott 3. pont |
| 05 | TortState | a kikapcsolt élek felirata halványan megmarad, átfedhet | – | kikapcsolt élnél a felirat is tűnjön el (`a` szerint) |
| 02 | TortState | az automatikus „irányít” nyíl nem kerüli ki a közbeeső dobozokat (6. lépés: átfut a dictator dobozán) | – | `bend` automatikusan, ha a szakasz dobozt metsz |
| 13 | TortState.card | sűrű sémán más feliratokra lóg | saját kártya az alsó sávban | `card` helye: `o.dock` (alsó/oldalsó sáv) |
| 16 | TortState.card | kézi x/y mellett nem rajzol a dobozhoz mutató jelet | – | vezetővonal kézi helynél is |
| 16 | MatChart | a kategória-alfelirat csak egysoros | saját tördelés | `sub` tördelése `maxW`-re |
| 08 | MatChart | hosszú kategóriafeliratok (> ~130 px) átfednek | rövid kategóriák | tördelés vagy automatikus döntés |
| 14 | MatChart.pie | kis szeleteknél ütköznek a címkék | – | címke-szétnyomás (mint FoldChart.endLabels) |
| 07, 12 | alfa-konvenció | TortTimeline / TortSource.card / TortCards szorozza a `globalAlpha`-t, a MatChart abszolút `o.a`-t vár | `al(1)` / `GA·p` | dokumentált viselkedés (7–8 4. fejezet); egységesítés csak egy közös, sorozatközi körben |
| 07 | TortCards | a tálca a kártyákat az összes kártya szerinti sorokba rendezi (10 kártya → 4 sor, a lerakottak helye üres marad) | tálcamagasság kézzel | doksiban jelezni |
| 06 | TortCards | zónacím fix 40 px – hosszú zónanév nem fér 316 px-be | rövid cím + alcím | zónacím `max` (kicsinyítés) |
| 01, 13 | TortMap.labels | ütközéskor a feliratot (folyónév, területnév) csendben elhagyja | horgonyok kézi hangolása, felsőbb folyásra tett folyónév | `o.onDrop` / QA-figyelmeztetés az elhagyott feliratra |
| 01 | TtTipp.stamp | az alfát a 4. paraméterből állítja (lépésidőzített megjelenéshez `p(t)` kell, nem 1) | – | doksiban jelezni |
| 03 | TtTipp | a fejléc nem tölt `#`-et a 2. kérdéssorban | leckén belüli fejléc | – |
| 11 | TortMap.base | a `mountains` réteg a színes foltokkal sáros barna masszát ad | kikapcsolva | – (a hívó dönt; doksiba) |
| 02 | build | a quote-forrás `DEATH_RE` csak 3–4 jegyű évet fogad (Kr. u. 14/17) | „† 0014/0017” a megjegyzésben | 1–4 jegyű év, „Kr. e./Kr. u.” előtaggal |
| 03, 10 | build | a `series` típus nem fogad x-mértékegységet (`ux`) évszámoknál | sima „év: érték” lista | `ux` elhagyható x-egységgel |
| 10 | build | a „(kitalált példa)” adatjelölés nem támogatott | „(modell)” | új jelölés vagy alias |
| 17 | build | idézetkulcsokhoz `"quotes": {kulcs: {}}` kell a specben | – | doksiba |
| 17 | font | a ✓/✗ jel nincs a fontokban | saját rajzolt pipa/iksz | `shared/fonts` részhalmaz bővítése vagy `U.check()` rajzoló |

**Sürgős (más sorozatot is érinthet):** a TortMap v1.1 equalEarth nézetdoboz-hibája (10) és a TortTerr `land`-vágása
a map-karpat bbox-án kívül (09) – mindkettő némán eltünteti a rajzot, a QA nem jelzi.

## 4. Ismétlődő, leckén belüli rajzolás – javaslat: TortPoly

Hét lecke (04, 08, 09, 12, 13, 14, 17; részben 06, 10) **kézzel rajzolt, vázlatos történeti sokszögeket** használ
(birodalmak, hódoltság, tartományurak, kuruc/császári ellenőrzés), és mindegyik a saját kódjában oldja meg ugyanazt:

| lecke | adat | időbeli változás | rajzolás | egyéb |
|---|---|---|---|---|
| 04 | `{poly}` + `{blobs}` kulcsállapotonként (395/450/475/565/600/650/720/800–814) | `framesAt(frames, y)` – két kulcsállapot közt áttűnés | `TortMap.region` (blur) | nézet-áttűnés `TortMap.lerp` |
| 06 | `BLOB_*` = `[lon, lat, km]` foltok | – | `TortMap.region` | gerincrajz külön |
| 08 | tartományúr-foltok (`blobs`) + `pt(k)` nevesített pontok | `lordA(Lr, y)` (kezdő/záró év) | `TortMap.region` + `TortTerr.fill` (mo1914hsz alap) | – |
| 09 | `Z(f, t, poly)` zónák, töréspontok helységnévvel | `zoneW(z, d)` = smooth be/ki `FADE` alatt | offscreen + saját szárazföld-maszk (`destination-in`) | sraffozott vazallus-réteg, `regionLabels(d)` |
| 12 | `Z(f, t, poly, o)` 17 kulcsállapot | `zoneW(z, d)` (azonos a 09-cel) | `TortTerr.fill({g: 'mo1914hsz', clip: poly})` offscreen-re, egyszer alfázva | sraff (`hatch`), `regionLabels(d)`, max-súly felirathoz |
| 13 | `CH9` közös határláncok + `CAT(…)`/`RV(…)` összefűzés (szomszédos országok közös éle egyszer adott) | – (1812 állapot) | saját `trace` | kategória (birodalom/függő/szövetséges) |
| 14 | kuruc foltok `KUR1705`/`KUR1710` (`blobs`), Temesi bánság/Határőrvidék sokszög | két állapot közti keverés (`w05`) | `TortMap.region` (`land: true`) + sraff | `swatchLine`/`swatchHatch` jelmagyarázat |
| 17 | `TILE` – 13 tájegység-csempe × 12 havi tábla (`HAVI[m]`) | hónaponkénti csempe-hozzárendelés | `TortProj.trace` + mo1914 vágás | sraffozott „vitatott” |

Közös elemek: (1) **[lon, lat] töréspontlista helységnév-megjegyzéssel**, (2) **érvényességi idő** (`f`/`t`
kulcsévvel, smooth áttűnéssel), (3) **kitöltés kerettel vágva** (mo1914hsz vagy szárazföld), **egyszer alfázva**
(átfedés ne sötétedjen), (4) **sraff** (vazallus/vitatott), (5) **címke** a legnagyobb súlyú zóna súlyával,
(6) **jelmagyarázat-minta** (négyzet / sraff / vonal), (7) a közös határok egyszeri megadása (13).

Javasolt API (NEM megvalósítva; leendő referencia: a 12-es lecke, mert ott van a legtöbb elem):

```
TortPoly.create(L, {map, terr?, fade: 0.6})        → P
P.zone(id, {poly | blobs | tile, f?, t?, c, hatch?, cat?, label?: {k, at: [lon, lat]}})
P.chain(id, [[lon, lat]…]); P.cat('a', '-b', 'c')  → közös határláncok összefűzése (a 13 CAT/RV-je)
P.weight(id, d)                                    → 0…1 (a 09/12 zoneW-je; f/t év vagy tört év)
P.draw(ctx, d, {clip: 'mo1914hsz' | 'land' | poly, alpha, flat: true, blur?})   → offscreen, egyszer alfázva
P.labels(ctx, d, o)                                → a TortMap.labels-szel, súly szerinti alfával
P.swatch(x, y, kind, col)                          → 'fill' | 'hatch' | 'line' | 'dash' jelmagyarázat-minta
P.at(d) / P.hit(px, py, d)                         → melyik zóna (kattintható térképhez)
```

A `land`-vágás a TortTerr v1.1-gyel együtt oldandó meg (3. fejezet, 09), a `flat` kompozit ugyanaz, mint a
TortTerr.fill-re javasolt. A jelmagyarázat-minta (`swatch`, `swatchHatch`, `swatchLine`) öt leckében külön él
(09, 12, 14, 15, 17) – ez a legkisebb, legkönnyebben kiemelhető darab.

## 5. Vizuális egységesség (gyors kör)

Mind a 17 lecke minden lépésképe átnézve (a meglévő `build/qa/<slug>/` képekből, áttekintő lapokon), a gyanús
helyek teljes felbontásban. Javítva:

- **14-ujranepesules, 5. lépés:** a forgatott „vázlatos – az 1914-es határral közelítve” bélyeg jobb vége a
  jelmagyarázat utolsó sorát („Határőrvidék – katonai igazgatás”) fedte (a QA a forgatott feliratot nem vizsgálja)
  → 11 px-szel lejjebb (`y` 990 → 1001), a forrássor fölött marad.
- **17-forradalom-1848, 1., 5., 6. lépés:** a térkép forrássora alátét nélkül futott át a partvonalon és a határon
  (5. lépés: a „Natural Earth” és a „vázlatosak” szó vonalba lógott) → papírszínű, lekerekített `L.pill` alátét.
- **15-iparosodas:** lásd 2. fejezet.

QA a három javított leckén (`--back --states --det --at 1.5,settle`, ugrópróba): **mind 0 hiba**.

Csak jelezve (nem hiba, stíluseltérés a párhuzamos gyártásból):

- a térkép címe hol keretes „chip” a térképen, hol sima címsor a térkép fölött – leckén belül is vegyesen
  (pl. 11, 17), egyik sem rossz;
- a térkép-forrássor helye változó (a térképen belül bal alul, a jelmagyarázat alatt, jobb alul) – egy közös
  `mapCredit()` segéd (alátéttel) egységesítené;
- a Tippelj-lépések „tipp előtt” képe (04/6, 07/3, 12/8, 14/4, 17/3) szándékosan üres grafikont/elmosott panelt
  mutat – rendben.

## 6. Nyitott tételek

1. TortMap v1.2: equalEarth nézetdoboz kis térképen (10), `line` varratbontás (10), rétegvarrat (04), labels
   elhagyás-jelzés (01, 13) – a 7–8 memo-névtér javaslatával együtt.
2. TortTerr v1.1: land-clip a vilag/mediterran rétegen (09), `flat` kitöltés (12) – a 7–8 5. fejezetéhez.
3. TortPoly (4. fejezet) – leendő referencia: 12-hodoltsag-merlege; első lépésként a `swatch` kiemelése.
4. FoldChart: `vspan` felirat-minimum (05, 15), `cursor` ↔ y-tengelycím (15; 7–8: 09), `endLabels` vezetővonal (04).
5. TortSource: tört év a mini-idővonalon (05), kompakt kártya (09, 12, 14), „vitatott” bélyeg (08).
6. TortState: kikapcsolt él felirata (05), nyíl-kikerülés (02), `card` dokkolás és vezetővonal (13, 16).
7. MatChart: alfelirat-tördelés (16), hosszú kategória (08), pie-címkeütközés (14).
8. Build: `DEATH_RE` 1–2 jegyű év (02), `series` `ux` (03, 10), „kitalált példa” jelölés (10), `quotes` spec (17).
9. Adat: map-europa 60° K-en túl (06; 7–8: 10).
