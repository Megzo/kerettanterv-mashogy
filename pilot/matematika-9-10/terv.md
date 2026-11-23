# Pilot: Matematika 9–10. – a leckesor terve

Forrás: [`kerettanterv/matematika/9-10.md`](../../kerettanterv/matematika/9-10.md) (NAT 2020,
4 évfolyamos gimnázium, 17 témakör, 204 óra). Az idézetek szó szerint onnan valók (a forrás
dőlt betűit és felső indexeit itt egyszerű szövegként írjuk: *a*<sup>2</sup> → a²). A
lecke-formátum: [`leckek/SZERZODES.md`](../../leckek/SZERZODES.md).

> **Kapcsolat a Matematika 5–6. sorozattal.** A közös matematikai eszközkészletet
> (koordináta-rendszer, számegyenes, alapgeometria, átdarabolás, halmazábra, diagram,
> véletlen kísérlet) a párhuzamosan készülő `pilot/matematika-5-6/` sorozat építi meg. A terv
> írásakor annak terve még nem létezett, ezért az 5. fejezet azt rögzíti, **mit várunk** a
> közös készlettől, és mit épít hozzá a 9–10. Ha a Matek 5–6 terve vagy kódja más nevet vagy
> API-t használ, **az az irányadó**; ez a terv csak a minimális elvárást írja le.

## 1. Bevezető

A pilot **15 leckéje** a 9–10. osztályos gimnáziumi matematika mind a 17 témakörét érinti. A
formátum ugyanaz, mint a fizikánál és a történelemnél: 7–9 lépés, 1920×1080-as színpad, bal
oldalt animáció, jobb oldalt magyarázó panel, világos, papírszerű háttér. Az esztétika az
`iskola` *matek-kor-pi* leckéjének „rajzlapja”: rács, tintavonalak, pontos geometriai
morfolás, csúszkák.

**A kulcskérdés:** hol ad egy interaktív animáció *valódi* belátást a középiskolai matekban
egy táblai rajzhoz, a tankönyvhöz vagy egy GeoGebra-fájlhoz képest? Szerintünk hat helyzetben:

1. **A paraméter szerepe, csúszkával.** Az f(x + 3) *balra* tolja a parabolát, a
   diszkrimináns előjele dönti el, hány metszéspont van. Ezt a táblán egyetlen pillanatkép
   mutatja, csúszkával viszont a diák *látja*, ahogy a görbe a paraméterrel együtt mozog, és
   maga mondja ki a szabályt (07, 08).
2. **Geometriai bizonyítás átdarabolással.** A Pitagorasz-tétel, az (a + b)², a teljes
   négyzetté kiegészítés és a √2 irracionalitása mind „darabokból” bizonyítható. Az animáció
   a darabokat merev mozgással, követhetően teszi át, és a terület közben láthatóan nem
   változik (01, 05, 08, 09).
3. **Egyenlet ↔ grafikon.** Az egyenlet megoldása két grafikon metszéspontja, az
   egyenlőtlenségé egy tengelyszakasz. Ha a szöveges feladat adata változik, a metszéspont
   elmozdul, és néha „értelmetlen” helyre kerül (fél nyúl) – ebből lesz az ellenőrzés és az
   észszerűségi vizsgálat (06, 08).
4. **Húzható szerkesztés, sejtés → bizonyítás.** A háromszög csúcsait húzva a körülírt kör
   középpontja kilép a háromszögből, derékszögnél pont az átfogóra esik. A Thalész-kör
   szöge mindig 90°. A dinamikus ábra **sejtést** ad, utána a panel **bizonyít**. A két
   szerepet minden leckében megkülönböztetjük (4. fejezet, 1. pont).
5. **Transzformációk mozgásban.** Két tükrözés egymásutánja eltolás vagy forgatás, a
   nagyítás kétszeres oldalhoz négyszeres területet ad. Ez állóképen csak két alakzat,
   animálva viszont *út*, amelyet a diák követni tud (12, 13).
6. **Sok kísérlet → valószínűség.** Tízezer pénzfeldobás, ezer golyó a Galton-deszkán: a
   relatív gyakoriság szemünk előtt áll be. Ezt a tanórán kézzel nem lehet elvégezni (15).

**Mit hagyunk ki?** A rutinszámolást (egyenletrendezés, törtes kifejezések, százalékszámítási
gyakorlás), a definíciók felsorolását és a táblázatkitöltést: ezekhez feladatlap kell, nem
animáció. Szintén kimarad, ami tanórai tevékenység (adatgyűjtés, projektmunka, logikai
játékok, kiselőadás). A leckék ezekhez legfeljebb kiindulópontot adnak.

**Kiválasztási elv.**

1. **Arányosság:** nagyjából óraszám szerint, kb. 13–14 óránként egy lecke. A
   transzformációk (20 óra) és a háromszögek (16 óra) két-két leckét kapnak, a függvények
   (16 óra) egy saját leckét és a másodfokú lecke felét. A rövid, rokon témakörök össze vannak
   vonva: halmazok és logika (02), számhalmazok és négyzetgyök (01), négyszögek-sokszögek és
   parkettázás (12).
2. **Ahol a tanterv maga is szemléltetést kér:** „A nevezetes azonosságok geometriai
   megjelenítése”, „A derékszögű háromszög oldalaira szerkesztett négyzetek átdarabolása”, „A
   Thalész-tétel felfedeztetése szerkesztéssel, szögméréssel vagy dinamikus geometriai
   szoftver alkalmazásával”, „A „végtelen szálloda” mint modell”, „Konkrét valószínűségi
   kísérletek végrehajtása vagy dinamikus szoftver segítségével történő szimulálása” – ezek
   biztosan bekerülnek.
3. **Építőkockák újrahasznosítása:** a leckék a Matek 5–6 közös készletére és három új
   9–10-es modulra épülnek (5. fejezet). Két referencialecke építi az új modulokat: a
   **07-fuggveny-transzformacio** (függvényrajzoló + képletszedő) és a **10-nevezetes-pontok**
   (szerkesztő-motor).

**Miért 15 és nem 14?** A 17 témakörből 14 leckével vagy a százalékszámítást és a négyszögeket,
vagy a halmazokat és a logikát kellett volna teljesen kihagyni. A halmaz–logika témakörpár 20
óra (a tanév 10 %-a), és a Venn-diagram nagyon jól animálható, ezért külön leckét kapott. A
százalékszámítás és a speciális négyszögek a tartaléklista elején állnak (7. fejezet).

**Célcsoport és panel.** 15–16 évesek: a szerződés alapértéke (≤ 55 szó lépésenként)
megfelelő. A képletek a panelen **egy szónak** számítanak (6. fejezet), különben egy-két
egyenlet elvinné a keretet.

A leckék sorszáma a kerettanterv sorrendjét követi, a **gyártási sorrend** ettől eltér
(5. fejezet). A „Számpéldák” pontokban szereplő értékeket Pythonnal ellenőriztük (2026-11-23).
Az *(ellenőrizendő)* jelzés azt jelenti, hogy a történeti vagy földrajzi adatot a gyártás előtt
még forrásban kell ellenőrizni. A „Meglévő anyag” pontok saját ismereten alapulnak,
nincsenek ellenőrizve.

## 2. A leckék

| # | slug | cím | témakör | építőkocka | nehézség (1–3) |
|---|---|---|---|---|---|
| 01 | `01-gyok-ketto` | Milyen hosszú a négyzet átlója? – a √2 és az irracionális számok | 4 (+5) | Számegyenes, Darabolás | 2 |
| 02 | `02-halmazok-logika` | „Ha…, akkor…” – halmazok, logikai szita és a logika nyelve | 1, 2 | Venn | 2 |
| 03 | `03-fa-diagram` | Hányféleképpen? – fa-diagram, szorzási elv, gráfok | 3 | *MatGraf* (leckén belül) | 2 |
| 04 | `04-hatvany-normalalak` | Hányszor hajtható félbe egy papír? – hatványok és normálalak | 5 | Számegyenes (log-lépték leckén belül) | 2 |
| 05 | `05-nevezetes-azonossagok` | Miért nem a² + b²? – nevezetes azonosságok négyzetekkel | 6 | Darabolás, **MatKeplet** | 1 |
| 06 | `06-egyenletrendszer` | Hány tyúk és hány nyúl? – egyenletek, egyenlőtlenségek, egyenletrendszerek | 8 | **MatFv**, Számegyenes | 2 |
| 07 | `07-fuggveny-transzformacio` | Merre mozdul a parabola? – függvények és transzformációik | 10 (+7) | **MatFv + MatKeplet (referencia)** | 3 |
| 08 | `08-masodfoku` | Hol metszi a parabola a tengelyt? – teljes négyzet, megoldóképlet, diszkrimináns | 9 (+6, +10) | **MatFv**, Darabolás | 2 |
| 09 | `09-pitagorasz` | Miért éppen a² + b² = c²? – a Pitagorasz-tétel bizonyításai | 12 | Darabolás, **MatSzerk** | 2 |
| 10 | `10-nevezetes-pontok` | Hol legyen a mentőállomás? – a háromszög nevezetes pontjai és körei | 12, 11 | **MatSzerk (referencia)** | 3 |
| 11 | `11-kor-thalesz` | Miért mindig derékszög? – Thalész-tétel, érintő, körív | 14 | **MatSzerk** | 2 |
| 12 | `12-egybevagosag-parketta` | Hogyan fedi le a csempe a síkot? – tükrözés, forgatás, eltolás, parketta | 15, 13 | Geo-transzformációk, **MatSzerk** | 3 |
| 13 | `13-hasonlosag` | Milyen magas a torony? – nagyítás, hasonlóság, területarány | 15 (+7, +11) | **MatSzerk**, Geo-transzformációk | 2 |
| 14 | `14-statisztika` | Kinek hazudik az átlag? – középértékek és diagramtrükkök | 16 | Diagram | 2 |
| 15 | `15-valoszinuseg` | Mit tud a véletlen? – relatív gyakoriság, klasszikus modell, Galton-deszka | 17 | Véletlen, Diagram (Galton leckén belül) | 2 |

Nehézség = gyártási nehézség: 1 = egy fő vizuál, kevés interakció; 2 = egy közepes modul vagy
új interakció; 3 = új közös modul (referencialecke) vagy több szinkron nézet.

Témakörönként: 1 → 1 (02) · 2 → 1 (02) · 3 → 1 · 4 → 1 · 5 → 1 (+ 01) · 6 → 1 (+ 08) ·
7 → (07, 13) · 8 → 1 · 9 → 1 · 10 → 1 (+ 08) · 11 → (10) · 12 → 2 · 13 → (12) · 14 → 1 ·
15 → 2 · 16 → 1 · 17 → 1. A 7. témakörnek (arányosság, százalék) nincs saját leckéje:
a fordított arányosság a 07-ben, az arány és a méretarány a 13-ban szerepel, a
**százalékszámítás nincs lefedve** (tartalék 1.).

---

## 3. Briefek

Minden brief tartalmaz egy **„Sejtés → bizonyítás”** sort, ahol a lecke tételt mond ki: mi
az, amit az animáció csak *mutat* (mérés, kísérlet), és mi az, amit a panel *bizonyít*.

### 01 · `01-gyok-ketto` – Milyen hosszú a négyzet átlója? – a √2 és az irracionális számok

- **Tanulási cél:** Az egységnyi oldalú négyzet átlójának négyzete 2, a hossza tehát √2. Ezt
  a hosszt körzővel a számegyenesre lehet vinni, de **semmilyen tört nem pontosan egyenlő
  vele**: a √2 irracionális. A racionális számok tizedes alakja véges vagy szakaszos, az
  irracionálisoké nem. A valós számok kitöltik a számegyenest.
- **Kerettanterv:** „ismer példákat irracionális számokra” · „ismeri a valós számok és a
  számegyenes kapcsolatát” · „Irracionális számok szemléltetése” · „Tizedes törtek átírása
  közönséges tört alakba és viszont” · „valós számok közelítő alakjaival számol, és
  megfelelően kerekít” · (5.) „A négyzetgyök definíciója”.
- **Tévhitek:** a √2 = 1,41 (vagy 1,4142) „pontosan”, csak a számológép kerekít. Ha elég sok
  tizedesjegyet írunk, előbb-utóbb ismétlődni kezd. A számegyenesen a törtek „mindent
  kitöltenek”, mert bármely kettő között van harmadik. Az irracionális szám „nem igazi”,
  nem lehet megszerkeszteni.
- **Kulcsvizuál:** egységnégyzet a számegyenesen, átlója körzővel leforgatva: a körív az
  1,414…-nél metszi az egyenest. Utána nagyítás: minden zoomlépésnél egy újabb tizedesjegy
  jelenik meg, a pont mindig két szomszédos osztás közé esik. A bizonyítás *Tennenbaum*
  átdarabolásával: ha p² = 2q² volna (egész p, q), akkor egy p oldalú négyzetbe két q oldalú
  négyzetet tolunk az ellentétes sarkokba. Az átfedés (2q − p oldalú) területe egyenlő a két
  kimaradt sarok (p − q oldalú) területével – kisebb egész megoldás. Ez a lépés végtelenül
  ismételhető, ami lehetetlen.
- **Interaktív:** (1) tört-vadász: két csúszka (számláló p, nevező q ≤ 100), a vásznon p/q és
  a √2 távolsága, valamint a p² és a 2q² mint két négyzet: **sosem lesz egyforma**, a
  legközelebbi párok 3/2, 7/5, 17/12, 41/29, 99/70. (2) „Csökkentés” gomb: a Tennenbaum-lépést
  egy kiválasztott „majdnem-megoldáson” (99, 70) mutatja, és a pár egyre kisebb lesz,
  amíg 1 és 1 nem marad.
- **Lépések:** Négyzet átlója: hány egység? · Körzővel a számegyenesre · Tizedesjegyek:
  nagyítás · Törtek: véges vagy szakaszos · Vadásszunk törtet! · Két négyzet, amely sosem
  egyforma (bizonyítás) · A valós számok kitöltik az egyenest · Az A4-es lap titka ·
  Összefoglaló.
- **Sejtés → bizonyítás:** a tört-vadászat csak sejtést ad („még nem találtunk”), a
  Tennenbaum-átdarabolás bizonyít. A panel ki is mondja ezt a különbséget.
- **Számpéldák (ellenőrizve):** √2 = 1,41421356…; 1,414² = 1,999396; 1,415² = 2,002225;
  1,4142² = 1,99996164; 1,4143² = 2,00024449. A legjobb közelítő párok: 3² = 9 vs. 2·2² = 8;
  7² = 49 vs. 50; 17² = 289 vs. 288; 41² = 1681 vs. 1682; 99² = 9801 vs. 9800 (a különbség
  mindig ±1). A csökkentés (p, q) → (2q − p, p − q): (99, 70) → (41, 29) → (17, 12) → (7, 5) →
  (3, 2) → (1, 1). 1/7 = 0,142857 142857… (6 jegyű szakasz). Az A4-es lap 210 × 297 mm,
  297/210 = 99/70 = 1,4142857…: a szabvány a √2 egyik legjobb törtközelítése.
- **Történeti adat:** Tennenbaum bizonyítása 20. századi (az 1950-es évekből, J. H. Conway
  tette ismertté) *(ellenőrizendő)*. A görög hagyomány a felfedezést a püthagoreusokhoz köti,
  ez hagyomány, nem forrás.
- **Építőkocka:** Számegyenes (5–6), zoom és tizedes osztások; Darabolás (5–6), egy
  négyzetpár mozgatása. Új modult nem vezet be.

### 02 · `02-halmazok-logika` – „Ha…, akkor…” – halmazok, logikai szita és a logika nyelve

- **Tanulási cél:** A halmazműveletek és a logikai műveletek ugyanazt jelentik: „és” = metszet,
  „vagy” = unió, „nem” = komplementer. A „ha A, akkor B” azt jelenti, hogy A részhalmaza
  B-nek, és ebből nem következik a megfordítása. A logikai szita (bővített összeadás és
  kivonás) megadja az unió elemszámát.
- **Kerettanterv:** „látja a halmazműveletek és a logikai műveletek közötti kapcsolatokat” ·
  „alkalmazza a logikai szita elvét” · „Két-három halmaz elemszámával kapcsolatos feladatok
  megoldása logikai szita segítségével” · (2.) „ismeri és alkalmazza az „és”, a (megengedő és
  kizáró) „vagy” logikai jelentését” · (2.) „megfogalmazza adott állítás megfordítását” ·
  (2.) „helyesen használja a „minden” és „van olyan” kifejezéseket” · „Szemléletes kép
  végtelen halmazokról” · javasolt tevékenység: „A „végtelen szálloda” mint modell”.
- **Tévhitek:** az unió elemszáma a két elemszám összege. A „vagy” mindig kizáró („vagy…,
  vagy…”). Ha egy állítás igaz, a megfordítása is igaz. A „minden hattyú fehér” tagadása
  „minden hattyú fekete”. Két végtelen halmaz közül a „bővebb” több elemű (a páros számok
  „feleannyian vannak”).
- **Kulcsvizuál:** 1-től 100-ig a számok 10 × 10-es rácsban. Gombnyomásra a 2-vel, 3-mal,
  5-tel osztható számok pöttyei a megfelelő Venn-tartományba repülnek, mindegyik tartomány
  mellett élő számláló. A szita lépései (összeadás, levonás, visszaadás) oszlopként
  épülnek, ahogy a túl- és alulszámolás látszik.
- **Interaktív:** (1) logikai kapcsolók („és”, „vagy”, „kizáró vagy”, „nem”): a Venn-ábrán a
  megfelelő tartomány színeződik, mellette a kijelentés magyarul („páros és nem osztható
  3-mal”). (2) „Ha…, akkor…” lépés: a diák választ két tulajdonságot (pl. „osztható 4-gyel”,
  „páros”). Ha az egyik halmaz a másik részhalmaza, a buborék „belecsúszik” a másikba, a
  megfordításnál viszont egy ellenpélda (6) kiugrik.
- **Lépések:** Száz szám, három tulajdonság · „És” = metszet, „vagy” = unió · Kizáró vagy és
  tagadás · Hány szám osztható 2-vel, 3-mal vagy 5-tel? (szita) · „Ha…, akkor…” = részhalmaz ·
  A megfordítás és az ellenpélda · „Minden” és „van olyan” tagadása · A végtelen szálloda ·
  Összefoglaló.
- **Sejtés → bizonyítás:** a szita képlete a rácson megszámolt eredményből indul; a
  bizonyítás: minden szám, amely pontosan k halmazban van, a képletben pontosan egyszer
  számít (a három lehetséges esetet a Venn-tartományok színe mutatja).
- **Számpéldák (ellenőrizve):** 1–100 között 2-vel osztható 50, 3-mal 33, 5-tel 20; 6-tal 16,
  10-zel 10, 15-tel 6, 30-cal 3. Unió: 50 + 33 + 20 − 16 − 10 − 6 + 3 = 74, egyikkel sem
  osztható 26 szám. Ez a 26: az 1, a 7 és 97 közötti 22 prím, valamint a **49, 77, 91** –
  ezek a 7 miatt maradnak a „szitán” (kapcsolat Eratoszthenész szitájával; a 100-ig tartó
  szitához a 7 is kell, mert √100 = 10). A „Minden 4-gyel osztható szám páros” igaz; a
  megfordítás hamis (ellenpélda: 6). A végtelen szálloda: az n. vendég a 2n. szobába költözik,
  így minden páratlan szoba felszabadul; a párosítás n ↔ 2n kölcsönösen egyértelmű.
- **Történeti adat:** a végtelen szálloda David Hilbert 1924-es előadásából ered, George Gamow
  tette közismertté (1947) *(ellenőrizendő)*. Az ausztráliai fekete hattyú (Cygnus atratus)
  valódi ellenpélda.
- **Építőkocka:** Venn (5–6, halmazábra), kiegészítve: 3 halmaz, tartományonkénti
  elemszám, a pöttyök zárt képletű röppályája.
- **Meglévő anyag:** GeoGebra-feladatok a Venn-diagramhoz; nálunk a hangsúly a logikai
  műveletek és a halmazműveletek azonosságán van.

### 03 · `03-fa-diagram` – Hányféleképpen? – fa-diagram, szorzási elv, gráfok

- **Tanulási cél:** Ha egy döntés több lépésből áll, és minden lépésben ugyanannyi lehetőség
  van, a lehetőségek száma a lépésenkénti számok szorzata (fa-diagram). Ha a sorrend nem
  számít, ugyanazt a csoportot többször számoltuk, és ezzel a számmal osztani kell. A gráf
  (pontok és élek) ugyanezt a számolást láthatóvá teszi.
- **Kerettanterv:** „megold sorba rendezési és kiválasztási feladatokat” · „Esetszétválasztás
  és szorzási elv alkalmazása feladatok megoldásában” · „konkrét szituációkat szemléltet és
  egyszerű feladatokat megold gráfok segítségével” · javasolt tevékenység: „Sorba rendezési
  feladatok megoldásának szemléltetése gráffal” · „Téves megoldású kombinatorikafeladatokban
  a hiba megtalálása és a tévedés kijavítása”.
- **Tévhitek:** a lehetőségeket össze kell adni, nem szorozni. A dobogóra állás (sorrend
  számít) és a bizottságválasztás (nem számít) ugyanaz a feladat. Egy kézfogást kétszer
  számolunk („A kezet fog B-vel” és „B kezet fog A-val”). A háromjegyű számoknál az első
  jegy is lehet 0.
- **Kulcsvizuál:** a fa-diagram balról jobbra nő ki: póló → nadrág → cipő, az ágak végén a
  kész öltözékek apró ikonjai. Ugyanaz a fa a dobogónál 8 → 7 → 6 ágra nyílik, majd egy
  „összecsukás” animáció mutatja, hogy a bizottságnál minden csoport 6 ágon (3! sorrend)
  szerepel, ezek egyetlen pöttybe olvadnak össze.
- **Interaktív:** (1) a dobogós feladat létszáma és a helyek száma csúszkával állítható, a fa
  (nagy számnál összefoglalt „köteg”) és a szorzat élőben frissül. (2) Kézfogás-gráf:
  n = 2…12 ember körben, az élek egymás után rajzolódnak ki, a számláló n·(n − 1)/2-nél áll
  meg. A „Számolj kétszer” gomb élenként két nyilat mutat (ez a tipikus hiba).
- **Lépések:** Hányféleképpen öltözhetsz fel? · A fa-diagram és a szorzási elv · Sorba
  rendezés: négy könyv a polcon · Dobogó: számít a sorrend · Bizottság: nem számít a sorrend ·
  Háromjegyű számok: esetszétválasztás · Kézfogások gráfja · Hol a hiba? · Összefoglaló.
- **Számpéldák (ellenőrizve):** 3 póló · 2 nadrág · 2 cipő = 12 öltözék. 4 könyv sorrendje:
  4 · 3 · 2 · 1 = 24. Dobogó 8 versenyzőből: 8 · 7 · 6 = 336; 3 tagú bizottság 8 főből:
  336 / 6 = 56. Különböző jegyű háromjegyű számok: 9 · 9 · 8 = 648. Kézfogás 6 ember között:
  6 · 5 / 2 = 15. 12 csapatos bajnokság oda-visszavágóval: 12 · 11 = 132 mérkőzés. Ötöslottó
  (5 szám 90-ből): 43 949 268 különböző szelvény (a 15-ös leckében visszatér).
- **Építőkocka:** *MatGraf* (leckén belül, blokkban): fa- és körgráf-elrendezés, élek
  növekvő kirajzolása, köteg-összevonás. A 15-ös Galton-deszka útjai újrahasznosíthatják.
  A faktoriális jelölés (n!) a 11–12. évfolyam fogalma: csak egy mellékmondatban, a panelen
  szorzatként írjuk.

### 04 · `04-hatvany-normalalak` – Hányszor hajtható félbe egy papír? – hatványok és normálalak

- **Tanulási cél:** A hatvány ismételt szorzás, ezért a kitevők összeadódnak, ha azonos alapú
  hatványokat szorzunk. A 2⁰ = 1 és a 2⁻³ = 1/8 nem önkényes: a felezés mintázata
  „visszafelé” folytatva ide vezet. A normálalak (a · 10ⁿ, 1 ≤ a < 10) a nagyon nagy és a
  nagyon kicsi számok összehasonlítására szolgál.
- **Kerettanterv:** „ismeri és alkalmazza az egész kitevőjű hatvány fogalmát és a
  hatványozás azonosságait” · „ismeri és alkalmazza a normálalak fogalmát” · „Hatványozás 0
  és negatív egész kitevőre” · „A hatványozás azonosságainak megfigyelése, felfedezése” ·
  „Számolás normálalak segítségével” · javasolt tevékenység: „Projektmunka: hányszor lehet
  félbehajtani egy nagyméretű papírt? […]” · „Internetes forrásból származó, nagyon kicsi
  vagy nagyon nagy számokat tartalmazó cikkek valóságtartalmának megállapítása […]”.
- **Tévhitek:** a 2⁻³ negatív szám. A 3⁰ = 0. A 2³ · 2⁴ = 2¹² (a kitevőket összeszorozzák).
  A hajtogatás „lineárisan” vastagít (50 hajtás = 50 lapnyi). A 10⁻⁶ „majdnem nulla, tehát
  mindegy”.
- **Kulcsvizuál:** oldalnézetben egy papírköteg, minden hajtásnál duplázódik; a kamera
  logaritmikusan kifelé zoomol: asztal, ház, Mount Everest, a Hold pályája. A második felében
  egy logaritmikus „lépték-szalag” az atomtól a Tejútig: minden osztás tízszeres, a
  tárgyak (atom, vörösvértest, hajszál, ember, Föld, Föld–Nap, fényév, Tejút) a helyükre
  csúsznak, mellettük a normálalak.
- **Interaktív:** (1) hajtáscsúszka (0–50): a vastagság élőben, mértékegységváltással
  (mm → m → km). (2) a lépték-szalagon a diák behúz egy tárgyat a becsült helyére, és a
  szalag megmutatja, hány nagyságrendet tévedett. (3) „Kitevő-kockák”: 2³ · 2⁴ három és négy
  kocka egy sorban → hét kocka.
- **Lépések:** Hajtsuk félbe! · Duplázás = kettő hatványai · Kitevők összeadódnak · Visszafelé:
  2⁰ és a negatív kitevő · Hányadik hajtás ér el a Holdig? · Normálalak: a · 10ⁿ · Az atomtól
  a galaxisig · Mekkora hiba egy nagyságrend? · Összefoglaló.
- **Számpéldák (ellenőrizve):** 0,1 mm-es papír (kb. 80 g/m²-es irodai lap). 10 hajtás:
  2¹⁰ = 1024 réteg ≈ 10,2 cm; 42 hajtás: 0,1 mm · 2⁴² ≈ 439 805 km > Föld–Hold 384 400 km
  (log₂-vel számolva 41,8 hajtás kell). 103 hajtás ≈ 1,07 · 10¹¹ fényév, ez több a
  megfigyelhető Világegyetem átmérőjénél (≈ 9,3 · 10¹⁰ fényév). A valóságban kézzel kb.
  7–8 hajtás megy; a rekord 12 hajtás (Britney Gallivan, 2002, egy 1,2 km-es papírcsíkkal)
  *(ellenőrizendő)*. Lépték: hidrogénatom ≈ 1 · 10⁻¹⁰ m; vörösvértest ≈ 7,5 · 10⁻⁶ m;
  hajszál ≈ 7 · 10⁻⁵ m; ember ≈ 1,7 · 10⁰ m; Föld átmérője 1,2742 · 10⁷ m; Föld–Nap
  1,496 · 10¹¹ m; fényév 9,461 · 10¹⁵ m; a Tejút átmérője kb. 1 · 10²¹ m (kb. 100 ezer
  fényév; a becslések eltérnek, „kb.”-val).
- **Építőkocka:** Számegyenes (5–6) logaritmikus változata leckén belül (*log-lépték*:
  10ⁿ osztások, „egy osztás = tízszeres” felirat). Ha a 13-as vagy a 15-ös leckének is
  kell, a 04-ből emelhető át.
- **Meglévő anyag:** *Powers of Ten* (Eames, 1977) és a *Scale of the Universe* weboldal
  (mindkettő jogvédett, csak hivatkozás). Nálunk a hangsúly a kitevő-azonosságokon és a
  negatív kitevőn van.

### 05 · `05-nevezetes-azonossagok` – Miért nem a² + b²? – nevezetes azonosságok négyzetekkel

- **Tanulási cél:** Az (a + b)² egy a + b oldalú négyzet területe, amely négy darabra esik:
  a², b² és két a·b téglalap. Az a² − b² átdarabolással (a + b)·(a − b) téglalappá alakítható.
  Az azonosságok minden számra igazak, ezért fejszámolásra és bizonyításra is használhatók.
- **Kerettanterv:** „átalakít algebrai kifejezéseket összevonás, szorzattá alakítás,
  nevezetes azonosságok alkalmazásával” · „Az (a + b)², az (a – b)² és az (a + b)(a – b)
  kifejezésekre vonatkozó nevezetes azonosságok ismerete és alkalmazása (például oszthatósági
  feladatokban, egyenletek megoldásában, függvények ábrázolásában)” · javasolt tevékenység:
  „A nevezetes azonosságok geometriai megjelenítése” · „„Gondolj egy számra, és én kitalálom”
  játék, matematikai bűvésztrükkök algebrai magyarázata” · „Számolási „trükkök” a nevezetes
  azonosságok segítségével, például kétjegyű számok négyzetének, 99 · 101 típusú szorzat
  eredményének kiszámolása fejben”.
- **Tévhitek:** (a + b)² = a² + b² (a leggyakoribb algebrai hiba). (a − b)² = a² − b².
  Az azonosság „csak pozitív számokra” vagy „csak ha a > b” igaz. A betűs kifejezés csak
  „kitalált” szám, nem mondhat semmit minden számról.
- **Kulcsvizuál:** algebra-csempék: a a² négyzet kék, a b² narancs, az a·b téglalapok
  kékeszöld. Az (a + b)² négyzet szétnyílik négy darabra. Az a² − b²-nél a kivágott sarok
  után maradó L alak egy csíkja átfordul, és téglalap lesz belőle.
- **Interaktív:** a és b csúszkával (pl. 1–10, egész és tizedes), a csempék és a mellettük
  lévő számok (a², 2ab, b², összeg) élőben. Ha b > a, az (a − b)² ábra tükröződik, és a
  képlet ugyanaz marad. „Bűvésztrükk” gomb: a diák gondol egy számot, a csempék lépésenként
  mutatják, miért mindig 1 a végeredmény.
- **Lépések:** Mekkora a (3 + 5)²? (a hiba kimondva) · Négy darab: a², 2ab, b² · (a − b)²:
  levágunk · a² − b²: átdarabolás téglalappá · Fejszámolás: 47² és 99 · 101 · Gondolj egy
  számra! · Oszthatóság: két páratlan szám négyzete · Összefoglaló.
- **Sejtés → bizonyítás:** a csúszkás ábra bizonyos számokra mutatja; a panel kimondja, hogy
  a területes bizonyítás pozitív a, b-re szól, az általános bizonyítás a szorzás tagonkénti
  elvégzése (disztributivitás). Mindkettő látszik: a csempék *és* a kifejtés.
- **Számpéldák (ellenőrizve):** (3 + 5)² = 64, 3² + 5² = 34 (a hiány 2 · 15 = 30).
  47² = (50 − 3)² = 2500 − 300 + 9 = 2209. 99 · 101 = 100² − 1 = 9999. 103² = 10 609.
  7² − 3² = 40 = (7 + 3)·(7 − 3). Bűvésztrükk: gondolj egy számra (x), adj hozzá 3-at,
  szorozd 2-vel, vonj ki 4-et, oszd el 2-vel, vond ki az eredeti számot: (2(x + 3) − 4)/2 − x = 1.
  Két szomszédos páratlan szám négyzetének különbsége osztható 8-cal:
  (2k + 1)² − (2k − 1)² = 8k (pl. 9² − 7² = 32).
- **Építőkocka:** Darabolás (5–6), téglalapdarabok; **MatKeplet** (a 07-ből) a vásznon lévő
  azonosságokhoz. Kicsi, gyors lecke, jó próbája a képletjelölésnek (6. fejezet).
- **Meglévő anyag:** PhET *Area Model Algebra*.

### 06 · `06-egyenletrendszer` – Hány tyúk és hány nyúl? – egyenletek, egyenlőtlenségek, egyenletrendszerek

- **Tanulási cél:** A mérlegelv szerint az egyenlet mindkét oldalán ugyanazt a műveletet
  végezzük el. Egyenlőtlenségnél negatív számmal szorozva a reláció megfordul. Egy
  kétismeretlenes elsőfokú egyenlet megoldásai egy egyenest alkotnak, két egyenletéi a két
  egyenes metszéspontját. Párhuzamos egyeneseknél nincs megoldás, egybeesőknél végtelen sok.
  A kapott eredményt a szövegbe visszahelyettesítve ellenőrizzük: a „fél nyúl” nem megoldás.
- **Kerettanterv:** „ismeri és alkalmazza a következő egyenletmegoldási módszereket:
  mérlegelv, grafikus megoldás, szorzattá alakítás” · „megold elsőfokú egyismeretlenes
  egyenleteket és egyenlőtlenségeket, elsőfokú kétismeretlenes egyenletrendszereket” ·
  „Elsőfokú kétismeretlenes egyenletrendszer megoldása behelyettesítéssel, közös együtthatók
  módszerével, grafikusan” · „a modellben kapott megoldását az eredeti problémába
  visszahelyettesítve értelmezi, ellenőrzi, és az észszerűségi szempontokat figyelembe véve
  adja meg válaszát” · javasolt tevékenység: „Hiányos, túlhatározott, illetve ellentmondó
  adatokat tartalmazó problémák vizsgálata”.
- **Tévhitek:** az egyenlőtlenség ugyanúgy rendezhető, mint az egyenlet (−2x < 6 → x < −3).
  Ha kijött egy szám, az már a válasz. Minden egyenletrendszernek pontosan egy megoldása van.
  A grafikus megoldás „csak közelítés”, ezért nem számít.
- **Kulcsvizuál:** (a) kétkarú mérleg: a bal tálon 3 doboz + 5 golyó, a jobbon 1 doboz +
  13 golyó; mindkét oldalról ugyanaz kerül le, amíg 1 doboz = 4 golyó nem marad. (b)
  Számegyenes, amelyet a −1-gyel szorzás *tükröz*: a 2 < 3 pontpár helyet cserél, a nyíl
  megfordul. (c) Az udvar tyúkjai és nyulai (stilizált ikonok) mellett koordináta-rendszer,
  benne az x + y = 35 („fejek”) és a 2x + 4y = 94 („lábak”) egyenes; a metszéspont (23; 12).
- **Interaktív:** a lábak száma csúszkával (70–140): a „lábak” egyenes eltolódik, a
  metszéspont vándorol. Páratlan lábszámnál fél nyúl, 140 fölött negatív tyúk jelenik meg,
  pirossal áthúzva – a matematikai megoldás létezik, a feladatnak nincs megoldása. „Minden
  állat kétlábú” gomb: a két egyenes párhuzamos lesz (ellentmondó), 70 lábnál egybeesik
  (hiányos adat: végtelen sok megoldás).
- **Lépések:** A mérleg: mindkét oldalon ugyanazt · Egyenlőtlenség: mikor fordul a jel? ·
  Két tarifa: melyik éri meg? (grafikus megoldás) · Tyúkok és nyulak: két egyenlet · Egy
  egyenlet = egy egyenes · A metszéspont a megoldás · Fél nyúl? Ellenőrzés · Párhuzamos és
  egybeeső egyenesek · Összefoglaló.
- **Számpéldák (ellenőrizve):** 3x + 5 = x + 13 → 2x = 8 → x = 4 (ellenőrzés: 17 = 17).
  −2x < 6 → x > −3. Kitalált taxitarifák (bélyeg: „kitalált adat”): A: 700 Ft + 400 Ft/km,
  B: 1000 Ft + 350 Ft/km; 6 km-nél mindkettő 3100 Ft, 6 km fölött a B olcsóbb. Tyúk–nyúl:
  35 fej, 94 láb → 23 tyúk, 12 nyúl (23 + 12 = 35; 46 + 48 = 94). 95 lábnál y = 12,5;
  150 lábnál x = −5. Két kétlábú: x + y = 35 és 2x + 2y = 94 párhuzamos (nincs megoldás),
  2x + 2y = 70 egybeesik vele.
- **Történeti adat:** a tyúk–nyúl feladat (35 fej, 94 láb) a kínai *Szun-ce matematikai
  kézikönyvében* (Sunzi suanjing, kb. 3–5. század) szerepel *(ellenőrizendő; nem azonos „A
  háború művészete” szerzőjével)*.
- **Építőkocka:** **MatFv** (két egyenes, metszéspont, kiemelt tengelyszakasz), Számegyenes
  (5–6, tükrözés-animációval). Mérleg: leckén belül (a fizika 01-es mérlege ötletnek jó).
- **Meglévő anyag:** PhET *Equality Explorer* (mérleg), GeoGebra.

### 07 · `07-fuggveny-transzformacio` – Merre mozdul a parabola? – függvények és transzformációik

*Referencialecke: ez építi a **MatFv** és a **MatKeplet** modult (5. fejezet).*

- **Tanulási cél:** A függvény hozzárendelés: minden x-hez pontosan egy y tartozik. A
  grafikonról leolvasható az értelmezési tartomány, az értékkészlet, a zérushely, a
  szélsőérték, a növekedés és a fogyás. A négy alaptranszformáció: f(x) + c függőleges
  eltolás; f(x + c) vízszintes eltolás **c-vel balra** (pozitív c-nél); c·f(x) függőleges
  nyújtás; |f(x)| a tengely alatti rész felhajtása. A kölcsönösen egyértelmű függvény
  megfordítható, a grafikonja az y = x egyenesre tükröződik.
- **Kerettanterv:** „képlettel adott függvényt hagyományosan és digitális eszközzel ábrázol” ·
  „a grafikonról megállapítja függvények alapvető tulajdonságait” · „Lineáris függvény,
  másodfokú függvény, négyzetgyökfüggvény, fordított arányosságot leíró függvény (elemi
  függvények) grafikonja, tulajdonságai” · „Elemi függvényekkel egyszerű függvénytranszformációs
  lépések végrehajtása: f(x) + c, f(x + c), c·f(x), |f(x)|” · „Egyszerű függvények esetén az
  f(x) = c alapján x meghatározása […]” · „Kölcsönösen egyértelmű hozzárendelés megfordítása
  és a megfordított hozzárendelés ábrázolása” · (7.) „Az egyenes és a fordított arányosság
  grafikonjának felismerése és elkészítése”.
- **Tévhitek:** az f(x + 3) jobbra tolja a grafikont (mert „+”). A 2·f(x) kétszer olyan
  „széles”. Minden görbe függvény (a kör is). A 1/x grafikonja a 0-nál „összeér”. Az
  értékkészlet = az y-tengely. Az |f(x)| ugyanaz, mint az f(|x|).
- **Kulcsvizuál:** „függvénygép”: x golyó megy be, f(x) jön ki, a pár pontként esik a
  koordináta-rendszerbe, sok pontból összeáll a grafikon. Utána a transzformációs „labor”: a
  halvány, szaggatott alapgörbe (szellem) és az élénk transzformált görbe, a kettő között
  vékony nyilak a megfelelő pontpárokon. A vízszintes eltolásnál egy kiemelt pont: „az új
  görbe x-ben azt veszi fel, amit a régi x + 3-ban” – a nyíl **balra** mutat.
- **Interaktív:** alapfüggvény-választó (x, x², √x, 1/x, |x|), négy csúszka:
  g(x) = a · f(x + u) + v, és egy |·| kapcsoló. A képlet a vásznon élőben, a csúszkákkal
  szinkron színezett paraméterekkel. A csúcspont/kezdőpont húzható is (az u és a v
  csúszka követi). Az utolsó lépésben „Találd el!”: egy véletlen (de determinisztikus magból
  számolt) célgörbe jelenik meg, a diák a csúszkákkal fedi le.
- **Lépések:** A függvénygép · Mit árul el a grafikon? (ÉT, ÉK, zérushely, szélsőérték) ·
  Az elemi függvények (fordított arányosság is) · f(x) + c: fel és le · f(x + c): miért balra? ·
  c · f(x): nyújtás és tükrözés · |f(x)|: felhajtás · f(x) = c és a megfordítás (tükör az
  y = x-en) · Találd el a görbét!
- **Számpéldák (ellenőrizve):** g(x) = (x + 3)² csúcsa (−3; 0). g(x) = x² − 4 zérushelyei
  ±2; |x² − 4| a [−2; 2] szakaszon felhajtva, helyi maximuma 4 az x = 0-ban. x² = 5 →
  x = ±√5 ≈ ±2,236. 1/x: ÉT x ≠ 0, ÉK y ≠ 0. √x: ÉT x ≥ 0, ÉK y ≥ 0. f(x) = 2x + 1
  megfordítása x ↦ (x − 1)/2; az x² (x ≥ 0) megfordítása a √x. Fordított arányosság:
  x · y = 12 téglalapjai (1 × 12, 2 × 6, 3 × 4, 4 × 3, 6 × 2) csúcsai a 12/x hiperbolán.
- **Építőkocka:** **MatFv** és **MatKeplet** – itt készülnek. Koordináta-rendszer (5–6).
- **Meglévő anyag:** GeoGebra és Desmos (szabad függvényrajzolás csúszkákkal), PhET
  *Graphing Quadratics*. Nálunk a hangsúly a „miért balra?” magyarázatán és a tévhiteken van,
  nem a szabad kísérletezésen.

### 08 · `08-masodfoku` – Hol metszi a parabola a tengelyt? – teljes négyzet, megoldóképlet, diszkrimináns

- **Tanulási cél:** A teljes négyzetté kiegészítés szó szerint egy négyzet kiegészítése: az
  x² + 10x két téglalappal kiegészített négyzetből csak egy sarok hiányzik. Ebből jön a
  megoldóképlet. A másodfokú egyenlet megoldásai a parabola és az x tengely metszéspontjai; a
  diszkrimináns előjele mondja meg, hány ilyen pont van. A gyöktényezős alak a zérushelyeket
  mutatja. A másodfokú egyenlőtlenség megoldása az a szakasz, ahol a parabola a tengely
  alatt (fölött) van.
- **Kerettanterv:** „megold másodfokú egyismeretlenes egyenleteket és egyenlőtlenségeket;
  ismeri és alkalmazza a diszkriminánst, a megoldóképletet és a gyöktényezős alakot” ·
  „Másodfokú egyenlet megoldása szorzattá alakítással, teljes négyzetté kiegészítéssel,
  megoldóképlettel és grafikusan” · „Másodfokú egyenlőtlenség megoldása grafikusan” · (6.)
  „Egyszerű másodfokú polinom átalakítása teljes négyzetté kiegészítéssel” · (10.) javasolt
  tevékenység: „[…] adott hosszúságú spárgával bekeríthető maximális területű téglalap
  adatainak mérése, megfigyelése”.
- **Tévhitek:** az x² = 9 megoldása csak x = 3. Az x² = 3x egyenletet x-szel osztva
  „x = 3” – elveszik az x = 0. Negatív diszkriminánsnál „elrontottam a számolást”. Az
  x² − x − 6 < 0 megoldása „x < 3”.
- **Kulcsvizuál:** al-Hvárizmi négyzete: az x² négyzet két oldalára 5 · x-es csík kerül, a
  sarokban 5 × 5-ös lyuk marad; kitöltve egy (x + 5) oldalú, 64 területű négyzet lesz. Utána
  a parabola: a teljes négyzetes alakból a csúcs, a csúcsból a két metszéspont szimmetrikusan
  ± √(…) távolságra.
- **Interaktív:** a, b, c csúszkák: a parabola, a csúcspont, a zérushelyek és a diszkrimináns
  „mérője” (negatív – nulla – pozitív sáv) élőben. Ha D < 0, a metszéspont-jelzők a tengelyen
  „eltűnnek” (halvány üres karika). A spárga-lépésben a téglalap egyik oldala húzható, mellette
  a T(x) = x · (10 − x) parabolán fut a pont, a csúcsnál felvillan a „maximum”.
- **Lépések:** Al-Hvárizmi négyzete · Teljes négyzet a betűkkel · A parabola csúcsa · Hol
  metszi a tengelyt? · Diszkrimináns: kettő, egy vagy nulla · Megoldóképlet és gyöktényezős
  alak · Ne ossz x-szel! · Mikor negatív? (egyenlőtlenség) · A legnagyobb kert.
- **Számpéldák (ellenőrizve):** x² + 10x = 39 → (x + 5)² = 64 → x = 3 (és x = −13;
  al-Hvárizmi csak a pozitívat adta meg). x² − 4x + 3 = (x − 2)² − 1 = (x − 1)(x − 3),
  D = 16 − 12 = 4, zérushelyek 1 és 3, csúcs (2; −1). 2x² + 3x − 2 = 0: D = 25,
  x = (−3 ± 5)/4 → 0,5 és −2. x² − x − 6 < 0 ⟺ (x − 3)(x + 2) < 0 ⟺ −2 < x < 3. 20 m spárga:
  T(x) = x(10 − x), a maximum 25 m² az 5 × 5-ös négyzetnél (6 × 4 → 24 m², 7 × 3 → 21 m²).
- **Történeti adat:** al-Hvárizmi (Muhammad ibn Músza al-Hvárizmi) bagdadi könyve kb. 820–830
  körül készült; a címében szereplő *al-dzsabr* szóból lett az „algebra” *(az átírás és a
  dátum ellenőrizendő)*.
- **Építőkocka:** **MatFv** (a 07-ből), Darabolás (5–6), MatKeplet.
- **Meglévő anyag:** PhET *Graphing Quadratics*.

### 09 · `09-pitagorasz` – Miért éppen a² + b² = c²? – a Pitagorasz-tétel bizonyításai

- **Tanulási cél:** Derékszögű háromszögben a befogókra rajzolt négyzetek együttes területe
  egyenlő az átfogóra rajzolt négyzet területével. Ez átdarabolással bizonyítható. A
  megfordítás is igaz: ha a² + b² = c², a háromszög derékszögű; tompaszögnél c² nagyobb,
  hegyesszögnél kisebb.
- **Kerettanterv:** „ismeri és alkalmazza a Pitagorasz-tételt és megfordítását” · „A
  Pitagorasz-tétel bizonyítása” · „Háromszög területének kiszámítása” · javasolt tevékenység:
  „A derékszögű háromszög oldalaira szerkesztett négyzetek átdarabolása a Pitagorasz-tételnek
  megfelelő módon, pitagoraszi tangramok vagy dinamikus geometriai szoftver alkalmazásával”.
- **Tévhitek:** a tétel minden háromszögre igaz. A „c” mindig a vízszintes vagy az utolsónak
  megnevezett oldal (nem: az átfogó, a derékszöggel szemközti). a + b = c („a két rövidebb
  oldal összege”). A tétel csak egész számokra (3, 4, 5) igaz. Pitagorasz fedezte fel.
- **Kulcsvizuál:** (1) Két egyforma, a + b oldalú négyzet. Az egyikben négy derékszögű
  háromszög körbefogja a c² négyzetet; a háromszögek merev mozgással átrendeződnek, és a
  maradék helyén a² és b² jelenik meg. A „le nem fedett terület” színe végig ugyanaz marad.
  (2) Eukleidész nyírása: az a² négyzet területtartó nyírással paralelogrammává, majd az
  átfogó-négyzet egy téglalapjává alakul (azonos alap, azonos magasság).
- **Interaktív:** a derékszögű csúcs húzható egy félkörön (Thalész-kör, a 11-es előzetese), a
  három négyzet élő területe és a² + b² − c² = 0 kijelzés. „Megfordítás” lépésben a szög
  szabadon állítható (60°–150°), a mérleg-ikon jelzi, melyik oldal nagyobb. „Tévé” kérdés: a
  képernyőátló csúszkával (32–85″), a 16 : 9-es kép szélessége és magassága cm-ben.
- **Lépések:** Három négyzet egy háromszögön · Mérjük meg! (sejtés) · Négy háromszög
  két keretben (bizonyítás) · Eukleidész nyírása · Ha nem derékszög? · A megfordítás · Egész
  számhármasok · Mekkora az 55 colos tévé? · Összefoglaló.
- **Sejtés → bizonyítás:** a 2. lépés csak mér (néhány háromszögre egyezik), a 3. bizonyít,
  és a panel kimondja: a mérés sosem bizonyíték.
- **Számpéldák (ellenőrizve):** 3² + 4² = 5²; 5–12–13; 8–15–17; 20–21–29 (400 + 441 = 841 =
  29²). a = 3, b = 4, γ = 60° esetén c² = 13 < 25, γ = 120°-nál c² = 37 > 25 (a koszinusztételt
  nem nevezzük meg, a vászon a rajzból mér). 55″ = 139,7 cm átló; 16 : 9-es képnél a
  szélesség ≈ 121,8 cm, a magasság ≈ 68,5 cm.
- **Történeti adat:** a tétel jóval Pitagorasz előtt ismert volt: a babiloni *Plimpton 322*
  agyagtábla (kb. Kr. e. 1800) pitagoraszi számhármasokat tartalmaz (értelmezése vitatott).
  J. A. Garfield, később amerikai elnök, 1876-ban közölt egy trapézos bizonyítást
  *(ellenőrizendő; kitekintésként, a megjegyzésben)*.
- **Építőkocka:** Darabolás (5–6) merev mozgással, nyírással bővítve (leckén belül);
  **MatSzerk** (a 10-ből) a húzható háromszöghöz és a derékszögjelhez.
- **Meglévő anyag:** számtalan GeoGebra-bizonyítás; az NKP tankönyvi ábrái.

### 10 · `10-nevezetes-pontok` – Hol legyen a mentőállomás? – a háromszög nevezetes pontjai és körei

*Referencialecke: ez építi a **MatSzerk** szerkesztő-motort (5. fejezet).*

- **Tanulási cél:** A szakaszfelező merőleges azon pontok halmaza, amelyek a szakasz két
  végpontjától egyenlő távolságra vannak; a szögfelező azoké, amelyek a két szögszártól. Ebből
  következik, hogy a háromszög három oldalfelező merőlegese egy pontban metszi egymást (a
  körülírt kör középpontja), és a három belső szögfelező is (a beírt kör középpontja). A
  súlyvonalak a súlypontban 2 : 1 arányban metszik egymást, a magasságvonalak a
  magasságpontban.
- **Kerettanterv:** „ismeri és alkalmazza a háromszög nevezetes vonalaira, pontjaira és köreire
  vonatkozó fogalmakat és tételeket” · „A háromszög nevezetes vonalaira, pontjaira és köreire
  vonatkozó fogalmak, tételek ismerete és alkalmazása: oldalfelező merőleges, szögfelező,
  magasságvonal, súlyvonal, középvonal, körülírt, illetve beírt kör” · „Az oldalfelező
  merőlegesek és a belső szögfelezők metszéspontjára vonatkozó tétel bizonyítása” · (11.)
  „A szakaszfelező merőleges és a szögfelező mint ponthalmazok tulajdonságainak ismerete” ·
  (11.) „Alapszerkesztések végrehajtása hagyományos vagy digitális eszközzel euklideszi módon:
  szakaszfelező merőleges, szögfelező, merőleges és párhuzamos egyenesek szerkesztése, szög
  másolása” · (11.) javasolt tevékenység: „Számszerű adatként csak méretarányt tartalmazó
  térképen adott helységektől (közelítőleg) egyenlő távolságra levő helységek megkeresése”.
- **Tévhitek:** a körülírt kör középpontja mindig a háromszög belsejében van. A súlypont, a
  beírt és a körülírt kör középpontja ugyanaz a pont. A szögfelező felezi a szemközti oldalt.
  Három egyenes „általában” egy pontban metszi egymást (pedig ez itt tétel, nem véletlen).
- **Kulcsvizuál:** három település egy vázlatos Magyarország-térképen (Budapest, Debrecen,
  Szeged). „Hol legyen a mentőállomás, hogy mindháromtól egyformán messze legyen?” Körzős
  szerkesztés animálva: két körív, az összekötő egyenes = szakaszfelező merőleges. Egy
  futópont a merőlegesen végigmegy, a két távolságot mutató szakasz mindig egyforma. A két
  merőleges metszéspontjából a kör mindhárom városon átmegy.
- **Interaktív:** a csúcsok húzhatók (térkép nélkül, üres rajzlapon is). Kapcsolók a négy
  nevezetes ponthoz (K, O, S, M – a betűk a `.md` Feliratok-ból jönnek, tankönyvenként
  eltérhetnek). Tompaszögnél a K kilép, derékszögnél az átfogó felezőpontjára ül (felvillan:
  „Thalész → 11. lecke”). Súlypont: a háromszög egy „tűhegyen” egyensúlyoz, ha a tűt a
  súlypontra húzzuk, máshol billen. Kitekintés: az Euler-egyenes (K, S, M egy egyenesen,
  KS : SM = 1 : 2) kapcsolóval.
- **Lépések:** Hol legyen a mentőállomás? · Szerkesszünk: szakaszfelező merőleges · Egyenlő
  távolság = ponthalmaz · Miért metszik egymást egy pontban? (bizonyítás) · Tompa- és
  derékszög: hová kerül a K? · Szögfelezők és a beírt kör · Súlyvonal és súlypont ·
  Magasságpont és az Euler-egyenes · Összefoglaló.
- **Sejtés → bizonyítás:** a húzogatás azt sejteti, hogy a három merőleges mindig egy pontban
  metszi egymást; a bizonyítás a ponthalmaz-tulajdonságból három sor (PA = PB és PB = PC ⇒
  PA = PC). A súlypont 2 : 1 arányát és az Euler-egyenest *nem* bizonyítjuk, ezt a panel
  kimondja („mérés, nem bizonyítás”).
- **Számpéldák (ellenőrizve, közelítő):** Budapest (47,50° É, 19,04° K), Debrecen (47,53° É,
  21,63° K), Szeged (46,25° É, 20,14° K) körülírt körének középpontja kb. 47,19° É,
  20,34° K, Törökszentmiklós mellett (kb. 6 km-re, Szolnoktól kb. 12 km-re), a sugár kb.
  105 km (helyi, síkba vetített számítás, a gyártáskor a lecke vetületével újraszámolandó)
  *(ellenőrizendő)*. Súlypont a súlyvonalon a csúcstól 2/3-nyira.
- **Építőkocka:** **MatSzerk** – itt készül. Térkép: `shared/tort/map-karpat.js` és
  `TortProj` (közös adat, a történelemmel); a lecke csak a partvonalat/országkontúrt és három
  várost rajzolja, halványan, „vázlatos” bélyeggel.
- **Meglévő anyag:** GeoGebra-szerkesztések; nálunk a hangsúly a ponthalmaz-érvelésen és a
  térképes alkalmazáson van.

### 11 · `11-kor-thalesz` – Miért mindig derékszög? – Thalész-tétel, érintő, körív

- **Tanulási cél:** Ha egy háromszög egyik oldala a kör átmérője, és a harmadik csúcs a körön
  van, akkor ott a szög derékszög (Thalész-tétel); megfordítva: a derékszög csúcsa az átfogó
  fölé rajzolt körön van. A kör érintője merőleges az érintési pontba húzott sugárra, és egy
  külső pontból húzott két érintőszakasz egyenlő hosszú. A körív hossza és a körcikk
  területe egyenesen arányos a középponti szöggel.
- **Kerettanterv:** „ismeri és alkalmazza a Thalész-tételt és megfordítását” · „A Thalész-tétel
  bizonyítása” · „ismeri a kör érintőjének fogalmát, kapcsolatát az érintési pontba húzott
  sugárral” · „Annak ismerete és alkalmazása, hogy a kör érintője merőleges az érintési pontba
  húzott sugárra, és hogy külső pontból húzott érintőszakaszok egyenlő hosszúak” · „Annak
  ismerete és alkalmazása, hogy a középponti szög egyenesen arányos a hozzá tartozó körív
  hosszával” · „ki tudja számolni a kör és részeinek kerületét, területét” · javasolt
  tevékenység: „A Thalész-tétel felfedeztetése szerkesztéssel, szögméréssel vagy dinamikus
  geometriai szoftver alkalmazásával”.
- **Tévhitek:** a szög a félkör tetején a legnagyobb, a szélek felé csökken. Az érintő az az
  egyenes, amelynek egy közös pontja van a körrel (igaz, de a „súrolja” szemlélet a szelőt is
  ideérti). A kétszer akkora középponti szöghöz kétszer akkora *húr* tartozik.
- **Kulcsvizuál:** félkör, a C pont végigcsúszik rajta, a szögív mindig 90°-ot mutat (a
  derékszögjel „rátapad”). A bizonyításnál a CO sugár behúzásával két egyenlő szárú háromszög
  jelenik meg, a szögeik színe α, β – a háromszög szögösszegéből α + β = 90°. Ácstrükk: egy
  derékszögű vonalzó csúcsát a körre téve a két szár a kör átmérőjének végpontjait jelöli ki;
  két átmérő metszéspontja a középpont.
- **Interaktív:** C húzható a körön (és a körön *kívül/belül* is: a szög tompa, illetve hegyes
  lesz – a megfordítás szemléltetése). Szelő → érintő: egy egyenes a kör egyik pontja körül
  forog, a második metszéspont rácsúszik az elsőre, ekkor a sugárral bezárt szög 90°. Külső
  pont húzható, a két érintőszakasz hossza élőben. Középponti szög csúszkával: ív, körcikk,
  és mellettük az arány.
- **Lépések:** Mérjük meg a szöget (sejtés) · Két egyenlő szárú háromszög (bizonyítás) · A
  megfordítás: kívül tompa, belül hegyes · Ácstrükk: hol a kör középpontja? · Szelőből érintő ·
  Érintő szerkesztése külső pontból · Két egyenlő érintőszakasz · Ív és cikk: arány a szöggel ·
  Összefoglaló.
- **Számpéldák (ellenőrizve):** r = 10 cm, 72°: ív = 2π · 10 · 72/360 ≈ 12,57 cm, körcikk =
  π · 10² · 72/360 ≈ 62,83 cm². Körgyűrű R = 10 cm, r = 6 cm: π · (100 − 36) ≈ 201,06 cm².
  Érintőszakasz: a középponttól 13 cm-re lévő pontból egy 5 cm sugarú körhöz
  √(13² − 5²) = 12 cm (kapcsolat a 09-cel).
- **Történeti adat:** a tételt a hagyomány Thalésznek (Milétosz, kb. Kr. e. 6. század)
  tulajdonítja; erről csak jóval későbbi szerzők írnak, ezért „a hagyomány szerint”.
- **Építőkocka:** **MatSzerk** (kör–egyenes metszés, érintő, szögív és derékszögjel, húzható
  pont pályára kötve).

### 12 · `12-egybevagosag-parketta` – Hogyan fedi le a csempe a síkot? – tükrözés, forgatás, eltolás, parketta

- **Tanulási cél:** A tengelyes tükrözés megtartja a távolságot és a szöget, de megfordítja a
  körüljárási irányt. Két tükrözés egymásutánja párhuzamos tengelyeknél eltolás (a tengelyek
  távolságának kétszeresével), metsző tengelyeknél forgatás (a tengelyek szögének
  kétszeresével). Az eltolást egy vektor adja meg. A konvex n-szög belső szögeinek összege
  (n − 2) · 180°, a külső szögeké 360°. A síkot azok a szabályos sokszögek fedik le hézag
  nélkül, amelyek belső szöge osztója a 360°-nak: a háromszög, a négyzet és a hatszög; és
  **bármely** háromszög vagy négyszög.
- **Kerettanterv:** „ismeri és alkalmazza a síkbeli egybevágósági transzformációkat és
  tulajdonságaikat; alakzatok egybevágóságát” · „A vektor fogalmának kialakítása a
  párhuzamos eltolás segítségével” · „Egybevágósági transzformációk egymás utáni végrehajtása” ·
  „Gyakorlati feladatok megoldása egybevágóságok segítségével (például a sík parkettázása
  különféle síkidomokkal; szabásminta készítése, használata)” · javasolt tevékenység: „A
  középpontos tükrözés, a pont körüli forgatás és a párhuzamos eltolás bemutatása mint két
  tengelyes tükrözés egymásutánja” · „M. C. Escher és Victor Vasarely néhány interneten is
  elérhető alkotásának elemzése a szimmetriák szempontjából; hasonló módszerrel képek
  alkotása” · (13.) „Konvex sokszögeknél az átlók számára, a belső és külső szögösszegre
  vonatkozó tételek ismerete, bizonyítása és alkalmazása” · (13.) „ismeri és alkalmazza a
  szabályos sokszög fogalmát; kiszámítja a konvex sokszög belső és külső szögeinek összegét”.
- **Tévhitek:** a tükörkép „ugyanaz” az alakzat (a jobb kesztyű tükörképe bal kesztyű). Két
  tükrözés = egy tükrözés. A szabályos ötszög is parkettáz („hiszen a focilabda…” – az gömb,
  és hatszög is van rajta). Csak a szabályos sokszögek parkettáznak.
- **Kulcsvizuál:** egy aszimmetrikus figura (stilizált „F” betű vagy csizma) két tükörben:
  párhuzamosaknál az eredmény egyszerűen eltolódik, a két tengely távolságát és az eltolás
  nyilát (vektort) méretjel köti össze. Metsző tengelyeknél forgásív, 2φ felirattal. A
  parkettában a csempék egy közös csúcs körül körbeforognak, a szögek egy 360°-os
  „tortadiagrammá” állnak össze, az ötszögnél rés marad.
- **Interaktív:** a két tükörtengely húzható és forgatható, az eredő transzformáció élőben
  (eltolásvektor vagy forgásközéppont + szög). Sokszögválasztó (n = 3…8): belső szög és
  parkettapróba. „Saját csempe”: a négyzet egyik oldalára 2–3 húzható pontot tehetünk, ez a
  görbe eltolással a szemközti oldalra másolódik (Escher *módszere*, nem Escher-mű), és a csempe
  azonnal kitölti a síkot. Négyszög-parketta: egy tetszőleges (akár konkáv) négyszög csúcsai
  húzhatók, a parketta az oldalfelező pontok körüli 180°-os forgatásokkal épül.
- **Lépések:** Tükör: mi marad meg, mi fordul meg? · Két párhuzamos tükör = eltolás
  (vektor) · Két metsző tükör = forgatás · Sokszögek szögösszege · Melyik szabályos sokszög
  parkettáz? · Bármely háromszög és négyszög · Rajzolj saját csempét! · Kitekintés: csempe,
  amely sosem ismétlődik · Összefoglaló.
- **Sejtés → bizonyítás:** a szögösszeget a sokszög háromszögekre bontása bizonyítja (n − 2
  háromszög, a háromszög 180°-a a párhuzamos és a váltószögek miatt – egy mondat, ábrával). A
  „két tükrözés = forgatás” az ábrán szögfelezéssel bizonyítható; a panel egy mondatban
  mutatja.
- **Számpéldák (ellenőrizve):** belső szögek: háromszög 60°, négyzet 90°, ötszög 108°,
  hatszög 120°, hétszög ≈ 128,57°, nyolcszög 135°; 360/60 = 6, 360/90 = 4, 360/120 = 3,
  360/108 ≈ 3,33 (nem egész). Szögösszeg: ötszög 540°, hatszög 720°. Átlók száma n(n − 3)/2:
  5 → 5, 6 → 9, 10 → 35.
- **Kitekintés (ellenőrizendő):** konvex ötszögekből 15 parkettázó típus ismert, az utolsót
  2015-ben találták, a lista teljességét 2017-ben bizonyították (M. Rao). 2023-ban
  találtak egy 13 oldalú sokszöget („kalap”), amely csak nem ismétlődő módon fedi le a
  síkot (D. Smith és társai). Ezek a megjegyzésbe vagy a kitekintő lépésbe kerülnek.
- **Jogok:** Escher (†1972) és Vasarely (†1997) művei jogvédettek: a leckében nem jelennek meg,
  csak a módszerüket mutatjuk saját, kóddal rajzolt csempén.
- **Építőkocka:** Geo-transzformációk (5–6: tengelyes tükrözés, eltolás, forgatás merev
  mozgásként), **MatSzerk** (húzható tengelyek, szögív). A parketta-kitöltés (rácsban ismételt
  csempe, a látható tartományra vágva) leckén belül.

### 13 · `13-hasonlosag` – Milyen magas a torony? – nagyítás, hasonlóság, területarány

- **Tanulási cél:** A középpontos hasonlóság (nagyítás) minden távolságot λ-szorosára változtat,
  a szögeket megtartja. Hasonló alakzatoknál a kerületek aránya λ, a területeké λ². A
  hasonlóság a valóságban mérésre használható: egy bot és az árnyéka megadja a torony
  magasságát, egy térkép méretaránya a valódi távolságot.
- **Kerettanterv:** „ismeri és alkalmazza a középpontos hasonlósági transzformációt, a
  hasonlósági transzformációt és az alakzatok hasonlóságát” · „ismeri és alkalmazza a hasonló
  síkidomok kerületének és területének arányára vonatkozó tételeket” · „Gyakorlati feladatok
  megoldása hasonlóság segítségével (például alaprajz-, térképkészítés, modellezés)” · javasolt
  tevékenység: „Az iskola közelében lévő magas épület (például templomtorony) magasságának
  meghatározása egy egyenes bot segítségével a bot és az épület árnyékának méréséből
  („Thalész-módszer”) csoportmunkában” · (11.) „Számszerű adatként csak a méretarányt
  tartalmazó térkép alapján valódi távolságok meghatározása, becslése”.
- **Tévhitek:** kétszer akkora oldalhoz kétszer akkora terület tartozik. Két 22 cm-es pizza
  több, mint egy 32 cm-es. A hasonló alakzatok csak „nagyobbak”, a λ < 1 nem hasonlóság. Minden
  téglalap hasonló.
- **Kulcsvizuál:** egy középpontból sugarak indulnak; a háromszög csúcsai a sugarakon
  csúsznak, a λ csúszka szerint. Mellette a kis háromszög csempéi λ² darabban töltik ki a
  nagyot (λ = 2-nél 4, λ = 3-nál 9 egybevágó kis háromszög). A torony-jelenet: Nap, bot,
  torony, két árnyék, a két hasonló derékszögű háromszög kiemelve. Az A-papírsor: A0 → A1 →
  … → A4 egymásba hajtva, mindegyik az előző fele, és mindegyik hasonló (λ = 1/√2).
- **Interaktív:** λ csúszka (0,25–3) és húzható középpont; kerület- és területarány
  élőben. Torony: a Nap magassága csúszkával (az árnyékok változnak, a kiszámolt magasság
  nem). Pizza-kérdés: két átmérő-csúszka, a területek oszlopa.
- **Lépések:** Nagyítás egy pontból · Mi marad meg? (szög, arány) · Kétszeres oldal,
  négyszeres terület · Pizza-kérdés · Thalész a piramisnál: árnyékmérés · Méretarányos térkép ·
  Az A4-es lap családja · Összefoglaló.
- **Számpéldák (ellenőrizve):** λ = 2 → terület 4×, λ = 3 → 9×. Pizza: 32² = 1024 >
  2 · 22² = 968 (az egy nagy kb. 5,8 %-kal több). Bot 1 m, árnyéka 1,6 m; a torony árnyéka 48 m
  → a torony 30 m. Kheopsz-piramis eredeti magassága ≈ 146,6 m (a történelem 02-vel azonos
  adat). 1 : 50 000-es térkép: 4 cm → 2 km; 1 cm² → 0,25 km². A0 = 1 m² (841 × 1189 mm), A4 =
  210 × 297 mm; két A4 egy A3 (λ = √2, terület 2×) – kapcsolat a 01-gyel.
- **Történeti adat:** a hagyomány szerint Thalész a piramis magasságát árnyékméréssel
  határozta meg (Diogenész Laertiosz, Plutarkhosz – jóval későbbi szerzők; „a hagyomány
  szerint”).
- **Építőkocka:** Geo-transzformációk (5–6) + középpontos hasonlóság (leckén belül, a MatSzerk
  transzformációs részéhez illesztve), MatSzerk (párhuzamos, arányjelek).

### 14 · `14-statisztika` – Kinek hazudik az átlag? – középértékek és diagramtrükkök

- **Tanulási cél:** Az átlag az adatok „egyensúlyi pontja”, a medián a középső adat, a módusz
  a leggyakoribb. Egy kiugró adat az átlagot erősen elhúzza, a mediánt alig. Ugyanaz az adat
  egy diagramon megtévesztő lehet: levágott tengely, felületarányos ikonok, 3D-s kördiagram.
  Oszlopdiagram és kördiagram ugyanazt az adatot más kérdésre mutatja.
- **Kerettanterv:** „hagyományos és digitális forrásból származó adatsokaság alapvető
  statisztikai jellemzőit meghatározza, értelmezi és értékeli” · „felismer grafikus
  manipulációkat diagramok esetén” · „Statisztikai adatok rendszerezése, jellemzése
  középértékekkel hagyományos és digitális eszközzel” · „Kördiagramból oszlopdiagram készítése
  és viszont” · „Grafikus manipulációk felismerése és javítása diagramok esetén” · javasolt
  tevékenység: „Érvelés a tanuló saját érdemjegyei alapján különböző statisztikai jellemzők
  segítségével a kedvezőbb év végi jegyért”.
- **Tévhitek:** az átlag „a tipikus érték”. A medián az adatsor középső *eleme* rendezés
  nélkül. Két oszlop magasságaránya mindig az adatok aránya. A nagyobb ikon „csak szebb”.
- **Kulcsvizuál:** számegyenes-mérleghinta: az adatok súlyok, az átlag az alátámasztási pont,
  amelyen a hinta egyensúlyban van. Ha egy adatot jobbra húzunk, a hinta billen, és az
  alátámasztás utánacsúszik; a medián-jelző közben áll. Diagram-morf: az oszlopdiagram
  oszlopai egymás után „meghajlanak”, és kördiagram-cikkekké tekerednek (és vissza).
- **Interaktív:** az adatpöttyök húzhatók; az átlag, a medián és a módusz élőben. „Megérkezik
  a tulajdonos” gomb: egy kiugró fizetés esik a hintára. Diagram-labor: a tengely kezdete
  csúszkával (0 → 45 %), és mellette egy „hányszor nagyobbnak látszik?” mérő; ikonos
  diagramnál „lineáris” ↔ „területarányos” kapcsoló.
- **Lépések:** Az átlag mint egyensúly · Medián: a középső · Módusz · Jön egy kiugró adat ·
  Melyik jegy jár? (érvelés) · Oszlopból kör, körből oszlop · A levágott tengely · Az ikonok
  csapdája · Összefoglaló.
- **Számpéldák (ellenőrizve):** jegyek 2, 3, 5, 5, 5: átlag 4,0, medián 5, módusz 5 („a
  medián szerint ötös”). Kitalált kis cég (bélyeg: „kitalált adat”), 9 dolgozó havi bére ezer
  forintban: 400, 420, 450, 450, 480, 500, 520, 550, 600 → átlag ≈ 485,6, medián 480. Ha
  belép a tulajdonos 6000-rel: átlag 1037, medián 490. Levágott tengely: 52 % és 48 %, a tengely
  45 %-tól → az oszlopok 7 : 3 arányúak, a különbség 2,33-szorosnak látszik. Kétszer akkora
  értékhez kétszeres oldalú ikon → négyszeres terület (kapcsolat a 13-mal).
- **Valódi adat (opcionális):** a magyar bruttó átlagkereset és mediánkereset különbsége (KSH)
  jó záró példa, de csak a gyártás napján letöltött, forrással megadott adattal *(frissítendő)*.
- **Építőkocka:** Diagram (5–6: oszlop- és kördiagram), kiegészítve a leckén belül: oszlop ↔
  kör morf, tengely-levágás; a hinta a Számegyenesre épül.
- **Meglévő anyag:** PhET *Mean: Share and Balance* (alsóbb szint), a KSH oktatási anyagai.

### 15 · `15-valoszinuseg` – Mit tud a véletlen? – relatív gyakoriság, klasszikus modell, Galton-deszka

- **Tanulási cél:** Egy esemény relatív gyakorisága sok kísérlet után egy szám körül
  ingadozik, egyre kisebb kilengéssel – ez a valószínűség statisztikai fogalma. Ha az elemi
  események egyformán valószínűek, a valószínűség a kedvező és az összes eset hányadosa
  (klasszikus modell). A kockának nincs emlékezete: független kísérleteknél a korábbi
  eredmények nem számítanak. A Galton-deszkán a golyók eloszlását az utak száma adja meg.
- **Kerettanterv:** „konkrét valószínűségi kísérletek esetében az esemény, eseménytér, elemi
  esemény, relatív gyakoriság, valószínűség, egymást kizáró események, független események
  fogalmát megkülönbözteti és alkalmazza” · „tapasztalatai alapján véletlen jelenségek
  jövőbeni kimenetelére észszerűen tippel” · „véletlen kísérletek adatait rendszerezi, relatív
  gyakoriságokat számol, nagy elemszám esetén számítógépet alkalmaz” · „A valószínűség
  fogalmának bevezetése statisztikai alapon” · „A klasszikus valószínűségi modell fogalma és
  alkalmazása” · „Diszkrét valószínűség-eloszlások ábrázolása hagyományos és digitális
  eszközzel” · javasolt tevékenység: „Játékokban a szerencsefaktor vizsgálata, például „Ki
  nevet a végén” játék esetében az első hatos dobás eloszlása”.
- **Tévhitek:** öt fej után „jár már” az írás (szerencsejátékos-tévedés). Két kockával a 11 és
  a 12 egyformán valószínű („mindkettő egy összeg”). 10 dobásból pontosan 5 fej lesz. A
  valószínűség „csak elmélet”, a kísérlet „úgyis más”.
- **Kulcsvizuál:** (1) pénzfeldobás-szalag: a dobások egyre gyorsulva (10, 100, 1000, 10 000)
  sorakoznak, alattuk a relatív gyakoriság grafikonja „tölcsérben” áll be 0,5-re. (2) Két
  kocka 6 × 6-os rácsa, az átlók mentén azonos összegek: a 7-es átló a leghosszabb.
  (3) Galton-deszka 10 sorral: a golyók lepattognak, a rekeszekben oszlopok nőnek, fölöttük
  halványan az elméleti eloszlás; minden szög mellett kis szám: hány út vezet oda (minden szám a
  fölötte lévő kettő összege).
- **Interaktív:** dobásszám-gomb (+10, +100, +1000), minden kísérlet egy rögzített magú
  (`U.rng`) sorozatból jön, a látható állapot a dobásszámból számolható (visszaléptethető). A
  kockarácson a diák kijelöl egy eseményt (pl. „az összeg legalább 10”), a kedvező mezők
  kigyúlnak. Galton: golyószám-gomb és a szögek „ferdesége” (balra pattanás esélye 0,5 helyett
  0,3–0,7) csúszkán. „Ki nevet a végén”: hányadik dobásra jön az első hatos – 1000 játszma
  hisztogramja.
- **Lépések:** Fej vagy írás: tíz dobás · Tízezer dobás: a relatív gyakoriság beáll · Jár már az
  írás? (függetlenség) · Két kocka: 36 elemi esemény · Melyik összeg a leggyakoribb? · Ki nevet a
  végén? · A Galton-deszka · Utak száma és eloszlás · Összefoglaló.
- **Számpéldák (ellenőrizve):** két kockával P(7) = 6/36 ≈ 16,7 %, P(2) = P(12) = 1/36 ≈ 2,8 %,
  P(11) = 2/36 ≈ 5,6 %. Az első hatos az első dobásra 1/6 eséllyel jön; hat dobás alatt sem jön
  (5/6)⁶ ≈ 0,335 eséllyel. Legalább egy hatos négy dobásból: 1 − (5/6)⁴ ≈ 0,518; legalább egy
  dupla hatos 24 dobásból két kockával: 1 − (35/36)²⁴ ≈ 0,491 (de Méré lovag kérdése, Pascal és
  Fermat levelezése, 1654). Galton, 10 sor: a rekeszekbe vezető utak száma 1, 10, 45, 120, 210,
  252, 210, 120, 45, 10, 1 (összesen 1024); a középső rekesz esélye 252/1024 ≈ 24,6 %.
  Ötöslottó telitalálat: 1/43 949 268 ≈ 2,3 · 10⁻⁸ (a 03-ból).
- **Történeti adat:** hogy Leibniz a 11-et és a 12-t egyformán valószínűnek tartotta, gyakran
  idézett anekdota *(ellenőrizendő; csak forrással kerülhet be, különben a tévhit név nélkül
  szerepel)*. A de Méré-féle kérdés és a Pascal–Fermat levelezés (1654) jól dokumentált.
- **Építőkocka:** Véletlen (5–6: magolt véletlen, számlálók, gyakorisági táblázat), Diagram
  (hisztogram). A Galton-deszka leckén belül: a golyók útja a magból zárt képlettel számolható
  (sor → bal/jobb döntések), a pattogás animációja `L.st`-ből. A 03 *MatGraf* fa-elrendezése
  az útszámláláshoz átvehető.
- **Meglévő anyag:** PhET *Plinko Probability* (Galton-deszka) – nálunk a hangsúly az útszámlálás
  és a „Ki nevet a végén” kérdésen van.

---

## 4. Szerkesztői elvek

1. **Sejtés és bizonyítás külön.** A matematikában a dinamikus ábra bizonyos esetekre
   *mutat* valamit; a bizonyítás minden esetre szól. Minden tételt kimondó leckében legalább
   egy lépés **bizonyít** (a tanterv a nevezetes pontok, a Pitagorasz- és a Thalész-tételnél,
   a szögösszegnél és a hatványazonosságoknál kifejezetten kéri). Ahol csak mérünk vagy
   kísérletezünk, a panel kimondja („ez mérés, nem bizonyítás”). A vásznon a két szerepet
   jelölés különbözteti meg (6. fejezet, szerződés-kiegészítés).
2. **Egy gondolat, egy ábra.** Egy lépés egy összefüggést mutat. Nem rakunk ki egyszerre
   minden nevezetes pontot, minden képletet; ami nem fontos, halványul.
3. **Tévhit kimondva.** Minden leckében van egy lépés, amely a leggyakoribb hibát (pl.
   (a + b)² = a² + b², f(x + 3) jobbra) **szemtől szemben** mutatja, és a képen cáfolja.
4. **Becsületes számok.** A vásznon megjelenő minden szám abból a geometriából vagy modellből
   számolódik, amelyet a rajz mutat. Kerekített értéknél „≈” áll, és legfeljebb 2 tizedesjegy.
   A kitalált adat (taxitarifa, bérek) „kitalált adat” bélyeget kap; valódi adat csak
   forrással (`.md` megjegyzés) és dátummal.
5. **Történeti anekdota óvatosan.** Pitagorasz, Thalész, Hilbert, al-Hvárizmi: a hagyományt
   „a hagyomány szerint” kerettel mondjuk el, és megmondjuk, ha a tétel régebbi a névadójánál.
   A matematikatörténet érdekesség, nem tananyag – a `> megjegyzés:` vagy egy kitekintő lépés
   viszi.
6. **Jelölés a magyar tankönyvek szerint.** Tizedesvessző, pontosvessző a koordinátákban
   (A(2; −3)), nyílt intervallum ]a; b[, a nevezetes pontok betűi a `.md`-ből (tankönyvenként
   eltérnek). A részletek: szerződés-kiegészítés.
7. **Jogvédett kép nincs.** Escher, Vasarely, tankönyvi ábra, *Powers of Ten*: csak hivatkozás.
   Minden ábra saját, kóddal rajzolt.

---

## 5. Építőkockák és gyártási sorrend

### 5.1 Amit a Matek 5–6 közös készletétől várunk

A tervezett nevek a `Mat…` névteret követik (a történelem `Tort…` mintájára). Ha a Matek
5–6 más nevet vagy API-t választ, azt vesszük át, és ezt a táblázatot frissíteni kell.

| Modul (5–6) | Minimális elvárás a 9–10 szemszögéből | 9–10 leckék |
|---|---|---|
| **MatKoord** · koordináta-rendszer | világ ↔ képernyő leképezés, rács, tengelyek nyíllal, osztásfeliratok magyar tizedesvesszővel és valódi mínusszal (≥ 22 px), pont koordinátával (A(2; −3) alak), egyenes rajzolása, kamera (eltolás, nagyítás zárt képlettel); nem egész lépték (pl. 1 egység = 50 Ft) | 06, 07, 08, 14 |
| **MatSzam** · számegyenes | osztások több szinten (egész, tized, század), zoom egy pont köré, pont és intervallum (nyílt/zárt végpont: üres/teli karika), lépegetés-nyíl; tükrözés 0-ra animálva | 01, 04, 06, 14 |
| **MatGeo** · alapgeometria | pont, szakasz, egyenes, félegyenes, kör, körív, szögív felirattal, derékszögjel, egyenlőségjelek (vonalkák), sokszög kitöltéssel; merev transzformációk (eltolás, forgatás, tengelyes tükrözés) **időparaméterrel**; **húzható pont** (fogantyú, ≥ 28 px találati sugár, megkötés pályára) | 09–13 |
| **MatDarab** · átdarabolás | darabonként sokszög + kulcskockák (eltolás, forgatás, tükrözés), zárt képletű áttűnés; a darab színe és területfelirata vele mozog; „szellem” a régi helyen | 01, 05, 08, 09 |
| **MatVenn** · halmazábra | 2–3 halmaz, tartományok kitöltése logikai feltételből, elemek (pöttyök/számok) a tartományukban, tartományonkénti számláló | 02 |
| **MatDiagram** · diagramok | oszlop-, kör-, pont- és vonaldiagram, tengelyfeliratok, hisztogram | 14, 15 |
| **MatVeletlen** · véletlen kísérlet | magolt (`U.rng`) sorozat, a látható állapot a kísérletszámból számolható; számláló, gyakorisági és relatív gyakorisági táblázat | 15 |
| **Közös UI** | kapcsológomb-csoport (pl. alapfüggvény-választó), számkijelző „dobozban” | mind |

**Kockázat:** a két sorozat ugyanazon az éjszakán készül. Ha a 9–10 1. kötegének indulásakor a
Matek 5–6 MatKoord/MatGeo modulja még nincs kész, a 9–10 referencialeckéi **ugyanazzal a
névvel és a fenti minimális API-val** saját változatot írnak leckén belüli blokkban, és a
koordinátor a két sorozat 1. kötege után egyesíti őket (az 5–6-os az alap, a 9–10 bővítései
rákerülnek). Ezért a 9–10 1. kötegét **az 5–6 1. kötege után** érdemes indítani.

### 5.2 Új, 9–10-es modulok

| Modul | Mit tud | Lecke | Első megépítés (referencialecke) |
|---|---|---|---|
| **MatFv** · paraméteres függvényrajzoló | f(x) JS-függvényként vagy `expr` adatból (6. fejezet); adaptív mintavétel szakadással (1/x aszimptotánál megszakad, √x az ÉT határán indul); „szellem” alapgörbe; g(x) = a·f(x + u) + v és |·| paraméterei zárt képletű áttűnéssel; pontpár-nyilak az eredeti és a transzformált görbe között; kiemelt pontok (zérushely, csúcs, metszéspont numerikus gyökkereséssel – felezés), vízszintes egyenes y = c, tengelyszakasz-kiemelés (egyenlőtlenség megoldáshalmaza nyílt/zárt végpontokkal), tükrözés az y = x egyenesre, húzható csúcs/kezdőpont a paraméterekhez kötve, élő képletfelirat (MatKeplet) a paraméterek színével | 06, 07, 08 (+ 13, 14 egyszerű görbéi) | **07-fuggveny-transzformacio** |
| **MatKeplet** · képletszedő a vásznon | a panellel azonos mini-jelölés (6. fejezet) szedése canvasra (`MatKeplet.draw(L, src, x, y, o)` → doboz; `o`: méret, szín, paraméterszínek, `k` md-kulcs): kitevő, index, gyökjel vízszintes vonallal, emeletes tört, abszolútérték, dőlt változók, valódi mínusz, műveleti jelek körüli térköz; részenként színezhető (pl. a paraméter cinóber); visszaadja a dobozt (`{w, h, asc}`), a QA-nak egy egész dobozt jelöl | 05, 06, 07, 08, 09, 11 | **07-fuggveny-transzformacio** |
| **MatSzerk** · szerkesztő-motor | függőségi gráf: szabad (húzható) pontok, belőlük származtatott objektumok lusta újraszámolással: felezőpont, merőleges/párhuzamos adott ponton át, szakaszfelező merőleges, szögfelező, metszéspont (egyenes–egyenes, egyenes–kör, kör–kör), körülírt és beírt kör, magasság talppontja, súlypont, érintő külső pontból; elfajulás-jelzés (egy egyenesbe eső csúcsok → felirat); a szerkesztés **animált** végrehajtása (körzőív, vonalzó-vonal, `prog` 0→1 lépésenként); ponthalmaz-szemléltetés (futópont + két egyenlő szakasz); mért szög és hossz felirata egy közös kerekítéssel; pálya-megkötés (pont körön, egyenesen) | 09, 10, 11, 12, 13 | **10-nevezetes-pontok** |

Leckén belüli, nem általánosított részek: Tennenbaum-négyzetek (01), *MatGraf* fa/körgráf (03,
a 15 átveheti), log-lépték (04), mérleg (06), parketta-kitöltés (12), Galton-deszka (15), oszlop
↔ kör morf (14). Ha egy második lecke is igényli, a koordinátor a referencia mintájára emeli ki.

**A két referencialecke és ami bennük kötelező.**

- **07-fuggveny-transzformacio** → MatFv + MatKeplet. A MatKeplet API-ja és jelöléskészlete
  **pontosan** a build panel-jelölését követi (6. fejezet), hogy egy `.md`-felirat a vásznon
  és a panelen ugyanúgy nézzen ki. A MatFv tesztje: 1/x és √x helyes szakadás/kezdés, a
  „Találd el!” célgörbéje magból.
- **10-nevezetes-pontok** → MatSzerk. Tesztje: a csúcsok szélső húzásainál (tompaszög, közel
  elfajuló háromszög, derékszög) a K, O, S, M számított helye egyezik a rajzzal, és a
  „mérés” feliratai ugyanabból a koordinátából jönnek.

Mindkét modul a szerződés szerinti **külön, jól elhatárolt blokkban** készül
(`/* ── MODUL MatFv ── */ … /* ── MODUL VÉGE ── */`), saját névtérrel, a blokk elején rövid
API-leírással, hogy változtatás nélkül átemelhető legyen a `shared/mat/` alá (javaslat; a
`shared/` módosítása egyeztetendő).

### 5.3 Gyártási sorrend (legfeljebb 3 párhuzamos lecke kötegenként)

| Köteg | Leckék (nehézség) | Új modul | Újrahasznosított |
|---|---|---|---|
| 0 | **Előkészítés** (1 ügynök): build-bővítés (képletjelölés, új adattípusok, szószámlálás), matematikai betűkészlet-kiegészítés, szerződés-kiegészítés beillesztése, öntesztek | – | – |
| 1 | **07-fuggveny-transzformacio** (3), **10-nevezetes-pontok** (3), **01-gyok-ketto** (2) | MatFv, MatKeplet (07) · MatSzerk (10) | MatKoord, MatSzam, MatDarab, MatGeo (5–6) |
| 2 | **08-masodfoku** (2), **06-egyenletrendszer** (2), **09-pitagorasz** (2) | – | MatFv, MatKeplet, MatSzerk, MatDarab |
| 3 | **11-kor-thalesz** (2), **12-egybevagosag-parketta** (3), **13-hasonlosag** (2) | – | MatSzerk, MatGeo, MatKeplet |
| 4 | **02-halmazok-logika** (2), **03-fa-diagram** (2), **04-hatvany-normalalak** (2) | MatGraf (03, leckén belül) | MatVenn, MatSzam |
| 5 | **05-nevezetes-azonossagok** (1), **14-statisztika** (2), **15-valoszinuseg** (2) | – | MatDarab, MatKeplet, MatDiagram, MatVeletlen, MatGraf |

Az 1. köteg a két referencialecke és egy olyan lecke, amely csak az 5–6 készletére és az
új képletjelölésre épül (01): ebből derül ki, hogy a build-bővítés bírja-e a matematikai
szöveget. A 2. kötegben mindhárom lecke az új modulokat veszi át változtatás nélkül – ez a
modulok valódi próbája. A 4–5. köteg leckéi nagyrészt az 5–6 készletére épülnek, ezért
akkor is gyárthatók, ha a 9–10 modulok átnézése csúszik.

---

## 6. Build- és szerződés-kiegészítési igények

A `tools/build_lesson.py` jelenleg ezt tudja: `**félkövér**`, `*dőlt*`, `==kiemelés==`,
`F_fel` alsó index, `{adat}`, `képlet:` blokk (Fraunces dőlt, 44 px). A matematikához ez kevés,
és két ponton **ütközik** is:

- a `*dőlt*` jelölés miatt a `*` nem lehet szorzásjel (az `a*b*c` dőlt „b”-t ad);
- a panel szószámlálója minden betűt és számot külön szónak vesz, így egy
  `x² − 4x + 3 = 0` sor 5–6 „szó”.

A betűkészletek (`shared/lesson.css`) csak a Latin-1, a Latin Extended, az általános
írásjelek, a ⁴ és a − (U+2212) jelet szolgálják ki. **Hiányzik:** ≤ ≥ ≠ ≈ √ ∞ π, a görög betűk
(α β γ φ λ), ∈ ∉ ⊂ ⊆ ∪ ∩ ∅, ℕ ℤ ℚ ℝ, ↦ → ⇒ ⇔, ∢ ∥ ⊥ △ ≅ ∼, ∎, és a ⁰ ⁵–⁹ ⁻ felső indexek. Ezek
most rendszerfontra esnek vissza, amely Windowson és Linuxon más szélességű (ez a CLAUDE.md
tanulsága szerint kilógó szöveghez vezet). A π-hiány már az `iskola` leckéjében is előjött.

### 6.1 Képletjelölés a `.md`-ben (build, `inline()` bővítése)

**Képletszakasz:** `` `…` `` (backtick) – a panelen önálló „képlet” elem lesz (`<span
class="mx">`), és **egy szónak** számít. Csak benne érvényesek az alábbi jelölések; a
backtickek között a `*` és a `_` nem dőlt/index-jelölés, hanem matematika. A `képlet:` blokk
teljes sora ugyanígy képlet.

| a tanár írja | megjelenik | megjegyzés |
|---|---|---|
| `` `x^2` ``, `` `10^-3` ``, `` `2^(n+1)` `` | x², 10⁻³, 2ⁿ⁺¹ (HTML `<sup>`) | hatvány; a zárójel csak csoportosít, nem jelenik meg |
| `` `x_1` ``, `` `D_f` `` | x₁, D_f (`<sub>`) | index (a meglévő szabály) |
| `` `√2` ``, `` `√(x + 1)` ``, `` `gyök(x + 1)` `` | √ felülvonással | `gyök(…)` a billentyűzetbarát alak |
| `` `\|x − 3\|` `` | \|x − 3\| | abszolútérték, változatlan |
| `` `(a + b) / 2` `` | (a + b) / 2 | a panelen ferde törtvonal |
| `képlet: x = (−b ± √(b^2 − 4ac)) / (2a)` | emeletes tört | csak `képlet:` blokkban, ha a számláló és a nevező is zárójeles |
| `` `a*b` `` → `` `a · b` `` | a · b | a `*` szorzáspont lesz |
| `-` | − | képletben a kötőjel mínuszjel |
| `<=` `>=` `!=` `~=` | ≤ ≥ ≠ ≈ | ASCII-rövidítések |
| `->` `\|->` `=>` `<=>` | → ↦ ⇒ ⇔ | függvény: `f: x \|-> 2x + 1` → f: x ↦ 2x + 1 |
| `pi`, `inf` | π, ∞ | csak backtickben (a szövegben a „pi” szó marad) |
| `f(x) = ...` | f(x) = … | a betűváltozók (egyetlen latin betű) dőltek, a számok és a függvénynév álló |

Szabályok és figyelmeztetések:

- A sor elején álló `>` megjegyzésdoboz, ezért **egyenlőtlenség sor elején** nem állhat
  (`x > 3` bekezdés elején → írd `` `x > 3` ``-ként vagy előtte szóval). A build szól, ha egy
  `>`-sor nem `> megjegyzés:`-sel kezdődik.
- Backticken kívüli `^`, valamint `\d\s*\*\s*\d` (szám*szám) → figyelmeztetés („képletet tegyél
  `` ` `` közé”).
- Lezáratlan backtick, páratlan zárójel a képletben → hiba sorszámmal.
- A szószámláló minden képletszakaszt 1 szónak, egy `képlet:` blokkot 3 szónak számol.
- Feliratokban (`### Feliratok`) ugyanez a jelölés használható; a hosszkorlát a **forrás**
  karaktereire vonatkozik. A vásznon a MatKeplet szedi (5. fejezet).
- CSS: `.lp-text .mx` (Fraunces, a változók dőltek, `sup`/`sub` 0,7 em; gyökjel: a gyök alatti
  rész `border-top`), `.big-fx .frac` emeletes törthöz. Ez `shared/lesson.css` módosítás –
  egyeztetendő; ha elutasítják, a meglévő `.fx` stílus (JetBrains Mono, címke) a tartalék.

### 6.2 Új adattípusok (`### Adatok`)

| típus | `.md` alak | JSON | példa leckében |
|---|---|---|---|
| `number` + `"int": true` | `35` | a build hibát ad, ha nem egész | fejek, lábak (06), rétegek száma (04) |
| `point` | `(2; −1,5)` – **pontosvessző** a tizedesvessző miatt | `{t:'point', x:2, y:-1.5, s:'(2; −1,5)'}`; spec: `"box": [xmin, ymin, xmax, ymax]` | csúcsok (10), városok helyett síkpontok |
| `list` | `2; 3; 5; 5; 5` | `{t:'list', v:[2,3,5,5,5], u, d}`; spec: `"len": [min, max]`, `min`/`max` elemenként | jegyek, bérek (14), Galton-utak (15) |
| `frac` | `1/6`, `16 : 9` | `{t:'frac', p:1, q:6, v:0.1667, s:'1/6'}` | valószínűségek (15), képarány (09) |
| `expr` *(opcionális, 2. körtől)* | `x^2 − 4x + 3` | ellenőrzött kifejezésfa (csak x, számok, + − · / ^, √, \|·\|, zárójel), a JS biztonságosan kiértékeli (nincs `eval`) | alapfüggvény (07), példaegyenlet (08) |

A `number` típus egység nélkül is működjön (`"unit": ""`), és a `°` szögegység (már
támogatott) maradjon szóköz nélküli. Egy `point` vagy `list` értékre a `{kulcs}` hivatkozás a
magyar alakot adja.

### 6.3 Betűkészlet

Egy OFL-licencű matematikai betűkészlet részhalmaza (javaslat: **STIX Two Text/Math** vagy
**Noto Sans Math**, csak a fenti hiányzó jelek, várhatóan < 30 KB) `shared/fonts/` alá, és a
`lesson.css`-ben **ugyanazokkal a családnevekkel** (`Fraunces`, `Bricolage Grotesque`,
`JetBrains Mono`) további `@font-face` szabályként, a hiányzó tartományok `unicode-range`-ével
(U+0370–03FF, U+2070–209F, U+2100–214F, U+2190–21FF, U+2200–22FF, U+25B3, U+27FA). Így a
canvas és a panel is automatikusan ezt használja, kódváltozás nélkül, és a felhasználó gépén
sem esik rendszerfontra. A licencszöveg az `OFL.txt` mellé kerül. Ez `shared/` módosítás:
egyeztetendő; a fizika- és a történelemleckék megjelenése a ρ, Δ, λ stb. jeleknél változhat
(QA-val ellenőrizni).

### 6.4 QA-kiegészítés (javaslat)

- **Állapotbeállítás:** az interaktív matek-leckék tegyenek ki egy `window.__lesson.poke({…})`
  függvényt (pl. `{A: [3, 1], a: -2, lab: 95}`), és a `qa_lesson.py` kapjon `--poke '<json>'`
  kapcsolót. Így a szélső állapotok (tompaszög, D < 0, 95 láb) fotózhatók egér-szimuláció
  nélkül.
- **Önellenőrzés:** opcionális `window.__lesson.checks()` → `[{name, ok, got, want}]`, amelyet
  a QA minden lépésnél lefuttat, és `✗`-gel jelez (pl. „K egyenlő távol A-tól, B-től, C-től”,
  „a kiírt c² = a rajzolt négyzet területe”). A matek-leckéknél a számolt és a rajzolt érték
  eltérése a fő hibaforrás.

---

## 7. Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** tanulási eredmény / altéma |
|---|---|---|
| 1. Halmazok (10) | 02 | halmaz megadása utasítással, diszjunkt részhalmazokra bontás (osztályozás) csak érintőlegesen; a végtelen halmazok csak a szálloda-lépésben |
| 2. Matematikai logika (10) | 02, (minden tételes lecke: bizonyítás) | stratégiai és logikai játékok (NIM, „szigetlakók”, Einstein-fejtörő), „bírósági tárgyalás” – tanórai tevékenységek; a bizonyítás *fogalma* csak a sejtés/bizonyítás jelölésen keresztül |
| 3. Kombinatorika, gráfok (12) | 03, (15: útszámlálás) | gráfok önálló alkalmazása (órarend, ismeretségi háló) csak a kézfogás-gráfban; a königsbergi hidak és a fokszám a 11–12. évfolyam fogalma („csúcs fokszáma gráfban”), ezért kimarad |
| 4. Számhalmazok, műveletek (8) | 01 | műveleti azonosságok (kommutativitás, disztributivitás) csak a 05 kifejtésében; intervallumok csak a 06 és a 08 egyenlőtlenségénél; kerekítés, becslés, számológép-használat (gyakorlás) |
| 5. Hatvány, gyök (14) | 04, 01 (négyzetgyök) | **a négyzetgyökvonás azonosságai** (√a · √b = √(ab)); az n-edik gyök és a racionális kitevő (a tanterv a szakasz – 12. évfolyam – végére írja) |
| 6. Betűs kifejezések (10) | 05, 08 (teljes négyzet) | polinomok összevonása, szorzattá alakítás kiemeléssel (rutinszámolás) |
| 7. Arányosság, százalékszámítás (12) | (07: fordított arányosság), (13: arány, méretarány) | **a teljes százalékszámítás** (alap, érték, láb, százalékpont, kamat); mértékegységek átváltása; négyzetes és gyökös arányosság csak a 13 területarányában |
| 8. Elsőfokú egyenletek… (18) | 06 | a szöveges feladattípusok (közös munka, keverés, út–idő) csak egy-egy példával; a behelyettesítő és az egyenlő együtthatók módszere csak egy lépésben, nem begyakorolva |
| 9. Másodfokú egyenletek… (12) | 08 | másodfokúra visszavezethető egyenletek; paraméteres egyenletek; szöveges feladatok (csak a kert) |
| 10. A függvény fogalma (16) | 07, 08, (06: lineáris) | valódi adatsorok grafikonelemzése (demográfia, pénzügy), saját mérés ábrázolása; az egyértelmű / kölcsönösen egyértelmű hozzárendelés hétköznapi példái csak röviden |
| 11. Geometriai alapismeretek (8) | 10 (alapszerkesztések, ponthalmazok), (12: váltószögek) | a térelemek kölcsönös helyzete, távolsága, hajlásszöge (térben); a nevezetes szögpárok önállóan; a szög másolása |
| 12. Háromszögek (16) | 09, 10 | a háromszögek osztályozása; az oldalak és szögek közötti egyenlőtlenségek (háromszög-egyenlőtlenség, nagyobb oldallal szemben nagyobb szög); a középvonal; a területszámítás csak a 09-ben |
| 13. Négyszögek, sokszögek (10) | 12 (szögösszeg, átlók, szabályos sokszög) | **a speciális négyszögek tulajdonságai és területe** (trapéz, deltoid, paralelogramma…); a szabályos sokszög területe átdarabolással |
| 14. A kör és részei (10) | 11 | körszelet területe csak egy mondatban; a kerületi szög tétele nem 9–10. tananyag (a forrás nem említi) |
| 15. Transzformációk, szerkesztések (20) | 12, 13 | **a háromszögek egybevágóságának alapesetei**; vektorok összege; a szerkeszthetőség diszkussziója; merőleges/párhuzamos vetítés és affinitás mint hozzárendelés |
| 16. Leíró statisztika (10) | 14 | adatgyűjtés tervezése és lebonyolítása (tanórai projekt); a szórás és a terjedelem a 11–12. évfolyam fogalma, ezért kimarad |
| 17. Valószínűség-számítás (8) | 15, (03: lottó) | szerencsejátékok összehasonlítása csak a lottóval; a „stratégia esélylatolgatás alapján” tanórai beszélgetés |

**Tartalék-jelöltek** (fontossági sorrendben, a vastagon szedett hiányok miatt):

1. `szazalek-csapdak` – +20 %, majd −20 % ≠ az eredeti (0,96); százalék vs. százalékpont;
   kamatos kamat oszlopokban (7. témakör; MatDiagram, MatKoord).
2. `negyszogek` – a négyszögek „családfája” Venn-diagramként (deltoid, rombusz, paralelogramma,
   téglalap, négyzet), területképletek átdarabolással (13. témakör; MatVenn, MatDarab).
3. `egybevagosag-alapesetek` – mikor határoz meg három adat egy háromszöget? Az „oldal, oldal,
   nem közbezárt szög” kétértelműsége húzható ábrán (15. témakör; MatSzerk).
4. `haromszog-egyenlotlenseg` – három pálcából mikor lesz háromszög? (12. témakör; MatSzerk).
5. `gyok-azonossagok` – √a · √b = √(ab) területtel, és miért nem √(a + b) = √a + √b (5. témakör;
   MatDarab).
6. `grafikon-olvasas` – valódi (KSH) adatsor grafikonja: növekedés, szélsőérték, „mit nem
   mutat a grafikon?” (10. és 16. témakör; MatKoord).

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): **GeoGebra** (a geometria és a
függvénytan szinte minden témájához van kész anyag, a magyar tanárok széles körben használják –
a legnagyobb átfedés); Desmos; PhET (*Graphing Quadratics*, *Plinko Probability*, *Area Model
Algebra*, *Equality Explorer*); a Nemzeti Köznevelési Portál (NKP) 9–10. osztályos digitális
matematikatankönyvei. A mi többletünk a vezetett, lépésenkénti narratíva, a kimondott tévhit,
a sejtés/bizonyítás szétválasztása és a tanár által szerkeszthető szöveg.

---

## 8. Javasolt szerződés-kiegészítés (kész szöveg a `leckek/SZERZODES.md` végére)

> Ha a Matek 5–6 terve már ír „Matematika-kiegészítést”, ez a fejezet annak **folytatása**: a
> közös pontok (képletjelölés, betűkészlet, koordináta-jelölés, állapotkezelés) ott maradnak,
> innen csak a *(9–10)* jelű pontok kerülnek át.

```markdown
## 13. Matematika-kiegészítés (9–10. évfolyam)   <!-- a fejezetszám a Matek 5–6 kiegészítéséhez igazítandó -->

Matematikaleckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:**
`pilot/matematika-9-10/terv.md` 4. fejezet (szerkesztői elvek) és a saját briefed a 3. fejezetben.

- **Mappa, fejléc:** `leckek/matematika-9-10/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Matematika · évfolyam: 9–10. · témakör: N. <a kerettanterv témakörének címe>`.
  Panel: lépésenként ≤ 55 szó (alapérték); egy képletszakasz 1 szónak számít.
- **Képlet a panelen:** képletet mindig `` `…` `` közé vagy `képlet:` sorba írj. Benne:
  `x^2`, `10^-3`, `2^(n+1)` (kitevő), `x_1` (index), `√(x + 1)` vagy `gyök(x + 1)`, `|x|`,
  `a · b` (a `*` is szorzás), `<=` `>=` `!=` `~=` → ≤ ≥ ≠ ≈, `|->` → ↦, `=>` `<=>` → ⇒ ⇔.
  Egyenlőtlenséggel sor nem kezdődhet (a `>` megjegyzésdobozt nyit).
- **Képlet a vásznon:** csak a MatKeplet modullal (`MatKeplet.draw(L, src, x, y, o)`), amely a
  panellel azonos jelölést szed, és a QA-nak egy dobozt jelöl. Unicode felső index (⁵, ⁻) és
  kézzel rakott `L.tx`-darabok helyett is ezt használd.
- **Magyar jelölés:** tizedesvessző; pont koordinátái pontosvesszővel: `A(2; −3)`; intervallum:
  `[a; b]`, `]a; b[`; szorzás `·` (normálalakban is: `3,0 · 10^8`); függvény: `f(x) = 2x + 1`
  vagy `f: x ↦ 2x + 1`; értelmezési tartomány `D_f`, értékkészlet `R_f`; halmazok `ℕ` (a 0-t is
  tartalmazza), `ℤ`, `ℚ`, `ℝ`, `A ∩ B`, `A ∪ B`, `A \ B`, `Ā`; szög `ABC∢` vagy görög betű;
  `e ∥ f`, `e ⊥ f`; derékszögű háromszögben `a`, `b` befogó, `c` átfogó. Közelítő értéknél „≈”,
  sosem „=”. *(9–10)* A nevezetes pontok betűi (körülírt kör középpontja, beírt kör középpontja,
  súlypont, magasságpont) a `### Feliratok` alatt legyenek: tankönyvenként eltérnek.
- **Sejtés és bizonyítás** *(9–10)*: ami csak mér vagy kísérletezik, az a vásznon **„mérés”**
  bélyeget kap (`L.pill`, Bricolage 22 px, 600, halvány tinta `#565d72` keret, −3°); a bizonyító
  lépés címkéje **„bizonyítás”** (cinóber `#c8401c` keret), a végén `∎`. A panel mondja ki, ha
  egy állítást a lecke nem bizonyít. Minden tételt kimondó leckében legalább egy lépés bizonyít.
- **Számok a vásznon:** minden kiírt szám (hossz, szög, terület, koordináta, valószínűség)
  **ugyanabból a koordinátából vagy modellből** számolódik, amelyet a rajz használ; a
  kerekítés egyetlen közös függvényen megy át (`U.fmt`, legfeljebb 2 tizedes, szög 1 tizedes);
  kerekített értéknél „≈”. Egész rácspontokra „pattintás” csak ott, ahol a brief kéri.
- **Húzható pont:** látható fogantyú (kitöltött kör + gyűrű, ≥ 28 px találati sugár), húzás
  közben a pont neve és koordinátája; pályára kötött pont (körön, egyenesen) nem hagyhatja el
  a pályát. Elfajuló helyzetben (egy egyenesbe eső csúcsok, nullához közeli oldal) a származtatott
  objektumok halványulnak, és egy `.md`-felirat jelzi („a három pont egy egyenesen van”).
  Minden húzható elem csúszkával vagy gombbal is elérhető állapotba vihető (kivetítésnél a
  tanár gyakran billentyűzettel léptet).
- **Grafikonstílus:** tengely tinta 2,5 px nyíllal, rács `rgba(28,36,64,.08)`, osztásszámok
  JetBrains Mono ≥ 22 px valódi mínusszal; a fő görbe 4 px cinóber, a második kékeszöld, az
  alapgörbe („szellem”) szaggatott halvány tinta; a görbe a rajzterületre vágva, szakadásnál
  megszakítva (nem „függőleges vonal” az aszimptotánál). Nyílt végpont: üres karika, zárt: teli.
- **Véletlen:** csak `U.rng(mag)`; a látható állapot (dobások száma, golyók helye) a
  lépésindexből, `L.st`-ből és a gombnyomások számából zárt képlettel számolható, így
  visszaléptetve és a QA-ban is ugyanaz.
- **Kitalált és valódi adat** *(9–10)*: kitalált szöveges adat (tarifák, bérek) „kitalált adat”
  bélyeget kap; valódi adat (méret, távolság, statisztika) forrással és dátummal a `.md`
  `<!-- -->` megjegyzésében.
- **Új adattípusok:** `point` `(2; −1,5)`, `list` `2; 3; 5; 5; 5`, `frac` `1/6`, `"int": true`
  (részletek: `tools/build_lesson.py` fejléce).
- **Modulok:** a közös `Mat…` modulokat (5–6 készlet + `MatFv`, `MatKeplet`, `MatSzerk`) a
  referencialeckékből **változtatás nélkül** emeld át a saját `<script>`-edbe, jól elhatárolt
  blokkban. Ha hibát találsz bennük, a javítást jelezd a jelentésedben (a koordinátor viszi
  vissza a referenciába), ne írj párhuzamos változatot.
- **Minden `.md`** végén `<!-- Matematikai ellenőrzés: … -->` blokk: a leckében szereplő
  számpéldák és tételek listája, és hogy mivel ellenőrizted (pl. „Python, 2026-11-23”); a
  történeti állításoknál a forrás és a bizonyosság foka („a hagyomány szerint”).
```
