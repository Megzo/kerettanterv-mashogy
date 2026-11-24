# Gazdagabb = egészségesebb? – a fejlettség mérése, centrum és periféria
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 7. A nemzetgazdaságtól a globális világgazdaságig

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/11-fejlettseg.md
  Az országok mutatói (GDP, GNI, várható élettartam, népesség, foglalkoztatás) a
  shared/foldrajz/fejlettseg-wdi.js adatfájlból jönnek (Világbank WDI), a térkép a
  shared/foldrajz/orszagok.js-ből (Natural Earth). Az alábbi számok azok, amelyeket a panel kimond
  vagy a vászon kiemel; a lecke ellenőrzi, hogy egyeznek-e az adatfájllal (eltérésnél a QA hibát jelez).
  Az országnevek a vásznon az adatfájl magyar nevei; a kiemelt országok nevei itt, a Feliratok alatt.
-->

## Közös

### Feliratok
- modell: modell
- becslés: becslés
- log. skála: log. skála
- Kína: Kína
- Svájc: Svájc
- India: India
- Nigéria: Nigéria
- Magyarország: Magyarország
- Dél-Korea: Dél-Korea
- Írország: Írország
- Luxemburg: Luxemburg
- Lengyelország: Lengyelország
- Németország: Németország
- Egyesült Államok: Egyesült Államok
- Japán: Japán
- Brazília: Brazília
- r EAS: Kelet-Ázsia és Óceánia
- r SAS: Dél-Ázsia
- r SSF: Szubszaharai Afrika
- r MEA: Közel-Kelet és Észak-Afrika
- r ECS: Európa és Közép-Ázsia
- r LCN: Latin-Amerika
- r NAC: Észak-Amerika
- csúszka év: Év
- gomb lejátszás: Lejátszás
- x bub: egy főre jutó GDP vásárlóerőn ($, 2021-es árakon)
- y bub: várható élettartam (év)
- méret: buborék területe ~ népesség

### Adatok
<!-- forrás (az alábbiakra): World Bank, World Development Indicators (data.worldbank.org, API v2, frissítve: 2026-11-11), shared/foldrajz/fejlettseg-wdi.js, lekérdezve: 2026-11-23, CC BY 4.0 – a forrás megjelölése kötelező (a vásznon a forrássorban). A foglalkoztatási adatok az ILO modellbecslései. Térkép: Natural Earth 1:110m (közkincs, „Made with Natural Earth”), shared/foldrajz/orszagok.js. -->
- WDI adatkészlet: Világbank WDI, 2026
- országhatárok: Natural Earth
- első adatév: 1990
<!-- forrás: a WDI vásárlóerő-paritásos GDP/fő idősora (NY.GDP.PCAP.PP.KD) 1990-ben kezdődik -->
- utolsó adatév: 2024
<!-- forrás: a várható élettartam (SP.DYN.LE00.IN) utolsó adatéve a letöltéskor (2024) -->

## 1. Mit mér a GDP?
A **GDP** (bruttó hazai termék) az egy év alatt az országban előállított termékek és szolgáltatások értéke. **Tévhit:** a nagyobb GDP-jű ország a gazdagabb. Kína GDP-je {Kína GDP-je}, Svájcé {Svájc GDP-je}. ==Elosztva a népességgel== viszont Svájcban {Svájc egy főre jutó GDP-je} jut egy lakosra, Kínában {Kína egy főre jutó GDP-je}.

> megjegyzés: Kapcsolj: összesen vagy egy főre?

### Feliratok
- cím 1: Kína vagy Svájc: melyik a gazdagabb?
- gomb összesen: Összesen
- gomb egy főre: Egy főre
- fej összesen: GDP összesen, folyó áron
- fej egy főre: egy főre jutó GDP, folyó áron
- érték összesen: # billió $
- érték egy főre: # $ / fő
- osztás: ÷ # lakos
- szorzó: #-szer akkora
- jel terület: a négyzet területe arányos az értékkel
- forrás 1: Forrás: Világbank, WDI (GDP, folyó áras USD), 2024

### Adatok
<!-- forrás (az alábbiakra): Világbank WDI (NY.GDP.PCAP.CD, SP.POP.TOTL), 2024, lekérdezve: 2026-11-23, CC BY 4.0; az ország GDP-je = egy főre jutó GDP × népesség (saját számítás) -->
- Kína GDP-je: 18,7 billió dollár (2024, frissítendő)
- Svájc GDP-je: 0,97 billió dollár (2024, frissítendő)
- Kína egy főre jutó GDP-je: 13 293 dollár (2024, frissítendő)
- Svájc egy főre jutó GDP-je: 107 702 dollár (2024, frissítendő)
- Kína népessége: 1,41 milliárd fő (2024, frissítendő)
- Svájc népessége: 9,0 millió fő (2024, frissítendő)

## 2. GDP vagy GNI?
**Tévhit:** a GDP a lakók jövedelme. A GDP azt méri, mennyit termelnek **az országban**. A **GNI** (bruttó nemzeti jövedelem) azt, mennyi jövedelem jut **az ország lakóinak**. Egy külföldi tulajdonú gyár hazautalt nyeresége a GDP-ben benne van, a GNI-ben nem. ==Írországban a GNI a GDP-nek csak {Írország GNI-je}-a==, Magyarországon {Magyarország GNI-je}-a.

> megjegyzés: Válassz országot!

### Feliratok
- cím 2: Hol termelnek – kié a jövedelem?
- ország: az ország
- külföld: külföld
- gyár: külföldi tulajdonú gyár
- bérek: bérek, hazai tulajdonosok
- anyavállalat: anyavállalat
- nyereség: hazautalt nyereség
- befelé: hazahozott jövedelem
- GDP: GDP
- GNI: GNI
- cím 2b: A GNI a GDP %-ában, #
- tengely 2: a GDP = 100 %
- kevesebb: ← kevesebb marad
- több: több jön be →
- forrás 2: Forrás: Világbank, WDI (GDP és GNI/fő vásárlóerőn, mindkettő 2021-es áron), 2021

### Adatok
<!-- forrás (az alábbiakra): Világbank WDI, NY.GNP.PCAP.PP.CD és NY.GDP.PCAP.PP.KD, 2021 – ebben az évben a kettő ugyanabban a mértékegységben (2021-es nemzetközi dollár) van, ezért a hányadosuk a GNI/GDP arány; saját számítás, lekérdezve: 2026-11-23, CC BY 4.0. A brief „4–6 %”-os magyar eltérése más évekre vonatkozhat; 2021-ben 2,9 %. -->
- GNI-GDP év: 2021
- Írország GNI-je: 71 % (2021)
- Magyarország GNI-je: 97 % (2021)

## 3. Egy főre és vásárlóerőn
Egy dollárért nem mindenhol ugyanannyit kapsz: ==Indiában ugyanaz a kosár az amerikai ár kb. {India árszintje}-ába kerül==, Magyarországon {Magyarország árszintje}-ába. Ezért **vásárlóerő-paritáson** (PPP) is számolunk: így Indiában egy főre {India GDP/fő folyó áron} helyett {India GDP/fő vásárlóerőn} jut.

> megjegyzés: A PPP-szorzó becslés: a Nemzetközi Összehasonlító Program (ICP) árfelméréséből.

### Feliratok
- cím 3: Mennyit ér egy dollár?
- kosár: Ugyanaz a kosár ára
- kosár x: USA = 100
- folyó áron: folyó áron (USD)
- vásárlóerőn: vásárlóerőn (PPP)
- gomb folyó áron: Folyó áron
- gomb vásárlóerőn: Vásárlóerőn
- x 3: egy főre jutó GDP ($ / fő), 2021
- forrás 3: Forrás: Világbank, WDI (GDP/fő folyó USD-ben és PPP-n), 2021 · árszint = folyó áras / PPP

### Adatok
<!-- forrás (az alábbiakra): Világbank WDI, NY.GDP.PCAP.CD (folyó USD) és NY.GDP.PCAP.PP.KD (2021-es nemzetközi dollár), 2021; az árszint a kettő hányadosa (az USA-ban 100 %), saját számítás, lekérdezve: 2026-11-23, CC BY 4.0 -->
- árszint év: 2021
- India árszintje: 29 % (2021)
- Magyarország árszintje: 49 % (2021)
- India GDP/fő folyó áron: 2240 dollár (2021)
- India GDP/fő vásárlóerőn: 7819 dollár (2021)

## 4. Tévhit: a lineáris tengely csal
Minden buborék egy ország. **Lineáris** tengelyen az egyenlő távolság egyenlő különbséget jelent, ezért ==a {sávhatár} alatt élő {népesség a sávhatár alatt} a tengely bal szélére zsúfolódik==. A **logaritmikus** tengelyen az egyenlő távolság egyenlő **arányt** jelent: 1000-ről 10 000-re ugyanannyi, mint 10 000-ről 100 000-re.

> megjegyzés: Kapcsolj a két tengely között!

### Feliratok
- cím 4: Melyik tengely mutat többet?
- gomb lineáris: Lineáris
- gomb log: Logaritmikus
- sáv 4: a világ népességének #-a
- sáv 4b: # alatt
- tízszeres: ×10
- forrás 4: Forrás: Világbank, WDI (GDP/fő PPP, várható élettartam, népesség), #

### Adatok
<!-- forrás (az alábbiakra): saját számítás a Világbank WDI 2024-es adataiból (azok az országok, amelyeknek van GDP/fő PPP-, várható élettartam- és népességadata: 195 ország, 7,97 milliárd fő), lekérdezve: 2026-11-23, CC BY 4.0 -->
- sávhatár: 10 000 dollár
- népesség a sávhatár alatt: 42 % (2024)

## 5. Gazdagabb = tovább él?
Játszd le! ==Szinte minden ország jobbra és felfelé halad.== Log. tengelyen közel egyenesre esnek: a jövedelem duplázása nagyjából ugyanannyi évet ad. Ez a **Preston-görbe** ({Preston-görbe éve}). Nigériában ma {Nigéria várható élettartama} a várható élettartam, Dél-Koreában {Dél-Korea várható élettartama}.

> megjegyzés: Kattints egy buborékra! Szaggatott kör: válságév.

### Feliratok
- cím 5: Jövedelem és várható élettartam, #
- trend: trendvonal (illesztett)
- duplázás: kétszeres jövedelem ≈ +# év
- válságév: válságév (becslés)
- kattints: Kattints egy buborékra!
- forrás 5: Forrás: Világbank, WDI (GDP/fő PPP 1990-től), # · trendvonal: saját illesztés

### Adatok
<!-- forrás: Samuel H. Preston (1975): The Changing Relation between Mortality and Level of Economic Development. Population Studies 29(2), 231–248 -->
- Preston-görbe éve: 1975
<!-- forrás (az alábbiakra): Világbank WDI, SP.DYN.LE00.IN, 2024, lekérdezve: 2026-11-23, CC BY 4.0 (a WDI az ENSZ WPP 2024 becslését közli) -->
- Nigéria várható élettartama: 54,6 év (2024, frissítendő)
- Dél-Korea várható élettartama: 83,6 év (2024, frissítendő)
- válságév határa: 8 év (modell)
<!-- forrás: a lecke saját jelölési küszöbe: ha egy év várható élettartama ennyivel tér el a két szomszédos év átlagától, szaggatott körrel „válságév (becslés)” jelölést kap (pl. Ruanda 1994, Haiti 2010, Közép-afrikai Köztársaság 2008, 2019, 2022) -->

## 6. Szerkezetváltás: a földtől az irodáig
A dolgozók három **gazdasági szektorban** dolgoznak: mezőgazdaság, ipar, szolgáltatás. A gépek miatt ==egyre kevesebb ember termel egyre több élelmiszert==, a munkaerő az iparba, majd a szolgáltatásba megy. Kínában a dolgozók {Kína mezőgazdaság 1991}-a dolgozott a földeken 1991-ben, {Kína mezőgazdaság 2025}-a 2025-ben. **Tévhit:** a szolgáltatás nem termel – a tanítás, a gyógyítás is érték.

### Feliratok
- cím 6: Hol dolgoznak az emberek?
- mezőgazdaság: mezőgazdaság
- ipar: ipar
- szolgáltatás: szolgáltatás
- y 6: a foglalkoztatottak %-a
- forrás 6: Forrás: Világbank, WDI – az ILO modellbecslései, 1991–2025

### Adatok
<!-- forrás (az alábbiakra): Világbank WDI, SL.AGR.EMPL.ZS (ILO modellbecslés), lekérdezve: 2026-11-23, CC BY 4.0. A 2025-ös érték is modellbecslés. Magyarország 1949: a keresők kb. fele a mezőgazdaságban (KSH-népszámlálás; a pontos arány ellenőrizendő, ezért a lecke nem mondja ki) -->
- foglalkoztatás első éve: 1991
- foglalkoztatás utolsó éve: 2025
- Kína mezőgazdaság 1991: 59,6 % (1991, becslés)
- Kína mezőgazdaság 2025: 21,7 % (2025, becslés)

## 7. Centrum, félperiféria, periféria
A Világbank a GNI/fő alapján négy **jövedelmi csoportba** sorolja az országokat. A **centrum–periféria** modellben a **centrumban** a tőke és a kutatás, a **periférián** a nyersanyag és az olcsó munka jellemző, a **félperiféria** köztes. ==A térkép jövedelmet mér; a modell közelítés.==

> megjegyzés: Válts mutatót, és kattints egy országra!

### Feliratok
- cím 7 jövedelem: A Világbank jövedelmi csoportjai
- cím 7 GDP: Egy főre jutó GDP vásárlóerőn, #
- cím 7 élettartam: Várható élettartam, #
- gomb jövedelem: Jövedelmi csoport
- gomb GDP: GDP/fő (PPP)
- gomb élettartam: Várható élettartam
- leg jövedelem: GNI/fő (Atlas-módszer, USD), # alapján
- inc LIC: alacsony
- inc LMC: alsó-közepes
- inc UMC: felső-közepes
- inc HIC: magas jövedelmű
- jel centrum: ≈ centrum
- jel félperiféria: ≈ félperiféria
- jel periféria: ≈ periféria
- leg GDP: egy főre jutó GDP (PPP), $
- leg élettartam: várható élettartam, év
- nincs adat: nincs adat
- vitatott: szaggatott határ: vitatott terület
- kártya jövedelem: csoport
- kártya GDP: GDP/fő (PPP)
- kártya GNI: GNI/fő (Atlas)
- kártya élettartam: várható élettartam
- kártya népesség: népesség
- érték dollár: # $
- érték év: # év
- érték fő: # millió fő
- érték nincs: –
- forrás 7: Forrás: Világbank, WDI és jövedelmi csoportok (2026. július) · Natural Earth · Equal Earth-vetület

### Adatok
<!-- forrás (az alábbiakra): World Bank Country and Lending Groups, FY2027 (2026. július 1-jétől, a 2025-ös GNI/fő alapján, Atlas-módszer, USD): alacsony ≤ 1175, alsó-közepes 1176–4635, felső-közepes 4636–14 375, magas > 14 375; a határokat Our World in Data (ourworldindata.org/grapher/world-banks-income-groups) közli a Világbank alapján, lekérdezve: 2026-11-24, CC BY 4.0. Az adatfájl csoportbesorolása a letöltéskori (a lecke ellenőrzi, hogy a 2025-ös GNI/fő és e határok szerint az országok legalább 95 %-a ugyanide esik; eltér pl. Argentína és Törökország). -->
- jövedelmi besorolás éve: 2025
- alacsony jövedelem felső határa: 1175 dollár (2025, frissítendő)
- alsó-közepes jövedelem felső határa: 4635 dollár (2025, frissítendő)
- felső-közepes jövedelem felső határa: 14 375 dollár (2025, frissítendő)
- GDP osztályközök: 2500; 5000; 15 000; 40 000 dollár
<!-- forrás: a lecke saját osztályközei (kb. logaritmikus lépések), a tanár átírhatja -->
- élettartam osztályközök: 60; 65; 70; 75; 80 év
<!-- forrás: a lecke saját osztályközei (5 éves lépések), a tanár átírhatja -->

## 8. Felzárkózók
A periféria nem végzet. **Dél-Korea**, az egyik **újonnan iparosodott ország**, 1990-ben az EU-átlag {Dél-Korea 1990}-án állt, 2024-ben {Dél-Korea 2024}-án. ==Kína {Kína 1990}-ról {Kína 2024}-ra zárkózott fel==; ő a **BRICS**-csoport egyik alapítója. Nigéria {Nigéria 2024}-on maradt.

> megjegyzés: Kapcsold be a többi országot is!

### Feliratok
- cím 8: Ki zárkózik fel? #
- cím 8b: GDP/fő (PPP), az EU-átlag %-ában
- EU = 100: EU-átlag = 100
- forrás 8: Forrás: Világbank, WDI, 1990–# · EU: a mai 27 tagállam átlaga

### Adatok
<!-- forrás (az alábbiakra): saját számítás a Világbank WDI GDP/fő PPP (NY.GDP.PCAP.PP.KD) adataiból; az EU-átlag a WDI „European Union” (EUU, a mai 27 tagállam) aggregátuma, lekérdezve: 2026-11-23, CC BY 4.0. A BRICS alapítói (2009–2010): Brazília, Oroszország, India, Kína, Dél-Afrika; 2024 óta bővült (frissítendő) -->
- Dél-Korea 1990: 43 % (1990)
- Dél-Korea 2024: 101 % (2024, frissítendő)
- Kína 1990: 5 % (1990)
- Kína 2024: 44 % (2024, frissítendő)
- Nigéria 2024: 15 % (2024, frissítendő)

## 9. Összefoglalás
A GDP a termelést, a GNI a lakók jövedelmét méri; összevetéshez egy főre és vásárlóerőn számolunk. ==A jövedelem és a várható élettartam logaritmikusan függ össze.== A fejlődéssel a munka a földekről a gyárakba, majd az irodákba vándorol. A jövedelmi csoportok nem véglegesek: van, aki felzárkózik.

> megjegyzés: Minden adat becslés, és utólag módosulhat.

### Feliratok
- honnan típus: Honnan tudjuk?
- honnan cím: Nemzeti számlák és árfelmérés
- honnan 1: GDP, GNI:
- honnan 1 v: a statisztikai hivatalok számolják, a Világbank egységesíti
- honnan 2: PPP:
- honnan 2 v: több ezer termék árának felmérése (ICP), néhány évente
- honnan 3: Hibahatár:
- honnan 3 v: becslés, a régebbi évek is utólag változnak
- cím 9: Jövedelmi csoportok, #
- ö 1: GDP: az országban termelt érték; GNI: a lakók jövedelme.
- ö 2: Összevetéshez: egy főre és vásárlóerőn (PPP).
- ö 3: Logaritmikus tengely: minden osztás tízszeres.
- ö 4: Szegény országban kevés pénz is sok életévet ad.
- ö 5: Szerkezetváltás: mezőgazdaság → ipar → szolgáltatás.
- ö 6: Centrum és periféria – de van, aki felzárkózik.
- forrás 9: Forrás: Világbank, WDI · Natural Earth · 2024

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - A WDI-mutatók becslések, és visszamenőleg is módosulnak (új PPP-kör, népszámlálás). A PPP-szorzó az ICP
    2021-es árfelméréséből jön; a GDP/fő PPP 2021-es állandó áron van, ezért az évek összevethetők, de 1990
    előtt nincs összehasonlítható PPP-adat – a buborékdiagram ezért 1990-ben kezdődik (a brief 1960-at írt).
  - A GNI/GDP arány csak 2021-re számolható pontosan az adatfájlból (a GNI PPP folyó áras, a GDP PPP
    2021-es állandó áras); Magyarországon 2021-ben 97,1 % (a brief 4–6 %-os eltérése más évre vonatkozhat).
  - A centrum–félperiféria–periféria modell (Wallerstein) elméleti modell, nem mérés; a lecke a Világbank
    négy jövedelmi csoportjával közelíti (magas ≈ centrum, közepes ≈ félperiféria, alacsony ≈ periféria).
    Ez egyszerűsítés: pl. az olajexportáló magas jövedelmű országok vagy a nagy, de közepes jövedelmű
    országok (Kína) helye a modellben vitatott.
  - A jövedelmi csoportok az adatfájl letöltéskori (2026. júliusi, FY2027) besorolását mutatják; a lecke a
    határokat a .md-ből olvassa, és ellenőrzi, hogy a 2025-ös GNI/fő szerint az országok ≥ 95 %-a ugyanoda
    esik (Argentína, Törökország eltér – a Világbank a besoroláskor még más adattal számolt).
  - A várható élettartam válságévekben (háború, népirtás, járvány, földrengés) a WPP becslése szerint
    egyetlen évre is nagyot esik (Ruanda 1994: 12,2 év; Közép-afrikai Köztársaság 2022: 18,8 év). A
    Közép-afrikai Köztársaság idősora 2008 és 2022 között többször ugrál – ezek bizonytalan becslések. A
    lecke nem hagyja el őket, hanem szaggatott körrel „válságév (becslés)” jelöléssel mutatja.
  - A Preston-görbe trendvonala saját, egyszerű illesztés (várható élettartam = a + b · ln GDP/fő, az
    országok súlyozás nélkül); nem a Preston-féle eredeti függvény.
  - A foglalkoztatási szerkezet az ILO modellbecslése (sok országban kevés a felmérés); Magyarország
    1949-es mezőgazdasági aránya (kb. a keresők fele) a KSH-népszámlálásból ellenőrizendő.
  - Tajvan, Észak-Ciprus, Szomáliföld, Nyugat-Szahara és a Falkland-szigetek a WDI-ben nem szerepel külön
    (nincs adat); a vitatott területek határa szaggatott (shared/foldrajz/README.md). A határok a Natural
    Earth de facto vonalai.
  - A BRICS tagsága 2024 óta bővült (frissítendő); a lecke csak az alapítókat említi.
-->
