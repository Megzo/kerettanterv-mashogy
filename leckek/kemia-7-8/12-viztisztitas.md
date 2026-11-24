# Tiszta-e, ami átlátszó? – természetes vizek és víztisztítás
tantárgy: Kémia · évfolyam: 7–8. · témakör: 5. Kémia a természetben

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/kemia-7-8/12-viztisztitas.md

  A lecke a 02-szetvalasztas elválasztási műveleteire (ülepítés, szűrés, bepárlás) épít, és
  a 13-szappan-vizkemenyseg előtt áll. A budapesti adatok (Fővárosi Vízművek) helyi adatok:
  más településen a saját vízszolgáltató honlapján találod a csapvíz adatait, és átírhatod
  őket (a „csapvíz bepárlási maradéka” és a „nitrát a csapvízben” sor a vásznat is vezérli).
-->

## Közös

### Feliratok
- nagyítás: nagyítás · szemléltetés
- modell: modell
- szemléltetés: szemléltetés
- gyorsítva: gyorsítva
- ne próbáld: NE PRÓBÁLD KI
- vízmolekula: vízmolekula
- ion: oldott ion
- baktérium: baktérium
- nitrátion: NO₃⁻ nitrátion
- agyagszemcse: agyagszemcse
- újra gomb: Újra

## 1. Mennyi iható víz van a Földön?
Ha a Föld összes vize **100 liter** lenne, ebből kb. {sós víz literben} sós. Az édesvíz kb. {édesvíz literben}, és ennek nagy része jég vagy mélyen fekvő felszín alatti víz.

==A tavak és a folyók édesvize alig 7 ml== – egy kémcsőnyi. Ezt a kevés vizet használjuk újra meg újra.

> megjegyzés: Húzd a csúszkát, és nagyíts bele!

### Feliratok
- kérdés 1: Ha a Föld összes vize 100 liter lenne…
- tartály: a Föld összes vize
- sós: sós víz
- édes: édesvíz
- jég: jég, hó
- talajvíz: felszín alatti édesvíz
- egyéb: egyéb (pára, élőlények…)
- tavak folyók: tavak, folyók
- liter: # l
- milliliter: # ml
- nagyítás csúszka: nagyítás
- n0: minden víz
- n1: csak az édesvíz
- n2: tavak és folyók
- kémcső: egy kémcsőnyi
- forrás víz: Forrás: USGS (Shiklomanov, 1993)

### Adatok
<!-- forrás (az alábbiakra): USGS Water Science School, „Where is Earth's Water?” (Shiklomanov, 1993,
     in: Gleick (szerk.): Water in Crisis), lekérdezve: 2026-11-24 – ugyanaz a táblázat, mint a földrajz
     9–10. „06-felszin-alatti-viz” leckében. A literértékeket a lecke számolja (térfogat / összes × 100 l). -->
- Föld vízkészlete: 1 386 000 000 km³
- sós víz: 1 350 955 400 km³
<!-- óceánok 1 338 000 000 + sós felszín alatti víz 12 870 000 + sós tavak 85 400 km³ = 97,47 % -->
- jég és állandó hó: 24 064 000 km³
- felszín alatti édesvíz: 10 530 000 km³
- tavak és folyók édesvize: 93 120 km³
<!-- édesvizű tavak 91 000 + folyók 2120 km³. Az „egyéb” (talajnedvesség, fagyott talaj, légköri pára,
     mocsarak, élőlények) a maradék: kb. 342 000 km³ ≈ 25 ml a 100 literből. -->
- sós víz literben: 97,5 l
- édesvíz literben: 2,5 l

## 2. Átlátszó = tiszta?
Négy pohár, négy átlátszó víz. Mégsem egyformák: ==a feloldott anyag nem látszik==, a víz mégsem tiszta.

**Bepárlással** kiderül: a desztillált víz után nem marad semmi, a csapvíz után kevés, a tengervíz után sok só.

> megjegyzés: Húzd a csúszkát! A tengervíz forralva sem iható: a só ott marad, sőt töményebb lesz.

### Feliratok
- kérdés 2: Mi marad, ha elpárologtatjuk a vizet?
- minta 0: desztillált víz
- minta 1: csapvíz (Budapest)
- minta 2: ásványvíz
- minta 3: tengervíz
- bepárlás csúszka: elpárolgott víz
- maradék: maradék: #
- egy liter: 1 l vizet párolunk be
- semmi: nem marad semmi
- ionok túlzás: az ionok száma erősen túlzott
- tévhit átlátszó: Ami átlátszó, az tiszta.
- helyes átlátszó: Nem: az oldott anyag nem látszik.

### Adatok
- desztillált víz maradéka: 0 mg/l
- csapvíz bepárlási maradéka: 250 mg/l
<!-- forrás: Fővárosi Vízművek, „A Fővárosi Vízművek által szolgáltatott ivóvíz minősége” – összes oldott
     ásványi anyag (TDS): 2019: 248, 2020: 245, 2021: 275 mg/l (a 2023-as táblázatban „n.a.”); lekérdezve:
     2026-11-24 (vizmuvek.hu, vizminoseg-2023.pdf). A lecke kerekítve 250 mg/l-t használ. -->
- ásványvíz ásványianyag-tartalma: 800 mg/l
<!-- példa: a palackos ásványvizek ásványianyag-tartalma a címkén szerepel, néhány tíz mg/l-től több ezer
     mg/l-ig. A 65/2004. (IV. 27.) FVM–GKM–ESzCsM rendelet szerint „csekély ásványianyag-tartalmú” ≤ 500 mg/l,
     „ásványi anyagban gazdag” > 1500 mg/l. Írd át a saját palackod címkéje szerint! -->
- tengervíz sótartalma: 35 g/kg
<!-- közismert átlag (óceánok, kb. 3,5 %). A leckében 1 l ≈ 1 kg (a tengervíz sűrűsége kb. 1,025 g/cm³,
     ezt a lecke elhanyagolja). -->
- konyhasó oldhatósága: 35,9 g/100 g víz
<!-- 20 °C, CRC Handbook (mint a 02-szetvalasztas és a 04-oldodas leckében); a lecke ezzel számolja,
     mikor kezd kiválni a só a bepárlócsészében (egyszerűsítés: minden oldott anyagot konyhasóként kezel). -->

## 3. Folyóvízből ivóvíz: rács, ülepítés, derítés
A folyóvízből a **rács** kiszedi az ágakat, az **ülepítőben** leül a homok. Az agyagszemcsék viszont hetekig lebegnének.

Ezért **derítőszert** adunk a vízhez: ==pelyhek képződnek, amelyek összegyűjtik a szemcséket==, és gyorsan leülepednek.

> megjegyzés: Nyomd meg a gombot, és figyeld a nagyítót!

### Feliratok
- kérdés 3: Hogyan ülepíthető le, ami nem akar leülepedni?
- folyó: folyó
- rács: rács
- ülepítő: ülepítő
- derítő: derítő
- homokszűrő: homokszűrő
- fertőtlenítés: fertőtlenítés
- tároló: tároló
- derítőszer gomb: Derítőszer!
- derítőszer: derítőszer
- pehely: pehely
- süllyedés cím: 1 m süllyedés ideje
- homokszem: homokszem (0,2 mm)
- agyag sáv: agyagszemcse (1 µm)
- pehely sáv: pehely (1 mm)
- eltelt: eltelt: #
- célba ért: # alatt leért
- még: kb. # kellene
- perc: # perc
- óra: # óra
- hét: # hét
- sebesség forrás: Stokes-törvény alapján, kerekítve

### Adatok
- homokszem süllyedése: 2 cm/s
- agyagszemcse süllyedése: 3 mm/óra
- pehely süllyedése: 1,5 m/óra
<!-- Süllyedési sebességek vízben, 20 °C-on, a Stokes-törvény szerint (v = 2/9 · Δρ · g · r² / η, η = 1,0 mPa·s,
     Δρ = 1,65 g/cm³ a kvarcra és az agyagásványra): 0,2 mm-es homokszem ≈ 3,6 cm/s (a Stokes-törvény itt már
     kissé túlbecsül; mért érték kb. 2–3 cm/s), 1 µm-es agyagszemcse ≈ 0,9 µm/s ≈ 3,2 mm/óra → 1 m kb. 13 nap
     (kb. 2 hét). A pehely laza, sok vizet tartalmaz (Δρ kicsi), süllyedése a víztisztítási gyakorlatban kb.
     1–2 m/óra (az ülepítők méretezési „felületi terhelése” ehhez igazodik) – ellenőrizendő szakkönyvben.
     Derítőszer: alumínium-szulfát, vas(III)-klorid vagy polialumínium-klorid; a lecke nem nevezi meg. -->

## 4. Parti szűrés: a Duna kavicsa szűr
Budapest ivóvize ==szinte teljes egészében parti szűrésű kutakból jön==. A kutak a Duna partján és szigetein állnak; a folyó vize a **kavicsrétegen** át jut beléjük.

A kavicsszemek felületén élő baktériumok és a szűk járatok visszatartják a szemcséket és a kórokozókat. Az oldott ionok átjutnak.

> megjegyzés: Húzd a csúszkát: kövesd a víz útját!

### Feliratok
- kérdés 4: Mit szűr ki a kavics a Duna vizéből?
- duna: Duna
- sziget: sziget
- kavics: homokos kavics (víztartó)
- agyag réteg: agyag (vízzáró)
- csápos kút: csápos kút
- csáp: csáp: lyukacsos cső
- szivattyú: a vízműbe
- útvonal csúszka: a víz útja
- út: # m a mederből
- mederben: a mederben
- kútban: a kútban
- lebegő: lebegő szemcsék
- baktériumok sáv: baktériumok
- ionok sáv: oldott ionok
- marad: # % marad
- biofilm: baktériumréteg a kavicson
- adatkártya cím: Budapest vízbázisa
- kutak: kb. # kút, ebből kb. # csápos kút
- termelés: naponta # ivóvíz
- csáp hossz: csápok: #
- akna sor: akna: # mélyen
- torzítás: függőleges torzítás #×
- méretarányos: méretarányos
- mélység: mélység (m)

### Adatok
- kutak száma: 756
<!-- forrás: Fővárosi Vízművek Zrt., Üzleti tájékoztató 2023 (vizmuvek.hu): 756 víztermelő kút a Szentendrei-
     szigeten, a Csepel-szigeten és a Duna bal partján; lekérdezve: 2026-11-24. -->
- csápos kutak száma: 150
<!-- forrás: Fővárosi Vízművek / DUNA-KÚT Kft.: „Víztermelés a parti szűrés kihasználásával” (Duna-kút
     kiadvány, vizmuvek.hu): „Budapest vízellátása 100%-osan parti szűrésre épül, melynek alapját … mintegy 150
     csáposkút jelenti.” A többi kút cső- és aknakút. -->
- napi termelés: 450–650 ezer m³
<!-- forrás: ugyanott: „napi 450 000–650 000 m3 jó minőségű ivóvíz”. Ellenőrzés: 2023-ban 162 185 000 m³/év
     ≈ 444 000 m³/nap (Üzleti tájékoztató 2023). -->
- akna mélysége: 12–20 m
- csápok hossza: 30–60 m
<!-- forrás: ugyanott: a 2200 mm átmérőjű aknát a vízzáró rétegig süllyesztik, „Budapest viszonylatában
     12–20 méter mélységben”; a csápok 219 mm átmérőjű, perforált csövek, hosszuk 30–60 m. -->
- biológiailag aktív réteg: 3 m
<!-- forrás: ugyanott: „A biológiailag aktív réteg … vastagsága a medernél történő belépéstől számítva csupán
     néhány méter.” A lecke modellje: a baktériumok és a lebegő szemcsék a mederből számított úttal exponenciálisan
     fogynak (felezési út ≈ 0,7 × ez az érték); ez szemléltető modell, nem mérés. -->

## 5. Fertőtlenítés – és ami mégis átjut
A szűrt vízbe kevés **klórt** adnak: ez elpusztítja a maradék kórokozókat a csövekben is.

A **nitrát** (például a trágyából) viszont feloldott ion: ==átjut minden szűrőn==, a klór sem bontja el. A forralás a baktériumokat megöli, de a nitrátot nem – sőt töményebb lesz.

> megjegyzés: Nyomd meg a trágyázás gombot!

### Feliratok
- kérdés 5: Mi jut át a szűrőn, a klóron és a forraláson?
- s talaj: talajvíz
- s szűrő: homokszűrő
- s klór: klórozás
- s forralás: forralás (otthon)
- s pohár: pohár
- trágya gomb: Trágyázás!
- trágya: trágya
- tiszta gomb: Trágya nélkül
- nitrát sor: nitrát (mg/l)
- baktérium sor: szürke, törött: elpusztult
- határérték: határérték: #
- hypo: nátrium-hipoklorit
- hypo jelek: maró · környezetre veszélyes
- hypo tanács: Hypót ne tegyél ivóvízbe!
- csepp csúszka: a csepp helye
- tévhit forralás: A forralás minden szennyezést eltávolít.
- helyes forralás: Nem: a nitrát marad, sőt töményebb lesz.
- túl sok: határérték fölött!

### Adatok
- nitrát a csapvízben: 8 mg/l
<!-- forrás: Fővárosi Vízművek, ivóvízminőség 2023 – évi átlag, Budapest: nitrát 8 mg/l (2019–2022: 8,8; 8,7;
     9,6; 9 mg/l); lekérdezve: 2026-11-24. -->
- nitrát határértéke: 50 mg/l
<!-- forrás: 5/2023. (I. 12.) Korm. rendelet (ivóvíz), az (EU) 2020/2184 irányelvvel egyezően; a Fővárosi
     Vízművek táblázata is ezt közli. A nitrát elsősorban a csecsemőkre veszélyes (methemoglobinémia). -->
- nitrát a trágyázott föld alatt: 80 mg/l
<!-- példa (kitalált, de reális nagyságrend): sekély, ásott kutak vize trágyázott területen gyakran a
     határérték fölött van. A forralás a nitrátot nem távolítja el, mert a nitrát nem illékony – a víz
     párolog el, ezért a nitrát töményebb lesz (pl. Minnesota Department of Health: „Nitrate in Well Water”).
     A lecke a forralásnál a víz felének elpárolgásával számol (szemléltetés: a valóságban kevesebb párolog el). -->
- elpárolgó hányad: 50 %

## 6. A szennyvíz útja: a tisztítótelep
A lefolyóba öntött víz nem tűnik el: csatornán a **szennyvíztisztító telepre** jut. Ott ugyanazok a műveletek dolgoznak, mint a laborban: rács, ülepítés – és ==baktériumok, amelyek megeszik az oldott szennyezést==.

Állítsd sorba a lépéseket!

> megjegyzés: Kattints a kártyákra! A víz a sorrendedben folyik végig.

### Feliratok
- kérdés 6: Milyen sorrendben tisztítsuk a szennyvizet?
- k rács: rács
- k homokfogó: homokfogó
- k előülepítő: előülepítő
- k eleveniszap: eleveniszap
- k utóülepítő: utóülepítő
- csatorna: csatornából
- vissza duna: a Dunába
- m rács: rongy, műanyag, ág
- m homokfogó: homok, kavics
- m előülepítő: leülepedő iszap
- m eleveniszap: oldott szerves anyag
- m utóülepítő: baktériumpelyhek
- v jó: Jó sorrend: tiszta víz megy a Dunába!
- v rács: A rongy eltömi a szivattyúkat – a rács legyen elöl!
- v homok: A homok az iszapba kerül, és koptatja a gépeket.
- v elő: Ami leülepíthető, előbb ülepítsd le!
- v utó: A baktériumpelyhek a Dunába kerülnének!
- kártyák: Kattints a kártyákra a sorrendhez!
- jó gomb: Mutasd a jó sorrendet!
- ürítés gomb: Ürítés
- telep cím: Budapesti Központi Szennyvíztisztító Telep
- telep adat: Csepel-sziget, # óta · naponta átlagosan # m³
- tévhit eltűnik: A szennyvíz eltűnik a csatornában.
- helyes eltűnik: Nem: a tisztítótelepen át a folyóba jut.

### Adatok
- központi telep átadása: 2010
<!-- forrás: a telep próbaüzeme 2009 augusztusában indult, üzemszerű működése 2010 augusztusában kezdődött
     (ICPDR: „The living Danube in Budapest”; hvg.hu, 2011. 11. 25.); lekérdezve: 2026-11-24. -->
- központi telep napi szennyvize: 350 000 m³
<!-- forrás: Európai Beruházási Bank, projekt 20010343 („a capacity of 350.000 m3/day”); ICPDR: átlagosan
     350 000 m³/nap. A tervezett csúcskapacitás ennél nagyobb (esős időben). Az Észak-pesti és a Dél-pesti telep
     együtt további kb. 235 ezer m³/nap (Fővárosi Csatornázási Művek, fcsm.hu). -->

## 7. Eleveniszap: baktériumok tisztítanak
Az **eleveniszapos medencében** baktériumpelyhek úsznak. ==Az oldott szerves anyagot oxigénnel lebontják== szén-dioxiddá és vízzé, mint a sejtlégzésben.

Ehhez **levegőt fújunk** a vízbe.

> megjegyzés: Húzd a levegőztetés csúszkáját!

### Feliratok
- kérdés 7: Ki bontja le, amit a szűrő nem fog meg?
- levegőztetés csúszka: levegőztetés
- szerves anyag: oldott szerves anyag
- oxigén: oxigén
- szén-dioxid: szén-dioxid
- baktériumpehely: baktériumpehely
- lebontás szóegyenlet: szerves anyag + oxigén → szén-dioxid + víz
- grafikon y: szerves anyag (mg/l)
- grafikon x: idő (óra)
- befolyó: befolyó: #
- kifolyó határ: kifolyó, határérték: #
- most: most: # mg/l
- levegő nélkül: levegő nélkül alig bomlik
- gyorsítva óra: 1 s ≈ 1 óra

### Adatok
- befolyó szerves anyag: 250 mg/l
<!-- A szerves anyag mértéke a biokémiai oxigénigény (BOI₅, mg/l O₂). Települési szennyvízben jellemzően kb.
     200–300 mg/l (pl. 60 g BOI₅ / fő / nap, kb. 200–300 l szennyvízzel). Tankönyvi nagyságrend; ellenőrizendő. -->
- kifolyó határérték: 25 mg/l
<!-- forrás: 91/271/EGK irányelv (települési szennyvíz), 1. melléklet, 1. táblázat: BOI₅ legfeljebb 25 mg/l O₂
     (az új, (EU) 2024/3019 irányelv ugyanezt az értéket tartja meg). A „mg/l” itt mg O₂/l. -->
- tartózkodási idő: 6 óra
<!-- modell: az eleveniszapos medencében a víz jellemzően kb. 4–12 órát tölt (tankönyvi nagyságrend). A lecke
     modellje: teljes levegőztetésnél a szerves anyag exponenciálisan fogy, és ennyi idő alatt éri el a
     határértéket (250 → 25 mg/l); levegő nélkül a sebesség kb. 5 %-a. Szemléltető modell, nem mérés. -->

## 8. Összefoglalás: egy vízcsepp útja
A csapvíz a Dunából indul, és oda tér vissza. Útközben ==minden lépés egy különbséget használ ki==: méretet, sűrűséget, és ahol ez kevés, kémiát (derítés, klór) vagy élőlényeket (baktériumok).

Egy ember naponta kb. {napi vízhasználat} vizet használ itthon – minden litert meg kell tisztítani.

> megjegyzés: Kattints az állomásokra!

### Feliratok
- kérdés 8: Honnan jön, és hová megy a csapvíz?
- á duna: Duna
- á parti: parti szűrés
- á klór: fertőtlenítés
- á csap: csap, háztartás
- á csatorna: csatorna
- á telep: szennyvíztisztító
- é duna: a víz forrása és befogadója
- é parti: méret + baktériumok a kavicson
- é klór: kémia: elpusztítja a kórokozókat
- é csap: kb. # / fő / nap
- é csatorna: a szennyvíz nem tűnik el
- é telep: méret, sűrűség, baktériumok
- á kattints: Kattints egy állomásra!
- körforgás: körforgás

### Adatok
- napi vízhasználat: 93 l
<!-- forrás: KSH, „A víz világnapja” infografika (2018. március 22., 2016-os adatok): az egy főre jutó éves
     ivóvízfogyasztás 34 m³ → 34 000 l / 365 ≈ 93 l/nap; lekérdezve: 2026-11-24. Frissítendő. -->

<!-- Modell-egyszerűsítések és források:
  - A részecskék (vízmolekula, ion, baktérium, agyagszemcse) mérete és száma nem arányos. A csapvíz
    nagyítójában az ionok száma erősen túlzott (valójában kb. 6000–7000 vízmolekulára jut egy ion, lásd a
    03-elem-vegyulet-keverek leckét); az arányok sorrendje (desztillált < csapvíz < ásványvíz < tengervíz)
    helyes.
  - 2. lépés: a bepárlás 1 kg vizet párol el; a kiváló anyagot a lecke konyhasóként kezeli (oldhatóság
    35,9 g/100 g víz); a maradék kupacának területe a tömeggel arányos.
  - 3. lépés: a süllyedési időket a lecke az adatokból számolja (1 m / sebesség); a nagyító pehelyképződése
    szemléltetés (a valóságban gyors keverés, majd lassú keverés, összesen kb. fél óra). A vízmű sémája
    egy felszíni (folyó- vagy tó-) vizes vízmű általános lépéseit mutatja; Budapest nem ilyen, hanem parti
    szűrésű (4. lépés). Felszíni vizet tisztító vízmű Magyarországon is van – ellenőrizendő, melyiket érdemes
    példaként megnevezni.
  - 4. lépés: a metszet vázlatos (rétegvastagság a forrás tartományai szerint: kavics a meder alatt, agyag
    kb. 17 m mélyen, akna a vízzáró rétegig, csápok kb. 45 m); a fennakadás modellje exponenciális (biológiailag
    aktív réteg néhány méter). A kavics a valóságban rétegzett és változó szemcséjű; egyes helyeken a parti
    szűrésű vizet további kezelésnek (pl. vas- és mangántalanítás) is alávetik – ellenőrizendő.
  - 5. lépés: a fertőtlenítés klórral történik (Fővárosi Vízművek: „a legbiztonságosabb és leghatásosabb
    fertőtlenítési eljárás a klórozás”, árvíz/aszály idején UV is); a vegyszer pontos fajtáját (klórgáz,
    nátrium-hipoklorit, klór-dioxid) a lecke nem állítja – a hipoklorit-tartály szemléltetés. A nátrium-hipoklorit
    GHS-jelei (GHS05, GHS09) a harmonizált besorolás szerint; háztartási termékeknél eltérhet. A 80 mg/l-es
    nitrát kitalált példa. A forralásnál a víz fele párolog el (szemléltetés). Az állomások nagyítójában
    kb. 8 mg/l nitrát = 1 ion, a baktériumok száma szemléltető (talajvíz → szűrő → klór: 6 → 1 → 0).
  - 6. lépés: a tisztítótelep sora egy általános, mechanikai + biológiai (eleveniszapos) telep; a valódi
    telepeken zsírfogó, kémiai foszforeltávolítás és iszapkezelés (rothasztás, biogáz) is van (fcsm.hu). A
    Budapesti Központi Szennyvíztisztító biológiai fokozata a szakirodalom szerint biofilmes szűrőkkel működik
    (nem klasszikus eleveniszappal) – ellenőrizendő; a lecke ezért az általános sort mutatja, a telepet csak a
    méret (napi 350 000 m³) példájaként említi.
  - 7. lépés: a szerves anyag fogyása exponenciális modell (sebesség ∝ levegőztetés, kis alapértékkel); a
    baktériumok szaporodását és az iszap visszavezetését a modell nem követi. Az idő gyorsítva (1 s ≈ 1 óra).
  - 8. lépés: a napi vízhasználat országos átlag (KSH, 2016); Budapesten nagyobb.
  - Források: USGS Water Science School; Fővárosi Vízművek (vízminőség 2019–2023, Üzleti tájékoztató 2023,
    Duna-kút kiadvány); 5/2023. (I. 12.) Korm. rendelet; 91/271/EGK irányelv; 65/2004. (IV. 27.) együttes
    rendelet; EIB 20010343; ICPDR; fcsm.hu; KSH 2018; CRC Handbook.
-->
