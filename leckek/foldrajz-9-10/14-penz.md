# Mennyibe kerül egy hitel? – költségvetés, infláció, kamat, hitel, árfolyam
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 9. A pénz és a tőke mozgásai a világgazdaságban

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/14-penz.md
  A kitalált példák (költségvetés, megtakarítás, hitel, frankhitel törlesztője, adósságmodell) a vásznon
  „kitalált adat” vagy „modell” bélyeget kapnak. A valódi adatok (KSH infláció, MNB alapkamat, árfolyam)
  évszámmal és forrással szerepelnek; az évenként változók „frissítendő” jelölést kapnak.
  Szerkesztői elv (terv 7. fejezet 8. pont): bank, termék, márka vagy konkrét befektetés nem szerepel,
  a lecke nem ad befektetési tanácsot; a jegybank döntéseit tényként, dátummal írja le, nem értékeli.
  Az eredményeket (törlesztő, kamat, THM, árszint) a lecke számolja; ha a panelen kiírt szám eltér a
  számolttól, a QA hibát jelez (L.checks).
-->

## Közös

### Feliratok
- kitalált adat: kitalált adat
- modell: modell
- csúszka év: Év
- gomb lejátszás: Lejátszás
- forint: # Ft
- százalék: # %
- év egység: # év

## 1. Bevétel, kiadás, tartalék
A **költségvetés** a bevételek és a kiadások terve. A **fix kiadás** havonta ugyanannyi, a **változó** rajtunk is múlik. ==Ami megmarad, az a tartalék==: ebből fizetjük a váratlan kiadást. Ha nincs, hitel kell.

### Feliratok
- cím 1: Hová lesz a havi pénz?
- bevétel: bevétel
- kiadás: kiadás
- fix kiadás: fix kiadás
- változó kiadás: változó kiadás
- tartalék: tartalék
- hiány: hiány
- havi tartalék: havi tartalék: #
- havi hiány: havi hiány: #
- cím 1b: Megtakarítás a hónapok végén
- hónap: hónap
- ezer Ft: ezer Ft
- váratlan: váratlan kiadás
- hitel kell: itt már hitel kell
- év vége: az év végén: #
- csúszka bevétel: Havi bevétel
- csúszka fix: Fix kiadások
- csúszka változó: Változó kiadások
- gomb váratlan: Váratlan kiadás
- fix példa: lakhatás, rezsi, bérlet
- változó példa: étel, ruha, szórakozás

### Adatok
<!-- forrás (az alábbiakra): kitalált példa egy háztartás havi költségvetésére (kerek számok, nem átlagadat) -->
- havi bevétel: 450 000 Ft
- havi fix kiadás: 260 000 Ft
- havi változó kiadás: 150 000 Ft
- váratlan kiadás: 150 000 Ft
- váratlan kiadás hónapja: 6

## 2. Infláció: mennyit ér a pénzed?
A pénz **csereeszköz**, **értékmérő** és **értékőrző**. Az **infláció** az árak általános emelkedése. A KSH szerint ugyanaz a kosár {kosár első éve}-ben 10 000 Ft, {kosár utolsó éve}-ben {kosár ára a végén} volt. ==A fiókban tartott 10 000 Ft vásárlóereje {vásárlóerő a végén}-ra olvadt.== **Tévhit:** ami megvan, az nem fogy el.

> megjegyzés: Húzd az év-csúszkát!

### Feliratok
- cím 2: Mennyit ér a 10 000 forintod?
- kosár: a kosár ára
- bankjegy: 10 000 Ft vásárlóereje
- bankjegy felirat: 10 000 Ft
- eredeti: az első év kosarához mérve
- cím 2b: Infláció az előző évhez képest (%)
- honnan típus: Honnan tudjuk?
- honnan cím: KSH, fogyasztói árindex
- honnan 1: Mit mér?
- honnan 1 v: kb. 1000 termék és szolgáltatás árát
- honnan 2: Hogyan?
- honnan 2 v: havonta, sok ezer üzletben, országszerte
- honnan 3: Mennyit számít?
- honnan 3 v: amire több pénz megy el, nagyobb súlyú
- szerepek cím: A pénz három szerepe
- szerep 1: csereeszköz
- szerep 1 v: ezzel fizetünk
- szerep 2: értékmérő
- szerep 2 v: ebben mérjük az árakat
- szerep 3: értékőrző
- szerep 3 v: félretehető – ezt rontja az infláció
- forrás 2: Forrás: KSH, fogyasztóiár-index (előző év = 100), 2015–2025

### Adatok
<!-- forrás (az alábbiakra): KSH STADAT 1.1.1.1. Főbb ármutatók (előző év = 100,0 %), fogyasztói árindex, éves átlag, frissítve: 2026-08-07, lekérdezve: 2026-11-24 (ksh.hu/stadat_files/ara/hu/ara0001.html). A KSH 2022-ben 978 reprezentáns termék és szolgáltatás árát figyelte (KSH reprezentánsok tájékoztató 2022), havonta kb. 75 000 árat rögzít. -->
- kosár első éve: 2015
- kosár utolsó éve: 2025
- infláció évente: −0,1; 0,4; 2,4; 2,8; 3,4; 3,3; 5,1; 14,5; 17,6; 3,7; 4,4 %
<!-- forrás: KSH STADAT 1.1.1.1 (2015–2025; az utolsó érték 2025, frissítendő: évente januárban jön az új éves adat) -->
- kosár ára a végén: kb. 17 300 Ft (2025, frissítendő)
<!-- forrás: saját számítás a KSH éves indexeiből: 10 000 · 1,004 · 1,024 · … · 1,044 = 17 296 Ft (a lecke számolja és ellenőrzi) -->
- vásárlóerő a végén: kb. 5780 Ft (2025, frissítendő)
<!-- forrás: saját számítás: 10 000 / 1,7296 = 5782 Ft (a lecke számolja és ellenőrzi) -->

## 3. Kamatos kamat
Ha a betét **kamatát** bent hagyod, jövőre a kamat is kamatozik: ez a **kamatos kamat**. ==Évi {példa kamat} mellett a pénz {duplázódási idő} alatt duplázódik==, nem 10 év alatt (**72-es szabály**: 72 / 7 ≈ 10). Betétnél az **EBKM** mutatja az éves hozamot.

### Feliratok
- cím 3: Kamat a kamaton
- tőke: befizetett összeg
- egyszerű kamat: kamat a befizetésre
- kamat a kamaton: kamat a kamaton
- képlet 3: FV = PV · (1 + r)ⁿ
- ezer Ft 3: ezer Ft
- év 3: év
- duplázódás: duplázódási idő:
- szabály: 72-es szabály: 72 / # ≈ # év
- végösszeg: # év múlva:
- ebből kamat: ebből kamat:
- korábban: ha 5 évvel korábban kezded:
- csúszka összeg: Befizetés most
- csúszka kamat: Éves kamat
- csúszka évek: Évek száma
- gomb korábban: 5 évvel korábban

### Adatok
<!-- forrás (az alábbiakra): kitalált példa; a duplázódási idő saját számítás: ln 2 / ln 1,07 = 10,24 év (a lecke számolja és ellenőrzi); 10 %-nál 7,27 év. A 72-es szabály közismert közelítés. EBKM: 82/2010. (III. 25.) Korm. rendelet az egységesített betéti kamatláb-mutatóról. -->
- példa összeg: 100 000 Ft
- példa kamat: 7 %
- példa évek: 30 év
- duplázódási idő: kb. 10,2 év

## 4. A jegybank és a reálkamat
Az **MNB** fő feladata az árstabilitás: kb. {inflációs cél} inflációt céloz. Ha az árak gyorsan nőnek, **emeli az alapkamatot**: a hitel drágul, a megtakarítás többet hoz, lassul a költés és az áremelkedés. ==A megtakarítás valódi hozama a kamat és az infláció különbsége== (**reálkamat**).

> megjegyzés: Mikor volt negatív a reálkamat?

### Feliratok
- cím 4: Infláció és jegybanki alapkamat
- infláció jel: infláció (éves átlag)
- alapkamat jel: alapkamat az év végén
- cél sáv: inflációs cél ± 1 százalékpont
- reálkamat pozitív: kamat − infláció: +# százalékpont
- reálkamat negatív: kamat − infláció: # százalékpont
- leolvasás 4: #: infláció #, alapkamat #
- most 4: alapkamat # óta: #
- lánc 1: alapkamat ↑
- lánc 2: drágább hitel, többet hozó betét
- lánc 3: kevesebb költés
- lánc 4: lassul az áremelkedés
- y 4: %
- forrás 4: Forrás: KSH, fogyasztóiár-index; MNB, jegybanki alapkamat (év végi érték), 2015–2025

### Adatok
<!-- forrás (az alábbiakra): MNB, a jegybanki alapkamatról szóló elnöki rendeletek (mnb.hu → Monetáris politika → A Monetáris Tanács), lekérdezve: 2026-11-24. Év végi értékek: 2015: 1,35 % (2015. júl. óta); 2016–2019: 0,90 % (2016. máj. óta); 2020: 0,60 % (2020. júl. óta); 2021: 2,40 % (2021. dec.); 2022: 13,00 % (2022. szept. óta); 2023: 10,75 % (2023. dec.); 2024–2025: 6,50 % (2024. szept. óta). Az inflációs cél 3 %, ±1 százalékpontos toleranciasávval (MNB, 2015 óta); az árstabilitás elsődlegessége: 2013. évi CXXXIX. törvény a Magyar Nemzeti Bankról, 3. §. -->
- alapkamat év végén: 1,35; 0,9; 0,9; 0,9; 0,9; 0,6; 2,4; 13; 10,75; 6,5; 6,5 %
- inflációs cél: 3 %
- jelenlegi alapkamat: 5,5 % (2026, frissítendő)
<!-- forrás: MNB elnöki rendeletek listája (2026: II. 24., VI. 23., VII. 21., VIII. 25.) és global-rates.com (6,25 → 6,00 → 5,75 → 5,50 %, hatályos 2026-08-26), lekérdezve: 2026-11-24 – ellenőrizendő az MNB honlapján -->
- jelenlegi alapkamat kezdete: 2026. augusztus 26.
<!-- forrás: mint fent (ellenőrizendő) -->

## 5. A hitel törlesztőrészlete
Havi részletes (**annuitásos**) hitelnél eleinte a részlet nagy része kamat, később egyre több a tőke. **Tévhit:** a kisebb részlet olcsóbb hitel. ==Hosszabb futamidőnél kisebb a részlet, de több a kamat.== {példa hitelösszeg}, {példa futamidő}, évi {példa hitelkamat}: havonta {példa törlesztő}.

### Feliratok
- cím 5: Mennyi a havi részlet – és mennyi az egész?
- tőkerész: tőketörlesztés
- kamatrész: kamat
- havi törlesztő: havi törlesztő:
- teljes: összesen visszafizetsz:
- kamat összesen: ebből kamat:
- hónap 5: hónap
- ezer Ft 5: ezer Ft / hó
- cím 5b: Ugyanez a hitel más futamidővel
- futamidő tengely: futamidő (év)
- részlet görbe: havi részlet (ezer Ft)
- kamat görbe: összes kamat (ezer Ft)
- csúszka hitelösszeg: Hitelösszeg
- csúszka futamidő: Futamidő
- csúszka hitelkamat: Éves kamat

### Adatok
<!-- forrás (az alábbiakra): kitalált példa (a terv briefje); annuitás: A = P · i / (1 − (1 + i)^−n), i = évi kamat / 12, n = hónapok. 3 000 000 Ft, 60 hónap, 10 % → 63 741 Ft/hó, 824 468 Ft kamat (a lecke számolja és ellenőrzi). -->
- példa hitelösszeg: 3 000 000 Ft
- példa futamidő: 5 év
- példa hitelkamat: 10 %
- példa törlesztő: kb. 63 700 Ft

## 6. THM, fix vagy változó kamat
A **THM** (teljes hiteldíj mutató) a kamatot és a díjakat is egy évi százalékba számolja. Jogszabály írja elő, ezért ==a hitelek THM-je összevethető==. A **fix kamat** a futamidő alatt nem változik. A **változó kamat** kezdetben gyakran kisebb, de ha emelkedik, ==nő a törlesztő is==.

> megjegyzés: Nyomd meg: +3 százalékpont!

### Feliratok
- cím 6: Mit mutat a THM?
- sor hitel: hitelösszeg
- sor kamat: éves kamat
- sor díj egyszeri: folyósítási díj
- sor díj havi: havi számlavezetési díj
- thm: THM
- bar kamat: éves kamat
- bar thm díj nélkül: THM díjak nélkül
- bar thm díjjal: THM díjakkal
- havi tőkésítés: havi tőkésítés miatt több
- cím 6b: Havi törlesztő: fix vagy változó kamat
- fix vonal: fix kamat: #
- változó vonal: változó kamat: #
- emelés: +# százalékpont
- kamat fix: kamat összesen (fix): #
- kamat változó: kamat összesen (változó): #
- gomb díjak: Díjakkal
- gomb díjak nélkül: Díjak nélkül
- gomb emelés: +3 százalékpont a 2. évtől
- gomb vissza: Marad a kamat
- hónap 6: hónap

### Adatok
<!-- forrás (az alábbiakra): kitalált példa; a THM számítása: 83/2010. (I. 25.) Korm. rendelet a teljes hiteldíj mutató meghatározásáról (évi effektív kamatláb, amelynél a kifizetések jelenértéke = a kapott összeg). 3 000 000 Ft, 10 %, 60 hónap: díjak nélkül THM = (1 + 0,10/12)^12 − 1 = 10,47 %; 1 % folyósítási díjjal és 1000 Ft havi díjjal 11,70 % (a lecke számolja és ellenőrzi). Fix 11 % → 65 227 Ft/hó; változó 10 % → 63 741 Ft/hó, a 13. hónaptól 13 % → 67 423 Ft/hó (saját számítás). -->
- folyósítási díj: 1 %
- havi díj: 1000 Ft
- THM díjakkal: kb. 11,7 %
- fix kamat: 11 %
- változó kamat: 10 %
- kamatemelés: 3 %

## 7. Árfolyam: ha a hitel frankban van
Az **árfolyam** megmutatja, hány forintot adnak egy egység devizáért. 2008 előtt sokan svájci frankban vettek fel hitelt, mert kisebb volt a kamata. A törlesztő frankban alig változott, ==forintban az árfolyammal együtt nőtt==: 2008 nyarán 1 frank {frank 2008 nyarán}, 2015 elején {frank 2015 elején} volt.

> megjegyzés: 2015-ben a devizahiteleket forintra váltották.

### Feliratok
- cím 7: Mennyi forint egy svájci frank?
- y 7: Ft / svájci frank (havi átlag)
- y2 7: havi törlesztő, Ft
- törlesztő jel: a törlesztő: # frank havonta
- leolvasás 7: #: 1 frank = # Ft → törlesztő #
- változás 7: +# % a 2008. júliusihoz képest
- válság: 2008 ősze: pénzügyi világválság
- küszöb: 2015. jan.: a svájci jegybank elengedi a frankot
- csúszka hónap: Hónap
- hónapnevek: jan.; febr.; márc.; ápr.; máj.; jún.; júl.; aug.; szept.; okt.; nov.; dec.
- dátum 7: #. #
- forrás 7: Forrás: Európai Központi Bank, EUR/HUF és EUR/CHF havi átlag (a frank ára ezekből számolva)

### Adatok
<!-- forrás (az alábbiakra): Európai Központi Bank, Data Portal, EXR.M.HUF.EUR.SP00.A és EXR.M.CHF.EUR.SP00.A (havi átlagos referencia-árfolyam), lekérdezve: 2026-11-24; HUF/CHF = (HUF/EUR) / (CHF/EUR), saját számítás, egy tizedesre kerekítve. A svájci jegybank 2015. január 15-én szüntette meg az 1,20 CHF/EUR árfolyamküszöböt. A forintosítás: 2014. évi LXXVII. törvény (a forint-átváltás 2015 elején történt). -->
- frank első hónapja: 2006. január
- frank havonta: 161,8; 161,5; 166,2; 168,6; 168,6; 174,6; 176,9; 173,9; 173,2; 168,0; 162,6; 159,0; 157,2; 156,2; 155,0; 150,2; 150,5; 151,3; 149,0; 155,8; 153,8; 150,3; 154,4; 152,6; 158,0; 163,0; 165,4; 159,0; 152,5; 150,2; 143,2; 145,5; 151,0; 171,2; 175,0; 172,2; 187,4; 200,1; 201,6; 194,9; 186,5; 185,1; 179,0; 177,2; 179,5; 177,4; 179,4; 181,9; 182,5; 184,9; 183,3; 185,2; 195,2; 204,5; 210,8; 209,8; 215,5; 203,7; 205,0; 216,7; 215,4; 209,0; 210,5; 204,4; 212,9; 220,7; 227,5; 243,1; 237,4; 241,4; 251,2; 247,8; 253,8; 240,8; 242,3; 245,2; 244,5; 244,4; 238,4; 232,2; 235,1; 233,2; 234,2; 236,4; 239,3; 238,0; 247,0; 244,8; 235,4; 240,0; 238,5; 242,7; 242,9; 239,3; 241,7; 245,2; 245,6; 254,0; 255,8; 252,2; 249,6; 251,1; 255,0; 259,0; 259,4; 254,9; 255,2; 258,5; 289,3; 289,0; 286,1; 288,5; 294,8; 298,4; 296,9; 289,1; 286,9; 286,0; 288,3; 290,4 Ft
- frank 2008 nyarán: 143,2 Ft
<!-- forrás: ECB, 2008. július havi átlaga (a lecke ellenőrzi, hogy egyezik a sorral) -->
- frank 2015 elején: 289,3 Ft
<!-- forrás: ECB, 2015. január havi átlaga (a lecke ellenőrzi) -->
- törlesztő frankban: 300 CHF
<!-- forrás: kitalált példa (egyszerűsítés: a frankban számolt törlesztő változatlan; a valóságban a frankkamat és a bank árfolyamrése is változott) -->

## 8. Adósságcsapda: egyén és ország
Ha a kamat több, mint amennyit évente törlesztesz, ==az adósság magától nő==: ez az **adósságcsapda**. {modell kamat} kamat és {modell törlesztés} törlesztés mellett a fordulópont a jövedelem {fordulópont}-a. Egy országnál a jövedelem helyett a GDP számít.

> megjegyzés: Keresd meg a fordulópontot!

### Feliratok
- cím 8: Mikor nő magától az adósság?
- y 8 háztartás: adósság az éves jövedelem %-ában
- y 8 ország: államadósság a GDP %-ában
- x 8: év
- fordulópont jel: fordulópont: #
- kamat oszlop: évi kamat
- törlesztés oszlop: évi törlesztés
- csökken: az adósság csökken
- nő: adósságcsapda: az adósság nő
- csúszka modell kamat: Éves kamat
- csúszka törlesztés: Évi törlesztés (a jövedelem / GDP %-a)
- gomb háztartás: Háztartás
- gomb ország: Ország
- kezdő adósság jel: kiinduló adósság: #

### Adatok
<!-- forrás (az alábbiakra): modell (saját): adósság(t + 1) = adósság(t) · (1 + kamat) − törlesztés, az éves jövedelem (GDP) %-ában, jövedelemnövekedés és infláció nélkül. Fordulópont: adósság = törlesztés / kamat (10 / 12 % → 83 %). Az ország valódi adósságdinamikájában a GDP növekedése és az infláció is számít, ezt a modell elhagyja. -->
- modell kamat: 12 % (modell)
- modell törlesztés: 10 % (modell)
- kezdő adósság: 100 % (modell)
- fordulópont: kb. 83 % (modell)

## 9. Összefoglalás: a befektetési háromszög
Egy befektetés **hozama**, **biztonsága** (kis **kockázata**) és **likviditása** (gyors pénzzé tehetősége) közül ==egyszerre csak kettő lehet kedvező==. Aki mindhármat ígéri, annál légy óvatos. A költségvetés, a tartalék, a kamatos kamat és a THM ismerete segít a döntésben.

> megjegyzés: Kattints egy befektetésfajtára!

### Feliratok
- cím 9: A befektetési háromszög
- csúcs hozam: hozam
- csúcs biztonság: biztonság
- csúcs likviditás: likviditás
- készpénz: készpénz
- bankbetét: bankbetét
- állampapír: állampapír
- részvény: részvény
- ingatlan: ingatlan
- gyenge: gyenge pont: #
- miért készpénz: nem kamatozik, az infláció rontja
- miért bankbetét: a kamat gyakran az infláció alatt
- miért állampapír: lejárat előtt nehezebb pénzzé tenni
- miért részvény: az ára erősen ingadozhat
- miért ingatlan: lassan és költségesen adható el
- nincs: hozam + biztonság + likviditás?
- nincs 2: ilyen nincs
- ö cím: Amit megtanultál
- ö 1: Költségvetés: előbb a tartalék, aztán a többi.
- ö 2: Az infláció a pénz vásárlóerejét rontja.
- ö 3: A kamatos kamat lassan indul, aztán gyorsul.
- ö 4: A hitel árát a THM mutatja, nem a részlet.
- ö 5: Változó kamat és deviza: a részlet nőhet.
- ö 6: Ha a kamat gyorsabb a törlesztésnél: csapda.
- jel 9: általános tankönyvi besorolás, nem ajánlás

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - A befektetési háromszögben a termékcsoportok helye tankönyvi általánosítás (pl. a lakossági állampapír
    egyes fajtái lejárat előtt is visszaválthatók, kisebb hozammal vagy díjjal; a betét lekötött vagy
    látra szóló is lehet). A lecke nem ajánl terméket.
  - A jegybanki alapkamatot az év végi értékkel, az inflációt az éves átlaggal ábrázoljuk (KSH): a kettő
    különbsége csak közelítő reálkamat; a reálkamat pontosan (1 + i) / (1 + π) − 1, és a betétek kamata
    nem azonos az alapkamattal.
  - A 2026-os alapkamat-adatok (5,50 % 2026. augusztus 26-tól) egy aggregátor oldalról és az MNB
    rendeletlistájából valók – az MNB honlapján ellenőrizendő, és évente frissítendő.
  - A frankhitel-példa egyszerűsítés: a frankban számolt törlesztőt állandónak vesszük; a valóságban a
    bankok kamatot is emeltek, és az árfolyamrés is számított. A devizahitelezés okait és a 2014–2015-ös
    intézkedéseket (elszámolás, forintosítás) a lecke csak tényként, egy mondatban említi.
  - Az adósságcsapda-modell növekedés és infláció nélküli; az államadósság valódi dinamikájához a GDP
    növekedése, az infláció és az elsődleges egyenleg is kell (a modell ezt nem mutatja). Valódi
    államadósság-adatot a lecke szándékosan nem mutat (évente változik, külön lecke tárgya lehet).
  - A THM-számítás a 83/2010. Korm. rendelet elve szerint (évi effektív ráta, a hónapok tört évként);
    a valódi hirdetésekben további díjak (pl. biztosítás, értékbecslés) is beleszámíthatnak.
-->
