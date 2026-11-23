# Miért ingadozik a hiúzok száma? – ragadozó, zsákmány, populációs kölcsönhatások
tantárgy: Biológia · évfolyam: 7–8. · témakör: 6. Életközösségek vizsgálata

## Közös
### Feliratok
- nyulak: nyulak
- hiúzok: hiúzok
- növényzet: növényzet
- év tengely: év
- létszám tengely: létszám (ezer, modell)
- modell bélyeg: modell – egyszerűsít
- vázlat: vázlat
- honnan tudjuk: HONNAN TUDJUK?
- újra gomb: Újra (új véletlen)
<!-- A lecke két valódi állatfajt használ: a kanadai hiúzt (Lynx canadensis) és a hótalpú nyulat (Lepus americanus). Az 1–4. és a 6. lépés modellje didaktikus (exponenciális, logisztikus, Lotka–Volterra, ill. növényzet–nyúl–hiúz modell); a számok „modellegységek”, nem mért létszámok. -->

## 1. Ha semmi sem korlátozná
Egy nyúl egy nyáron több almot is ellethet. Tegyük fel, hogy a nyulak száma minden évben **ugyanannyiszorosára** nő – a csúszkán állíthatod, hányszorosára. Nézd a számlálót: néhány év alatt ezrek, húsz év alatt ==milliók== lennének. Ez a **korlátlan (exponenciális) növekedés**. A természetben soha nem tart sokáig. Miért?

### Feliratok
- kérdés 1: Mi lenne, ha semmi sem korlátozná a nyulakat?
- számláló: # nyúl
- év felirat: # év múlva
- húsz év: 20 év múlva: # nyúl
- kifut: kifut a grafikonból ↑
- szorzó csúszka: évi szaporodás (hányszoros)
- korlátlan: korlátlan növekedés
### Adatok
- kezdő nyulak: 20
- évi szorzó: 2
<!-- Modellbeállítás: N(t) = N0 · szorzó^t (folytonos változat: dN/dt = r·N, r = ln szorzó). A hótalpú nyúl évente 2–4 almot ellethet, almonként átlagosan kb. 2–6 kölyökkel (a ciklus szakaszától függően); a „×2 évente” kerek, didaktikus szám, nem mért érték. 20 · 2^10 = 20 480; 20 · 2^20 = 20 971 520. -->

## 2. A határ: az eltartóképesség
Minél több a nyúl, annál kevesebb táplálék és búvóhely jut egy-egy állatra. A létszám előbb lassan, aztán gyorsan nő, végül ==megáll egy határnál==: ez az **eltartóképesség**, ahány egyedet a terület tartósan eltart. Tévhit, hogy a populáció egyenletesen nő: a görbe S alakú.

> megjegyzés: Állítsd a növényzetet! Több táplálék – magasabb határ.

### Feliratok
- kérdés 2: Meddig nőhet a nyulak száma?
- eltartóképesség: eltartóképesség
- lassan: lassan indul
- gyorsan: gyorsan nő
- megáll: megáll a határnál
- növényzet csúszka: növényzet (táplálék)
- K felirat: határ: # nyúl
### Adatok
- eltartóképesség bő növényzetnél: 400
- növényzet kezdetben: 75 %
<!-- Modellbeállítás: logisztikus növekedés, dN/dt = r·N·(1 − N/K), r = ln 2 /év (mint az 1. lépésben), K = eltartóképesség · növényzet. A valóságban a létszámot egyszerre több tényező korlátozza (táplálék, búvóhely, ragadozók, betegségek); a modell ezeket egyetlen K-ba sűríti. -->

## 3. Jön a ragadozó
A havas mezőre hiúzok érkeznek. A közelükbe kerülő nyulat elkaphatják. Amelyik hiúz eleget eszik, utódot nevel, amelyik éhezik, elpusztul. Figyeld: ==a hiúzok a nyulak után futnak==. Minden futás kicsit más, mert a véletlen is számít – néha a hiúzok ki is halnak.

> megjegyzés: A szimuláció egyszerűsít: a valódi erdő sokkal nagyobb.

### Feliratok
- kérdés 3: Mi történik, ha hiúzok is vannak?
- nyúlgörbe: nyulak a mezőn
- hiúzgörbe: hiúzok a mezőn
- kihaltak: a hiúzok kihaltak ebben a futásban
- jelmagyarázat nyúl: = nyúl
- jelmagyarázat hiúz: = hiúz
### Adatok
- szimuláció hossza: 24 év
<!-- Modellbeállítás (ágensalapú szimuláció): a nyulak véletlenszerűen bolyonganak, és a létszámtól függő eséllyel szaporodnak (logisztikusan); a hiúzok bolyonganak, a közelükbe kerülő nyulat bizonyos eséllyel elkapják, energiát gyűjtenek, és ha elég sok energiájuk van, évente egyszer (tavasszal) utódot hoznak; éhezve elpusztulnak. Ha a mezőn 2-nél kevesebb hiúz marad, kis eséllyel a szomszéd területről bevándorol egy (enélkül a hiúzok az első összeomlás után gyakran végleg kihalnak, és a ciklus nem ismétlődik). A paraméterek a lecke kódjában vannak (nem tényadatok). Minden futás egy seedelt véletlenszám-sorozatból jön; a QA az alapseeddel fotóz. -->

## 4. Egymást kergető görbék
Sok nyúl – ==szaporodnak a hiúzok==. Sok hiúz – fogynak a nyulak. Kevés nyúl – éheznek a hiúzok. Kevés hiúz – újra nőnek a nyulak. Ezért a hiúzcsúcs **később** jön. Tévhit, hogy a ragadozó kiirtja a zsákmányát: előbb ő maga fogy meg. Több hiúzzal nagyobb a hullám, de az átlag marad.

### Feliratok
- kérdés 4: Miért ingadozik a két létszám?
- fázis cím: nyulak – hiúzok sík
- negyed 1: sok nyúl: nő a hiúz
- negyed 2: sok hiúz: fogy a nyúl
- negyed 3: kevés nyúl: fogy a hiúz
- negyed 4: kevés hiúz: nő a nyúl
- nyúlcsúcs: nyúlcsúcs
- hiúzcsúcs: hiúzcsúcs
- késés: ≈ # év késés
- átlag: a nyulak átlaga
- egyensúly: egyensúlyi pont
- r csúszka: nyulak szaporodása
- a csúszka: hiúzok vadászsikere
- hiúz gomb: + 20 ezer hiúz
- most: most
### Adatok
- nyulak szaporodása: 0,54
- vadászsiker: 0,027
- hiúzok gyarapodása: 0,024
- hiúzok pusztulása: 0,80
- nyulak 1900-ban: 34,6
- hiúzok 1900-ban: 5,8
<!-- Modellbeállítás: Lotka–Volterra-modell, dN/dt = r·N − a·N·P; dP/dt = c·N·P − m·P (N: nyulak, P: hiúzok, ezer prémben mérve; az idő években). A paraméterek a Hudson's Bay Company 1900–1920-as prémadataira illesztett értékek (legkisebb négyzetek a logaritmusokon; saját illesztés, egyezik B. Carpenter: „Predator-Prey Population Dynamics: the Lotka-Volterra model in Stan”, 2018 esettanulmányának becslésével: 0,55; 0,028; 0,80; 0,024; kezdőérték 33,9 és 5,9). A modellben a nyulak átlaga egy teljes ciklusra pontosan m/c (≈ 34 ezer), a hiúzoké r/a (≈ 20 ezer), akármekkora a hullám – ezt a lecke ki is számolja. -->

## 5. Mit mutatnak a prémek?
A **Hudson's Bay Company** évszázadokon át vásárolt prémeket kanadai vadászoktól, és minden évet feljegyzett. A kanadai hiúz és a hótalpú nyúl prémjeinek száma ==kb. tízévente csúcsosodik==, és a hiúz egy-két évvel később. A modell jól illik rá, de a prém nem létszám: a vadászattól is függ, és a nyulakat a táplálék is korlátozza.

### Feliratok
- kérdés 5: Valóban így van a természetben?
- prém tengely: felvásárolt prém (ezer)
- forrás: Hudson's Bay Company, Kanada, 1900–1920
- adat nyúl: hótalpú nyúl (prém)
- adat hiúz: kanadai hiúz (prém)
- modell nyúl: modell
- modell gomb: Modell rá / le
- csúcstáv: # év
- prémes kártya: Prémfelvásárlási könyvek
- prémes szöveg: évről évre: hány prémet vettek
- Elton: Elton és Nicholson, 1942
### Adatok
- nyúlprémek: 1900: 30 · 1901: 47,2 · 1902: 70,2 · 1903: 77,4 · 1904: 36,3 · 1905: 20,6 · 1906: 18,1 · 1907: 21,4 · 1908: 22 · 1909: 25,4 · 1910: 27,1 · 1911: 40,3 · 1912: 57 · 1913: 76,6 · 1914: 52,3 · 1915: 19,5 · 1916: 11,2 · 1917: 7,6 · 1918: 14,6 · 1919: 16,2 · 1920: 24,7
- hiúzprémek: 1900: 4 · 1901: 6,1 · 1902: 9,8 · 1903: 35,2 · 1904: 59,4 · 1905: 41,7 · 1906: 19 · 1907: 13 · 1908: 8,3 · 1909: 9,1 · 1910: 7,4 · 1911: 8 · 1912: 12,3 · 1913: 19,5 · 1914: 45,7 · 1915: 51,1 · 1916: 29,7 · 1917: 15,8 · 1918: 9,7 · 1919: 10,1 · 1920: 8,6
- ciklus hossza: 9–11 év
<!-- Az adatsor (ezer prém évente): a széles körben használt 1900–1920-as tankönyvi táblázat, amelyet a Stan példaadatai (stan-dev/example-models, hudson-bay-lynx-hare.csv, P. Howard egyetemi jegyzetéből) közölnek; eredetileg Hewitt (1921) és MacLulich (1937) feldolgozásaiból származik. Az elsődleges forrással (a Hudson's Bay Company archívumának táblázatai, Elton és Nicholson 1942) NINCS egyeztetve – ellenőrizendő. A hosszabb, kb. 1845–1935-ös sorozat (Elton és Nicholson, 1942; MacLulich, 1937) kb. 9–11 éves ciklust mutat. Becsületes megjegyzések: (1) a prémszám a vadászati erőfeszítéstől és az árától is függ; (2) Krebs és mtsai (1995, Science 269: 1112–1115) kanadai terepkísérlete szerint a nyúlciklust a táplálék ÉS a ragadozás együtt alakítja, a hiúz mellett más ragadozók (prérifarkas, nagy szarvas bagoly) is számítanak; (3) Gilpin (1973) szerint egyes évtizedekben a görbék sorrendje „fordított”, ami a prémadatok korlátaira utal. -->

## 6. Ha eltűnik a ragadozó
Mi lenne, ha kilőnénk az összes hiúzt? A nyulak ==elszaporodnak==, lerágják a növényzetet, aztán éhínség jön, és a létszám összeomlik. Tévhit, hogy a ragadozó „káros”: a gyenge egyedeket viszi el, és fékezi a zsákmányt. Próbáld ki: vedd ki, majd telepítsd vissza a hiúzokat!

> megjegyzés: Yellowstone-ban 1995–96-ban 31 farkast telepítettek vissza; hatásuk mértéke vitatott.

### Feliratok
- kérdés 6: Mi lenne a hiúzok nélkül?
- kivétel gomb: Hiúzok ki
- vissza gomb: Hiúzok vissza
- alap gomb: Eredeti
- kivették: a hiúzokat kivették
- visszatelepítették: visszatelepítették
- elszaporodnak: elszaporodnak a nyulak
- éhínség: éhínség: elfogy a növényzet
- növényzet tengely: növényzet (%)
### Adatok
- kivétel éve: 16
- visszatelepített hiúzok: 10
- növényzet növekedése: 0,69
- legelés erőssége: 0,0074
- nyulak gyarapodása növényzetből: 1,73
- nyulak pusztulása: 0,30
- vadászsiker (telítődő): 0,031
- zsákmány kezelési ideje: 0,24
- hiúzok gyarapodása (telítődő): 0,0155
- hiúzok pusztulása (telítődő): 0,42
<!-- Modellbeállítás: növényzet (V, a lehetséges maximum aránya) – nyúl (N) – hiúz (P) tápláléklánc: dV/dt = g·V·(1 − V) − q·V·N; dN/dt = N·(b·V − d) − a·N·P/(1 + a·h·N); dP/dt = c·N·P/(1 + a·h·N) − m·P. A paramétereket úgy választottuk (saját numerikus keresés), hogy hiúzokkal kb. 9–10 éves ciklus legyen, nélkülük a nyulak 2–3 év alatt kb. kétszeres–háromszoros létszámra szaporodjanak, majd a növényzet kimerülése után összeomoljanak. Didaktikus modell, nem mért adat. Yellowstone: 1995-ben 14, 1996-ban 17 farkast hoztak Kanadából (összesen 31), 1997-ben további 10-et Montanából (ellenőrizendő: National Park Service); a „trofikus kaszkád” (szarvas → fűzfa → hód) erősségéről a szakirodalom megosztott (pl. Ripple és Beschta 2012 vs. Hobbs és mtsai 2024). -->

## 7. Versengés, szimbiózis, élősködés
A ragadozás csak egy a **populációs kölcsönhatások** közül. Hogy melyikről van szó, abból látszik, ki nyer (+) és ki veszít (−). **Versengés** (− / −): ugyanazért a táplálékért vagy helyért. **Szimbiózis** (+ / +): mindkét fél nyer. **Élősködés** (+ / −): az élősködő a gazdán él, de ==ritkán öli meg==. Húzd a kártyákat a helyükre!

### Feliratok
- kérdés 7: Ki nyer, ki veszít?
- doboz pm: + / −
- doboz mm: − / −
- doboz pp: + / +
- doboz pm név: egyik nyer, másik veszít
- doboz mm név: mindkettő veszít
- doboz pp név: mindkettő nyer
- k1: hiúz és nyúl
- k1 típus: ragadozás
- k2: kullancs és őz
- k2 típus: élősködés
- k3: hiúz és róka (a nyulakért)
- k3 típus: versengés
- k4: bükk és tölgy (a fényért)
- k4 típus: versengés
- k5: gomba és alga a zuzmóban
- k5 típus: szimbiózis
- k6: méh és virág
- k6 típus: szimbiózis
- húzd: Húzd a kártyát a helyére – vagy kattints rá, majd a dobozra!
- nem jó: Nem ide – gondold át: ki nyer, ki veszít?
- kész: Mind a helyén!
- megoldás gomb: Mutasd a megoldást
- újrakezdés gomb: Újrakezdés
<!-- A méh és a virág kapcsolatát a tankönyvek kölcsönös előnyökön alapuló együttélésnek (mutualizmus, tágabb értelemben szimbiózis) nevezik; a zuzmó a klasszikus szimbiózis-példa. A kullancs vérszívó külső élősködő. A hiúz és a vörös róka ugyanazt a zsákmányt (hótalpú nyúl) eszi – táplálékért versengenek. A + / 0 kapcsolatot (pl. asztalközösség) a lecke nem tárgyalja. -->

## 8. Napi és évszakos ciklusok
Az életközösségben vannak **ismétlődő (ciklikus) változások**. Évszakos ciklus: a hótalpú nyúl ősszel fehér bundát növeszt, tavasszal barnát; nyáron születnek a kölykök, télen fogy a létszám. Napi ciklus: nappal megbújik, ==alkonyattól hajnalig táplálkozik==, a hiúz ekkor vadászik. Az **előrehaladó** változás nem tér vissza.

### Feliratok
- kérdés 8: Mi ismétlődik évről évre, napról napra?
- hónap csúszka: hónap
- hónapok: jan.; febr.; márc.; ápr.; máj.; jún.; júl.; aug.; szept.; okt.; nov.; dec.
- hó: hótakaró
- vedlés: vedlés
- kölykök: kölykök születnek
- fehér bunda: téli bunda: fehér
- barna bunda: nyári bunda: barna
- egy nap: egy nap (24 óra)
- éjszaka: éjszaka
- nyúl aktív: a nyúl táplálkozik
- hiúz aktív: a hiúz vadászik
- évközi: a nyulak száma egy éven belül
- előrehaladó: Előrehaladó változás: a felhagyott szántóból erdő lesz
- ciklikus: ciklikus
### Adatok
- születések kezdete: 4
- születések vége: 8
- hótakaró kezdete: 11
- hótakaró vége: 4
<!-- Hónapok sorszámmal (1 = január). Hótalpú nyúl (Lepus americanus): évente kétszer vedlik; a vedlést a nappalok hossza indítja el, nem a hó (Mills és mtsai 2013, PNAS 110: 7360–7365 – a rövidülő hótakaró miatt egyre több fehér nyúl ül barna talajon). Szaporodási időszak kb. márciustól augusztusig, a kölykök kb. április–augusztus között születnek, évente 2–4 alom (ellenőrizendő; a hótakaró és a szaporodás időzítése földrajzi helytől függ). Napi aktivitás: a hótalpú nyúl főként éjszaka és szürkületkor aktív, a kanadai hiúz is főként éjjel és szürkületkor vadászik. Az évközi létszámgörbe a vásznon vázlat (nem mért adat). -->

## 9. Összefoglalás
- Korlátlanul egy populáció **exponenciálisan** nőne; a valóságban az **eltartóképesség** megállítja.
- A ragadozó és a zsákmány létszáma ==késve követi egymást==, ezért ingadozik.
- A prémadatok kb. tízéves ciklust mutatnak – a modell egyszerűsít.
- A kölcsönhatás típusa abból látszik, ki nyer és ki veszít.
- Vannak napi és évszakos ciklusok is.

### Feliratok
- összegzés cím: Amit megtanultunk
- ö1: J és S: korlátlan és korlátozott
- ö2: körbe-körbe: ragadozó és zsákmány
- ö3: + és −: kölcsönhatások
- ö4: a prémek tanúsága
- ö ragadozás: ragadozás, élősködés
- ö versengés: versengés
- ö szimbiózis: szimbiózis

<!-- Vitatott / bizonytalan pontok:
- A Hudson's Bay Company-adatsor (1900–1920) másodlagos forrásból (Stan-példaadat, Howard jegyzete) van; az elsődleges táblázattal (Elton és Nicholson 1942; MacLulich 1937; Hewitt 1921) egyeztetni kell. A prémszám nem létszám.
- A nyúl–hiúz ciklus oka: a ragadozás mellett a táplálék és más ragadozók is számítanak (Krebs és mtsai 1995). A Lotka–Volterra-modell ezt nem tartalmazza; a lecke ezt a 5. lépésben kimondja.
- A 3. lépés ágensalapú szimulációja és a 6. lépés táplálékláncmodellje didaktikus, a paraméterek nem mért értékek.
- Yellowstone: a visszatelepítés száma (31 farkas, 1995–96) ellenőrizendő (National Park Service); a hatás (trofikus kaszkád) erőssége vitatott.
- A hótalpú nyúl szaporodási időszaka és vedlése helyfüggő; a lecke kerek hónapokat használ.
- A „szimbiózis” szót a lecke a kölcsönösen előnyös együttélésre használja (a magyar tankönyvek többsége így); szakirodalomban a mutualizmus a pontosabb név.
-->
