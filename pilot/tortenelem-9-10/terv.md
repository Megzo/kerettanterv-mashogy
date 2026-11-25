# Pilot: Történelem 9–10. (gimnázium, 4 évfolyamos) – a leckesor terve

Forrás: [`kerettanterv/tortenelem/9-10.md`](../../kerettanterv/tortenelem/9-10.md) (NAT 2020, gimnázium 4 évfolyamos
változat, *Történelem 9–12.* kerettanterv, 13 témakör, 121 óra). Az idézetek szó szerint onnan valók, a forrás elírásaival
együtt. A zárójeles szám (pl. „(7.)”) azt jelzi, ha az idézet nem a lecke fő témaköréből jön. A lecke-formátum leírása:
[`leckek/SZERZODES.md`](../../leckek/SZERZODES.md) – a 11. (Történelem 5–6.), a 20. (Történelem 7–8.) és az új 21. fejezet
(Történelem 9–10., kész szövege a 7. fejezetben). Előzmények:
[`pilot/tortenelem-5-6/terv.md`](../tortenelem-5-6/terv.md) (ugyanezek a korok, életmód- és portré-szinten – a 4. fejezet
szerkesztői elvei itt is érvényesek) és [`pilot/tortenelem-7-8/terv.md`](../tortenelem-7-8/terv.md) (20. század; a
modulok és a szerkesztői fegyelem mintája), valamint a modulok aktuális állapota:
[`pilot/tortenelem-7-8/EGYSEGESITES.md`](../tortenelem-7-8/EGYSEGESITES.md).

Jelölések az „Adatok” pontokban (mint a 7–8-ban):
- *(becslés)* – a forrás tartományt ad, vagy a szám kerekített nagyságrend; a leckében is ki kell mondani.
- *(vitatott)* – a szakirodalomban több érték vagy értelmezés él; a lecke tartományt vagy két forrást mutat.
- *(ellenőrizendő)* – a terv emlékezetből írta; **gyártás előtt forrásban ellenőrizni kell**.
- *(modell)* – a lecke didaktikus modellje, nem mért adat.
- *(kitalált példa)* – szemléltető adat, a `.md`-ben is így jelölve.

**A terv tényei nincsenek külső forrásban átnézve** (a 7–8-cal ellentétben itt nem futott ellenőrző kör – 0. döntés, 13.).
A koordinátori brief nem megbízható forrás (`pilot/EJSZAKAI-GYARTAS.md`, 7. tanulság): a leckeügynök **minden** számot,
dátumot és helynevet ellenőriz, a forrást a `.md`-be írja, és az eltérést a metrikasorában jelzi.

## 0. Döntések a felhasználó távollétében

A felhasználó nem volt elérhető, ezért ezekben magam döntöttem. Mind visszavonható.

1. **Mappa- és slugnevek.** Terv: `pilot/tortenelem-9-10/terv.md`; leckék:
   `leckek/tortenelem-9-10/NN-slug.{md,html,content.js}`; metrika: `pilot/tortenelem-9-10/metrika/NN-slug.md`. A
   metaadat-sor: `tantárgy: Történelem · évfolyam: 9–10. · témakör: N. <a kerettanterv témakörének címe>` (a
   `tools/build_index.py` a `Történelem` tárgyat és a `9–10` / „gimnázium (4 évfolyamos)” oszlopot már ismeri). **A
   slugok az egész repóban egyediek** – a 17 slugot a meglévő 180 körüli sluggal összevetettem, nincs ütközés. Közeli,
   de eltérő: `tortenelem-5-6/15-mohacs` (≠ `12-hodoltsag-merlege`), `tortenelem-5-6/18-gozgep` (≠ `15-iparosodas`),
   `tortenelem-7-8/11-forradalom-1956` (≠ `17-forradalom-1848`), `tortenelem-7-8/16-demokracia`.
2. **17 lecke, a 121 óra arányában.** Az 1. témakör (13 óra) 2 leckét kap (01 Athén + Hammurapi, 02 Róma), az 5. (14 óra)
   2-t (06 őstörténet, 07 Árpád-kori állam), a 6. (13 óra) 2-t (08 Anjouk, 09 Hunyadiak), a 7. (12 óra) 2-t (10
   világkereskedelem, 11 reformáció); a többi kilenc témakör egyet-egyet. A 4. (10 óra), 8. (10), 10. (10) és 12. (10)
   témakör sűrű – ott a lecke a legjobban animálható szálat viszi, a többi a 6.2 lefedettségi táblában „nem lefedett”.
3. **Gyártási mód: mind a 17 egyszerre** (10 párhuzamos ügynök, majd a maradék 7). Ezért **nincs referencialecke és
   nincs új közös modul.** Minden lecke kizárólag **kész, közös modulokra** épül, ezeket **bájtra azonosan** másolja
   (4. fejezet: forráslecke + sorszám + md5). Ami új rajz vagy szimuláció kell (Kleiszthenész-keverés, esetkalkulátor,
   jobbágy-költségvetés, futószalag, örökváltság-számoló, vázlatos birodalom-sokszögek …), az **leckén belüli kód**,
   `/* ── MODUL: … ── */` jelölés **nélkül** (nehogy két párhuzamos „modul” szülessen ugyanarra). Ha egy ügynök hibát talál
   egy modulban, a saját példányában javít, és pontosan leírja a metrikasorban (16. fejezet) – az egységesítés a gyártás
   utáni kör dolga.
4. **Két forráslecke a modulokhoz.** Hogy a másolás egyszerű és ellenőrizhető legyen, minden modult a
   `leckek/tortenelem-7-8/13-rendszervaltas.html`-ből (TtTipp, TortTimeline, TortSource, TortMap, FoldChart, TortParl,
   TortState, TortTerr) vagy a `leckek/tortenelem-7-8/12-kadar-rendszer.html`-ből (TortCards, MatChart) vesznek át (4.1).
   Mindkét lecke az EGYSEGESITES utáni, legfrissebb változatot tartalmazza; a sorszámok 2026-11-25-i állapotot mutatnak –
   az md5 a mérvadó, ha a sorszám elcsúszna.
5. **Szókorlát: 55 szó** (alapérték, nincs `maxWords`). A gimnazista bírja, a cél 40–50 szó; a hosszabb magyarázat
   forrás- vagy adatkártyára kerül a vásznon.
6. **Mélyebb, elemzőbb szint, mint az 5–6.** Az 5–6. évfolyam ugyanezeket a korokat életmód- és történetszinten
   dolgozta fel (Nílus-árvíz, vár és uradalom, céhes karrier, honfoglalási útvonal, tatárjárás-harapófogó, Nándorfehérvár
   folyózár, Kolumbusz „kicsi Földje”, nyomdák terjedése, Mohács taktikai térképe, Eger metszete, marhahajtás, gőzgép,
   március 15. órás csúszkája, tavaszi hadjárat operatív térképe). **Ezeket a kulcsvizuálokat nem ismételjük** – a 9–10
   kulcsvizuálja **államszervezet-összevetés, gazdasági és népességi adat, térképes elemzés, forráskritika**. Ahol a
   téma ugyanaz, a brief „Ne ismételd” sora megnevezi az 5–6-os leckét. A 7–8 `16-demokracia` (Athén–UK–USA–HU
   intézményséma) miatt a 13-as lecke nem a brit és amerikai sémát teszi középre, hanem a francia forradalom
   **időben változó** intézményrendszerét; a 01 az athéni demokráciát a Kleiszthenész-reform *mechanizmusán* mutatja.
7. **Történeti határok ókor–18. század: csak vázlatosan.** A `shared/tort/map-torthatar.js` (`TORT_HATAR`) 1914 előtti
   csoportot nem tartalmaz; **új közös adatfájl nem készül.** Ezért:
   - ókori, középkori, kora újkori birodalmak, hódoltság, kuruc terület, frontok: **leckén belül rajzolt sokszög** vagy
     lágy szélű folt (`TortMap.region` `{poly}` / `{blobs}`), „vázlatos” bélyeggel és dátummal; a töréspontok
     helységnévvel a kódban kommentezve, a kulcshelyek (városok, várak, csatahelyek) koordinátaként az `### Adatok` alatt;
     a `.md` megjegyzése felsorolja a két egybevetett atlaszt (geometriát onnan nem veszünk át);
   - a **középkori–kora újkori Magyar Királyság külső kerete** vázlatosan a `TORT_HATAR` `mo1914hsz` csoportjával
     közelíthető (TortTerr `outline`), **„vázlatos – az 1914-es határral közelítve”** felirattal; a `.md` mondja meg,
     miben tér el (Dalmácia, a boszniai bánságok, a Szörényi bánság, a Szepesség 13 elzálogosított városa 1412–1772, a
     Határőrvidék és a Temesi bánság külön igazgatása). Az `erdely` csoport a **mai értelmű** Erdély (Partiummal és a
     romániai Bánsággal) – az Erdélyi Fejedelemség határa **nem** ez, azt a lecke rajzolja;
   - a hivatalos terület- és népességszám mindig az `### Adatok`-ból jön, soha nem a sokszögből.
8. **Eredetkérdés (06): tudományos konszenzus és vita, áltudomány nem tényként.** A magyar nyelv uráli (finnugor, ugor
   ág) – ez a nyelvtudomány konszenzusa. A nyelvrokonság nem genetikai rokonság. A hun–magyar azonosság **középkori
   krónikás hagyomány** (Kézai, 1280-as évek) – „hagyomány” rétegként. A kettős honfoglalás (László Gyula) a
   szakmában kisebbségi, nem igazolt hipotézis – „vitatott”. Az archeogenetika eredményei (2018–2022) „keveredett
   népesség” szinten, a cikkek saját óvatos megfogalmazásával; a honfoglaló elit egyes egyéneinek belső-ázsiai
   kapcsolatát a lecke kimondja, de leszögezi, hogy ez **nem** igazolja a krónikás hun–magyar azonosságot, és a nyelvi
   eredetről nem szól. Áltudományos elmélet (pl. sumer–magyar nyelvrokonság) nem jelenik meg tényként; legfeljebb a
   forráskritikai lépésben, kifejezetten elvetett állításként, a cáfoló bizonyítékkal. Három szakmai lektor kell
   (`"review": ["történész", "nyelvész", "régész"]`).
9. **Vallások tárgyilagosan.** Leíró keret („a Biblia szerint”, „a muszlimok hite szerint”, „a keresztény tanítás
   szerint”), egyik vallás sem értékelve, nincs „igaz/hamis” tanítás. Vallási szöveg és élő hagyomány: „hagyomány”
   réteg (okker kartus), a történeti-kritikai adat: „forrás”/„rekonstrukció”. A reformáció és a katolikus megújulás
   kiegyensúlyozott; a vallásháborúk és az üldözések (keresztényüldözés, inkvizíció, Szent Bertalan-éj) ténye
   kimondva, hatásvadászat nélkül. Vallási lektor: 03 (`"review": ["vallástörténész"]`), 11 (`"review":
   ["egyháztörténész"]`).
10. **Erőszak méltósággal.** Keresztes háborúk, inkvizíció, rabszolgaság, a gyarmatosítás áldozatai, hódoltság,
    jakobinus terror, megtorlás 1849: számmal és forrással, tartománnyal; **nincs effektus, pontszám, animált
    halottszámláló, vér, kitalált áldozati történet, „Tippelj!” áldozatszámra**. Csatát nem játszunk le: a 9–10-ben a
    háború térképen (ki mit ellenőriz, mikor), erőviszony-oszlopon és forráson jelenik meg. A két fél semleges színű
    (indigó `#3b4590` / szilva `#7d3a66`), nincs „jó” zöld és „rossz” piros.
11. **Szerzői jog: 70 éves szabály, a fordítóra is.** Az ókori, középkori és reformkori **eredeti** szöveg közkincs, de a
    **modern magyar fordítása gyakran jogvédett** (pl. Hammurapi, Hérodotosz, Res Gestae, az Aranybulla mai
    fordításai). Ezért: szó szerinti idézet csak az eredetiből készült **saját fordítás** („saját fordítás”
    jelöléssel), vagy olyan fordítás, amelynek fordítója 1955-ben vagy előbb halt meg (a `.md`-ben a fordító neve és
    halálozási éve). Ha nem biztos: **parafrázis**. A reformkori magyar eredeti szövegek (Széchenyi † 1860, Kossuth
    † 1894, Kölcsey † 1838, Petőfi † 1849, Deák † 1876) közkincsek. Jogszabályszöveg (pl. 1848. évi törvénycikkek)
    `### Idézet`-ben, † nélkül. Fotó, festmény, metszet, térképlap nem kerül be; minden vizuál saját rajz. Uralkodóról,
    szentről, politikusról nincs „hiteles” portré: sziluett, pecsét- vagy érmestílus, névkártya („illusztráció”).
12. **Számformátum magyarul:** tizedesvessző, valódi mínuszjel, ezres tagolás (`16 886 815 kg` – a build `U+202F`),
    „Kr. e. 508/507” (a `year` típus egy évet fogad: a perjeles alak a szövegben, a vásznon Kr. e. 508), „Kr. e. 5.
    század közepe”, pénz „650 ezer forint”, „1 mina = 60 sékel”.
13. **Ellenőrzés a gyártásban.** Időkorlát miatt a terv tényei nincsenek külső forrásban átnézve. A leckeügynök minden
    számot forrásból ellenőriz (a brief ajánlott forrásokat ad), és a `.md` `<!-- forrás: … -->` sorába a ténylegesen
    használt forrást írja; az eltérést a metrikasorában jelzi. A brief *(ellenőrizendő)* jelű számát ellenőrzés nélkül
    nem szabad leckébe tenni.
14. **Kronológiai korlát.** A sorozat 1849-cel zárul (a megtorlással és egy kitekintő mondattal); mai politikai
    párhuzam, „mi lett volna, ha”, mai határvita nincs. A Habsburg–magyar viszonyban mindkét fél érvei (dinasztikus
    birodalomépítés, a török elleni védelem költsége ↔ rendi alkotmányosság, vallásszabadság) azonos súllyal.

---

## 1. Bevezető

A 9–10. évfolyam az ókortól 1849-ig ível. A gimnazista már nem a „mi történt?”-re kíváncsi elsősorban, hanem arra, hogy
**hogyan működött** egy rendszer (állam, egyház, gazdaság), **miből tudjuk**, és **mi változott meg, ha egy szabály
megváltozott**. Ezért a leckék mércéje: a vásznon egy *mechanizmus* működjön (szavazás, adózás, ármozgás, népességváltozás,
hatalmi jogkörök átrendeződése), és a diák a kapcsolóval, csúszkával maga lássa a következményt.

### 1.1 Hol ad egy animáció *valódi* belátást ebben a tárgyban?

| Belátás | Hogyan | Lecke |
|---|---|---|
| A demokrácia egy *térképészeti* trükkel kezdődött | Kleiszthenész szétválogatja Attika démoszait 30 harmadba, és mindegyik phülébe három különböző vidékről tesz egyet – a nemzetségi tömbök szétesnek | 01 |
| A „népgyűlés” nem egyenlő szavazatokat jelent | a 193 centuria szavazása: a lovagok és az első osztály 98 szavazata után a többi már nem is szavaz | 02 |
| Hogyan lesz köztársaságból egyeduralom, miközben az intézmények megmaradnak | intézményséma dátumcsúszkával: Caesar, majd Augustus kezébe kerülnek a jogkörök, a dobozok közben a helyükön maradnak | 02 |
| Egy üldözött kisebbség vallása 300 év alatt birodalmi vallás | exponenciális növekedési modell logaritmikus tengelyen, forráskritikával („modell, nem népszámlálás”) | 03 |
| Mekkora volt egy birodalom – és meddig tartott | birodalmak területe az időben (Róma, hunok, Bizánc, Omajjád kalifátus, Frank Birodalom) + vázlatos térkép dátumcsúszkával | 04 |
| Miért éhezett a jobbágy, ha egész évben dolgozott | a termés útja: vetőmag (1 : 3 hozam), tized, földesúri járadék – mi marad a családnak; a pestis utáni munkaerőhiány | 05 |
| Melyik tudomány mit tud mondani az eredetről | bizonyítékmátrix: nyelvészet, régészet, genetika, írott forrás × állítás, konszenzus/vitatott/elvetett jelöléssel | 06 |
| Kié volt a föld, és miből élt a király | királyi birtok → adományok → Aranybulla; III. Béla jövedelemjegyzéke forráskritikával | 07 |
| Az arany és a pénzpolitika | bányák térképe, a kamara haszna ↔ kapuadó modell: ki fizet, mennyit, és mi lesz a pénz értékével | 08 |
| Mennyibe került a védelem | Mátyás bevételei és kiadásai, a fekete sereg ára; az oszmán terjeszkedés dátum szerint | 09 |
| A pénz mennyisége és az árak | Amerikából Sevillába érkező ezüst évtizedenként ↔ árindex; a mennyiségi modell csúszkával | 10 |
| Ki dönti el, mit hisz az alattvaló | „cuius regio” kapcsoló ↔ tordai határozat; három egyházszervezet sémája | 11 |
| A hódoltság ára | a határ 1526 → 1699 dátumcsúszkán, a két magyar állam sémája, népesség-görbe Nyugat-Európával összevetve | 12 |
| Hogyan fordul a szabadság forradalma diktatúrába | intézményséma 1789 → 1804, a hatalommegosztás elemei dátum szerint kapcsolnak ki | 13 |
| Honnan jöttek az új lakók | népességgörbe 1720 → 1787 és vándorlási nyilak; kettős vámhatár áruáramlás-modellel | 14 |
| Mitől lett tízszer olcsóbb egy autó | futószalag-szimuláció: állomások száma → átfutási idő; Manchester népessége és halandósága | 15 |
| Miért tartott 15 évig egy reform | a rendi országgyűlés „törvényútja”: vármegyei követutasítás → alsótábla → felsőtábla → király; örökváltság-számoló | 16 |
| Mit változtattak meg az áprilisi törvények | intézményséma 1847 → 1848 április; a választójogosultak aránya; az ellenőrzött terület havonta 1848 szeptember – 1849 augusztus | 17 |

### 1.2 Kiválasztási elv

- **Témakörönként legalább egy lecke**; a leghosszabb témakörök kettőt (0. döntés, 2.).
- **A fogalomlista legyen a vásznon**, nem a panelen: a kerettanterv „Fogalmak” sorából a lecke témájához tartozók
  legalább fele feliratként, kártyán, sémadobozban vagy diagramcímként jelenik meg.
- **„Honnan tudjuk?”** minden leckében – a 9–10-ben **forráskritikai kérdéssel**: ki írta, mikor, milyen céllal,
  mennyivel az esemény után, mit nem tudhatott, mit akart elérni (pl. III. Béla jövedelemjegyzéke egy házassági
  ajánlathoz; Kézai hun–magyar története; Hamilton 1934-es ezüstadatai; Chadwick 1842-es halandósági táblája).
- **Adat és modell elválik:** a mért vagy forrásban közölt adat (`forrás`), a történészi becslés (`becslés`), a lecke
  saját egyszerűsítő modellje (`modell` bélyeg) a vásznon is másképp néz ki.
- **A tanári review gyorsítása:** minden szám, dátum, helyszín az `### Adatok` alatt; a sokszögek töréspontjai
  helységnévvel a kódban; a tanár jelezni tudja.

### 1.3 Szerkesztői elvek (az 5–6. évfolyam 4. fejezetén és a 7–8. évfolyam 1.3 pontján felül)

1. **Konszenzus, vita, elvetett nézet – három külön jelölés.** Ahol a szakma egyetért, a vászon tényt mond. Ahol
   vitatkozik (őstörténet, honfoglalás, létszámok, népességbecslések, a Szent Korona-tan értelmezése, a mohácsi vereség
   okai, a francia forradalom mérlege), **legalább két nézőpont** és a „vitatott” bélyeg; értékítélet helyett forrás,
   adat, kérdés. Ami tudományosan elvetett, az nem „egy másik nézőpont”: ha szerepel, a cáfolattal együtt (0. döntés, 8.).
2. **Monda és hagyomány érték, nem hazugság** (5–6: 4.4) – de a 9–10-ben a lecke megmondja, *mikor* és *miért*
   keletkezett (Anonymus kb. 1200, Kézai 1280-as évek, a Szent László-legendák, a millenniumi „ezer év”).
3. **Vallások** (0. döntés, 9.), **erőszak** (0. döntés, 10.), **szerzői jog** (0. döntés, 11.), **térképek**
   (0. döntés, 7.), **számformátum** (0. döntés, 12.).
4. **Felelősség pontos alanya** (7–8: 1.3.8): „az oszmán hadsereg”, „a Habsburg-udvar”, „a bécsi Haditanács”, „a
   Közjóléti Bizottság”, „a császári hadbíróság” – nem „a törökök”, „az osztrákok”, „a franciák”. Az 1848–49-ben a
   császár oldalán harcoló nemzetiségek **céllal és indokkal** szerepelnek (saját nemzeti követelések), nem árulóként.
5. **Anakronizmus kerülése:** a középkori térképen nincs mai zászló, nincs mai országnév a korabeli állam helyett
   (Német-római Császárság, nem Németország); „lovag”, „nemes”, „jobbágy” pontos jelentésben; a
   `modern: 1` vizek (tározók, csatornák) ókori–kora újkori térképen elhagyva.
6. **Modell ≠ történet.** A leckék saját modelljei (jobbágy-költségvetés, pénzmennyiség–ár, futószalag, örökváltság,
   növekedési modell) „modell” bélyeget kapnak, és a lépés kimondja, mit hagy ki a modell.
7. **Helynév:** a korabeli magyar név, első említéskor a mai hivatalos névvel (Nándorfehérvár – ma Beograd; Gyulafehérvár
   – ma Alba Iulia; Karlóca – ma Sremski Karlovci); ókori név a mai mellett (Aquincum – ma Budapest, Óbuda; Savaria –
   ma Szombathely).

---

## 2. A leckék

| # | slug | cím | témakör | fő modulok | nehézség (1–3) | lektor |
|---|---|---|---|---|---|---|
| 01 | `01-polisz-demokracia` | Ki hozza a törvényt? – Hammurapitól Periklész Athénjáig | 1 | TortState, MatChart, TortMap, TortCards | 3 | – |
| 02 | `02-romai-koztarsasag` | Hogyan lett a köztársaságból egyeduralom? – a római állam és jog | 1 | TortParl, TortState, FoldChart, TortCards, TortMap | 3 | – |
| 03 | `03-monoteizmus` | Hogyan lett egy üldözött hitből birodalmi vallás? – politeizmus, zsidó és keresztény monoteizmus | 2 (+3) | FoldChart (log), TortCards, TortMap, TortTimeline | 2 | vallástörténész |
| 04 | `04-hodito-birodalmak` | Mekkora volt egy birodalom, és meddig tartott? – Róma bukása, hunok, arab hódítás | 3 | FoldChart, TortMap (vázlatos sokszögek), TortCards, TortTimeline | 3 | – |
| 05 | `05-rendi-tarsadalom` | Mennyi maradt a jobbágynak? – rendek, terhek és válság a középkori Európában | 4 | MatChart, TortState, FoldChart, TortMap, TortCards | 2 | – |
| 06 | `06-magyar-ostortenet` | Mit tud a nyelvész, a régész és a genetikus? – a magyar nép eredetének bizonyítékai | 5 | TortMap, TortSource, TortTimeline, TortCards | 3 | történész, nyelvész, régész |
| 07 | `07-arpad-kori-allam` | Kié volt a föld? – az Árpád-kori állam a királyi birtoktól az Aranybulláig | 5 | MatChart, TortMap, TortTerr, TortCards, TortSource | 2 | – |
| 08 | `08-anjou-gazdasag` | Mitől lett erős az Anjou-kori király? – arany, kapuadó és a Szent Korona | 6 | TortMap, TortTerr, MatChart, FoldChart | 2 | – |
| 09 | `09-hunyadiak-torok` | Mennyibe került megvédeni az országot? – Zsigmondtól Mátyásig a török árnyékában | 6 | TortMap, TortTerr, MatChart, TortTimeline | 3 | – |
| 10 | `10-arforradalom` | Hová lett Amerika ezüstje? – felfedezések, árforradalom, korai kapitalizmus | 7 | FoldChart, TortMap (világ), TortCards | 2 | – |
| 11 | `11-reformacio` | Ki dönti el, mit hisz az alattvaló? – reformáció, katolikus megújulás, vallásbéke | 7 | TortState, TortMap, TortCards, TortTimeline | 3 | egyháztörténész |
| 12 | `12-hodoltsag-merlege` | Mibe került másfél évszázad? – a három részre szakadt ország mérlege | 8 | TortMap, TortTerr, TortState, FoldChart, MatChart | 3 | történész |
| 13 | `13-francia-forradalom` | Hogyan fordult a szabadság forradalma diktatúrába? – felvilágosodás és francia forradalom | 9 | TortState (timeline), TortCards, TortMap, TortTimeline | 3 | történész |
| 14 | `14-ujranepesules` | Honnan jöttek az új lakók? – Magyarország a 18. században | 10 | FoldChart, TortMap, TortTerr, MatChart, TortCards | 3 | történész |
| 15 | `15-iparosodas` | Mitől lett tízszer olcsóbb egy autó? – az ipari forradalmak és az új eszmék | 11 | FoldChart, MatChart, TortCards | 2 | – |
| 16 | `16-rendi-orszaggyules` | Miért tartott évtizedekig egy reform? – a reformkor országgyűlése és vitái | 12 | TortState, TortParl, TortCards, TortTimeline | 3 | – |
| 17 | `17-forradalom-1848` | Mit vívtak ki 1848-ban, és miért kellett megvédeni? – áprilisi törvények és szabadságharc | 13 | TortState, TortMap, TortTerr, MatChart, TortParl | 3 | történész |

Minden leckében ezen felül: **TtTipp** (Tippelj!, bélyegek), **TortTimeline** (a TortSource `Y`-ja miatt mindig kell),
**TortSource** („Honnan tudjuk?”). Nehézség = gyártási nehézség: 1 = egy fő vizuál, kevés adat; 2 = kész modulokra épülő
közepes interakció; 3 = összetett leckén belüli rajz/szimuláció vagy kényes tartalom.

**Témakörönként** (óra → lecke): 1 (13) → 01, 02 · 2 (5) → 03 · 3 (6) → 04 (+03: az iszlám az összevetésben) · 4 (10)
→ 05 · 5 (14) → 06, 07 · 6 (13) → 08, 09 · 7 (12) → 10, 11 · 8 (10) → 12 · 9 (5) → 13 · 10 (10) → 14 · 11 (5) → 15 ·
12 (10) → 16 · 13 (8) → 17.

---

## 3. Briefek

Közös minden briefben (a 21. fejezet szabályai szerint):

- **Tippelj!** – legalább egy jóslat a kipróbálás *előtt* (2–4 válasz a TtTipp-pel, a megoldás a választásig rejtve).
  Rossz tipp után: „Sokan gondolják így – nézzük meg!” **Soha** áldozatszámra, kivégzettek számára.
- **Kipróbálom** – legalább egy valódi interakció (csúszka, kapcsoló, húzás, kalkulátor, kattintható séma). Az állapot a
  lépés `enter()`-jében visszaáll, `init()`-ben is inicializálva (ugrópróba!).
- **Tévhit-lépés** – a felsorolt tévhitek közül legalább egyet a vászon *cáfol* (adattal, térképpel, forrással).
- **„Honnan tudjuk?”** – legalább egy forráskártya (TortSource `card`) forráskritikai kérdéssel.
- **Rétegek, bélyegek:** *forrás* (kékeszöld), *rekonstrukció* (szaggatott tinta), *hagyomány/monda* (okker kartus);
  bélyegek: „vázlatos”, „illusztráció”, „becslés”, „vitatott” (TtTipp.stamp – a TortSource nem ismeri), „modell”,
  „kitalált”.
- **Lépésszám:** 7–9, az utolsó összefoglalás; a lépéscímek kérdések vagy rövid állítások.
- **Spec:** `"sources": true` mindenhol; lektort kérő leckében `"review": […]` (2. tábla); a 06 és a 11 `"interpretive":
  true` (értelmező dobozt kér).

### 01 · `01-polisz-demokracia` – Ki hozza a törvényt? – Hammurapitól Periklész Athénjáig

- **Tanulási cél:** Az első államokban a törvényt az uralkodó hozta és az isteneknek tulajdonította (Hammurapi, Kr. e.
  18. század); a büntetés a sértett és az elkövető **társadalmi helyzetétől** függött. Athénban a hatalom lépésről
  lépésre a **démosz**hoz került: Szolón **vagyoni** elve (Kr. e. 594) után Kleiszthenész (Kr. e. 508/507) a
  **területi** elvvel szétverte a nemzetségi (vérségi) tömböket. A Periklész-kori demokrácia intézményei (népgyűlés,
  ötszázak tanácsa, sorsolás, választott sztratégoszok, cserépszavazás) közvetlen részvételt adtak – de csak a felnőtt
  férfi polgároknak. Spárta ellenpéldája: kevesek uralma (arisztokratikus/oligarchikus berendezkedés).
- **Kerettanterv:** „Az állam működése az Óbabiloni Birodalom példáján.” · „A pénz megjelenése.” · „Arisztokratikus
  köztársaság és demokrácia.” · „Kleiszthenész és Periklész.” · „Az athéni államszervezet és működése.” · Fogalmak:
  „városállam/polisz, arisztokrácia, démosz, demokrácia, népgyűlés, sztratégosz, cserépszavazás, rabszolga” ·
  Személyek: „Hammurapi, Kleiszthenész, Periklész” · Kronológia: „Kr. e. 508 Kleiszthenész reformjai, Kr. e. 5. sz.
  közepe az athéni demokrácia fénykora” · Topográfia: „Mezopotámia, Babilon, Athén” · fejlesztés: „Az állam
  szerepének bemutatása Hammurapi törvényeinek elemzésén keresztül.”, „Az athéni demokrácia és a római köztársaság
  működésének bemutatása.”, „A Periklész-kori athéni demokrácia ellentmondásainak feltárása.”, „Az athéni demokrácia
  összehasonlítása a modern demokráciával.” · tevékenység: „Ábra készítése az athéni demokrácia és a római köztársaság
  működési rendjéről.”
- **Tévhitek:** „Hammurapi törvénye: szemet szemért – mindenkinek ugyanaz.” (Osztályonként más.) „Athénban mindenki
  szavazhatott.” „A demokrácia = választások.” (Athénban a legtöbb tisztséget **sorsolták**.) „Kleiszthenész
  egyszerűen kihirdette a demokráciát.” (Átszervezte a polgárságot.) „Spárta is demokrácia volt, csak katonásabb.”
- **Ne ismételd:** `tortenelem-5-6/03-gorogok` (Marathón, falanx, olimpia), `tortenelem-7-8/16-demokracia` 1. lépése
  (népgyűlés + polgárok aránya) – itt a *mechanizmus* (phülé-keverés, sorsolás, intézmények útja) a lényeg.
- **Kulcsvizuál:** **Kleiszthenész-keverő** (leckén belüli rajz, „modell” + „vázlatos” bélyeg): Attika sematikus
  térképe három sávval (*város*, *tengerpart*, *belföld*), rajta 30 **harmad** (trittüsz) színes csempeként, eleinte
  4 régi phülé (nemzetségi alapon) foltjaiban. Gombnyomásra a csempék sorsolással 10 új phülébe rendeződnek úgy, hogy
  minden phülébe egy városi, egy parti és egy belföldi harmad kerül; a régi nemzetségi foltok szétszakadnak. Utána a
  10 phülé egyenként 50 tanácstagot küld a **boulé**ba (500 pötty, MatChart pontrács vagy saját rács). Mellette a
  **TortState**-séma: ekklészia → boulé → (sorsolt) tisztviselők, választott sztratégoszok (10), népbíróság (héliaia),
  cserépszavazás; Spárta elrendezése (`layout`): 2 király, geruszia, népgyűlés, 5 ephorosz.
- **Kipróbálom:**
  1. **Hammurapi-esetkalkulátor:** a diák kiválasztja a sértett és az elkövető helyzetét (*awīlum* szabad ember /
     *muškēnum* alárendelt szabad / *wardum* rabszolga) és a sérülést (szem, csont, fog) → a vásznon megjelenik a
     vonatkozó paragrafus (saját fordítás) és a büntetés (megtorlás vagy ezüstben fizetett kártérítés, mina/sékel).
  2. **Keverő:** „sorsolj újra” gomb – minden új sorsolás más phülé-összetételt ad, de mindig 3 vidékről; a régi
     nemzetségi tömb „szavazóereje” egy phülében mindig legfeljebb a harmada.
  3. **„Ki szavazhat?” szűrő** (MatChart pontrács, 100 pötty = Attika lakossága, *becslés*): kapcsolók – nő, gyermek,
     metoikosz, rabszolga, felnőtt férfi polgár; a végén kb. 10–20 pötty marad.
- **Tippelj!** 2. lépés: „Hammurapi törvénye szerint mi a büntetés, ha egy szabad ember egy rabszolga szemét üti ki?
  szemét kiütik / ezüstöt fizet a gazdának / nincs büntetés” (→ §199: a rabszolga értékének felét fizeti a gazdának).
- **Lépések:**
  1. Az állam az uralkodó törvénye – Hammurapi sztéléje: a kép felső része (a király a napistennel – *illusztráció*,
     saját vázlat), a szöveg 282 paragrafusa. Mezopotámia mini-térképen (TortMap, `map-mediterran`): Babilon.
  2. Szemet szemért? – esetkalkulátor, Tippelj!; a tanulság: a jog a **rendet** védi, nem az egyenlőséget.
  3. Ár, bér, ezüst – a törvény árakat és béreket rögzít ezüstben (pl. az orvos díja a beteg helyzete szerint); a
     **pénz** előtt mért fém fizetőeszköz; a vert pénz Lüdiában, Kr. e. 7. század (egy mondat + idővonal-pont).
  4. Athén: kié a hatalom? – arisztokrácia; Szolón négy vagyoni osztálya (sávdiagram: ki milyen tisztséget viselhet).
  5. Kleiszthenész keverője – a kulcsvizuál, „sorsolj újra”; **vérségi → területi elv**.
  6. Ötszáz tanácstag, ezernyi sorsolás – a TortState-séma; kattintásra kártya: ki választja / sorsolja, mennyi időre,
     mit dönt. A cserépszavazás (osztrakiszmosz) egy cserépkártyán (*vitatott*: a 6000-es küszöb értelmezése).
  7. Kik maradtak ki? – „Ki szavazhat?” szűrő; Periklész napidíja: a szegény polgár is ráér részt venni.
  8. Ellenpélda: Spárta – TortState `layout` váltás; mi hiányzik belőle Athénhoz képest (sorsolás, nyilvános népbíróság).
     Honnan tudjuk? – Hérodotosz és Arisztotelész (*Az athéni állam*, kb. Kr. e. 330 – kétszáz évvel Kleiszthenész
     után; a Spártáról szóló források többsége nem spártai szerzőtől).
  9. Összefoglalás – három modell egymás mellett (király törvénye / kevesek uralma / népuralom) és egy nyitott kérdés a
     modern demokráciához (képviselet, mindenki szavaz – utalás a 7–8 `16-demokracia`-ra).
- **Adatok:**
  - Hammurapi uralkodása: Kr. e. 1792–1750 (középső kronológia) *(vitatott – a kronológiai rendszerek eltérnek)*; a
    sztélé: Szúza, 1901–1902-es francia ásatás (J. de Morgan), ma a Louvre-ban *(ellenőrizendő)*; 282 paragrafus
    (modern számozás) *(ellenőrizendő)*.
  - §196: szabad ember szeme → szem; §197: csont → csont; §198: muškēnum szeme/csontja → 1 mina ezüst; §199:
    rabszolga szeme/csontja → a vételára fele; §200: fog → fog; §201: muškēnum foga → ⅓ mina *(ellenőrizendő)*; §215–217
    az orvos díja: 10 / 5 / 2 sékel *(ellenőrizendő)*. 1 mina = 60 sékel; 1 sékel kb. 8,3 g ezüst *(becslés)*.
    Forrás: L. W. King angol fordítása (1910; King † 1919 – közkincs) és R. F. Harper (1904; † 1914); a vásznon **saját
    fordítás** ezekből, így jelölve. A mai magyar fordítás nem idézhető szó szerint.
  - Lüdiai vert pénz (elektron): Kr. e. 7. század második fele *(becslés)*.
  - Szolón: Kr. e. 594 (arkhón) *(ellenőrizendő)*; osztályok: pentakosziomedimnoszok (≥ 500 medimnosz), hippeuszok
    (≥ 300), zeugitészek (≥ 200), thétészek (alatta) *(ellenőrizendő)*.
  - Kleiszthenész: Kr. e. 508/507; 10 phülé, 30 trittüsz (10 városi, 10 parti, 10 belföldi), kb. 139 démosz
    *(becslés)*; boulé 500 tag (phülénként 50) – Arisztotelész, *Ath. Pol.* 21 *(ellenőrizendő)*.
  - 10 sztratégosz, évente választva; cserépszavazás: legalább 6000 cserép *(vitatott: összesen vagy egy névre)*;
    száműzetés 10 évre.
  - Periklész: kb. Kr. e. 495–429 *(ellenőrizendő)*; napidíj bevezetése: Kr. e. 450-es évek *(becslés)*.
  - Attika lakossága a Kr. e. 5. század közepén kb. 250–300 ezer, ebből felnőtt férfi polgár kb. 30–60 ezer
    *(becslés, vitatott)* – ugyanaz a szám és forrás, mint a 7–8 `16-demokracia`-ban (a `> megjegyzés:` hivatkozik).
  - Spárta: 2 király, geruszia (28 vén + 2 király), 5 ephorosz, népgyűlés (apella) *(ellenőrizendő)*.
- **Modulok:** TortState (ekklészia-séma, Spárta-layout, kártya), MatChart (pontrács, sáv), TortMap (`map-mediterran`:
  Mezopotámia, Attika helye), TortCards (opcionális: tisztség → sorsolt / választott), TortSource, TortTimeline, TtTipp.
  Leckén belül: Kleiszthenész-keverő (sematikus Attika, csempék, determinisztikus sorsolás `U.rng` maggal), esetkalkulátor.
- **Review-pontok:** a paragrafusok saját fordítása (a tanár vesse össze egy kiadással); a három társadalmi csoport
  magyar neve (szabad ember / alárendelt / rabszolga) – a szakirodalomban többféle; a sematikus Attika nem térkép
  (bélyeg!); a 6000-es küszöb két értelmezése.

### 02 · `02-romai-koztarsasag` – Hogyan lett a köztársaságból egyeduralom? – a római állam és jog

- **Tanulási cél:** A római köztársaság (hagyomány szerint Kr. e. 510/509) a hatalmat **megosztotta és időben
  korlátozta**: két consul egy évre, a senatus tanácsol, a népgyűlések választanak és törvényt hoznak, a **néptribunus**
  vétózhat, válság idején **dictator** legfeljebb fél évre. A népgyűlés szavazata **vagyon szerint súlyozott** volt
  (centuriák). A polgárháborúk korában Caesar, majd Augustus a régi intézményeket **meghagyva** gyűjtötte kezébe a
  jogköröket – így lett a köztársaságból **császárság** (principatus). A **római jog** néhány elve máig él; a
  **polgárjog** fokozatosan kiterjedt (212). Pannónia **provincia** volt, városokkal és légiós táborokkal.
- **Kerettanterv:** „A vérségi, a vagyoni és a területi elv.” · „A római köztársaság államszervezete és működése.” ·
  „Köztársaságból egyeduralom: Caesar és Augustus.” · „A római jog néhány máig élő alapelve.” · „A birodalom
  kiterjedése és a provinciák (Pannónia).” · Fogalmak: „patrícius, plebejus, consul, senatus, dictator, néptribunus,
  császár, provincia, légió, limes, polgárjog” · Személyek: „Julius Caesar, Augustus” · Kronológia: „Kr. e. 510 a
  köztársaság kezdete Rómában, Kr. e. 44. Caesar halála” · Topográfia: „Itália, Róma, Római Birodalom, Pannónia,
  Aquincum, Savaria” · fejlesztés: „A római jog alapelveinek felidézése és azonosítása.”, „A demokrácia és a diktatúra
  összehasonlítása.”, „Caesar diktatúrája előzményeinek, okainak feltárása.”, „Pannónia jelentősebb városainak
  azonosítása.”
- **Tévhitek:** „A római köztársaság demokrácia volt, egy ember – egy szavazat.” „Caesar volt az első római császár.”
  „Augustus eltörölte a senatust.” „A dictator mindig zsarnok.” (Eredetileg alkotmányos, időkorlátos tisztség.) „Minden
  latin jogi mondás a rómaiaktól származik.” (Sok középkori vagy újkori megfogalmazás.)
- **Ne ismételd:** `tortenelem-5-6/04-pannonia` (a birodalom színfoltja évszázadonként, limes-tornyok, Aquincum →
  Óbuda) – a provincia itt csak egy kis térképlépés (városhálózat + polgárjog), nem kiterjedés-animáció.
- **Kulcsvizuál:** két kép.
  (a) **A centuriák szavazása** (TortParl `hemi`, 193 „ülés” = 193 centuria, osztályonként egy tónus + minta: lovagok
  18, I. osztály 80, II–IV. 20–20–20, V. 30, egyéb 5): a szavazás a lovagokkal és az I. osztállyal **kezdődik**; a 97.
  azonos szavazatnál a patkón kigyullad a „többség” vonal (TortParl `lines`: 97), és a többi centuria halványan
  „nem szavazott” marad. Mellette sáv (TortParl `bar`): a polgárok aránya *(becslés)* ↔ a centuriák aránya.
  (b) **A köztársaság sémája dátumcsúszkával** (TortState `timeline`): consulok, senatus, népgyűlések, néptribunusok,
  dictator, censor; a csúszka Kr. e. 509 → Kr. u. 14: Sulla dictaturája (Kr. e. 82), Caesar örökös dictator (Kr. e.
  44), Augustus (Kr. e. 27, Kr. e. 23): a dobozok a helyükön maradnak, de egyenként a princeps „irányítása” alá kerülnek
  (`over`; a `T.over` felirata „a princeps kezében”) – a forma marad, a tartalom változik.
- **Kipróbálom:**
  1. A centuria-szavazás csúszkája: „Mi lett volna, ha minden polgár szavazata egyenlő?” kapcsoló – a polgárok becsült
     aránya szerint újraosztott patkó (*modell*).
  2. Az intézményséma dátumcsúszkája; kattintásra kártya: ki választja, mennyi időre, kit ellenőriz, mi lett vele
     Augustus alatt.
  3. TortCards: hat jogi elv → hat mai helyzet párosítása (pl. „hallgattassék meg a másik fél is” ↔ bírósági tárgyalás);
     egy kártya „csapda”: egy újkori latin mondás, amely *nem* római (a megoldás megmondja, kitől való).
- **Tippelj!** 2. lépés: „A 193 centuriából hányat kellett megnyerni a döntéshez – és hányadik osztálynál dőlhetett el
  a szavazás?” – válasz: „97; már az első osztály után (18 + 80 = 98)”.
- **Lépések:**
  1. Királyok után – Kr. e. 510/509, a hagyomány és a régészet (*hagyomány* réteg: Lucretia-történet; *rekonstrukció*:
     a köztársaság kezdete). Patrícius és plebejus.
  2. Vagyon szerint szavaznak – a centuriák, Tippelj!, patkó.
  3. Ki ellenőriz kit? – a köztársaság sémája: kettősség (2 consul), időkorlát (1 év), vétó (néptribunus, Kr. e. 494
     *hagyomány*), a dictator fél éve.
  4. A rendszer repedései – hódítások, gazdag és szegény polgárok, hadsereg a hadvezérhez hű (Marius hadsereg-reformja
     egy mondatban); Sulla. Idővonal-mini.
  5. Caesar – Rubicon (Kr. e. 49), örökös dictator (Kr. e. 44 eleje), Kr. e. 44. március 15. A csúszka itt kikapcsolja
     az időkorlátot.
  6. Augustus – Kr. e. 27: a „köztársaság helyreállítása” a forrás szerint, valójában a jogkörök egy kézben (`over`).
     Honnan tudjuk? – *Res Gestae* (Augustus saját beszámolója, közkincs latin; saját fordítás): mit akart elhitetni?
  7. Polgárjog és provincia – a censusszámok a *Res Gestae*-ből (Kr. e. 28, Kr. e. 8, Kr. u. 14) FoldChart-oszlopon;
     212: Caracalla rendelete. Pannónia kis térképe (TortMap, `map-karpat`): Aquincum, Savaria, Scarbantia, Sopianae,
     Brigetio, a limes vonala a Dunán (vázlatos).
  8. A római jog öröksége – párosítás (TortCards); a XII táblás törvények (Kr. e. 451–450 *hagyomány szerinti*
     dátum).
  9. Összefoglalás – Athén ↔ Róma ↔ Augustus egy táblában (ki dönt, ki választ, ki ellenőriz).
- **Adatok:**
  - A köztársaság kezdete: Kr. e. 510 (a kerettanterv szerint) / Kr. e. 509 (a hagyományos varrói számítás) –
    *(vitatott, a lecke mindkettőt megnevezi)*.
  - Comitia centuriata: 193 centuria = equites 18 + I. osztály 80 + II. 20 + III. 20 + IV. 20 + V. 30 + 5 (mesteremberek,
    zenészek, proletarii) *(ellenőrizendő – Livius 1,43 és Dionüsziosz; a Kr. e. 3. századi reform után más)*; a
    többség 97.
  - Consul: 2, egy évre; dictator: legfeljebb 6 hónap; néptribunus: Kr. e. 494 *(hagyomány)*; senatus kb. 300 tag
    (Sulla után 600, Caesar alatt kb. 900) *(ellenőrizendő)*.
  - Sulla dictator: Kr. e. 82–79 *(ellenőrizendő)*; Rubicon: Kr. e. 49. január; Caesar dictator perpetuo: Kr. e. 44
    február *(ellenőrizendő)*; halála: Kr. e. 44. március 15.; Augustus név: Kr. e. 27. január 16. *(ellenőrizendő)*;
    tribunusi hatalom élethossziglan: Kr. e. 23; halála Kr. u. 14. augusztus 19.
  - *Res Gestae* 8: polgárok száma Kr. e. 28: 4 063 000; Kr. e. 8: 4 233 000; Kr. u. 14: 4 937 000 *(ellenőrizendő;
    az ugrás értelmezése vitatott – a nők és gyerekek beszámítása?)*.
  - Constitutio Antoniniana: 212 (Caracalla).
  - Pannónia városai (coord, `box: [9, 42, 30, 51]`): Aquincum 47,56° É 19,05° K; Savaria 47,23° É 16,62° K; Scarbantia
    47,68° É 16,59° K; Sopianae 46,07° É 18,23° K; Brigetio 47,74° É 18,18° K; Carnuntum 48,11° É 16,86° K
    *(ellenőrizendő)*.
  - Jogi elvek (latin + magyar): *audiatur et altera pars*, *nemo iudex in causa sua*, *pacta sunt servanda*, *in
    dubio pro reo*, *ne bis in idem* – mindegyiknél a `.md` megjegyzésben, hogy ókori forrásban így szerepel-e, vagy
    későbbi megfogalmazás *(ellenőrizendő; pl. a „nullum crimen sine lege” Feuerbach, 1801 – ez a csapdakártya)*.
- **Modulok:** TortParl (`hemi`, `bar`, `palette`, `legend`), TortState (`timeline`, `over`, `card`), FoldChart
  (oszlop), TortCards, TortMap (`map-karpat`), TortSource, TortTimeline, TtTipp.
- **Review-pontok:** a TortParl semleges tónusai itt **vagyoni osztályokat** jelölnek (nem pártot) – a jelmagyarázat
  mondja ki; az `over` bordó „irányít” nyila itt az egyeduralkodó, nem párt; a centuriarendszer változásai (Kr. e. 241
  utáni reform) egy mondatban; a censusszámok értelmezése.

### 03 · `03-monoteizmus` – Hogyan lett egy üldözött hitből birodalmi vallás? – politeizmus, zsidó és keresztény monoteizmus

- **Tanulási cél:** Az ókori Kelet és a görög–római világ vallásai **többistenhívők** (politeizmus); a **zsidó vallás**
  egyetlen Istenben hisz, a Tízparancsolatban és a Héber Bibliában rögzített szövetségben; a jeruzsálemi templom
  lerombolása (70) után a **diaszpóra** közösségei és az írás köré szerveződő vallásgyakorlat tartották meg. A
  **kereszténység** a zsidóság egyik irányzataként indult; Pál missziója nyitotta meg a nem zsidók felé. Kis,
  időnként üldözött közösségből a 4. századra **birodalmi vallás** lett: 313 milánói rendelet, 325 niceai zsinat
  (Szentháromság-tan), 380 államvallás. A növekedés üteme **modellből** becsülhető, mert népszámlálás nincs.
- **Kerettanterv:** „A politeizmus az ókori Keleten.” · „Görög és római istenek.” · „A zsidó monoteizmus.” · „Jézus
  tanításai.” · „A páli fordulat.” · „Keresztény-üldözések, a kereszténység elterjedése a Római Birodalomban.” · „A
  Szentháromság-tan.” · Fogalmak: „politeizmus, monoteizmus, zsidó vallás, Ószövetség/Héber Biblia, Tízparancsolat
  próféta, jeruzsálemi templom, diaszpóra,, Messiás, keresztény vallás, keresztség és úrvacsora, apostol, misszió,
  Biblia, Újszövetség, evangélium, püspök, zsinat.” · Kronológia: „a keresztény időszámítás kezdete (Kr. e. és Kr. u.),
  313 a milánói rendelet, 325 a niceai zsinat.” · fejlesztés: „A zsidó és a keresztény vallások jellemzőinek
  összehasonlítása.”, „A kereszténység terjedésének végigkövetése térképen.” · (3.) tevékenység: „A monoteista vallások
  (zsidó, keresztény, iszlám) összehasonlítása különböző szempontok alapján.”
- **Tévhitek:** „A rómaiak mindig és mindenhol üldözték a keresztényeket.” (Hullámokban: 64, 250, 303–311.) „Constantinus
  államvallássá tette a kereszténységet.” (313: türelem; 380: Theodosius.) „A kereszténység a zsidóságtól teljesen
  független új vallás volt.” „A zsidóság a 70-es pusztulás után eltűnt a Közel-Keletről.” „A politeizmus = babona, a
  monoteizmus = fejlettebb.” (Értékítélet – a lecke nem rangsorol.)
- **Ne ismételd:** `tortenelem-5-6/05-keresztenyseg` (Pál útjai térképen, gyülekezetek pontjai 100 → 300,
  levél-útvonalválasztó) – itt **nincs** útvonal- és gyülekezettérkép; a terjedés modellen és jogi státuszon át jön.
- **Kulcsvizuál:** **növekedési modell logaritmikus tengelyen** (FoldChart `log`): a keresztények becsült száma 40 és
  350 között évtizedenként kb. 40 %-os növekedéssel (Stark-modell) – egyenes vonal a log tengelyen, „modell” bélyeg; a
  birodalom becsült lakossága (kb. 60 millió) vízszintes vonal; a jogi státusz sávokként a háttérben (FoldChart
  `vspan`: tűrt / üldözött / türelem / államvallás). Mellette **összehasonlító tábla** (TortCards-zónák): zsidó vallás ↔
  kereszténység ↔ (görög–római politeizmus) – szent irat, istenkép, közösség vezetése, szertartás, szent hely.
- **Kipróbálom:**
  1. Csúszka: évtizedenkénti növekedés 20 % … 60 % → mikor érné el a modell a birodalom lakosságának felét? A valós
     becslések (kb. 10 % 300 körül *(vitatott)*) pontként a görbén. A tanulság: kis, állandó növekedés is óriási
     számot ad 300 év alatt – a modell nem bizonyít, csak megmutat egy lehetőséget.
  2. TortCards: 10 jellemző → zsidó / keresztény / mindkettő (a „mindkettő” zóna a közös gyökér).
  3. Kattintható idővonal (TortTimeline): 64, 250, 303, 311, 313, 325, 380 – kártyán: ki adta ki, mit mondott (rövid
     parafrázis vagy saját fordítás).
- **Tippelj!** 4. lépés: „Ha egy közösség évtizedenként 40 %-kal nő, és Kr. u. 40-ben 1000 tagja van, nagyjából hány
  tagja lesz 300-ban? kb. 15 ezer / kb. 600 ezer / kb. 6 millió” (→ 1000 · 1,4²⁶ ≈ 6,3 millió – a számolás a `.md`-ben).
- **Lépések:**
  1. Sok isten – Mezopotámia, Egyiptom, Görögország, Róma: istenek feladatkörrel (Zeusz, Pallasz Athéné; Kheopsz mint
     isteni király) – kártyasor, nincs „babona” címke.
  2. Egy Isten – a zsidó monoteizmus: Ábrahám, Mózes, Tízparancsolat (*hagyomány* réteg), a Héber Biblia mint
     *forrás* és mint szent irat; Jeruzsálem, a templom.
  3. 70 és utána – a templom lerombolása, a diaszpóra; a zsinagóga és az írás köré szerveződő közösség. Kis térkép
     (TortMap, `map-mediterran`): néhány dokumentált diaszpóra-közösség pontként (Alexandria, Róma, Antiokheia,
     Babilónia) – nem terjedési animáció.
  4. Jézus tanítása és a páli fordulat – a Messiás-várakozás, Jézus tanításai (szeretetparancs – evangéliumi
     *hagyomány*), Pál: a nem zsidók befogadása; keresztség és úrvacsora; Tippelj!
  5. Növekedés modellel – a kulcsvizuál, csúszka.
  6. Üldözés és türelem – idővonal (64 Néró, 250 Decius, 303 Diocletianus, 311 Galerius, 313 Milánó); a jogi státusz a
     görbe hátterében.
  7. Birodalmi egyház – püspök, zsinat; 325 Nicaea: a Szentháromság-tan egy mondatban, leíró keretben; 380
     Thesszalonikéi rendelet. Honnan tudjuk? – Eusebius egyháztörténete (4. sz. eleje): résztvevő, keresztény püspök –
     mit lát, mit nem.
  8. Összehasonlítás – TortCards zsidó / keresztény / mindkettő; kitekintés: a 04-ben jön a harmadik monoteista vallás,
     az iszlám.
  9. Összefoglalás – Kr. e. / Kr. u. időszámítás egy mondatban (Dionysius Exiguus, 525; utalás `tortenelem-5-6/01-idoszamitas`).
- **Adatok:**
  - Stark-modell (R. Stark: *The Rise of Christianity*, 1996): 40: 1 000; 100: 7 530; 150: 40 496; 200: 217 795;
    250: 1 171 356; 300: 6 299 832; 350: 33 882 008 – évtizedenként kb. 40 % *(modell, vitatott; ellenőrizendő a kötet
    táblázatából)*. A birodalom lakossága kb. 60 millió *(becslés)*; keresztények aránya 300 körül kb. 10 %
    *(becslés, vitatott)*.
  - Néró: 64; Decius: 250; Diocletianus: 303; Galerius türelmi rendelete: 311; milánói megállapodás: 313; Nicaea: 325;
    Theodosius rendelete (*Cunctos populos*): 380. február 27. *(ellenőrizendő)*; Jeruzsálem: 70; Bar Kohba-felkelés:
    132–135.
  - Dionysius Exiguus húsvéttáblái: 525 *(ellenőrizendő)*.
  - Bibliai idézet: közkincs magyar fordítás – Károli Gáspár (1590, revideált szöveg is közkincs, ha 1955 előtti
    revízió) *(ellenőrizendő, melyik revízió)*; vagy parafrázis.
- **Modulok:** FoldChart (`log`, `vspan`, `line`, `dot`), TortCards, TortMap (`map-mediterran`), TortTimeline
  (`cards`), TortSource, TtTipp.
- **Review-pontok (vallástörténész):** leíró keret minden hittételnél („a keresztény tanítás szerint”); a zsidóság
  bemutatása ne „a kereszténység előzménye” legyen csak, hanem önálló, élő vallás; a Stark-modell vitatottsága; a
  „keresztényüldözés” mértéke (helyi és birodalmi hullámok).

### 04 · `04-hodito-birodalmak` – Mekkora volt egy birodalom, és meddig tartott? – Róma bukása, hunok, arab hódítás

- **Tanulási cél:** A Nyugatrómai Birodalom **belső** (gazdasági, katonai, politikai) és **külső** (népvándorlás)
  okok együttes hatására bomlott fel (476); a keleti fele **Bizánc**ként még ezer évig élt. A **hunok** sztyeppei
  birodalma (Attila) gyorsan nőtt és gyorsan szétesett – a **nomád államszervezés** személyes hűségen és zsákmányon
  alapult. Az **iszlám** (Mohamed, 622 hidzsra, Korán) összekovácsolta az arab törzseket; az **Arab Birodalom** száz év
  alatt az Industól az Ibériai-félszigetig terjedt, és Poitiers (732) és Konstantinápoly (717–718) állította meg. Róma
  örökösei: Bizánc, a Frank Birodalom (Nagy Károly, 800), a Német-római Császárság (I. Ottó, 962).
- **Kerettanterv:** „A nomád életmód, harcmodor és államszervezés.” · „A népvándorlás.” · „A Hun Birodalom.” · „Az ókor
  vége Nyugaton: a Római Birodalom összeomlása.” · „Róma örökösei Európa térképén.” · „Mohamed tanításai és a Korán.” ·
  „Az Arab Birodalom és az arab hódítás.” · „Az arab hódítás feltartóztatása Európában: Poitiers, Bizánc.” · Fogalmak:
  „népvándorlás, hunok, ortodox, iszlám, Korán, kalifa.” · Személyek: „Attila, Justinianus, Mohamed, Nagy Károly, I.
  Ottó.” · Kronológia: „476 a Nyugatrómai Birodalom bukása, 622 Mohamed Medinába költözése, 732 a poitiers-i csata.” ·
  Topográfia: „Hun Birodalom, Konstantinápoly, Bizánci Birodalom, Mekka, Poitiers, Frank Birodalom, Német-római
  Császárság.” · fejlesztés: „A népvándorlás irányainak és résztvevőinek nyomon követése térkép segítségével a Kr. u.
  4–8. sz. időszakában.”, „A sztyeppei állam működésének, sajátosságainak bemutatása.”, „Az iszlám vallás és az arab
  terjeszkedés közötti összefüggések feltárása.” · tevékenység: „A Római Birodalom bukása külső és belső okainak
  összegyűjtése.”
- **Tévhitek:** „Róma egy nap alatt, 476-ban bukott el.” „A Római Birodalom teljesen megszűnt 476-ban.” (Bizánc 1453-ig.)
  „A hunok birodalma olyan volt, mint Rómáé, csak kisebb.” (Más szervezet: adó helyett sarc, hivatalnokság helyett
  kíséret.) „Az iszlámot karddal terjesztették, mindenkit áttérítettek.” (A hódítás és az áttérés két külön folyamat; a
  meghódított keresztények és zsidók adó fejében gyakorolhatták vallásukat – *dhimmi* –, az áttérés évszázadokig
  tartott.) „A legnagyobb ókori birodalom Róma volt.”
- **Ne ismételd:** `tortenelem-5-6/04-pannonia` (Róma kiterjedése színfoltként, hunok Pannóniában), `08-vandorlas`.
- **Kulcsvizuál:** **birodalmak területe az időben** (FoldChart: x = Kr. e. 100 – Kr. u. 1000, y = millió km²,
  görbénként egy birodalom: Római, Hun, Bizánci, Omajjád/Abbászida kalifátus, Frank) – a csúcsok és a hirtelen
  zuhanások; a Taagepera-adatok „becslés” bélyeggel. Felette **térkép** (TortMap, `map-vilag` + `map-mediterran`,
  Lambert vagy Equal Earth): dátumcsúszka 395 → 814, a birodalmak **vázlatos**, leckén belül rajzolt, lágy szélű foltjai
  (`TortMap.region` `{poly}`) dátumozott kulcsállapotokból (395, 450, 476, 565, 650, 720, 814) áttűnve; a csúszka és a
  grafikon kurzora együtt mozog (FoldChart `cursor`). Népvándorlási nyilak (TortMap `line`, `head`) a 4–6. századra.
- **Kipróbálom:**
  1. A közös dátumcsúszka (térkép + grafikon). Kulcsállapotra kattintva kártya: ki uralkodik, mi a főváros, mekkora
     (az `### Adatok`-ból).
  2. TortCards: „Miért bukott el a Nyugatrómai Birodalom?” – 10 ok → belső / külső zóna (és „vitatott” csillag ahol a
     történészek vitatkoznak: pl. ólommérgezés – elvetett elmélet, csapdakártya).
  3. „Mennyi idő alatt?” mérő: két tű a grafikonon – hány év alatt nőtt az Arab Birodalom 1 millióról 10 millió km²
     fölé, és mennyi alatt Róma.
- **Tippelj!** 6. lépés: „Melyik volt a legnagyobb területű a négy közül 720 körül? Róma a csúcsán (117) / a Hun
  Birodalom (441) / az Omajjád kalifátus (720)” (→ kalifátus, kb. 11 millió km² *(becslés)*).
- **Lépések:**
  1. Két birodalom egy helyett – 395, a kettéosztás (kerettantervi kronológia: „Kr. u. 395 a Római Birodalom
     kettéosztása” – 1. témakör); Konstantinápoly.
  2. Népek mozgásban – nyilak 375–568 (hunok, gótok, vandálok, frankok, longobárdok); „vázlatos” bélyeg.
  3. Sztyeppei birodalom – a hunok: lovas-íjász hadviselés, kíséret, sarc; Attila (434–453), 451 Catalaunum; a gyors
     szétesés 453 után a grafikonon. Honnan tudjuk? – Priszkosz rétor (448/449-es követjárás, szemtanú, de bizánci
     szemmel; töredékekben maradt).
  4. 476 – mi történt valójában? (Odoaker leteszi Romulus Augustulust; a városi élet nem állt meg egy napra.) TortCards:
     belső és külső okok.
  5. Bizánc – Justinianus (527–565): hódítások, a Corpus iuris (kapcsolat a 02-vel), a csúcs 555 körül.
  6. Az iszlám és a kalifátus – Mekka, 622 hidzsra (Medina), a Korán, öt pillér (leíró keret); a terjeszkedés
     632–750; Tippelj!
  7. Megállított hódítás – Konstantinápoly 717–718, Poitiers 732 (*vitatott*: 732 vagy 733; a jelentőségének
     megítélése is vita).
  8. Róma örökösei – Frank Birodalom (Nagy Károly császár 800), 843 Verdun (egy mondat), Német-római Császárság (I.
     Ottó 962); ortodox és latin kereszténység felé (átvezetés a 05-höz: 1054).
  9. Összefoglalás – a grafikon egészben: melyik birodalom meddig tartott; a „mérő” eredménye.
- **Adatok:**
  - Területek (R. Taagepera 1979, *Social Science History* 3(3/4); 1997, *International Studies Quarterly* 41(3)), millió
    km²: Római Birodalom kb. 5,0 (117 körül); Hun Birodalom kb. 4,0 (441); Bizánc kb. 2,7 (555); Omajjád kalifátus kb.
    11,1 (720); Abbászida kb. 11,1 (750); Frank Birodalom kb. 1,2 (814) *(becslés; mind ellenőrizendő a
    táblázatokból)*. A görbék köztes pontjai is Taagepera táblázataiból, interpoláció nélkül (a hiányzó szakasz
    szaggatott).
  - 375 (hunok a Don–Dnyeszter vidékén, a gótok menekülése) *(ellenőrizendő)*; 410 Alarik Rómában; 434–453 Attila
    (453-ig Bledával 445-ig közösen) *(ellenőrizendő)*; 451 Catalaunum; 476; 527–565 Justinianus; 568 longobárdok
    Itáliába, avarok a Kárpát-medencében; 622; 632 Mohamed halála; 711 Ibéria; 717–718; 732; 750 Abbászidák; 800.
    december 25.; 843; 962. február 2.
  - Kulcsállapotok sokszögeinek töréspontjai: a kódban, helységnévvel; két egybevetett atlasz a `.md`-ben.
- **Modulok:** FoldChart (`line`, `cursor`, `vspan`), TortMap (`map-vilag`, `map-mediterran`; `region` poly, `line`,
  `labels`, `stamp`), TortCards, TortTimeline (`mini`), TortSource, TtTipp. Leckén belül: a kulcsállapot-sokszögek
  áttűnése (zárt képlet a dátumból).
- **Review-pontok:** a sokszögek (különösen a hun „birodalom” – laza befolyási övezet, nem határ: lágy szél, erős
  „vázlatos”); a Taagepera-számok becslés jellege; az iszlám leíró kerete; a „dhimmi” helyzet se idealizálva, se
  démonizálva (adó, korlátozások).

### 05 · `05-rendi-tarsadalom` – Mennyi maradt a jobbágynak? – rendek, terhek és válság a középkori Európában

- **Tanulási cél:** A középkor **hierarchikus világképe** szerint a társadalom három rendből áll: aki imádkozik
  (egyháziak), aki harcol (nemesek), aki dolgozik (parasztok). A **hűbériség** személyes kötelékek lánca (hűbérúr –
  hűbéres); a **rendi monarchia** az uralkodó hatalmát a rendek kiváltságaival korlátozta. A **jobbágy** földet kapott
  használatra, cserébe **terheket** viselt (tized az egyháznak, termény, pénz, munka – robot – a földesúrnak); alacsony
  terméshozamnál ez kevés tartalékot hagyott – ezért pusztítottak az éhínségek. A **nagy pestis** (1347–1351) a népesség
  harmadát–felét elvitte; utána a munkaerő drága lett, a terhek és a bérek átalakultak, felkelések törtek ki. A
  **városok** (céh, polgár, kiváltság, Hanza, levantei kereskedelem) az árutermelés felé vitték a gazdaságot.
- **Kerettanterv:** „A hierarchikus világkép.” · „Az uradalom.” · „A jobbágyok kötelességei és jogai.” · „Az
  önellátástól az árutermelésig.” · „Éhínségek, járványok, felkelések.” · „Az uralkodói hatalom és korlátai (hűbériség,
  rendiség).” · „A középkori város és lakói.” · „A céhek.” · „A helyi és távolsági kereskedelem.” · „Az egyházszakadás
  és a 11. századi reform.” · Fogalmak: „uradalom, földesúr, majorság, jobbágy, robot, kiváltság, rend, pápa, …,
  lovag, nemes, feudalizmus, hűbériség, király, rendi monarchia, keresztes hadjáratok, polgár, céh.” · Kronológia:
  „476–1492 a középkor, 1054 az egyházszakadás, 1347 a nagy pestisjárvány.” · Topográfia: „levantei kereskedelmi
  hálózat, Velence, Firenze, Hanza kereskedelmi hálózat, Szentföld.” · fejlesztés: „A társadalmi csoportok közötti jogi
  különbségek azonosítása.”, „A jobbágyság jogainak és kötelességeinek rendszerezése.”, „A középkor társadalmi
  berendezkedése és a rendi szemlélet értelmezése.”, „A városok életének bemutatása … kitérve a zsidóság
  városiasodásban játszott szerepére, valamint az antijudaista törekvésekre.”
- **Tévhitek:** „A jobbágy rabszolga volt.” (Jogai is voltak: család, ingóság, sok helyen költözés.) „A hűbéres
  hűbérese az én hűbéresem.” („A hűbéresem hűbérese nem az én hűbéresem” – a kontinensen.) „A középkorban mindenki
  ugyanúgy élt ezer évig.” „A pestis után minden rosszabb lett.” (A túlélők bére sok helyen nőtt.) „A középkori ember
  azt hitte, a Föld lapos.” (Csak utalás: `tortenelem-5-6/13-felfedezesek`.)
- **Ne ismételd:** `tortenelem-5-6/06-var-uradalom` (évszak-csúszka, két- és háromnyomás, zoomolható falujelenet),
  `07-kozepkori-varos` (inas–legény–mester karrierjáték). Itt **nincs** jelenet és karrierjáték: költségvetés,
  séma, népességgörbe, kereskedelmi hálózat.
- **Kulcsvizuál:** **a termés útja** (leckén belüli rajz + MatChart): egy jobbágytelek egy évi gabonatermése
  zsákokban; a zsákok szétválnak – vetőmag a jövő évre (1 : 3–1 : 4 hozamnál a termés negyede–harmada!), tized,
  földesúri termény, a pénzjáradékhoz eladott rész, robotnapok (naptársáv) – és ami a családnak marad, összevetve a
  család **éves gabonaszükségletével** (szaggatott vonal). „Modell” bélyeg; a részarányok forrásból vagy tartománnyal.
  Második kép: Nyugat-Európa becsült népessége 1000–1500 (FoldChart), a pestis zuhanással, mellette egy reálbér-görbe
  (Anglia) – a munkaerőhiány hatása.
- **Kipróbálom:**
  1. **Termés-kalkulátor:** csúszkák – hozamarány (1 : 2 … 1 : 6), rossz év (−30 % termés), a földesúri járadék formája
     (termény / pénz / munka) → marad-e elég a családnak? Rossz évben a vetőmagot is meg kell enni → a következő év is
     rosszabb (két év egymás után).
  2. **Hűbérlánc** (TortState): király → herceg/gróf → lovag → jobbágyfalu; kapcsoló „kontinens / Anglia (1086 után)”:
     kinek tartozik hűséggel a lovag? (Salisburyi eskü, 1086 – egy mondat.)
  3. TortCards: jogok és kötelességek – 10 kártya → jobbágy / nemes / polgár / egyházi (kiváltság-összevetés).
- **Tippelj!** 3. lépés: „1 : 3-as hozamnál a termés mekkora részét kell félretenni vetőmagnak? egytizedét / egyharmadát
  / felét” (→ a harmadát).
- **Lépések:**
  1. Akik imádkoznak, harcolnak, dolgoznak – a hármas rend (Adalbero laoni püspök, 1020-as évek – közkincs latin;
     saját fordítás); a „rend” fogalma: születés szerinti jogállás.
  2. Hűbérúr és hűbéres – TortState hűbérlánc, kapcsoló; rendi monarchia: Magna Charta 1215 egy mondatban (az
     uralkodó hatalmának korlátja).
  3. A jobbágy terhei – a kalkulátor első fele, Tippelj!; tized, járadék, robot – fogalomkártyák a zsákokon.
  4. Rossz év – kalkulátor második fele; éhínség 1315–1317 *(ellenőrizendő)*.
  5. Az egyház – pápa, érsek, püspök, plébános (egyszerű TortState-hierarchia vagy saját fa); 1054 egyházszakadás
     (keleti/nyugati), a 11. századi reform (VII. Gergely, invesztitúra) egy-egy mondatban; a kolostor mint gazdasági
     egység.
  6. 1347 – a pestis: a népességgörbe zuhanása (*becslés*, tartomány); terjedése a kereskedelmi utakon (TortMap,
     `map-europa`, dátumozott vázlatos hullámfrontok 1347 → 1351 – „vázlatos”); a zsidóellenes pogromok mint a bűnbakképzés
     példája (1348–1349, Strasbourg) – tényként, forrással, méltósággal.
  7. Bérek és felkelések – a reálbér-görbe; Jacquerie (1358), angol parasztfelkelés (1381) – idővonal-pontként.
  8. Az önellátástól az árutermelésig – a város: céh (minőség, ár, verseny korlátozása), kiváltságok; a távolsági
     kereskedelem két hálózata (TortMap `line`: levantei – Velence, Genova, Alexandria; Hanza – Lübeck, Brugge,
     Novgorod, London). Honnan tudjuk? – egy céhszabályzat vagy vámtarifa (közkincs; saját fordítás / parafrázis).
  9. Összefoglalás – a három rend és a polgár egy ábrán; ki miből él.
- **Adatok:**
  - Adalbero (Laon), *Carmen ad Rotbertum regem*, kb. 1027–1031 *(ellenőrizendő)* – közkincs latin, saját fordítás.
  - Hozamarány: Anglia 13. század kb. 1 : 3–1 : 4 (B. H. Slicher van Bath, *The Agrarian History of Western Europe*, 1963)
    *(ellenőrizendő)*; tized 1/10; a családi gabonaszükséglet *(modell; a `.md` megadja, milyen becslésből: pl. fejenként
    kb. 200–250 kg/év)*.
  - A jobbágyterhek részaránya *(modell; tartomány a szakirodalomból; a `.md` megjegyzés felsorolja)*.
  - Salisburyi eskü: 1086 *(ellenőrizendő)*; Magna Charta: 1215. június 15.; Canossa: 1077; egyházszakadás: 1054;
    nagy éhínség: 1315–1317; pestis Európában: 1347–1351, a halálozás a népesség kb. 30–50 %-a *(becslés, vitatott;
    egyes újabb becslések 60 %)*; Jacquerie: 1358; angol felkelés (Wat Tyler): 1381.
  - Nyugat-Európa népessége 1000–1500 (C. McEvedy – R. Jones: *Atlas of World Population History*, 1978) *(becslés;
    ellenőrizendő; ha nem érhető el megbízhatóan, csak két-három pont tartománnyal)*.
  - Angol reálbér 1300–1500 (Phelps Brown – Hopkins 1956 vagy G. Clark 2007) *(ellenőrizendő; az adatsor forrását és
    évét a `series` megjegyzése rögzíti)*.
  - Hanza és levantei városok koordinátái (coord, `box: [-25, 30, 60, 72]`).
- **Modulok:** MatChart (`bars` halmozva / `pie`), TortState (hűbérlánc, egyházi hierarchia), FoldChart (népesség,
  reálbér, `vspan` pestis), TortMap (`map-europa`; `line`, `region` blobs a pestishez, `labels`), TortCards, TortSource,
  TortTimeline, TtTipp. Leckén belül: a zsákok szétválása (zárt képlet a csúszkákból).
- **Review-pontok:** a kalkulátor számai modell – a tanár ellenőrizze a nagyságrendeket; „feudalizmus” fogalmának
  vitatottsága (a mai szakirodalom óvatos vele) egy mondatban; a pogromok megfogalmazása (antijudaizmus a kerettanterv
  szóhasználatával).

### 06 · `06-magyar-ostortenet` – Mit tud a nyelvész, a régész és a genetikus? – a magyar nép eredetének bizonyítékai

- **Tanulási cél:** A magyar nép eredetéről **négy forrástípus** beszél, és mindegyik mást tud: a **nyelvészet** a
  nyelv eredetét (uráli/finnugor, ugor ág; jövevényszavak rétegei – ótörök, iráni, szláv), a **régészet** a tárgyi
  kultúrát és a temetkezést (Volga–Urál-vidék, Etelköz, Kárpát-medence), az **archeogenetika** a népesség
  leszármazását (keveredett népesség), az **írott források** a korabeli külső szemlélőt (bizánci, arab, latin). A
  nyelv, a gének és a tárgyi kultúra **nem szükségképpen együtt vándorolnak**. A **mondák és krónikák** (Anonymus,
  Kézai) később keletkeztek, és a saját koruk igényeit is tükrözik (hun–magyar azonosság). A **kettős honfoglalás**
  elmélete nem igazolt kisebbségi nézet. A honfoglalás 895 körül kezdődött, és több lépésben ment végbe (Etelköz →
  Kárpát-medence, besenyő támadás, 900 Pannónia, 907 pozsonyi csata).
- **Kerettanterv:** „Az eredet kérdései, a nyelvészet, a régészet, a néprajz és a genetika eredményei.” · „A magyar
  törzsszövetség az Etelközben.” · „A honfoglalás okai és menete.” · „A kalandozások – a lovas-íjász harcmodor.” ·
  Fogalmak: „finnugor, törzs, fejedelem, kabarok, vérszerződés, honfoglalás, kettős honfoglalás elmélete, avarok,
  rovásírás, kalandozások, székelyek” · Személyek: „Álmos, Árpád” · Kronológia: „895 a honfoglalás, 907 a pozsonyi
  csata” · Topográfia: „Etelköz, Vereckei-hágó, Kárpát-medence” · fejlesztés: „A magyarság eredetére vonatkozó
  elméletek közötti különbségek megállapítása.”, „A mondák, a történeti hagyomány és a történettudomány eredményeinek
  megkülönböztetése.”, „A kalandozó hadjáratok céljainak azonosítása.” · (bevezető) „ismeri a magyar nép őstörténetére
  és a honfoglalásra vonatkozó tudományos elképzeléseket és tényeket, tisztában van legfőbb vitatott kérdéseivel, a
  különböző tudományterületek kutatásainak főbb eredményeivel”.
- **Tévhitek:** „A finnugor rokonság azt jelenti, hogy a finnek a vérrokonaink.” „A genetika eldöntötte, hogy nem
  vagyunk finnugorok.” (A genetika a népesség leszármazásáról szól, a nyelv eredetéről nem.) „A magyarok a hunok
  egyenes leszármazottai – ezt a krónikák bizonyítják.” (Középkori hagyomány; a krónikák 400–800 évvel később
  keletkeztek.) „A honfoglalás egyetlen év alatt, egy hágón át történt.” „A kalandozás csak rablás volt.” (Zsoldos
  szolgálat, szövetségi hadjárat, zsákmány és adó – a célok különböztek.)
- **Ne ismételd:** `tortenelem-5-6/08-vandorlas` (vándorlási útvonal animáció), `09-honfoglalas` (három átlátszó fólia:
  forrás / krónika / régészet, mini időszalag a források keletkezéséről). Itt **nincs** útvonal-animáció és fólia:
  **bizonyítékmátrix** és „melyik tudomány mire válaszol” logika.
- **Kulcsvizuál:** **bizonyítékmátrix** (leckén belüli rajz): sorok = állítások („a magyar nyelv uráli eredetű”, „a
  honfoglalók egy része a Volga–Urál-vidékről jött”, „a honfoglalók keveredett népesség voltak”, „a magyarok a hunok
  utódai”, „a magyarok egy része már 670 körül beköltözött (kettős honfoglalás)”, „a honfoglalás 895 körül kezdődött”);
  oszlopok = nyelvészet / régészet / genetika / írott forrás / monda. Cellák: támogatja (teli kör), nem szól róla
  (üres), ellentmond (áthúzott kör), részben (félkör). A sor végén a **státusz-bélyeg**: „konszenzus” (tinta),
  „vitatott” (okker), „nem igazolt” (halvány tinta), „hagyomány” (okker kartus). Kattintásra a cella mögötti bizonyíték
  kártyán (TortSource `card`: ki, mikor, mit talált, hány évvel az esemény után). Mellette Eurázsia-térkép (TortMap,
  `map-vilag` + `map-europa`): a lelőhelyek pontként (Uelgi, Bolsije Tigani, Szubbotci, Kárpát-medencei temetők), a
  Magna Hungaria (Julianus) helye, Etelköz; a nyelvrokonok mai beszélőterülete halvány, „vázlatos” folttal (`region`
  blobs).
- **Kipróbálom:**
  1. A mátrix: a diák **először maga tippel** egy sor celláira (TtTipp-szerű választás cellánként: támogatja / nem
     szól róla / ellentmond), aztán „megmutat” – a lecke összeveti.
  2. **Szórétegek:** 12 szó (pl. *kéz, víz, hal, három* / *búza, alma, ökör, kecske* / *tehén, tej, asszony* /
     *asztal, király, szombat*) → TortCards zónák: uráli alapszókincs / ótörök / iráni / szláv jövevényszó. A tanulság:
     a jövevényszó az együttélés nyoma, nem a nyelv eredetéé.
  3. **„Hány évvel később?”** – a forráskártyákon a TortSource `line` mini-szalagja: Bíborbanszületett Konstantin
     (kb. 950, kb. 55 évvel 895 után), Anonymus (kb. 1200, kb. 300 év), Kézai (1282–1285, kb. 390 év), Julianus
     beszámolója (1236–1237, kortárs a keleti magyarokról).
- **Tippelj!** 2. lépés: „Melyik tudomány tudja megmondani, milyen nyelven beszéltek a honfoglalók? a genetika / a
  nyelvészet (és az írott források) / a régészet” (→ nyelvészet + írott forrás; a csont és a gén nem beszél).
- **Lépések:**
  1. Négy tanú – a négy forrástípus, mire jó és mire nem (kártyák); a „Honnan tudjuk?” itt maga a lecke.
  2. A nyelv – uráli családfa (saját ábra: uráli → finnugor → ugor → magyar, manysi, hanti; a szétválások „kb.”
     dátummal, „becslés”); Tippelj!
  3. Szórétegek – TortCards; ótörök hatás (Kazár Kaganátus, Etelköz), iráni (alán), szláv (Kárpát-medence).
  4. A régész – Volga–Urál-vidék, Etelköz, Kárpát-medence: temetkezési szokások (lókoponya, lábcsont, tarsolylemez,
     íj, szablya); a térkép pontjai, „rekonstrukció” réteg.
  5. A genetikus – archeogenetikai eredmények óvatosan: a honfoglalók egy része ugor (manysi-szerű) és szarmata/szkíta
     sztyeppei összetevőt hordozott, az elit egyes egyéneinek belső-ázsiai kapcsolatai is vannak; a honfoglalók
     kisebbséget alkottak a Kárpát-medence népességében; a mai magyarok génállománya nagyrészt közép-európai. A
     „vitatott” bélyeg az értelmezéseken; **értelmező doboz**: miért nem dönt a genetika a nyelvről.
  6. Az írott forrás és a monda – Bíborbanszületett Konstantin (Levedia, Etelköz, hét törzs + kabarok, Árpád
     megválasztása) – *forrás*; Anonymus (vérszerződés, Álmos) és Kézai (hun–magyar) – *hagyomány/monda*, a
     keletkezés korával és céljával; a székelyek eredetének kérdése (*vitatott*).
  7. A mátrix – kulcsvizuál, a diák tippel, a lecke megmutat; konszenzus / vitatott / nem igazolt.
  8. A honfoglalás menete és a kalandozások – 895 körül (besenyő–bolgár háború), 900 Pannónia, 907 Pozsony; a
     kalandozások céljai (TortCards: zsoldos szolgálat / zsákmány / adó / szövetség) és 955 Augsburg egy mondatban.
  9. Összefoglalás – „Mit tudunk biztosan, mit valószínűsítünk, miről vitatkozunk?” három oszlop.
- **Adatok:**
  - Uráli → finnugor → ugor szétválás: a nyelvészek becslései tág tartományban (pl. ugor egység felbomlása Kr. e. 1. ezredben)
    *(becslés, vitatott; ellenőrizendő – Bakró-Nagy M., Honti L., Zaicz G. (szerk.) *Etimológiai szótár*, 2006; MTA
    Nyelvtudományi Intézet kiadványai)*.
  - Jövevényszavak rétegei – minden példaszónál a szótári forrás (Zaicz 2006 / TESz) *(ellenőrizendő szavanként)*.
  - Lelőhelyek (coord): Uelgi (Cseljabinszki terület), Bolsije Tigani (Tatárföld), Szubbotci (Ukrajna, Kirovohradi
    terület) *(koordináták ellenőrizendők)*; Julianus útja 1235–1236, beszámoló: Riccardus 1237 (közkincs latin).
  - Archeogenetika: Neparáczki E. és mtsai (2019, *Scientific Reports*); Maróti Z. és mtsai (2022, *Current Biology*,
    „The genetic origin of Huns, Avars, and conquering Hungarians”); Szeifert B. és mtsai (2022, *Communications
    Biology*) *(az eredmények megfogalmazása a cikkek összefoglalójából, ellenőrizendő; a lecke a cikkek saját óvatos
    szóhasználatát követi)*.
  - Bíborbanszületett Konstantin: *De administrando imperio*, kb. 948–952 *(ellenőrizendő)*, † 959 – közkincs görög;
    Moravcsik Gyula fordítása († 1972) **nem** közkincs → saját fordítás vagy parafrázis.
  - Anonymus: *Gesta Hungarorum*, kb. 1200 *(vitatott: 1196–1210 körüli datálás)*; Kézai Simon: *Gesta Hunnorum et
    Hungarorum*, 1282–1285 *(ellenőrizendő)* – latin közkincs; Pais Dezső († 1973) és Bollók János (élő/friss)
    fordításai nem közkincsek → saját fordítás/parafrázis.
  - Kettős honfoglalás: László Gyula, 1970-es évek (*A „kettős honfoglalás”*, 1978) *(ellenőrizendő)* – kisebbségi,
    nem igazolt nézet.
  - Honfoglalás: 895 körül (894–900 közötti szakaszok) *(vitatott)*; 900 Pannónia; 907. július 4–6. Pozsony
    *(ellenőrizendő)*; 955. augusztus 10. Augsburg.
- **Modulok:** TortMap (`map-vilag` + `map-europa`; pontok, `region` blobs, `labels`), TortSource (`card` + `line`),
  TortTimeline, TortCards (szórétegek, kalandozási célok), TtTipp (`stamp` „vitatott”, választás). Leckén belül: a
  bizonyítékmátrix (cellánkénti tipp, státusz-bélyeg), az uráli családfa (egyszerű fa saját kóddal).
- **Review-pontok (történész, nyelvész, régész):** a mátrix minden cellája – a lektorok egyenként hagyják jóvá; a
  genetikai eredmények megfogalmazása (ne legyen sem lekicsinylő, sem túlzó); a „hun” szó két jelentése (krónikás
  hagyomány ↔ genetikai kapcsolat egyes ázsiai hun-kori egyénekkel); a székely eredet kérdése; az áltudományos nézetek
  kezelése (0. döntés, 8.). `"interpretive": true`.

### 07 · `07-arpad-kori-allam` – Kié volt a föld? – az Árpád-kori állam a királyi birtoktól az Aranybulláig

- **Tanulási cél:** Géza és I. (Szent) István államszervezése a **királyi birtokra** és a **vármegyére** épült (ispán,
  várnép), mellette az **egyházszervezet** (érsekségek, püspökségek, tized). A 11–12. században a törvények (Szent
  László, Könyves Kálmán) a rendet és a tulajdont védték. III. Béla jövedelme európai mércével is nagy volt – ezt egy
  **forrás**ból tudjuk, amelyet forráskritikával kell olvasni. II. András **birtokadományai** („új berendezkedés”)
  megváltoztatták a társadalmat; az **Aranybulla** (1222) a királyi szerviensek (a későbbi köznemesség) jogait
  rögzítette. A tatárjárás után IV. Béla a várépítéshez magánkézbe is adott földet. Az Árpádok házasságokkal kötődtek
  Európához.
- **Kerettanterv:** „Géza és I. (Szent) István államszervező tevékenysége.” · „A földbirtokrendszer és a
  vármegyeszervezet.” · „Az egyházszervezés.” · „Szent László, az országépítő.” · „Könyves Kálmán törvénykezési
  reformjai.” · „A kül- és belpolitika új irányai: III. Béla uralkodása.” · „II. András kora: az átalakuló társadalom.” ·
  „Újjáépítés a tatárjárás után: IV. Béla.” · „Az Árpádok európai kapcsolatai.” · Fogalmak: „vármegye, egyházmegye,
  érsekség, tized, nádor, ispán, kancellária, kettős kereszt, szászok, kunok, tatárok/mongolok” · Személyek: „Géza, I.
  (Szent) István, Koppány, Szent László, Könyves Kálmán, III. Béla, II. András, IV. Béla” · Kronológia: „997/1000–1038
  I. (Szent) István uralkodása, 1222 az Aranybulla, 1241–1242 a tatárjárás” · Topográfia: „Pannonhalma, Esztergom,
  Székesfehérvár, Buda, Muhi, Erdély, Horvátország” · tevékenység: „Folyamatábra készítése II. András politikai
  döntéseinek okairól és következményeiről.”, „A 13. századi társadalmi rétegek azonosítása az Aranybulla szövegében.”,
  „Az Árpádok európai dinasztikus kapcsolatainak ábrázolása térképen.”
- **Tévhitek:** „Az Aranybulla a jobbágyok szabadságlevele volt.” (A királyi szerviensek kiváltságai.) „Szent István
  idején már nemesség és jobbágyság volt, mint később.” „II. András csak pazarolt.” (Adományai mögött politikai cél is
  volt – vitatott megítélés.) „A középkori magyar király mindig szegény volt.” „Az Árpád-ház elszigetelt volt Európában.”
- **Ne ismételd:** `tortenelem-5-6/10-allamalapitas` (rétegenként épülő állam: püspökségek, ispáni várak, dénárok,
  családfa), `11-tatarjaras` (harapófogó, kővárak). Itt **birtokszerkezet, jövedelem, jogszöveg, dinasztikus háló**.
- **Kulcsvizuál:** **a föld és a jövedelem szerkezete** dátumcsúszkával (MatChart kör vagy halmozott sáv): királyi
  birtok / egyházi / világi magánbirtok aránya 1038 → 1200 → 1270 körül – **„becslés, vitatott”** bélyeggel, a
  tartomány halvány sávként; ha a szakirodalom csak szöveges becslést ad, a lecke **három állapotot** mutat számok
  helyett („túlnyomó / jelentős / kisebbségbe kerül”) és ezt kimondja. Mellette **III. Béla jövedelemjegyzéke**
  (MatChart oszlop: tételek márkában) forráskártyával. A lecke végén **dinasztikus térkép** (TortMap, `map-europa`):
  vonalak Esztergom/Székesfehérvár-tól a házastársak hazájáig (Bizánc, Kijev, Franciaország, Aragónia, Csehország,
  Lengyelország, Bajorország …), évszámmal.
- **Kipróbálom:**
  1. A birtokszerkezet dátumcsúszkája; a döntések (adományok, Aranybulla, várépítési adományok) pontként az idővonalon.
  2. **Aranybulla-olvasó** (TortCards): 10 cikkely rövid parafrázisa → kinek kedvez / kit korlátoz: királyi
     szerviensek / egyház / várjobbágyok / idegenek (vendégek) / izmaeliták és zsidók (tisztségviselés tilalma) /
     király. A végén a 31. cikkely (ellenállási záradék) kiemelve.
  3. „Hihető-e?” – a jövedelemjegyzék tételeinek szorzása (pl. sóbevétel × …) és összevetése két másik uralkodó becsült
     jövedelmével *(ha a szakirodalom ad ilyet; különben csak a forráskritikai kérdés)*.
- **Tippelj!** 5. lépés: „Kiknek a kiváltságait rögzítette az Aranybulla elsősorban? a jobbágyokét / a királyi
  szerviensekét (a későbbi köznemességét) / a városokét”.
- **Lépések:**
  1. Fejedelemből király – Géza, István, Koppány (997), koronázás (1000/1001 – *vitatott* dátum); a kettős kereszt
     (egy mondat, jelkép).
  2. Vármegye és egyházmegye – TortMap (`map-karpat`) pontjai: 2 érsekség és a püspökségek István korában
     (*vitatott* alapítási évek), néhány ispáni vár; TortTerr `mo1914hsz` keret „vázlatos – az 1914-es határral
     közelítve” felirattal (vagy keret nélkül, ha a lecke csak a Kárpát-medence tájat mutatja). Nádor, ispán,
     kancellária egy sémában (egyszerű saját ábra vagy TortState).
  3. Törvény és rend – Szent László és Könyves Kálmán törvényei: egy-egy rendelkezés (pl. lopás büntetése; „boszorkányok
     pedig, akik nincsenek…” – Kálmán, *vitatott* fordítás és értelmezés) – parafrázis.
  4. A gazdag király? – III. Béla jövedelemjegyzéke (a „párizsi lista”, 1180-as évek). Honnan tudjuk? – ki, kinek, miért
     írta (házassági tárgyalás a francia udvarral) → valószínűleg felfelé kerekített; „vitatott”.
  5. Új berendezkedés – II. András adományai, a csúszka; Aranybulla 1222, Tippelj!, TortCards-olvasó.
  6. A tatárjárás és ami utána jött – 1241–1242 (kitérő: `tortenelem-5-6/11-tatarjaras`), IV. Béla: kunok, várépítés,
     vendégek (szászok); a birtokszerkezet utolsó állapota.
  7. Az Árpádok Európában – dinasztikus térkép; III. Béla bizánci kapcsolatai; Szent Margit (egy mondat).
  8. Honnan tudjuk? – oklevelek, törvények, krónikák: melyik mit mond a földről.
  9. Összefoglalás – folyamatábra (a kerettanterv tevékenysége): II. András döntései → ok → következmény.
- **Adatok:**
  - Koppány: 997; István koronázása: 1000. december 25. vagy 1001. január 1. *(vitatott)*; István † 1038. augusztus 15.
  - Egyházmegyék István korában: Esztergom és Kalocsa érsekség + Veszprém, Győr, Pécs, Eger, Erdély, Csanád, Bihar, Vác
    *(ellenőrizendő; több alapítási év vitatott)*; a vármegyék száma István korában kb. 30–40 *(becslés, vitatott)*.
  - Birtokszerkezet: *(becslés, vitatott; ellenőrizendő – pl. Engel Pál: *Szent István birodalma*, 2001; Zsoldos Attila
    munkái)*; ha nincs megbízható szám, a lecke szöveges állapotot mutat (fent).
  - III. Béla jövedelemjegyzéke: összesen kb. 166 000 márka ezüst (a lista szerint) *(ellenőrizendő; a hitelesség és az
    értelmezés vitatott – Barta J.–Barta J. ifj., Kristó Gy., Weisz B.)*; a lista kora: 1185–1186 *(ellenőrizendő)*.
  - Aranybulla: 1222 (31 cikkely; megújítás 1231); latin közkincs. Az *Ezeréves magyar törvénytár* (1896–1900)
    fordítóinak halálozási évét ellenőrizni kell – ha ≤ 1955, idézhető; különben saját fordítás/parafrázis.
  - Dinasztikus kapcsolatok (évszám, házastárs, ország): legalább 8 tétel, mindegyik forrással *(ellenőrizendő)*.
  - Tatárjárás: 1241. április 11. Muhi; a népességveszteség *(vitatott: 15–50 %, régiónként eltérő)*.
- **Modulok:** MatChart (`pie` / halmozott `bars`, oszlop), TortMap (`map-karpat`, `map-europa`; `line`, `labels`),
  TortTerr (`outline` `mo1914hsz`, opcionális), TortCards, TortSource, TortTimeline, TtTipp.
- **Review-pontok:** a birtokszerkezet becslésének forrása (ha szám nincs, szöveges állapot!); a Kálmán-féle
  „boszorkány”-törvény fordítása; az egyházmegyék alapítási évei; a dinasztikus térkép tételei.

### 08 · `08-anjou-gazdasag` – Mitől lett erős az Anjou-kori király? – arany, kapuadó és a Szent Korona

- **Tanulási cél:** Az Árpád-ház kihalása (1301) után I. Károly a tartományurak legyőzésével és új jövedelmekkel
  állította helyre a királyi hatalmat. Az uralkodó **regálé**jogai (bányák, pénzverés, vám) adták a bevétel gerincét:
  a **bányavárosok** aranya és ezüstje (a 14. században Magyarország Európa legnagyobb aranytermelője), az
  **aranyforint** (1325 körül), a **kapuadó**, a **harmincad**. A **visegrádi királytalálkozó** (1335) a Bécset elkerülő
  kereskedelmi utat is célozta. Nagy Lajos **1351-es törvényei** (ősiség, kilenced, a nemesi jogok egysége) a nemesség
  helyzetét rögzítették; a **perszonálunió** Lengyelországgal (1370). A **Szent Korona** a hatalom legitimitásának
  jelképe lett – Károly háromszori koronázása ezt mutatja; a **Szent Korona-tan** később (Werbőczy, 1514) fogalmazódott
  meg.
- **Kerettanterv:** „A királyi hatalom újbóli megszilárdítása I. Károly idején.” · „A visegrádi királytalálkozó.” · „Az
  1351-es törvények.” · „Nagy Lajos hadjáratai.” · „A Szent Korona.” · Fogalmak: „aranyforint, regálé, kapuadó,
  kilenced, bandérium, perszonálunió, sarkalatos nemesi jogok, fő- és köznemes, szabad királyi város, bányaváros,
  mezőváros, Szent Korona, Szent Korona-tan” · Személyek: „I. (Anjou) Károly, I. (Nagy) Lajos” · Kronológia: „1301 az
  Árpád-ház kihalása,1308. I. Károly uralkodásának kezdete, 1335 a visegrádi királytalálkozó, 1351 I.(Nagy) Lajos
  törvényei” · Topográfia: „Visegrád, Lengyelország, Csehország, osztrák tartományok” · fejlesztés: „A 14–15. századi
  magyar uralkodók politikai pályájának felidézése.”
- **Tévhitek:** „Az aranyforint magyar találmány.” (A firenzei forint mintájára.) „A kapuadót minden ház fizette.” (A
  jobbágytelek „kapuja” után.) „A kilenced a király adója volt.” (A földesúré.) „Nagy Lajos alatt a három tenger
  mosta az ország partjait.” (Hagyomány és túlzás – a befolyási övezet nem uralom.) „A Szent Korona-tan Szent István
  korából való.”
- **Kulcsvizuál:** **a király kincstára** – a Kárpát-medence térképe (TortMap, `map-karpat`) a bányavárosokkal
  (Körmöcbánya, Selmecbánya, Besztercebánya, Nagybánya, Felsőbánya, Rozsnyó …; arany/ezüst jellel), a harmincadhelyekkel
  és a Buda–Brünn–Prága úttal (Visegrád 1335); a jövedelemfolyamok vonalakként Buda felé futnak, vastagságuk a
  becsült bevétel (*becslés*). Mellette a bevételek szerkezete (MatChart oszlop/halmozott sáv, *becslés*). TortTerr
  `mo1914hsz` keret („vázlatos”).
- **Kipróbálom:**
  1. **„Kamara haszna vagy kapuadó?”** modell (leckén belül, „modell” bélyeg): kapcsoló – évenkénti kötelező
     pénzbeváltás rontott pénzre (a kamara haszna) ↔ állandó értékű pénz + kapuadó. A vásznon egy kitalált falu 20
     jobbágytelke: ki mennyit veszít/fizet, és mi történik a pénz értékével, a kereskedelemmel; a király bevétele a
     két esetben.
  2. A térkép kapcsolói: bányák / vámok és harmincad / Visegrád útja.
  3. **Koronázás-kirakó:** Károly három koronázása (1301, 1309, 1310) – melyik feltétel teljesült (megfelelő korona,
     helyszín, koronázó főpap)? Három oszlopos táblában pipák.
- **Tippelj!** 7. lépés: „Miért kellett Károlyt háromszor megkoronázni? mert elveszett a korona / mert csak a Szent
  Koronával, Székesfehérváron, az esztergomi érsek által végzett koronázást tartották teljes értékűnek / mert a pápa
  így rendelte”.
- **Lépések:**
  1. 1301 – az Árpád-ház kihal: trónharc, tartományurak (Csák Máté, Aba Amadé – térképen vázlatos foltok, „vázlatos”).
  2. Rozgonyi csata 1312 – a tartományurak legyőzése egy mondatban; a hatalom gazdasági alapja a cél.
  3. Arany a hegyekből – bányavárosok, urbura (bányabér), az 1327-es bányareform (a földesúr részesedése a bányabérből)
     *(ellenőrizendő)*; aranyforint (firenzei minta, súly, finomság).
  4. Kamara haszna vagy kapuadó? – a modell, kapcsoló.
  5. Utak és vámok – harmincad, Visegrád 1335 (három király, a Bécset elkerülő út; az árumegállító jog).
  6. Nagy Lajos – 1351: ősiség, kilenced, „egy és ugyanazon szabadság”; hadjáratok (Nápoly, Balkán) és a lengyel
     trón 1370: **perszonálunió** (egy uralkodó, két ország – sémarajz). Bandérium egy mondatban.
  7. A korona – Szent Korona (tárgy: a részek datálása *vitatott*), Károly három koronázása, Tippelj!, kirakó.
  8. Honnan tudjuk? – a Szent Korona-tan: Werbőczy, *Hármaskönyv* (1514, közkincs latin): a korona = király és
     nemesség közössége; *vitatott* a tan későbbi (19–20. századi) értelmezése – két nézőpont, értékítélet nélkül.
  9. Összefoglalás – a király kincstára egészben; átvezetés a 09-hez (a bevételt a török elleni védelem nyeli el).
- **Adatok:**
  - 1301. január 14. III. András halála *(ellenőrizendő)*; Károly koronázásai: 1301 (Esztergom), 1309. június 15/16.
    (Buda), 1310. augusztus 27. (Székesfehérvár, Szent Korona) *(ellenőrizendő)*; Rozgonyi csata: 1312. június 15.
    *(ellenőrizendő)*; Károly † 1342.
  - Aranyforint: 1325/1326 *(ellenőrizendő)*, kb. 3,5 g, 23¾–24 karát *(ellenőrizendő)*; firenzei fiorino d'oro: 1252.
  - Kapuadó: 1336-tól *(ellenőrizendő)*; összege telkenként *(ellenőrizendő)*; harmincad: az áru értékének 1/30-a
    (később 1/20) *(ellenőrizendő)*; urbura: a kitermelt nemesfém kb. 1/10-e *(ellenőrizendő)*.
  - Aranytermelés a 14. században: évi kb. 1–2,5 tonna *(becslés, vitatott; ellenőrizendő – Weisz Boglárka, Draskóczy
    István munkái)*; „Európa termelésének nagy része” – csak tartománnyal, *(vitatott)*.
  - Bevételek szerkezete *(becslés; ha nincs megbízható szám, a térkép vonalvastagsága csak sorrendet mutat, és ezt a
    lecke kimondja)*.
  - Visegrád: 1335. november *(ellenőrizendő)* – I. Károly, III. Kázmér, Luxemburgi János.
  - 1351-es dekrétum (közkincs latin; fordítás: lásd 07); Lajos lengyel király: 1370. november 17. *(ellenőrizendő)*.
  - Werbőczy: *Tripartitum*, 1514 (nyomtatva 1517, Bécs) – latin közkincs; a régi magyar fordítások (pl. Kolosvári–Óvári,
    1897) fordítói halálozási évét ellenőrizni kell.
  - Bányavárosok koordinátái (coord, `box: [9, 42, 30, 51]`).
- **Modulok:** TortMap (`map-karpat`; `line` vastagsággal, `labels`, `stamp`), TortTerr (`outline` `mo1914hsz`),
  MatChart (oszlop, halmozott sáv), FoldChart (opcionális: a pénz értéke a modellben), TortSource, TortTimeline, TtTipp.
  Leckén belül: a kamara haszna ↔ kapuadó modell (kitalált falu), a koronázás-kirakó tábla.
- **Review-pontok:** a modell kitalált falujának számai („kitalált példa”); az aranytermelés becsléseinek forrása; a Szent
  Korona részeinek datálása; a Szent Korona-tan kiegyensúlyozott, értékítélet nélküli bemutatása.

### 09 · `09-hunyadiak-torok` – Mennyibe került megvédeni az országot? – Zsigmondtól Mátyásig a török árnyékában

- **Tanulási cél:** A 14. század második felétől az **Oszmán Birodalom** lépésről lépésre hódította meg a Balkánt, és
  az ország déli határához ért. **Luxemburgi Zsigmond** (nikápolyi vereség, 1396) után a déli **végvárrendszer**
  kiépítése kezdődött. **Hunyadi János** támadó hadjáratai (hosszú hadjárat 1443–1444, Várna 1444) és védelmi győzelme
  (Nándorfehérvár 1456) feltartóztatták a hódítást. **Hunyadi Mátyás** központosította a hatalmat, **rendkívüli
  hadiadó**val és **füstpénz**zel növelte a bevételeit, zsoldos **fekete sereget** tartott, kettős végvárláncot épített,
  és **aktív védelemmel**, közben nyugati birodalomépítő tervekkel politizált. A kérdés: elég volt-e az ország
  jövedelme egy nagyhatalommal szemben?
- **Kerettanterv:** „Az Oszmán Birodalom.” · „Török hódítás a Balkánon.” · „Luxemburgi Zsigmond, a közép-európai uralkodó
  és a török veszély.” · „Hunyadi János, a politikus és hadvezér.” · „Hunyadi János törökellenes harcai.” · „Mátyás útja
  a trónig.” · „A központosított királyi hatalom.” · „Jövedelmek és kiadások.” · „Birodalomépítő tervek.” · „Aktív
  védelem a török ellen.” · Fogalmak: „kormányzó, szekérvár, végvár, szultán, szpáhi, janicsár, rendkívüli hadiadó,
  füstpénz, fekete sereg, zsoldos, Corvina” · Személyek: „Luxemburgi Zsigmond, Hunyadi János, I. (Hunyadi) Mátyás” ·
  Kronológia: „1396 a nikápolyi csata, 1443–1444-es hosszú hadjárat, 1444 a várnai csata, 1453 Konstantinápoly eleste,
  1456 a nándorfehérvári diadal, 1458–90 Mátyás uralkodása” · Topográfia: „Nikápoly, Várna, Nándorfehérvár, Kolozsvár,
  Kenyérmező, Oszmán Birodalom” · fejlesztés: „A késő középkori magyar állam és az Oszmán Birodalom főbb
  összecsapásainak felidézése.”, „Annak értékelése, hogy az Oszmán Birodalom terjeszkedő politikája milyen hatást
  gyakorolt a magyar történelemre.”, „Mátyás hatalom-gyakorlásának jellemzése.”
- **Tévhitek:** „Mátyás bevétele nagyobb volt, mint a szultáné.” „A fekete sereg magyar nemesekből állt.” (Zsoldosok,
  sok nemzetiségű.) „Mátyás nyugati háborúi értelmetlen kalandok voltak.” (Vitatott megítélés: két nézőpont.) „A
  török egyetlen nagy csatában hódította meg a Balkánt.” „A janicsárok önkéntes török harcosok voltak.” (Gyűjtött
  keresztény fiúkból – devsirme.)
- **Ne ismételd:** `tortenelem-5-6/12-nandorfehervar` (vár és folyózár felülnézetben, ostromnapok csúszkája) –
  Nándorfehérvár itt csak egy pont az idővonalon és a térképen.
- **Kulcsvizuál:** két kép.
  (a) **Az oszmán terjeszkedés** dátumcsúszkával 1354 → 1480 (TortMap, `map-mediterran` + `map-karpat`): leckén belül
  rajzolt, vázlatos, lágy szélű foltok kulcsállapotokból (1354, 1389, 1396, 1430, 1459, 1463, 1480), az ország déli
  peremén a végvárlánc kiépülése (Zsigmond: Nándorfehérvár 1427 *(ellenőrizendő)*, Szendrő elvesztése 1459, Mátyás:
  Jajca 1463, Szabács 1476) – kettős vonal; csaták pontként (Nikápoly, Várna, Rigómező 1448, Nándorfehérvár, Kenyérmező
  1479). TortTerr `mo1914hsz` keret („vázlatos”).
  (b) **Mátyás költségvetése** (MatChart oszlopok, *becslés*): bevételek (rendes: urbura, harmincad, sóregálé,
  városok adója, kapuadó; rendkívüli hadiadó) ↔ kiadások (fekete sereg, végvárak, udvar, diplomácia); mellette az
  Oszmán Birodalom becsült bevétele azonos skálán.
- **Kipróbálom:**
  1. A terjeszkedés dátumcsúszkája; csatapontra kattintva kártya (ki, ki ellen, kimenetel, következmény) – csata nem
     játszódik le.
  2. **„Mennyi katonát tart el?”** kalkulátor (*modell*): a bevétel csúszkája (Mátyás becsült éves bevételének
     tartománya) → hány zsoldost tud egész évben fizetni egy becsült éves zsoldon, és mennyi marad a végvárakra és az
     udvarra. A tanulság: a hadiadó nélkül a fekete sereg nem fizethető.
  3. Kapcsoló a költségvetésen: „rendkívüli hadiadóval / nélküle”.
- **Tippelj!** 6. lépés: „Mátyás becsült éves bevétele hogyan aránylott a szultánéhoz? nagyobb volt / nagyjából azonos /
  kisebb – kb. a fele vagy kevesebb” *(a pontos arány ellenőrizendő; a lecke tartománnyal adja)*.
- **Lépések:**
  1. Egy új nagyhatalom – az Oszmán Birodalom: szultán, szpáhi (földet kap szolgálatért), janicsár (devsirme); a
     terjeszkedés első szakasza a csúszkán.
  2. Zsigmond – közép-európai uralkodó (római király 1411, császár 1433, cseh király; egy kis sémán); Nikápoly 1396; a
     déli határ megerősítése.
  3. Hunyadi János – a politikus (kormányzó 1446–1453) és a hadvezér (szekérvár, hosszú hadjárat, Várna); a térképen.
  4. 1453 és 1456 – Konstantinápoly eleste, Nándorfehérvár (utalás az 5–6-ra); a déli harangszó egy mondatban (pápai
     bulla, utólagos értelmezés – *hagyomány*).
  5. Mátyás útja a trónig – 1458. január 24. (a pesti Duna jegén, *hagyomány*), a korona visszaszerzése 1463
     (80 000 aranyforintért *(ellenőrizendő)*), koronázás 1464; a központosítás: titkos kancellária, királyi tanács,
     egyszerű séma.
  6. Bevétel és kiadás – a költségvetés, Tippelj!, kapcsoló.
  7. A fekete sereg ára – a kalkulátor; aktív védelem (kettős végvárlánc) a térképen.
  8. Nyugat vagy dél? – Csehország, Ausztria (Bécs 1485): két nézőpont (birodalomépítés a török elleni erőgyűjtéshez /
     erőforrások elvonása délről) – „vitatott”. Honnan tudjuk? – Bonfini (udvari történetíró, a király megbízásából)
     ↔ a kincstári számadások töredékei: kinek a számai nagyobbak, és miért?
  9. Összefoglalás – a csúszka 1490-en: mit hagyott hátra Mátyás (Corvina egy mondatban), és mi jön 1521–1526-ban
     (átvezetés a 12-höz).
- **Adatok:**
  - 1354 Gallipoli; 1389 Rigómező; 1396. szeptember 25. Nikápoly; 1443–1444 hosszú hadjárat; 1444. november 10. Várna;
    1448. október 17–19. Rigómező (második); 1453. május 29.; 1456. július 4–22.; 1459 Szendrő; 1463 Bosznia, Jajca
    (december); 1476 Szabács; 1479. október 13. Kenyérmező; 1485. június 1. Bécs *(dátumok ellenőrizendők)*.
  - Mátyás megválasztása: 1458. január 24.; koronázás: 1464. március 29. *(ellenőrizendő)*; † 1490. április 6.
  - Mátyás éves bevétele: átlagosan kb. 650 ezer, a legjobb években 800–900 ezer aranyforint *(becslés, vitatott;
    ellenőrizendő – Kubinyi András; a régebbi, Bonfinira épülő 1–2 milliós becslés túlzó)*; az oszmán bevétel a 15.
    század végén *(ellenőrizendő; forrással, tartománnyal)*.
  - Fekete sereg: állandó létszám kb. 8–10 ezer, hadjáratban 20–30 ezer *(becslés, vitatott)*; zsold havonta kb. 2–3
    forint/fő *(ellenőrizendő)*.
  - Rendkívüli hadiadó: kapunként 1 forint *(ellenőrizendő)*.
  - Kulcsállapot-sokszögek: töréspontok a kódban; két atlasz a `.md`-ben.
  - Bonfini: *Rerum Ungaricarum decades* (1490-es évek, † 1503 – közkincs latin); Kulcsár Péter fordítása nem közkincs.
- **Modulok:** TortMap (`map-mediterran`, `map-karpat`; `region` poly, `labels`, `line`), TortTerr (`outline`
  `mo1914hsz`), MatChart (oszlop), TortTimeline (`cards`), TortSource, TtTipp. Leckén belül: a terjeszkedés
  kulcsállapotai, a zsoldkalkulátor.
- **Review-pontok:** a költségvetési számok forrása és tartománya; a „nyugati politika” két nézőpontja; a sokszögek
  (Balkán 15. század – a vazallus és a közvetlen uralom különbsége: két árnyalat).

### 10 · `10-arforradalom` – Hová lett Amerika ezüstje? – felfedezések, árforradalom, korai kapitalizmus

- **Tanulási cél:** A portugál és spanyol **felfedezések** célja az ázsiai fűszer- és nemesfém-kereskedelem
  közvetítőinek megkerülése volt. Amerika meghódítása és **gyarmatosítása** népirtással felérő pusztulással járt
  (járványok, kényszermunka), és Európába rengeteg **ezüstöt** hozott. A pénz mennyiségének növekedése (és a népesség
  növekedése) **árforradalmat** okozott – másfél évszázad alatt többszörösére nőttek az árak. Kialakult a
  **világkereskedelem** (Atlanti-óceán, Manila-gálya), az új gazdasági formák (**manufaktúra**, **bank**, **tőzsde**,
  **részvény**: VOC, 1602), és az **európai munkamegosztás**: Nyugaton bérmunka és ipar, az Elbától keletre
  **örökös jobbágyság** és gabonaexport.
- **Kerettanterv:** „A portugál és spanyol felfedezések.” · „A korai gyarmatosítás és következményei.” · „A
  világkereskedelem kialakulása.” · „Az árforradalom.” · „A manufaktúrák.” · „Bankok és tőzsdék.” · „Az európai
  munkamegosztás és következményei” · Fogalmak: „gyarmat, világkereskedelem, abszolutizmus, infláció, manufaktúra, tőke,
  tőkés, bérmunkás, kapitalizmus, bank, tőzsde, részvény, örökös jobbágyság” · Személyek: „Kolumbusz Kristóf, Vasco da
  Gama, Ferdinánd Magellán” · Kronológia: „1492-től az újkor, 1492 Amerika felfedezése” · Topográfia: „Spanyolország,
  India, London” · fejlesztés: „A felfedezők céljainak és útjainak bemutatása tematikus térképeken.”, „Információk
  gyűjtése a kialakuló világkereskedelem új útvonalairól, fontosabb termékeiről és szereplőiről.”, „Az új
  munkaszervezési formák bemutatása és összehasonlítása a céhes iparral.”, „Az európai régiók közötti gazdasági és
  társadalmi különbségek felismerése.” · (7.) „Az abszolutizmus.”
- **Tévhitek:** „Amerika aranya gazdaggá tette Spanyolországot.” (Az ezüst továbbáramlott; a spanyol államcsőd
  ismétlődött.) „Az infláció modern jelenség.” „A felfedezők a Föld gömbölyűségét akarták bizonyítani.” (Utalás az
  5–6-ra.) „A manufaktúra = gyár gépekkel.” (Kézi munka, munkamegosztással egy helyen.) „Kelet-Európa azért maradt le,
  mert nem dolgoztak eleget.” (A munkamegosztás szerkezete.)
- **Ne ismételd:** `tortenelem-5-6/13-felfedezesek` (forgatható földgömb, Kolumbusz „kicsi Földje”, passzátszelek, a Föld
  kerülete csúszkán) – itt **nincs** földgömb és kerület-csúszka; Equal Earth síktérkép, ezüstáramlás és árindex.
- **Kulcsvizuál:** **ezüst és ár egy grafikonon** (FoldChart, két tengely `y2`): a Sevillába érkezett amerikai ezüst
  évtizedenként (oszlopok, kg; Hamilton 1934) és egy árindex (vonal; spanyol vagy angol, 1500 = 100). Felette
  **világtérkép** (TortMap, `map-vilag`, Equal Earth `lon0: 0`): az ezüst útja Potosí → Panama/Cartagena → Sevilla →
  Antwerpen/Genova → (Levante, India) és Acapulco → Manila → Kína, vonalvastagsággal *(becslés)*; a felfedező utak
  csak halványan, dátummal (Dias 1488, Kolumbusz 1492, da Gama 1498, Magellán–Elcano 1519–1522).
- **Kipróbálom:**
  1. **Mennyiségi modell** (*modell* bélyeg): csúszkák – pénzmennyiség, árumennyiség (népesség/termelés) → árszint
     (egyszerűsített P = M · V / Q, V állandó); a modell görbéje a valós árindex mellé kerül. Kérdés: elég-e a modell
     az árforradalom magyarázatára? (Népességnövekedés, pénzrontás – két másik ok.)
  2. A térkép rétegkapcsolói: felfedező utak / ezüstút / rabszolga-kereskedelem (szám forrással, méltósággal, nincs
     animált „szállítmány”) / fűszer.
  3. **Elba-vonal** kapcsoló: Európa két fele (TortMap `map-europa`, vázlatos vonal az Elbán és a Lajtán): mit termel,
     ki dolgozik, hová visz az út (gabona és marha keletről, posztó és fém nyugatról) – kártyákkal.
- **Tippelj!** 4. lépés: „Hányszorosára nőtt az árszint Spanyolországban 1500 és 1600 között? kb. 1,5× / kb. 3–4× /
  kb. 20×” *(az érték ellenőrizendő Hamilton indexéből; a lecke tartománnyal adja)*.
- **Lépések:**
  1. Miért indultak el? – fűszer, arany, közvetítők megkerülése, térítés; a portugál és spanyol utak (halvány vonalak,
     dátummal); Tordesillas 1494.
  2. A hódítás ára – az amerikai népesség pusztulása (*becslés, vitatott* tartomány, forrással; járványok szerepe,
     encomienda, kényszermunka a bányákban); méltósággal, számlálóanimáció nélkül. Honnan tudjuk? – Las Casas (1552,
     közkincs; spanyol szerzetes, aki vádirat céljával írt – forráskritika).
  3. Az ezüst útja – térkép, Potosí (1545), Manila-gálya (1565-től).
  4. Árforradalom – a kulcsgrafikon, Tippelj!
  5. A modell – csúszkák; mit nem magyaráz (népesség, pénzrontás).
  6. Új munkaszervezés – céh ↔ manufaktúra összevetés (TortCards: munkamegosztás, gép, tulajdonos, verseny, bér);
     bérmunkás, tőkés, tőke.
  7. Bank, tőzsde, részvény – Amszterdam, VOC (1602): a részvény mint kockázatmegosztás – egy kis kitalált példa
     (100 befektető, egy hajóút).
  8. Az európai munkamegosztás – Elba-vonal; örökös jobbágyság (Magyarország 1514 után: utalás 08/12); abszolutizmus
     egy mondatban (XIV. Lajos – a 13-hoz).
  9. Összefoglalás – a világ összekapcsolódott: egy ezüstérme útja Potosítól Kínáig.
- **Adatok:**
  - E. J. Hamilton: *American Treasure and the Price Revolution in Spain, 1501–1650* (1934): 1503–1660 között Sevillába
    16 886 815 kg ezüst és 181 333 kg arany érkezett (hivatalosan nyilvántartva) *(ellenőrizendő; a csempészet miatt
    alsó becslés)*; évtizedenkénti tábla a kötetből *(ellenőrizendő)*.
  - Árindex: Hamilton (Spanyolország) vagy Phelps Brown – Hopkins (Dél-Anglia, 1956) *(ellenőrizendő; a `series`
    megjegyzése rögzíti, melyik)*.
  - Dias: 1488; Kolumbusz: 1492. október 12.; Tordesillas: 1494. június 7.; da Gama Kalikut: 1498. május *(ellenőrizendő)*;
    Magellán–Elcano: 1519–1522; Potosí: 1545; Manila-gálya: 1565–1815 *(ellenőrizendő)*; VOC: 1602. március 20.
    *(ellenőrizendő)*; Las Casas: *Brevísima relación*, 1552.
  - Amerika őslakos népességének zuhanása: *(becslés, vitatott – tág tartomány, legalább két forrással, pl. N. D. Cook
    1998; a lecke kimondja a bizonytalanságot)*.
  - Atlanti rabszolga-kereskedelem: a Trans-Atlantic Slave Trade Database (slavevoyages.org) összesítője (1501–1866: kb.
    12,5 millió elhurcolt) *(ellenőrizendő; a 16–17. századi rész külön)*.
- **Modulok:** FoldChart (oszlop + vonal, `y2`, `axes`), TortMap (`map-vilag` Equal Earth, `map-europa`; `line`
  vastagsággal, `labels`, `stamp`), TortCards, TortSource, TortTimeline, TtTipp. Leckén belül: a mennyiségi modell.
- **Review-pontok:** a népességzuhanás és a rabszolga-kereskedelem számai – forrással, tartománnyal, méltósággal; a
  modell egyszerűsítése kimondva; az Elba-vonal mint vázlatos tendencia, nem éles határ.

### 11 · `11-reformacio` – Ki dönti el, mit hisz az alattvaló? – reformáció, katolikus megújulás, vallásbéke

- **Tanulási cél:** A **reformáció** (Luther 1517, Kálvin) a humanizmus és az egyházi reform igényéből nőtt ki, és az
  egyház tanításáról, szervezetéről és a világi hatalomhoz való viszonyáról is mást mondott. Kialakult az
  **evangélikus**, a **református**, az **anglikán**, Erdélyben az **unitárius** egyház; a katolikus egyház a **tridenti
  zsinat**on (1545–1563) megújult (**jezsuiták**, **barokk**). A vallás és a politika összefonódott: az augsburgi
  vallásbéke (1555) szerint a fejedelem döntött az alattvalók vallásáról; Erdélyben a **tordai határozat** (1568) a
  gyülekezetek prédikátorválasztását biztosította – a korabeli Európában ritka **vallási türelem**. A harmincéves
  háborút lezáró vesztfáliai béke (1648) új egyensúlyt hozott. Magyarországon a reformáció és a katolikus megújulás
  iskolákat, könyveket, anyanyelvű Bibliát adott (Károli 1590, Pázmány).
- **Kerettanterv:** „A reformáció előzményei (humanizmus és az egyházi reform igénye).” · „Luther és Kálvin fellépése.” ·
  „A protestáns egyházak megszerveződése és a protestantizmus elterjedése.” · „A reformáció eredményei Magyarországon” ·
  „Vallási konfliktusok Európában.” · „Etnikai sokszínűség és vallásbéke Erdélyben.” · „A magyar protestáns és katolikus
  iskolák.” · „A katolikus megújulás és a barokk Európában és Magyarországon.” · Fogalmak: „reformáció, protestáns,
  evangélikus, református, anglikán, unitárius, vallási türelem, ellenreformáció, katolikus megújulás, jezsuiták,
  barokk” · Személyek: „Luther Márton, Kálvin János, Károli Gáspár, Pázmány Péter, Apáczai Csere János,
  Habsburg-dinasztia, V. Károly, Loyolai (Szent) Ignác” · Kronológia: „1517 a reformáció kezdete, 1545 a tridenti zsinat
  megnyitása, 1568 a tordai határozat, 1648 a vesztfáliai békék.” · Topográfia: „Sárospatak” · fejlesztés: „A
  katolikus és a protestáns tanítások és egyházszervezet összehasonlítása.”, „A reformáció egyes irányzatai terjedésének
  nyomon követése térképen.”, „Vallás és politika összefonódásának felismerése.”, „Az erdélyi vallási türelem szerepének
  és jelentőségének felismerése.”
- **Tévhitek:** „A tordai határozat teljes vallásszabadságot adott mindenkinek.” (A bevett felekezeteknek; az ortodox
  románság tűrt, nem bevett; a későbbi szombatosokat üldözték.) „A »cuius regio, eius religio« szöveg az augsburgi
  békében áll.” (Későbbi jogtudósi összefoglalás.) „A reformáció egyetlen egyházat hozott létre.” „A katolikus megújulás
  csak erőszak volt.” (Iskolák, egyetem, irodalom is – Pázmány.) „Magyarország a 16. században végig katolikus maradt.”
- **Ne ismételd:** `tortenelem-5-6/14-konyvnyomtatas` (nyomdák kigyúlása 1450–1500, a Luther-iratok hulláma, másoló ↔
  prés verseny) – itt **nincs** terjedési hullám és nyomda-animáció.
- **Kulcsvizuál:** két kép.
  (a) **Három egyházszervezet** (TortState, három `layout`): katolikus (pápa → érsek → püspök → plébános; a hívek nem
  választanak), evangélikus (fejedelem/világi hatóság – szuperintendens – lelkész), református (gyülekezet → presbitérium
  → lelkész; zsinat; a hívek választanak) – a nyilak címkéi: „kinevez”, „választ”, „felügyel”. Kattintásra kártya:
  tanítás (üdvözülés, szentségek száma, Biblia szerepe, istentisztelet nyelve) – leíró keret.
  (b) **„Ki dönt a hitről?” térkép** (TortMap, `map-europa` + `map-karpat`): Európa 1600 körül vázlatos felekezeti
  foltokkal (`region` blobs, „vázlatos”, legalább két atlasz alapján), a Kárpát-medencében az Erdélyi Fejedelemség
  külön kiemelve.
- **Kipróbálom:**
  1. **„Cuius regio” ↔ Torda kapcsoló** (leckén belüli modell): egy kitalált tartomány 6 faluja különböző
     felekezetű lakókkal; a diák kiválasztja a fejedelem vallását. „Augsburg 1555” módban a fejedelem vallásától eltérő
     falvak lakói választhatnak: áttérés vagy kivándorlás (*ius emigrandi*); „Torda 1568” módban minden falu maga
     választ prédikátort. „Kitalált példa” bélyeg; a falvak lakói nem kapnak nevet, csak felekezeti jelet.
  2. A TortState-layoutok váltása és kattintható dobozok.
  3. Idővonal 1517 → 1648 (TortTimeline `cards`): 1517, 1521, 1530, 1534, 1541, 1545, 1555, 1568, 1572, 1590, 1598,
     1618, 1635, 1648.
- **Tippelj!** 5. lépés: „Mit engedett meg az 1555-ös augsburgi béke egy evangélikus fejedelem katolikus alattvalójának?
  semmit / hogy kivándoroljon / hogy szabadon gyakorolja a hitét” (→ kivándorolhatott).
- **Lépések:**
  1. Miért kellett reform? – humanizmus (Erasmus, a forrásokhoz vissza), búcsúcédula, egyházi visszaélések – leíró
     keret; *forrás* réteg: a 95 tétel egy tétele (közkincs, saját fordítás).
  2. Luther és Kálvin – két tanítás összevetése (kártyák), V. Károly és Worms (1521).
  3. Három egyház – TortState layoutok; az anglikán egy mondatban (1534).
  4. Térkép 1600 körül – a felekezeti foltok; „vázlatos”.
  5. Vallás és politika – „cuius regio” kapcsoló (Augsburg), Tippelj!; Szent Bertalan-éj (1572) és a nantes-i edictum
     (1598) idővonal-pontként.
  6. Erdély – a tordai határozat (1568): a kapcsoló Torda-módja; négy bevett vallás (katolikus, evangélikus, református,
     unitárius), az ortodox románság tűrt helyzete. Honnan tudjuk? – az országgyűlési határozat szövege (közkincs; magyar
     nyelvű eredeti!) – mit mond és mit nem.
  7. A katolikus megújulás – Trento (1545–1563), jezsuiták, Pázmány (Nagyszombati egyetem, 1635), barokk – a barokk
     templom mint üzenet (egy vázlatos saját homlokzatrajz, „illusztráció”).
  8. Iskolák és könyvek – Sárospatak, Debrecen, Nagyszombat; Károli Biblia (Vizsoly, 1590); Apáczai (Magyar
     encyclopaedia, 1653).
  9. Összefoglalás – 1648: Vesztfália; a vallási türelem mint kérdés (értelmező doboz: mai vallásszabadság ↔ korabeli
     türelem).
- **Adatok:**
  - 1517. október 31. (95 tétel – a kiszögezés *hagyomány*, a levél ténye *forrás*); 1521 Worms; 1530 Augsburgi
    hitvallás; 1534 Supremacy Act; 1541 Kálvin végleg Genfben *(ellenőrizendő)*; 1545. december 13. – 1563 Trento;
    1555. szeptember 25. Augsburg *(ellenőrizendő)*; 1568. január Torda *(ellenőrizendő)*; 1572. augusztus 23–24.
    Szent Bertalan-éj; 1590 Vizsoly; 1598 Nantes; 1618–1648; 1635 Nagyszombat; 1648. október 24. Vesztfália
    *(ellenőrizendő)*; Sárospataki iskola: 1531 *(ellenőrizendő)*.
  - „Cuius regio, eius religio”: Joachim Stephani, 1599/1612 körül *(ellenőrizendő)* – a formula későbbi.
  - A „négy bevett vallás” rögzítése: 1568–1595 közötti országgyűlési határozatok *(ellenőrizendő)*.
  - A tordai határozat szövege: magyar nyelvű eredeti (1568) – közkincs, betűhív vagy modernizált átírással (jelölve).
  - Felekezeti arányok Magyarországon 1600 körül *(becslés, vitatott; ha szám, tartománnyal és forrással)*.
- **Modulok:** TortState (három `layout`, `card`), TortMap (`map-europa`, `map-karpat`; `region` blobs, `labels`,
  `stamp`), TortCards (opcionális: Luther ↔ Kálvin ↔ katolikus tanítás), TortTimeline (`cards`), TortSource, TtTipp.
  Leckén belül: a „cuius regio ↔ Torda” falumodell.
- **Review-pontok (egyháztörténész):** a tanítások leíró összevetése minden felekezetnél azonos mélységben; a felekezeti
  térkép; az ortodoxok és az antitrinitáriusok helyzete Erdélyben; „ellenreformáció” ↔ „katolikus megújulás” – mindkét
  szó a kerettantervben, a lecke elmagyarázza a különbséget. `"interpretive": true`.

### 12 · `12-hodoltsag-merlege` – Mibe került másfél évszázad? – a három részre szakadt ország mérlege

- **Tanulási cél:** A mohácsi vereség (1526) és a **kettős királyválasztás** után az ország Buda elestével (1541) három
  részre szakadt: **királyi Magyarország** (Habsburg-uralkodó, Pozsony), **hódoltság**, **Erdélyi Fejedelemség**
  (Gyulafehérvár). A két magyar állam **államszervezete** különbözött. A **végvárrendszer** költségét a királyi
  Magyarország jövedelme nem fedezte – a Habsburg-tartományok és a Német-római Birodalom segélye kellett. A
  hódoltságban **kettős adóztatás** volt. A 17. század a rendi és abszolutista törekvések ütközése (Bocskai, Bethlen,
  Zrínyi, a vasvári béke) volt. A **török kiűzése** (1683–1699) után az ország népessége alig volt nagyobb, mint 1500
  körül – miközben Nyugat-Európáé nőtt: ez a hódoltság **hosszú távú ára**.
- **Kerettanterv:** „A mohácsi csata és közvetlen előzményei, a kettős királyválasztás.” · „Az ország három részre
  szakadása.” · „A várháborúk és az új végvárrendszer.” · „A Magyar Királyság a Habsburg Birodalomban: rendi és
  abszolutista törekvések, konfliktusok.” · „Az Erdélyi Fejedelemség viszonylagos önállósága és aranykora.” ·
  „Magyarország az európai munkamegosztásban.” · „Háborús békeévek: másfél évszázad hódoltság és az ország pusztulása.” ·
  „A török kiűzése.” · Fogalmak: „rendi országgyűlés, hajdúszabadság.” · Személyek: „I. Szulejmán, II. Lajos,
  (Szapolyai) János, I. Ferdinánd, Dobó István, Zrínyi Miklós (a szigetvári hős), Báthory István, Bocskai István,
  Bethlen Gábor, Zrínyi Miklós (a költő és hadvezér), I. Lipót, Savoyai Jenő.” · Kronológia: „1526 a mohácsi csata, 1541
  Buda eleste, 1552 Eger védelme, 1566 Szigetvár eleste, 1664 a vasvári béke, 1686 Buda visszafoglalása, 1699 karlócai
  béke.” · Topográfia: „Mohács, Kőszeg, Eger, Szigetvár, Habsburg Birodalom, Erdélyi Fejedelemség, Hódoltság, Magyar
  Királyság (királyi Magyarország), Pozsony, Gyulafehérvár, Bécs.” · fejlesztés: „A három részre szakadt ország
  gazdasági lehetőségeinek és szerepének értelmezése adatok, grafikonok, diagramok alapján.”, „A török hódoltság hosszú
  távú hatásainak azonosítása.” · tevékenység: „Államszervezeti ábrák készítése a Magyar Királyságról és az Erdélyi
  Fejedelemségről.”, „A török kiűzése állomásainak nyomon követése térképen.”, „A mohácsi csata eseményeinek
  megvitatása különböző interpretációk alapján.”
- **Tévhitek:** „1526-ban az ország egy nap alatt török kézre került.” (1541-ig önálló, a hódoltság 1541 után nőtt.)
  „A hódoltság területe 150 évig ugyanaz volt.” „Erdély független állam volt.” (Az Oszmán Birodalom adófizető
  vazallusa, viszonylagos önállósággal.) „A Habsburgok csak elnyomták az országot.” (A végvárak fizetése – és az
  abszolutista törekvések: két oldal.) „A népesség a török alatt felére csökkent.” (*Vitatott* – a teljes ország
  népessége stagnált, a hódoltság egyes vidékei elnéptelenedtek, a különbség régiónként nagy.)
- **Ne ismételd:** `tortenelem-5-6/15-mohacs` (a mohácsi csata taktikai térképe, 1526–1570 hódoltsági folt, kettős
  királyválasztás családfán), `16-eger` (ostrom), `17-mezovaros` (marhahajtás). Itt **államszervezet-összevetés,
  költségvetés, népesség, határ 1526 → 1699**.
- **Kulcsvizuál:** **a határ 173 éve** (TortMap, `map-karpat` + TortTerr `mo1914hsz` keret „vázlatos – a középkori
  királyság határa az 1914-es határral közelítve”): dátumcsúszka 1526 → 1699, a hódoltság és az Erdélyi Fejedelemség
  **leckén belül rajzolt** kulcsállapot-sokszögei (1541, 1552, 1566, 1606, 1664, 1683, 1686, 1699 – „vázlatos”,
  töréspontok helységnévvel), a fontos várak pontként (Buda, Eger, Szigetvár, Kanizsa, Érsekújvár, Temesvár, Várad,
  Kőszeg), a béke- és csataidőpontok idővonalon. Mellette **népesség-görbe** (FoldChart, index 1500 = 100): Magyarország
  ↔ Anglia ↔ Franciaország ↔ Csehország, 1500 → 1720 (*becslés*), a különbség kitöltve (`diff`).
- **Kipróbálom:**
  1. A dátumcsúszka (térkép + idővonal + népesség kurzor).
  2. **Két állam sémája** (TortState, két `layout`): királyi Magyarország (király – Bécs; Magyar Kancellária, Magyar
     Kamara, Udvari Haditanács (Bécs), nádor, országgyűlés két táblával, vármegyék) ↔ Erdélyi Fejedelemség (szultán
     ← adó; fejedelem, tanács, országgyűlés: három rendi nemzet + négy bevett vallás). Kattintásra kártya: ki választja,
     kitől függ, mi a különbség.
  3. **Végvár-költségvetés** (MatChart oszlop, *becslés*): a végvárrendszer évi költsége ↔ a magyar kamarai bevétel ↔ a
     birodalmi segély; kapcsoló „segély nélkül”.
  4. **Kettős adó** (kitalált hódoltsági falu, *modell*): a szultáni adók (dzsizje, tized a szpáhinak) + a magyar
     földesúrnak és a vármegyének titokban fizetett adó.
- **Tippelj!** 7. lépés: „Hogyan változott Magyarország becsült népessége 1500 és 1720 között, Angliáéhoz képest? mindkettő
  nőtt / Magyarországé nagyjából stagnált, Angliáé jelentősen nőtt / mindkettő csökkent” *(az adatok ellenőrizendők)*.
- **Lépések:**
  1. Mohács és két király – 1526 (az 5–6 utalással; a vereség okainak két-három interpretációja kártyán, „vitatott”),
     Szapolyai és Ferdinánd (1526).
  2. Három részre – 1541; a csúszka 1526 → 1570.
  3. Két magyar állam – TortState, két layout; hajdúszabadság (Bocskai 1605) egy mondatban.
  4. Mibe kerül egy végvár? – költségvetés, kapcsoló; Eger, Szigetvár pontként (utalás az 5–6-ra).
  5. Élet a hódoltságban – kettős adó modell; a mezővárosok (utalás `17-mezovaros`).
  6. Rendek és Habsburgok – Bocskai (1604–1606), Bethlen (1613–1629), Zrínyi és a vasvári béke (1664) – idővonal; két
     nézőpont: rendi alkotmányosság ↔ birodalmi központosítás, mindkettő indokaival.
  7. A kiűzés – 1683 Bécs, 1686 Buda, 1687 Nagyharsány, 1697 Zenta, 1699 Karlóca – a csúszka; Honnan tudjuk? – Schulhof
     Izsák budai zsidó krónikás beszámolója 1686-ról (kortárs, közkincs héber; saját fordítás/parafrázis) ↔ egy császári
     hadijelentés: ki mit lát.
  8. A mérleg – népesség-görbe, Tippelj!; a hódoltság hosszú távú hatásai (TortCards: népesség, településhálózat,
     etnikai összetétel → 14, gazdasági lemaradás, kultúra).
  9. Összefoglalás – a határ 1699-ben; átvezetés a 14-hez (újranépesülés).
- **Adatok:**
  - 1526. augusztus 29.; Szapolyai koronázása 1526. november 11.; Ferdinánd választása 1526. december 16–17. (Pozsony)
    *(ellenőrizendő)*; 1538 váradi béke; 1541. augusztus 29.; 1552; 1566. szeptember 7–8.; 1568 drinápolyi béke; 1570
    speyeri egyezmény; 1591/1593–1606 tizenöt éves háború; 1606 bécsi és zsitvatoroki béke; 1664. augusztus 1.
    Szentgotthárd, augusztus 10. Vasvár; 1683. szeptember 12. Kahlenberg; 1686. szeptember 2.; 1687. augusztus 12.
    Nagyharsány; 1697. szeptember 11. Zenta; 1699. január 26. Karlóca *(dátumok ellenőrizendők)*.
  - Népesség: Magyarország 1500 körül kb. 3,5–4 millió; 1720 körül kb. 4 millió *(becslés, vitatott; ellenőrizendő –
    Kovacsics J. (szerk.) *Magyarország történeti demográfiája*, 1963; Dávid Géza a hódoltsági defterekről)*; Anglia
    és Franciaország: E. A. Wrigley – R. S. Schofield, J. Dupâquier *(ellenőrizendő)*.
  - Végvárrendszer költsége a 16. század második felében: évi kb. 1–1,5 millió rajnai forint; a magyar bevételek ennek
    kb. harmadát–felét fedezték *(becslés; ellenőrizendő – Pálffy Géza munkái)*.
  - Sokszög-töréspontok: a kódban; két atlasz a `.md`-ben. Várak koordinátái (coord).
  - Schulhof Izsák: *Megillat Ofen* (1686 után, † 1733 – közkincs) *(ellenőrizendő)*; magyar fordítás (Kohn, ?) –
    fordító halálozási éve ellenőrizendő, különben saját fordítás/parafrázis.
- **Modulok:** TortMap (`map-karpat`; `region` poly, `labels`, `stamp`), TortTerr (`outline` `mo1914hsz`; `fill` poly
  hatch a vazallus Erdélyre), TortState (két `layout`, `card`), FoldChart (index-vonalak, `diff`, `cursor`), MatChart
  (oszlop), TortTimeline, TortSource, TtTipp. Leckén belül: kulcsállapot-sokszögek, kettős adó modell.
- **Review-pontok (történész):** a sokszögek (különösen a hódoltság északi pereme és a „hódoltsági peremvidék” –
  kettős adózás: harmadik árnyalat); a népesség-becslések; a mohácsi interpretációk; a Habsburg-szerep két oldala.

### 13 · `13-francia-forradalom` – Hogyan fordult a szabadság forradalma diktatúrába? – felvilágosodás és francia forradalom

- **Tanulási cél:** A **felvilágosodás** a tapasztalatra és az észre épített világképet (Kopernikusz, Newton), és új
  államelméleteket adott: **társadalmi szerződés**, **népfelség** (Rousseau), **hatalmi ágak megosztása**
  (Montesquieu), **szabad verseny** (Smith). A brit **alkotmányos monarchia** (Jognyilatkozat 1689) és az amerikai
  **elnöki köztársaság** (1776, 1787) ezek gyakorlati változatai. A **francia forradalom** (1789) kihirdette az **Emberi és
  polgári jogok nyilatkozatát**, és 1791-ben hatalommegosztásos alkotmányos monarchiát hozott létre – majd háború,
  belső válság és radikalizálódás közben a **jakobinus diktatúra** (1793–1794) a hatalmi ágakat egy kézbe vonta és
  terrort alkalmazott. Napóleon a forradalom polgári vívmányait (Code civil) **császári egyeduralommal** exportálta. A
  Szent Szövetség (1815) a régi rend helyreállítását célozta.
- **Kerettanterv:** „Tapasztalat és értelem − a felvilágosodás új világképe.” · „A felvilágosodás államelméletei.” · „A
  szabad verseny elmélete.” · „A parlamentáris rendszer: parlament és kormány.” · „Az elnöki rendszer: kongresszus és
  elnök.” · „A forradalom kitörése és az Emberi és polgári jogok nyilatkozata.” · „A jakobinus diktatúra.” · „Napóleon
  birodalma: a polgári berendezkedés exportja.” · Fogalmak: „felvilágosodás, jogegyenlőség, hatalmi ágak megosztása,
  népfelség, társadalmi szerződés, szabad verseny, alkotmány, alkotmányos monarchia, elnök, miniszterelnök, felelős
  kormány, cenzus, általános választójog, forradalom, diktatúra, jakobinus, Szent Szövetség.” · Személyek: „Nikolausz
  Kopernikusz, Isaac Newton, Charles Louis Montesquieu, Jean-Jacques Rousseau, Adam Smith, George Washington, Maximilien
  Robespierre, Bonaparte Napóleon.” · Kronológia: „1689 a Jognyilatkozat, 1776 a Függetlenségi nyilatkozat, 1789 a
  francia forradalom, 1804–1814/1815 Napóleon császársága, 1815 a waterlooi csata.” · fejlesztés: „A felvilágosodás
  államelméleteinek összehasonlítása különböző szempontok alapján.”, „A brit és az amerikai államszervezetet bemutató
  ábrák értelmezése.”, „Az Emberi és polgári jogok nyilatkozatában megjelenő felvilágosult elvek azonosítása.”, „A
  forradalmi gondolat és a legitimitás eszméjének értelmezése, azonosítása.” · tevékenység: „Vita rendezése a francia
  forradalom pozitív és negatív hatásairól.”
- **Tévhitek:** „A francia forradalom egyetlen nap volt: a Bastille ostroma.” „A forradalom kezdettől köztársaságot
  akart.” (1791: alkotmányos monarchia.) „1789-ben mindenki szavazhatott.” (Cenzus: aktív és passzív polgár.) „A
  jakobinusok a nyilatkozat elveit valósították meg.” (Felfüggesztették a hatalommegosztást.) „Napóleon visszahozta a
  régi rendet.” (Polgári jogrend + egyeduralom.)
- **Ne ismételd:** `tortenelem-7-8/16-demokracia` (UK, USA, Athén, HU intézménysémája TortState-tel; Montesquieu lépés) –
  itt az UK és az USA csak **egy** lépés kisebb, kétlayoutos összevetésként; a fő kép a **francia intézményrendszer
  időben**.
- **Kulcsvizuál:** **intézményséma dátumcsúszkával 1789 → 1804** (TortState `timeline`, `align: 'end'`): király,
  Nemzetgyűlés/Törvényhozó Nemzetgyűlés/Konvent, minisztérium, bíróságok, választók (cenzusos → általános férfi
  választójog 1792), sajtó, helyi önkormányzatok; 1791: hatalommegosztás (minden „ellenőriz” él él); 1792 augusztus –
  szeptember: a király felfüggesztése, köztársaság; 1793 április–szeptember: Közjóléti Bizottság (új csomópont) –
  forradalmi törvényszék, a gyanúsakról szóló törvény; a sajtó és a bíróság ellenőrző élei kialszanak, a csomópontok a
  bizottság „irányítása” alá kerülnek (`over`; felirat: „a Közjóléti Bizottság kezében”); 1794. július: thermidor;
  1795 Direktórium; 1799 konzulátus; 1804 császárság. A bordó „irányít” itt nem pártállam, hanem a forradalmi
  diktatúra (jelmagyarázat mondja ki).
- **Kipróbálom:**
  1. A dátumcsúszka; kattintásra intézménykártya (ki választja, kinek felel, mi lett vele).
  2. **„Kinek a gondolata?”** (TortCards): 8 állítás (parafrázis vagy saját fordítás közkincs szövegből – Locke, Montesquieu,
     Rousseau, Smith, Voltaire) → szerző-zónák; a megoldáskor a kulcsfogalom (társadalmi szerződés, hatalmi ágak,
     népfelség, szabad verseny) felirata kigyullad.
  3. **Nyilatkozat-kereső:** a nyilatkozat 4–5 cikkének saját fordítása; a diák megjelöli, melyik felvilágosult elvet
     mondja ki (jogegyenlőség, népfelség, hatalommegosztás, tulajdon) – pipa a TortState megfelelő élén.
- **Tippelj!** 3. lépés: „Kik szavazhattak az 1791-es alkotmány szerint? minden felnőtt / a bizonyos adót fizető
  férfiak (aktív polgárok) / csak a nemesek” (→ cenzusos választójog).
- **Lépések:**
  1. Ész és tapasztalat – a világkép változása (Kopernikusz → Newton) egy kis égi-mechanikai rajzzal; a középkori
     hierarchia (05) ↔ természettörvény.
  2. Államelméletek – TortCards „Kinek a gondolata?”; társadalmi szerződés, népfelség, hatalommegosztás, szabad verseny.
  3. Két gyakorlati minta – UK (alkotmányos monarchia, felelős kormány, 1689) és USA (elnöki köztársaság, 1787) –
     TortState két kis layout, egy lépésben (utalás a 7–8 `16-demokracia`-ra). Tippelj! az 1791-es választójogról.
  4. 1789 – rendi gyűlés → Nemzetgyűlés (június 17.), Bastille (július 14.), augusztus 4. (a kiváltságok eltörlése), a
     Nyilatkozat (augusztus 26.) – nyilatkozat-kereső.
  5. 1791 – alkotmányos monarchia: a séma minden ellenőrző éle él; cenzus.
  6. Háború és radikalizálódás – 1792 háború, köztársaság, 1793 a király kivégzése; a csúszka.
  7. A jakobinus diktatúra – Közjóléti Bizottság, a terror (a halálos ítéletek száma forrással és tartománnyal, **nincs
     számláló**); az ellenőrző élek kialszanak. Honnan tudjuk? – D. Greer 1935-ös statisztikája a forradalmi
     törvényszékek ítéleteiről: mit számolt meg, mit nem (a tárgyalás nélküli halálesetek).
  8. Thermidortól a császárságig – 1794, 1795, 1799, 1804; Code civil (1804): mi maradt meg a forradalomból
     (jogegyenlőség, tulajdon), mi nem (népfelség); Napóleon birodalma 1812-ben vázlatos térképen (TortMap,
     `map-europa`, leckén belül rajzolt foltok: Francia Császárság, függő államok, szövetségesek – „vázlatos”), Waterloo
     1815, Szent Szövetség.
  9. Összefoglalás – a csúszka három állapota egymás mellett (1791 / 1794 / 1804); értelmező kérdés a tanárnak: pozitív és
     negatív hatások (a kerettanterv vitája).
- **Adatok:**
  - 1689 Bill of Rights; Locke: *Két értekezés*, 1689/1690; Montesquieu: *A törvények szelleméről*, 1748 († 1755);
    Rousseau: *A társadalmi szerződés*, 1762 († 1778); Smith: *A nemzetek gazdagsága*, 1776 († 1790); 1776. július 4.;
    1787. szeptember 17. *(ellenőrizendő)* – mind közkincs, a régi magyar fordítások fordítóit ellenőrizni kell.
  - 1789. május 5.; június 17.; július 14.; augusztus 4.; augusztus 26.; 1791. szeptember 3. alkotmány; aktív polgárok
    kb. 4,3 millió *(ellenőrizendő)*; 1792. április 20. hadüzenet; augusztus 10.; szeptember 21–22. köztársaság; 1793.
    január 21.; április 6. Közjóléti Bizottság *(ellenőrizendő)*; 1793. szeptember 17. a gyanúsakról szóló törvény;
    1794. július 27. (thermidor 9.); 1795. október–november Direktórium; 1799. november 9. (brumaire 18.); 1804. március
    21. Code civil; 1804. december 2. koronázás; 1812; 1815. június 18. Waterloo; 1815. szeptember 26. Szent Szövetség
    *(dátumok ellenőrizendők)*.
  - Halálos ítéletek: kb. 16 600 (Greer 1935: 16 594 *(ellenőrizendő)*); a tárgyalás nélküli kivégzésekkel és a
    börtönhalálokkal együtt kb. 35–40 ezer *(becslés, vitatott)*; a vendée-i háború áldozatai *(vitatott, külön
    tartomány, ha szerepel)*.
  - A Nyilatkozat (1789) – hivatalos szöveg, közkincs; magyar szöveg: saját fordítás.
  - Napóleoni Európa 1812 sokszögei: a kódban; két atlasz a `.md`-ben.
- **Modulok:** TortState (`timeline` `align: 'end'`, `over`, `layout`, `card`, `hlEdge`), TortCards, TortMap
  (`map-europa`; `region` poly), TortTimeline (`cards`), TortSource, TtTipp.
- **Review-pontok (történész):** a terror számai és megfogalmazása (méltóság, tartomány); a jakobinusok és Robespierre
  bemutatása értékítélet nélkül, a kortárs indokokkal (háború, belső felkelés); a 7–8 `16-demokracia` ábrájától eltérő,
  de nem ellentmondó UK/USA-séma.

### 14 · `14-ujranepesules` – Honnan jöttek az új lakók? – Magyarország a 18. században

- **Tanulási cél:** A **Rákóczi-szabadságharc** (1703–1711) a rendi jogokért és a Habsburg-abszolutizmus ellen
  indult; a **szatmári béke** (1711) kompromisszuma a rendi alkotmány megtartása és a Habsburg-uralom elismerése volt;
  a **Pragmatica Sanctio** (1723) a nőági örökösödést és a birodalom egységét rögzítette. A 18. században az ország
  népessége megkétszereződött: **belső vándorlás** (északról és nyugatról az Alföldre), **szervezett betelepítés**
  (német telepesek – „svábok”) és **öntevékeny betelepülés** (szerbek, románok, szlovákok, ruszinok) eredményeként
  **többnyelvű és többvallású** ország lett, amelyben a magyar anyanyelvűek aránya csökkent. A **felvilágosult
  abszolutizmus** (Mária Terézia: úrbéri rendelet, Ratio Educationis; II. József: türelmi rendelet, nyelvrendelet)
  reformokkal és központosítással akart modernizálni; a **kettős vámhatár** a birodalmi munkamegosztást szolgálta.
- **Kerettanterv:** „Magyarország a Habsburg Birodalomban.” · „A szabadságharc okai és céljai.” · „A szatmári béke
  kompromisszuma.” · „A belső vándorlás, a szervezett betelepítés és az öntevékeny betelepülés.” · „A többnyelvű és
  többvallású ország.” · „Gazdaság és életmód.” · „A Pragmatica Sanctio.” · „Mária Terézia: együttműködés és reform.” ·
  „II. József reformpolitikája és kudarca.” · Fogalmak: „kuruc, labanc, szabadságharc, trónfosztás, amnesztia,
  felvilágosult abszolutizmus, kettős vámhatár, úrbéri rendelet, Ratio Educationis, türelmi rendelet, nyelvrendelet.” ·
  Személyek: „II. Rákóczi Ferenc, Mária Terézia, II. József.” · Kronológia: „1703–1711 a Rákóczi-szabadságharc, 1711 a
  szatmári béke, 1740–1780 Mária Terézia uralkodása, 1780–1790 II. József uralkodása.” · Topográfia: „Temesvár,
  Határőrvidék, Poroszország.” · fejlesztés: „Magyarország újranépesülésének és a folyamat eredményének értelmezése
  tematikus térképek segítségével.”, „Mária Terézia és II. József politikájának összehasonlítása.” · tevékenység: „A
  népességmozgások és az egyes népcsoportok nyomon követése térképen.”, „Magyarázó ábra készítése a kettős vámhatár
  működéséről.”
- **Tévhitek:** „Az országot a Habsburgok szándékosan töltötték fel idegenekkel a magyarok ellen.” (A betelepítés
  gazdasági-adózási és katonai célú volt; a földesurak is hívtak telepeseket; a szerbek, románok nagyrészt maguktól
  jöttek – *vitatott* megítélés, két nézőpont.) „A népesség csak a betelepítés miatt nőtt.” (A természetes szaporodás
  és a belső vándorlás nagyobb tényező – *vitatott* arányok.) „A szatmári béke vereség volt, semmit sem ért el.” „II.
  József mindent rosszul csinált.” (A türelmi rendelet és a jobbágyrendelet megmaradt.) „A kettős vámhatár csak
  Magyarországot sújtotta.”
- **Ne ismételd:** nincs közvetlen 5–6-os előzmény (az 5–6 a 18. századot kihagyta); a `tortenelem-7-8/14-hataron-tul`
  20. századi etnikai adatait itt nem vetítjük vissza.
- **Kulcsvizuál:** **újranépesülés térképen és görbén** (TortMap, `map-karpat` + TortTerr `mo1914hsz` keret
  „vázlatos”): vándorlási nyilak (TortMap `line`, `head`, szín csoportonként – egymáshoz hasonló, semleges tónusok,
  mintával, hogy egyik nép se „rossz” színű), dátummal: belső vándorlás (Felvidék → Alföld, Dunántúl), szlovák
  telepesek (Békéscsaba, Nyíregyháza), német telepek (Bánság, Bácska, Tolna–Baranya, Buda környéke) három hullámban,
  szerb (1690 és később), román (Erdély, Partium, Bánság), ruszin; a Temesi bánság és a Határőrvidék külön igazgatása
  sraffozott sávként (TortTerr `fill` `poly` + `hatch`, „vázlatos”). Mellette **népesség-görbe** (FoldChart) 1720 →
  1787 (és az 1787-es népszámlálás), és az etnikai összetétel becslése két időpontban (MatChart kör, *becslés,
  vitatott*).
- **Kipróbálom:**
  1. **Időcsúszka 1690 → 1787**: a nyilak megjelennek, a görbe nő; kattintásra csoportkártya (honnan, miért, ki hívta,
     milyen kedvezmény – pl. adómentesség évei).
  2. **Kettős vámhatár modell** (leckén belül, *modell*): áruk (gabona, marha, bor ↔ posztó, vas, üveg) indulnak
     Magyarországról, az örökös tartományokból és külföldről; a két vámhatáron (a birodalom külső határa; a magyar–osztrák
     belső határ) a vám színes pöttyként rakódik az árura; a diák kiválasztja, honnan hová visz egy árut, és látja a
     végső árat. A tanulság: a magyar mezőgazdasági termék a birodalmon belül olcsón talált piacot, a külföldi ipari
     termék drága lett – az ipar nem fejlődött.
  3. **Mária Terézia ↔ II. József** (TortCards): 10 intézkedés → melyiké; és kinek a módszere: együttműködés a
     rendekkel / rendeleti kormányzás. A végén: mit vont vissza II. József 1790-ben (három kivétel).
- **Tippelj!** 4. lépés: „Nagyjából hányszorosára nőtt a Magyar Királyság (Erdéllyel) népessége 1720 és 1787 között? kb.
  1,2× / kb. 2× / kb. 5×” *(ellenőrizendő; a lecke tartománnyal adja)*.
- **Lépések:**
  1. Kuruc és labanc – a Rákóczi-szabadságharc okai (abszolutizmus, adók, vallási sérelmek, a jobbágyok és a nemesek
     eltérő céljai) – TortCards vagy két oszlop; Rákóczi kiáltványa (*Recrudescunt*, 1703, közkincs latin; saját
     fordítás egy mondatra).
  2. A szabadságharc fordulópontjai – kis idővonal (1703, 1704, 1705 Szécsény, 1707 Ónod – trónfosztás, 1708 Trencsén,
     1711) és egy **vázlatos** térkép a kuruc ellenőrzés kiterjedéséről két időpontban (1705, 1710) – lágy szélű folt.
  3. A kompromisszum – szatmári béke (1711): amnesztia, rendi alkotmány, vallásügy; Pragmatica Sanctio (1723) – a
     birodalom egysége és a magyar alkotmány egymás mellett (két kis doboz).
  4. Üres vidékek – a hódoltság utáni állapot (12-re utalás), Tippelj!
  5. Honnan jöttek? – a kulcsvizuál, időcsúszka; a három betelepülési forma megkülönböztetése (kártyák).
  6. Többnyelvű, többvallású ország – az etnikai becslés két időpontban; „becslés, vitatott”; Honnan tudjuk? – az 1720-as
     adóösszeírás (nem népszámlálás: adózó háztartásokat számolt – mit hagy ki?) és II. József népszámlálása (1784–1787,
     anyanyelvet nem kérdezett! – a nemzetiségi becslések más forrásból).
  7. Kettős vámhatár – a modell.
  8. Felvilágosult abszolutizmus – Mária Terézia ↔ II. József (TortCards); úrbéri rendelet (1767), Ratio Educationis
     (1777), türelmi rendelet (1781), nyelvrendelet (1784), a visszavonás (1790).
  9. Összefoglalás – az ország 1787-ben: népesség, nyelvek, vallások, vámhatár; átvezetés a 16-hoz (nyelvkérdés).
- **Adatok:**
  - 1703. június (Tiszahát); 1704. július 8. Gyulafehérvár (erdélyi fejedelem); 1705. szeptember Szécsény; 1707. június
    Ónod; 1708. augusztus 3. Trencsén; 1711. április 29–30. szatmári béke, május 1. majtényi fegyverletétel
    *(ellenőrizendő)*; Pragmatica Sanctio: 1722–23. évi I–III. tc. *(ellenőrizendő)*.
  - 1690 nagy szerb vándorlás (III. Arsenije Čarnojević) – létszám *(vitatott, tartomány)*; impopulációs pátens 1689
    *(ellenőrizendő)*; 1723. évi CIII. tc. (szabad személyek betelepítése) *(ellenőrizendő)*; a német betelepítés három
    hulláma: 1720-as évek, 1763–1773, 1782–1787 *(ellenőrizendő)*; Békéscsaba 1718 *(ellenőrizendő)*.
  - Népesség: 1720 kb. 4 millió *(becslés, vitatott – az 1720-as összeírásból korrigálva)*; 1787: a Magyar Királyság és
    Erdély (és külön a Határőrvidék, Horvátország) népszámlálási adata *(ellenőrizendő – Dányi Dezső – Dávid Zoltán:
    *Az első magyarországi népszámlálás (1784–1787)*, KSH 1960)*.
  - Etnikai összetétel 1720 körül és 1787 körül: becslések (Acsády Ignác 1896; Thirring Gusztáv; Kováts Zoltán)
    *(becslés, vitatott; a lecke két forrást mutat, és kimondja, hogy 1787-ben anyanyelvet nem kérdeztek)*.
  - Kettős vámhatár: 1754 *(ellenőrizendő)*; a vámtételek *(modell: a lecke kitalált, de nagyságrendben forrás alapú
    tételekkel dolgozik, „kitalált példa”)*.
  - Úrbéri rendelet 1767; Ratio Educationis 1777; türelmi rendelet 1781. október 25. *(ellenőrizendő)*; nyelvrendelet
    1784; jobbágyrendelet 1785; II. József † 1790. február 20.; a visszavonás 1790. január 28.
- **Modulok:** FoldChart (görbe, pont), TortMap (`map-karpat`; `line` nyilak, `region`, `labels`, `stamp`), TortTerr
  (`outline` `mo1914hsz`, `fill` poly `hatch`), MatChart (`pie`), TortCards, TortTimeline (`cards`), TortSource, TtTipp.
  Leckén belül: kettős vámhatár modell, kuruc-folt.
- **Review-pontok (történész):** a betelepítés értékelésének két nézőpontja; a népességi és etnikai becslések forrása és
  tartománya; a nyilak (honnan pontosan) – vázlatosság; a csoportszínek semlegessége.

### 15 · `15-iparosodas` – Mitől lett tízszer olcsóbb egy autó? – az ipari forradalmak és az új eszmék

- **Tanulási cél:** Az **első ipari forradalom** (Nagy-Britannia, 18. század második fele) a textiliparban, a
  bányászatban, a kohászatban és a gőzgéppel indult; a **közlekedés forradalma** (vasút, gőzhajó) összekötötte a
  piacokat. A **második hullám** (19. század vége) az elektromosság és a vegyipar korszaka; a **futószalag** (Ford, 1913)
  a **tömegtermelés** jelképe. Az iparosodás nagyvárosokat (Manchester) teremtett, rossz lakás- és egészségügyi
  viszonyokkal, **munkanélküliség**gel és társadalmi **szegregáció**val; ökológiai következményei is voltak. Az új
  helyzetre három eszme adott választ: **liberalizmus** (jogegyenlőség, alkotmányosság), **nacionalizmus** (nemzetépítés,
  nemzetállam), **konzervativizmus** (szerves reform, a forradalom elutasítása).
- **Kerettanterv:** „Liberalizmus: jogegyenlőség és alkotmányosság.” · „Nacionalizmus: nemzetépítés és nemzetállam.” ·
  „Konzervativizmus: szerves reform és a forradalom elutasítása.” · „Az első hullám: textilipar, bányászat, kohászat.” ·
  „A közlekedés forradalma.” · „A második hullám: elektronika és vegyipar.” · „A gyár és a futószalag.” · „Az ipari
  forradalmak társadalmi és környezeti hatásai.” · Fogalmak: „liberalizmus, nacionalizmus, nemzetállam,
  konzervativizmus, reform, ipari forradalom, munkanélküliség, tömegtermelés, szegregáció.” · Személyek: „James Watt,
  Thomas Edison, Henry Ford.” · Topográfia: „Manchester, New York.” · fejlesztés: „Az iparosodás hullámainak
  azonosítása és összevetése.”, „Egy ipari nagyváros életkörülmé- nyeinek jellemzése.”, „Az ipari forradalmak ökológiai
  következmé-nyeinek azonosítása.”, „A 19. századi demográfiai változások okainak feltárása.” · tevékenység:
  „Grafikonok, adatsorok elemzése az ipari forradalmak társadalmi és demográfiai hatásairól.”
- **Tévhitek:** „Watt találta fel a gőzgépet.” (Newcomen 1712; Watt a külön kondenzátorral tette hatékonnyá – utalás az
  5–6-ra.) „Az ipari forradalom mindenkinek azonnal jobb életet hozott.” „A futószalag a munkásokat gyorsabb munkára
  hajtotta – ennyi.” (A munka szétbontása + szállítás a munkáshoz.) „A liberális és a konzervatív a mai pártokat
  jelenti.” (Utalás a 7–8 `01-nemzetallamok`-ra.) „A környezetszennyezés 20. századi jelenség.”
- **Ne ismételd:** `tortenelem-5-6/18-gozgep` (gőzgép metszete, Newcomen ↔ Watt, orsók száma csúszkán, fonóterem),
  `tortenelem-7-8/01-nemzetallamok` (eszme-kártyák, 7. lépés – ott 20. század eleje). Itt **adatsorok és futószalag**;
  az eszmék a 19. század első felének kérdéseire adott válaszként (forrásrészlettel).
- **Kulcsvizuál:** **futószalag-szimuláció** (leckén belüli rajz, „modell”): egy alváz útja; kapcsoló „álló szerelés”
  (egy csapat mindent csinál egy helyen) ↔ „futószalag” (a munka n lépésre bontva, a szalag viszi az alvázat); csúszka:
  állomások száma 1 … 45 → átfutási idő és óránként elkészülő autók; mellette a valós adat (12,5 óra → kb. 1,5 óra,
  1913–1914) és a Ford T-modell árának esése (FoldChart). Második kép: **Manchester** – népesség 1771 → 1851 (FoldChart)
  és **Chadwick 1842-es táblája**: az átlagos halálozási életkor osztályonként (MatChart oszlop) – forráskártyával.
- **Kipróbálom:**
  1. Futószalag-csúszka; a „munka szétbontása” animáció (egy feladat egyre kisebb mozdulatokra bomlik).
  2. „Melyik hullám?” – TortCards: 12 találmány/termék → első / második hullám (pl. fonógép, kokszolás, gőzmozdony ↔
     dinamó, izzólámpa, műtrágya, festékipar, belső égésű motor).
  3. **Eszme-olvasó:** három rövid közkincs forrásrészlet (Burke 1790 – konzervatív; Mill 1859 vagy Constant 1819 –
     liberális; Mazzini 1830-as évek – nemzeti) saját fordításban → melyik eszme; a kulcsszó kiemelve.
- **Tippelj!** 2. lépés: „A futószalag bevezetésével (1913–1914) mennyi lett egy T-modell alvázának összeszerelési ideje a
  korábbi kb. 12,5 óra helyett? kb. 10 óra / kb. 6 óra / kb. 1,5 óra”.
- **Lépések:**
  1. Miért Nagy-Britannia? – szén, tőke, piac, gyarmatok, mezőgazdasági változás (kártyák); az első hullám ágazatai.
  2. Futószalag – a kulcsvizuál, Tippelj!, csúszka (Ford, 1913; tömegtermelés).
  3. A közlekedés forradalma – vasút (Liverpool–Manchester 1830), a vasúthálózat hossza (FoldChart), a távolság
     „zsugorodása” (London–Manchester utazási idő a postakocsi ↔ vasút korában *(ellenőrizendő)*).
  4. A második hullám – Edison (izzólámpa 1879), elektromos hálózat, vegyipar; TortCards „Melyik hullám?”.
  5. Az ipari város – Manchester népessége (FoldChart); szegregáció: a gazdag külváros és a munkásnegyed (egyszerű saját
     térképvázlat, „vázlatos”). Honnan tudjuk? – Engels (*A munkásosztály helyzete Angliában*, 1845, † 1895 – közkincs;
     saját fordítás) – szemtanú és politikai céllal író szerző.
  6. Hány évet élt egy manchesteri munkás? – Chadwick-tábla (MatChart), forráskritika: az „átlagos halálozási életkor”
     a csecsemőhalandóság miatt alacsony – nem azt jelenti, hogy 17 évesen öregek voltak.
  7. Szén és füst – a brit szénkitermelés (FoldChart) és a környezeti hatások (szmog, folyószennyezés; London „nagy
     bűz”, 1858).
  8. Három válasz – liberalizmus, nacionalizmus, konzervativizmus: eszme-olvasó.
  9. Összefoglalás – két hullám egymás mellett (ágazat, energia, jelkép, város) és New York (a második hullám
     metropolisa, egy adat).
- **Adatok:**
  - Newcomen: 1712; Watt külön kondenzátora: 1769 (szabadalom) *(ellenőrizendő)*; Liverpool–Manchester vasút: 1830.
    szeptember 15.; Edison izzó: 1879; Ford T-modell: 1908; mozgó futószalag (Highland Park): 1913, az alváz szerelése
    kb. 12,5 óráról kb. 1,5 órára (93 perc) *(ellenőrizendő)*; a T-modell ára: 850 USD (1908) → kb. 260–290 USD
    (1924–1925) *(ellenőrizendő)*.
  - Manchester népessége: 1771/1773 kb. 22–30 ezer; 1801 kb. 70–75 ezer; 1851 kb. 300 ezer *(ellenőrizendő; a
    közigazgatási határ változott – a `.md` rögzíti, melyik egység)*.
  - E. Chadwick: *Report on the Sanitary Condition of the Labouring Population of Great Britain* (1842, † 1890 –
    közkincs): Manchester, átlagos halálozási életkor: „professional persons and gentry” 38, „tradesmen” 20, „mechanics,
    labourers” 17 év *(ellenőrizendő a jelentés táblázatából)*.
  - Brit szénkitermelés: 1800 kb. 10–15 millió t; 1850 kb. 50–60 millió t; 1913 kb. 287 millió t *(ellenőrizendő –
    B. R. Mitchell: *British Historical Statistics*)*.
  - Brit vasúthálózat: 1840 kb. 2 400 km; 1850 kb. 10 000 km; 1900 kb. 30 000 km *(ellenőrizendő)*.
  - Forrásrészletek: Burke 1790 († 1797), Constant 1819 († 1830), Mill 1859 († 1873), Mazzini († 1872) – közkincs;
    saját fordítás.
- **Modulok:** FoldChart (vonal, oszlop, log opcionális), MatChart (oszlop), TortCards, TortSource, TortTimeline,
  TtTipp. Leckén belül: futószalag-szimuláció (zárt képlet a csúszkából és `L.st`-ből), szegregáció-vázlat.
- **Review-pontok:** a Ford-adatok forrása (gyakran ismételt, de ellenőrizendő számok); a Chadwick-tábla helyes
  értelmezése; az eszme-részletek ne legyenek karikatúrák.

### 16 · `16-rendi-orszaggyules` – Miért tartott évtizedekig egy reform? – a reformkor országgyűlése és vitái

- **Tanulási cél:** A reformkorban (1830–1848) a polgári átalakulás programja (**érdekegyesítés**, **közteherviselés**,
  **jobbágyfelszabadítás**, magyar nyelv, polgári alkotmányosság) a **rendi országgyűlésen** keresztül próbált
  törvénnyé válni. A **rendi államszervezet** lassú volt: a vármegyék **követutasítás**sal kötötték követeiket, az
  **alsótábla** megyénként szavazott, a **felsőtábla** (főrendek) és az **uralkodó** (Bécs, Metternich) is
  megakaszthatta a javaslatot. Ezért egy reform – pl. az örökváltság vagy a magyar államnyelv – éveken, országgyűléseken
  át vándorolt. **Széchenyi** és **Kossuth** a célokban sokban egyetértett, a módszerben (fokozatos, felülről ↔ a
  nyilvánosságra támaszkodó, gyorsabb) és a Bécshez való viszonyban vitatkoztak. A **nyelvkérdés** a nemzetté válás
  kérdése volt – és a nemzetiségeké is.
- **Kerettanterv:** „A Habsburg Birodalom és Magyarország.” · „A rendi országgyűlés és a megyerendszer.” · „A nyilvánosság
  megteremtése, politika és kultúra.” · „A magyar nyelv ügye és a nemzetté válás.” · „A jobbágykérdés: örökváltság,
  kárpótlás.” · „A polgári alkotmányosság kérdése.” · „Széchenyi és Kossuth programja és vitája.” · Fogalmak: „alsó- és
  felsőtábla, érdekegyesítés, közteherviselés, jobbágyfelszabadítás, örökváltság.” · Személyek: „József nádor, Klemens
  Metternich, Wesselényi Miklós, Széchenyi István, Kölcsey Ferenc, Deák Ferenc, Kossuth Lajos, Ganz Ábrahám.” ·
  Kronológia: „1830–1848 a reformkor, 1830 a Hitel megjelenése, 1844 törvény a magyar államnyelvről.” · fejlesztés: „A
  jobbágykérdés és megoldási javaslatainak értelmezése szövegek és adatok alapján.”, „A nyelvkérdés és a nemzetté válás
  bemutatása különböző források segítségével. (Pl. magyar államnyelv, a zsidóság nyelvváltása, Lőv Lipót)”, „A polgári
  alkotmányosság programjának bemutatása politikai írások, országgyűlési felszólalások és ábrák alapján.”, „Széchenyi és
  Kossuth társadalmi hátterének, egyéniségének, álláspontjának és eredményeinek összevetése.” · tevékenység: „Ábrák
  készítése a rendi államszervezet működéséről.”, „Táblázatos összefoglaló készítése a reformellenzék, a konzervatívok és
  az udvar álláspontjáról a főbb vitakérdésekben.”
- **Tévhitek:** „A rendi országgyűlésen a képviselők egyenként szavaztak.” (Az alsótáblán vármegyénként; a városok
  együtt egy szavazatot értek.) „A reformokat csak Bécs akadályozta.” (A felsőtábla és a konzervatív megyék is.) „Az
  örökváltság ingyenes volt.” „Széchenyi és Kossuth ellenségek voltak.” (Vitatkozó szövetségesek – két nézőpont.) „A
  magyar nyelv ügye mindenkinek egyformán fontos volt.” (A horvát, szlovák, román nemzeti mozgalom saját nyelvét
  védte.)
- **Ne ismételd:** `tortenelem-5-6/19-marcius-15` (Pest-Buda térkép, Lánchíd, órás csúszka), `20-szabadsagharc`. Itt
  **nincs** Pest-Buda térkép: intézményséma, szavazás, kalkulátor.
- **Kulcsvizuál:** **a törvény útja a rendi országgyűlésen** (TortState): vármegyei közgyűlés → (követutasítás) →
  követek → **alsótábla** → üzenetváltás → **felsőtábla** → felirat → **uralkodó** (Magyar Udvari Kancellária,
  Államtanács, Metternich) → szentesítés / elutasítás; a nádor a felsőtábla elnöke; a Helytartótanács végrehajt. Az
  alsótábla szavazása **TortParl-patkón**: minden „ülés” egy vármegye (+ kerületek; a szabad királyi városok
  együtt egy ülés, külön mintával) – a megye színe a követutasítása (igen / nem / nincs utasítás); a patkó alatt a
  felsőtábla kis sávja (főrendek – egyenként szavaztak) és a „király” kapu. Egy javaslat (pl. „önkéntes örökváltság”)
  pöttyként halad a sémán; ha elakad, a következő országgyűlésen újraindul (évszám-számláló: 1832 → 1836 → 1840 → 1844 →
  1848).
- **Kipróbálom:**
  1. **Törvénygyár** (*kitalált példa* a megyék szavazatára, valós intézményi szabályokkal): a diák kapcsolókkal
     átállít vármegyéket (követutasítás), és nézi, átmegy-e az alsótáblán, a felsőtáblán, szentesíti-e az uralkodó.
     Négy valós esetet is „lejátszik” gombnyomásra (forrással): pl. 1840. évi VII. tc. (önkéntes örökváltság) ✔, 1844.
     évi II. tc. (magyar nyelv) ✔, a közteherviselés 1844-ben ✘ (a felsőtáblán vagy a megyéken *(ellenőrizendő, melyik
     javaslat hol bukott el)*).
  2. **Örökváltság-számoló** (*modell*): a jobbágy évi terhei (robot napokban × napszám, kilenced, cenzus) → megváltási
     ár (a terhek tőkésítve, pl. 5 %-kal = 20×); mennyi év megtakarításából tudná kifizetni egy átlagos telkes jobbágy?
     A tanulság: önkéntes örökváltságra kevesen voltak képesek → kötelező, állami kárpótlásos megoldás kell (1848 → 17).
  3. **Széchenyi ↔ Kossuth** (TortCards): 10 állítás (közkincs eredeti szövegekből, rövid idézet vagy parafrázis) →
     Széchenyi / Kossuth / mindkettő.
- **Tippelj!** 3. lépés: „Hány szavazata volt az alsótáblán az összes szabad királyi városnak együtt? annyi, ahány város /
  annyi, mint egy vármegyének (egy) / egy sem” *(ellenőrizendő: a városok együttes szavazata a gyakorlatban)*.
- **Lépések:**
  1. Bécs és Pozsony – a Habsburg Birodalom és Magyarország viszonya (kancellária, Helytartótanács, nádor, országgyűlés)
     egy kis sémán; Metternich rendszere; József nádor.
  2. A vármegye – közgyűlés, követválasztás, követutasítás; a nemesség aránya a népességben (*becslés*) – „ki
     politizálhat?” (MatChart pontrács).
  3. Az országgyűlés – alsó- és felsőtábla; a TortParl-patkó; Tippelj!
  4. Egy reform útja – a törvénygyár, négy valós eset.
  5. A jobbágykérdés – örökváltság-számoló; kárpótlás; közteherviselés (a nemesi adómentesség).
  6. Széchenyi – *Hitel* (1830), MTA (1825), Lánchíd, gőzhajózás (Ganz Ábrahám gyára egy mondatban); a fokozatos reform.
     Honnan tudjuk? – a *Hitel* egy mondata (közkincs, eredeti).
  7. Kossuth és a nyilvánosság – Országgyűlési Tudósítások, Pesti Hírlap (1841); Wesselényi, Kölcsey (*Parainesis* vagy
     országgyűlési beszéd – közkincs); a vita (Kelet Népe, 1841); TortCards.
  8. A nyelv ügye – 1790 → 1844 idővonal (latin → magyar), a zsidóság nyelvváltása (Lőw Lipót, 1844-es magyar nyelvű
     prédikáció *(ellenőrizendő)*), a nemzetiségi mozgalmak ellenvetései (horvát: Gaj; szlovák: Štúr) – két nézőpont.
  9. Összefoglalás – a reformellenzék, a konzervatívok és az udvar álláspontja táblában (a kerettanterv tevékenysége);
     1847–48: az utolsó rendi országgyűlés.
- **Adatok:**
  - Vármegyék és szavazatok az alsótáblán: a vármegyék száma (Horvátország megyéivel), a kerületek (Jászkun, hajdú
    városok), a szabad királyi városok együttes szavazata, a káptalanok és a távollevők követeinek helyzete
    *(ellenőrizendő – pl. Szijártó M. István: *A diéta*, 2005; Pajkossy Gábor munkái)*.
  - Országgyűlések: 1825–1827, 1830, 1832–1836, 1839–1840, 1843–1844, 1847–1848 *(ellenőrizendő)*.
  - 1825. november 3. MTA-felajánlás; *Hitel*: 1830; *Kelet Népe*: 1841; *Pesti Hírlap*: 1841. január 2.; 1840. évi VI. és
    VII. tc.; 1844. évi II. tc.; 1836. évi IV. tc. (Lánchíd) *(ellenőrizendő)*.
  - Az örökváltságok száma 1840–1848 között *(ellenőrizendő; ha nincs megbízható szám, a lecke kimondja: „kevés”)*.
  - A nemesség aránya a népességben kb. 4–5 % *(becslés, ellenőrizendő)*.
  - A törvénygyár megyei szavazatai: *(kitalált példa)* – a négy valós eset kimenetele forrással.
  - Széchenyi († 1860), Kossuth († 1894), Wesselényi († 1850), Kölcsey († 1838), Deák († 1876) – közkincs eredeti
    szövegek.
- **Modulok:** TortState (a törvény útja, `card`, kapcsolók), TortParl (`hemi` a megyékre, `palette` mintákkal, `legend`),
  TortCards, MatChart (pontrács), TortTimeline (`cards`), TortSource, TtTipp. Leckén belül: a javaslat-pötty útja,
  örökváltság-számoló.
- **Review-pontok:** az alsótábla szavazási rendje (a tankönyvi egyszerűsítés és a tényleges gyakorlat eltérése!); a
  négy valós eset; a nemzetiségi nézőpontok arányos megjelenése; a TortParl mintáinak jelentése (követutasítás, nem
  párt).

### 17 · `17-forradalom-1848` – Mit vívtak ki 1848-ban, és miért kellett megvédeni? – áprilisi törvények és szabadságharc

- **Tanulási cél:** Az 1848-as európai forradalmi hullám idején a pesti forradalom (március 15.) és a pozsonyi
  országgyűlés az **áprilisi törvényekkel** (1848. április 11.) a rendi államot **polgári alkotmányos monarchiává**
  alakította: **népképviseleti országgyűlés**, **felelős minisztérium** (Batthyány-kormány), **sajtószabadság**,
  **jobbágyfelszabadítás** állami kárpótlással, **közteherviselés**, Erdély uniója. A választójog cenzusos maradt, de a
  rendi kiváltság helyett vagyon és műveltség döntött. A **politikai nemzet** fogalma a nemzetiségek egy részének
  követeléseivel ütközött. Az udvar és a vele szövetkező horvát, szerb, román, szlovák mozgalmak elleni harcban a
  **honvédség** szerveződött (Pákozd), a tavaszi hadjárat után a **Függetlenségi nyilatkozat** (1849. április 14.)
  kísérlet volt az önálló államra; az orosz beavatkozás után a szabadságharc **Világosnál** ért véget; a **megtorlás**
  (Arad, Batthyány) a forradalom mártírjait adta. A vívmányok egy része (jobbágyfelszabadítás) megmaradt.
- **Kerettanterv:** „Az európai forradalmi hullám és március 15.” · „Az első magyar polgári alkotmány: az áprilisi
  törvények.” · „A Batthyány-kormány tevékenysége.” · „Harc a dinasztiával és a vele szövetkező nemzetiségekkel.” · „A
  tavaszi hadjárat.” · „A Függetlenségi nyilatkozat, kísérlet az önálló állam megteremtésére.” · „A szabadságharc
  leverése és a megtorlás.” · Fogalmak: „márciusi ifjak, sajtószabadság, cenzúra, áprilisi törvények, népképviseleti
  országgyűlés, politikai nemzet, nemzetiség, honvédség, Függetlenségi nyilatkozat.” · Személyek: „Petőfi Sándor,
  Batthyány Lajos, Görgei Artúr, Bem József, Klapka György, Ferenc József, Julius Haynau.” · Kronológia: „1848. március
  15. a pesti forradalom, 1848. április 11. az áprilisi törvények, 1848. szeptember 29. a pákozdi csata, 1849.
  április–május a tavaszi hadjárat, 1849. április 14. a Függetlenségi nyilatkozat, 1849. május 21. Buda visszavétele,
  1849. augusztus 13. a világosi fegyverletétel, 1849. október 6. az aradi vértanúk és Batthyány kivégzése.” ·
  Topográfia: „Pákozd, Debrecen, Isaszeg, Világos, Komárom, Arad.” · fejlesztés: „A reformkori elképzeléseknek, a
  forradalom követeléseinek és az áprilisi törvényeknek az összehasonlítása.”, „A nemzetiségek és a kisebbségek
  részvételének (pl. németek, szlávok, és zsidók) bemutatása a szabadságharcban és az azt követő megtorlás során.”, „A
  magyar forradalom és szabadságharc elhelyezése az európai környezetben.”
- **Tévhitek:** „Az áprilisi törvények általános választójogot adtak.” (Cenzusos – a felnőtt férfiak egy része.) „A
  nemzetiségek mind a császár oldalán harcoltak.” (Sok szlovák, német, szerb, zsidó, lengyel honvéd is volt; a nemzeti
  mozgalmak saját célokat követtek.) „A szabadságharcot csak az orosz túlerő verte le.” („Vitatott”: katonai,
  politikai, gazdasági okok.) „A Függetlenségi nyilatkozat köztársaságot kiáltott ki.” (Az államforma nyitva maradt;
  Kossuth kormányzó-elnök.) „1849 után minden vívmány elveszett.” (A jobbágyfelszabadítás maradt.)
- **Ne ismételd:** `tortenelem-5-6/19-marcius-15` (órás csúszka, Pilvax → Múzeum útvonal, 12 pont ↔ áprilisi törvények
  párosítása), `20-szabadsagharc` (a tavaszi hadjárat napról napra Hatvantól Komáromig, erőviszony-oszlop az orosz
  beavatkozásnál). Itt **intézményséma, választójog-arány, havonkénti ellenőrzött terület a teljes háborúra**, nemzetiségi
  nézőpontok; a tavaszi hadjárat csak egy kulcsállapot.
- **Kulcsvizuál:** két kép.
  (a) **1847 ↔ 1848 április** (TortState `morph` két layout között): rendi állam (16-os séma, egyszerűsítve) →
  népképviseleti országgyűlés (választók → képviselőház; főrendiház), felelős minisztérium (miniszterelnök + 8
  miniszter, az országgyűlésnek felel – „ellenőriz” él), nádor királyi helytartó, uralkodó (szentesít), sajtó (szabad),
  vármegye (népképviseleti bizottmány). Mellette a **választójog aránya** (MatChart pontrács, 100 pötty = népesség):
  rendi (kb. 1,5–2 % részvétel? *ellenőrizendő* – a nemesség kb. 5 %) ↔ 1848. évi V. tc. (a népesség kb. 7–9 %-a, a
  felnőtt férfiak kb. negyede *(becslés, vitatott)*).
  (b) **Ki mit ellenőriz?** (TortMap, `map-karpat` + TortTerr `mo1914hsz` keret „vázlatos”): havonkénti
  kulcsállapotok 1848. szeptember → 1849. augusztus, leckén belül rajzolt, lágy szélű foltok (honvédség / császári és
  orosz csapatok / nemzetiségi felkelők – semleges színek: indigó, szilva + egy harmadik semleges tónus, sraffozással),
  a csatahelyek pontként (Pákozd, Kápolna, Isaszeg, Buda, Temesvár, Segesvár, Világos, Komárom). Mellette az
  erőviszony-oszlop (MatChart) három időpontban (1848 ősz, 1849 tavasz, 1849 nyár) *(becslés)*.
- **Kipróbálom:**
  1. A TortState `morph`-csúszkája (1847 → 1848); kattintásra kártya: melyik törvénycikk hozta (1848: III. – felelős
     minisztérium, IV. – évenkénti országgyűlés, V. – választójog, VII. – unió, IX. – úrbér, XVIII. – sajtó …).
  2. **„Szavazhatott-e?”** – a diák kiválaszt egy kitalált személyt (céhes mester, negyedtelkes jobbágy, zsellér,
     tanár, nemes, nő, zsidó kereskedő – „kitalált példa”), és a V. tc. feltételei szerint a vásznon kiderül, szavazhatott-e
     (*ellenőrizendő*: a zsidóság választójogának kérdése 1848-ban – vita volt, a törvény nem zárta ki kifejezetten, a
     gyakorlat helyenként igen).
  3. A havonkénti térkép dátumcsúszkája; csatapontra kattintva kártya (csata nem játszódik le).
  4. **Nemzetiségi nézőpontok** (TortSource-kártyák): a horvát, szerb, román, szlovák mozgalom egy-egy követelése
     (1848 tavasz–nyár, közkincs programszövegek – parafrázis), és a szegedi nemzetiségi törvény (1849. július 28.).
- **Tippelj!** 2. lépés: „A népesség nagyjából hány százaléka kapott választójogot 1848-ban? kb. 1 % / kb. 7–9 % / kb.
  50 %” *(a szám ellenőrizendő; tartománnyal)*.
- **Lépések:**
  1. 1848 Európája – Párizs (február), Bécs, Berlin, Milánó (március) – mini-idővonal; március 15. egy mondatban
     (utalás az 5–6-ra) és a 12 pont: mit követelt.
  2. Az áprilisi törvények – `morph`, kattintható törvénycikkek; Tippelj! a választójogról; „Szavazhatott-e?”.
  3. Jobbágyfelszabadítás – kinek mi lett (úrbéres jobbágy ↔ zsellér ↔ majorsági föld) és az állami kárpótlás
     ígérete; kapcsolat a 16 örökváltság-számolójával.
  4. Politikai nemzet és nemzetiségek – a fogalom; a nemzetiségi követelések kártyái, két nézőpont, értékítélet nélkül.
  5. Háború – 1848. szeptember: Jelačić, Pákozd (szeptember 29.), honvédség, OHB; a térkép első kulcsállapotai.
  6. A tél és a tavasz – Windisch-Grätz Pesten (1849. január 5.), Debrecen, Kápolna, az olmützi alkotmány (március 4.),
     a tavaszi hadjárat (egy kulcsállapotként), Isaszeg; a Függetlenségi nyilatkozat (április 14.) – mit mond ki (az
     uralkodóház trónfosztása; az államforma nyitva).
  7. Buda és ami utána jött – május 21.; orosz beavatkozás (június), erőviszony-oszlop; Temesvár, Segesvár (július 31.,
     Petőfi eltűnése – egy mondat), Világos (augusztus 13.), Komárom (október 2. *(ellenőrizendő)*).
  8. Megtorlás – Haynau; október 6.: Arad (13 tábornok – névsor, ábrázolás nélkül) és Pest (Batthyány); a vértanúk között
     nem magyar származásúak is (Aulich, Damjanich, Knezić, Lahner, Leiningen-Westerburg, Poeltenberg …); emlékhely
     (Arad, Szabadság-szobor; Pest, örökmécses) – méltósággal. Honnan tudjuk? – a hadbírósági ítéletek ↔ a későbbi
     emlékirodalom: mit őriz az emlékezet, és miért.
  9. Összefoglalás – mi maradt meg (jobbágyfelszabadítás, polgári jogegyenlőség eszméje), mi nem; értelmező kérdés a
     tanárnak (a vereség okai – vitatott).
- **Adatok:**
  - 1848. február 22–24. Párizs; március 13. Bécs; március 15. Pest; március 18. Berlin és Milánó *(ellenőrizendő)*;
    április 7. Batthyány-kormány kinevezése; április 11. szentesítés (1848. évi I–XXXI. tc.) *(ellenőrizendő)*.
  - 1848. évi V. tc.: választójog 20 éves, vagyoni/műveltségi cenzussal *(a feltételek a törvényszövegből)*; a
    választójogosultak száma és aránya *(becslés, vitatott: a népesség kb. 6,5–9 %-a – ellenőrizendő)*; a népképviseleti
    országgyűlés képviselőinek száma *(ellenőrizendő)*.
  - 1848. szeptember 11. Jelačić átkel a Dráván; szeptember 29. Pákozd; október 30. Schwechat; december 2. Ferenc József;
    1849. január 5.; február 26–27. Kápolna; március 4. olmützi alkotmány; április 6. Isaszeg; április 14.; május 21.;
    június 15–18. orosz beavatkozás kezdete *(ellenőrizendő)*; július 28. szegedi nemzetiségi és zsidóemancipációs
    törvény; július 31. Segesvár; augusztus 9. Temesvár; augusztus 13. Világos; október 2. Komárom; október 6. Arad, Pest.
  - Erőviszonyok: a honvédség legnagyobb létszáma kb. 150–170 ezer; a császári és orosz erők 1849 nyarán együtt kb.
    350–370 ezer *(becslés, vitatott; ellenőrizendő – Hermann Róbert munkái)*.
  - Az aradi 13 vértanú névsora; Batthyány kivégzése Pesten.
  - Törvényszöveg (1848-as törvénycikkek): `### Idézet` † nélkül (jogszabály); Petőfi († 1849), Kossuth († 1894)
    eredeti szövegei közkincsek.
  - A havonkénti kulcsállapot-sokszögek: töréspontok a kódban; két egybevetett atlasz a `.md`-ben.
- **Modulok:** TortState (`morph`, két `layout`, `card`), TortMap (`map-karpat`; `region` poly, `labels`, `stamp`),
  TortTerr (`outline` `mo1914hsz`; `fill` poly `hatch`), MatChart (pontrács, oszlop), TortParl (opcionális: a
  képviselőház patkója, `grey: true` – nem pártok, hanem a képviselők csak számként), TortSource, TortTimeline, TtTipp.
  Leckén belül: havonkénti kulcsállapotok, „Szavazhatott-e?”.
- **Review-pontok (történész):** a választójog aránya és a zsidóság választójoga; a nemzetiségi mozgalmak bemutatásának
  arányossága (céllal és indokkal, nem árulóként); a térkép kulcsállapotai (a frontvonal nem egységhatár, foltszerű
  befolyási terület); a vereség okainak két-három nézőpontja; a megtorlás méltósága (nincs ábrázolás, csak név, dátum,
  hely).

---

## 4. Modulok – minden lecke kész modulokra épül

### 4.1 Forrás, sorszám, md5 (2026-11-25-i állapot)

Az md5 a blokkra vonatkozik: a `/* ── MODUL: …` sortól az első utána következő `MODUL VÉGE` sor végéig, záró újsor
nélkül (EGYSEGESITES.md). A sorszám a MODUL-sor – MODUL VÉGE-sor (mindkettő benne). **Másolás után md5-tel
ellenőrizd**; ha a sorszám elcsúszott, az md5 dönt (bármely azonos md5-ű példány jó). Nem használható változatok:
TortSource `50d3c6fd…`/`134cb7b3…`, TortCards `c2a85a56…` (`tortenelem-5-6` régi példányai).

| Modul | Forrás (`leckek/tortenelem-7-8/…`) | sorok | md5 | megjegyzés |
|---|---|---|---|---|
| **TtTipp** | `13-rendszervaltas.html` | 830–976 | `fa839199626ca8aa31f3693a24150d81` | mind a 17 lecke; `stamp` a „vitatott”, „modell”, „kitalált” bélyegekhez |
| **TortTimeline** | `13-rendszervaltas.html` | 978–1393 | `9c5cebae791ce43f3d93b5f2785e6dfd` | mind a 17 (a TortSource `Y`-ja miatt); `cards` elemei soronként csökkenő sorrendben |
| **TortSource** | `13-rendszervaltas.html` | 1395–1563 | `a59b107413f4949197b9d51f1c5a174e` | mind a 17; a `card` előtt `al(1)` (az alfát szorozza) |
| **TortMap** v1.1 | `13-rendszervaltas.html` | 1565–2017 | `05bd08a1c2d32bdd050cba4c4fdbc2e2` | a TortTerr is erre épül; `labels` id-előtag jelenetenként |
| **FoldChart** | `13-rendszervaltas.html` | 2019–2443 | `92a03151ff1c93037ec9a611e70c9e91` | log, `y2`, `diff`, `cursor`, `vspan`; a színek `#rrggbb` |
| **TortParl** v1.1 | `13-rendszervaltas.html` | 2445–2770 | `875d1496e5cd038b159ec13c96dde51f` | `hemi`, `bar`, `legend` (`pd`), `palette` |
| **TortState** v1.1 | `13-rendszervaltas.html` | 2772–3048 | `5c74bd23baebc49fc0345746b1c4ab47` | `layout`/`morph`, `timeline` (`align`), `over`, `hlEdge`, `card` |
| **TortTerr** v1.0 | `13-rendszervaltas.html` | 3050–3437 | `d7e8dcc3e82e93db533ecaef134c4a26` | `TORT_HATAR` + TortMap kell; `outline`/`fill` (poly, hatch) |
| **TortCards** | `12-kadar-rendszer.html` | 1247–1385 | `2c411077c00d1ba0d984102651b64c44` | rendezés zónákba |
| **MatChart** v1.1 | `12-kadar-rendszer.html` | 1813–2331 | `02e3710065229ffbf2fd7f1ac155933a` | oszlop, kör, pontrács, sáv |

Betöltési sorrend a leckében (a `13-rendszervaltas.html` 823–828. sora a minta): `<lecke>.content.js` →
`../../shared/lesson.js` → (térképes leckében) `../../shared/tort/proj.js` → a térképadatok → a leckeszkript, benne a
modulblokkok ebben a sorrendben: TtTipp, TortTimeline, TortSource, TortCards, TortMap, FoldChart, MatChart, TortParl,
TortState, TortTerr (a függőség: TortSource → TortTimeline; TortTerr → TortMap). Térképadat (`shared/tort/`):
`map-mediterran.js` (ókor, Balkán), `map-karpat.js` (Kárpát-medence), `map-europa.js` (Európa), `map-vilag.js` (világ,
durva háttér), `map-torthatar.js` (csak a TortTerr-es leckékben – a `mo1914hsz` kerethez), `map-orszaghatarok.js`
(opcionális „mai határok” réteg).

### 4.2 Leckénként: mit honnan

Rövidítés: **R** = `leckek/tortenelem-7-8/13-rendszervaltas.html`, **K** = `leckek/tortenelem-7-8/12-kadar-rendszer.html`.
A sorszámok a 4.1 táblából. „Kötelező” = minden leckében: TtTipp (R 830–976), TortTimeline (R 978–1393), TortSource
(R 1395–1563).

| Lecke | Kötelező + | Térképadat | Leckén belüli (új) kód |
|---|---|---|---|
| 01 | TortState (R 2772–3048), MatChart (K 1813–2331), TortMap (R 1565–2017), TortCards (K 1247–1385) | `map-mediterran` | Kleiszthenész-keverő, esetkalkulátor |
| 02 | TortParl (R 2445–2770), TortState (R 2772–3048), FoldChart (R 2019–2443), TortCards (K 1247–1385), TortMap (R 1565–2017) | `map-karpat` | centuria-sorrend, „egyenlő szavazat” modell |
| 03 | FoldChart (R 2019–2443), TortCards (K 1247–1385), TortMap (R 1565–2017) | `map-mediterran` | növekedési modell (képlet) |
| 04 | FoldChart (R 2019–2443), TortMap (R 1565–2017), TortCards (K 1247–1385) | `map-vilag`, `map-mediterran` | birodalom-kulcsállapotok (sokszögek, áttűnés), „mérő” tűk |
| 05 | MatChart (K 1813–2331), TortState (R 2772–3048), FoldChart (R 2019–2443), TortMap (R 1565–2017), TortCards (K 1247–1385) | `map-europa` | termés-kalkulátor (zsákok), pestis-hullámfrontok |
| 06 | TortMap (R 1565–2017), TortCards (K 1247–1385) | `map-vilag`, `map-europa` | bizonyítékmátrix, uráli családfa |
| 07 | MatChart (K 1813–2331), TortMap (R 1565–2017), TortTerr (R 3050–3437), TortCards (K 1247–1385) | `map-karpat`, `map-europa`, `map-torthatar` | birtokszerkezet-állapotok, dinasztikus vonalak |
| 08 | TortMap (R 1565–2017), TortTerr (R 3050–3437), MatChart (K 1813–2331), FoldChart (R 2019–2443, opcionális) | `map-karpat`, `map-torthatar` | kamara haszna ↔ kapuadó modell, koronázás-tábla |
| 09 | TortMap (R 1565–2017), TortTerr (R 3050–3437), MatChart (K 1813–2331) | `map-mediterran`, `map-karpat`, `map-torthatar` | oszmán kulcsállapotok, zsoldkalkulátor |
| 10 | FoldChart (R 2019–2443), TortMap (R 1565–2017), TortCards (K 1247–1385) | `map-vilag`, `map-europa` | mennyiségi modell, ezüstút-vastagság |
| 11 | TortState (R 2772–3048), TortMap (R 1565–2017), TortCards (K 1247–1385) | `map-europa`, `map-karpat` | „cuius regio ↔ Torda” falumodell |
| 12 | TortMap (R 1565–2017), TortTerr (R 3050–3437), TortState (R 2772–3048), FoldChart (R 2019–2443), MatChart (K 1813–2331) | `map-karpat`, `map-torthatar` | hódoltsági kulcsállapotok, kettős adó modell |
| 13 | TortState (R 2772–3048), TortCards (K 1247–1385), TortMap (R 1565–2017) | `map-europa` | nyilatkozat-kereső, napóleoni foltok |
| 14 | FoldChart (R 2019–2443), TortMap (R 1565–2017), TortTerr (R 3050–3437), MatChart (K 1813–2331), TortCards (K 1247–1385) | `map-karpat`, `map-torthatar` | kettős vámhatár modell, kuruc-folt |
| 15 | FoldChart (R 2019–2443), MatChart (K 1813–2331), TortCards (K 1247–1385) | – | futószalag-szimuláció, szegregáció-vázlat |
| 16 | TortState (R 2772–3048), TortParl (R 2445–2770), TortCards (K 1247–1385), MatChart (K 1813–2331) | – | javaslat-pötty útja, örökváltság-számoló |
| 17 | TortState (R 2772–3048), TortMap (R 1565–2017), TortTerr (R 3050–3437), MatChart (K 1813–2331), TortParl (R 2445–2770, opcionális) | `map-karpat`, `map-torthatar` | havonkénti kulcsállapotok, „Szavazhatott-e?” |

Idővonal nélküli lecke nincs (a TortTimeline mindenhol bent van), így a `window.TortTimeline = … {Y: null}` csonk
sehol sem kell.

### 4.3 Leckén belüli kód – szabályok (mert nincs új modul)

- **Nincs `/* ── MODUL: … ── */` jelölés** a leckék saját kódján (0. döntés, 3.). Saját segédfüggvény a lecke
  szkriptjében, a modulblokkok **után**, egyértelmű előtaggal (pl. `kleisz…`, `oszmanPoly…`).
- **Sokszögek** (04, 08 (tartományurak), 09, 12, 13, 14, 17): kulcsállapotonként `[[lon, lat], …]` tömb a kódban,
  töréspontonként helységnév-kommenttel; az áttűnés két kulcsállapot között vagy egyszerű keresztáttűnés (alfa), vagy –
  ha a pontszám egyezik – pontonkénti interpoláció; **zárt képlet a dátumból** (visszaléptetés, ugrópróba). Rajzolás:
  `map.region(ctx, [{poly, a}], {color, alpha, blur})` (lágy szél = vázlatos), határvonal helyett. A TortTerr `fill`
  `{poly, hatch}`-ot ott használd, ahol sraffozás kell (vazallus, külön igazgatás), és `{clip}`-pel a
  `mo1914hsz`-keretre vághatsz.
- **Modellek** (esetkalkulátor, termés, kamara haszna, zsold, mennyiségi modell, falumodell, kettős adó, vámhatár,
  futószalag, örökváltság): a számolás tiszta függvény (bemenet → kimenet), a rajz ebből; `L.checks()` kampóval a
  számolt ↔ rajzolt érték egyezését ellenőrizd (szerződés 9.); minden modellen „modell” vagy „kitalált” bélyeg.
- **TortParl nem pártokra** (02: vagyoni osztályok; 16: követutasítás; 17: képviselők szürkén): a `palette` semleges
  tónusai + minta; a jelmagyarázat kimondja, mit jelöl a tónus.
- **TortState `over`** (02, 13): a bordó „irányít” itt egyeduralkodót / forradalmi diktatúrát jelöl – a jelmagyarázat
  mondja ki (a szerződés 20. fejezete a bordót a pártállamhoz rendeli; itt kiterjesztjük „egy kézbe vont hatalom”-ra).

### 4.4 Ismert buktatók (a 7–8 metrikáiból és az EGYSEGESITES-ből)

- `TortMap.labels` id szerint megjegyzi a helyet → **jelenetenként eltérő id-előtag** (különben `--det` hiba).
- `TortMap.frame()` minden hívásnál új nézetobjektumot ad – a TortTerr-nek **egyszer létrehozott, állandó** nézetet adj
  (különben lassú/villog; `pilot/tortenelem-7-8/metrika/05-diktaturak.md`).
- `TortMap.base` a teljes vásznat tengerrel tölti → mindig vágd a térkép keretére.
- `TortSource.stamp` nem ismeri a „vitatott” fajtát → `TtTipp.stamp`.
- `TortTimeline.cards`: a kártyákat soronként csökkenő sorrendben add át; 2 soros kártyánál növeld a `pitch`-et.
- `FoldChart.upTo` log skálán lineárisan interpolál (03: ha `upTo`-t használsz a log görbén, log-térben interpolálj
  magad); az y2 nem kapcsolható ki; a `cursor` felirata ütközhet az y-tengely címével (feljebb tett saját címsor).
- `U.mix` `rgb()`-t ad, a FoldChart `#rrggbb`-t vár.
- Equal Earth: `lon0: 0` (10, 04, ha világtérkép).
- `__qaStates` kulcsa 1-alapú lépésszám; ne nevezz állapotot „vissza”-nak.
- `Lesson.create({resetCtx: true})`; kattintás: `L.pointer.pressed/released/events`; `slider.set(v, {fire: true})`.

---

## 5. Build-, QA- és motorigények

### 5.1 A helyzet (ellenőrizve: `tools/build_lesson.py` fejléce, 2026-11-25)

| Igény | Megoldás a meglévő eszközökkel |
|---|---|
| 55 szavas panel | alapérték (nincs `maxWords`) |
| lektorálás (03, 06, 11, 12, 13, 14, 17) | spec `"review": [...]` (2. tábla) → a build kéri a `<!-- Szakmai ellenőrzés: … -->` blokkot |
| értelmező doboz (06, 11) | spec `"interpretive": true` → a build figyelmeztet, ha nincs `> értelmezés:` doboz |
| forrás minden adathoz | spec `"sources": true` (mind a 17) |
| Kr. e. évszám, tört év | `year` („Kr. e. 508”), `date` („Kr. e. 44. március 15.”); `L.dat(k).a` csillagászati év |
| tartomány, becslés | `range` („kb. 30–60 ezer fő”), „kb.”, „(becslés)” → `est` |
| helyszín | `coord` + `box` (Kárpát: `[9, 42, 30, 51]`; Mediterrán: `[-10, 20, 50, 56]`; Európa: `[-25, 30, 60, 72]`; világ: `[-180, -60, 180, 85]`) |
| idősor (ezüst, ár, népesség, szén) | `series` („1503: … · 1510: …”, `"ux": "év"`, `"unit": "kg"`) |
| arány (centuriák, mina–sékel) | `ratio` („98 : 193”, „1 : 60”) |
| jogszabály- és közkincs idézet | `### Idézet` + `<!-- idézet: … · szerző † <év> · közkincs -->`; saját fordításnál a megjegyzés: „saját fordítás az eredetiből (<kiadás>)” |
| kitalált falu, személyek, megyei szavazatok | „(kitalált példa)” a `.md`-ben, `model` |
| QA-állapotok | `__qaStates` + `--states`; késői állapot: `__lesson.st` közvetlen állítása |

**Új build-, QA- vagy motorfunkció a gyártáshoz nem kell.**

### 5.2 Kis, nem blokkoló javaslatok (a koordinátornak)

1. **`year` perjeles alak** („Kr. e. 508/507”, „1000/1001”): `{v, v2, a}` – ma két kulcs vagy a szövegben áll.
2. **„saját fordítás” jelölés a buildben**: `<!-- idézet: … · saját fordítás · eredeti: <szerző> † <év> -->` formátum
   ellenőrzése (a † + 70 szabály az eredeti szerzőre).
3. **Közös sokszög-segéd a következő egységesítő körben:** a 9–10-ben hét lecke ír kulcsállapot-sokszöget – utána
   érdemes egy `TortPoly` (kulcsállapotok, áttűnés, töréspont-felirat) modult kiemelni (most szándékosan nincs).

---

## 6. Gyártás és lefedettség

### 6.1 Gyártás (10 + 7 párhuzamos ügynök, nincs függőség)

Mivel egyik lecke sem épít modult, a sorrend csak a kockázat szerint számít: az **első kötegbe a nehezebb és lektort kérő
leckék** kerülnek (hosszabb QA, több ellenőrizendő adat), hogy a második köteg indulásakor a koordinátor már lássa a
modulhasználat tipikus hibáit (és a második kötegnek továbbadhassa).

| Köteg | Leckék (nehézség) |
|---|---|
| 1 (10 ügynök) | **06-magyar-ostortenet** (3, 3 lektor), **12-hodoltsag-merlege** (3), **17-forradalom-1848** (3), **04-hodito-birodalmak** (3), **13-francia-forradalom** (3), **14-ujranepesules** (3), **16-rendi-orszaggyules** (3), **11-reformacio** (3), **02-romai-koztarsasag** (3), **01-polisz-demokracia** (3) |
| 2 (7 ügynök) | **09-hunyadiak-torok** (3), **03-monoteizmus** (2), **05-rendi-tarsadalom** (2), **07-arpad-kori-allam** (2), **08-anjou-gazdasag** (2), **10-arforradalom** (2), **15-iparosodas** (2) |

- **A koordinátori prompt** leckénként: a slug, a brief helye (3. fejezet), a 4.2 sora (modulok + sorszámok), és a
  `lecke-utasitas.md`. Mivel nincs referencialecke, a prompt **ne** mondja „referencialecke vagy”.
- **Modulhiba:** a leckeügynök a saját példányában javít, és a metrikasorba írja (melyik modul, mi, hogyan) – a 17 lecke
  után egy egységesítő kör viszi vissza (mint a 7–8 EGYSEGESITES).
- **Költség** (kerethasználati jegyzet alapján): 17 × ~0,45 % ≈ **7,5–8 % heti keret**; a térképes és lektoros leckék
  inkább 45–60 perc ügynöki munka; két köteg ≈ 2 × 60–75 perc falióra.
- **QA-szűk keresztmetszet:** 10 párhuzamos Chromium-QA lassítja egymást (a headless `dt`-vágás miatt az animáció
  lassított) – a késői állapotokat `__lesson.st` közvetlen állításával fotózzák.

### 6.2 Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / fejlesztési feladat |
|---|---|---|
| 1. Civilizáció és államszervezet az ókorban (13) | 01, 02 | „A Közel-Kelet civilizációi” csak Hammurapi; Egyiptom (5–6), „Tudomány”, „A görög anyagi kultúra öröksége”, „A filozófia és a történetírás” (Platón, Arisztotelész csak forrásként), „A görög embereszmény”, „A hellenisztikus kultúra elterjedése” (Nagy Sándor, Alexandria), „Római városépítészet, amfiteátrumok, fürdők, vízvezetékek és utak”, „A latin nyelv és írás elterjedése”, Kr. e. 776, Kr. u. 70 (→ 03), 395 (→ 04) |
| 2. Vallások az ókorban (5) | 03 | bibliai történetek és művészeti alkotások gyűjtése (tevékenység) – tanári |
| 3. Hódító birodalmak (6) | 04 | „Az iszlám kultúra jellegzetességei” csak egy lépés; a monoteizmusok összevetése a 03-ban kezdődik, itt kitekintés |
| 4. A középkori Európa (10) | 05 | **„Az egyházi rend”** nagy része (szerzetesség – bencés, ferences –, eretnekség, inkvizíció, egyetemek, román és gótikus építészet), **„A nemesi rend”** lovagi kultúrája és **a keresztes hadjáratok eszméje**, a reneszánsz (Leonardo, Gutenberg), Dózsa György – csak egy-egy mondat vagy semmi (tartalék 1) |
| 5. A magyar nép eredete és az Árpád-kor (14) | 06, 07 | a kulturális alkotások (tabló) és Szent László kultusza (tevékenység) |
| 6. A középkori Magyar Királyság fénykora (13) | 08, 09 | „A magyar középkor kulturális hagyatéka” (honfoglalás kori leletek, várak, királyi udvar, geszták, krónikák, Képes krónika, Corvina) – csak említés (tartalék 2); „Mátyás és a budai zsidók” (tevékenység) |
| 7. A kora újkor (12) | 10, 11 | az abszolutizmus (XIV. Lajos, Versailles) csak egy mondat a 10-ben és utalás a 13-ban |
| 8. A török hódoltság kora Magyarország (10) | 12 | a végvári élet (5–6 `16-eger`), Báthory István lengyel királysága, „kulturális alkotások”; a mohácsi csata részletei (5–6 `15-mohacs`) |
| 9. A felvilágosodás kora (5) | 13 | a brit és amerikai államszervezet csak egy lépés (a 7–8 `16-demokracia` mélyebben) |
| 10. Magyarország a 18. században (10) | 14 | a Rákóczi-szabadságharc katonai története és nemzetközi kapcsolatai csak két lépés; „Gazdaság és életmód”, a 18. századi kulturális eredmények |
| 11. Az új eszmék és az iparosodás kora (5) | 15 | „A 19. századi demográfiai változások okainak feltárása” csak a Manchester-adatokon át |
| 12. A reformkor (10) | 16 | „A reformkori Pest-Buda” (5–6 `19-marcius-15`), a reformkor kulturális alkotásai (Kölcsey, Vörösmarty, Nemzeti Színház) csak említés |
| 13. A forradalom és a szabadságharc (8) | 17 | a tavaszi hadjárat részletei (5–6 `20-szabadsagharc`); mikrotörténeti életutak (tevékenység) |

**A forrásszöveg kinyerési hibái** (a `kerettanterv/tortenelem/9-10.md`-ben, javítás nélkül):
- A 8. témakör címe: „A török hódoltság kora Magyarország” – valószínűleg „…Magyarországon” (a forrás alakja, megtartva).
- A 2. témakör fogalomlistájában: „Tízparancsolat próféta” (hiányzó vessző), „diaszpóra,,” (dupla vessző); a táblázat
  után egy üres `**` / `**` sorpár.
- A 11. témakör fejlesztési feladataiban két szó elválasztójellel tört: „életkörülmé-” / „nyeinek” (két bekezdésre
  szakadva), „következmé-nyeinek”.
- A 6. témakör kronológiájában „kihalása,1308.” (hiányzó szóköz, pont az évszám után), „I.(Nagy)” (hiányzó szóköz);
  fogalomlistájában „fekete sereg,  zsoldos” (dupla szóköz). Az 5. témakörben „szászok,  kunok” (dupla szóköz).
- Több kronológia- és személylista két bekezdésre tört: 1. témakör („…70 Jeruzsálem lerombolása,” / „Kr. u. 395…”),
  7. („…1568 a tordai határozat,” / „1648 a vesztfáliai békék.”), 10. („Mária Terézia,” / „II. József.”).
- Az altémák egy része `<blockquote>`-ba csomagolva került a táblázatba (2., 3., 6., 7., 8., 10–13. témakör) – a
  DOCX-ből jövő behúzás nyoma, tartalmi hiba nincs.
- Az óraszámok összege 121, egyezik a forrás összesítőjével.

**Tartalék-jelöltek**, ha a sorozat folytatódik (fontossági sorrendben):
1. `18-egyhaz-lovag` – a középkori egyház és a lovagi kultúra: szerzetesrendek, egyetemek, keresztes hadjáratok
   (eszme, útvonal, következmény – méltósággal), román és gótikus építészet saját vázlatrajzokon (4.).
2. `19-kozepkori-hagyatek` – a magyar középkor kulturális hagyatéka: krónikák és geszták forráskritikája, a Képes krónika
   (leírás, kép nélkül), a Corvina sorsa (6.).
3. `20-hellenizmus` – Nagy Sándor birodalma és a hellenisztikus kultúra, Alexandria tudománya (1.).
4. `21-abszolutizmus` – XIV. Lajos és Versailles; a francia állam költségvetése a forradalom előtt (7., 9.).
5. `22-reformkori-kultura` – a reformkor kulturális intézményei és a nyilvánosság (lapok példányszáma, Nemzeti Színház,
   MTA) (12.).

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): az NKP *Történelem 9.* és *10.* digitális tankönyve; az MTA BTK
őstörténeti kiadványai és a Magyar Őstörténeti Témacsoport (2012–2016) összefoglalói; a Hadtörténeti Intézet 1848–49-es
térképei (jogvédett – csak egybevetésre). Nálunk a többlet: a működő modellek (szavazás, adózás, ár, futószalag), a
dátum szerint mozgó vázlatos térkép és a bizonyítékmátrix.

---

## 7. Szerződés-kiegészítés (kész szöveg a `leckek/SZERZODES.md`-hez)

A következő fejezet változtatás nélkül beillesztve a `SZERZODES.md` végére, a 20. (Történelem 7–8.) után (2026-11-25).

```markdown
## 21. Történelem-kiegészítés (9–10. évfolyam, gimnázium)

Történelemleckénél a 9–10. évfolyamon a fenti szabályok, a 11. (Történelem 5–6.) és a **20. (Történelem 7–8.)
fejezet** együtt érvényesek – ahol ez a fejezet mást mond, ez az irányadó. **Kötelező olvasmány:**
`pilot/tortenelem-9-10/terv.md` – a 0. fejezet (döntések), az 1.3 pont (szerkesztői elvek), a saját briefed (3. fejezet)
és a 4. fejezet (melyik modult melyik leckéből, melyik sorból másolod).

- **Mappa, fejléc:** `leckek/tortenelem-9-10/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Történelem · évfolyam: 9–10. · témakör: N. <a kerettanterv témakörének címe>`. Panel ≤ 55 szó (cél 40–50),
  spec `"sources": true`; a lektort kérő leckékben `"review": [...]` a terv 2. táblája szerint.
- **Elemző szint:** a vásznon egy *mechanizmus* működjön (szavazás, adózás, ár, népesség, jogkörök), és a diák a
  kapcsolóval/csúszkával a következményt lássa. Az 5–6. évfolyam kulcsvizuálját (a brief „Ne ismételd” sora) nem
  ismételjük. Adat, becslés és **modell** a vásznon is elválik: a lecke saját modellje „modell” bélyeget kap, és a lépés
  kimondja, mit hagy ki.
- **„Honnan tudjuk?” forráskritikával:** ki írta, mikor, milyen céllal, mennyivel az esemény után, mit nem tudhatott.
- **Vitatott kérdések** (őstörténet, honfoglalás, hun–magyar kapcsolat, kettős honfoglalás, Szent Korona-tan, létszám- és
  népességbecslések, mohácsi vereség, a francia forradalom mérlege, a szabadságharc veresége): **konszenzus / vitatott /
  nem igazolt** – három külön jelölés; vitánál legalább két nézőpont, értékítélet helyett forrás, adat, kérdés.
  Áltudományos állítás nem jelenhet meg tényként; ha szerepel, csak elvetettként, a cáfolattal. A nyelvrokonság nem
  genetikai rokonság; a krónikás hun–magyar azonosság „hagyomány” réteg.
- **Vallások tárgyilagosan:** leíró keret („a … hite / tanítása szerint”), egyik vallás sem értékelve vagy rangsorolva;
  szent szöveg és élő hagyomány: „hagyomány” réteg. Reformáció és katolikus megújulás kiegyensúlyozottan.
- **Erőszak méltósággal** (keresztes háborúk, inkvizíció, pogromok, rabszolgaság, gyarmatosítás, hódoltság, terror,
  megtorlás): a 20. fejezet szabályai szerint – nincs pontszám, effektus, animált számláló, vér, kitalált áldozati
  történet, „Tippelj!” áldozatszámra; csatát nem játszunk le (térkép, erőviszony, forrás).
- **Szerzői jog:** az ókori, középkori, kora újkori eredeti szöveg közkincs, de **a modern fordítása gyakran nem** – szó
  szerint csak az eredetiből készült **saját fordítás** (így jelölve, a megjegyzésben a felhasznált kiadással) vagy 1955-ben
  vagy előbb elhunyt fordító munkája idézhető; bizonytalanságnál parafrázis. Jogszabályszöveg † nélkül. Portré nincs
  (sziluett, pecsét, névkártya).
- **Térképek, határok:** 1914 előtti történeti határ **nincs** a `TORT_HATAR`-ban, új közös adatfájl nem készül. Ókori,
  középkori, kora újkori terület, hódoltság, front: **leckén belül rajzolt, lágy szélű sokszög** (`TortMap.region`),
  „vázlatos” bélyeggel és dátummal; a töréspontok helységnévvel a kódban, a kulcshelyek `coord`-ként az `### Adatok`
  alatt, a `.md` két egybevetett atlaszt nevez meg (geometriát onnan nem veszünk át). A középkori–kora újkori Magyar
  Királyság kerete a `mo1914hsz` csoporttal közelíthető, **„vázlatos – az 1914-es határral közelítve”** felirattal, az
  eltérések a `.md`-ben. Terület és népesség mindig az `### Adatok`-ból.
- **Színek:** háborús feleknél indigó `#3b4590` / szilva `#7d3a66` (+ egy harmadik semleges tónus sraffozással);
  népcsoportoknál, felekezeteknél egymáshoz hasonló semleges tónusok mintával – nincs „jó” és „rossz” szín. A TortState
  bordó „irányít” nyila itt egy kézbe vont hatalmat is jelölhet (princeps, forradalmi diktatúra) – a jelmagyarázat
  kimondja; a TortParl tónusai nem pártokat jelölhetnek (vagyoni osztály, követutasítás) – szintén kimondva.
- **Modulok:** **új közös modul nincs**, referencialecke nincs. Minden modult (TtTipp, TortTimeline, TortSource, TortMap,
  FoldChart, TortParl, TortState, TortTerr, TortCards, MatChart) **bájtra azonosan** a terv 4.1 táblája szerinti
  forrásleckéből veszel át, md5-tel ellenőrizve. Ami új rajz, modell vagy szimuláció, az leckén belüli kód, **MODUL-jelölés
  nélkül**, a modulblokkok után. Modulhibát a saját példányodban javíts, és írd a metrikasorba.
- **Számformátum:** a 20. fejezet szerint; ókori évszám „Kr. e. 508”, évszázad „Kr. e. 5. század közepe”, perjeles év
  („Kr. e. 508/507”, „1000/1001”) a szövegben, a `year` adat egy évet tartalmaz.
- **Kész, ha** (a 10. és a 20. fejezeten felül): [ ] a brief „Ne ismételd” sora teljesül; [ ] minden modell „modell” vagy
  „kitalált” bélyeges, és a lépés kimondja a korlátját; [ ] vitatott kérdésnél konszenzus / vitatott / nem igazolt jelölés
  és legalább két nézőpont; [ ] vallási tartalom leíró keretben; [ ] szó szerinti idézetnél a fordító is rendben (saját
  fordítás vagy † ≤ 1955); [ ] minden kézi sokszög „vázlatos”, dátumozott, töréspontjai kommentezve, két atlasz a `.md`-ben;
  [ ] a modulblokkok md5-je egyezik a terv 4.1 táblájával (vagy az eltérés a metrikasorban).
```
