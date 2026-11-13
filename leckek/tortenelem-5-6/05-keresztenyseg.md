# Hogyan terjedt el egy új hit a Római Birodalomban? – a Biblia és a kereszténység
tantárgy: Történelem · évfolyam: 5–6. · témakör: 3. A kereszténység

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/tortenelem-5-6/05-keresztenyseg.md

  Kerettanterv (kerettanterv/tortenelem/5-6.md, 3. témakör), szó szerint:
  „Az Ószövetség/Héber Biblia: Ábrahám és Mózes.” · „Az önálló zsidó állam alapítói: Dávid és
  Salamon története.” · „Jézus élete legfontosabb eseményeinek bemutatása.” · „A kereszténység fő
  jellemzőinek és elterjedésének bemutatása.” · „A Héber Biblia máig ható innovációi: egyistenhit,
  tízparancsolat, heti pihenőnap” · „A kereszténység elterjedése.” · „A keresztény hitélet
  színterei és szertartásai.” · „A kereszténység jelképei.” · „Pál apostol missziós útjainak
  követése tematikus térképen.” · Fogalmak: „egyistenhit, Biblia, Ószövetség/Héber Biblia,
  Újszövetség, zsidó vallás, keresztény vallás, keresztség és úrvacsora”. · Topográfia:
  „Jeruzsálem, Betlehem”.

  Szerkesztői elv (pilot/tortenelem-5-6/terv.md, 4. fejezet, 9. pont): a hitbeli tartalom leíró
  keretben szerepel („a Biblia szerint”, „a keresztények hite szerint”). A lecke nem térít és nem
  cáfol: azt mutatja meg, mit hittek és mit tanítottak, és honnan tudjuk.

  Formátum-megjegyzések:
  – Minden évszám, helyszín (koordináta) és arány az ### Adatok alatt van; a térkép és az
    idővonalak ezekből rajzolnak. A „körül” / „kb.” jelölésű érték becslés.
  – A „becslés” bélyeget a kód akkor is kiteszi, ha egy tartomány maga a bizonytalanság
    (Jézus születése és kereszthalála, Pál útjainak évei, az Ó- és Újszövetség keletkezése).
  – Az útvonalak (Ábrahám, Mózes, Pál útjai, a levél útja) töréspontjai a kódban vannak,
    VÁZLATOSAN: a megnevezett városok koordinátája itt javítható, a közbülső kanyar nem.
  – A keresztény közösségek foltjai (100, 300, 400 körül) vázlatok a kódban; a három évszám itt
    javítható.
  – A háromféle jelölés: forrás (kékeszöld keret), rekonstrukció (szaggatott keret), hagyomány
    (okker kartus). A Héber Biblia elbeszéléseit (Ábrahám, Mózes) „hagyomány” jelöli: ezeket a
    Biblián kívüli forrás nem erősíti meg, és a vallásos hagyomány szent története.
  – Feliratban a # jel helyére a lecke számot ír (pl. „# km”).
  – Térképadat: Made with Natural Earth (naturalearthdata.com, közkincs). A partok és folyók a mai
    állapotot mutatják.

  Vitatott / bizonytalan pontok (tanári és szakmai review-hoz):
  – Ábrahám és Mózes: a Héber Biblia elbeszélései. Történetiségüket Biblián kívüli forrás nem
    igazolja; a kutatók többsége a hagyomány késői lejegyzésével számol. A lecke „a Biblia
    szerint” mutatja be, évszám nélkül. Az útvonalak vázlatosak: Ur helye a hagyományos azonosítás
    (Tell el-Muqajjar), a Sínai-hegy a hagyományos Dzsebel Musza; a kivonulás útja és a
    tengeri átkelés helye vitatott.
  – Dávid kora: a hagyományos időrend szerint kb. Kr. e. 1010–970 (Salamon kb. Kr. e. 970–931).
    A régészek vitatják, mekkora volt akkor Jeruzsálem és a királyság.
  – Tel Dan-i felirat: 1993–94-ben került elő; arámi nyelvű, kb. Kr. e. 9. század második fele
    (kb. Kr. e. 840–800). A „bjtdwd” szót a kutatók többsége „Dávid házának” olvassa; néhányan
    vitatják.
  – A tízparancsolat számozása a hagyományokban eltér (zsidó, katolikus–evangélikus,
    református–ortodox), ezért a lecke csak hat parancsot idéz, számozás nélkül.
  – A heti pihenőnap: a zsidóknál a szombat (sabbat), a keresztényeknél kb. a 2. századtól a
    vasárnap (az „Úr napja”, Jézus feltámadásának napja); Constantinus 321-ben rendelte el a
    vasárnapi munkaszünetet. A „szombat” szavunk szláv közvetítéssel a héber „sabbat” szóból ered.
    Egy év 52 hét és 1 (szökőévben 2) nap, ezért 52 vagy 53 pihenőnap jut rá.
  – Jézus születése: a történészek szerint kb. Kr. e. 7–4 (Nagy Heródes Kr. e. 4-ben halt meg;
    lásd a 01-idoszamitas leckét). A betlehemi születést Máté és Lukács evangéliuma írja le.
  – Kereszthalál: Poncius Pilátus júdeai helytartósága (26–36) alatt; a legtöbb kutató 30-ra vagy
    33-ra teszi (becslés). Ezt nem keresztény forrás is említi (Tacitus, Évkönyvek 15.44).
  – Az Ószövetség keletkezése: a lecke a történészek becslését mutatja (a legrégebbi részek
    hagyománya kb. Kr. e. 1000 körüli, a legkésőbbi könyvek kb. Kr. e. 2. századiak); a
    vallási hagyományok egy része korábbra teszi. A könyvek száma felekezetenként más: a zsidó
    hagyomány ugyanezt a szöveget 24 könyvnek számolja, a protestáns Biblia 39, a katolikus 46
    könyvet tartalmaz. Az Újszövetség 27 könyve minden nagy egyházban azonos.
  – Pál levelei: a legkorábbi (1Thessz) kb. 50–51, a Rómaiakhoz írt levél kb. 56–57 (Korinthosz).
    Az evangéliumok: Márk kb. 65–70, Máté és Lukács kb. 80–90, János kb. 90–100 (becslés). Hogy
    Márk Péter kísérője volt, az 2. századi hagyomány (Papiasz).
  – Fordítások: Septuaginta – a Tóra görög fordítása kb. Kr. e. 3. század közepe, a többi könyv a
    Kr. e. 2–1. században; Vulgata – Szent Jeromos, kb. 382–405; Vizsolyi Biblia – Károli Gáspár,
    1590, az első teljes, nyomtatott magyar Biblia (részleges magyar fordítások korábban is
    voltak, pl. a 15. századi „Huszita Biblia”).
  – Pál útjai (az Apostolok cselekedetei alapján): az évszámok rekonstrukciók, a kézikönyvek 1–2
    évvel eltérnek (pl. 1. út 46–48 vagy 47–48; 3. út 53–57 vagy 54–58; a római út 59–60 vagy
    60–61). Az útvonalak vázlatosak.
  – Utazási sebesség: gyalog kb. 25–35 km/nap, kereskedelmi hajóval kedvező szélben kb. 100–150
    km/nap (becslés; L. Casson, Ships and Seamanship in the Ancient World). Télen (kb. novembertől
    márciusig) a nyílt tengeri hajózás nagyrészt szünetelt. A szárazföldi út az Adriai-tengeren
    egy rövid hajós átkelést is tartalmaz (Dyrrhachium – Brundisium). A napok száma a lecke saját
    vázlatos útvonalából számolt, kerekített érték.
  – Üldözések: Néró 64-ben (Róma tűzvésze után, csak Rómában); Decius 250–251 és Valerianus
    257–260 (birodalmi rendelet); a „nagy üldözés” Diocletianus alatt 303-tól; Galerius 311-es
    türelmi rendelete keleten nagyrészt véget vetett neki (Maximinus Daia 313-ig folytatta).
    Közben voltak helyi zaklatások is (pl. Lugdunum, 177). A hagyomány szerint Péter és Pál
    Rómában halt vértanúhalált, Néró idején.
  – 313: Constantinus és Licinius megállapodása (a „milánói rendelet” a hagyományos név; a szöveg
    Licinius 313. júniusi nikomédiai rendeletéből ismert). Minden vallásnak szabadságot adott,
    nem tette államvallássá a kereszténységet.
  – 380. február 27.: Theodosius thesszalonikéi rendelete (Cunctos populos) a niceai hitvallást
    tette kötelezővé; a régi kultuszokat 391–392-ben tiltották be.
  – A keresztények aránya 300 körül kb. 10 % (becslés; K. Hopkins, R. Stark): a becslések kb.
    5–10 % között szórnak.
  – A közösségek foltjai: emlékezetből, általános tankönyvi tudás alapján rajzolt, erősen
    egyszerűsített vázlatok (100 körül: az Újszövetségben és a korai forrásokban említett
    városok; 300 körül: Kis-Ázsia, Szíria, Egyiptom, Észak-Afrika, Itália sűrűbben; 400 körül:
    a birodalom nagy része). Legalább két mainstream atlasszal egyeztetendő – ez még NEM történt
    meg.
  – Sopianae (Pécs): ókeresztény temető, sírkamrák a 4. századból (főleg a második feléből);
    2000 óta a világörökség része.
  – Jelképek: az IKHTHÜSZ (hal) betűszó a 2–3. századtól ismert; a Krisztus-monogram (Kh–R)
    Constantinus korától terjedt el; a kereszt mint általános jelkép főleg a 4. századtól.
-->

## Közös

### Feliratok
- forrás jel: forrás
- rekonstrukció jel: rekonstrukció
- monda jel: hagyomány
- becslés: becslés
- vázlatos: vázlatos
- illusztráció: illusztráció
- Kr. e.: Kr. e.
- Kr. u.: Kr. u.
- század: század
- év sablon: # év
- lépték: # km
- Jeruzsálem: Jeruzsálem
- Róma: Róma
- Földközi-tenger: Földközi-tenger

### Adatok
- Jeruzsálem helye: 31,778° É, 35,235° K
- Róma helye: 41,892° É, 12,486° K
<!-- A kereszthalál éve: a kutatók többsége 30-ra vagy 33-ra teszi (becslés). -->
- kereszthalál, legkorábban: 30
- kereszthalál, legkésőbb: 33

## 1. Egy nép, egy Isten
A környező népek **sok istent** imádtak. A zsidók ==egyetlen Istenben hittek==: ez az **egyistenhit**.

A Héber Biblia szerint ősük, **Ábrahám** Urból költözött Kánaánba. **Mózes** Egyiptomból vezette ki népét. Később **Dávid** és **Salamon** király Jeruzsálemből uralkodott. Válassz egy történetet!

### Feliratok
- Egyiptom: Egyiptom
- Mezopotámia: Mezopotámia
- Kánaán: Kánaán
- Nílus: Nílus
- Eufrátesz: Eufrátesz
- Ur: Ur
- Hárán: Hárán
- Sínai-hegy: Sínai-hegy
- sok isten: sok isten
- egyiptomi istenek: Ré · Ozirisz · Ízisz · Hórusz
- mezopotámiai istenek: Marduk · Istár · Enlil · Samas
- egy Isten: egy Isten
- egy Isten alcím: a zsidók hite: egyistenhit
- Jeruzsálem alcím: Dávid és Salamon fővárosa
- kártya biblia cím: A Héber Biblia elbeszélése
- kártya Ábrahám: Ábrahám: Urból Kánaánba
- kártya Mózes: Mózes: ki Egyiptomból, a Sínai-hegyen át
- kártya Dávid: Dávid és Salamon: Jeruzsálem
- gomb Ábrahám: Ábrahám
- gomb Mózes: Mózes
- gomb Dávid: Dávid és Salamon
- gomb mind: Mind

### Adatok
<!-- Ur: Tell el-Muqajjar (hagyományos azonosítás). Hárán: a mai Harran. Gósen: a Nílus-delta
     keleti része (a Biblia szerint itt éltek Egyiptomban). Sínai-hegy: a hagyományos Dzsebel Musza.
     Az Egyiptom, Mezopotámia és Kánaán pont a tájnév felirat helye. -->
- Ur helye: 30,962° É, 46,103° K
- Hárán helye: 36,865° É, 39,031° K
- Gósen helye: 30,60° É, 31,90° K
- Sínai-hegy helye: 28,539° É, 33,975° K
- Kánaán helye: 32,40° É, 35,50° K
- Egyiptom helye: 27,60° É, 30,20° K
- Mezopotámia helye: 33,60° É, 43,40° K
<!-- Dávid uralkodása a hagyományos időrend szerint kb. Kr. e. 1010–970. -->
- Dávid kora: Kr. e. 1000 körül

## 2. Tízparancsolat és pihenőnap
A Biblia szerint Mózes a Sínai-hegyen kapta a **tízparancsolatot**: tíz szabályt Istenről és az emberek együttéléséről.

Az egyik: ==minden hetedik nap pihenőnap.== A **szombat** szavunk is a héber *sabbat* (pihenés) szóból ered. Húzd a csúszkát: hány pihenőnap jut egy évre?

### Feliratok
- tábla cím: A Biblia szerint – néhány a tíz közül:
- parancs 1: Ne legyenek más isteneid!
- parancs 2: Szenteld meg a pihenőnapot!
- parancs 3: Tiszteld apádat és anyádat!
- parancs 4: Ne ölj!
- parancs 5: Ne lopj!
- parancs 6: Ne tanúskodj hamisan!
- tábla megjegyzés: Mózes a Sínai-hegyen kapta
- év cím: Egy év, hétről hétre
- napok rövid: H, K, Sze, Cs, P, Szo, V
- szombat felirat: zsidó pihenőnap: szombat
- vasárnap felirat: keresztény pihenőnap: vasárnap
- sabbat: szombat ← héber „sabbat” = pihenés
- csúszka hét: Hány hét telt el?
- hét sablon: # hét
- pihenőnap sablon: # pihenőnap
- hétnyi pihenés: ez összesen kb. # hétnyi pihenés!

### Adatok
- napok egy héten: 7 nap
- hetek egy évben: 52 hét

## 3. Jézus élete
A keresztények hite szerint **Jézus** Isten Fia. **Betlehemben** született, **Názáretben** nőtt fel. Galileában tanított: ==„Szeresd felebarátodat, mint önmagadat!”==

Jeruzsálemben Poncius Pilátus római helytartó keresztre feszíttette, kb. Kr. u. {kereszthalál, legkorábban}–{kereszthalál, legkésőbb} között. Követői hite szerint harmadnap **feltámadt**.

### Feliratok
- Betlehem: Betlehem
- Názáret: Názáret
- Kafarnaum: Kafarnaum
- Galilea: GALILEA
- Szamária: SZAMÁRIA
- Júdea: JÚDEA
- Jordán: Jordán
- Galileai-tó: Galileai-tó
- Holt-tenger: Holt-tenger
- út kártya cím: Az evangéliumok szerint
- állomás 1: Betlehem: itt született
- állomás 1 alatt: szülei: Mária és József
- állomás 2: Názáret: itt nőtt fel
- állomás 3: Galilea: tanított, tanítványokat hívott
- állomás 4: Jeruzsálem: kereszthalál
- állomás 4 alatt: a keresztények hite szerint feltámadt
- idővonal születés: születése
- idővonal kereszthalál: kereszthalál
- idővonal Pilátus: Poncius Pilátus helytartó

### Adatok
- Betlehem helye: 31,705° É, 35,200° K
- Názáret helye: 32,699° É, 35,304° K
- Kafarnaum helye: 32,881° É, 35,575° K
- Jerikó helye: 31,857° É, 35,444° K
- Galilea helye: 32,95° É, 35,10° K
- Szamária helye: 32,25° É, 35,05° K
- Júdea helye: 31,45° É, 34,95° K
<!-- A történészek szerint kb. Kr. e. 7–4 (lásd a 01-idoszamitas leckét). -->
- Jézus születése, legkorábban: Kr. e. 7
- Jézus születése, legkésőbb: Kr. e. 4
- Pilátus helytartósága, kezdete: 26
- Pilátus helytartósága, vége: 36

## 4. Nem egy könyv: egy egész könyvtár
==Tévhit, hogy a Biblia egyetlen, egyszerre írt könyv.== Sok szerző írta, sok száz év alatt.

Két része van. Az **Ószövetség** (Héber Biblia) a zsidók és a keresztények közös szent irata. Az **Újszövetség** Jézusról és követőiről szól, görögül írták. Később **lefordították** latinra, majd magyarra is.

### Feliratok
- tévhit 4: Tévhit: a Biblia egyetlen, egyszerre írt könyv.
- valóság 4: Valóság: sok könyv, sok szerző, kb. # év.
- ószövetség cím: Ószövetség (Héber Biblia)
- ószövetség alcím: {ószövetségi könyvek száma} · héberül
- felekezet: a felekezetek másként számolják
- újszövetség cím: Újszövetség
- újszövetség alcím: {újszövetségi könyvek száma} · görögül
- tl ószövetség: az Ószövetség írása
- tl újszövetség: az Újszövetség írása
- tl Septuaginta: Septuaginta
- tl Septuaginta alatt: görög fordítás
- tl Vulgata: Vulgata
- tl Vulgata alatt: latin fordítás (Jeromos)
- tl Vizsoly: Vizsolyi Biblia
- tl Vizsoly alatt: Károli Gáspár magyar fordítása

### Adatok
- Ószövetség írása, kezdete: Kr. e. 1000 körül
- Ószövetség írása, vége: Kr. e. 150 körül
- Pál levelei, kezdete: 50
- Pál levelei, vége: 60
- evangéliumok, kezdete: 70
- evangéliumok, vége: 100
- Septuaginta: Kr. e. 250 körül
- Vulgata: 400 körül
- Vizsolyi Biblia: 1590
<!-- A protestáns Biblia 39, a katolikus 46 ószövetségi könyvet tartalmaz. -->
- ószövetségi könyvek száma: 39–46 könyv
- újszövetségi könyvek száma: 27 könyv

## 5. Honnan tudjuk?
A legrégebbi keresztény írások **Pál levelei**, Kr. u. {Pál levelei, kezdete} körülről. Az evangéliumok később születtek.

Nem keresztény szerző is ír Jézusról: a római **Tacitus**. Egy kőfelirat pedig Dávid házát említi. ==Kattints: ki írta, és hány évvel később?==

### Feliratok
- gomb Tel Dan: Tel Dan-i felirat
- gomb Pál: Pál levelei
- gomb Márk: Márk evangéliuma
- gomb Tacitus: Tacitus
- ki írta címke: Ki írta?
- mit mond címke: Mit mond?
- szemtanú címke: Szemtanú?
- hány év később: # évvel később
- esemény Dávid: Dávid uralkodása
- esemény kereszthalál: Jézus kereszthalála
- td típus: régészeti lelet · kőfelirat
- td cím: A Tel Dan-i felirat
- td ki: egy szomszédos, arámi király
- td mit: „Dávid házát”, vagyis Dávid utódait említi
- td szemtanú: nem: Dávid után több nemzedékkel
- td keletkezés: a felirat
- pál típus: írott forrás · levél
- pál cím: Pál apostol levelei
- pál ki: Pál, aki Jézus halála után lett keresztény
- pál mit: Jézus haláláról, feltámadásáról és tanításáról ír
- pál szemtanú: Jézust nem ismerte, de Péterrel találkozott
- pál keletkezés: az első levél
- márk típus: írott forrás · evangélium
- márk cím: Márk evangéliuma
- márk ki: a hagyomány szerint Márk, Péter kísérője
- márk mit: Jézus tanítását, halálát és feltámadását mondja el
- márk szemtanú: nem: a tanítványok elbeszéléseit írta le
- márk keletkezés: az evangélium
- tac típus: írott forrás · római történetírás
- tac cím: Tacitus: Évkönyvek
- tac ki: Tacitus római történetíró – nem keresztény
- tac mit: Krisztust Pilátus kivégeztette, Néró üldözte a keresztényeket
- tac szemtanú: nem: két nemzedékkel később írt
- tac keletkezés: az Évkönyvek
- oszlop cím: Hány évvel az esemény után írták le?

### Adatok
<!-- A hagyományos időrend szerint. -->
- Dávid uralkodása, kezdete: Kr. e. 1010
- Dávid uralkodása, vége: Kr. e. 970
- Tel Dan-i felirat: Kr. e. 840 körül
- Márk evangéliuma: 70 körül
- Tacitus Évkönyvei: 116 körül

## 6. Pál útjai
**Pál apostol** (apostol = küldött) kb. {1. út kezdete} és {3. út vége} között három nagy utat tett. Városról városra járt, és **gyülekezeteket** (közösségeket) alapított.

Leveleivel tartotta a kapcsolatot. ==Római utakon és hajókon gyorsan lehetett utazni.== Hány nap alatt ért Rómába egy levél?

### Feliratok
- Antiochia: Antiochia
- Tarzusz: Tarzusz
- Ikónium: Ikónium
- Efezus: Efezus
- Troász: Troász
- Filippi: Filippi
- Thesszaloniké: Thesszaloniké
- Athén: Athén
- Korinthosz: Korinthosz
- Cézárea: Cézárea
- Málta: Málta
- Ciprus: Ciprus
- Kréta: Kréta
- út 1: 1. út
- út 2: 2. út
- út 3: 3. út
- út Róma: út Rómába, fogolyként
- csúszka év 6: Év
- levél cím: Levél Korinthoszból Rómába
- levél tenger: hajón:
- levél szárazföld: gyalog, szárazföldön:
- nap sablon: kb. # nap
- km sablon: # km
- levél súgó: Pál innen írt a rómaiaknak, {Rómaiakhoz írt levél} körül
- tél: télen nem hajóztak a nyílt tengeren
- gomb tenger: Levél hajón
- gomb szárazföld: Levél gyalog

### Adatok
<!-- Az Apostolok cselekedetei alapján rekonstruált évek (becslés; a kézikönyvek 1–2 évvel eltérnek). -->
- 1. út kezdete: 46
- 1. út vége: 48
- 2. út kezdete: 49
- 2. út vége: 52
- 3. út kezdete: 53
- 3. út vége: 57
- római út kezdete: 59
- római út vége: 60
- Rómaiakhoz írt levél: 57
- Antiochia helye: 36,202° É, 36,160° K
- Tarzusz helye: 36,918° É, 34,895° K
- Ikónium helye: 37,871° É, 32,485° K
- Efezus helye: 37,941° É, 27,342° K
- Troász helye: 39,752° É, 26,159° K
- Filippi helye: 41,013° É, 24,286° K
- Thesszaloniké helye: 40,640° É, 22,944° K
- Athén helye: 37,972° É, 23,726° K
- Korinthosz helye: 37,906° É, 22,879° K
- Cézárea helye: 32,500° É, 34,892° K
- Málta helye: 35,947° É, 14,400° K
- Ciprus helye: 35,05° É, 33,20° K
- Kréta helye: 35,22° É, 24,90° K
<!-- Becslés (L. Casson): gyalog kb. 25–35 km/nap; kereskedelmi hajó kedvező szélben kb. 100–150 km/nap. -->
- gyalog egy nap alatt: 30 km
- hajón egy nap alatt: 100–150 km

## 7. Üldözött kisebbségből államvallás
==Tévhit, hogy mindig üldözték őket.== Az üldözés **hullámokban** jött: Néró ({Néró üldözése}, csak Rómában), Decius, Diocletianus ({nagy üldözés, kezdete}–{nagy üldözés, vége}). Közben a gyülekezetek nőttek.

{milánói rendelet}: **szabad vallás** lett. {Theodosius rendelete}: **államvallás**. Ehhez évszázadok kellettek. Húzd a csúszkát!

### Feliratok
- Alexandria: Alexandria
- Karthágó: Karthágó
- Lugdunum: Lugdunum
- Lugdunum alcím: ma Lyon
- Milánó: Milánó
- Milánó alcím: {milánói rendelet}: szabad vallás
- Thesszaloniké alcím: {Theodosius rendelete}: államvallás
- Sopianae: Sopianae
- Sopianae alcím: ma Pécs · ókeresztény temető, #
- Római Birodalom: RÓMAI BIRODALOM
- csúszka év 7: Év
- állapot tiltott: nem engedélyezett vallás
- állapot Róma: üldözés Rómában
- állapot üldözés: üldözés a birodalomban
- állapot szabad: szabad vallás, egy a sok közül
- állapot állam: államvallás
- évvel Jézus után: # évvel Jézus halála után
- üldözés Néró: Néró
- üldözés Decius: Decius, Valerianus
- üldözés Diocletianus: Diocletianus
- esemény Milánó: milánói rendelet
- esemény Theodosius: Theodosius rendelete
- arány: {gyülekezetek 2. kép} körül: a lakosság {keresztények aránya 300 körül}-a
- közösségek jel: keresztény közösségek

### Adatok
- gyülekezetek 1. kép: 100
- gyülekezetek 2. kép: 300
- gyülekezetek 3. kép: 400
- Néró üldözése: 64
- Decius üldözése, kezdete: 250
- Decius üldözése, vége: 251
- Valerianus üldözése, kezdete: 257
- Valerianus üldözése, vége: 260
- nagy üldözés, kezdete: 303
- nagy üldözés, vége: 311
- milánói rendelet: 313
- Theodosius rendelete: 380
<!-- Becslés (K. Hopkins, R. Stark): kb. 5–10 %. -->
- keresztények aránya 300 körül: kb. 10 %
<!-- Pécs, ókeresztény temető: 4. század (főleg a második fele). -->
- Sopianae temetője: 350 körül
- Alexandria helye: 31,200° É, 29,918° K
- Karthágó helye: 36,853° É, 10,323° K
- Lugdunum helye: 45,760° É, 4,835° K
- Milánó helye: 45,464° É, 9,190° K
- Sopianae helye: 46,072° É, 18,233° K

## 8. Jelképek
Az első keresztények **jelképekkel** is kifejezték hitüket: falfestményeken, sírokon, edényeken. Legfontosabb szertartásaik: a **keresztség** (belépés a közösségbe) és az **úrvacsora** (Jézus utolsó vacsorájának emléke). ==Húzd a jelentéseket a jelképekhez!==

### Feliratok
- zóna hal: hal
- zóna hal alatt: görögül: IKHTHÜSZ
- zóna kereszt: kereszt
- zóna kereszt alatt: a leggyakoribb jelkép
- zóna khírhó: Krisztus-monogram
- zóna khírhó alatt: görög betűk: Kh és R
- zóna alfaómega: alfa és ómega
- zóna alfaómega alatt: görög betűk: A és Ó
- zóna kehely: kenyér és bor
- zóna kehely alatt: kehely és kenyér
- zóna víz: víz
- zóna víz alatt: keresztelőmedence
- alfa: Α
- ómega: Ω
- kártya hal: „Jézus Krisztus, Isten Fia, Megváltó”
- kártya kereszt: Jézus kereszthalálára emlékeztet
- kártya khírhó: Krisztus nevének első két betűje
- kártya alfaómega: kezdet és vég: első és utolsó betű
- kártya kehely: úrvacsora: az utolsó vacsora emléke
- kártya víz: keresztség: belépés a közösségbe
- tálca súgó: Húzd a jelentéseket a jelképekhez!
- pontszám: # / # jó helyen
- kész: Ügyes! Minden a helyén.
- gomb megoldás: Megoldás
- gomb újra: Újra

## 9. Összefoglalás
- Az **egyistenhit** és a tízparancsolat a Héber Bibliából ered.
- Jézus követői, főleg **Pál**, a birodalom útjain vitték tovább a hitet.
- ==Üldözött kisebbségből {Theodosius rendelete}-ra államvallás lett.==
- Máig hat: a Biblia és a **heti pihenőnap**.

### Feliratok
- összefoglaló cím: A kereszténység útja
- ö1 cím: egy Isten
- ö1 sor: a Héber Biblia népe
- ö2 cím: Jézus
- ö2 sor: kereszthalál
- ö3 cím: Pál útjai
- ö3 sor: gyülekezetek a birodalomban
- ö4 cím: üldözések
- ö4 sor: hullámokban, nem mindig
- ö5 cím: milánói rendelet
- ö5 sor: szabad vallás
- ö6 cím: Theodosius
- ö6 sor: államvallás
- máig hat: Máig hat:
- máig 1: egyistenhit
- máig 2: tízparancsolat
- máig 3: heti pihenőnap
- máig 4: a Biblia
