# Pilot: Kémia 7–8. – a leckesor terve

Forrás: [`kerettanterv/kemia/7-8.md`](../../kerettanterv/kemia/7-8.md) (NAT 2020, általános
iskola, 6 témakör, 102 óra). Az idézetek szó szerint onnan valók; a forrás `<sub>`/`<sup>`
jelölését (H<sub>2</sub>O, Cl<sup>-</sup>) itt Unicode-dal írjuk (H₂O, Cl⁻). A lecke-formátum:
[`leckek/SZERZODES.md`](../../leckek/SZERZODES.md).

> A felhasználó a terv írásakor nem volt elérhető. A döntéseket indoklással rögzítjük
> (**Döntés:** jelölés), hogy átnézéskor egyenként felülbírálhatók legyenek.

## 1. Bevezető

A pilot **14 leckéje** a 7–8. osztályos kémia-kerettanterv mind a 6 témakörét lefedi. A
formátum ugyanaz, mint a fizikánál: 7–9 lépés, 1920×1080-as színpad, bal oldalt animáció vagy
szimuláció, jobb oldalt magyarázó panel, világos, papírszerű háttér. Célcsoport: 13–14 évesek,
panelszöveg ≤ 55 szó lépésenként.

**Hol ad egy interaktív animáció valódi belátást a kémiában?** A kerettanterv maga mondja ki a
fő célt: „A kémiai szimbólumok (vegyjelek, képletek, reakcióegyenletek) és azok jelentésének
tanítása háttérbe szorul az anyagok és folyamatok makroszintű és részecskeszintű értelmezésével
szemben.” A tankönyv ezt állóképekkel próbálja megoldani, a videó pedig csak a makroszintet
mutatja. Szerintünk öt helyzetben ad többet egy animáció:

1. **Makroszint ↔ részecskeszint egyszerre.** A fecskendő, a pohár vagy a sókristály mellett
   egy **nagyító** mutatja ugyanazt a pillanatot részecskeszinten, szinkronban. A diák a
   csúszkát a makroszinten húzza (melegít, összenyom, önt), és a részecskéken látja a
   következményt. Ez a lecke-sorozat vezérmotívuma: a három szint (makro, részecske, jel)
   **minden leckében ugyanazzal a vizuális kóddal** jelenik meg (lásd 5. fejezet).
2. **Modellalkotás mint folyamat.** Kísérlet → tapasztalat → magyarázat (a kerettanterv első
   tanulási eredménye). A modellt a diák szeme előtt építjük fel és vetjük el. Például a
   gyertyás oxigénmérés hibás, a modell mégis jó, ha tudjuk a korlátját. A modellek
   korlátait mindig kimondjuk („szemléltetés: a méretek nem arányosak”).
3. **A reakció mint átrendeződés.** Az atomok megtartják a színüket és a számukat, csak a
   kötések bomlanak fel és jönnek létre. A tömegmegmaradás így nem szabály, hanem *látszik*. A
   reakció feltételei (ütközés, energia, katalizátor) szimulációban kipróbálhatók: lassú
   részecskék lepattannak, gyorsak reagálnak.
4. **Láthatatlan szerkezet → látható tulajdonság.** A héjak elektronszámából jön az ion töltése,
   a kötés fajtájából a rács, a rácsból az olvadáspont és a vezetés. Ugyanez a csúszka-elv:
   melegítsd a négy kristályt, és nézd meg, melyik esik szét előbb.
5. **Valódi adatsorok.** Oldhatósági görbék, a szénhidrogének forráspontja a lánchossz
   függvényében, pH-értékek, a levegő összetétele. A görbét a diák maga „járja be”; a számok a
   tartalomfájlból jönnek, és egy tanár javíthatja őket.

**Kihagyjuk** azt, amiből csak illusztrált szöveg vagy lista lenne: a laboratóriumi eszközök és a
balesetvédelmi szabályok felsorolását (a lab-eszközök a leckékben helyes használatban
*szerepelnek*, de nincs róluk külön lecke), a veszélyességi jelek katalógusát (a 10-ben és a
13-ban egy-egy valódi címkén szerepelnek), a vegyjel-játékokat és a memóriakártyákat, a
kiselőadás-, poszter- és vitatémákat, valamint a káros szenvedélyek, a gyógyszerek és a drogok
témáját. Ez utóbbiak prevenciós és nevelési kérdések; egy animáció itt könnyen
bagatellizálhat vagy éppen vonzóvá tehet, ezért ezeket tanórai beszélgetésre hagyjuk.

**Kiválasztási elv.**

1. **Arányosság:** 102 óra / 14 lecke ≈ 7,3 óra leckénként. A 17 órás 1. és 2. témakör
   kettőt-kettőt kap, a 20 órás 4. témakör hármat, a 15 órás 5. kettőt, a 19 órás 6. kettőt.
   **Döntés:** a 14 órás 3. témakör (Atomok, molekulák, ionok) arányán felül **hármat** kap, a 6.
   témakör egyet „veszít”. Indoklás: a kerettanterv bevezetője ezt nevezi a szakasz „fő
   csomópontjának”, és ez a legláthatatlanabb, tehát a legjobban animálható anyag. A 6.
   témakör óráinak nagy része címkeolvasás, egészségnevelés és vita, ezekhez nem kell animáció.
2. **Ahol a tanterv maga is animációt kér:** „A diffúziót részecskeszemlélet alapján bemutató
   … animáció” (2.), „A halmazállapot-változással kapcsolatos videofilmek megtekintése és
   értelmezése a részecskeszemlélet alapján” (1.), „A kőolaj feldolgozásával kapcsolatos idegen
   nyelvű animáció szöveges narrációja” (6.), „Atomszerkezeti modellező játékok” (3.). Ezek
   biztosan bekerülnek (01, 05, 14).
3. **Építőkockák újrahasznosítása:** a 14 lecke 8 közös modulra épül (4. fejezet). Ez a
   sorozat építi a projekt **részecskemotorját**, amelyet a biológia (diffúzió, ozmózis) és a
   fizika (gázok, halmazállapotok) is használhat.
4. **Átfedés a fizikával:** a fizika 7–8. sorozat `06-halmazallapot` (olvadás- és
   forrásplató), `01-suruseg` és `14-uveghaz` leckéje már kész. A kémia ezeket nem ismétli,
   hanem hivatkozik rájuk (`> megjegyzés:`), és a kémiai oldalt hangsúlyozza: szublimáció,
   elegyedés, a molekulán belüli és a molekulák közötti kötés különbsége, az ózon és a savas
   eső.

A leckék sorszáma a kerettanterv sorrendjét követi; a **gyártási sorrend** ettől eltér
(4. fejezet). Az „Adatok” pontokban szereplő számok a tartalomfájl `### Adatok` rétegébe
kerülnek. A *(frissítendő)* jelzésű értékek évről évre változnak, az *(ellenőrizendő)*
jelzésűekhez a gyártó ügynöknek forrást kell keresnie és a `.md` `<!-- -->` megjegyzésébe
írnia.

## 2. A leckék

| # | slug | cím | témakör | építőkocka | nehézség (1–3) |
|---|---|---|---|---|---|
| 01 | `01-reszecskemodell` | Mi van a fecskendőben? – kísérlet, tapasztalat, golyómodell | 1 (+2) | **A**, G, Tx | 3 |
| 02 | `02-szetvalasztas` | Hogyan válogatjuk szét a keveréket? – elválasztási műveletek | 1 | G, A | 2 |
| 03 | `03-elem-vegyulet-keverek` | Tiszta anyag-e a csapvíz? – elem, vegyület, keverék | 2 | B, G, A | 2 |
| 04 | `04-oldodas` | Hová tűnik a cukor a teában? – oldódás, oldhatóság, oldatok | 2 | A, B, G, Gr | 3 |
| 05 | `05-atom-hejak` | Milyen az atom belülről? – atommag, elektronhéjak, periódusos rendszer | 3 | **C**, **D**, **Tx** | 3 |
| 06 | `06-molekulak` | Miért H₂O, és miért nem HO? – molekulák, közös elektronpár | 3 | **B**, C, Tx | 3 |
| 07 | `07-ionok-kristalyok` | Miért nem olvad meg a só a serpenyőben? – ionok és kristályrácsok | 3 | C, B, Tx | 2 |
| 08 | `08-kemiai-reakcio` | Hová lesz a gáz a tűzhelyen? – a kémiai reakció mint átrendeződés | 4 | F, A, B, Tx, Gr | 3 |
| 09 | `09-eges-korrozio` | Mi a közös a csillagszóróban és a rozsdás szögben? – égés és korrózió | 4 | F, G, B | 2 |
| 10 | `10-sav-bazis` | Mit mutat a lilakáposzta-lé? – savak, lúgok, pH, közömbösítés | 4 | H, A, G, Gr | 2 |
| 11 | `11-levego` | Mi van a levegőben, és mi kerül bele? – légkör, savas eső, ózon, szmog | 5 | A, B, H | 2 |
| 12 | `12-viztisztitas` | Tiszta-e, ami átlátszó? – természetes vizek és víztisztítás | 5 | G, A | 2 |
| 13 | `13-szappan-vizkemenyseg` | Hogyan viszi el a szappan a zsírt? – mosószerek és vízkeménység | 6 | B, A, G | 2 |
| 14 | `14-koolaj` | Mi lesz a kőolajból? – szénhidrogének, lepárlás, műanyag | 6 (+5) | B, G, Gr, Tx | 2 |

Építőkockák (4. fejezet): **A** részecskemotor · **B** molekula-rajzoló · **C** atommodell ·
**D** periódusos rács · **F** reakció-réteg · **G** labor + nagyító · **H** pH és indikátor ·
**Tx** képletírás a vásznon · **Gr** grafikonrajzoló (a fizika-sorozatból). Vastagon: ott épül
meg először.

Nehézség = gyártási nehézség: 1 = kevés elem; 2 = egy közepes szimuláció vagy új modul; 3 =
valódi részecskeszimuláció, új alapmodul vagy kényes pontosság.

Témakörönként: 1 → 2 · 2 → 2 · 3 → 3 · 4 → 3 · 5 → 2 · 6 → 2.

---

## 3. Briefek

### 01 · `01-reszecskemodell` – Mi van a fecskendőben? – kísérlet, tapasztalat, golyómodell

*Referencialecke: a részecskemotor (A) és a nagyító (G) első megépítése.*

- **Tanulási cél:** A kísérlet, a tapasztalat és a magyarázat három különböző dolog. A
  golyómodell (apró, mozgó részecskék, köztük üres tér) egyszerre magyarázza, hogy a levegő
  összenyomható, a víz nem; hogy a szag lassan terjed; és hogy 50 cm³ alkohol meg 50 cm³ víz
  együtt kevesebb, mint 100 cm³. A melegebb anyagban gyorsabban mozognak a részecskék.
- **Kerettanterv:** „megkülönbözteti a kísérletet, a tapasztalatot és a magyarázatot” ·
  „egyszerű modelleket (golyómodellt) használ az anyagot felépítő kémiai részecskék
  modellezésére” · „ismeri a halmazállapot-változásokat, konkrét példát tud mondani a
  természetből (légköri jelenségek) és a mindennapokból” · „A részecskeszint és a makroszint
  megkülönböztetése” · „Hipotézisalkotás alapvető szinten” · tevékenységek: „a levegő vizsgálata
  műanyag fecskendős kísérletben” · „Endoterm és exoterm folyamatok (pl. az alkohol és a víz
  elegyedésének) követése hőmérsékletméréssel/termoszkóppal” · „a kámfor és a mentol
  szublimációjának vizsgálata” · (2.) „A diffúziót szemléltető tanulókísérletek elvégzése”.
- **Tévhitek:** A levegő „semmi”, az üres fecskendőben nincs semmi. A részecskék között levegő
  van (és nem üres tér). Melegítéskor a részecskék megnőnek. Ha a gázrészecskék 470 m/s-mal
  száguldanak, a parfümillatnak azonnal át kellene érnie a termen. A térfogatok mindig
  összeadódnak. A modell a valóság kicsinyített fényképe.
- **Kulcsvizuál:** bal oldalt egy nagy, átlátszó fecskendő (makroszint), a dugattyú húzható. Egy
  kúp alakú nagyító vezet a jobb oldali kör alakú „részecskeablakba”, ahol ugyanaz a térfogat
  részecskékkel látszik. Ha a dugattyút benyomjuk, a levegős fecskendőben a részecskék
  közelebb kerülnek egymáshoz, a vizesben nincs hová. Alul egy háromlépcsős sáv:
  **kísérlet → tapasztalat → magyarázat**. Mindig az aktuális szint világít.
- **Interaktív:** a dugattyú húzható (levegő / víz / homok választható). A hőmérséklet
  csúszkával állítható (−20…+100 °C), és ettől látványosan gyorsulnak a részecskék. A „Parfüm!”
  gomb egy színes részecskecsomót enged el; egy kapcsolóval ki lehet kapcsolni az
  ütközéseket, és akkor a parfüm egy pillanat alatt átér: így látszik, hogy az ütközések
  lassítják. Az elegyítésnél egy „borsó + mák” makromodell mellett ott vannak az
  alkohol- és a vízrészecskék.
- **Lépések (9):** Mi van az „üres” fecskendőben? (hipotézis) · Kísérlet: összenyomom –
  levegő, víz, homok (tapasztalat) · Magyarázat: részecskék és üres tér · Szilárd, folyékony,
  légnemű a nagyítóban · Melegebb = gyorsabb · Ilyen gyors, mégis lassú a szag? – a diffúzió ·
  50 + 50 ≠ 100: alkohol és víz · A halmazállapot-változások köre: szublimáció, dér, endoterm és
  exoterm · Összefoglalás: a modell eszköz, nem fénykép.
- **Adatok:** 20 °C-on a nitrogénmolekulák átlagsebessége ≈ 470 m/s (oxigén ≈ 440 m/s,
  hidrogén ≈ 1760 m/s; v̄ = √(8RT/πM)). Közepes szabad úthossz a levegőben ≈ 66 nm, ebből
  másodpercenként ≈ 7 milliárd ütközés jut egy molekulára. A levegőben a részecskék átlagosan
  kb. 10–11 molekulaátmérőnyire vannak egymástól (a folyékony vízben kb. 1330-szor több
  részecske van egységnyi térfogatban, köbgyöke ≈ 11). Fecskendő: 20 cm³ levegő 10 cm³-re
  nyomva a nyomás kétszeresére nő (Boyle–Mariotte); a víz kb. 0,005 %-kal nyomódik össze
  1 bar többletnyomásra (kompresszibilitás 4,6·10⁻¹⁰ 1/Pa), vagyis gyakorlatilag nem
  nyomható össze. Elegyítés 20 °C-on: 50 cm³ etanol (0,789 g/cm³) + 50 cm³ víz (0,998 g/cm³)
  = 89,4 g, 44 tömeg%-os elegy, sűrűsége ≈ 0,926 g/cm³, **térfogata ≈ 96,5 cm³** (≈ 3,5 %
  kontrakció). A hőmérséklet-emelkedés néhány °C (≈ 3–6 °C, az edénytől függ)
  *(ellenőrizendő: mérési adat kell, a számolt adiabatikus érték ≈ 6–8 °C)*. Szárazjég (CO₂)
  légköri nyomáson −78,5 °C-on szublimál; a jód 113,7 °C-on olvad, de már enyhe melegítésre
  lila gőzt ad. Endoterm: olvadás, párolgás, forrás, szublimáció; exoterm: fagyás,
  lecsapódás, gáz → szilárd (dér).
- **Szóhasználat (ellenőrizendő a tanári review-ban):** a gáz → szilárd átalakulás neve a
  magyar tankönyvekben nem egységes („kristályosodás” vagy „deszublimáció”). A felirat a
  `.md`-ből jön, a tanár átírhatja.
- **Építőkocka:** A (részecskemotor: dugattyú, hőmérséklet, két részecskefajta, ütközés
  ki/be), G (fecskendő, nagyító), Tx (CO₂ felirat).
- **Meglévő anyag:** PhET *States of Matter*, *Gas Properties*, *Diffusion*. Nálunk a hangsúly a
  kísérlet → tapasztalat → magyarázat láncon, az elegyedési kontrakción és azon van, hogy miért
  lassú a diffúzió a gyors részecskék ellenére.
- **Kapcsolat:** az olvadás- és forráspontos platót a fizika `06-halmazallapot` lecke mutatja
  meg, erre a 8. lépés megjegyzése hivatkozik.

### 02 · `02-szetvalasztas` – Hogyan válogatjuk szét a keveréket? – elválasztási műveletek

- **Tanulási cél:** A keverékben minden alkotórész megtartja a saját tulajdonságait, és az
  elválasztás mindig egy *különbséget* használ ki: sűrűséget, részecskeméretet, oldhatóságot,
  mágnesességet vagy forráspontot. Oldás után a só átjut a szűrőn, mert a részecskéi
  sokkal kisebbek a pórusoknál.
- **Kerettanterv:** „tudja, hogy a keverékek alkotórészeit az alkotórészek egyedi tulajdonságai
  alapján választhatjuk szét egymástól, ismer konkrét példákat az elválasztási műveletekre (pl.
  bepárlás, szűrés, ülepítés)” · „Elválasztási műveletek” · tevékenységek: „Háromkomponensű
  (konyhasó−homok−vaspor) keverék szétválasztásának megtervezése, a várható tapasztalatok
  megbecsülése, a vizsgálat csoportokban történő megvalósítása, a tapasztalatok összevetése az
  előzetes elképzeléssel, a következtetések levonása” · „A víz vagy vörösbor desztillációjának
  bemutatása, a desztilláció folyamatának értelmezése” · „Alkoholos filctollak festékanyagainak
  elválasztása papírkromatográfiával”.
- **Tévhitek:** A szűrő a feloldott sót is visszatartja. Ha a só feloldódik, eltűnik, és nem
  lehet visszanyerni. Desztilláláskor az alkohol elég vagy elfogy. Egyszeri lepárlással tiszta
  alkohol lesz. A fekete filctoll tinta egyetlen festékből áll.
- **Kulcsvizuál:** egy „szétválasztó asztal” a só–homok–vaspor keverékkel és öt eszközzel
  (mágnes, víz + üvegbot, tölcsér szűrőpapírral, bepárlócsésze borszeszégővel, ülepítőpohár).
  Minden eszköz fölött kis nagyítóablak mutatja, *miért* működik: a szűrőpapír pórusai a
  homokszemhez képest szűkek, a nátrium- és a kloridionokhoz képest óriási kapuk.
- **Interaktív:** **„Tervezd meg!”** – a diák sorba állítja a műveleteket (kártyák). Rossz
  sorrendnél a szimuláció megmutatja a következményt: ha a mágnes az oldás után jön, a vaspor
  nedves és rozsdásodni kezd; ha a szűrés az oldás előtt, a só a homokkal marad. A
  desztilláló készüléknél a melegítés csúszkával állítható, és élő hőmérő mutatja a
  gőz hőmérsékletét (78 °C körüli plató, aztán 100 °C felé).
- **Lépések (9):** Keverék: mindenki marad, ami volt · Ülepítés és dekantálás · Szűrés: mi fér
  át? · Bepárlás: visszajön a só · Mágnes · Tervezd meg: só, homok, vaspor · Desztilláció:
  a forráspont dönt · Papírkromatográfia: hány festék van a filctollban? · Összefoglalás:
  melyik tulajdonságot használtuk?
- **Adatok:** sűrűség: homok (kvarc) 2,65 · konyhasó 2,16 · vas 7,87 g/cm³. A konyhasó
  oldhatósága 20 °C-on ≈ 36 g/100 g víz; a homok és a vas gyakorlatilag nem oldódik. A
  szűrőpapír pórusmérete ≈ 2–25 µm (laboratóriumi minőségtől függően); a homokszemek
  0,06–2 mm-esek; a Na⁺- és a Cl⁻-ion átmérője ≈ 0,2–0,4 nm, vagyis a pórus
  ≈ 5000–100 000-szer nagyobb. Forráspont (1013 hPa): etanol 78,4 °C, víz 100 °C. Az
  etanol–víz elegy 95,6 tömeg%-nál (78,2 °C) azeotróp, ennél töményebb egyszerű lepárlással
  nem lesz. Bor ≈ 12 térfogat% alkohol; a pálinka legalább 37,5 térfogat%
  *(ellenőrizendő: a pálinkatörvény hatályos szövege)*. Tengervíz ≈ 35 g só/kg.
- **Biztonság:** a desztilláció *tanári bemutató*; az alkoholgőz gyúlékony. Az otthoni
  pálinkafőzésről a lecke nem ad útmutatót, a `.md` megjegyzésben ez szerepel. A bepárlás
  otthon is elvégezhető (sós víz, lábasban).
- **Építőkocka:** G (eszközök: tölcsér, szűrő, bepárlócsésze, desztilláló Liebig-hűtővel,
  mérőhenger, mágnes), A (részecskék a szűrő pórusánál), kártyák (sorba rendezés, ezt a
  történelem `TortCards`-ból emeljük át).
- **Meglévő anyag:** kevés jó interaktív anyag van; a PhET-ben nincs elválasztás. Az NKP
  tankönyvekben állóképek vannak.

### 03 · `03-elem-vegyulet-keverek` – Tiszta anyag-e a csapvíz? – elem, vegyület, keverék

- **Tanulási cél:** Részecskeszinten dől el, mi az elem (egyféle atom), mi a vegyület (többféle
  atom, kötött, állandó arányban) és mi a keverék (többféle részecske, változó arányban,
  kötés nélkül). A vegyület tulajdonságai mások, mint az alkotó elemeié. Ugyanaz az anyag
  ugyanolyan, akár természetes, akár mesterséges.
- **Kerettanterv:** „különbséget tesz elem, vegyület és keverék között” · „tudja, hogy melyek az
  anyag fizikai tulajdonságai” · „tudja és érti, hogy attól még, hogy egy elem vagy vegyület
  mesterségesen került előállításra vagy természetes úton került kinyerésre, még ugyanolyan
  tulajdonságai vannak, ugyanannyira lehet veszélyes vagy veszélytelen, mérgező vagy
  egészséges” · „Példák bemutatása a köznapi életből elemre (pl. grafit, vörösréz, kén),
  vegyületre (pl. víz, nátrium-klorid, szőlőcukor) és keverékre (pl. benzin, levegő,
  sárgaréz)”.
- **Tévhitek:** A víz hidrogén és oxigén keveréke. Az elem mindig egyedülálló atomokból áll (az
  O₂ ezért „vegyület” lenne). A tiszta anyag az, ami átlátszó, vagy amin nincs piszok. A
  „vegyszermentes” vagy „természetes” termék biztosan egészségesebb. A mesterséges C-vitamin
  „más”, mint a citromban lévő.
- **Kulcsvizuál:** kilenc anyagminta a polcon (grafit, vörösréz, kén, víz, konyhasó,
  szőlőcukor, levegő, sárgaréz, benzin). Egy húzható nagyító mutatja a részecskéiket (kén:
  S₈-gyűrűk, oxigén: O₂-párok, réz: fémrács, levegő: N₂, O₂, Ar vegyesen). Mellette egy
  háromágú fa: **tiszta anyag** (elem | vegyület) | **keverék**.
- **Interaktív:** a minták a fára húzhatók (azonnali visszajelzés a nagyító képével). A
  **„Keverék vagy vegyület?”** lépésben két tartály van: H₂ + O₂ keverék és víz; a
  csúszkával az arány változtatható. A keveréknél bármilyen arány lehet, a víznél mindig
  2 : 1. Gombbal egy „szikra” mutatja, hogy a keverék *más* (éghető), mint a víz. A szikra
  csak szemléltetés, a jelenet „NE PRÓBÁLD KI” bélyeget kap.
- **Lépések (9):** Tiszta anyag vagy keverék? · Nagyító: egyféle részecske = tiszta anyag ·
  Elem: egyféle atom (az O₂ is elem) · Vegyület: többféle atom, kötve, állandó arányban ·
  Vegyület ≠ keverék: hidrogén + oxigén kontra víz · Keverék: változó összetétel (levegő,
  sárgaréz, benzin) · Válogasd szét! · Természetes vagy mesterséges? · Összefoglalás: a fa.
- **Adatok:** a levegő (száraz, térfogat%): N₂ 78,08 · O₂ 20,95 · Ar 0,93 · CO₂ ≈ 0,04
  *(frissítendő, lásd 11)*. Vízbontáskor a hidrogén és az oxigén térfogataránya 2 : 1.
  Sárgaréz: réz + cink, kb. 60–70 % réz; bronz: réz + ón. Kén: S₈-gyűrű, olvadáspont
  115 °C. Ismert elemek száma 118 (a legutóbbi négyet 2016-ban nevezték el). A C-vitamin
  (aszkorbinsav, E300) képlete C₆H₈O₆, akár citromból, akár gyárból származik.
- **Építőkocka:** B (molekula- és rácsrajz golyómodellel), G (nagyító, polc), A (levegő mint
  mozgó keverék).
- **Meglévő anyag:** PhET *Build a Molecule* (csak részben).

### 04 · `04-oldodas` – Hová tűnik a cukor a teában? – oldódás, oldhatóság, oldatok

- **Tanulási cél:** Oldódáskor az oldószer részecskéi kiszakítják az oldandó anyag részecskéit a
  kristályból, és szétosztják őket maguk között. Az anyag nem tűnik el, a tömeg megmarad. Egy
  adott hőmérsékleten csak meghatározott mennyiség oldódik (telített oldat); az oldhatóság
  anyagonként másképp függ a hőmérséklettől. Az oldatok összetételét tömegszázalékkal adjuk
  meg. A kolloid részecskék nagyobbak, és szórják a fényt.
- **Kerettanterv:** „a részecskemodell alapján értelmezi az oldódást” · „részecskeszemlélettel
  értelmezi az oldódás folyamatát és az oldatok összetételét” · „példát mond a valódi oldatra és
  a kolloid oldatra” · tevékenységek: „Egyszerű oldási kísérletek a „Mi miben oldódik?” kérdés
  eldöntésére, pl. vas, konyhasó, répacukor és jód oldódásának vizsgálata vízben, alkoholban és
  benzinben” · „Grafikonok és táblázatok adatainak elemzése a különböző anyagok oldhatóságával,
  valamint egy anyag különböző hőmérsékleten való oldhatóságával kapcsolatban” · „Az oldás
  sebességét befolyásoló tényezők kísérleti úton történő vizsgálata” · „Nagyon egyszerű
  számítási feladatok elvégzése a tömegszázalék köréből” · „Szövegkeresés és -értelmezés a
  fiziológiás sóoldat összetételéről és szerepéről az orvosi gyakorlatban”.
- **Tévhitek:** A cukor „elolvad” a vízben (az oldódás és az olvadás összekeverése, ez az egyik
  legjobban dokumentált tévhit). Az oldat tömege kisebb, mint az összetevőké. A feloldott só a
  pohár aljára ül, csak nem látszik. Ha keverem, *több* oldódik (pedig csak *gyorsabban*).
  Melegítve minden jobban oldódik (a gázok rosszabbul, a konyhasó alig jobban). 9 g só +
  1000 g víz = 0,9 %-os oldat.
- **Kulcsvizuál:** egy kockacukor egy pohár vízben, mérlegen. A nagyítóban a vízmolekulák
  ütköznek a kristály szélével, és molekulánként leszakítják a cukrot. A konyhasónál a
  nátrium- és a kloridionokat a vízmolekulák körbeveszik (a víz „töltéses vége” felé
  fordulva). A mérleg kijelzője végig ugyanazt mutatja.
- **Interaktív:** csúszkák: hőmérséklet, keverés, szemcseméret (kockacukor / kristálycukor /
  porcukor). Az oldódás *sebessége* nő, a *végső mennyiség* csak a hőmérséklettől függ. Egy
  „Még egy kanál!” gomb addig ad sót, amíg az oldat telítetté nem válik: ekkor a nagyítóban
  ugyanannyi ion szakad le, mint ahány visszakötődik. Az oldhatósági grafikonon (konyhasó,
  kálium-nitrát, oxigén) a pont húzható; ha lehűtjük, a KNO₃-oldatból kristályok válnak ki. A
  tömegszázalék-mérleg két serpenyőjébe só és víz tehető. A Tyndall-lépésben a fénysugár
  sóoldaton, tejen és ködön megy át.
- **Lépések (9):** Eltűnt a cukor? – a mérleg nem hazudik · Oldódás ≠ olvadás: a nagyítóban ·
  Mi miben oldódik? (jód vízben és benzinben) · Gyorsabban, de nem többet · Telített oldat:
  ennyi fér bele · Oldhatóság és hőmérséklet: a görbék · Tömegszázalék: a fiziológiás
  sóoldat · Oldat vagy kolloid? – a fény útja · Összefoglalás.
- **Adatok** (oldhatóság, g / 100 g víz):

  | °C | 0 | 20 | 40 | 60 | 80 | 100 |
  |---|---|---|---|---|---|---|
  | konyhasó (NaCl) | 35,7 | 35,9 | 36,4 | 37,1 | 38,0 | 39,2 |
  | kálium-nitrát (KNO₃) | 13,3 | 31,6 | 63,9 | 110 | 169 | 246 |
  | répacukor (szacharóz) | 179 | 204 | 238 | 287 | 362 | 487 |

  *(ellenőrizendő: a NaCl tizedesjegyei forrásonként ±0,2-vel eltérnek; a KNO₃ és a szacharóz
  standard táblázati értékek, pl. CRC Handbook vagy a Négyjegyű függvénytáblázatok.)*
  Oldott oxigén levegővel telített vízben: 0 °C 14,6 · 10 °C 11,3 · 20 °C 9,1 · 30 °C
  7,6 mg/L. Jód: vízben ≈ 0,03 g/100 g (20 °C), alkoholban és benzinben sokkal jobban (barna,
  illetve lila oldat). Fiziológiás sóoldat: 0,9 tömeg% NaCl (9 g só + 991 g víz; a 9 g só +
  1000 g víz csak 0,89 %). A telített sóoldat 20 °C-on ≈ 26,4 tömeg% (35,9/135,9). Valódi
  oldat: részecskeméret < 1 nm; kolloid: ≈ 1–500 nm (tej: zsírcseppek és fehérjék, köd,
  füst, zselé, majonéz).
- **Biztonság:** a Tyndall-kísérletnél a lézermutató sugara ne kerüljön senki szemébe (ez a
  `> megjegyzés:` része).
- **Építőkocka:** A (oldódás: kristály + oldószer, leszakadás és visszakötődés; két
  részecskefajta), B (vízmolekula irányítással), G (pohár, mérleg, fénysugár), Gr
  (oldhatósági görbe).
- **Meglévő anyag:** PhET *Sugar and Salt Solutions*, *Concentration*. Nálunk az „oldódás ≠
  olvadás” és a „gyorsabban, de nem többet” kép kap hangsúlyt.

### 05 · `05-atom-hejak` – Milyen az atom belülről? – atommag, elektronhéjak, periódusos rendszer

*Referencialecke: az atommodell (C), a periódusos rács (D) és a vásznon használt képletírás
(Tx) első megépítése.*

- **Tanulási cél:** Az atom szinte teljesen üres: egy apró, nehéz atommagból (protonok,
  neutronok) és körülötte az elektronburokból áll. A protonok száma (a rendszám) dönti el,
  melyik elemről van szó. Az elektronok héjakon helyezkednek el (2, 8, 8 …). A periódusos
  rendszer sora megmutatja a héjak számát, az oszlopa a külső elektronok számát, és az azonos
  oszlopban lévő elemek hasonlóan viselkednek.
- **Kerettanterv:** „tudja, hogy az atom atommagból és elektronburokból épül fel” · „fel tudja
  írni a kisebb atomok elektronszerkezetét a héjakon lévő elektronok számával (Bohr-féle
  atommodell)” · „különbséget tesz elemi részecske és kémiai részecske, valamint atom, molekula
  és ion között” · „ismeri a legfontosabb elemek vegyjelét” · „Az atomok periódusos rendszere” ·
  tevékenységek: „Atomszerkezeti modellező játékok keresése az interneten” · „A lángfestés
  jelenségének elvégzése vagy bemutatása, kapcsolat keresése a tűzijátékokkal” · „az atomok
  méretviszonyainak megfigyelése”.
- **Tévhitek:** Az atom kicsi, tömör golyó. Az elektronok bolygóként, pontos körpályán
  keringenek (a Bohr-modell korlátját ki kell mondani). A neutronszám dönti el, milyen elem az
  atom. A periódusos rendszer önkényes táblázat, amit „be kell magolni”. Az atom színes (a
  golyómodell színei kódok, nem valódi színek).
- **Kulcsvizuál:** egy „végtelen zoom” egy sókristálytól az atomig, közben léptékcsíkkal (1 mm
  → 1 µm → 1 nm → 0,1 nm). Az atom középen egy 3D-hatású nukleonkupac (az `iskola`
  maghasadás-leckéjének golyóstílusával), körülötte koncentrikus héjak forgó elektronokkal; a
  külső héj kiemelt színű. Jobbra a periódusos rendszer első négy sora; a kiválasztott elem
  cellája összeköttetésben van az atomrajzzal.
- **Interaktív:** a rendszám csúszkával vagy a táblázat celláira kattintva választható
  (Z = 1–20, a 21–36 csak cellaként, „a héjszerkezet bonyolultabb” megjegyzéssel). A
  protonok, a neutronok és az elektronok egyenként is hozzáadhatók („atomépítő”): ha a
  protonszám változik, az elem is megváltozik; ha csak a neutronszám, ugyanaz az elem marad. A
  lángfestésnél egy elemre kattintva a láng színe megváltozik, és a külső elektron „felugrik”
  majd visszaesik.
- **Lépések (8):** Milyen kicsi? – zoom a sókristálytól az atomig · Mag és burok: szinte üres ·
  Proton, neutron, elektron – a rendszám · Héjak: 2, 8, 8 · A periódusos rendszer: sor = héjak,
  oszlop = külső elektronok · Családok: alkálifémek, halogének, nemesgázok · Lángfestés: a
  külső elektron és a tűzijáték · Összefoglalás.
- **Adatok:** Az atom átmérője ≈ 0,1–0,5 nm. A hidrogénatom (≈ 0,106 nm) kb. 60 000-szer
  nagyobb, mint a magja (proton ≈ 1,7 fm): ha a mag egy 1 mm-es mákszem lenne, az atom
  ≈ 60 m-es lenne (fél focipálya). A szénatomnál ez az arány ≈ 30 000–60 000 (a
  sugárdefiníciótól függ). A tömeg több mint 99,9 %-a a magban van; a proton tömege az
  elektronénak ≈ 1836-szorosa. Elektronszerkezet (Z ≤ 20): H 1 · He 2 · Li 2,1 · C 2,4 ·
  N 2,5 · O 2,6 · F 2,7 · Ne 2,8 · Na 2,8,1 · Mg 2,8,2 · Al 2,8,3 · Cl 2,8,7 · Ar 2,8,8 ·
  K 2,8,8,1 · Ca 2,8,8,2. Lángfestés: lítium kárminvörös (670,8 nm), nátrium sárga (589 nm),
  kálium fakóibolya, kalcium téglavörös, stroncium bíborvörös, bárium fakózöld, réz
  kékeszöld. Mengyelejev táblázata 1869. 118 elem, 7 periódus, 18 csoport.
- **Csoportjelölés – Döntés:** a cellák fölött az IUPAC szerinti 1–18-as számozás áll, mellette
  zárójelben a magyar iskolai főcsoportjelölés (I.A … VIII.A). Mindkettő felirat a `.md`-ben,
  így a tanár az egyiket elhagyhatja. A csoportnevek (alkálifémek, alkáliföldfémek, földfémek,
  halogének, nemesgázok) a kerettanterv fogalmai.
- **Modell-őszinteség:** a lángfestésnél a nátrium sárga fénye valójában a külső héjon belüli
  állapotváltás. A panel így mondja: „a külső elektron magasabb energiájú állapotba kerül (a
  rajzon: kijjebb)”, és a `.md` megjegyzésében ott a pontosítás. A héjak körpályája
  szemléltetés; ezt a 2. lépés kimondja.
- **Biztonság:** lángfestés: tanári bemutató, a báriumsók mérgezőek – „NE PRÓBÁLD KI otthon”.
- **Építőkocka:** C (Bohr-atom, nukleonkupac, héjak, elektronanimáció), D (periódusos rács +
  elemadatok), Tx (vegyjelek, ionjelek), zoom-léptékcsík.
- **Meglévő anyag:** PhET *Build an Atom* – nagyon jó, magyarul is van. Nálunk a hangsúly a
  léptéken (szinte üres atom), a táblázat és a héjak közvetlen kapcsolatán és a lángfestésen
  van.

### 06 · `06-molekulak` – Miért H₂O, és miért nem HO? – molekulák, közös elektronpár

*Referencialecke: a molekula-rajzoló (B) első megépítése.*

- **Tanulási cél:** Az atomok a párosítatlan külső elektronjaikból **közös elektronpárokat**
  alkotnak, és így nemesgázszerkezetet érnek el (hidrogén: 2, a többi: 8 elektron a külső
  héjon). Ebből következik, hogy hány kötést létesít egy atom (H 1, O 2, N 3, C 4), és ezért
  H₂O, CH₄, CO₂ a képlet. A molekulán belüli kötés erős, a molekulák között gyenge: forraláskor
  a vízmolekulák nem esnek szét.
- **Kerettanterv:** „tudja, hogy az atom külső elektronjainak fontos szerep jut a molekula- és
  ionképzés során” · „érti egyszerű molekulák kialakulását (H₂, Cl₂, O₂, N₂, H₂O, HCl, CH₄, CO₂),
  és fel tudja írni a képletüket” · „ismeri a köznapi anyagok molekula- és halmazszerkezetét
  (hidrogén, oxigén, nitrogén, víz, metán, szén-dioxid, …)” · „érti, hogy az atomok és ionok
  között jellemzően erősebb, a molekulák között gyengébb kémiai kötések alakulhatnak ki” ·
  fogalmak: „elemmolekula, vegyületmolekula, … nemesgázszerkezet, kémiai kötés, … képlet”.
- **Tévhitek:** Forraláskor a víz hidrogénre és oxigénre bomlik, a buborékban H₂ és O₂ van
  (jól dokumentált tévhit, a fizika 06 „a buborék vízgőz” képéhez kapcsolódik). A képletben a
  szám a molekulák számát jelenti (H₂O = „két víz”). Egy molekula lapos, ahogy a füzetbe
  rajzoljuk. Az atomok azért kapcsolódnak, mert „szeretnének” (az antropomorf magyarázatot
  energiára cseréljük: a kötött állapot kisebb energiájú, stabilabb).
- **Kulcsvizuál:** **molekulaépítő asztal.** Az atomok a külső héjukkal együtt jelennek meg (a
  párosítatlan elektronok kiemelve). Ha két párosítatlan elektron találkozik, összefonódnak,
  és közös párként a két atom közé kerülnek. Ezután a rajz Lewis-szerű képből (pöttyök)
  pálcikás golyómodellbe, majd kalottamodellbe vált át, 3D-hatású, forgatható golyókkal.
- **Interaktív:** atomok húzhatók egy készletből (H, C, N, O, Cl). Ha a kötés lehetséges,
  bepattannak; ha egy atomnak még van párosítatlan elektronja, az pulzál. A kész molekula
  egérrel forgatható (CH₄: tetraéder, H₂O: hajlott, CO₂: egyenes). A 7. lépésben egy
  hőmérséklet-csúszka melegíti a víz-, a metán- és az oxigénhalmazt: a molekulák elválnak
  egymástól, de egyik sem esik szét atomjaira.
- **Lépések (8):** Miért kapcsolódnak az atomok? – a párosítatlan elektron · H₂: az első közös
  elektronpár · Cl₂ és HCl: a nyolcas külső héj · O₂ és N₂: kettős és hármas kötés · H₂O,
  CH₄, CO₂: hány kötés jut egy atomra? · A molekula térben · Erős belül, gyenge kívül:
  forraláskor mi szakad el? · Összefoglalás.
- **Adatok:** kötésszög: H₂O 104,5°, CH₄ 109,5°, CO₂ 180°. Forráspont (1013 hPa): H₂
  −252,9 °C · N₂ −195,8 °C · O₂ −183,0 °C · CH₄ −161,5 °C · HCl −85,1 °C · Cl₂ −34,0 °C ·
  H₂O 100 °C; a CO₂ −78,5 °C-on szublimál. Erős belül, gyenge kívül: 1 g víz elforralásához
  ≈ 2,26 kJ kell, atomjaira bontásához ≈ 50 kJ, vagyis kb. 20-szor annyi (a víz
  atomizációs entalpiája ≈ 918 kJ/mol, a párolgáshő 100 °C-on 40,7 kJ/mol; a mol szó nem
  kerül a panelre). H–H kötéstávolság 74 pm.
- **Megjegyzés a vízhez:** a víz kiugróan magas forráspontját (a hidrogénkötést) a 7–8-os
  tanterv nem nevezi meg. A panel csak annyit mond, hogy „a vízmolekulák különösen erősen
  vonzzák egymást”; a fogalom a 9–10. évfolyamra marad.
- **Építőkocka:** B (atomgolyók, kötésvonal, elektronpár-pöttyök, 3D-forgatás, molekulasablonok
  a tanterv 8 molekulájára), C (külső héj a Lewis-képhez – a 05 C-moduljának csak a „külső
  héj” rajzolóját használja, ezért párhuzamosan gyártható vele, lásd 4. fejezet), Tx.
- **Meglévő anyag:** PhET *Build a Molecule*, *Molecule Shapes*. Nálunk a hangsúly az
  elektronpárból eredő kötésszámon és a „forraláskor nem esik szét” képen van.

### 07 · `07-ionok-kristalyok` – Miért nem olvad meg a só a serpenyőben? – ionok és kristályrácsok

- **Tanulási cél:** A fématom külső elektronjait átadja (pozitív ion lesz), a nemfématom felveszi
  őket (negatív ion lesz); mindkettő nemesgázszerkezetet ér el. Az egy oszlopban lévő elemek
  ugyanolyan töltésű ionokat képeznek. Az ionvegyület képletében a töltések kiegyenlítik egymást.
  A szilárd anyag tulajdonságait (olvadáspont, keménység, vezetés) a rács fajtája szabja meg:
  molekula-, ion-, atom- és fémrács.
- **Kerettanterv:** „érti az egyszerű ionok kialakulását (Na⁺, K⁺, Mg²⁺, Ca²⁺, Al³⁺, Cl⁻, O²⁻),
  és analógiás gondolkodással következtet az egy oszlopban található elemekből képződő ionok
  képletére” · „érti az ionvegyületek képletének megállapítását” · „ismeri a köznapi anyagok
  molekula- és halmazszerkezetét (… gyémánt, grafit, vas, réz, nátrium-klorid)” · „érti, hogy az
  atomok és ionok között jellemzően erősebb, a molekulák között gyengébb kémiai kötések
  alakulhatnak ki” · „Az ion képződése és fontosabb jellemzői, csoportosítás töltés alapján” ·
  „Az anyagok halmazszerkezete és fizikai tulajdonságai”.
- **Tévhitek:** A konyhasó NaCl-molekulákból áll. A képletben a kis szám a töltést jelenti (a
  CaCl₂-ben a „2” a kalcium töltése). A Na⁺ „elvesztett valamit”, ezért nagyobb lett (valójában
  kisebb: elveszíti a teljes külső héját). A fémek azért vezetnek, mert az atomjaik „fémesek”. A
  gyémánt és a grafit két különböző elem.
- **Kulcsvizuál:** egy nátrium- és egy klóratom a 05-ös héjrajzzal. A nátrium külső elektronja
  átugrik a klórra, a két ion mérete látványosan megváltozik (Na⁺ összezsugorodik, Cl⁻
  megnő), és a vonzásuk egy ionrácsot indít el, amely a képernyőn kockává nő. Később négy
  kristály áll egymás mellett egy „főzőlapon” (jég, só, réz, grafit), mindegyik fölött a
  nagyító.
- **Interaktív:** **ionképlet-kirakó**: kationok és anionok húzhatók egy tálcára, a mérleg
  akkor áll egyensúlyba, ha az össztöltés 0 (NaCl, MgO, CaCl₂, Al₂O₃, K₂O). A négy kristály
  hőmérséklet-csúszkája −100 és 4000 °C között állítható (logaritmikus skálán): a rácsok a
  saját olvadáspontjukon esnek szét. A „Vezet?” kapcsoló egy izzót kapcsol a kristályokra
  szilárd, olvadék és oldott állapotban.
- **Lépések (8):** 801 °C – miért nem olvad meg a só? · Elektronátadás: Na⁺ és Cl⁻ · Oszlop →
  töltés: az analógia · Képlet: a töltések kiegyenlítik egymást · Ionrács: nincs NaCl-molekula
  · Négy rács: molekula, ion, atom, fém · Melegítsd meg, és kapcsold áramkörbe! ·
  Összefoglalás.
- **Adatok:** olvadáspont: jég 0 °C · NaCl 801 °C · Cu 1085 °C · Fe 1538 °C · Al 660 °C; a
  szárazjég −78,5 °C-on szublimál; a grafit légköri nyomáson nem olvad meg, kb. 3600 °C fölött
  szublimál *(ellenőrizendő: a forrásokban 3640–3650 °C)*. A gyémánt levegőn kb. 700–900 °C-on
  elég. Mohs-keménység: gyémánt 10 · grafit 1–2 · NaCl 2,5 · Cu 3 · Fe 4 (tiszta vas
  ≈ 4–5). Méret (sugár): Na-atom 186 pm → Na⁺ 102 pm; Cl-atom 99 pm (kovalens) → Cl⁻ 181 pm
  *(a sugárdefiníciók eltérnek, a lecke csak az irányt és a nagyságrendet mutatja)*. A NaCl-rácsban
  a Na–Cl távolság 0,282 nm, vagyis egy 1 mm-es sókristály élén ≈ 3,5 millió ion sorakozik.
  Vezetés: a fémek és a grafit szilárdan is vezetnek; a NaCl szilárdan nem, olvadékban és
  oldatban igen.
- **Építőkocka:** C (elektronátadás animáció, ion töltéssel), B (rácsrajzoló: köbös ionrács,
  fémrács elektronfelhővel, gyémánt és grafit, molekularács), Tx (ionképletek), G
  (főzőlap, izzós vezetésvizsgáló).
- **Meglévő anyag:** a PhET-ben nincs pontos megfelelője.

### 08 · `08-kemiai-reakcio` – Hová lesz a gáz a tűzhelyen? – a kémiai reakció mint átrendeződés

*A reakció-réteg (F) első megépítése, a 01 részecskemotorjára és a 06 molekula-rajzolójára
építve.*

- **Tanulási cél:** A kémiai reakcióban új anyag keletkezik: a kötések felbomlanak, és új kötések
  jönnek létre, az atomok viszont megmaradnak, ezért a tömeg sem változik. A reakcióhoz a
  részecskéknek ütközniük kell, mégpedig elég nagy energiával. A katalizátor kisebb
  energiájú utat nyit, és közben nem fogy el. Van, amelyik reakció hőt ad le (exoterm), és
  van, amelyik hőt vesz fel (endoterm).
- **Kerettanterv:** „a részecskemodell alapján értelmezi az egyszerű kémiai reakciókat” · „ismeri
  a kémiai reakciók végbemenetelének legalapvetőbb feltételeit (ütközés, energia)” · „ismeri a
  katalizátor fogalmát, érti a katalizátorok működési elvének lényegét” · „A fizikai és a kémiai
  változások megkülönböztetése” · „A reakciók egyenletének leírása szavakkal, a folyamat
  értelmezése” · „A reakciók energiaviszonyai” · „A kémiai változások típusai” · tevékenységek:
  „A katalizátor hatásának bemutatása érdekes kísérleteken, pl. a hidrogén-peroxid bontása
  barnakőporral (vagy apróra vágott májdarabkákkal), a fejlődő oxigén kimutatása parázsló
  gyújtópálcával” · „A melegítőpárna működésének bemutatása” · fogalmak: „exoterm reakció,
  endoterm reakció, egyesülés, bomlás”.
- **Tévhitek:** Égéskor az anyag eltűnik (a gyertya rövidebb lesz, a gáz „elfogy”). Reakcióban
  az atomok átalakulnak egymásba. Ha összekeverem, azonnal reagál (az ütközés és az energia
  szerepe). A katalizátor elfogy, vagy „hozzáad” valamit a termékhez. Ami melegszik, az
  biztosan kémiai reakció (a melegítőpárna kristályosodása fizikai változás!). Az oldódás és
  az olvadás kémiai reakció.
- **Kulcsvizuál:** egy gázláng a tűzhelyen, mellette a nagyító. A metán- és az
  oxigénmolekulák golyói **megtartják a színüket**, a kötéseik szétnyílnak, és az atomok
  szén-dioxiddá és vízzé állnak össze (zárt képletű átrendeződés-animáció). Alatta élő
  „atomszámláló”: oszloponként C, H és O a reakció előtt és után, mindig egyforma. Mellette egy
  kétkarú mérleg, amelynek egyik serpenyőjében egy zárt palack van, benne ecet és
  szódabikarbóna, rajta léggömb.
- **Interaktív:** **reakcióedény-szimuláció** (A + F): hidrogén-peroxid-molekulák mozognak. A
  hőmérséklet-csúszkával nő az ütközések energiája; egy energiaküszöb alatt a molekulák
  lepattannak, fölötte elbomlanak (2 H₂O₂ → 2 H₂O + O₂), és az oxigénbuborékok számlálója
  pörög. A **„Barnakő”** gomb katalizátorfelületet tesz az edény aljára: ugyanazon a
  hőmérsékleten sokkal több a sikeres ütközés. Mellette az energiadiagram mutatja a két utat.
  A mérlegen a palack kupakja levehető: zártan a tömeg nem változik, nyitva a CO₂ elszáll.
- **Lépések (9):** Fizikai vagy kémiai változás? – új anyag keletkezik? · Atomok átrendeződése:
  metán + oxigén · Számold meg az atomokat! – a tömeg megmarad · Ütközés kell · Energia is
  kell: a gyufa szerepe · Exoterm és endoterm · Katalizátor: rövidebb út · Egyesülés és bomlás ·
  Összefoglalás.
- **Adatok:** szóegyenletek (elsődleges, a tanterv szerint): metán + oxigén → szén-dioxid + víz;
  hidrogén-peroxid → víz + oxigén. Képlettel (kiegészítő, a build ellenőrzi):
  CH₄ + 2 O₂ → CO₂ + 2 H₂O · 2 H₂O₂ → 2 H₂O + O₂ · NaHCO₃ + CH₃COOH → CH₃COONa + H₂O + CO₂.
  Hőfejlődés: 1 m³ földgáz ≈ 34 MJ (≈ 9,5 kWh) *(ellenőrizendő: a hazai gázszolgáltatói
  átlagos égéshő/fűtőérték)*. Endoterm példák: a szódabikarbóna és az ecet reakciója
  (néhány °C-ot hűl, *mérendő*), a fotoszintézis (fényenergiát köt meg), a mészkő hevítése
  (CaCO₃ → CaO + CO₂). Exoterm fizikai változás: a melegítőpárna (nátrium-acetát-trihidrát)
  58 °C-on kristályosodik. Gyógyszertári hidrogén-peroxid: 3 %-os. Lavoisier tömegmegmaradási
  kísérletei: 1770-es, 1780-as évek. Egyesülés: vas + kén → vas-szulfid; hidrogén + oxigén →
  víz. Bomlás: hidrogén-peroxid, mészkő, víz (árammal).
- **Modell-őszinteség:** a metán égése valójában sok lépésben, gyökökön keresztül megy végbe. A
  2. lépés átrendeződés-animációja szemléltetés („nem így, egyetlen ütközésben történik”). A
  szimuláció ezért egy valódi kétrészecskés lépést mutat (H₂O₂). Az energiadiagram
  minőségi (nincs számskála).
- **Biztonság:** a hidrogén + oxigén egyesülését (durranógáz) csak szóban, „NE PRÓBÁLD KI”
  bélyeggel említjük, látványos robbanás nélkül.
- **Építőkocka:** F (reakciószabályok, energiaküszöb, katalizátorfelület, atomkönyvelés,
  energiadiagram), A, B (molekulasablonok, átrendeződés-morf), Tx (egyenlet), Gr, mérleg (a
  fizika 01-ből).
- **Meglévő anyag:** PhET *Reactants, Products and Leftovers*, *Balancing Chemical Equations*,
  *Reactions & Rates*. Nálunk a hangsúly az „atomok megtartják a színüket” képen, a mérlegen
  és az ütközési energiaküszöbön van.

### 09 · `09-eges-korrozio` – Mi a közös a csillagszóróban és a rozsdás szögben? – égés és korrózió

- **Tanulási cél:** Az égéshez három dolog kell: éghető anyag, oxigén és a gyulladási
  hőmérséklet. A tűzoltás ezek közül legalább egyet elvesz. Kevés oxigénnél tökéletlen az
  égés, és mérgező szén-monoxid keletkezik. Ugyanaz az anyag (a vas) gyorsan is éghet
  (csillagszóró), és lassan is „éghet” (rozsdásodás); a különbség a sebesség és a felület. A
  vas korróziójához oxigén és víz kell, a só gyorsítja. A korrózió ellen bevonattal vagy
  ötvözéssel védekezünk.
- **Kerettanterv:** „ismeri a köznapi élet szempontjából legalapvetőbb kémiai reakciókat (pl.
  égési reakciók, …)” · „ismeri a korrózió fogalmát és a fémek csoportokba sorolását
  korrózióállóságuk alapján, érti a vas korróziójának lényegét, valamint a korrózióvédelem
  módjait” · tevékenységek: „Az égés tanulmányozása, a gyors (gyufa égése, földgáz égése,
  borszesz égése, csillagszóró égése, magnézium égése) és lassú égés (rozsdásodás, korhadás)
  tanulmányozása egyszerű kísérletekkel” · „Az égés feltételeinek vizsgálata, az éghetetlen
  zsebkendő kísérlet elvégzése” · fogalmak: „égés, gyors égés, lassú égés, … korrózió, rozsda” ·
  a sáv bevezetője: „életmentő is lehet számukra (például a benzingőz robbanásveszélye, a
  szén-monoxid és a klórgáz végzetes hatása)”.
- **Tévhitek:** A vas nem ég. A rozsdás szög könnyebb, mint az eredeti (valójában nehezebb:
  oxigén kötődött hozzá). A tűz „anyag”. Az égő olajat vízzel kell oltani. A szén-monoxid
  szaga figyelmeztet (színtelen, szagtalan). A rozsdamentes acél nem tartalmaz vasat.
- **Kulcsvizuál:** a **tűzháromszög** (éghető anyag, oxigén, hő) egy égő fahasáb körül; mindhárom
  oldal kivehető, és a láng ennek megfelelően kialszik. Később osztott kép: bal oldalt egy
  csillagszóró szikrái, jobb oldalt egy szög a nedves vattán, ugyanazzal a reakcióval
  (vas + oxigén → vas-oxid), két időskálán: másodpercek és napok.
- **Interaktív:** a tűzháromszög oldalai gombbal elvehetők (fedő = oxigén el; víz = hő el;
  homok vagy fedő). Az olajtűz-gombra a jelenet egy egyértelmű „NE!” kártyát mutat a gőz
  szétcsapódásának egyszerű sémájával, nem látványos lángcsóvát. Az oxigén csúszkája
  (21 % → 10 %) a tökéletes égésből tökéletlenbe visz: megjelennek a CO-molekulák, és megszólal
  egy CO-jelző. A korrózióasztalon három kémcső van (száraz levegő, kiforralt víz olajréteggel,
  nedves vatta) és egy sós változat; egy időcsúszka 0–14 napig mutatja a rozsdásodást. A
  védelem lépésében a szög festhető, horganyozható, vagy cserélhető rozsdamentesre.
- **Lépések (8):** Mi kell a tűzhöz? – a tűzháromszög · Gyulladási hőmérséklet: papír, fa,
  benzingőz · Tűzoltás: melyik oldalt veszed el? · Kevés oxigén: szén-monoxid · Gyors és lassú
  égés: csillagszóró és rozsda · Mi kell a rozsdához? – a három kémcső · Korrózióvédelem és
  nemesfémek · Összefoglalás.
- **Adatok:** A levegő oxigéntartalma 20,95 térfogat%; a gyertya kb. 15–16 % oxigénnél alszik ki
  *(ellenőrizendő)*. Gyulladási (öngyulladási) hőmérséklet, kerekítve: papír ≈ 230 °C, fa
  ≈ 250–300 °C, benzin ≈ 250–280 °C, földgáz (metán) ≈ 540–600 °C. A benzin lobbanáspontja
  ≈ −40 °C: a gőze fagyban is meggyulladhat. Robbanási határok (térfogat%): metán ≈ 4,4–17,
  benzingőz ≈ 1,4–7,6. Szén-monoxid: színtelen, szagtalan; 0,1–0,2 % a levegőben órák alatt
  életveszélyes; a CO-jelzők 50 ppm körül riasztanak (EN 50291) *(ellenőrizendő)*. A vas
  rozsdásodása: 10 g vasból ≈ 14,3 g vas(III)-oxid lesz (Fe₂O₃/2 Fe = 1,43). A rozsda
  térfogata az eredeti vasénak többszöröse, ezért leválik. A rozsdamentes acél legalább
  10,5 % krómot tartalmaz. Az alumínium felületén néhány nanométeres, védő oxidréteg van. A
  korrózióállóság szerint: nemesfémek (arany, platina, ezüst), patinásodók (réz), védőréteget
  képzők (alumínium, cink), rozsdásodók (vas). Kézmelegítő tasak: vaspor + víz + só + aktív
  szén, órákig 50–60 °C.
- **Biztonság:** ez a sorozat legkényesebb leckéje. Olajtűz, benzingőz, CO: mindig
  *figyelmeztetés*, sosem bemutatható kísérlet. A tűzoltás lépésében a helyes cselekvés áll
  (fedő, 105/112 hívása) – ezt a tanár ellenőrizze.
- **Építőkocka:** F (égés: O₂-koncentráció → tökéletes vagy tökéletlen termékek), G (kémcsövek,
  láng), B (CO, CO₂, Fe₂O₃ golyómodell), időcsúszka.
- **Meglévő anyag:** a katasztrófavédelem oktatóanyagai (tűzoltás, CO). Érdemes megnézni, és a
  `.md`-ben hivatkozni rájuk.

### 10 · `10-sav-bazis` – Mit mutat a lilakáposzta-lé? – savak, lúgok, pH, közömbösítés

- **Tanulási cél:** Az oldatok kémhatása savas, semleges vagy lúgos; a pH-skála 0-tól 14-ig
  méri, a 7 semleges. Az indikátorok a kémhatástól függően színt váltanak. Savas oldatban
  hidrogénionból, lúgosban hidroxidionból van több; közömbösítéskor ezek vízzé egyesülnek, és
  só marad vissza.
- **Kerettanterv:** „ismer sav-bázis indikátorokat, érti felhasználásuk jelentőségét” ·
  „ismeri a köznapi élet szempontjából legalapvetőbb kémiai reakciókat (pl. … savak és bázisok
  reakciói …)” · fogalmak: „sav, bázis, só, savas kémhatás, semleges kémhatás, lúgos kémhatás,
  közömbösítés, pH-érték, indikátor” · tevékenységek: „Laboratóriumi és növényi indikátorok
  színváltozásának vizsgálata (lakmusz, fenolftalein, pH-papír, antociánok)” · „A háztartásban
  megtalálható semleges, savas és lúgos oldatok kémhatásának vizsgálata egyszerű
  tanulókísérlettel” · „A közömbösítés vizsgálata egyszerű laboratóriumi kísérletekkel” · „A
  szúnyogcsípés fájdalmas érzésének csökkentése szódabikarbónás bedörzsöléssel – beszélgetés,
  vita, eszmecsere a módszer kémiai-biológiai hátteréről és hatékonyságáról” · (1.) „Néhány
  háztartási vegyszer (pl. sósav, hypo stb.) címkéjének megismerése, a veszélyességi jelek
  értelmezése”.
- **Tévhitek:** Ami savas, az mind maró és veszélyes (a citromlé is savas), illetve ami lúgos,
  az ártalmatlan (a lefolyótisztító a legveszélyesebb háztartási vegyszerek egyike). A
  semleges oldatban nincs sem H⁺, sem OH⁻. A pH 6 „kicsit”, a pH 3 „háromszor” savasabb (a
  skála tízszeres lépésű – ez kiegészítő megjegyzés). A közömbösítés után „semmi” marad
  (pedig só és víz). Az indikátor maga is sav vagy lúg, és ettől lesz savas az oldat.
- **Kulcsvizuál:** egy sor kémcső vöröskáposzta-lével (citromlé, ecet, kóla, tej, csapvíz,
  szódabikarbóna-oldat, szappanos víz, lefolyótisztító). Mindegyik a saját pH-jának megfelelő
  színt kapja, alattuk egy 0–14-es skála. A nagyítóban H⁺ (piros pötty) és OH⁻ (kék pötty) arány
  látszik; a semleges vízben mindkettő egyformán kevés.
- **Interaktív:** az **indikátorválasztó** (vöröskáposzta, lakmusz, fenolftalein, univerzális)
  átszínezi a kémcsöveket; ebből látszik, hogy a fenolftalein savban és semlegesben egyaránt
  színtelen, vagyis nem tud különbséget tenni. A **közömbösítésnél** egy büretta-csap
  (csúszka) cseppenként adagolja a lúgot a savhoz. A nagyítóban a H⁺ és az OH⁻ találkozásakor
  egy vízmolekula villan fel; a pH-görbe élőben rajzolódik, és az ekvivalenciapontnál
  hirtelen ugrik. Bepárlás után ott a só (kapcsolat a 02-vel).
- **Lépések (9):** Mit mutat a lilakáposzta-lé? · Savas, semleges, lúgos: a pH-skála ·
  Részecskeszint: H⁺ és OH⁻ · Indikátorok: melyik mit lát? · Közömbösítés cseppenként · Só és
  víz marad · A konyhában: szódabikarbóna, gyomorsav, csípések · Maró! – a címke
  veszélyességi jelei · Összefoglalás.
- **Adatok** (tipikus pH, kerekítve; *a `.md` megjegyzésébe forrás kell*): gyomorsav 1–2 ·
  citromlé ≈ 2,3 · ételecet ≈ 2,5 · kóla ≈ 2,5 · narancslé ≈ 3,5 · kávé ≈ 5 · bőr felszíne
  ≈ 5,5 · tiszta esővíz ≈ 5,6 · tej ≈ 6,7 · tiszta víz 7 · vér 7,35–7,45 · tengervíz ≈ 8,1 ·
  szódabikarbóna-oldat ≈ 8,3 · szappanos víz ≈ 9–10 · szalmiákszesz ≈ 11,5 · hypo ≈ 12–13 ·
  lefolyótisztító (NaOH) ≈ 13–14. Indikátorok átcsapási tartománya: lakmusz 4,5–8,3 (piros →
  kék) · fenolftalein 8,2–10 (színtelen → ciklámen). Vöröskáposzta (antocián), tájékoztató
  jelleggel: pH 1–2 piros · 4 rózsaszín-lila · 6–7 ibolya · 8 kék · 10 kékeszöld · 12 zöld ·
  13–14 sárga *(a színek a kivonat töménységétől függnek)*. Közömbösítési modell (erős sav +
  erős lúg): 50 cm³ pH 1-es sósav + pH 13-as nátronlúg; az ekvivalenciapont 50 cm³ lúgnál van,
  a pH a 49,9 és a 50,1 cm³ között ≈ 4-ről ≈ 10-re ugrik (számolt érték). Szóegyenlet:
  sósav + nátrium-hidroxid → nátrium-klorid + víz.
- **A szúnyogcsípés – Döntés:** a tanterv vitát kér a módszer hatékonyságáról. A lecke nem
  állítja, hogy a szódabikarbóna „közömbösíti” a szúnyogcsípést: a viszketést főleg a
  szervezet immunválasza okozza, nem sav. A hangyacsípésben viszont valóban sav
  (hangyasav) van. A lépés egy kérdéssel zárul („Mit gondolsz, miért segíthet – vagy miért
  nem?”), a forrásokat a `.md` megjegyzése adja *(ellenőrizendő)*.
- **Biztonság:** a vegyszert sosem kóstoljuk és nem szagoljuk meg közvetlenül; a
  lefolyótisztító és a hypo GHS-jeleit a lecke valósághűen rajzolja (piros keretes
  rombusz: maró, figyelmeztető). Otthoni kísérlet csak vöröskáposzta-lével és élelmiszerekkel.
- **Építőkocka:** H (pH → indikátorszín, skála, titrálási görbe), A (H⁺/OH⁻ találkozása mint
  egyszerű reakció, az F-ből), G (kémcsősor, büretta), Gr (pH-görbe), GHS-piktogram
  rajzoló.
- **Meglévő anyag:** PhET *pH Scale*, *Acid-Base Solutions*. Nálunk a hangsúly a háztartási
  sor színein és az élő pH-ugráson van.

### 11 · `11-levego` – Mi van a levegőben, és mi kerül bele? – légkör, savas eső, ózon, szmog

- **Tanulási cél:** A levegő keverék: főleg nitrogén és oxigén, kevés argon, nagyon kevés
  szén-dioxid. Égéskor szén-dioxid, vízgőz, és ha a tüzelőanyagban kén van vagy az égés
  forró, kén- és nitrogén-oxidok kerülnek bele. Ezekből vízzel savak lesznek: savas eső, ami
  a mészkövet is oldja. Az ózon fent véd az UV-sugárzástól, lent szennyező. Az ózonréteg
  vékonyodása és az üvegházhatás két különböző jelenség.
- **Kerettanterv:** „ismeri természeti környezetének, azon belül a légkörnek … legalapvetőbb
  anyagait” · „érti a globális klímaváltozás, a savas esők, az ózonréteg károsodásának, valamint
  a szmogoknak a kialakulását és emberiségre gyakorolt hatását” · „azonosítja és példát hoz fel a
  környezetében előforduló leggyakoribb, levegőt, vizet és talajt szennyező forrásokra” ·
  tevékenységek: „Egyszerű tanulókísérletek a levegő összetételének vizsgálatára, pl. az oxigén
  mennyiségének meghatározása a levegőben” · „Az esővíz kémhatásának vizsgálata” · „A savas esők
  épületekre, illetve műemlékekre gyakorolt hatásának modellezése egy mészkő- vagy
  márványdarabon”.
- **Tévhitek:** A levegő nagy része oxigén. Az üvegházhatást az ózonlyuk okozza, vagy fordítva
  (jól dokumentált keveredés, a fizika 14 is említi). Minden ózon jó. A savas eső maró, mint a
  sósav (pH 4–5: inkább a paradicsomlé tartománya, de hosszú távon kőzetet old, és tavakat
  savanyít). A gyertyás kísérletben azért emelkedik a víz, mert „elfogy az oxigén” (a hibás
  kísérlet maga is tananyag).
- **Kulcsvizuál:** egy 100 részecskés „levegőablak” (78 N₂, 21 O₂, 1 Ar), és egy gomb, amely
  10 000 részecskére nagyít, ahol végre megjelenik ≈ 4 CO₂. Később egy márványszobor egy
  időcsúszkával (0–100 év), amely savas esőben lassan elmosódik; a nagyítóban a H⁺ ionok
  megtámadják a kalcium-karbonát-rácsot, és CO₂-buborék szabadul fel.
- **Interaktív:** a **gyertyás és a vasgyapotos kísérlet** egymás mellett, egy-egy
  „magyarázat” gombbal. A gyertyánál a víz emelkedését részben a gáz lehűlése és a
  szén-dioxid elnyelődése okozza, és a gyertya 15–16 % oxigénnél már kialszik. A vasgyapot
  rozsdásodása lassú, de a teljes oxigént elhasználja: ≈ 1/5. Az eső pH-csúszkája (5,6 → 4)
  a szobor kopását gyorsítja. Az ózonlépésben a magasság csúszkával állítható: a fenti
  ózonréteg elnyeli az UV-t, a lenti ózon nyári szmogot okoz.
- **Lépések (9):** Miből áll a levegő? · Mennyi az oxigén? – két kísérlet, egy hiba · Mi kerül a
  levegőbe égéskor? · Savas eső: oxidok + víz · A márványszobor · Ózon: fent pajzs, lent méreg ·
  Üvegházhatás ≠ ózonlyuk · Téli és nyári szmog · Összefoglalás: mit tehetsz?
- **Adatok:** száraz levegő (térfogat%): N₂ 78,08 · O₂ 20,95 · Ar 0,93 · CO₂ ≈ 0,0425
  (≈ 425 ppm, globális átlag 2025, *frissítendő*); a vízgőz 0–4 % között változik. A tiszta
  esővíz pH-ja ≈ 5,6 (az oldott CO₂ miatt), savas eső: pH < 5,6, szennyezett területen
  4–4,5. Ózon: a rétege 15–35 km magasan van, a teljes mennyisége a felszínre hozva
  ≈ 3 mm vastag lenne (≈ 300 Dobson-egység). Az ózonlyukat 1985-ben írták le, a montreali
  jegyzőkönyv 1987-es; az antarktiszi ózonréteg várhatóan 2066 körül áll helyre (WMO/UNEP
  2022) *(frissítendő)*. Londoni szmog, 1952. december: néhány nap alatt ≈ 4000 haláleset
  (későbbi becslések ≈ 10–12 ezer). PM10 napi határérték 50 µg/m³ (EU; 2030-tól 45);
  a hazai szmogriadó fokozatai *(ellenőrizendő, frissítendő: a hatályos kormányrendelet
  szerint)*. Szóegyenlet: kén + oxigén → kén-dioxid; kén-dioxid + víz → kénessav.
- **Építőkocka:** A (levegőablak, H⁺ a rácson), B (N₂, O₂, Ar, CO₂, O₃, SO₂ sablon), H (eső
  pH-ja), G (kémcső a vízzel), időcsúszka.
- **Kapcsolat:** az üvegházhatás fizikáját a fizika `14-uveghaz` lecke mutatja meg; a 7.
  lépés csak a megkülönböztetést végzi el, és hivatkozik rá.
- **Meglévő anyag:** PhET *Greenhouse Effect* (csak az üvegházhatás).

### 12 · `12-viztisztitas` – Tiszta-e, ami átlátszó? – természetes vizek és víztisztítás

- **Tanulási cél:** A Föld vizének csak kis része iható édesvíz. A természetes víz mindig
  oldat: ionok, gázok, esetleg szennyezők vannak benne, amelyek nem látszanak. Az ivóvízgyártás
  és a szennyvíztisztítás lépései az 1. témakör elválasztási műveletei (szűrés, ülepítés),
  kiegészítve biológiai és kémiai lépésekkel. Ami feloldódott (pl. a trágyából a nitrát),
  átjut a szűrőn.
- **Kerettanterv:** „ismeri természeti környezetének, azon belül … a természetes vizeknek …
  legalapvetőbb anyagait” · „megérti és példákkal szemlélteti az emberi tevékenység és a
  természeti környezet kölcsönös kapcsolatát kémiai szempontok alapján” · „A természetes vizek
  összetétele, szennyezői, víztisztítás, ivóvízgyártás” · tevékenységek: „Természetes vizek
  mintáinak vizsgálata bepárlással” · „Üzemlátogatás a helyi vagy egy regionális
  szennyvíztisztítóban, egy hulladéklerakóban vagy egy hulladékégetőben” · fogalmak: „édes víz,
  sós víz, ásványvíz, … trágya”.
- **Tévhitek:** Ami átlátszó, az tiszta. A desztillált víz a legegészségesebb. A forralás minden
  szennyezést eltávolít (a baktériumokat elpusztítja, de a nitrátot nem, sőt a sókat
  töményíti). A tengervíz forralva iható. A szennyvíz „eltűnik” a csatornában.
- **Kulcsvizuál:** egy 100 literes „Föld-víz” tartály, amelyből csak egy pohárnyi a hozzáférhető
  édesvíz. Ezután egy vízcsepp útja: Duna → parti szűrés (homok- és kavicsrétegek, a nagyítóban
  a fennakadó szemcsék és baktériumok, az átjutó ionok) → fertőtlenítés → csap → szennyvíz →
  tisztítótelep (rács, homokfogó, ülepítő, eleveniszap-medence baktériumokkal, utóülepítő) →
  vissza a folyóba.
- **Interaktív:** három bepárlócsésze (desztillált víz, csapvíz, ásványvíz): a csúszkával
  elpárologtatva más-más mennyiségű „maradék” marad. A szennyvíztisztítás lépései kártyákkal
  sorba rendezhetők (a 02 kártyamodulja); minden lépésnél a nagyító mutatja, mi távozik. A
  trágyaszóró gomb nitrátot juttat a talajvízbe, és a nitrátmérő végigköveti a szűrőkön.
- **Lépések (8):** Mennyi iható víz van a Földön? · Átlátszó = tiszta? – a nagyítóban ·
  Bepárlás: mi marad vissza? · Parti szűrés: a homok mint szűrő · Fertőtlenítés, és ami átjut
  (nitrát) · A szennyvíz útja · Tengervízből ivóvíz: lepárlás és energia · Összefoglalás:
  takarékosság.
- **Adatok:** a Föld vize: ≈ 97 % sós, ≈ 2,5–3 % édes; az édesvíz ≈ 69 %-a jég, ≈ 30 %-a
  talajvíz, ≈ 1 %-a felszíni (USGS). Tengervíz ≈ 35 g só/kg. Nitrát-határérték az ivóvízben
  50 mg/L (EU ivóvízirányelv). Az ásványvíz hazai definíciója legalább 500 mg/L oldott
  ásványianyag-tartalom vagy más, rendeletben meghatározott feltétel *(ellenőrizendő: a
  hatályos rendelet szerint)*. Budapest ivóvizének csaknem egésze parti szűrésű kutakból
  származik (Szentendrei- és Csepel-sziget) *(ellenőrizendő: Fővárosi Vízművek)*. Egy
  ember napi vízfogyasztása itthon ≈ 100 L *(frissítendő)*.
- **Építőkocka:** G (bepárlócsésze, rétegzett szűrő, medencék), A (ionok és baktériumok a
  pórusoknál, ezt a 02-ből emeljük át), kártyák.
- **Meglévő anyag:** a vízművek oktatási oldalai és üzemlátogatásai. A tanterv maga is
  üzemlátogatást javasol, a lecke erre készít fel.

### 13 · `13-szappan-vizkemenyseg` – Hogyan viszi el a szappan a zsírt? – mosószerek és vízkeménység

- **Tanulási cél:** A víz és a zsír nem elegyedik. A szappanmolekulának vízkedvelő „feje” és
  zsírkedvelő „farka” van, ezért a zsírcseppet körbeveszi és a vízben elszállítja (micella). A
  kemény vízben kalcium- és magnéziumionok vannak: ezek a szappannal oldhatatlan csapadékot
  adnak, ezért kevesebb a hab. Melegítéskor vízkő válik ki, ami savval (ecettel,
  citromsavval) oldható. A hypót savas tisztítószerrel összekeverni életveszélyes.
- **Kerettanterv:** „A vízkeménység” · „Mosószerek, tisztítószerek” · „Fertőtlenítőszerek” ·
  „képes a forgalomban lévő kemikáliák (növényvédő szerek, háztartási mosó- és tisztítószerek)
  címkéjén feltüntetett használati útmutató értelmezésére, azok felelősségteljes használatára” ·
  tevékenységek: „A kemény és lágy víz összehasonlítása egyszerű tanulókísérlettel (pl. szappan
  habzása különböző keménységű vizekben, vízlágyítás csapadékos vízlágyítással)” · „A hypo
  vizsgálata, színtelenítő hatásának megfigyelése egyszerű kémcsőkísérletekkel, a hypo és a
  háztartási sósav egymásra hatásának veszélyei” · fogalmak: „kemény víz, vízlágyítás,
  vízkőoldás, mosószer, szappan, fertőtlenítőszer”.
- **Tévhitek:** A szappan „feloldja” a zsírt. Több mosószer = tisztább ruha. A hab mossa a
  ruhát. A vízkő szennyeződés vagy „mész a csőből”. Két tisztítószer együtt kétszer olyan jól
  tisztít.
- **Kulcsvizuál:** egy zsírfolt egy szálon, a nagyítóban: szappanmolekulák (kör alakú fej,
  hullámos szénláncfarok) rajzanak; a farkak a zsírba fúródnak, a fejek kifelé állnak, és a
  zsírcsepp micellaként leválik. Kemény vízben a Ca²⁺-ionok két szappanfejet összekapcsolnak,
  és a pár szürke pelyhekként kiválik.
- **Interaktív:** csúszkával a szappan mennyisége (kevés: nem elég a micellához; sok: a
  felesleg habbá válik, de nem tisztít jobban) és a vízkeménység (Ca²⁺-szám). Gombok:
  „szóda” (csapadékos vízlágyítás: a Ca²⁺ kalcium-karbonátként kiválik), „forralás” (a
  vízforraló falán vízkő rakódik le), „ecet” (a vízkő pezseg, CO₂ szabadul fel). A címkés
  lépésben két palack (hypo, savas WC-tisztító) között egy áthúzott nyíl van, és egy
  tiltókártya magyarázza, hogy mérgező klórgáz keletkezne.
- **Lépések (8):** Víz és olaj nem keveredik · A szappanmolekula: fej és farok · Micella:
  becsomagolt zsír · Kemény víz: kalcium- és magnéziumionok · Vízkő a vízforralóban ·
  Vízlágyítás és vízkőoldás · Címke: mit nem szabad összekeverni? · Összefoglalás.
- **Adatok:** a szappan zsírsavak nátrium- (vagy kálium-) sója, pl. nátrium-sztearát (18
  szénatomos lánc). Vízkeménység: 1 német keménységi fok (nk°) = 10 mg CaO literenként. Hazai
  szokásos beosztás: lágy < 8 nk°, közepes 8–18 nk°, kemény > 18 nk° *(ellenőrizendő: a
  forrásokban több beosztás van)*; a budapesti csapvíz ≈ 14–16 nk° *(ellenőrizendő)*.
  Szóegyenletek: kalcium-hidrogén-karbonát → kalcium-karbonát + víz + szén-dioxid (melegítésre,
  vízkő); kalcium-karbonát + ecetsav → kalcium-acetát + víz + szén-dioxid. A hypo hatóanyaga
  nátrium-hipoklorit; savval klórgázt fejleszt.
- **Biztonság:** a hypo + sav jelenet **nem mutat gázfelhőt** mint látványelemet; egy
  szemléltető ábra áll ott (két palack, tiltó jel, a keletkező Cl₂ golyómodellje), „NE
  KEVERD!” felirattal. A címkén a GHS-jelek valósághűek.
- **Építőkocka:** B (lánc-molekula: fej + hajlékony farok, ezt a 14 is használja), A
  (micellaképződés: amfipatikus részecskék egyszerű vonzásszabállyal), G (vízforraló,
  kémcső), GHS-piktogram (a 10-ből).
- **Meglévő anyag:** kevés jó interaktív anyag van a micelláról; ez a sorozat egyik
  legígéretesebb „wow” leckéje.

### 14 · `14-koolaj` – Mi lesz a kőolajból? – szénhidrogének, lepárlás, műanyag

- **Tanulási cél:** A kőolaj sokféle szénhidrogén keveréke. Minél hosszabb a lánc, annál
  erősebben vonzzák egymást a molekulák, és annál magasabb a forráspont. Ezt használja ki a
  lepárlótorony, ahol minden frakció a saját magasságában csapódik le. A frakciókból
  üzemanyag, kenőanyag, aszfalt lesz; a rövid láncokból óriásmolekulák, vagyis műanyag. Égéskor
  a szén szén-dioxiddá alakul: 1 liter benzinből több mint 2 kg CO₂ lesz.
- **Kerettanterv:** „ismeri a kőolaj feldolgozásának módját, fő alkotóit, a szénhidrogéneket,
  tudja, hogy ezekből számos termék (motorhajtóanyag, kenőanyag, műanyag, textília, mosószer)
  készül” · „tisztában van azzal, hogy a bennünket körülvevő anyagokat a természetben található
  anyagokból állítjuk elő” · „A kőolaj” · (5.) „A fosszilis energiahordozók” · tevékenységek:
  „A kőolaj feldolgozásával kapcsolatos idegen nyelvű animáció szöveges narrációja” ·
  „Kőolajpárlatok (pl. benzin, petróleum, szilárd paraffin) egyszerű laboratóriumi vizsgálata
  (oldási és oldódási kísérletek, sűrűség megfigyelése)” · „„Áldás vagy átok a műanyag?” –
  érvelő vita a műanyagok használata mellett és ellen”.
- **Tévhitek:** A kőolaj egyetlen anyag. A benzint a kőolajból „kiszűrik”. 1 liter benzinből
  legfeljebb 1 liternyi (vagy 0,75 kg-nyi) CO₂ lehet: hogyan lehetne több, mint ami volt?
  (A levegő oxigénje kötődik hozzá – kapcsolat a 08 tömegmegmaradásával.) A műanyag
  „mesterséges”, ezért semmi köze a természethez. A kőolaj dinoszauruszokból lett (főleg
  tengeri planktonból).
- **Kulcsvizuál:** egy lepárlótorony metszete, alul a kemence, fölfelé csökkenő hőmérséklettel.
  A gőzben különböző hosszúságú láncmolekulák szállnak fölfelé, és mindegyik azon a tálcán
  csapódik le, ahol a hőmérséklet a forráspontja alá esik. A kivezetéseknél ikonok: gázpalack,
  benzinkút, repülő, dízel, kenőolaj, aszfalt.
- **Interaktív:** egy **lánchossz-csúszka** (C1–C20) mutatja a molekulát, a valódi
  forráspontját és azt, hogy melyik tálcán jön ki. Egy kemencehőmérséklet-csúszkával
  megfigyelhető, hogy túl alacsony hőmérsékleten a hosszú láncok lent maradnak. A „Krakkolás”
  gomb egy hosszú láncot rövidebbekre vág, az „Összekapcsolás” gomb az etilénből
  polietilénláncot fűz. A CO₂-lépésben egy mérleg mutatja: 1 L benzin (0,75 kg) + oxigén →
  2,3 kg CO₂ + víz.
- **Lépések (8):** Fekete, sűrű keverék · Lánchossz és forráspont · A lepárlótorony · Frakciók és
  termékek · Krakkolás: rövidebb láncok · Műanyag: óriásmolekula · 1 liter benzin → 2,3 kg CO₂ ·
  Évmilliók alatt keletkezett, évtizedek alatt fogy – összefoglalás.
- **Adatok:** forráspont (1013 hPa): metán −161,5 · etán −88,6 · propán −42,1 · bután −0,5 ·
  pentán 36,1 · hexán 68,7 · heptán 98,4 · oktán 125,7 · dekán 174,1 · dodekán 216,3 ·
  hexadekán 286,9 · eikozán 343 °C. Frakciók (közelítő forráspont-tartomány, lánchossz):
  gáz < 30 °C (C1–C4) · benzin 30–180 °C (C5–C10) · petróleum/kerozin 150–275 °C (C10–C16) ·
  gázolaj 250–350 °C (C14–C20) · kenőolaj, paraffin > 350 °C (C20–C40) · bitumen: maradék
  *(a határok forrásonként eltérnek, a lecke „kb.”-kal mutatja őket)*. Benzin sűrűsége
  0,72–0,775 g/cm³ (MSZ EN 228); kőolaj ≈ 0,8–0,95 g/cm³ (úszik a vízen). CO₂: 1 L benzin
  ≈ 2,3 kg (oktánnal számolva 2,30), 1 L gázolaj ≈ 2,65 kg. Polietilén: egy lánc több tízezer
  szénatomból áll. Szóegyenlet: oktán + oxigén → szén-dioxid + víz; képlettel:
  2 C₈H₁₈ + 25 O₂ → 16 CO₂ + 18 H₂O.
- **Építőkocka:** B (lánc-molekula a 13-ból, cikk-cakk szénlánc, polimer), G (torony, kemence,
  tálcák), Gr (forráspont–lánchossz pontsor), Tx, mérleg.
- **Meglévő anyag:** a tanterv maga „idegen nyelvű animációt” javasol – ez a lecke a magyar
  nyelvű, interaktív változat.

---

## 4. Építőkockák és gyártási sorrend

### Modulok

A modulok először egy-egy referencialeckében készülnek, **a lecke `<script>`-jében külön,
jól elhatárolt blokkban**, saját névtérrel (a történelem-kiegészítés mintájára:
`/* ── MODUL: Részecskemotor (Reszecske) ── */ … /* ── MODUL VÉGE ── */`). Az első köteg
átnézése után kerülnek a közös könyvtárba. **Döntés:** a részecskemotor tantárgyfüggetlen
neve `Reszecske`, helye `shared/reszecske.js` (a biológia és a fizika is használhatja); a
kémiaspecifikus modulok `Kem*` névtérrel a `shared/kemia/` alá kerülnek. A `shared/`
módosítása továbbra is csak egyeztetve történhet.

| Modul | Mit tud | Lecke | Első megépítés |
|---|---|---|---|
| **A · Részecskemotor** (`Reszecske`) | 2D korongok rugalmas ütközéssel, falak, dugattyú, hőmérséklet ↔ sebesség, vonzás (halmazállapotok), több részecskefajta, zónák (szűrő, felület), diffúzió, statisztikák; **determinisztikus visszajátszás** | 01, 02, 03, 04, 08, 10, 11, 12, 13 | **01** |
| **B · Molekula-rajzoló** (`KemMol`) | 3D-hatású atomgolyók (egységes színkód), kötésvonal, elektronpár-pöttyök, pálcikás és kalottamodell, forgatás, sablonok (H₂, Cl₂, O₂, N₂, H₂O, HCl, CH₄, CO₂, O₃, SO₂, H₂O₂, CO, NH₃), átrendeződés-morf, szénlánc és polimer, kristályrácsok | 03, 04, 06, 07, 08, 09, 11, 13, 14 | **06** (rácsok: 07, lánc: 13) |
| **C · Atommodell** (`KemAtom`) | Bohr-héjak Z ≤ 20, nukleonkupac, elektronanimáció, külső héj kiemelése, elektronátadás és ionképzés, „felugró” elektron (lángfestés) | 05, 06, 07 | **05** (ionképzés: 07) |
| **D · Periódusos rács** (`KemPSE`) + `shared/kemia/elemek.js` | rács (1–4. periódus vagy teljes, f-mező nélkül), cellaszínezés családonként, kijelölés, kattintás → Z; elemadatok | 05, (07), (03) | **05** |
| **F · Reakció-réteg** (`KemRx`) | az A-ra épül: reakciószabályok (A + B → termékek, felületi szabály), energiaküszöb, ΔE (exo/endo → sebesség), katalizátorfelület, atomkönyvelés, energiadiagram | 08, 09, 10, (11) | **08** |
| **G · Labor + nagyító** (`KemLab`) | főzőpohár, kémcső, lombik, mérőhenger, büretta, fecskendő, tölcsér + szűrőpapír, bepárlócsésze, borszeszégő, Liebig-hűtő, torony; folyadékszint és -szín; **nagyító** (kis makrokör → nagy részecskeablak, vágással, „nagyítás · szemléltetés” felirattal) | 01, 02, 03, 04, 09, 10, 12, 13, 14 | **01** (desztilláló: 02) |
| **H · pH és indikátor** (`KemPH`) | pH → szín indikátoronként (színpontok + interpoláció), 0–14 skála, erős sav – erős lúg titrálási görbe | 10, 11 | **10** |
| **Tx · Képletírás** (`KemTx`) | képlet és ion a vásznon valódi alsó/felső indexszel (a fontokban nincs Unicode-index, lásd 6. fejezet), reakcióegyenlet vektoros nyíllal, tagonkénti dobozok kiemeléshez | 01, 05–10, 14 | **05** |
| **Gr · Grafikonrajzoló** | a fizika-sorozat (01-suruseg, 06-halmazallapot) grafikonjának átemelése: tengely, magyar tizedesvessző, élő görbe, húzható pont | 04, 08, 10, 14 | átvétel (04) |
| **Közös UI** | kártyák sorba rendezéshez (a `TortCards` átemelése), GHS-piktogramok, bélyegek („NE PRÓBÁLD KI”, „tanári bemutató”, „szemléltetés”), mérleg (fizika 01), időcsúszka | több | 02 (kártyák), 10 (GHS) |

### API-vázlatok

Csak a lényeg; a végleges API-t a referencialecke dönti el, és a modulblokk elején
dokumentálja. Minden rajzoló a lecke `L`-jét kapja, és szöveget **csak `L.tx` / `L.pill` /
`KemTx.tx`** útján ír (QA, review mód).

**A · Részecskemotor (`Reszecske`)**

```js
const S = Reszecske.create({
  seed: 42, dt: 1 / 120,                         // fix lépésköz → determinisztikus
  box: { x, y, w, h } | { poly: [[x,y],…] },     // tartály (sokszög is)
  species: { N2: { r: 9, m: 28, draw: 'N2' },    // draw: KemMol-sablon vagy saját fn(ctx, p)
             O2: { r: 9, m: 32, draw: 'O2' } },
  T: 293,                                         // K; a sebességskála: v_px = k·√(T/m), vizuálisan lassítva
  attract: { eps, range } | null,                 // levágott vonzás → folyadék/szilárd
  gravity: 0, collide: true,                      // collide:false → a 01 „ütközések nélkül” kapcsolója
  zones: [{ id: 'szuro', poly, pass: (sp) => sp.r < 6 }, { id: 'kat', poly, kind: 'surface' }],
  piston: { side: 'top', pos: (t) => … },         // zárt képletű dugattyú-helyzet
});
S.add('N2', 40, { region, lattice: 'hex' | 'random', vScale: 1 });
S.at(t, events)       // a szimulációt pontosan t mp-ig futtatja; events: [{t, set: {T: 350}}, {t, add: …}]
S.stats(region?)      // {n: {N2: 31, …}, vAvg, Tkin, wallHits, …}
S.draw(ctx, { alpha, clip, highlight: (p) => bool, trail: 0..1, style: 'korong' | '3d' })
S.particles           // [{id, sp, x, y, vx, vy, ang, w}] – csak olvasásra
```

**Determinizmus – Döntés.** A szerződés 8. pontja szerint az állapot a lépésindexből és
`L.st`-ből számolható. Egy valódi ütközéses szimuláció halmozott, ezért a motor
**determinisztikus visszajátszást** használ: azonos `seed` és azonos esemény-napló (a
csúszkamozgások időbélyeggel) mellett `S.at(t)` mindig ugyanazt az állapotot adja. Előre csak
továbbfut, visszafelé a legközelebbi ellenőrzőpontból (0,5 mp-enként mentve) számol újra. A
QA az `L.st` beállításával így bármely pillanatot lefotózhatja. A szilárd és a folyékony
„díszítő” halmazokhoz (rezgő rács) a fizika 06 zárt képletű megoldása (`seedMotion` +
`relax`) is elég, a motor ezt `mode: 'zart'`-ként kínálja. Teljesítménycél: ≤ 400 részecske,
térbeli rács (cella = 2r), 60 fps egy átlagos iskolai laptopon is; a QA headless
renderelésénél `S.at` gyorsabb a valós időnél.

**B · Molekula-rajzoló (`KemMol`)**

```js
KemMol.EL = { H: {c: '#f2ede2', bd: '#565d72', r: 0.55}, C: {c: '#3b4050', r: 0.77}, O: {c: '#d6452c', r: 0.73},
              N: {c: '#2f5fb3', r: 0.75}, Cl: {c: '#3e9a4b', r: 0.99}, S: {c: '#e2b62b', r: 1.02},
              Na: {c: '#8a5cc2', r: 1.1}, Fe: {c: '#a3643c'}, Cu: {c: '#c17a44'}, Ca: …, Mg: …, Al: …, Ar: … }
KemMol.tpl('H2O')                     // {atoms: [{el, x, y, z}], bonds: [[i, j, rend]], name}
KemMol.draw(ctx, mol, x, y, { scale, rot: {yaw, pitch}, style: 'kalotta' | 'palcika' | 'lewis',
                              alpha, outline: true, highlight: [i…] })
KemMol.morph(from[], to[], map, t)    // atomazonosság szerinti átrendeződés (08): kötések halványulnak/megjelennek
KemMol.chain(n, { kind: 'alkan' | 'szappan', wiggle: t })   // 13, 14
KemMol.lattice(kind, { nx, ny, cell, t, melt: 0..1 })        // 'ion' | 'fem' | 'gyemant' | 'grafit' | 'molekula'
```

Színkód: a molekulakészletek megszokott színei (H fehér, C fekete, O piros, N kék, Cl zöld, S
sárga), a világos papírhoz igazítva, **mindig sötét körvonallal**. Az oxigén piros színe
közel van a cinóber kiemelőszínhez, ezért a kiemelés ebben a sorozatban **gyűrű vagy
fényudvar** legyen, ne kitöltés (5. fejezet). A 3D-hatás: radiális fény (bal felső
csúcsfény), mélység szerinti rendezés, az `iskola/kemia-maghasadas` nukleonrajzának
mintájára. *(Az `iskola` mappa a terv írásakor ezen a gépen nem volt elérhető; ha a gyártáskor
sincs meg, a stílust a leírás alapján kell újraírni.)*

**C · Atommodell (`KemAtom`)**

```js
KemAtom.config(Z)                     // [2, 8, 1]; Z > 20 → null (a lecke jelzi: „bonyolultabb”)
KemAtom.draw(ctx, L, Z, x, y, { R: 260, charge: 0, N: null, t, nucleus: 'kupac' | 'pont',
                                 outer: 'kiemel', eAnim: {from: shell, to: shell, p: 0..1}, labels: true })
KemAtom.transfer(ctx, L, a, b, p)     // elektronátadás a → b (07), p: 0..1
KemAtom.outer(ctx, Z, x, y, r, opts)  // csak a külső héj pöttyei (a B Lewis-nézetéhez)
```

**D · Periódusos rács (`KemPSE`)** + **`shared/kemia/elemek.js`**

```js
KemPSE.layout({ x, y, cell, periods: 4 | 7, fblock: false })
KemPSE.draw(ctx, L, { fill: (Z) => color, sel: Z, show: ['Z', 's'], fade: (Z) => bool })
KemPSE.hit(px, py)                    // → Z | null
window.KEM_ELEMEK = [{ Z: 11, s: 'Na', nev: 'nátrium', A: 23, cs: 1, p: 3, fem: true,
                       csalad: 'alkalifem', hal: 'szilárd' }, …]   // 1–118
```

**Döntés:** az elemtáblázat (vegyjel, magyar név, rendszám, csoport, periódus, kerekített
relatív atomtömeg) nem leckénkénti tartalom, hanem egyszer, tanárral átnézett közös adatfájl
(mint a `shared/tort/` térképei). A review módban „kódban rögzített”-ként jelenik meg. Ami egy
leckében *állítás* (pl. a nátrium lángszíne), az a lecke `.md`-jébe kerül.

**F · Reakció-réteg (`KemRx`)**

```js
const R = KemRx.create(S, {
  rules: [{ a: 'H2O2', b: 'H2O2', to: ['H2O', 'H2O', 'O2'], Ea: 0.8, dE: +0.3 },   // dE > 0: exoterm (sebességet ad)
          { a: 'H2O2', surface: 'kat', Ea: 0.25, to: … }],
  conserve: true,                     // betöltéskor ellenőrzi, hogy minden szabály atommegmaradó
});
R.counts()        // {C: 1, H: 4, O: 4} – atomkönyvelés
R.events          // [{t, rule, x, y}] – villanáshoz, buborékszámlálóhoz
KemRx.diagram(ctx, L, { x, y, w, h, Ea, EaKat, dE, p })   // minőségi energiadiagram, haladó ponttal
```

Az energiák a szimuláció belső egységében vannak (nem kJ): az energiadiagram minőségi, ezt
a panel kimondja.

**G · Labor + nagyító (`KemLab`)**

```js
KemLab.beaker(ctx, x, y, w, h, { level: 0..1, liquid: '#…', marks: [cm³…], label })
KemLab.tube / flask / cylinder / burette / syringe(… { piston }) / funnel / dish / burner({ flame: 0..1 })
KemLab.condenser / column({ trays, T: (y) => °C })
KemLab.lens(ctx, L, { from: {x, y, r}, to: {x, y, R}, label: 'nagyítás', draw: (ctx) => {…} })
```

A nagyító mindig ugyanúgy néz ki: kis kör a makrotárgyon, két érintő vonal, nagy kör
tintakerettel, benne a részecskék, a keret mellett a „nagyítás · szemléltetés” felirat.

**H · pH és indikátor (`KemPH`)**

```js
KemPH.color('lakmusz' | 'fenolftalein' | 'voroskaposzta' | 'univerzalis', pH)   // → '#rrggbb'
KemPH.scale(ctx, L, x, y, w, { marks: [{pH, k}] })      // k: md-felirat kulcsa
KemPH.titrate({ Va, pHa, Vb, pHb })                     // → pH (erős sav + erős lúg, H⁺/OH⁻ fölöslegből)
```

Az indikátorok átcsapási tartománya a `.md`-ből jön (`range` típus), a színpontok a modulban
vannak, forrásmegjelöléssel.

**Tx · Képletírás (`KemTx`)**

```js
KemTx.tx(L, 'SO₄²⁻', x, y, o)          // o = L.tx opciói; index 0,62-es méretben, alsó +0,28 em, felső −0,42 em;
                                        // egymás fölé szedett index (₄ és ²⁻) → a felső qa:false
KemTx.eq(L, 'CH₄ + 2 O₂ → CO₂ + 2 H₂O', x, y, o)   // → {terms: [{s, box}], arrow: box}; a nyíl vektoros
KemTx.arrow(ctx, x1, y, x2, { label })               // pl. „hő”, „katalizátor” a nyíl fölött
KemTx.parse('Al₂O₃')                    // → {atoms: {Al: 2, O: 3}, charge: 0} (a build Python-párjával azonos logika)
```

### Referencialeckék – az első kör

| Referencialecke | Mit épít meg | Miért ez |
|---|---|---|
| **01-reszecskemodell** | **A** részecskemotor (visszajátszás, dugattyú, hőmérséklet, diffúzió, két fajta) · **G** nagyító + fecskendő, főzőpohár | a legtöbb lecke erre épül (9 a 14-ből), és itt derül ki, hogy a determinisztikus visszajátszás bírja-e a QA-t és a visszaléptetést |
| **05-atom-hejak** | **C** atommodell · **D** periódusos rács + `elemek.js` · **Tx** képletírás | független a részecskemotortól; a Tx-et minden további lecke használja |
| **06-molekulak** | **B** molekula-rajzoló (sablonok, 3D-golyók, Lewis-nézet, forgatás) | független a 01-től: a molekulákat állóképként és forgatva rajzolja. A 05-tel csak a „külső héj” rajzán osztozik, ezt a 06 saját, egyszerű `KemAtom.outer`-ként írja meg, és a 2. kötegben egyesítjük |

A három lecke párhuzamosan gyártható, mert a modulhatárok nem fedik egymást. A 2. köteg előtt
a B és a C „külső héj” rajzát egyesíteni kell, és az A + B összekötését (molekula-alakú
részecske a motorban) a 08 végzi el.

### Gyártási sorrend (legfeljebb 3 párhuzamos lecke kötegenként)

| Köteg | Leckék (nehézség) | Új modul | Újrahasznosított |
|---|---|---|---|
| 1 | **01-reszecskemodell** (3), **05-atom-hejak** (3), **06-molekulak** (3) | A, G (01) · C, D, Tx (05) · B (06) | – |
| 2 | **03-elem-vegyulet-keverek** (2), **07-ionok-kristalyok** (2), **08-kemiai-reakcio** (3) | B-rácsok (07) · F, A+B összekötés (08) | A, B, C, D, G, Tx |
| 3 | **02-szetvalasztas** (2), **04-oldodas** (3), **10-sav-bazis** (2) | G-desztilláló, kártyák (02) · Gr-átvétel (04) · H, GHS (10) | A, B, F, G, Tx |
| 4 | **09-eges-korrozio** (2), **11-levego** (2), **13-szappan-vizkemenyseg** (2) | B-lánc, micella (13) | A, B, F, G, H, GHS |
| 5 | **12-viztisztitas** (2), **14-koolaj** (2) | G-torony (14) | A, B, G, Gr, Tx, kártyák |

Az 1. köteg a három alapmodul referencialeckéje, mindhárom nehézségű. A 2. kötegbe azért
kerül a 08, mert az F réteg az A és a B összekötése, és a 4. köteg két leckéje is erre épül.
A 03 a legkevésbé kényes, jó próbája a B-nek egy másik kéz alatt. A 09 és a 13 (biztonsági
szempontból kényes) azért van a 4. kötegben, mert addigra a biztonsági elv (6. fejezet)
és a GHS-rajzoló a 10-ben kiforr. Minden köteg után az elkészült modult ki kell emelni a
közös könyvtárba (egyeztetve), mielőtt a következő köteg ráépül.

---

## 5. Szerkesztői elvek (a sorozat egészére)

1. **A három szint egységes jelölése.** *Makroszint*: természetes színek, tárgyak, eszközök.
   *Részecskeszint*: mindig a nagyítóban vagy egy „részecskeablakban”, tintakerettel, a
   „szemléltetés” jelzéssel. *Jelszint* (vegyjel, képlet, egyenlet): JetBrains Mono, a `KemTx`
   rajzolja. A diák így mindig tudja, melyik szinten van; a szintek közötti váltás animált
   (pl. a molekulagolyóból képlet „csúszik ki”).
2. **A modell becsületessége.** A részecskerajzon a méret, a távolság és a sebesség nem
   arányos. Ahol ez félrevezethet, a panel vagy a `> megjegyzés:` kimondja (pl. „a levegőben a
   részecskék valójában kb. 10 átmérőnyire vannak egymástól”). A Bohr-modellt modellként
   nevezzük meg. Egy lépésben csak egy egyszerűsítés legyen.
3. **Szóegyenlet először.** A tanterv szerint a jelrendszer „háttérbe szorul”, ezért minden
   reakció elsőként szavakkal jelenik meg; a képletes egyenlet kiegészítő, kisebb, és csak a
   részecskeanimáció *után* következik.
4. **Antropomorfizmus helyett energia.** „Az atom szeretne nyolc elektront” helyett: „így
   kisebb az energiája, stabilabb”. A „szeret”, „akar”, „boldog” szó nem kerülhet a panelre.
5. **Kemofóbia ellen, felelősen.** A „vegyszer” nem szitokszó: a víz és a C-vitamin is
   vegyület. Ugyanakkor a veszélyt sem bagatellizáljuk (6. fejezet, biztonsági elv).
6. **Tévhit-lépés minden leckében** a dokumentált tévhitekből (a briefekben felsorolva),
   lehetőleg egy kísérlettel cáfolva, és nem csak kimondva.

---

## 6. Build- és szerződés-kiegészítési igények

### 6.1 A helyzet (ellenőrizve)

- **A fontokban nincs Unicode-index.** A `shared/lesson.css` `unicode-range`-ei (latin +
  latin-ext) nem tartalmazzák az U+2070–209F tartományt (alsó és felső indexek: ₂, ⁺, ⁻),
  sem az U+2192 (→) és az U+21CC (⇌) jelet. Csak a ², ³, ¹ (U+00B2/B3/B9) és a ⁴ (U+2074) van
  benne. A `H₂O` tehát a panelen és a vásznon is rendszerfontra esik vissza, és a ₂ más
  betűtípussal, Windowson és Linuxon eltérően jelenik meg.
- **A build alsóindex-szabálya elrontja a képletet.** A `tools/build_lesson.py` `inline()`
  függvénye az `F_fel` mintára (`([A-Za-zρΔ])_([0-9A-Za-z…]+)`) a `H_2O`-ból `H<sub>2O</sub>`-t
  csinál, vagyis az O is indexbe kerül.
- **Számadat:** a `pH` mértékegység nélküli szám (spec: `"unit": ""`), a `0,9 tömeg%` és a
  `36 g/100 g víz` ma is működik (egységként szövegesen összevetve). Sorozatadat (görbe)
  nincs.

### 6.2 Kémiai jelölés a `.md`-ben – Döntés

- **Kanonikus alak: Unicode** (`H₂O`, `CO₂`, `Na⁺`, `Cl⁻`, `Mg²⁺`, `SO₄²⁻`, `→`). Indok: a
  tanár egy sima szövegszerkesztőben is pontosan azt látja, amit a diák. A töltés sorrendje:
  szám, majd előjel (`²⁺`), a mínusz valódi mínuszjel.
- **ASCII-bevitel kémialeckében** (spec: `"chem": true`): a build átalakítja, és minden
  átalakítást egyszer kiír (`info: H2O → H₂O (12. sor)`), hogy a tanár lássa:
  - képlet: egy szó, amely csak érvényes vegyjelekből és számokból áll, és van benne szám
    (`H2O`, `CO2`, `Al2O3`, `CaCl2`) → alsó index. A kivételeket egy rövid listával kezeli
    (`B12`, `A4`, `PM10` …), és a `\` előtag letiltja az átalakítást (`\B12`);
  - töltés: `^` jellel (`Na^+`, `Ca^2+`, `SO4^2-`) → felső index; a puszta `Na+` nem alakul át
    (a magyar kötőjeles írás miatt: `Na⁺-ion`, `Cl-atom`);
  - nyíl: `->` → `→`.
- **Kémialeckében a régi `_` szabály** `[A-Z][a-z]?_\d+[A-Z]` mintára hibát ad („képletet így
  írj: H₂O vagy H2O”), a fizikai `F_fel` jelölés változatlan.
- **Kimenet:** a panel HTML-je `<sub>`/`<sup>`-t kap **normál számjegyekkel** (amelyek benne
  vannak a fontban), valamint egy apró `.lp-text sub, .lp-text sup { font-size: .68em;
  line-height: 0 }` szabályt (a lecke `<style>`-jában, ez a szerződés szerint megengedett
  finomhangolás; később a `lesson.css`-be). A **nyíl** a panelen inline SVG lesz
  (`<svg class="nyil">`), így nem függ a fonttól. A **feliratok** (`labels`) Unicode-ban
  maradnak, a vásznon a `KemTx` bontja és rajzolja ki őket.
- **Nem kell a 7–8. évfolyamon:** a `⇌` (a kémiai egyensúly a 9–10. évfolyam anyaga; a
  telített oldatot szóban írjuk le), a **mol** és az anyagmennyiség (nem szerepel a tanterv
  fogalmai között; a lecke belül számolhat vele, de a diák nem látja). Engedélyezett
  mértékegységek: g, kg, mg, cm³, dm³, L, g/cm³, g/100 g víz, °C, tömeg%, térfogat%, ppm, nm,
  mg/L, µg/m³, kJ, MJ, kWh, nk°. A pH egység nélküli.

### 6.3 Új adattípusok és validálás (`tools/build_lesson.py`)

| típus | `.md`-ben | kimenet (`L.dat(k)`) | validálás |
|---|---|---|---|
| `formula` | `- víz képlete: H₂O` (vagy `H2O`) | `{t: 'formula', s: 'H₂O', atoms: {H: 2, O: 1}, charge: 0}` | vegyjelek az `elemek.js` listájából; ha a spec megadja az `"atoms"`-t, egyeznie kell vele (a képlet a golyómodellt is vezérli, ezért egy elírt `CH3` hiba) |
| `equation` | `- metán égése: CH₄ + 2 O₂ → CO₂ + 2 H₂O` | `{t: 'equation', s, lhs: [{k: 1, f: 'CH₄', atoms}], rhs: […]}` | **atom- és töltésmérleg**: „nincs kiegyenlítve: bal oldalon 4 O, jobb oldalon 3 O” – ez hiba; a nyíl kötelező |
| `series` | `- KNO₃ oldhatósága: 0 °C: 13,3 · 20 °C: 31,6 · 40 °C: 63,9` | `{t: 'series', x: [0, 20, 40], y: [13.3, 31.6, 63.9], ux: '°C', uy: 'g/100 g víz', s}` | x szigorúan nő, egységek a spec szerint, min/max mindkét tengelyre |
| `number` (meglévő) | `- citromlé pH-ja: 2,3` | változatlan | spec: `"unit": "", "min": 0, "max": 14` |
| `range` (meglévő) | `- lakmusz átcsapása: 4,5–8,3` | változatlan | – |

A szóegyenlet („metán + oxigén → szén-dioxid + víz”) sima felirat; a build csak arra
figyelmeztet, ha egy `egyenlet`-re végződő kulcsú feliratban nincs `→`. Az egyenletvalidálás
kb. 80 sor Python (képletelemző zárójelekkel: `Ca(OH)₂`, `CH₃COOH`; kristályvíz `·` nélkül –
erre a 7–8. évfolyamon nincs szükség), öntesztekkel a `tools/tests/` alatt.

### 6.4 QA-kiegészítés (`tools/qa_lesson.py`)

- **Glifellenőrzés:** figyelmeztetés minden vászon- és panelszövegre, amelyben a fontok
  `unicode-range`-én kívüli karakter van (visszaesés rendszerfontra). Ez a kémián kívül is
  hasznos (π, ≈, ⇌).
- **Szimulációs determinizmus:** a QA ugyanazt a lépést kétszer fotózza (`--at settle` kétszer,
  közte egy oda-vissza léptetéssel), és pixelkülönbséget mér. Ha van eltérés, a
  részecskemotor nem determinisztikus.

### 6.5 Javasolt „Kémia-kiegészítés” a `SZERZODES.md`-hez (kész szöveg)

> Az alábbi fejezet a `leckek/SZERZODES.md` 12. pontjaként illeszthető be a felhasználó
> jóváhagyása után. Ez a terv nem módosítja a szerződést.

```markdown
## 12. Kémia-kiegészítés (7–8. évfolyam)

Kémialeckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:**
`pilot/kemia-7-8/terv.md` 5. fejezet (szerkesztői elvek) és a saját briefed a 3. fejezetben.

- **Mappa, fejléc:** `leckek/kemia-7-8/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Kémia · évfolyam: 7–8. · témakör: N. <a kerettanterv témakörének címe>`.
  A spec-be: `"chem": true` (kémiai jelölés a buildben).
- **Három szint, egységes jelöléssel.** Makroszint: tárgyak természetes színekkel.
  Részecskeszint: **csak** nagyítóban vagy részecskeablakban (`KemLab.lens`), tintakeret,
  „nagyítás · szemléltetés” felirat (a `.md`-ből). Jelszint: vegyjel, képlet, egyenlet
  JetBrains Monóval, `KemTx`-szel.
- **Képletek a `.md`-ben Unicode-dal:** `H₂O`, `CO₂`, `Na⁺`, `Cl⁻`, `Mg²⁺`, `SO₄²⁻`, nyíl `→`.
  ASCII-ként is beírható (`H2O`, `Na^+`, `SO4^2-`, `->`), a build átalakítja és kiírja.
  A vásznon képletet és iont **csak `KemTx.tx`/`KemTx.eq`** írjon (a fontokban nincs
  Unicode-index; a `L.tx('H₂O')` rendszerfontra esik vissza). A panelen a build `<sub>`/`<sup>`-t
  készít; ne írj saját megoldást.
- **Szóegyenlet először.** Minden reakció elsőként szavakkal jelenik meg
  („metán + oxigén → szén-dioxid + víz”); a képletes egyenlet kiegészítő, és `equation`
  típusú adat, hogy a build ellenőrizze a kiegyenlítést. Mol, anyagmennyiség, ⇌ nincs.
- **Magyar kémiai nevek** (AkH. és a kémiai nevezéktan szerint): szén-dioxid, nátrium-klorid,
  hidrogén-peroxid, kalcium-karbonát; az ionok egy szóban: nátriumion, kloridion, oxidion,
  hidroxidion, hidrogénion; a jeles alak kötőjeles: Na⁺-ion. Halmazállapot: szilárd, folyékony,
  légnemű (gáz). Az ionvegyületnél ne írj „molekulát” (a konyhasó ionrácsos: „részecske”,
  „ion”, „kristály”).
- **Atomszínek** a `KemMol.EL` szerint, minden leckében ugyanúgy (H fehér, C fekete, O piros,
  N kék, Cl zöld, S sárga, Na lila), mindig sötét körvonallal. A **kiemelés** ebben a
  sorozatban gyűrű vagy fényudvar (cinóber `#c8401c`), ne kitöltés, mert összetéveszthető az
  oxigén pirosával.
- **A modell becsületessége.** A részecskerajz mérete, távolsága, sebessége nem arányos: ahol
  ez félrevezethet, a panel vagy a `> megjegyzés:` mondja ki. A Bohr-modell „modell”, a
  körpálya szemléltetés. Antropomorf szó („szeretne”, „akar”) nem kerülhet a panelre:
  „stabilabb, kisebb az energiája”.
- **Biztonsági elv (kötelező):**
  - Veszélyes kísérletet (durranógáz, nátrium vízben, klórgáz, benzingőz, olajtűz vízzel,
    metanol, tömény sav/lúg hígítása, otthoni lepárlás) **soha nem mutatunk követendő
    receptként**: nincs mennyiség, nincs lépésenkénti útmutató, és nincs látványos robbanás
    vagy gázfelhő mint jutalom. A jelenet a *veszély okát* mutatja részecskeszinten,
    sematikusan, „NE PRÓBÁLD KI” bélyeggel; tanári kísérletnél „tanári bemutató” bélyeggel.
  - Otthon elvégezhetőként csak konyhai anyagokkal végzett kísérlet szerepelhet (só, cukor,
    ecet, szódabikarbóna, citromsav, vöröskáposzta, étolaj), és ott is: nem kóstoljuk, nem
    szagoljuk közvetlenül, a szemet védjük.
  - A helyes cselekvést írjuk (fedővel oltás, szellőztetés, 112), és nem a hibát részletezzük.
  - Veszélyességi jel csak valósághű GHS-piktogram lehet (piros keretes rombusz), a valódi
    jelentésével; a közös GHS-rajzolót használd.
  - A bélyegek (`NE PRÓBÁLD KI`, `tanári bemutató`, `szemléltetés`) a `.md`-ből jönnek
    (felirat-kulcs), a történelmi bélyeg stílusában (`L.pill`, Bricolage 22 px, −3°), keret:
    „NE PRÓBÁLD KI” a rossz `#b3261e`, a többi halvány tinta.
  - Biztonsági állítást (gyulladási hőmérséklet, határérték) forrással adj meg a `.md`
    `<!-- -->` megjegyzésében; a tanári review ezt külön nézi.
- **Részecskeszimuláció:** a `Reszecske` motort használd determinisztikus visszajátszással
  (`S.at(L.st, events)`); a csúszka- és gombeseményeket időbélyeggel naplózd, az `enter(L)`
  ürítse a naplót. Ne léptesd a szimulációt `L.dt`-vel képkockánként.
- **Új közös modulok leckén belül** a történelem-kiegészítés szabálya szerint: külön,
  jól elhatárolt blokkban (`/* ── MODUL: … ── */ … /* ── MODUL VÉGE ── */`), saját névtérrel
  (`Reszecske`, `KemMol`, `KemAtom`, `KemPSE`, `KemRx`, `KemLab`, `KemPH`, `KemTx`), a blokk
  elején API-leírással, lecke-specifikus hivatkozás nélkül.
- **Minden `.md`** végén `<!-- Modell-egyszerűsítések és források: … -->` blokk: mit
  egyszerűsít a modell, és honnan valók a nem közismert adatok.
```

---

## 7. Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / fejlesztési feladat |
|---|---|---|
| 1. A kísérleti megfigyeléstől a modellalkotásig (17) | 01, 02, (10: veszélyességi jelek, 09: biztonság) | **a laboratórium felépítése, eszközei és a balesetvédelmi szabályok** – az eszközök a leckékben szerepelnek, de nincs róluk külön lecke (tanórai tevékenység); a tömeg- és térfogatmérés, a sűrűség (a fizika `01-suruseg` lefedi); a víz körforgása csak érintőlegesen (01, dér) |
| 2. Az anyagi halmazok (17) | 03, 04, (01: diffúzió) | a fizikai tulajdonságok rendszerezett összevetése (anyagismereti kártyák) csak a 03 nagyítójában; **az ötvözetek** csak példaként (sárgaréz, rozsdamentes acél a 09-ben); a térfogatszázalék csak az alkoholnál (01, 02) |
| 3. Atomok, molekulák és ionok (14) | 05, 06, 07 | az elemi részecske és a kémiai részecske megkülönböztetése csak a 05 egyik lépésében; a vegyjelek eredete és a vegyjel-játékok; a periódusos rendszer 4. periódus utáni része csak cellaként |
| 4. Kémiai reakciók (20) | 08, 09, 10 | **a fotoszintézis** csak endoterm példaként a 08-ban (a biológia 7–8. sorozatra hagyjuk); csapadékképződés csak a 13-ban (vízlágyítás); a gázfejlődés kimutatása (parázsló gyújtópálca) csak említésként |
| 5. Kémia a természetben (15) | 11, 12, (14: fosszilis) | **a kőzetburok anyagai, az ásványok**; **a hulladék, a veszélyes hulladék, a szelektív gyűjtés és az újrahasznosítás** (csak a 14 műanyag-lépésében); a megújuló energiaforrások kémiai háttere; a trágya csak nitrátként (12); a saját település környezetvédelmi kérdése (kiselőadás) |
| 6. Kémia a mindennapokban (19) | 13, 14 | **az élelmiszerek összetevői** (tápanyagok, E-számok, adalékok); **a káros szenvedélyek** (alkohol, metanol, dohány, drogok – szándékosan kihagyva, 1. fejezet); a gyógyszercímke; **az építőanyagok** (mész, cement, üveg); **a fémek előállítása** (vas, alumínium); a fertőtlenítőszerek csak a hypo kapcsán; a műtrágya és a növényvédő szerek |

A sáv általános céljai közül jól lefedett: a részecskeszemlélet, a makro- és a részecskeszint
megkülönböztetése, a modellalkotás, a tévhitek ütköztetése, a „természetes és mesterséges
ugyanaz” elv (03, 14). Gyengén lefedett: a kísérletezés manuális része, az információkeresés,
a prezentáció és a vita (ezek tanórai tevékenységek; a leckék legfeljebb alapot adnak hozzájuk:
10 – szúnyogcsípés, 14 – „Áldás vagy átok a műanyag?”).

**Tartalék-jelöltek**, ha a pilot után folytatódik a sor (a vastagon szedett hiányok miatt,
fontossági sorrendben):

1. `mesz-korforgasa` – mészkő → égetett mész → oltott mész → mészkő: egyesülés és bomlás
   körben, építőanyagok (B, F, G).
2. `vasgyartas` – a nagyolvasztó: az ércből fém, a korrózió „visszafelé” (F, G).
3. `metanol-etanol` – két majdnem egyforma molekula, nagyon különböző hatás. Egy
   mérgezéshez kötődő, prevenciós lecke, egészségnevelési szakértővel egyeztetve (B).
4. `tapanyagok` – szénhidrát, zsír, fehérje golyómodellben; energiatartalom és címke (B).
5. `hulladek` – mi lesz a szemétből: szelektív gyűjtés, újrahasznosítás, komposzt (kártyák).
6. `fotoszintezis` – a biológia-sorozattal közösen (A, F).

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): a PhET kémiai szimulációi
(*States of Matter*, *Build an Atom*, *Build a Molecule*, *Molecule Shapes*, *Sugar and Salt
Solutions*, *pH Scale*, *Reactants, Products and Leftovers*, *Balancing Chemical Equations*),
részben magyarul is. A Nemzeti Köznevelési Portál (NKP) 7–8. osztályos kémiatankönyvei
feladatokkal. A katasztrófavédelem tűz- és CO-megelőzési oktatóanyagai (09). Érdemes
mindegyiket megnézni a gyártás előtt, hogy egy leckét ne csináljunk újra feleslegesen.
