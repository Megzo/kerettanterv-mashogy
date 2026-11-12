# Pilot: Fizika 7–8. – a leckesor terve

Forrás: [`kerettanterv/fizika/7-8.md`](../../kerettanterv/fizika/7-8.md) (NAT 2020, általános
iskola, 10 témakör, 102 óra). Az idézetek szó szerint onnan valók.

## 1. Bevezető

A pilot **16 leckéje** a 7–8. osztályos fizika-kerettanterv mind a 10 témakörét érinti. Egy
lecke kb. egy tanórai „kulcsjelenetet” dolgoz fel (5–8 lépés, 1920×1080 színpad, bal oldalt
animáció/szimuláció, jobb oldalt magyarázó panel), **világos, papírszerű háttéren sötét
szöveggel**.

**Kiválasztási elv.**

1. **Arányosság:** nagyjából óraszám szerint, kb. 6–7 óránként egy lecke. A 14 órás témakörök
   (víz-levegő, elektromosság) kettőt kapnak, a 6 órás (globális problémák) egyet.
2. **Ott animálunk, ahol az animáció tényleg többet ad**, mint a tankönyv vagy egy videó:
   láthatatlan dolgok (részecskék, elektronok, infravörös sugárzás), egyszerre több nézőpont
   (űrből és a földről), csúszkával felfedezhető összefüggések (mitől *nem* függ a lengésidő),
   és dokumentált tévhitek, amelyeket egy jól megválasztott kép megcáfol. A mérés,
   tudománytörténet, prezentációkészítés és anyaggyűjtés jellegű tanulási eredményeket
   szándékosan kihagyjuk; ezek tanórai tevékenységek, nem animációk.
3. **Építőkockák újrahasznosítása:** a leckéket úgy választottuk, hogy kb. 8 közös modulra
   épüljenek (lásd 4. fejezet).

A leckék sorszáma a kerettanterv sorrendjét követi; a **gyártási sorrend** ettől eltér
(4. fejezet). Az „Adatok” pontokban szereplő számok a tartalomfájl „Adatok” rétegébe
kerülnek. A *(frissítendő)* jelzésű értékek évről évre változnak (árak, CO₂), ezeket a gyártás
előtt még ellenőrizni kell.

## 2. A leckék

| # | slug | cím | témakör | nehézség (1–3) |
|---|---|---|---|---|
| 01 | `01-suruseg` | Miért úszik a jég? – a sűrűség | 1 (+5) | 2 |
| 02 | `02-energia` | Hová lesz az energia? – energiaátalakulások | 2 | 2 |
| 03 | `03-mozgas-fekezes` | Miért kell bekötni az övet? – sebesség, tehetetlenség, fékezés | 3 | 2 |
| 04 | `04-lendulet-raketa` | Hogyan repül a rakéta? – lendület és kölcsönhatás | 4 | 2 |
| 05 | `05-inga` | Mitől függ a hinta lengésideje? – periodikus mozgás | 4 (+1) | 1 |
| 06 | `06-halmazallapot` | Miért nem melegszik tovább a forrásban lévő víz? – halmazállapot-változások | 5 | 3 |
| 07 | `07-felhajtoero` | Miért úszik az acélhajó? – nyomás és felhajtóerő | 5 | 2 |
| 08 | `08-aramkor` | Mi folyik a drótban? – töltés, áram, Ohm-törvény | 6 | 3 |
| 09 | `09-aram-otthon` | Miért old le a biztosíték? – Joule-hő, teljesítmény, fogyasztás | 6 + 2 | 2 |
| 10 | `10-arnyek-tukor` | Hol van a tükörkép? – árnyék és visszaverődés | 7 | 2 |
| 11 | `11-lencse-szem` | Miért kell szemüveg? – lencsék és a látás | 7 | 3 |
| 12 | `12-hullam-hang` | Mitől magas a hang? – hullámok és hang | 8 | 2 |
| 13 | `13-szinek` | Miért kék az ég? – a fény és a színek | 8 (+7) | 2 |
| 14 | `14-uveghaz` | Miért melegszik a Föld? – az üvegházhatás | 9 (+1) | 2 |
| 15 | `15-fold-forgasa` | Miért van nappal és éjszaka? – a Föld forgása és keringése | 10 | 3 |
| 16 | `16-holdfazisok` | Miért változik a Hold alakja? – holdfázisok és fogyatkozások | 10 (+7) | 2 |

Nehézség = gyártási nehézség: 1 = egyszerű fizika, kevés elem; 2 = egy közepes szimuláció
vagy új modul; 3 = összetett szimuláció, több szinkron nézet vagy kényes pontosság.

Témakörönként: 1 → 1 · 2 → 1 (+ a 09 fele) · 3 → 1 · 4 → 2 · 5 → 2 (+ a 01 egy része) ·
6 → 2 · 7 → 2 · 8 → 2 · 9 → 1 · 10 → 2.

---

## 3. Briefek

### 01 · `01-suruseg` – Miért úszik a jég? – a sűrűség

*Párhuzamosan már készül, a motorral együtt. Ez a brief csak a sorozatba illesztést mutatja,
eltérés esetén a gyártó ügynök terve az irányadó.*

- **Tanulási cél:** Az azonos anyagú testek tömege egyenesen arányos a térfogatukkal, a
  hányadosuk (a sűrűség) az anyagra jellemző. A jég azért úszik, mert fagyáskor kitágul, és
  ezért kisebb lesz a sűrűsége.
- **Kerettanterv:** „Azonos anyagból készült különböző tömegű testek tömegének és térfogatának
  kapcsolata. Az anyagra jellemző sűrűség megállapítása” · „Sűrűségadatok használata a tömeg
  vagy térfogat kiszámolására” · (5.) „A téli fagy romboló erejének fizikai magyarázata”.
- **Tévhitek:** „ami nehéz, elsüllyed” (a tömeget keverik a sűrűséggel). Egy nagyobb darabnak
  nagyobb a sűrűsége. A jég „ugyanaz a víz”, tehát ugyanolyan sűrű.
- **Kulcsvizuál:** különböző méretű kockák a mérlegen, a pontjaik az m–V grafikonon egy
  origón átmenő egyenesre esnek; minden anyagnak saját meredeksége van.
- **Interaktív:** a kocka élhossza csúszkával, az anyag választható; a testek a vízbe
  húzhatók, és látszik, mekkora részük merül be.
- **Lépések:** Nehéz vagy sűrű? · Mérleg és mérőhenger · Az m–V egyenes · Anyagok sűrűsége ·
  Úszik vagy elmerül? · Fagyáskor tágul a víz · Szétfagyott palack, úszó jéghegy.
- **Adatok:** víz 1,00 g/cm³ (= 1000 kg/m³); jég 0,917 g/cm³, tehát fagyáskor kb. 9 %-kal nő
  a térfogat. Édesvízben 92 %, tengervízben (1,025 g/cm³) kb. 89 % merül be. Vas 7,87 · alumínium
  2,70 · arany 19,3 · higany 13,5 · étolaj ≈ 0,92 · fenyő ≈ 0,5 g/cm³; levegő ≈ 0,0012 g/cm³.
- **Építőkocka:** A (tartály + úszás), B (grafikon), mérleg.

### 02 · `02-energia` – Hová lesz az energia? – energiaátalakulások

- **Tanulási cél:** Az energia egyik formából a másikba alakul, az összege nem változik. Amit
  „elveszni” látunk, az belső energia (melegedés) lesz.
- **Kerettanterv:** „előidéz egyszerű energiaátalakulással járó folyamatokat (melegítés,
  szabadesés), megnevezi az abban szereplő energiákat” · „A rugalmas energia mozgási energiává
  alakulásának (rugós eszközzel kilőtt golyó), a helyzeti energia mozgási energiává alakulásának
  (zuhanó test) megfigyelése” · „Az erőművekben bekövetkező energiaátalakulások vizsgálata, az
  energia megmaradása”.
- **Tévhitek:** az energia „elfogy” vagy „elhasználódik”. Energiája csak annak van, ami mozog.
  A nehezebb test gyorsabban esik.
- **Kulcsvizuál:** egy golyó gurul egy félcső alakú pályán, mellette élő energiaoszlopok
  (rugalmas, helyzeti, mozgási, belső). Az oszlopok összege mindig ugyanakkora; súrlódáskor a
  „belső” oszlop nő, és a pálya felmelegszik (meleg színárnyalat).
- **Interaktív:** az indítási magasság húzható, a súrlódás és a tömeg csúszkával állítható.
  Felfedezés: a pálya alján a sebesség nem függ a tömegtől.
- **Lépések:** Rugós kilövő · Fel a lejtőn · Zuhanás · Nehéz és könnyű golyó · Súrlódás: a
  dörzsölt tenyér · Az összeg állandó · Erőművi lánc (hő-, víz-, szél-, naperőmű).
- **Adatok:** g = 9,81 m/s²; E_h = m·g·h, E_m = ½·m·v². 1 kg, 2 m → 19,6 J; v = √(2gh) =
  6,3 m/s, tömegtől függetlenül. Hatásfok (kerekítve): hőerőmű 35–40 %, atomerőmű ≈ 33 %,
  gázturbinás kombinált ciklus ≈ 55–60 %, vízerőmű 85–90 %, szélturbina 35–45 % (elméleti
  felső határ 59 %), napelem 18–23 %.
- **Építőkocka:** C (1D mechanika + energiaoszlopok).
- **Meglévő anyag:** a PhET *Energy Skate Park* ugyanezt jól megmutatja. Nálunk az erőművi lánc
  és a „hová lesz?” kérdés kap hangsúlyt.

### 03 · `03-mozgas-fekezes` – Miért kell bekötni az övet? – sebesség, tehetetlenség, fékezés

- **Tanulási cél:** Az átlagsebesség az összes út osztva az összes idővel. A test a
  mozgásállapotát csak erő hatására változtatja meg. A megállási út a reakcióútból és a
  fékútból áll, és a sebességgel gyorsabban nő, mint egyenesen arányosan.
- **Kerettanterv:** „Különbséget tesz az út és elmozdulás fogalma között. Ismeri, és ki tudja
  számítani az átlagsebességet” · „ismeri az erő szerepét egy mozgó test megállításában,
  elindításában” · „A légzsák és a biztonsági öv működésének fizikai magyarázata” · „Az
  önvezérelt autó működési elve”.
- **Tévhitek:** a mozgás fenntartásához folyamatos erő kell (impetus-elképzelés). Az
  átlagsebesség a sebességek átlaga. Ütközéskor egy erő „előrelöki” az utast.
- **Kulcsvizuál:** felülnézetben autó halad az úton, és fékez a zebra előtt. Az úttesten két
  sáv rajzolódik ki: a reakcióút (kék) és a fékút (vörös). Egy be nem kötött bábu tovább halad.
- **Interaktív:** csúszkával állítható a sebesség (30–130 km/h), a reakcióidő (0,5–2 s,
  „telefonozik”) és az útburkolat (száraz, vizes, jeges); egy gombbal bekapcsolható az
  „önvezető mód”.
- **Lépések:** Út és elmozdulás a térképen · Átlagsebesség: a megállók is számítanak ·
  Tehetetlenség (Newton I.) · Erő, tömeg, gyorsulás (Newton II.) · Reakcióút + fékút ·
  Önvezető autó · Öv és légzsák: hosszabb fékezés, kisebb erő.
- **Adatok:** reakcióidő ≈ 1 s (0,7–1,5 s). Lassulás: száraz aszfalton ≈ 7 m/s², vizesen
  ≈ 5 m/s², jégen ≈ 1 m/s². Megállási út száraz úton, 1 s reakcióidővel: 50 km/h → 13,9 +
  13,8 ≈ 28 m; 90 km/h → 25 + 45 ≈ 70 m; 130 km/h → 36 + 93 ≈ 129 m. Egy 50 km/h-s ütközés kb.
  10 m-es zuhanásnak felel meg. KRESZ: 50 / 90 / 110 / 130 km/h.
- **Építőkocka:** C (jármű-kinematika), B (út–idő grafikon).

### 04 · `04-lendulet-raketa` – Hogyan repül a rakéta? – lendület és kölcsönhatás

- **Tanulási cél:** A lendület p = m·v. Ütközéskor a testek lendülete átadódik, de az összeg
  nem változik. Az erők mindig párban lépnek fel: a rakéta hátralöki a gázt, a gáz előrelöki a
  rakétát.
- **Kerettanterv:** „A lendület kiszámítása, a lendület megmaradásának vizsgálata néhány
  hétköznapi helyzetben” · „A rakéta mozgásának kísérleti vizsgálata (léggömb-rakéta), fizikai
  magyarázata. Newton harmadik törvénye”.
- **Tévhitek:** ütközéskor a nagyobb vagy gyorsabb test nagyobb erőt fejt ki (ezt az FCI-teszt
  is méri). A rakétának „el kell rugaszkodnia” a levegőtől, ezért az űrben nem működne. A mozgó
  test „erőt hordoz”.
- **Kulcsvizuál:** két kocsi egy sínen, mindkettőn lendületnyíl; alattuk egy összegnyíl,
  amelynek a hossza az ütközés alatt sem változik. Érintkezéskor két egyforma, ellentétes
  erőnyíl villan fel.
- **Interaktív:** a tömegek és a kezdősebességek csúszkával állíthatók; váltógomb: „rugalmas”
  vagy „összetapad”. A léggömbrakétánál gázrészecskék áramlanak ki; egy gombbal elvehető a
  levegő („világűr”), és a rakéta így is gyorsul.
- **Lépések:** Mi a lendület? · Ütközés: átadódik · Az összeg állandó · Összetapadó kocsik ·
  Két korcsolyázó ellöki egymást · Léggömbrakéta · Rakéta a légüres térben.
- **Adatok:** p mértékegysége kg·m/s. Teniszlabda 58 g, 50 m/s → 2,9 kg·m/s; bowlinggolyó
  7 kg, 8 m/s → 56 kg·m/s. Egymást ellökő korcsolyázók: 60 kg és 40 kg, sebességarányuk 2 : 3.
  Rakéta-gázkiáramlás 2,5–4,5 km/s.
- **Építőkocka:** C (1D ütközés, vektornyilak), D (egyszerű részecskeáram).

### 05 · `05-inga` – Mitől függ a hinta lengésideje? – periodikus mozgás

- **Tanulási cél:** Az inga lengésideje (kis kitérésnél) csak a hosszától függ, a tömegtől és
  a kitéréstől nem. Négyszer hosszabb inga kétszer lassabban leng.
- **Kerettanterv:** „egyszerű eszközökkel létrehoz periodikus mozgásokat, méri a
  periódusidőt, fizikai kísérleteket végez azzal kapcsolatban, hogy mitől függ a periódusidő” ·
  „A periódusidőt befolyásoló tényezők azonosítása.” · (1.) „A mérés pontosságának becslése
  ismételt mérések […] ismeretében”.
- **Tévhitek:** a nehezebb inga gyorsabban leng. A nagyobb kitérés jóval hosszabb lengésidőt
  ad. Ha a hintán felállsz, attól nem változik semmi (pedig a tömegközéppont feljebb kerül, az
  inga rövidül, a lengés gyorsul).
- **Kulcsvizuál:** két inga egymás mellett, mindkettő nyomot húz egy görgetett idő–kitérés
  grafikonon. A görbék fázisa csak akkor csúszik el, ha a hosszuk különbözik.
- **Interaktív:** csúszka a hosszra (0,25–2,5 m), a tömegre és a kitérésre. „Mérj!” gomb:
  stopper 10 lengésre; a diák saját mérései szóródnak, ebből látszik az átlagolás értelme. A
  Hold gombbal g = 1,62 m/s² lesz.
- **Lépések:** Ismétlődő mozgások · Periódusidő, rezgésszám, amplitúdó · Mérjünk 10 lengést ·
  Nehezebb test? · Nagyobb kitérés? · Hosszabb kötél · A hinta a Holdon.
- **Adatok:** T = 2π·√(l/g). 0,25 m → 1,00 s; 1 m → 2,01 s; 2,5 m → 3,17 s (a Holdon 1 m →
  4,94 s). Nagy kitérésnél: 30° → +1,7 %, 60° → +7,3 %, 90° → +18 %. Rezgésszám f = 1/T (Hz).
- **Építőkocka:** C (integrátor), B (görgetett grafikon), stopper widget.
- **Meglévő anyag:** a PhET *Pendulum Lab* ezt jól lefedi. Nálunk a hangsúly a saját mérésen
  és a „mitől *nem* függ” kérdésen van.

### 06 · `06-halmazallapot` – Miért nem melegszik tovább a forrásban lévő víz? – halmazállapot-változások

- **Tanulási cél:** A halmazállapotok a részecskék elrendeződésével és mozgásával
  magyarázhatók. Olvadás és forrás közben a hőmérséklet nem nő, mert a felvett energia a
  részecskék közti kötések bontására fordítódik.
- **Kerettanterv:** „A halmazállapotok és halmazállapot-változások értelmezése az anyagot
  alkotó részecskék (apró golyók) egyszerű modelljének felhasználásával” · „A jég olvadásának
  és a víz fagyásának kísérleti vizsgálata, a hőmérséklet időbeli változásának megfigyelése” ·
  „A víz forrásának kísérleti megfigyelése, a hőmérséklet mérése: forráspont, vízgőz”.
- **Tévhitek:** melegítéskor maguk a részecskék tágulnak vagy olvadnak meg. A forrásban lévő víz
  buborékjai levegőből állnak. Ha erősebb a láng, a forrásban lévő víz is melegebb lesz. A hő
  és a hőmérséklet ugyanaz.
- **Kulcsvizuál:** fazék a főzőlapon. Mellette nagyítóablakban a részecskék: rácsban rezegnek,
  aztán elcsúsznak egymáson, végül kirepülnek. Jobbra élő hőmérséklet–idő grafikon a 0 °C-os és
  a 100 °C-os platóval.
- **Interaktív:** csúszkával a főzőlap teljesítménye és a víz tömege. A diák azt látja, hogy
  ettől a platók *hossza* változik, a *magassága* nem.
- **Lépések:** Szilárd: rezgő rács · Melegítés · Olvadás: áll a hőmérő · Folyadék melegszik ·
  Forrás: a buborék vízgőz · Mitől gyorsabb a melegítés? · Párolgás és lecsapódás.
- **Adatok:** fajhő: víz 4,18 kJ/(kg·°C), jég 2,1 kJ/(kg·°C). Olvadáshő 334 kJ/kg,
  forráshő 2260 kJ/kg. Forráspont 100 °C (1013 hPa), a Kékesen ≈ 96–97 °C. Egy 2000 W-os
  forralóval 1 kg víz 20 → 100 °C kb. 2,8 perc, teljes elforralása további kb. 19 perc.
- **Építőkocka:** D (részecskeszimuláció kötésekkel), B. Az `iskola/fizika-hutes` párolgási
  részecskéi kiindulásnak jók.
- **Meglévő anyag:** PhET *States of Matter*.

### 07 · `07-felhajtoero` – Miért úszik az acélhajó? – nyomás és felhajtóerő

- **Tanulási cél:** A nyomás az erő és a felület hányadosa. A víz nyomása a mélységgel nő, és
  minden irányban egyforma. A felhajtóerő a kiszorított víz súlya, ezért úszik az üreges
  acélhajó.
- **Kerettanterv:** „A hidrosztatikai nyomás kísérleti vizsgálata, a mélységtől való függés és
  az iránytól való függetlenség felismerése” · „Az acélból készült hajók úszásának fizikai
  magyarázata, a sűrűségfeltétellel és Arkhimédész-törvényének segítségével” · „Az álló, ülő,
  fekvő ember által a talajra kifejtett nyomás becslése”.
- **Tévhitek:** a teljesen bemerült testre mélyebben nagyobb felhajtóerő hat. A nyomás csak
  lefelé hat. Több víz az edényben nagyobb felhajtóerőt ad. Ami nehéz, elsüllyed.
- **Kulcsvizuál:** egy acéltömb morfolódik hajótesté: a tömege ugyanaz marad, a kiszorított
  víz egyre több. A kiszorított víz egy mérőedénybe folyik át, és a mérlegen pont annyi, mint a
  hajó súlya.
- **Interaktív:** egy nyomásmérő szonda mélysége húzható, és el is forgatható (a kijelzett érték
  nem változik). A morfoló csúszka a lemezből hajót formál. A „Rakomány” gombbal addig pakolunk,
  amíg a hajó el nem süllyed. A Cartesius-búvárt össze lehet nyomni.
- **Lépések:** Nyomás: tűsarok vagy elefánt · Mélyebben nagyobb · Minden irányban egyforma ·
  Felhajtóerő = kiszorított víz súlya · Úszás, lebegés, elmerülés · Acélból hajó ·
  Cartesius-búvár.
- **Adatok:** p = F/A (Pa = N/m²), p_h = ρ·g·h. 10 m víz ≈ 98 kPa ≈ 1 légköri nyomás
  (101,3 kPa); a Mariana-árok alján (≈ 10 900 m) ≈ 1100 bar. Acél 7,85 g/cm³: 1 m³ acél
  elsüllyed, 7,85 m³-t kiszorító hajótestként úszik. Álló diák (50 kg, 2 × 150 cm²) ≈ 16 kPa;
  tűsarok (1 cm², fél testsúly) ≈ 3 MPa; elefánt ≈ 0,1 MPa.
- **Építőkocka:** A (tartály + úszás, a 01-ből), mérleg.
- **Meglévő anyag:** PhET *Buoyancy*, *Under Pressure*.

### 08 · `08-aramkor` – Mi folyik a drótban? – töltés, áram, Ohm-törvény

- **Tanulási cél:** Elektromos állapotban a testben elektrontöbblet vagy elektronhiány van. Az
  áram a töltések áramlása egy zárt körben. A feszültség hajtja, az ellenállás korlátozza:
  I = U/R.
- **Kerettanterv:** „ismeri az elektromos állapot fogalmát, kialakulását, és megmagyarázza azt
  az anyagban lévő töltött részecskék […] segítségével” · „szemléletes képe van az elektromos
  áramról, ismeri az elektromos vezetők és szigetelők fogalmát” · „használja a feszültség,
  áramerősség, ellenállás mennyiségeket egyszerű áramkörök jellemzésére”.
- **Tévhitek:** az izzó „elhasználja” az áramot, ezért visszafelé kevesebb folyik. Az
  elektronok a telepből jönnek, a telep „tárolja” őket. Egy vezeték is elég. Az elektronok
  fénysebességgel száguldanak.
- **Kulcsvizuál:** zárt áramkör, amelynek a vezetékében mindenütt egyszerre indulnak el a
  pöttyként rajzolt elektronok (mint egy kerékpárlánc). Az izzó előtt és után elhelyezett két
  ampermérő ugyanazt mutatja.
- **Interaktív:** a telep feszültsége választható (1,5, 4,5 vagy 9 V); a grafitbél hossza
  húzható; van kapcsoló, a LED pedig potenciométerrel szabályozható. Az ampermérő bárhová
  áthúzható.
- **Lépések:** Dörzsöléskor elektronok vándorolnak · Vezető és szigetelő · Zárt áramkör · Az
  áram nem fogy el · Feszültség · Ellenállás: a grafitbél · Ohm-törvény · LED és
  potenciométer.
- **Adatok:** elemek: ceruzaelem 1,5 V, laposelem 4,5 V, 9 V-os elem; hálózat 230 V, 50 Hz.
  Elektron töltése 1,6·10⁻¹⁹ C. Az elektronok sodródási sebessége 1 mm²-es rézhuzalban, 1 A
  mellett ≈ 0,07 mm/s. Piros LED: ≈ 2 V és 10–20 mA, 9 V-ról ≈ 330 Ω előtét-ellenállás kell.
- **Építőkocka:** E (áramkör-szimulátor, részecske a vezetékben).
- **Meglévő anyag:** a PhET *Circuit Construction Kit: DC* és a *Balloons and Static
  Electricity* nagyon jó. Nálunk az „áram nem fogy el” kép és a töltés–áram összekötés a
  hangsúly.

### 09 · `09-aram-otthon` – Miért old le a biztosíték? – Joule-hő, teljesítmény, fogyasztás

- **Tanulási cél:** Az áram melegíti a vezetőt (Joule-hő), ezen alapul a vasaló és a
  vízforraló. A fogyasztott energia a teljesítmény és az idő szorzata (kWh), ebből lesz a
  számla. Rövidzárnál vagy túlterhelésnél a biztosíték (kismegszakító) véd, a földelés és az
  áramvédő kapcsoló (FI-relé) pedig az embert védi.
- **Kerettanterv:** „A Joule-hő meghatározása. A vasaló, a hajszárító, a vízmelegítő működési
  elve” · „A rövidzár, a biztosíték és a földelés szerepe” · „Az emberre veszélyes feszültség
  és áramerősség értékek” · (2.) „A teljesítmény használata az energiafogyasztás
  meghatározására”.
- **Tévhitek:** a nagyobb teljesítményű készülék mindig többet fogyaszt (a teljesítményt keverik
  az energiával). Készenlétben a készülék nem fogyaszt. A biztosíték az embert védi. Csak a
  feszültség számít.
- **Kulcsvizuál:** lakás alaprajza egy közös áramkörrel. Minden bekapcsolt készülék
  hozzáadódik a vezeték áramához; a vezeték egyre melegebb színű, mellette pörög a
  fogyasztásmérő (kWh, Ft). 16 A fölött leold a kismegszakító.
- **Interaktív:** a készülékek ki-be kapcsolhatók, az idő csúszkával állítható; van
  „Rövidzár!” gomb, és van egy hibás, zárlatos készülékház földeléssel vagy anélkül.
- **Lépések:** A fűtőszál melegszik · Teljesítmény = feszültség × áramerősség · kWh és forint ·
  Izzó kontra LED · Túlterhelés · Rövidzár · Földelés és FI-relé · Áramütés.
- **Adatok:** 230 V; vízforraló 2000 W → 8,7 A, R ≈ 26 Ω; 3 perc → 0,1 kWh. Kismegszakító
  16 A (≈ 3,7 kW), FI-relé 30 mA. Az áram hatása az emberre: ≈ 1 mA érezhető, ≈ 10 mA felett nem
  lehet elengedni a vezetéket, 50–100 mA szívkamra-fibrillációt okozhat. 60 W-os izzó ≈ 8–9 W-os
  LED. Áramár: ≈ 36 Ft/kWh az átlagfogyasztásig (2523 kWh/év) *(frissítendő)*.
- **Építőkocka:** E (párhuzamos ágak), számláló widget.

### 10 · `10-arnyek-tukor` – Hol van a tükörkép? – árnyék és visszaverődés

- **Tanulási cél:** A fény egyenes vonalban terjed, ebből következik az árnyék és a félárnyék.
  A visszaverődéskor a beesési szög egyenlő a visszaverődési szöggel. A tükörkép ott van, ahonnan
  a szembe jutó sugarak látszólag jönnek: a tükör mögött, ugyanakkora távolságban.
- **Kerettanterv:** „tisztában van a fény egyenes vonalú terjedésével, szabályos
  visszaverődésének törvényével, erre hétköznapi példákat hoz” · „A síktükörben látható
  tükörkép kialakulásának magyarázata a fény szabályos visszaverődésével, a fénysugár útjának
  megrajzolásával” · „az árnyékjelenségeket, mint a fény egyenes vonalú terjedésének
  következményeit”.
- **Tévhitek:** a kép a tükör felületén van. Ha hátrébb lépsz, többet látsz magadból. Látáskor
  a szemből indul ki valami (látósugár). A tárgyat akkor is látjuk, ha a róla jövő fény nem
  jut a szemünkbe.
- **Kulcsvizuál:** felülnézetű szoba egy tárggyal, egy tükörrel és egy szemmel. A sugarak a
  tükörről a szembe pattannak; a meghosszabbításuk szaggatott vonallal a tükör mögött, egy
  pontban találkozik.
- **Interaktív:** a szem, a tárgy és a fényforrás húzható. Egy, két vagy kiterjedt fényforrás
  választható (árnyék és félárnyék). Az egész alakos tükörnél a diák a tükör méretét és a saját
  távolságát változtatja.
- **Lépések:** Egyenesen halad · Árnyék · Félárnyék · Hogyan látunk? · A visszaverődés
  törvénye · Hol a tükörkép? · Mekkora tükör kell? · Camera obscura.
- **Adatok:** a beesési és a visszaverődési szöget a beesési merőlegestől mérjük. Fénysebesség
  ≈ 300 000 km/s. Az egész alakos tükörnek a testmagasság felének kell lennie, a távolságtól
  függetlenül.
- **Építőkocka:** F (sugároptika: sugár, visszaverődés, árnyékkúp).

### 11 · `11-lencse-szem` – Miért kell szemüveg? – lencsék és a látás

- **Tanulási cél:** A gyűjtőlencse a párhuzamos sugarakat a fókuszpontba gyűjti, és képet alkot.
  A szem a recehártyára vetít. Rövidlátásnál a kép a recehártya *elé* esik, ezt szórólencse
  javítja; távollátásnál *mögé*, ezt gyűjtőlencse javítja.
- **Kerettanterv:** „ismeri a látás folyamatát, a szem hibáit és a szemüveg szerepét ezek
  kijavításában” · „A gyűjtőlencse optikai tulajdonságainak kísérleti vizsgálata. A nagyító
  képalkotásának fizikai magyarázata” · „Jellegzetes lencsehibák: rövidlátás, távollátás, ezek
  korrekciója szemüveggel, kontaktlencsével, lézeres beavatkozással”.
- **Tévhitek:** ha a lencse felét letakarjuk, a kép fele eltűnik (valójában az egész kép
  halványabb lesz). A kép csak akkor létezik, ha ernyő van ott. A rövidlátó közelre lát rosszul.
- **Kulcsvizuál:** nagy szemmetszet. Egy tárgy (betű) pontjaiból induló sugárkúpok a
  recehártyán találkoznak; ha nem ott találkoznak, elmosódott foltot adnak. A felhelyezett
  szemüveg „visszahúzza” a találkozási pontot a recehártyára.
- **Interaktív:** a tárgy távolsága húzható; a szemgolyó hossza csúszkával állítható (rövidlátó
  vagy távollátó); a szemüveg dioptriája is csúszkás (−4 … +4 D); egy gombbal letakarható a
  lencse fele.
- **Lépések:** Fénytörés: a megtört szívószál · Gyűjtőlencse, fókusz · Kép az ernyőn ·
  Nagyító · A szem mint kamera · Alkalmazkodás · Rövidlátás és szórólencse · Távollátás és
  gyűjtőlencse.
- **Adatok:** törésmutató: víz 1,33, üveg ≈ 1,5, szaruhártya ≈ 1,38. A szem törőereje ≈ 60 D
  (ebből a szaruhártya ≈ 43 D), a szemgolyó hossza ≈ 24 mm. Dioptria = 1/f (m). Tiszta látás
  távolsága 25 cm, nagyító nagyítása ≈ 25 cm / f. Lencsetörvény: 1/f = 1/t + 1/k. Kb. 1 mm-rel
  hosszabb szemgolyó ≈ −2,5…−3 D rövidlátás.
- **Építőkocka:** F (törés, vékony lencse).
- **Meglévő anyag:** PhET *Geometric Optics*, *Bending Light*.

### 12 · `12-hullam-hang` – Mitől magas a hang? – hullámok és hang

- **Tanulási cél:** A hullámban a minta és az energia halad, nem az anyag. A hullámot a
  frekvencia, az amplitúdó, a hullámhossz és a terjedési sebesség jellemzi (v = λ·f). A hang a
  levegő sűrűsödése és ritkulása: a hangmagasság a frekvenciától, a hangerő az amplitúdótól
  függ.
- **Kerettanterv:** „érti a hullámmozgás lényegét és a jellemző legfontosabb mennyiségeket:
  frekvencia, amplitúdó, hullámhossz, terjedési sebesség” · „A hang tulajdonságainak
  (hangmagasság, hangerő) fizikai magyarázata” · „Rugalmas kötélen, rugón kialakított
  állóhullámok megfigyelése” · „a hallást károsító tényezők ismerete”.
- **Tévhitek:** a hanggal a levegő a hangszórótól a fülig utazik. A hang légüres térben is
  terjed, és levegőben gyorsabb, mint szilárd anyagban. A hangosabb hang gyorsabban terjed.
- **Kulcsvizuál:** gyöngysor-kötél, amelyen egy kiemelt gyöngy csak fel-le mozog, miközben a
  hullám elhalad. Ugyanez levegőrészecskékkel: sűrűsödések vándorolnak, a részecskék helyben
  ide-oda mozognak.
- **Interaktív:** a frekvencia és az amplitúdó csúszkával állítható, és a hang meg is szólal
  (WebAudio, korlátozott hangerővel). A gitárhúron a lefogás helye húzható, az állóhullám
  módusai választhatók.
- **Lépések:** A minta halad, nem a kötél · Amplitúdó, frekvencia, hullámhossz · v = λ·f · A
  hang a levegőben · Hangmagasság és hangerő · A húr állóhulláma · Fül és decibel.
- **Adatok:** hangsebesség: levegőben 343 m/s (20 °C), vízben ≈ 1480 m/s, acélban ≈ 5900 m/s.
  Hallható tartomány 20 Hz – 20 kHz. Az A4 hang 440 Hz, λ ≈ 0,78 m. Húr: f = v/(2L); a 12.
  bundnál a hang egy oktávval magasabb. Hangerő: beszélgetés ≈ 60 dB, forgalom ≈ 80 dB,
  koncert ≈ 110 dB, fájdalomküszöb ≈ 120–130 dB; 85 dB felett már 8 óra is kárt okoz. 3 s
  késés a villám és a mennydörgés között ≈ 1 km távolság.
- **Építőkocka:** G (1D hullámmotor + hang), D (levegőrészecskék).
- **Meglévő anyag:** PhET *Wave on a String*, *Waves Intro*.

### 13 · `13-szinek` – Miért kék az ég? – a fény és a színek

- **Tanulási cél:** A fehér fény színek keveréke. A tárgy színe attól függ, milyen fényt ver
  vissza a megvilágító fényből. A fények összeadódnak (RGB), a festékek elnyelnek. Az ég azért
  kék, mert a levegő a rövid hullámhosszú fényt jobban szórja.
- **Kerettanterv:** „érti a színek kialakulásának elemi fizikai hátterét” · „Kísérleti
  vizsgálata és magyarázata annak, miért függ a tárgyak színe a megvilágító fény színétől” · „A
  színek észlelésének magyarázata, a kiegészítő színek” · „A felhők, az ég, a növényzet, a
  tenger, a folyók színének egyszerű magyarázata”.
- **Tévhitek:** a szín a tárgy saját tulajdonsága, a piros alma sötétben is piros. A prizma
  „megfesti” a fényt. Minden színes fény együtt barna vagy fekete lesz (a festékkeverésből
  általánosítva). Az ég azért kék, mert a tenger tükröződik benne.
- **Kulcsvizuál:** sötétített „színpadi” doboz a világos lapon, benne egy piros alma, egy zöld
  levél és egy fehér papír három színes reflektor fényében. Minden tárgy mellett egy kis
  spektrumsáv mutatja, mi jön be és mi verődik vissza.
- **Interaktív:** három reflektor-szabályzó (R, G, B), egymást átfedő fényfoltokkal; színszűrők;
  a napnál a Nap magassága csúszkával állítható (kék ég, vörös naplemente).
- **Lépések:** Prizma: felbomlik a fehér · Színek és hullámhosszak · Szivárvány · A tárgy színe
  visszavert fény · Más fényben más szín · Fénykeverés és kiegészítő színek · Festékkeverés ·
  Ég, felhő, tenger, levél.
- **Adatok:** látható tartomány ≈ 380–750 nm (ibolya ≈ 400, kék ≈ 450–495, zöld ≈ 495–570, sárga
  ≈ 570–590, narancs ≈ 590–620, vörös ≈ 620–750 nm). Szórás ∝ 1/λ⁴, ezért a kék (450 nm) ≈ 6×
  jobban szóródik, mint a vörös (700 nm). Szivárvány ≈ 42° (vörös) és ≈ 40° (ibolya). Kiegészítő
  párok: vörös–cián, zöld–bíbor, kék–sárga. A klorofill a vöröset és a kéket nyeli el.
- **Építőkocka:** F (prizma, n(λ)), színkeverő/spektrum widget.
- **Meglévő anyag:** PhET *Color Vision*.

### 14 · `14-uveghaz` – Miért melegszik a Föld? – az üvegházhatás

- **Tanulási cél:** A Föld hőmérsékletét a bejövő napfény és a kimenő infravörös sugárzás
  egyensúlya szabja meg. Az üvegházgázok elnyelik és részben visszasugározzák az infravörös
  sugárzást, ezért több CO₂ mellett az egyensúly magasabb hőmérsékleten áll be. A tengerszint a
  víz hőtágulása és a *szárazföldi* jég olvadása miatt emelkedik.
- **Kerettanterv:** „ismeri az éghajlatváltozás problémájának összetevőit, lehetséges okait” ·
  „A tüzelőanyagok elégetésének szerepe az üvegházhatás kialakulásában” · „A tengerszint
  emelkedésének fizikai okai” · (1.) „A Föld éghajlatának globális változásával kapcsolatos
  hőmérsékleti adatsorok elemzése”.
- **Tévhitek:** az üvegházhatás azonos az ózonlyukkal (jól dokumentált keveredés). A gázok
  „visszatükrözik” a napfényt. Az üvegházhatás csak káros. Az úszó tengeri jég olvadása emeli a
  tengerszintet (ez kapcsolódik a 01-hez). Egy hideg tél cáfolja a melegedést.
- **Kulcsvizuál:** a légkör metszete. Sárga napfény-fotonok érkeznek; a felszín vörös
  infravörös fotonokat bocsát ki; a CO₂-molekulák elnyelik őket, és véletlen irányba
  kisugározzák. Mellette egy „be / ki” energiamérleg és egy hőmérő.
- **Interaktív:** a CO₂ csúszkával állítható (280 → 420 → 560 ppm). Az albedó (jég vagy sötét
  felszín) is állítható. A „Légkör nélkül” gomb megmutatja a −18 °C-ot.
- **Lépések:** Napfény be · A Föld infravöröset sugároz · Légkör nélkül −18 °C · Üvegházgázok ·
  Több CO₂: új egyensúly · Világos és sötét felszín · Mit mutatnak a mérések? · A tengerszint
  emelkedése.
- **Adatok:** napállandó 1361 W/m², albedó ≈ 0,30. Légkör nélkül ≈ −18 °C (255 K), a valódi
  átlag ≈ +15 °C. CO₂: iparosodás előtt 280 ppm, ma ≈ 425 ppm, évente kb. 2,5 ppm-mel nő
  *(frissítendő)*. Egyensúlyi melegedés ≈ 3 °C CO₂-duplázásonként (IPCC AR6). Eddig ≈ +1,2–1,3 °C
  (1850–1900-hoz képest). Tengerszint-emelkedés 1900 óta ≈ 20 cm. A modell didaktikus: egyrétegű
  légkör, nem előrejelzés.
- **Építőkocka:** D (fotonok és molekulák), B (adatsor-grafikon).
- **Meglévő anyag:** PhET *Greenhouse Effect*.

### 15 · `15-fold-forgasa` – Miért van nappal és éjszaka? – a Föld forgása és keringése

- **Tanulási cél:** A nappalok és éjszakák váltakozását a Föld forgása okozza. A Nap
  látszólagos útja és egy bot árnyéka megadja az égtájakat. A csillagok a Sarkcsillag körül
  látszanak körbefordulni. A nap a Föld forgásához, az év a keringéséhez kötődik; az évszakokat
  a tengely ferdesége okozza.
- **Kerettanterv:** „érti a nappalok és éjszakák változásának fizikai okát” · „A Nap járásának
  megfigyelése egy bot árnyékának segítségével, az égtájak meghatározása” · „ismeri a
  csillagképek, a Sarkcsillag, valamint a Nap égi helyzetének szerepét a tájékozódásban” ·
  „csillagászati időegységeket (nap, hónap, év) és azok kapcsolatát a Föld és Hold forgásával és
  keringésével”.
- **Tévhitek:** a nappal és az éjszaka a Nap körüli keringés miatt váltakozik. Az évszakokat a
  Naptól mért távolság okozza. Délben a Nap mindenütt pontosan fölöttünk áll. A Sarkcsillag a
  legfényesebb csillag.
- **Kulcsvizuál:** osztott kép. Bal oldalt a forgó földgömb egy budapesti tűvel és a
  nappal–éjszaka határral. Jobb oldalt ugyanez a pillanat a budapesti horizontról: a Nap íve az
  égen és a bot árnyéka a földön, szinkronban. Az éjszakai ég egy sötét „ablakban” jelenik meg a
  világos lapon.
- **Interaktív:** csúszka a napszakra és a dátumra (változik a Nap ívének magassága és a nappal
  hossza). Választható helyszín: Budapest, az Egyenlítő vagy az Északi-sark. Egy kapcsolóval
  bekapcsolhatók a csillagok, és látszanak a Sarkcsillag körüli ívek.
- **Lépések:** Forgó Föld · A Nap látszólagos útja · A bot árnyéka · Égtájak · Éjjel: a
  Sarkcsillag · Keringés: más évszak, más csillagképek · Évszakok: a ferde tengely · Nap,
  hónap, év.
- **Adatok:** tengelyferdeség 23,44°. Budapest: 47,5° É, 19,0° K; a Sarkcsillag magassága
  ≈ 47,5°. Delelési napmagasság: június 21-én 65,9°, napéjegyenlőségkor 42,5°, december 21-én
  19,1°. A nappal hossza ≈ 16 h 0 min, illetve ≈ 8 h 26 min. Csillagnap 23 h 56 min, év 365,24
  nap. Napközelpont ≈ 147,1 millió km (január eleje), naptávolpont ≈ 152,1 millió km (július
  eleje).
- **Építőkocka:** H (égbolt/pálya-szimulátor: gömb, terminátor, helyi horizont).
- **Meglévő anyag:** Stellarium (ingyenes planetáriumprogram).

### 16 · `16-holdfazisok` – Miért változik a Hold alakja? – holdfázisok és fogyatkozások

- **Tanulási cél:** A Holdnak mindig az egyik fele van megvilágítva. Az, hogy ebből mennyit
  látunk, a Nap, a Föld és a Hold szögétől függ, és 29,5 naponként ismétlődik. Fogyatkozás csak
  akkor van, ha a három égitest egy vonalba kerül; a Hold pályájának ferdesége miatt ez nem
  minden hónapban történik meg.
- **Kerettanterv:** „megfigyelésekkel feltárja a holdfázisok változásának fizikai hátterét” ·
  „A Hold fázisainak megfigyelése, fizikai magyarázata a Nap, Föld, Hold helyzete alapján” · (7.)
  „A Hold árnyéka a Földön: a napfogyatkozás, a Föld árnyéka a Holdon: holdfogyatkozás”.
- **Tévhitek:** a holdfázisokat a Föld árnyéka okozza (a leggyakoribb, jól dokumentált tévhit).
  A Hold nem forog. A Hold csak éjjel látszik. Minden hónapban van fogyatkozás.
- **Kulcsvizuál:** felülnézetű pálya, a napfény balról érkezik, a Hold mindig félig világos.
  Szinkronban mellette egy kis kép: „ezt látod a Földről”. A Föld árnyékkúpja külön is
  bekapcsolható, és csak teliholdkor ér a Holdhoz.
- **Interaktív:** a Hold a pályán húzható, vagy egy napcsúszkával léptethető (0–29,5 nap). Egy
  kapcsoló megmutatja a Föld árnyékát. Oldalnézetben állítható a pálya 5°-os hajlása.
- **Lépések:** A Hold nem világít · Mindig félig megvilágított · Amit a Földről látunk · A
  fázisok sorban · Mikor kel a telihold? · Napfogyatkozás · Holdfogyatkozás: vörös Hold · Miért
  nem minden hónapban?
- **Adatok:** szinodikus hónap 29,53 nap, sziderikus hónap 27,32 nap. Föld–Hold távolság
  384 400 km. Átmérők: Hold 3474 km, Föld 12 742 km, Nap 1 392 000 km. A Nap ≈ 400× nagyobb és
  ≈ 390× messzebb van, ezért mindkettő ≈ 0,5°-nak látszik. A Hold pályájának hajlása 5,1°. A
  Hold forgási ideje megegyezik a keringési idejével, ezért mindig ugyanazt az oldalát látjuk.
- **Építőkocka:** H (a 15-ből), F (árnyékkúp a 10-ből).

---

## 4. Építőkockák és gyártási sorrend

### Modulok

| Modul | Mit tud | Lecke | Első megépítés |
|---|---|---|---|
| **A · Tartály + úszás** | folyadékszint, bemerülés, kiszorított térfogat, mérleg | 01, 07 (14) | 01 |
| **B · Grafikonrajzoló** | élő x–t / T–t / m–V görbe, görgetés, tengelyfeliratok magyar tizedesvesszővel | 01, 03, 05, 06, 14 | 01 |
| **C · 1D mechanika** | integrátor, pálya, ütközés, vektornyilak, energiaoszlopok | 02, 03, 04, 05 | 05 (az alap), 02 (energiaoszlopok) |
| **D · Részecskeszimuláció** | 2D golyók, kötések és hőmérséklet, kiáramlás, fotonok | 06, 14, 12, 04 | 06 |
| **E · Áramkör-szimulátor** | ideális elemek, soros/párhuzamos, áramló töltések, műszerek | 08, 09 | 08 |
| **F · Sugároptika** | sugár, visszaverődés, törés (n(λ)-val), vékony lencse, árnyékkúp | 10, 11, 13, 16 | 10 |
| **G · Hullámmotor + hang** | 1D lánc / analitikus hullám, állóhullám, WebAudio | 12 | 12 |
| **H · Égbolt/pálya** | földgömb terminátorral, helyi horizont, Nap/Hold/csillagok helyzete dátumból | 15, 16 | 15 |
| **Közös UI** | húzható fogantyú, mérőműszerek (stopper, hőmérő, ampermérő, számláló), váltógombok | mind | 01 + menet közben |

Egy modul először egy lecke részeként készül el. A sorozat végére a modulok egy közös
könyvtárba kerülnek: egy kötegen belül legfeljebb egy lecke vezessen be egy adott új modult,
hogy a párhuzamos ügynökök ne írják ugyanazt kétszer.

**A modulok építési sorrendje:** A, B (a 01-gyel már készülnek) → C, F → E → H, D, G.

### Gyártási sorrend (legfeljebb 3 párhuzamos lecke kötegenként)

| Köteg | Leckék | Új modul | Újrahasznosított |
|---|---|---|---|
| 1 | **01** (már folyamatban) | motor, tartalomformátum, A, B | – |
| 2 | **05-inga** (1), **07-felhajtoero** (2), **10-arnyek-tukor** (2) | C-alap (05), F (10) | A, B |
| 3 | **02-energia** (2), **11-lencse-szem** (3), **08-aramkor** (3) | energiaoszlopok (02), E (08) | C, F |
| 4 | **03-mozgas-fekezes** (2), **09-aram-otthon** (2), **15-fold-forgasa** (3) | H (15) | C, B, E |
| 5 | **06-halmazallapot** (3), **12-hullam-hang** (2), **16-holdfazisok** (2) | D (06), G (12) | B, F, H |
| 6 | **04-lendulet-raketa** (2), **13-szinek** (2), **14-uveghaz** (2) | színkeverő widget (13) | C, D, F, B |

A 2. köteg szándékosan könnyű: itt derül ki, hogy a motor és a tartalomformátum bírja-e a
párhuzamos gyártást. Minden köteg után érdemes a frissen elkészült modult kiemelni a közös
könyvtárba, mielőtt a következő köteg ráépül.

---

## 5. Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / fejlesztési feladat |
|---|---|---|
| 1. Bevezetés a fizikába (8) | 01, (05: ismételt mérés, átlag), (14: hőmérsékleti adatsor) | a mértékegységek és az átváltás önállóan; becslés; a tudományos érvelés kritikája; a fizika szakterületei és új eredményei; a mobilszenzoros mérés (tanórai tevékenység) |
| 2. Az energia (8) | 02, 09 (teljesítmény, kWh, ár) | a fosszilis és zöldenergia, az energiabiztonság, a jövő energiaforrásai csak érintőlegesen (a 02 erőművi lépése); a táplálék energiatartalma és a testsúly; a termosztát és a hőszigetelés; a gáz kontra áram fűtési költsége |
| 3. Mozgás (10) | 03, (02: a szabadesés tömegfüggetlensége) | a nehézségi gyorsulás és Newton II. csak kvalitatívan; az egyenletes mozgás számolási gyakorlása; Newton és Galilei élete |
| 4. Lendület és egyensúly (10) | 04, 05 | **a nyugvó testek egyensúlya és az egyszerű gépek (emelő)**; a rugalmas és rugalmatlan alakváltozás; a szilárd anyagok belső szerkezete csak a 06 részecskerácsában |
| 5. Víz és levegő (14) | 06, 07, (01: úszás, fagy) | **a levegő tulajdonságai, a páratartalom és az időjárási jelenségek** (szél, eső, harmat, dér, hó, felhők); a kapilláris jelenségek; a hőtágulás és a hővezetés; a légnyomás és a „pattogó fül” |
| 6. Elektromosság (14) | 08, 09 | **a Föld mágneses tere, az állandó mágnes és az iránytű** (ez külön tanulási eredmény!); a villám; az egyen- és váltakozó áram; az elemek és akkumulátorok; Jedlik, a motor és a transzformátor |
| 7. Fény, optika (12) | 10, 11, (13: fehér fény), (16: fogyatkozás) | a fényforrások tulajdonságai csak a 09 izzó–LED lépésében; a távcső és a mikroszkóp; az optikai illúziók |
| 8. Hullámok (10) | 12, 13 | a vízhullámok, a lökéshullám és a cunami; a fúvós és ütős hangszerek (csak húr van); a hallás mechanizmusa csak röviden |
| 9. Globális problémák (6) | 14 | **az ózonpajzs elvékonyodása** (ez is tanulási eredmény; a 14-ben csak tévhitként szerepel); a fény- és zajszennyezés (a zaj részben a 12-ben); az ökológiai lábnyom; a porszűrők |
| 10. Égi jelenségek (10) | 15, 16 | **a Nap fizikai jellemzői és energiaforrása**; a bolygók jellemzői; a csillagok, galaxisok, fekete lyukak és a fényév; az űrkutatás; Kopernikusz, Kepler, Galilei |

**Tartalék-jelöltek**, ha a pilot után folytatódik a sor (a vastagon szedett hiányok miatt,
fontossági sorrendben):

1. `idojaras` – felhő, eső, dér, szél (D + A);
2. `magnes-iranytu` – a Föld mint dipól;
3. `egyensuly-emelo` – Arkhimédész emelője (C);
4. `naprendszer-meretek` – a távolságok léptéke és a fényév (H);
5. `nap-energiaja` – fúzió, a Nap mint energiaforrás;
6. `ozonpajzs` – az UV elnyelése (D).
