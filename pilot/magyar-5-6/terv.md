# Pilot: Magyar nyelv és irodalom 5–6. – a leckesor terve

Forrás: [`kerettanterv/magyar-nyelv-es-irodalom/5-6.md`](../../kerettanterv/magyar-nyelv-es-irodalom/5-6.md)
(NAT 2020, általános iskola, 18 témakör, 216 óra + 2 × 28 óra szabad keret = 272 óra). Az
idézetek szó szerint onnan valók, a forrás elírásaival együtt. A lecke-formátum leírása:
[`leckek/SZERZODES.md`](../../leckek/SZERZODES.md). A tárgyra vonatkozó kiegészítő szabályok
kész szövegként a 7. fejezetben vannak.

> **A forrás sajátossága.** Az 5–6. évfolyamos magyar kerettantervben **nincs „Tanulási
> eredmények” rész** (a 3–4.-esben van). Témakörönként csak a „Fejlesztési feladatok és
> ismeretek” és a „Fogalmak” szerepel, ezek mellett a tananyagtartalom-táblázat sorolja fel a
> nyelvtani altémákat és a kötelező műveket. A briefek „Kerettanterv” sora ezért ezekből idéz.

## 0. Döntések a felhasználó távollétében

A felhasználó nem volt elérhető, ezért ezekben magam döntöttem. Mind visszavonható.

1. **17 lecke a „kb. 16” helyett: 8 nyelvtan- és 9 irodalomlecke.** Az irodalom óraszáma
   nagyobb (108 óra, szemben a nyelvtan animálható 91 órájával), és öt kötelező nagy műve van.
   Egy lecke elhagyásával egy egész témakör (Szülőföld, táj) maradt volna ki.
2. **A 3. és az 5. témakör egy leckében.** Az állandósult szókapcsolatok (5 óra) és a hangalak
   és jelentés (6 óra) közös leckébe kerül (`06`). A közös gondolat: a hangtól a jelentésig, majd
   az átvitt jelentésig jutunk.
3. **Az időmértékes verselés tartalékba kerül** (1. tartalék), pedig a 14. témakör fogalmai
   között szerepel. A 14-es lecke a balladára épül, mert a „Hősök” kötelező szövegei (*Mátyás
   anyja*, *A walesi bárdok*) balladák. Az időmérték-lecke kész brieffel szerepel a 6. fejezetben.
4. **Régi helyesírás az idézetekben.** A közkincs szövegek a forráskiadás írásmódjával
   jelennek meg (pl. *Kukoricza Jancsi*, *Taljánország*, *kislyány*), modernizálás nélkül. Ahol
   ez feltűnő, egy „régi írásmód” bélyeg jelzi. A modernizált iskolai kiadások szövegét nem
   vesszük át, mert a modernizálás szerkesztői döntés, amelyet nem tudunk ellenőrizni. Ez a
   kerettanterv saját célját is szolgálja: „A nyelv változó természetének megfigyelése”.
5. **Nincs gépi felolvasás, és nincs felvett emberi hang.** A hang **szintetizált** (Web Audio):
   dúdolt dallam, magánhangzó, kopogás. Szöveget nem olvas fel, és nem utánoz élő embert. A
   lecke hang nélkül is teljes; a hang kiegészítés (részletek: 4. fejezet, `MagHang`).
6. **A közkincs szövegek forrása a MEK és a magyar Wikiszótár / Wikisource.** A *János vitéz*
   a MEK 01010 számú szövege. A *Toldi*, a *Himnusz*, a *Szózat*, *Az alföld*, *A walesi
   bárdok*, a *Családi kör*, a *Mátyás anyja* és a *Huszt* a hu.wikisource.org-ról való. Mindet
   letöltöttem és ellenőriztem: szótagszám, versszakszám, idézett sorok. A szöveg közkincs, de a
   gyártó ügynök minden idézett sort vessen össze egy második kiadással is (7. fejezet).
7. **A nyelvtani példák saját mondatok, az értelmetlen szavak saját alkotások** (`07`). Ezeket
   a tanári review-n egy második ember is nézze át, nehogy véletlenül létező, durva vagy
   csúfolódó szóra hasonlítsanak.

## 1. Bevezető

**A kulcskérdés:** hol ad egy interaktív, animált lecke *valódi* belátást a nyelvtanban és az
irodalomban, amit a tábla vagy a könyv nem tud megadni? Hét helyzetet látunk:

1. **A láthatatlan nyelvi mozgás láthatóvá tétele.** A beszédhang a szájban születik, ott,
   ahova nem látunk be. A zönge, a nyelv helye és a „lusta száj” (a hasonulás oka) animált
   metszeten látszik. A diák maga mozgatja a nyelvet, és **hallja**, hogyan lesz az *á*-ból
   *é*.
2. **A szó mint építőkocka.** A magyar szó toldalékláncából (tő + képző + jel + rag) a tábla
   csak egy kész alakot mutat. Itt a darabok összeállnak, és a toldalék „kaméleonként”
   alakot vált (*-ban/-ben*, *-hoz/-hez/-höz*), amikor a tőhöz ér. A szabály így a szemünk előtt
   működik.
3. **A rendszer mint gép.** A nyelv szabálya algoritmus: illeszkedés, betűrend, -tja/-tsa,
   szótagszám. Ha a diák bármit beállít, a gép azonnal megmutatja az eredményt és a szabályt is,
   amely szerint dönt. Az *ige vezérlőpultján* például 52 rubrika telik meg.
4. **A vers mint zene.** Az ütemet, a szótagszámot és a rímet a könyv jelekkel írja le.
   Itt a szótagok kigyulladnak, a sor közepén megáll a hang, a diák kopog az ütemre (és a gép
   méri a pontosságát), a rímpárok egy színt kapnak. A *János vitéz* 1480 sorából a lecke
   kimutatja, hány nem tizenkét szótagos.
5. **A történet mint tér és idő.** Az epikai mű térképe és íve: a *Pál utcai fiúk* grundja és
   a csata menete, *János vitéz* útja (Indiától Franciaországig – „határosak”!), az *Egri
   csillagok* húsz évet átfogó szálai, egy tárgy (zászló, gyűrű) útja a szereplők között, a
   cselekmény szerkezete görbeként. A kerettanterv maga is kéri: „A cselekmény és térszerkezet
   vizuális megjelenítése analóg vagy digitális médiumban” (12.), „A szereplők közötti
   kapcsolatok vizuális megjelenítése analóg vagy digitális médiumban” (17.).
6. **A kép a szövegben.** A szókép átváltozás: a *Toldi* kútgémje „óriás szunyog” lesz, a
   szöcskék „nyájként” legelnek, a lóláb tényleg kilóg. A szó szerinti és az átvitt jelentés
   között a diák egy kapcsolóval vált.
7. **Forrás, átírás, olvasat.** Honnan vette Arany a Toldit (Ilosvai, 1574)? Mi monda *A walesi
   bárdokban*? (Arany saját lábjegyzete szerint: „A történelem kétségbe vonja, de a mondában
   erősen tartja magát…”.) A forrás és az átírás rétegei ki-be kapcsolhatók, akárcsak a
   történelemleckék „Honnan tudjuk?” lépésében. Ahol az olvasat értelmezés kérdése, ott a lecke
   **több olvasatot** mutat, és nyitott kérdéssel zár.

**Kihagyjuk**, amiből csak illusztrált szöveg vagy feladatlap lenne, és ami tanórai
tevékenység:

- a szövegalkotási gyakorlatokat (6. témakör, 13 óra: felelet, vázlat, levél, plakát,
  meghívó, jellemzés);
- a könyvtár- és múzeumlátogatást (7. témakör, 4 óra – maga a kerettanterv írja: „Elméleti
  tananyag helyett gyakorlati feladatokat javaslunk”);
- a drámajátékot, a beszédtechnikát és a memoriterek felmondását (ehhez csak segédet adunk:
  „memoriter-mód”, 4. fejezet);
- a szabadon választott regényeket (13. és 18. témakör), mert a tanár választ, így nincs közös
  szöveg. Védett mű (Fekete István, Szabó Magda, Saint-Exupéry magyar fordítása) amúgy sem
  idézhető;
- a helyesírási gyakorlást (diktálás, szabályok sulykolása). Ahol egy szabály mögött
  mechanizmus van (hasonulás → szóelemzés elve, illeszkedés, -tja/-tsa), azt animáljuk; a
  puszta szabálylistát nem.

**Kiválasztási elv.**

1. **A kötelező művek kiemelten.** A *János vitéz* (14 óra) két leckét kap (verselés és az út),
   a *Toldi* (16 óra) egyet, és a verselés-lecke egy lépése is vele foglalkozik. *A Pál utcai
   fiúk* (10 óra) és az *Egri csillagok* (12 óra) egyet-egyet. A memoriterek közül a *Himnusz*,
   a *Szózat*, a *János vitéz* és a *Toldi* részletei közvetlenül a leckékben vannak.
2. **Arányosság, korrigálva az animációs értékkel.** Irodalomból: 108 óra / 9 lecke ≈ 12 óra
   leckénként. Nyelvtanból: az animálható 91 óra / 8 lecke ≈ 11 óra (a 6. és a 7. témakör
   nélkül). A legnagyobb témakör, a szófajoké (46 óra) csak két leckét kap. Ennek az az oka,
   hogy óráinak nagy része helyesírási gyakorlás és szövegalkotás (a kerettanterv szerint:
   „A szófajokhoz kapcsolódó helyesírási, nyelvhelyességi, szövegalkotási, szövegértési
   tudnivalók”). A 3. tartalék (számnévírás) és a 4. (földrajzi nevek) ezt bővítené. Fordítva:
   a nyelvi szintek (20 óra) négy leckét kapnak, mert itt a legnagyobb a belátás (hang, fonéma,
   szóelem, hasonulás).
3. **Átjárás a nyelvtan és az irodalom között.** A leckék tudatosan egymásra épülnek. A szótag
   (03) a verselés alapja (10). A hangutánzó szó (06) visszatér az *Alföld*ben (12). A
   kommunikációs modell (01) választ ad arra, kihez beszél a *Himnusz* és kihez a *Szózat* (16).
   A szó szerinti és az átvitt jelentés (06) a szóképek alapja (10, 15).
4. **Építőkockák:** öt új modul (4. fejezet), és öt kész történelemmodul (térkép, időszalag,
   forráskártya, kártyák, jelenet-metszet).

**Célcsoport: 10–12 évesek.** A panelen lépésenként legfeljebb **45 szó** áll
(`"maxWords": 45`), rövid mondatokban. Minden új fogalom félkövéren szerepel, egy mondatnyi
magyarázattal. A vásznon több a kép és a játék, és kevesebb a szöveg; kivétel az idézett vers,
amely maga a tananyag. 6–8 lépés.

A jelölések ugyanazok, mint a korábbi terveknél: *(ellenőrizendő)* – gyártás előtt forrásban
ellenőrizni kell; *(becslés)* – a leckében is ki kell mondani; *(értelmezés)* – egy lehetséges
olvasat, a leckében `> értelmezés:` dobozban jelenik meg (7. fejezet). A „Meglévő anyagok” pont
saját ismereten alapul, nincs ellenőrizve.

## 2. A leckék

| # | slug | cím | témakör | építőkocka | nehézség (1–3) |
|---|---|---|---|---|---|
| 01 | `01-kommunikacio` | Kérdés vagy kijelentés? – a kommunikáció tényezői és a beszéd zenéje | 1 | **MagHang** (dallam), MagText | 2 |
| 02 | `02-beszedhang` | Hogyan lesz a levegőből „á”? – beszédszervek, magánhangzók, zönge | 4 | **MagHang** (szájmetszet, szintetizátor) | 3 |
| 03 | `03-hang-betu-fonema` | Kör, kőr, tőr – hang, betű, fonéma, ábécé | 4 (+2) | MagText | 2 |
| 04 | `04-toldalek` | Kertészeknek, halászoknak – szótő, toldalék, hangrend, illeszkedés | 4 | **MagText** (ref.), **MagMorph** (ref.) | 3 |
| 05 | `05-hasonulas` | Kútba vagy [kúdba]? – mássalhangzótörvények és a helyesírás négy elve | 4 (+2) | MagMorph, MagHang (metszet), TortCards | 2 |
| 06 | `06-kullog-lolab` | Kullog vagy tipeg? Kilóg a lóláb? – hangalak, jelentés, szólás | 5 (+3) | TortScene, saját járásanimáció, TortCards | 2 |
| 07 | `07-dorlak` | Mit csinált a dorlák? – a szófajok próbája | 8 | MagText, MagMorph, TortCards | 2 |
| 08 | `08-ige` | Hány alakja van egy igének? – idő, mód, ragozás, -tja/-tsa | 8 | MagMorph | 2 |
| 09 | `09-nepmese` | Miért mindig a legkisebb? – a népmese szerkezete és világa | 9 | MagStory, TortScene, TortCards | 2 |
| 10 | `10-janos-vitez-vers` | Tizenkét szótag, két ütem – a János vitéz verselése | 10 (+15) | **MagVers** (ref.), MagHang (ütem) | 3 |
| 11 | `11-janos-vitez-utja` | Határos-e India és Franciaország? – János vitéz útja | 10 | TortMap/TortGlobe, MagStory | 2 |
| 12 | `12-alfold` | „Felröpűlök ekkor gondolatban” – Petőfi: Az alföld | 11 | TortScene, TortMap, MagVers | 2 |
| 13 | `13-pal-utcai-fiuk` | Grund, Füvészkert, csata – A Pál utcai fiúk tere és íve | 12 | **MagStory** (ref.), saját vázlattérkép | 3 |
| 14 | `14-walesi-bardok` | „Ötszáz, bizony, dalolva ment” – a ballada | 14 | MagVers, MagText, TortSource | 2 |
| 15 | `15-toldi` | Félkézzel a szekérrúd – Toldi: forrás, szókép, túlzás | 15 | MagVers, MagStory, TortSource | 2 |
| 16 | `16-himnusz-szozat` | Mit mesél a Himnusz? – Himnusz és Szózat | 16 | TortTimeline, MagVers | 2 |
| 17 | `17-egri-csillagok` | Ki kicsoda, mikor? – az Egri csillagok szálai | 17 | MagStory, TortTimeline, TortSource | 3 |

A nehézség gyártási nehézséget jelent: 1 = egy fő vizuál, kevés adat; 2 = egy közepes modul
vagy új interakció; 3 = új modul, hangszintézis, kényes pontosság vagy hosszú szövegelemzés.

Témakörönként: 1 → 01 · 2 → 03, 05 · 3 → 06 · 4 → 02, 03, 04, 05 · 5 → 06 · 6 → – ·
7 → – · 8 → 07, 08 · 9 → 09 · 10 → 10, 11 · 11 → 12 · 12 → 13 · 13 → – · 14 → 14 ·
15 → 15 (+10) · 16 → 16 · 17 → 17 · 18 → –.

---

## 3. Briefek

Minden briefben van egy **„Szöveg és jog”** sor: milyen szöveget idéz a lecke szó szerint, és
miért szabad (7. fejezet). Az „Adatok” értékei a `### Adatok` rétegbe, az idézett sorok az új
`### Idézet` blokkba kerülnek (5. fejezet).

### 01 · `01-kommunikacio` – Kérdés vagy kijelentés? – a kommunikáció tényezői és a beszéd zenéje

- **Tanulási cél:** A kommunikációnak tényezői vannak: feladó, címzett, üzenet, kód, csatorna
  és beszédhelyzet. Az üzenet nemcsak szavakból áll. A hanglejtés, a hangsúly, a szünet, az
  arcjáték és a gesztus is jelentést hordoz, és ha a csatorna ezeket elveszíti (telefon, SMS),
  valamivel pótolni kell őket. A magyar eldöntendő kérdés dallama sajátos: emelkedik, aztán a
  végén **leesik**.
- **Kerettanterv:** „A kommunikáció tényezőinek megismerése” · „A kommunikáció nem nyelvi
  jeleinek felismerése, alkalmazása” · „A nyelv zenei kifejezőeszközeinek megismerése,
  alkalmazása” · „A jelek felismerése, elkülönítése, csoportosítása” · Fogalmak: „természetes
  jelek, mesterséges jelek, jelrendszerek, feladó, címzett, üzenet, kód, csatorna,
  beszédhelyzet, arcjáték, gesztusok, testhelyzet, külső megjelenés, térköz; hangsúly,
  hanglejtés, tempó, hangerő, szünet, csend” · ajánlott: „A kommunikációs illemszabályok
  tudatosítása (üdvözlési szokások, SMS, chat)”.
- **Tévhitek:** „Minden kérdés végén felmegy a hang.” (A magyarban nem így van: az eldöntendő
  kérdés dallama emelkedő–eső, a kérdőszavas kérdésé pedig ereszkedő, akárcsak a kijelentésé.)
  „A kommunikáció = beszéd.” „Ha leírom, ugyanazt mondom.” „A füst nem jel, mert senki sem
  küldte.” (Ez **természetes jel**.)
- **Kulcsvizuál:** egy mondat „partitúrája”: a szótagok vízszintesen sorakoznak, fölöttük a
  dallamvonal, a hangsúlyos szótag nagyobb, a szünet üres hely. Mellette a kommunikációs
  modell két figurával és a köztük futó csatornával. Ahogy a csatorna változik (szemtől
  szemben → telefon → SMS), a nem nyelvi jelek sorra kihullanak a csőből. SMS-nél a dallam is
  elvész, a helyére emoji lép.
- **Interaktív:** **Dallam-kitaláló:** négy dúdolt dallam szól szavak nélkül (`MagHang.hum`),
  a vásznon csak a dallamvonal látszik. Az osztály eldönti, kijelentés, eldöntendő kérdés,
  kérdőszavas kérdés vagy felkiáltás volt-e, és csak ezután jelennek meg a szavak. **Csatorna-
  kapcsoló:** szemtől szemben / telefon / levél / SMS. Mi marad meg, és mivel pótoljuk, ami
  elveszett?
- **Lépések:** Jelek körülöttünk · Ki küldi, ki kapja? · Ugyanaz a mondat, más dallam ·
  Találd ki a dallamból! · Nem minden kérdés megy fel · Hangsúly és szünet · Mi vész el a
  csatornán? · Összefoglaló.
- **Adatok:** a példamondatok szótagjainak dallamértékei (Hz) `series` típusként, pl. a „Megjött
  a levél?” mondatnál a csúcs az utolsó előtti szótagon („le”), az utolsón („vél”) a dallam
  esik. A „Megjött a levél.” mondat dallama végig ereszkedik; a „Ki jött meg?” is ereszkedő.
  A két szótagos eldöntendő kérdés („Esik?”) dallama a szakirodalom szerint az utolsó
  szótagon emelkedik *(ellenőrizendő: Varga László: Intonation and Stress, 2002; Gósy Mária:
  Fonetika, a beszéd tudománya, 2004)*. A magyar szóhangsúly mindig az első szótagon van. Szünet
  és jelentés: „Kegyelmet, nem kivégezni!” – „Kegyelmet nem, kivégezni!” (közismert iskolai
  példa).
- **Szöveg és jog:** csak saját példamondatok. Idézet nincs.
- **Építőkocka:** MagHang (`hum`, a dallamvonal rajza – első megépítés), MagText (szótagsor).

### 02 · `02-beszedhang` – Hogyan lesz a levegőből „á”? – beszédszervek, magánhangzók, zönge

- **Tanulási cél:** A beszédhang a kiáramló levegőből születik. A hangszalagok rezgése a
  **zönge**. A magánhangzót a szájüreg alakja formálja: a nyelv helyzete (elöl vagy hátul, fent
  vagy lent) és az ajak (kerek vagy réses). Ugyanaz a zönge más szájformán át más
  magánhangzóként szól. A mássalhangzónál a levegő akadályba ütközik; ha közben a hangszalag is
  rezeg, **zöngés** a hang (b, d, z), ha nem, **zöngétlen** (p, t, sz).
- **Kerettanterv:** „A beszédhangok képzésének megismerése, csoportosításának alapjai” · „A
  nyelv szerkezeti egységeinek és azok funkcióinak megismerése” · tananyagtartalom:
  „Hangképzés, fonéma” · „A magánhangzók csoportosítása” · ajánlott: „A hangképzés
  biológiája – digitális anyagok” · Fogalmak: „beszédhang, fonéma, magánhangzó, mássalhangzó,
  hangkapcsolódási szabályszerűségek”.
- **Tévhitek:** „Az *á* a hosszú *a*.” (Nemcsak hosszabb: az *a* hátul képzett és kerek, az *á*
  réses és nyíltabb, tehát más a hangszín. Ugyanez igaz az *e*–*é* párra.) „Az *a* nem kerek
  hang.” (A magyar iskolai csoportosításban ajakkerekítéses.) „A hang a szájban keletkezik.” (A
  zönge a gégében születik, a száj csak formálja.) „A magas hangrendű szó magasabb hangon
  szól.” (A „magas” itt a nyelv helyzetét jelenti, nem a hangmagasságot.)
- **Kulcsvizuál:** stilizált, oldalnézeti fejmetszet (tüdő → gége → garat → száj- és orrüreg).
  A hangszalagok zöngénél rezgő vonalpárként látszanak. A nyelv húzható görbe. Mellette a
  magánhangzó-négyszög: elöl/hátul × fent/középen/lent, a 14 magánhangzó betűjével. A
  metszet nyelvállása a négyszögben pöttyként jelenik meg.
- **Interaktív:** **Nyelv-húzó:** a diák húzza a nyelvet (2D) és kapcsolja az ajakkerekítést; a
  pötty a négyszögben mozog, a legközelebbi magánhangzó kigyullad, és ▶-ra a szintetizátor
  megszólaltatja (formánsszintézis, `MagHang.vowel`). **Kéz a torkon:** zönge ki/be ugyanazzal
  a szájformával. *sz* ↔ *z*, *f* ↔ *v*: zörej, illetve zörej + zümmögés (`MagHang.noise`). A
  csoportosítás kattintással ellenőrizhető: „melyik hang felső nyelvállású és ajakkerekítéses?”
- **Lépések:** Honnan jön a hang? · A hangszalag rezeg: zönge · A száj mint szűrő · Elöl vagy
  hátul (magas és mély magánhangzók) · Kerek vagy réses ajak · Fent, középen, lent – és rövid
  vagy hosszú · Zöngés vagy zöngétlen? · Összefoglaló.
- **Adatok:**
  - **csoportosítás** (5. osztályos tankönyvi rendszer *(ellenőrizendő a választott tankönyvvel)*):
    a nyelv vízszintes mozgása szerint **magas** (elöl képzett): e, é, i, í, ö, ő, ü, ű,
    **mély** (hátul képzett): a, á, o, ó, u, ú; ajakműködés szerint **ajakkerekítéses**: a, o,
    ó, u, ú, ö, ő, ü, ű, **ajakréses**: á, e, é, i, í; a nyelv függőleges mozgása szerint
    **alsó**: a, á, e, **középső**: é, o, ó, ö, ő, **felső**: i, í, u, ú, ü, ű; időtartam
    szerint rövid és hosszú. (Az *á* tankönyvenként „mély” vagy „középső helyzetű”; a lecke a
    választott tankönyvet kövesse, és ezt a `.md` megjegyzése rögzítse.)
  - **formánsok** (felnőtt férfi, közelítő értékek, F1/F2 Hz-ben): i 270/2250, é 400/2100,
    e 600/1700, ü 280/1700, ö 420/1500, á 750/1300, a 600/1000, o 450/850, u 320/750
    *(becslés, ellenőrizendő: Gósy 2004, magyar mérések)*. A lecke mondja ki, hogy a gépi hang
    egyszerűsített.
  - **alaphang** (zönge) *(becslés)*: felnőtt férfi kb. 100–130 Hz, felnőtt nő kb. 190–230 Hz,
    10–12 éves gyerek kb. 230–300 Hz.
  - **zöngés–zöngétlen párok** (9): b–p, d–t, g–k, gy–ty, v–f, z–sz, zs–s, dz–c, dzs–cs. Pár
    nélküli zöngés: j, l, m, n, ny, r; a h zöngétlen *(ellenőrizendő a tankönyvi besorolással)*.
- **Szöveg és jog:** idézet nincs. A fejmetszet saját rajz, anatómiai atlaszt nem veszünk át
  (a biológia `BioBody` stílusát követi).
- **Építőkocka:** **MagHang** (metszet `tract`, négyszög `vowelChart`, `vowel`, `noise` – első
  megépítés).

### 03 · `03-hang-betu-fonema` – Kör, kőr, tőr – hang, betű, fonéma, ábécé

- **Tanulási cél:** A hang a beszédé, a betű az írásé, és a kettő nem mindig fedi egymást. Egy
  hangot jelölhet két betűjel (*sz*), és egy betű jelölhet két hangot (*x* = [ksz]). A
  **fonéma** az a hang, amelynek cseréje új szót ad: *kör* → *tőr*. A magyarban a hosszúság is
  jelentést különböztet meg (*kör*–*kőr*, *kel*–*kell*). Az ábécé 44 betűből áll, és a betűrend
  ehhez igazodik (*c* < *cs*).
- **Kerettanterv:** tananyagtartalom: „Hang és betű, az ábécé” · „Betűrend, elválasztás” ·
  „Hangképzés, fonéma” · Fogalmak (2.): „hang és betű, ábécé, […] elválasztás” · (4.):
  „beszédhang, fonéma, magánhangzó, mássalhangzó” · „A nyelvi elemzőkészség fejlesztése”.
- **Tévhitek:** „A betű és a hang ugyanaz.” „Az *sz* két hang.” „A betűrendben a *cs* a *c*
  után, a *cu* előtt jön.” (Nem: a *cs* önálló betű, ezért *cukor* < *csiga*.) „A hosszú és a
  rövid hang csak kiejtési kérdés.” (*kor*–*kór*: két külön szó.)
- **Kulcsvizuál:** **szólétra**, amelynek fokai: *kör → kőr → tőr → tör → tér → tél → tál →
  sál → sas → kas*. Minden lépésben egyetlen hang cserélődik, és a kis rajz is átváltozik
  (kör, kártyaszín, tőr, törött pálca, tér, hópehely, tál, sál, sas, méhkas). Mellette a 44
  betű „betűsínen”, a két- és háromjegyűek egy-egy összetartozó csempén.
- **Interaktív:** **Létramászás:** a diák egy hangot cserél (választóból), és ha létező szót
  kapott, megjelenik a rajz. A hosszúság-kapcsoló (ö ↔ ő) a *kör*-ből *kőr*-t csinál.
  **Betűrend-gép:** a diák szavakat húz sorba, a gép betűnként összehasonlít, és megmutatja,
  hol dőlt el a sorrend. **Szótagolló:** ahány magánhangzó, annyi szótag (híd a 10. leckéhez).
- **Lépések:** Hallod vagy látod? · Betű ≠ hang (sz, ly, x) · Egy hang cseréje: új szó · A
  szólétra · A hossz is számít · 44 betű és a betűrend · Szótag és elválasztás · Összefoglaló.
- **Adatok:** az ábécé 44 betűje: 35 egyjegyű, 8 kétjegyű (cs, dz, gy, ly, ny, sz, ty, zs) és 1
  háromjegyű (dzs). A q, w, x, y idegen szavakban és régi nevekben fordul elő. Betűrendi
  szabályok *(ellenőrizendő: AkH. 12. – a betűrendbe sorolás pontjai)*: a többjegyű betű önálló
  betű (*cukor* < *csiga*); a rövid és a hosszú magánhangzó az első menetben egyenértékű, és csak
  akkor dönt (rövid előre), ha a két szó egyébként azonos (*kar* < *kár* < *karc*). Minimális
  párok: *kor–kór*, *öt–őt*, *ver–vér*, *kel–kell*, *szál–száll*, *tör–tőr*. A szólétra minden
  foka egy hangot változtat; ezt a lecke `L.checks()` próbája ellenőrzi. Elválasztás: egy
  mássalhangzó az új sorba kerül (*ke-rék*), mássalhangzó-torlódásnál csak az utolsó (*ab-lak*),
  a többjegyű betű nem válik szét (*asz-tal*), a kettőzött többjegyűből két betű lesz
  (*asz-szony*) *(ellenőrizendő: AkH. 12., elválasztás)*.
- **Szöveg és jog:** csak szavak, idézet nincs.
- **Építőkocka:** MagText (`letters`, `syllabify`, `collate`).

### 04 · `04-toldalek` – Kertészeknek, halászoknak – szótő, toldalék, hangrend, illeszkedés

- **Tanulási cél:** A szó szótőből és toldalékokból áll. A **képző** új szót alkot (*kert* →
  *kertész*), a **jel** a szó alakját módosítja (*kertészek*), a **rag** a mondatbeli
  kapcsolatát fejezi ki (*kertészeknek*). A sorrend: tő + képző + jel + rag. A toldalék
  **illeszkedik** a szó hangrendjéhez (*-nak/-nek*, *-hoz/-hez/-höz*). Az összetett szónál az
  utolsó tag dönt.
- **Kerettanterv:** „A szavak szerkezetének felismerése” · „A főbb szóelemek és funkciójuk
  (képző, jel, rag) felismerése, elkülönítése” · tananyagtartalom: „Magánhangzótörvények:
  Hangrend Illeszkedés” · „A szavak szerkezete: Egyszerű és összetett szavak Szótő és
  toldalékok A képző, a jel, a rag” · ajánlott: „A szótő és a toldalékok helyes használata”,
  „Nyelvi játékok: szóalkotási módok” · Fogalmak: „szó, szóelem, egyszerű szó, összetett szó”.
- **Tévhitek:** „Minden toldalék rag.” „A szó végén lévő *-k* mindig többes szám.” (*látok* –
  igei személyrag.) „A vegyes hangrendű szó toldaléka véletlenszerű.” (Szabály szerint
  alakul, néhány ingadozó kivétellel.) „A toldalékot bárhova tehetem.” („kertésznekek” nem
  létezik: a rag után nem jön jel.)
- **Kulcsvizuál:** a két szólánc egymás alatt: *kert | ész | ek | nek* és *hal | ász | ok |
  nak*. Ugyanaz a szerkezet, de a magánhangzók „átfordulnak”. A csempék színe a szóelem fajtáját
  jelzi (7. fejezet, színkód), a tő magánhangzója egy kis lámpa, amely „átvilágít” a
  toldalékokra.
- **Interaktív:** **Szóelem-láncoló:** a diák csempéket húz a tőhöz. A toldalékcsempén minden
  változat ott van (*-ban | -ben*), és a tőhöz érve a megfelelő alakra pattan. Rossz sorrendnél
  (rag után jel) a csempe visszapattan, és egy mondatban megmondja, miért. A tő cserélhető
  (*kert / hal / tükör / papír / sofőr / virágcserép*), így a diák kipróbálhatja a vegyes
  hangrendet és az összetett szót is.
- **Lépések:** Mi van egy szóban? · Képző: új szó születik · Jel: ugyanaz a szó, más alak ·
  Rag: kapcsolat a mondatban · A sorrend szabálya · Mély, magas, vegyes hangrend · A kaméleon
  toldalék · Összefoglaló (összetett szó: az utolsó tag dönt).
- **Adatok** (mind `morph` típus, 5. fejezet): *kert + ész (képző) + ek (jel) + nek (rag)*;
  *hal + ász (képző) + ok (jel) + nak (rag)*. Hármas alakú rag: *tükörhöz*, *kerthez*,
  *halhoz*. Vegyes hangrend: ha a mély magánhangzó után csak i, í, é áll, a toldalék mély
  (*papírnak*, *kávénak*, *kocsinak*); ha az utolsó magánhangzó ö, ő, ü vagy ű, a toldalék magas
  (*sofőrnek*, *parfümben*). Ingadozó: *fotelban/fotelben*, *hotelban/hotelben*
  *(ellenőrizendő: AkH. 12. és a NYTI helyesírási tanácsadója)*. Összetett szó: *virág + cserép
  → virágcserépben* (az utolsó tag magas). Az illeszkedési szabály kivételeit a `.md` sorolja
  fel, a kód nem találgat.
- **Szöveg és jog:** csak szavak.
- **Építőkocka:** **MagText**, **MagMorph** (referencia; mindkettő itt épül).

### 05 · `05-hasonulas` – Kútba vagy [kúdba]? – mássalhangzótörvények és a helyesírás négy elve

- **Tanulási cél:** Ha két mássalhangzó találkozik, a száj „előre készül” a következőre, ezért
  az első hasonul hozzá: zöngésségben (*kútba* [kúdba]), a képzés helyében (*színpad*
  [szímpad]), vagy teljesen (*egészség* [egésség]). Írásban mégis *kútba* áll, mert a magyar
  helyesírás négy elve közül itt a **szóelemzés elve** érvényesül: a szóelemek láthatók
  maradnak. A négy elv: kiejtés, szóelemzés, hagyomány, egyszerűsítés.
- **Kerettanterv:** tananyagtartalom: „Mássalhangzótörvények: Részleges hasonulás Írásban
  jelöletlen és jelölt teljes hasonulás Összeolvadás Rövidülés Kiesés” · „Helyesírásunk
  alapelvei: a kiejtés elve […] a szóelemzés elve […] a hagyomány elve […] az egyszerűsítés
  elve” · (2.): „Az alapvető helyesírási szabályok megismerése (kiejtés elve, szóelemzés elve,
  hagyomány elve, egyszerűsítés elve)” · „A megismert helyesírási esetek felismerése írott
  szövegekben” · Fogalmak (4.): „hangkapcsolódási szabályszerűségek”.
- **Tévhitek:** „Úgy írunk, ahogy beszélünk.” „A [kúdba] kiejtés hibás vagy tájszólás.” (Ez a
  természetes, köznyelvi kiejtés.) „Az *ly* azért van, hogy nehezebb legyen.” (Hagyomány: régen
  más hangot jelölt *(ellenőrizendő a tankönyvi megfogalmazással)*.) „A *sakkal* (sakk + val) elírás.” (Az
  egyszerűsítés elve: három azonos betű helyett kettő.)
- **Kulcsvizuál:** két hangcsempe (*t* és *b*) halad egymás felé, mindkettőn jelvények: zöngés?,
  hol képződik? Ütközéskor az első átveszi a második zöngéjét (a *t*-ből *d* lesz), alatta a
  02-es lecke szájmetszete mutatja, hogy a hangszalag „korábban kapcsol be”. Fölötte két sor:
  **írjuk:** *kútba* · **mondjuk:** [kúdba].
- **Interaktív:** **Hasonulás-gép:** a diák kiválaszt egy szópárt, és lépésenként nézi, melyik
  tulajdonság terjed át. Utána ő dönti el: „hogyan írjuk?” – a gép a négy elv egyikével felel.
  **Négy doboz (TortCards):** 12 szót kell a négy elv dobozába rendezni (*ház*, *kútba*,
  *látja*, *Kossuth*, *folyó*, *sakk-kör*, *tollal*, *Mariann-nal*, *egészség*, *kép*, *Széchenyi*,
  *rossz*).
- **Lépések:** Írjuk így, mondjuk úgy · A száj előre készül · Részleges hasonulás · Teljes
  hasonulás: jelölt és jelöletlen · Összeolvadás, rövidülés, kiesés · Miért nem írjuk, ahogy
  mondjuk? · Négy elv, négy doboz · Összefoglaló.
- **Adatok** (`pron` típus: írás + [ejtés]): részleges, zöngésség szerint: *kútba* [kúdba],
  *népdal* [nébdal], *zsákban* [zságban], *vízpart* [víszpart]; képzés helye szerint: *színpad*
  [szímpad], *különben* [külömben]; teljes, jelöletlen: *egészség* [egésség], *anyja* [annya];
  teljes, jelölt: *kéz + vel → kézzel*, *az + ban → abban*; összeolvadás: *barátság*
  [baráccság], *látja* [láttya], *adja* [aggya]; rövidülés: *jobbra* [jobra], *tollban*
  [tolban]; kiesés: *mondta* [monta], *mindnyájan* [minnyájan] *(a kiesés példáit ellenőrizni
  a tankönyvvel)*. Egyszerűsítés: *toll + val → tollal* (de: *sakk-kör*, *Mariann-nal* kötőjellel, AkH. 12. 61., 93. – javítva 2026-11-24 a 05-ös lecke nyomán), *sakk + val
  → sakkal*, *sz + sz → ssz* (*rossz*), *gy + gy → ggy* (*meggy*). Hagyomány: *ly*
  (*folyó*), régi családnevek (*Kossuth*, *Széchenyi*, *Batthyány*). A szabálypontok számát a
  `.md` megjegyzése rögzíti *(ellenőrizendő: AkH. 12.)*.
- **Szöveg és jog:** csak szavak.
- **Építőkocka:** MagMorph (`assim`), MagHang (`tract` a 02-ből), TortCards.

### 06 · `06-kullog-lolab` – Kullog vagy tipeg? Kilóg a lóláb? – hangalak, jelentés, szólás

- **Tanulási cél:** A szó hangalakja és jelentése többnyire megállapodáson alapul, de nem
  mindig. A **hangutánzó** szó a hangot utánozza (*csobban*), a **hangulatfestő** a mozgás vagy
  a látvány hangulatát festi (*kullog*, *tipeg*). Egy hangalakhoz tartozhat több, egymással
  összefüggő jelentés (*toll*: madártoll, írótoll – **többjelentésű**), vagy két, egymással
  nem összefüggő jelentés (*ég*: égbolt és lángol – **azonos alakú**). A köznyelvi metafora
  (*az asztal lába*) és a szólás (*kilóg a lóláb*) is átvitt jelentés; a közmondás teljes
  mondat, és tanulságot fogalmaz meg.
- **Kerettanterv:** (5.): „A hangalak és a jelentés kapcsolatának, illetve a jelentésmezőnek
  a felismerése” · „Az egyjelentésű, a többjelentésű, az azonos alakú, az ellentétes jelentésű
  szavak, a rokon értelmű szavak, a hasonló alakú szavak, a hangutánzó és a hangulatfestő
  szavak jelentése, felismerése” · (3.): „Az állandósult szókapcsolatok, szólások, közmondások
  értelmezése, szerkezetének, használati körének megfigyelése” · „A leggyakoribb mindennapi
  metaforák jelentésszerkezetének megfigyelése a beszélt és írott szövegekben – játékos
  gyakorlatokkal” · Fogalmak: „állandósult szókapcsolat, szólás, szóláshasonlat, közmondás,
  szállóige, köznyelvi metaforák”.
- **Tévhitek:** „A szólás és a közmondás ugyanaz.” „A *toll* és az *ég* ugyanolyan eset.” (Az
  egyik többjelentésű, a másik azonos alakú: a jelentések rokonságán múlik.) „A hangutánzó szó
  minden nyelvben ugyanaz.” (A kakas magyarul *kukorékol*, angolul *cock-a-doodle-doo*.) „A
  szólást szó szerint kell érteni.”
- **Kulcsvizuál:** egy stilizált alak, amely hat különböző módon megy végig a vásznon: tipeg,
  totyog, cammog, kullog, sántikál, csoszog. A járásuk zárt képletű mozgásciklus (lépéshossz,
  tempó, testtartás). Később egy díszes palást, amely alól tényleg kilóg egy lóláb, és egy
  „szó szerint ↔ átvitt” kapcsoló, amely a rajzot a jelentés kis jelenetére váltja.
- **Interaktív:** **Járás-tippelő:** a figura egy járásmódot mutat, a diák kiválasztja a
  hozzá illő igét, és a gép megmutatja az eredményt (osztályszavazásra is jó). **Bubu vagy
  kiki?** – két alak, két kitalált szó: melyik melyik? A tanár beírja a szavazás eredményét,
  és összeveti a kutatás eredményével. **Szó szerint / átvitt kapcsoló** négy szólásnál.
- **Lépések:** Hogyan szól a kakukk? · Kullog vagy tipeg? · Bubu vagy kiki? (Honnan tudjuk?) ·
  Egy hangalak, több jelentés · Rokon, ellentétes, hasonló alakú · Az asztal lába · Kilóg a
  lóláb: szólás, közmondás, szállóige · Összefoglaló.
- **Adatok:** a járások paraméterei (lépéshossz, tempó lépés/perc, törzsdőlés) – a tanár
  javíthatja, ha egy járás nem „olyan”. Bubu–kiki: Wolfgang Köhler 1929-ben a *maluma–takete*
  szópárral; Ramachandran és Hubbard 2001-ben a *bouba–kiki* párral (a válaszadók kb. 95 %-a a
  kerek alakot „bouba”-nak nevezte) *(ellenőrizendő)*. Példák: többjelentésű: *toll*, *körte*
  (gyümölcs és villanykörte), *fül* (testrész és a bögre füle); azonos alakú: *ég*, *nyúl*,
  *vár*; hasonló alakú: *helység–helyiség*, *egyelőre–egyenlőre*; köznyelvi metafora: *az
  asztal lába*, *a hegy lába*, *az üveg nyaka*, *a cipő nyelve*. Szólás: *kilóg a lóláb*,
  *eső után köpönyeg*, *kosarat ad*; szóláshasonlat: *hallgat, mint a sír*, *szegény, mint a
  templom egere*; közmondás: *Ki korán kel, aranyat lel.*, *Lassan járj, tovább érsz.*;
  szállóige: *A kocka el van vetve.* (Caesar, Suetonius szerint), *Lenni vagy nem lenni*
  (Shakespeare: Hamlet, Arany János fordítása). A szólások eredetmagyarázatai csak óvatosan,
  „egy magyarázat szerint” keretben *(ellenőrizendő)*.
- **Szöveg és jog:** a szólások és a közmondások közkincs népnyelvi anyag. A szállóigék
  rövidek, forrásuk közkincs (Arany fordítása, †1882). O. Nagy Gábor *Mi fán terem?* (szerzője
  1973-ban halt meg) és Kiss Gábor *Magyar szókincstár* (élő szerkesztő) című műve **védett**:
  legfeljebb a címükkel ajánlhatók, a szócikkeik szövege nem vehető át. A magyarázatok saját
  szavas összefoglalások.
- **Építőkocka:** TortScene (palást-jelenet), saját járásanimáció, TortCards (szólás /
  szóláshasonlat / közmondás / szállóige).

### 07 · `07-dorlak` – Mit csinált a dorlák? – a szófajok próbája

- **Tanulási cél:** A szófajt a szó **alakja és helye** is elárulja, nem csak a jelentése. Egy
  értelmetlen mondatban is megtaláljuk az igét (*-tak*), a főnevet (*a … -k*) és a melléknevet
  (*-s*, fokozható). A **toldalékpróba** és a **kérdés** (Ki? Mit csinál? Milyen? Hány? Hol?)
  két eszköz a szófaj megállapítására. Egy szónak lehet több szófaja (*ég*). Az igenév az ige
  „vendégszerepe” más szófaj helyén (*futni*, *futó*, *futva*).
- **Kerettanterv:** (8.): „A szófajok felismerése helyes leírása a mondatban és a szövegben:
  ige, főnév, számnév, határozószó, igenevek, névmások, viszonyszók, mondatszók” · „A
  szójelentés, a metaforikus jelentés, a több szófajúság megismerése” · „A nyelvi elemzőkészség
  kialakítása” · (4.): „Az alapszófajok (ige, főnév, melléknév, számnév, névmás) felismerése” ·
  ajánlott: „Többszófajúság”, „Szófajváltás”, „Az igenevek kapcsolata a többi szófajjal”, „A
  névmások szerepe a mondat- és szövegépítésben”.
- **Tévhitek:** „A szófaj a jelentésből derül ki.” „Ami cselekvés, az mindig ige.” (*a futás* –
  főnév.) „Minden szó egyféle szófajú.” „A *tegnap* főnév, mert időt jelent.”
- **Kulcsvizuál:** az értelmetlen mondat: ***A fimpás dorlák tegnap két szömbörköt
  vidáztak.*** A szavak alatt „nyomok” gyulladnak ki (*-s* képző, *-k* többes jel, *-t* tárgyrag,
  *-tak* múlt idő + személyrag), és a szavak a szófaj színét kapják. Második mondat: *A pölény
  még fimpásabb.* (A *-bb* középfok elárulja: *fimpás* melléknév.)
- **Interaktív:** **Szófaj-színező:** a diák minden szót kiszínez egy szófajjal, és a gép a
  „nyommal” indokolja, hogy jó-e. **Toldalékpróba valódi szavakon:** próbatoldalékok
  (*-tam/-tem*, *-k*, *-bb*, *-dik*) húzhatók egy szóra; az elfogadott zöldre vált, az
  elfogadhatatlan („*asztaltam*”) szürke lesz, és megbillen. **Szófajtérkép (TortCards):** kilenc
  szófajkártyát kell három csoportba rendezni.
- **Lépések:** Értelmetlen, mégis érted · Mi árulja el? · A toldalékpróba · Kérdezz rá! · Egy
  szó, két szófaj · Az ige vendégszerepei: igenevek · Helyettesítők és segítők: névmás,
  viszonyszó, mondatszó · Összefoglaló: szófajtérkép.
- **Adatok:** a kitalált szavak és a „nyomaik” (`morph` típus: *dorl + ák (jel)*? → a
  szóelemzés a `.md`-ben, pl. *szömbörk + öt (rag)*, *vidáz + t (jel) + ak (rag)*); a szófaj-
  besorolás. **A csoportosítás tankönyvenként eltér** (pl. a módosítószó hova tartozik; az
  igenév külön szófaj-e). A lecke a választott tankönyv rendszerét kövesse, ezt a `.md`
  megjegyzése rögzíti, a lecke pedig egy mondatban kimondja *(ellenőrizendő)*.
- **Szöveg és jog:** saját, értelmetlen mondatok. Lewis Carroll *Jabberwocky*-jának magyar
  fordításai (Tótfalusi István, Varró Dániel stb.) **védettek** – nem használjuk őket.
  Karinthy Frigyes (†1938) *Tegeződés*e közkincs, és a kerettanterv ajánlja. A névmás-lépés
  1–2 rövid mondatot idézhet belőle, ha a szöveget a gyártó ügynök megtalálja egy közkincs
  kiadásban *(ellenőrizendő)*; ha nem, saját példát használ.
- **Építőkocka:** MagText, MagMorph, TortCards.

### 08 · `08-ige` – Hány alakja van egy igének? – idő, mód, ragozás, -tja/-tsa

- **Tanulási cél:** Az ige cselekvést, történést vagy létezést fejez ki, és alakja öt dolgot
  mutat: az időt (múlt, jelen, jövő), a módot (kijelentő, feltételes, felszólító), a személyt
  és a számot, valamint a ragozást (alanyi: *látok*; tárgyas: *látom*). A jövő idő összetett
  alak (*látni fog*). A helyesírásban a *-t* végű igék a kényesek: a kijelentő módban *-tja*
  (*látja*), a felszólítóban *-tsa*/*-ssa* (*tanítsa*, *üsse*, *lássa*).
- **Kerettanterv:** tananyagtartalom: „Az ige fogalma”, „Az igeidők”, „Az igemódok”, „Az ige
  ragozása”, „A leggyakoribb igeképzők”, „Az igék helyesírása” · (8.): „Helyesírási készség
  fejlesztése” · „A nyelv szerkezeti egységeinek és azok funkcióinak megismerése”.
- **Tévhitek:** „A *látja* és a *lássa* ugyanaz, csak elírás.” „A jövő időnek saját jele van.”
  „A *mossa* csak felszólító lehet.” (Kijelentő is: *Mossa a kezét.* – a kettő egybeesik.) „A
  tárgyas ragozás = van tárgy.” (A **határozott** tárgy dönt: *látok egy házat* ↔ *látom a
  házat*.)
- **Kulcsvizuál:** az **ige vezérlőpultja**. A gombok: idő/mód (4 állás), személy (3), szám
  (2), ragozás (2). Középen a szó csempékből áll össze (tő + jel + rag, 7. fejezeti színkód),
  alatta egy 52 rubrikás rács telik meg, ahogy a diák kipróbálja a beállításokat. Az egyforma
  alakok (pl. a *láttam* az alanyi és a tárgyas ragozásban is) egy szálon összekapcsolódnak.
- **Interaktív:** a vezérlőpult (gombok, csúszkák). **-tja vagy -tsa?** döntési fa: a diák
  kiválaszt egy igét, és a fa ágain végigvilágít az út (rövid vagy hosszú magánhangzó + *t*?
  mássalhangzó + *t*? *-szt*, *-st*?) a helyes alakig. **Kijelentő vagy felszólító?**:
  ugyanaz a *mossa* két mondatban; a diák dönt, és a szövegkörnyezet adja meg a választ.
- **Lépések:** Mit csinál? (az ige fogalma) · Múlt, jelen, jövő · Kijelentő, feltételes,
  felszólító · Látok vagy látom? · A vezérlőpult: 52 rubrika · -tja vagy -tsa? · *Mossa*:
  melyik mód? · Összefoglaló.
- **Adatok:** a rubrikák: 4 egyszerű alakcsoport (kijelentő jelen, kijelentő múlt, feltételes
  jelen, felszólító) × 3 személy × 2 szám × 2 ragozás = **48**, és 4 *-lak/-lek* alak (*látlak*,
  *láttalak*, *látnálak*, *lássalak*) = **52 rubrika**. Az összetett alakok (*látni fog*, *látott
  volna*) külön, rubrikán kívül szerepelnek. Az egymástól **különböző** alakok számát a lecke
  maga számolja ki a `.md` alaktáblájából, és kiírja (pl. a *láttam* kétszer szerepel). A
  felszólító mód szabályai *(ellenőrizendő: AkH. 12., az igék felszólító módja)*: rövid
  magánhangzó + *t* → *ss* (*üt → üsse*, *fut → fusson*, *köt → kösse*); hosszú magánhangzó
  vagy mássalhangzó + *t* → *ts* (*tanít → tanítsa*, *ért → értse*, *tart → tartsa*); kivétel
  *lát → lássa*, *bocsát → bocsássa*; *-szt → ssz* (*választ → válassza*), *-st → ss*
  (*fest → fesse*); *s, sz, z* végű ige: *mos → mossa*, *olvas → olvassa*, *néz → nézze* (itt
  kijelentő és felszólító egybeesik).
- **Szöveg és jog:** csak saját példák.
- **Építőkocka:** MagMorph (csempék; az alaktábla a `.md`-ből jön, a kód nem ragoz).

### 09 · `09-nepmese` – Miért mindig a legkisebb? – a népmese szerkezete és világa

- **Tanulási cél:** A népmesének visszatérő szerkezete van: kezdőformula, egy baj vagy hiány,
  útnak indulás, próbák (gyakran **három**), segítő és csodás eszköz, győzelem, jutalom,
  záróformula. A **meseszámok** (3, 7, 12) és a visszatérő **motívumok** (legkisebb fiú, táltos
  ló, égig érő fa) a mesemondó „építőkockái”. A mese ideje és helye meghatározatlan, a mondáé
  valós hely vagy személy, a mítosz az istenekről és a világ eredetéről szól.
- **Kerettanterv:** (9.): „A korábban megismert műfajokhoz (pl. mese, monda) kapcsolódó
  elemzési szempontok alkalmazása hasonló témájú szövegekben” · „Különböző korokban keletkezett,
  különböző műfajú szövegek tematikus rokonságának, problémafelvetéseinek tanulmányozása” ·
  kötelező: „Fehérlófia”, „Az égig érő fa (magyar népmese)”, „Arany János: Rege a
  csodaszarvasról”, „Görög mítosz: Daidalosz és Ikarosz” · Fogalmak: „népmese, mese, mesealak,
  meseformálás, meseszám, kaland, motívum, monda, rege, mítosz”.
- **Tévhitek:** „A mese csak kicsiknek való.” „A monda igaz történet.” „A mítosz hazugság.”
  (Ezek a világ magyarázatai a maguk korában.) „Minden mesében három próba van.” (Gyakori, de
  nem szabály.)
- **Kulcsvizuál:** egy **égig érő fa**, amelynek gyökere az alsó, törzse a középső, koronája a
  felső világba ér. A hős felfelé mászik, és szintenként egy-egy próba vár rá. Mellette egy
  „mesecsontváz”: egy sáv kártyákkal (funkciósor). Két mese (*Az égig érő fa*, *Fehérlófia*)
  ugyanarra a csontvázra rajzolódik, átfedésben: más a hús, azonos a váz.
- **Interaktív:** **Mesegép:** a diák minden funkcióhoz kártyát választ (hős, baj, segítő,
  próba × 3, csodás eszköz), és a sáv egy kis mesévé áll össze; a meseszám-számláló jelzi, hol
  van 3, 7 vagy 12. **Mese, monda vagy mítosz? (TortCards):** a diák jellemzőket és
  szövegcímeket rendez három oszlopba.
- **Lépések:** Egyszer volt, hol nem volt · Mindig a legkisebb? · Három próba (meseszám) · A
  mese csontváza · Az égig érő fa: a mese világa · Két mese, egy csontváz · Mese, monda vagy
  mítosz? · Összefoglaló: írd tovább!
- **Adatok:** a funkciósor (saját, Propp nyomán egyszerűsítve; Propp neve csak a `.md`
  megjegyzésében áll), a két mese funkcióinak sorrendje és a meseszámok előfordulásai –
  **a választott közkincs szövegváltozatból megszámolva** *(ellenőrizendő)*. A három világ
  (felső, középső, alsó) és a „világfa” néprajzi **értelmezés**, nem a mese szövege – így is
  jelöljük. Kezdő- és záróformula: hagyományos.
- **Szöveg és jog:** a népmesék szövege csak **közkincs gyűjtésből** idézhető, pl. Arany László:
  *Eredeti népmesék* (1862; Arany László 1898-ban halt meg), Benedek Elek gyűjtései (†1929),
  Kriza János (†1875). A pontos kiadást és mesét a gyártó ügynök ellenőrizze. **Illyés Gyula**
  feldolgozásai (*Hetvenhét magyar népmese*, Illyés †1983) **védettek** – a legtöbb iskolai
  változat ebből való, ezért ezt kifejezetten kerüljük. Daidalosz és Ikarosz története saját
  összefoglaló: Ovidius közkincs, de magyar fordításai (pl. Devecseri Gábor, †1971) és Trencsényi-
  Waldapfel Imre *Görög regék* című könyve (†1970) védettek. Arany *Rege a csodaszarvasról*
  című verse (†1882) közkincs; legfeljebb 2–4 sora jelenhet meg a monda-példánál.
- **Építőkocka:** MagStory (`strip` – funkciósáv), TortScene (égig érő fa), TortCards.

### 10 · `10-janos-vitez-vers` – Tizenkét szótag, két ütem – a János vitéz verselése

- **Tanulási cél:** A *János vitéz* sorai **felező tizenkettesek**: minden sor 12 szótag, és a
  sor közepén (a 6. szótag után) egy kis szünet, a **sormetszet** osztja két ütemre. A magyar
  szó első szótagja hangsúlyos, ezért az ütem eleje „üt”: ez az **ütemhangsúlyos** verselés. A
  sorok párosával rímelnek (**páros rím**, *aabb*), egy versszak négy sor. A *Toldi* is felező
  tizenkettes, de nyolcsoros versszakokban. Petőfi szóképei is a vers zenéjébe illeszkednek:
  hasonlat, metafora, megszemélyesítés.
- **Kerettanterv:** (10.): „A szöveg néhány részletében a poétikai eszközök felismerése,
  szerepük értelmezése: verselés, szóképek, alakzatok” · „Alapvető verstani és műfaji
  fogalmak megismerése, alkalmazása a mű bemutatásakor” · Fogalmak: „verses epika, elbeszélő
  költemény; ütemhangsúlyos verselés, verssor; felező tizenkettes, páros rím; hasonlat,
  metafora, megszemélyesítés; párhuzam, ellentét” · memoriter: „Petőfi Sándor: János vitéz
  (részletek)”.
- **Tévhitek:** „A szótag a szótagolt írásból jön.” (A versben a kiejtés számít: ahány
  magánhangzó, annyi szótag.) „A rím = ugyanaz a végződés.” (Elég, ha a magánhangzók csengenek
  össze: *sugára – bojtárra*.) „A felező tizenkettes = két hatos sor.” (Egy sor, két ütemmel.)
  „Egy jó költő minden sora pontosan 12.” (A MEK-szövegben 2 sor 11 szótagos – lásd az
  adatokat.)
- **Kulcsvizuál:** az első versszak nagy betűkkel. A szótagok alatt sorra kigyulladnak a
  magánhangzó-pöttyök (1–12), a 6. után függőleges sormetszet-vonal húzódik, az ütemek eleje
  vastag. A sorvégek rímpárjai egyszínűek. Később egy „lemezjátszó”: a szótagok kopogásként
  haladnak egy sávon (ütemkezdetnél erősebb koppanás – `MagHang.click`).
- **Interaktív:** **Dobbants az ütemre!** – szól a kopogás, és a diák (vagy az osztály a tanár
  kattintásával) az ütem elejére kattint; a gép milliszekundumra méri az eltérést (`L.pointer.events`
  `ts`-e), és egy „pontossági” sávot rajzol. **Rím-színező:** a diák kattintással párosítja a
  sorvégeket, a gép megmondja a rímképletet. **Hány szótag?** – egy véletlenszerű sor a 370
  versszakból (a `.md`-ben megadott válogatásból), a diák tippel, a gép számol. **Memoriter-
  mód:** a versszak szavai fokozatosan a kezdőbetűjükre fogynak (`MagVers.fade`).
- **Lépések:** Hallgasd, mint a zenét · Számold meg! · A sor közepe: sormetszet · Dobbants az
  ütemre! · Párban csengő rímek · Négy sor egy versszak – és a Toldiban? · Képek a versben ·
  Összefoglaló.
- **Adatok** (a MEK 01010 szövegéből számolva, 2026-11-24): **27 fejezet, 370 versszak, 1480
  sor**. A gépi szótagszámlálás szerint 1478 sor 12 szótagos, 2 sor 11: „Be tudtam is őt
  szeretni, csodálni!” (14. fejezet) és „Tudja, én vagyok az a kis szomszédlány,” (17. fejezet)
  *(ellenőrizendő egy második kiadással: ha ott is 11, a lecke ezt kimondja és nem „javítja”)*.
  Keletkezés: a szöveg végén „(Pest, 1844, november-december)”. Az első versszak (szótagszám:
  12/12/12/12, rímképlet: aabb): „Tüzesen süt le a nyári nap sugára / Az ég tetejéről a
  juhászbojtárra. / Fölösleges dolog sütnie oly nagyon, / A juhásznak úgyis nagy melege
  vagyon.” A sormetszet: „Tüzesen süt le a | nyári nap sugára”. Szóképek a szövegből:
  metafora „Iluska az, Jancsi szivének gyöngyháza.” (1. fejezet); megszemélyesítés
  „Tatárország hegyes-völgyes tartománya / Messziről nézett a seregnek utána,” (9. fejezet);
  hasonlat „Mint felhő mellett a tündöklő szivárvány.” (a fejezet számát a gyártó ügynök
  keresse ki). A Toldi-összevetéshez a Toldi I. ének 1. versszaka (8 sor, aabbccdd, mind 12
  szótag – Wikisource-szöveg, ellenőrizve).
- **Szöveg és jog:** Petőfi (†1849) és Arany (†1882) közkincs. Forrás: MEK 01010 (*János
  vitéz*), hu.wikisource *Toldi*. A régi írásmód (*Kukoricza*, *kislyány*) marad. Jankovics
  Marcell rajzfilmje (1973) **védett**: a „más médiumbeli megjelenítés” lépés (a kerettanterv
  kéri) legfeljebb a címét említi, képet nem mutat.
- **Építőkocka:** **MagVers** (referencia), MagHang (`click` – ritmus; a 02 előtt elkészülhet,
  ha az ütemhang külön blokkban van).

### 11 · `11-janos-vitez-utja` – Határos-e India és Franciaország? – János vitéz útja

- **Tanulási cél:** Az elbeszélő költemény cselekménye egy utazás, amely a valóságból a mesébe
  vezet: a falu és a puszta valós; Tatárország, Taljánország, Lengyelország, India és
  Franciaország valós név, de mesei földrajz („Taljánországban örökös tél vagyon”,
  „Franciaország és India határos”); az óriások, a sötétség országa és Tündérország már tiszta
  mese. A fordulópontok: Jancsi elűzése, a francia királylány, Iluska halála, a rózsa, az élet
  vize.
- **Kerettanterv:** (10.): „A mű cselekményének megismerése, fő fordulópontjainak értelmezése” ·
  „A mű szövegének közös órai feldolgozása” · (9., tematikus kapcsolat): „A korábban megismert
  műfajokhoz (pl. mese, monda) kapcsolódó elemzési szempontok alkalmazása hasonló témájú
  szövegekben” · (11.): „Irodalmi atlasz vagy térkép használata”.
- **Tévhitek:** „Petőfi nem tudott földrajzot.” (Szándékos mesei játék.) „A *János vitéz* népmese.”
  (Műköltészet, elbeszélő költemény, népmesei elemekkel.) „Az út végig a valóságban játszódik.”
- **Kulcsvizuál:** két térkép egymáson. Alul a valódi világ (TortGlobe/TortMap, `map-vilag.js`),
  rajta a huszárok útvonala a valódi országokon át (Magyarország → Tatárország? → Itália →
  Lengyelország → India → Franciaország), kilométerszámlálóval. Felül egy rajzolt mesetérkép,
  amelyen India és Franciaország „határos”. Egy csúszka áttűnteti a valódi térképet a
  mesetérképbe; a végén az Óperenciás-tenger és Tündérország csak a mesetérképen létezik.
- **Interaktív:** **Fejezet-csúszka (1–27):** a hős jele halad az úton, a panel a fejezet
  címszavát mutatja, a „valóság–mese” mérő pedig fejezetenként mutatja, hol tart az út. A
  diák kattintással kiválasztja a fordulópontokat, és a MagStory-görbe kirajzolja a
  cselekmény ívét. **Mérd le!** – két pont a valódi gömbön, és kiírja a távolságot.
- **Lépések:** Egy falu, egy patak · Huszárnak áll · Tatárország, Taljánország · India és
  Franciaország határos? · Hősként haza – a griffmadár hátán · Iluska rózsája · Óriások,
  boszorkányok, Óperencia · Összefoglaló: a valóságtól a meséig.
- **Adatok** (a MEK 01010 szövegéből kikeresve): 1–3. fejezet: a falu, a patak, a nyáj; 4.:
  Jancsi elindul; 6.: zsiványtanya; 7.: a huszárok; 8.: Tatárország („Tatárországnak már
  elérte közepét”); 9.: Taljánország („Mert Taljánországban örökös tél vagyon”); 10.:
  Lengyelország, India, Franciaország („Franciaország és India határos”); 11–14.: a csata, a
  királylány, Jancsi elmeséli a múltját (14. fejezet: visszatekintés!); 16–17.: hajóút, vihar,
  felhő, griffmadár, haza; 18.: Iluska sírja, a rózsa; 19–20.: Óriásország; 21–22.: a
  sötétség országa, boszorkányok; 23.: „Az óperenciás tenger ez, tudod-e?”; 24.: az óriás
  átviszi; 25–27.: Tündérország, az élet vize, Iluska. A valódi útvonal (gömbi távolság,
  pontonként **becslés**; Tatárország helye bizonytalan – a Krím, kb. 45° É, 34° K):
  Kiskunság → Krím kb. 1140 km → Róma kb. 1760 km → Varsó kb. 1320 km → Delhi kb. 5270 km →
  Párizs kb. 6590 km, **összesen kb. 16 000 km**; Budapest–Párizs légvonalban kb. 1240 km. A falu
  neve a műben nem szerepel *(ellenőrizendő)*.
- **Szöveg és jog:** Petőfi (†1849) közkincs, MEK 01010. Idézet soronként, legfeljebb 2 sor
  egy lépésben.
- **Építőkocka:** TortGlobe vagy TortMap (`map-vilag.js`), MagStory (`arc`, fejezet-csúszka).

### 12 · `12-alfold` – „Felröpűlök ekkor gondolatban” – Petőfi: Az alföld

- **Tanulási cél:** *Az alföld* tájleíró vers, és a felépítése egy kameramozgás. Az elején egy
  ellentét (a „zordon Kárpátok” és az alföld), aztán a költő gondolatban felröppen, és madártávlatból
  nézi a „Dunától a Tiszáig nyúló róna képé”-t. Ezután közelít: gulya, ménes, tanya, nádas,
  csárda, nyárfaerdő, virágok. Végül a látóhatárt nézi, majd visszatér önmagához: „Szép vagy,
  alföld, legalább nekem szép!”. A versben régi és ma ritka szavak is vannak (*gulya*, *ménes*,
  *kútgém*, *délibáb*).
- **Kerettanterv:** (11.): „A táj- és környezetfestés eszközeiként szolgáló nyelvi formák
  megfigyelése lírai és prózai szövegekben” · „A tájhoz, környezethez fűződő érzéseket,
  gondolatokat kifejező szövegek megértése, összehasonlítása” · „A nyelv változó
  természetének megfigyelése különböző példák alapján” · „Az irodalmi szövegek keletkezéséhez,
  megértéséhez, tartalmához kapcsolódó földrajzi kérdések megbeszélése” · „Irodalmi atlasz vagy
  térkép használata” · kötelező: „Petőfi Sándor: Az alföld” · Fogalmak: „hagyomány, napló,
  személyesség, tájleírás, téma, útleírás”.
- **Tévhitek:** „A tájleíró vers csak felsorolja, mit lát.” (Kiválaszt, sorrendet ad, és érzést
  közvetít.) „A délibáb mese.” (Valódi légköri tükröződés.) „A lírai én = a költő.” (Itt
  közel áll hozzá, de a fogalom nem ugyanaz – a panel ezt egy mondatban kimondja.)
- **Kulcsvizuál:** egy panoráma (TortScene), amelyben a kamera a versszakokat követi. Az első
  versszaknál a távoli hegyek elhalványulnak. A harmadiknál a kamera felemelkedik, és alatta
  megjelenik a Duna–Tisza köze (TortMap, `map-karpat.js`: Duna, Tisza, Kecskemét, Kiskunság).
  Ezután versszakonként rázoomol a jelenetre, amelynek elemei a szó elhangzásakor tűnnek fel.
  A hatodik lépés egy kis délibáb-metszet: forró talaj, elhajló fénysugár, az ég tükörképe „tó”
  a földön.
- **Interaktív:** **Szó-nagyító:** a diák a versszak egy régi szavára (*gulya*, *ménes*,
  *kútgém*, *csárda*, *vércse*, *árvalányhaj*) mutat, és a jelenetben kiemelődik, amit a szó
  jelent. **Hang és mozgás:** a szöveg hangutánzó és mozgást kifejező szavai (*kolompol*,
  *zúg*, *dobognak*, *kurjantás*, *pattogása*) kattintásra „megszólalnak” (vizuálisan; hang
  opcionálisan) – híd a 06-os leckéhez. **Kamera-csúszka:** távol ↔ közel.
- **Lépések:** Hegy vagy síkság? · Felröpűlök – madártávlat · A Dunától a Tiszáig ·
  Gulya, ménes, kútgém · Hang és mozgás a tájban · Mi az a délibáb? · „Szép vagy, alföld” ·
  Összefoglaló: távolról közelre, aztán magunkhoz.
- **Adatok** (hu.wikisource *Az Alföld*, ellenőrizve): 12 versszak, 4 soros, mind a 48 sor 10
  szótagos; rímképlet x a x a (*tája – járja*, *világom – látom*); a szöveg alatt: „Pest, 1844.
  július” *(ellenőrizendő egy második kiadással)*. Helynevek a versben: Kárpátok, Duna, Tisza,
  Kis-Kunság, Kecskemét – koordinátájuk az Adatok között (`coord`). Délibáb: alsó délibáb
  (fata morgana egyszerű formája), a forró talaj fölötti ritkább levegő a fényt felfelé hajlítja
  – a lecke ezt egyszerűsítve mutatja, és ki is mondja *(a fizika-sorozat fénytörés-leckéjére
  hivatkozhat)*.
- **Szöveg és jog:** Petőfi (†1849) közkincs. Az egész vers idézhető; a lecke versszakonként
  mutatja. Nagy László *Balatonparton* (†1978) és Weöres Sándor *Tájkép* (†1989) **védett**:
  legfeljebb a címükkel szerepelhetnek egy összevető, saját szavas mondatban.
- **Építőkocka:** TortScene (panoráma, kamera), TortMap (`map-karpat.js`), MagVers (versszak-
  kiírás, kiemelés).

### 13 · `13-pal-utcai-fiuk` – Grund, Füvészkert, csata – A Pál utcai fiúk tere és íve

- **Tanulási cél:** A regény tere két szemben álló hely: a **grund** (a Pál utca és a Mária utca
  közti üres telek a fateleppel) és a **Füvészkert**, a vörösingesek szigete. A cselekmény
  fordulópontjai ehhez a két helyhez kötődnek: a zászló elrablása és visszaszerzése, Nemecsek
  három „vízbe esése”, a csata. Az epikai mű szerkezete (előkészítés, bonyodalom, tetőpont,
  megoldás, végkifejlet) görbeként rajzolható. A végkifejlet kérdést hagy: megérte?
- **Kerettanterv:** (12.): „A cselekmény főbb fordulópontjainak felismerése” · „Főbb
  helyszínek, térbeli viszonyok azonosítása” · „A cselekmény és térszerkezet vizuális
  megjelenítése analóg vagy digitális médiumban” · „A cselekményben megjelenő élethelyzetek,
  erkölcsi konfliktusok azonosítása, véleményalkotás” · „Egyes szereplők jellemzése” ·
  Fogalmak: „Az epikai mű szerkezete: előkészítés, cselekmény, fordulat, bonyodalom, tetőpont,
  megoldás, végkifejlet, helyszín, főszereplő, mellékszereplő”.
- **Tévhitek:** „A tetőpont a regény vége.” „A csata megnyerése a happy end.” (A grundra ház
  épül; Nemecsek meghal.) „A grund kitalált hely.” (Valós környéken van: Józsefváros, Pál utca;
  maga a telek ma nem létezik.)
- **Kulcsvizuál:** vázlatos, saját rajzú **madártávlati térkép** (nem méretarányos, „vázlatos”
  bélyeggel): az iskola, a Pál utca, az Üllői út, a Füvészkert a tóval és a szigettel. Rázoomolva
  a grund alaprajza: farakás-„erődök”, Janó kunyhója, a kerítés, a kapuk. A csata lépésében a két
  sereg mozgása zárt képletű animáció (TortBattle-szerű blokkok, semleges színekkel). Alul a
  szerkezeti görbe: a fejezetcsúszkával együtt halad.
- **Interaktív:** **Fejezet-csúszka (1–10):** a térképen a szereplők és a **zászló** helye
  fejezetenként változik (`MagStory.track`). A diák a görbén kijelöli, hol a bonyodalom, a
  tetőpont és a végkifejlet, és a gép összeveti a `.md` „egy lehetséges besorolásával”. Az
  eltérést nem pontozza hibának, hanem kérdést tesz fel (értelmezés). **Szereplőháló:** a két
  csapat a ranglistával és Geréb átállásával, fejezetről fejezetre.
- **Lépések:** Egy telek Józsefvárosban · A grund · Két csapat · A zászló útja · Háromszor a
  vízben · A csata · Megérte? · Összefoglaló: a regény íve.
- **Adatok:** a regény 10 fejezet; az események ideje 1889 tavasza *(ellenőrizendő a
  szövegben)*; először a *Tanulók Lapja* közölte folytatásokban (1906), könyvként 1907-ben jelent
  meg *(ellenőrizendő: a források 1906-ot és 1907-et is írnak)*. A grund a regény szerint a Pál
  utca és a Mária utca közötti telken volt; a fatelep, Janó kunyhója és a farakások leírását a
  gyártó ügynök a 2. fejezetből vegye ki *(ellenőrizendő)*. Nemecsek vízbe kerülésének
  fejezeteit, a csata tervét és lefolyását a szövegből kell kigyűjteni, nem emlékezetből. A
  szerkezeti besorolás (melyik fejezet a tetőpont) **értelmezés** – a `.md`-ben „egy lehetséges
  besorolás” megjegyzéssel áll. A szereplők listája: Boka János, Nemecsek Ernő, Geréb Dezső,
  Csónakos, Weisz, Kolnay, Barabás, Csele, Richter, Leszik, Áts Feri, Pásztorok, Szebenics,
  Wendauer, Janó, Hektor (a kutya) *(a nevek írásmódját a forrásszövegből ellenőrizni)*.
- **Szöveg és jog:** Molnár Ferenc 1952-ben halt meg, ezért 2023. január 1. óta közkincs
  (Szjt.: a halált követő év elejétől 70 év). Forrás: Project Gutenberg 69689 (az 1916-os
  Franklin-kiadás) – a letöltés idején karbantartás miatt nem volt elérhető, a gyártó
  ügynök próbálja újra, vagy keressen MEK-kiadást. Rövid részletek idézhetők (legfeljebb 2–3
  mondat lépésenként). A Fábri Zoltán-film (1969) és a 2003-as/2005-ös színpadi változatok
  **védettek**: csak megemlíthetők. A térkép saját rajz; az OpenStreetMap adataiból nem
  dolgozunk (ODbL-licenc).
- **Építőkocka:** **MagStory** (referencia: `arc`, `net`, `track`, fejezet-csúszka), saját
  vázlattérkép, TortBattle-minta (a mozgáskulcsokhoz; a blokk átvehető, ha a kevés gyalogos
  „egységhez” illik).

### 14 · `14-walesi-bardok` – „Ötszáz, bizony, dalolva ment” – a ballada

- **Tanulási cél:** A **ballada** dalban elmondott tragikus történet, amelyben egyszerre van
  jelen az epika (történet), a líra (érzés, zene) és a dráma (párbeszéd, feszültség). Jellemző
  rá a **kihagyás**: az események között hézagok vannak, a ki nem mondott rész a **balladai
  homály**. *A walesi bárdok* három bárdja **fokozás**. Arany maga írja a lábjegyzetben, hogy az
  ötszáz bárd kivégzése monda. A műnek van egy elterjedt második olvasata is (1857, Ferenc
  József látogatása) – ez **értelmezés**, és így is mutatjuk be.
- **Kerettanterv:** (14.): „A hősiesség különböző példáit kifejező szövegek megértése és
  összehasonlítása” · „Az irodalmi szövegek keletkezéséhez, megértéséhez, tartalmához
  kapcsolódó történelmi, földrajzi kérdések megbeszélése” · „Az olvasott szöveg szereplőiről,
  a megjelenített élethelyzetekről szóban és írásban véleményt fogalmaz meg” · kötelező:
  „Arany János: Mátyás anyja”, „Arany János: A walesi bárdok” · Fogalmak: „próbatétel,
  ismétlődő motívum, […] ballada, vígballada, népballada, műballada, balladai homály,
  kihagyás” · memoriter: „Arany János: A walesi bárdok (részlet)”.
- **Tévhitek:** „A ballada = szomorú vers.” „A walesi bárdok története megtörtént.” (Arany
  lábjegyzete szerint is vitatott: „A történelem kétségbe vonja, de a mondában erősen tartja
  magát…”.) „A versnek egyetlen jelentése van, és az a rejtett üzenet.” „A kihagyás a költő
  hibája.”
- **Kulcsvizuál:** a vers **színpadként**: a sorok balról jobbra haladó „forgatókönyv-
  sávban” állnak, a beszélők (elbeszélő, Edward, a bárdok, a lakomázó urak) saját színű
  sávot kapnak. A refrén két változata egymás fölött: „Edward király, angol király / Léptet
  fakó lován” → „S Edward király, angol király / Vágtat fakó lován” – egyetlen ige változik,
  és ez mutatja meg, mi történt közben. A tűz jelzésszerű (a hegyoldal izzik), alakok égése
  nem látszik.
- **Interaktív:** **Szereposztás:** a diák a versszakokat a beszélőkhöz húzza, és a gép
  megmutatja a `.md` besorolását. Ahol egy sor beszélője nem egyértelmű, ott a gép nem ítél, és
  ezt meg is mondja. **Hézag-kereső:** két versszak között egy „?” kártya: mi történhetett
  közben? A diák három lehetőség közül választhat, mindhárom elfogadható – a balladai homály
  lényege, hogy a szöveg nem dönt. **Két olvasat:** egy kapcsoló a Wales–1277 és a
  Magyarország–1857 réteg között (TortSource, „monda” és „értelmezés” jelöléssel).
- **Lépések:** Egy király lovagol · Ki beszél? · Néma tartomány · Három bárd · „Ötszáz,
  bizony…” – monda vagy történet? · Ami kimaradt: kihagyás · Két olvasat · Összefoglaló:
  epika, líra, dráma.
- **Adatok** (hu.wikisource, ellenőrizve): a versszakok 4 sorosak, a sorok szótagszáma többnyire
  8/6/8/6, de nem mindenütt (pl. „Van-e ott folyó és földje jó?” – 9 szótag). A lecke ezt
  megmutatja, és nem „javítja”. Rímképlet: x a x a, gyakori **belső rímmel** („Mint akarom, s
  mint a barom”, „Sürgő csoport, száz szolga hord”, „Fegyver csörög, haló hörög”, „Szó
  bennszakad, hang fennakad”). Arany lábjegyzete (szó szerint): „A történelem kétségbe vonja,
  de a mondában erősen tartja magát, hogy I. Eduárd angol király, Wales tartomány meghódítása
  (1277) után, ötszáz walesi bárdot végeztetett ki…”. A keletkezés dátuma: a Wikisource
  szövegének végén „(1856)” áll, a fejléc megjegyzése szerint pedig „1857 júniusában írta”;
  az első megjelenés 1863 *(ellenőrizendő – a dátumeltérést a `.md` megjegyzése rögzítse)*. Az
  1857-es Ferenc József-olvasat anekdotikus hagyományon alapul; a lecke „egy elterjedt
  olvasat” keretben mutatja.
- **Szöveg és jog:** Arany (†1882) közkincs. A *Mátyás anyja* (közkincs) egy
  összehasonlító lépésben jelenhet meg. A sorai 3/3/6 szótagos tördelésűek („Szilágyi /
  Örzsébet / Levelét megirta”), két ilyen sor együtt 12 szótag – ezt a gyártó ügynök
  „megfigyelésként” mutathatja, nem verstani tényként *(értelmezés)*. Kőmíves Kelemen
  (népballada, ajánlott) közkincs népköltészet.
- **Építőkocka:** MagText (forgatókönyv-sáv), MagVers (szótagszám, belső rím), TortSource
  (monda/értelmezés réteg).

### 15 · `15-toldi` – Félkézzel a szekérrúd – Toldi: forrás, szókép, túlzás

- **Tanulási cél:** Arany egy 1574-es verses históriából (Ilosvai Selymes Péter) indult ki: az
  énekek mottója és a ‚…’ jellel jelölt sorok onnan valók. A régi történetet saját képekkel
  töltötte meg. A **hasonlat** (a kútgém olyan, mint egy „óriás szunyog”), a **metafora**
  („szöcskenyájak”) és a **túlzás** (Toldi félkézzel, vízszintesen tartja a nehéz rudat)
  jellemet és hangulatot teremt. Három egymás utáni hasonlat **fokozás**. A 12 ének egy
  **előhanggal** indul, és epizódokra bomlik.
- **Kerettanterv:** (15.): „Az alkotás néhány stíluselemének megfigyelése (pl. verselés,
  szóképek, alakzatok)” · „Az elbeszélő költemény műfaji jellemzőinek felismerése, értelmezése
  a mű vonatkozásában” · „Az olvasás és megértés nyelvi nehézségeinek feltárása,
  szókincsbővítés és olvasási stratégiák fejlesztése” · „Az elbeszélői szerepek (narráció,
  költői kiszólások, rokonszenv) felismerése, értelmezése a jelentésteremtésben” · Fogalmak:
  „verses epika, elbeszélő költemény; s, előhang, epizód, késleltetés; allegória; fokozás,
  túlzás, megszólítás” · memoriter: „Arany János: Toldi (részletek)”.
- **Tévhitek:** „Arany találta ki Toldit.” (Toldi Miklós valós személy volt, a történetét Ilosvai
  már 1574-ben megírta – Arany átírta és kibővítette.) „A túlzás hazugság.” „A hasonlat és a
  metafora ugyanaz.” (A hasonlat kimondja a hasonlítást – *mint*, *képzelné valaki* –, a
  metafora nem.)
- **Kulcsvizuál:** az **Előhang** „pásztortűz”-hasonlata: a sötét pusztán messze egy tűz
  lobog, és lassan Toldi alakjává válik. Ezután a II. versszak kútgémje **átváltozik** óriás

  szúnyoggá, amely az „öreg föld” vérét szívja, majd vissza. Az 5. lépésben Toldi
  vízszintesen tartja a rudat; erőnyilak és egy „becslés” bélyeges kiírás mutatja, mekkora
  forgatónyomaték kellene hozzá.
- **Interaktív:** **Szókép-kapcsoló:** „szó szerint ↔ képként” (szöcskenyáj, kútgém–szúnyog,
  vas kéz). **Rúd-csúszka:** a diák állítja a rúd hosszát és tömegét (becslésként), a gép
  kiírja, hány kilót kellene egy kinyújtott karral tartani, hogy ugyanekkora legyen az erőhatás
  – a túlzás így mérhetővé válik. **Ilosvai-réteg:** egy kapcsolóval kiemelődnek a ‚…’ jelű
  sorok (TortSource: „forrás 1574” ↔ „Arany 1846”). **Ének-csúszka:** a 12 ének epizódjai
  sávon (MagStory `strip`).
- **Lépések:** Egy tűz a messzeségben (előhang) · Honnan vette Arany? · Dél a pusztán · Óriás
  szunyog a kútnál · Félkézzel a rúd · Bika, éjfél, vadkan · A tizenkét ének · Összefoglaló.
- **Adatok** (hu.wikisource *Toldi*, ellenőrizve): az előhang első sorai: „Mint ha pásztortűz
  ég őszi éjszakákon, / Messziről lobogva tenger pusztaságon: / Toldi Miklós képe úgy lobog fel
  nékem / Majd kilenc-tíz ember-öltő régiségben.” Az előhang mottója: „‚Mostan emlékezem az
  elmult időkről, / Az elmult időkben jó Tholdi Miklósról…’ Ilosvai”; az I. ének mottója:
  „‚Nyomó rúdat félkezével kapta vala, / Buda felé azzal utat mutatja vala.’ Ilosvai”. Arany
  saját jegyzete: „Az ezen ‚_’ jeggyel felhozott helyek Ilosvaiból vannak átvéve. A. J.”. Az I.
  ének 1. versszaka: „Ég a napmelegtől a kopár szík sarja, / Tikkadt szöcskenyájak legelésznek
  rajta;”; a 2. versszaka: „Ösztövér kútágas, hórihorgas gémmel / Mélyen néz a kútba s benne
  vizet kémel: / Óriás szunyognak képzelné valaki, / Mely az öreg földnek vérit most szíja ki.”;
  a 10. versszakban a rúd („Azzal a nehéz fát könnyedén forgatja, / Mint csekély botocskát,
  véginél ragadja; / Hosszan, egyenesen tartja félkezével”); a 14. versszakban a három hasonlat
  („Mint komor bikáé, olyan a járása, / Mint a barna éjfél, szeme pillantása, / Mint a sértett
  vadkan, fú veszett dühében,”). Szótagszám: az I. ének 112 verssora mind 12 szótagos (a mottók
  nélkül), versszakonként 8 sor, rímképlet aabbccdd. Ilosvai históriája 1574-ben jelent meg;
  Arany Toldija 1846-ban készült (a Kisfaludy Társaság pályázatára), és 1847-ben jelent meg
  *(ellenőrizendő)*. Toldi Miklós a 14. században élt, Nagy Lajos király idején (1342–1382)
  *(ellenőrizendő)*. A rúd-becslés: hossza kb. 4–6 m, tömege kb. 20–40 kg *(becslés)*; a végénél
  vízszintesen tartva a forgatónyomaték m · g · L/2, például 30 kg · 9,81 m/s² · 2,5 m ≈ 740 N·m
  – ennyi kellene ahhoz is, hogy valaki kinyújtott karral (kb. 0,7 m) egy kb. 107 kg-os tárgyat
  tartson. A panel mondja ki: becslés, a túlzás érzékeltetésére. Az énekek epizódjait (a
  malomkő, a farkasok, Bence, a bika, a cseh vitéz) és a sorszámukat a gyártó ügynök a szövegből
  ellenőrizze.
- **Szöveg és jog:** Arany (†1882) és Ilosvai (16. század) közkincs. A lecke versszakonként
  idéz.
- **Építőkocka:** MagVers, MagStory (`strip`), TortSource; a rúd-becslés saját kis rajz
  (vektornyilak).

### 16 · `16-himnusz-szozat` – Mit mesél a Himnusz? – Himnusz és Szózat

- **Tanulási cél:** A *Himnusz* imádság: **Istenhez** szól, a *Szózat* buzdító beszéd: **a
  magyarhoz** (híd a 01-es lecke kommunikációs modelljéhez). A *Himnusz* történelmi képeket
  sorol fel, de **nem időrendben**: a 2–3. versszak az áldásokat (honfoglalás, bőség, Mátyás),
  a 4–7. a csapásokat (tatár, török, belviszály, pusztulás) gyűjti egybe. Az első és az utolsó
  versszak keretet alkot („Isten, áldd meg a magyart” → „Szánd meg Isten a magyart”). Formája:
  7 és 6 szótagos sorok, **keresztrím** (abab).
- **Kerettanterv:** (16.): „A szeretet, szerelem, hazaszeretet különböző példáit kifejező
  szövegek megértése és összehasonlítása” · „A téma megjelenítését különböző korokban és
  műfajokban szolgáló nyelvi formák elkülönítése lírai és prózai szövegekben” · kötelező:
  „Kölcsey Ferenc: Himnusz”, „Vörösmarty Mihály: Szózat” · Fogalmak: „líra, lírai alany, lírai
  én, téma, motívum; versforma, rímszerkezet, keresztrím, alliteráció” · memoriter: „Kölcsey
  Ferenc: Himnusz (1-2. vsz.)”, „Vörösmarty Mihály: Szózat (1. és 2. vsz.+13.,14. vsz.)”.
- **Tévhitek:** „A Himnusz időrendben meséli el a történelmet.” „A Himnusz és a Szózat ugyanazt
  mondja.” „A Himnusznak csak egy versszaka van.” (Nyolc van; a himnuszként énekelt szöveg az
  első versszak.) „A *Szózat* címzettje Isten.”
- **Kulcsvizuál:** egy időszalag (TortTimeline), amelyre a versszakok képei sorban felkerülnek
  a leírás helyére: 2. versszak → honfoglalás (895 körül); 3. → Mátyás és Bécs (1485); 4. →
  tatárjárás (1241–1242), majd a török; 5. → török győzelmek, belviszály; 6–7. → bujdosók,
  romok. A versszakokból az időszalagra húzódó szálak összekuszálódnak – ebből látszik, hogy a
  vers nem időrendet követ, hanem két csoportot (áldás, csapás). Mellette a 01-es lecke modellje:
  feladó → címzett (Isten, illetve a magyar).
- **Interaktív:** **Versszak → idő:** a diák a versszakokat az időszalagra húzza, és a gép a
  `.md` értelmezése szerint visszajelez. Ahol több olvasat is lehetséges (5–6. versszak), azt
  „értelmezés” jelöli, és nincs egyetlen „jó” megoldás. **Rím-színező** (MagVers, abab). **Kihez
  beszél?** kapcsoló a Himnusz és a Szózat között. **Memoriter-mód** a megadott versszakokra.
- **Lépések:** Kihez beszél? · Hét és hat: forma és keresztrím · Áldások · Csapások · Nem
  időrendben! · A keret: áldd meg – szánd meg · A Szózat: hűség és két jövő · Összefoglaló.
- **Adatok** (hu.wikisource, ellenőrizve): a *Himnusz* 8 versszak × 8 sor = 64 sor,
  szótagszám 7/6 váltakozva (mind a 64 sor), rímképlet abab („magyart – kart”, „bőséggel –
  ellenséggel”). Az időszalag pontjai: honfoglalás 895 körül *(becslés)*; Mátyás elfoglalja
  Bécset: 1485; tatárjárás: 1241–1242; Buda eleste: 1541. A „Bendegúznak vére” a hun–magyar
  rokonság **krónikás hagyományára** utal (a történelemsorozat szerkesztői elve szerint
  hagyományként jelöljük). A keletkezés: 1823. január 22., Cseke; Erkel Ferenc zenéje: 1844;
  a *Szózat*: 1836, Egressy Béni zenéje: 1843 *(ellenőrizendő)*. A *Szózat* 14 versszak, a
  sorok 8/6 szótagosak; az első versszak: „Hazádnak rendületlenűl / Légy híve, oh magyar; /
  Bölcsőd az s majdan sírod is, / Mely ápol s eltakar.” A versszakok és korszakok párosítása
  **értelmezés**, a `.md`-ben megjegyzéssel.
- **Szöveg és jog:** Kölcsey (†1838) és Vörösmarty (†1855) közkincs. A nemzeti jelképnek
  kijáró tisztelettel: a lecke nem tréfál, nem torzítja a szöveget, nem teszi
  ritmusjátékká (a kopogás itt nincs), a rím-színezés visszafogott.
- **Építőkocka:** TortTimeline, MagVers, a 01-es lecke modelljének rajza (lecke-specifikus
  másolat).

### 17 · `17-egri-csillagok` – Ki kicsoda, mikor? – az Egri csillagok szálai

- **Tanulási cél:** A **történelmi regény** valós eseményekbe kitalált szereplőket és szálakat
  sző. Az *Egri csillagok* öt része kb. húsz évet fog át (1533 → 1552), és a szereplők
  kapcsolatai (barát, ellenség, család, szerelem) közben változnak. A cselekmény **több
  szálon fut**, és ezek Egerben futnak össze. Egy tárgy – Jumurdzsák gyűrűje – végigköveti a
  szálakat. Ami a regényben áll, nem forrás: az ostrom történetét a 16-eger történelemlecke
  mutatja be, ez a lecke a regény szerkezetéről szól.
- **Kerettanterv:** (17.): „A főbb szereplők kapcsolatának értelmezése” · „A szereplők közötti
  kapcsolatok vizuális megjelenítése analóg vagy digitális médiumban” · „A cselekmény
  fordulópontjainak összekapcsolása a műfaj jellegzetességeivel” · „Szövegalkotás az egyes
  szereplők nézőpontjának megjelenítésével” · Fogalmak: „történelmi regény, elbeszélő,
  időszerkezet, több szálon futó cselekmény, jellemek”.
- **Tévhitek:** „Az *Egri csillagok* minden része megtörtént.” „Jumurdzsák valós személy.”
  „Gergely és Éva története Tinódi énekében is benne van.” „A regény az ostrommal kezdődik.”
- **Kulcsvizuál:** **szereplőháló az időben:** vízszintesen az idő (1533–1552, az öt rész
  sávjaival), rajta a szereplők szálai (Gergely, Éva, Jumurdzsák, Dobó, Mekcsey, Török Bálint
  …). A szálak összefutnak és szétválnak, a kapcsolatok színes ívek. A gyűrű egy fénypont,
  amely egyik szálról a másikra ugrik. Egy kapcsoló minden szereplőt és eseményt **valós** vagy
  **kitalált** jellel lát el (a 16-eger lecke rétegjelöléseivel: forrás / regény).
- **Interaktív:** **Idő-csúszka:** a háló az adott pillanatot mutatja (ki ismer kit, ki hol
  van). **Kövesd a gyűrűt!** – a diák megjósolja, kinél lesz a gyűrű a következő részben, és a gép
  megmutatja. **Valós vagy kitalált? (TortCards).** **Nézőpontváltás:** egy jelenet rövid,
  saját szavas összefoglalója két szereplő szemével (a kerettanterv kéri: „Szövegalkotás az
  egyes szereplők nézőpontjának megjelenítésével” – a lecke a feladatot adja, nem írja meg
  helyette).
- **Lépések:** Öt rész, húsz év · Két gyerek az erdőben · Ki kit ismer? (szereplőháló) · Egy
  gyűrű útja · Több szál, egy cél: Eger · Valós vagy kitalált? · Kinek a szemével? ·
  Összefoglaló.
- **Adatok:** a részek címei: I. „Hol terem a magyar vitéz?”, II. „Oda Buda!”, III. „A rab
  oroszlán”, IV. „Eger veszedelme”, V. „Holdfogyatkozás”, majd Befejezés (MEK-
  tartalomjegyzék szerint) *(a részek időpontjait – kb. 1533, 1541, …, 1552 – a gyártó ügynök a
  szövegből ellenőrizze)*. Megjelenés: folytatásokban 1899-ben a *Pesti Hírlap*ban, könyvként
  1901-ben (a 16-eger lecke `.md`-je szerint). Az ostrom: 1552. szeptember 9. – október 18.
  körül (a 16-eger adatai, onnan átvéve, nem újraszámolva). A szereplők kapcsolatai `rel`
  típusú adatként (5. fejezet), forrásszöveg szerint. Valós személy: Dobó István, Mekcsey
  István, Bornemissza Gergely (a regénybeli élettörténete nagyrészt kitalált), Török Bálint,
  Tinódi Lantos Sebestyén; kitalált: Jumurdzsák és a gyűrű története (a 16-eger lecke
  megjegyzése szerint) *(a többi szereplőt ellenőrizni)*.
- **Szöveg és jog:** Gárdonyi (†1922) közkincs. Forrás: MEK 13387 vagy Gutenberg 76235/76236.
  Rövid részletek idézhetők. A Várkonyi Zoltán-film (1968) **védett**: csak megemlíthető. Az
  oszmán szereplőket a regény korának ábrázolása szerint, de leíró keretben mutatjuk („a
  regényben…”), ellenségkép nélkül (lásd a történelemterv 4. fejezetének 8. pontját).
- **Építőkocka:** MagStory (`net` időben, `track`), TortTimeline, TortSource/TortCards.

---

## 4. Közös modulok

### Modulok

| Modul | Mit tud | Lecke | Első megépítés |
|---|---|---|---|
| **A · Szöveg** (`MagText`) | szöveg betű/szótag/szó szintű tokenekre bontása (44 betűs ábécé, többjegyű betűk, magyar szótagolás), mért elrendezés tördeléssel, kiemelés/halványítás, írás ↔ [ejtés] morf (a betűk elrepülnek, átrendeződnek), tokenre kattintás, magyar betűrend-összehasonlítás, hangrend | mind | **04** |
| **B · Szóelem** (`MagMorph`) | színkódolt szóelem-csempék (tő, képző, jel, rag, kötőhangzó), húzható láncolás sorrend-ellenőrzéssel, toldalékváltozatok (*-ban/-ben*, *-hoz/-hez/-höz*) illeszkedési „átpattanással”, hasonulás-megjelenítés tulajdonság-jelvényekkel; az alakok a `.md`-ből jönnek – **a modul nem ragoz, csak mutat és ellenőriz** | 04, 05, 07, 08 | **04** |
| **C · Verstan** (`MagVers`) | verssor szótagolása (szóhatáron át), szótagszám-pöttyök, sormetszet, ütemkezdetek, rímpárok színezése és rímképlet, időmérték (hosszú/rövid, verslábak illesztése – a tartaléklecke miatt), dobbantós játék pontosságméréssel, memoriter-mód | 10, 12, 14, 15, 16 | **10** |
| **D · Hang** (`MagHang`) | Web Audio: dúdolt dallam (`hum`), formánsszintézis (`vowel`), zörej és zöngés zörej (`noise`), ütem-kopogás (`click`); a szájüreg oldalmetszete (`tract`) és a magánhangzó-négyszög (`vowelChart`); csak kattintásra hoz létre hangkontextust, hang nélkül is teljes | 01, 02, 05, 10 | **10** (`click`), **02** (`tract`, `vowel`, `noise`), **01** (`hum`) |
| **E · Cselekmény** (`MagStory`) | szerkezeti görbe (előkészítés … végkifejlet) fejezetekre vetítve, szereplőháló adott időpontban (élek: barát / ellenség / család / szerelem, időben változó), tárgykövetés (zászló, gyűrű), funkciósáv (mese, énekek), történetidő ↔ elbeszélési idő ábra (visszatekintés, késleltetés), fejezet-csúszka | 09, 11, 13, 15, 17 | **13** |
| **Átvett (történelem)** | TortMap + `map-vilag.js`/`map-karpat.js` (11, 12), TortGlobe (11), TortTimeline (16, 17), TortSource (14, 15, 17), TortCards (05, 06, 07, 09, 17), TortScene (06, 09, 12), TortBattle-minta (13) | – | megvan |
| **Közös UI** | „régi írásmód”, „értelmezés”, „vázlatos”, „becslés” bélyeg; ▶ hanggomb; „Egy lehetséges olvasat” keret | mind | 04 + menet közben |

Saját, nem általánosított rajzok: járásanimáció (06), égig érő fa (09), délibáb-metszet (12),
grund-térkép (13), rúd-nyomaték (15).

### API-vázlatok

A modulok a bevált mintát követik: a leckén belül, külön blokkban készülnek
(`/* ── MODUL: Szöveg (MagText) · forrás: magyar-5-6/04-toldalek, 2026-… ── */ … /* ── MODUL VÉGE ── */`),
saját névtérrel, a blokk elején API-leírással, és csak a Lesson motorra épülnek. Minden
felirat `{s, k}` párként érkezik, és **csak** `L.tx`/`L.pill`-lel kerül a vászonra (QA, review
mód). A minimális betűméret: tokenszövegnél 26 px, kis jelzéseknél (szótagszám-pötty felirata,
ütemjel) 22 px.

**A · MagText**
```
MagText.letters('csiga') → ['cs','i','g','a']          // 44 betűs ábécé; 'dzs' > 'dz' > 'd'; a „|” jel a
                                                       //   szóelemhatárt jelzi, és felülírja a betűfelismerést
                                                       //   (kis|szék: s + sz, nem ssz)
MagText.syllabify('asszony') → ['asz','szony']         // magánhangzónként egy szótag; egy msh. → következő szótag;
                                                       //   torlódásnál csak az utolsó; többjegyű betű egység;
                                                       //   kettőzött többjegyű (ssz) → sz|sz; „·” kézi felülírás
MagText.vowels(s) → [{i, v, long}]   MagText.harmony('papír') → 'mély' | 'magas' | 'vegyes'
MagText.collate(a, b) → −1 | 0 | 1                     // magyar betűrend (2 menet: a=á, majd rövid < hosszú)
const T = MagText.create(L, {font: {f, s, w}, lh})
T.tokens(s, 'betű' | 'szótag' | 'szó', {k}) → [{s, i, x, w, kind}]
T.layout(tokens, {x, y, w, a}) → lines                 // mért tördelés szóhatáron (nincs fix doboz)
T.draw(lines, {hi: {i: szín}, dim: .2, reveal: 0..1, under: {i: szín}, a})
T.morph(linesA, linesB, u)                             // írás ↔ [ejtés]: azonos betűk helyben, új betűk beúsznak
T.pick(px, py) → token | null
```

**B · MagMorph**
```
const M = MagMorph.create(L, {colors: MagMorph.KINDS, font})   // KINDS: tő, képző, jel, rag, kötőhangzó (7. fejezet)
const w = M.word(L.dat('kertészeknek'))                // a build „morph” adatából: [{s, k: 'tő'|…, alt?: ['nek','nak']}]
M.draw(w, {x, y, u: 0..1 (összeállás), gap: 0..1 (szétnyitás), hi, labels: true, a})
M.chain(L, {x, y, stem, tiles: [...], onChange})       // húzható csempék; a rossz sorrend visszapattan, why-szöveggel
M.pick(stem, alt, exceptions) → 'nek'                  // illeszkedés: az utolsó nem semleges magánhangzó dönt;
                                                       //   i, í, é a mély mellett semleges; kivételek a .md-ből
M.check(w) → {ok, why: {s, k}}                         // sorrend: tő < képző* < jel* < rag?
M.assim(a, b, {feature: 'zönge' | 'hely' | 'teljes' | 'összeolvadás', t}) // két hangcsempe tulajdonság-jelvénnyel
```

**C · MagVers**
```
const V = MagVers.create(L, {lines: [{s, k}], meter: '12/6' | '7-6' | '8-6' | '10' | 'hexameter' | 'pentameter',
                             rhyme: 'aabb', font})     // a sorok a .md „### Idézet” blokkjából, a meter/rhyme adatból
V.syl(i) → [{s, x, w, v, long}]                        // a long: hosszú magánhangzó VAGY ≥ 2 mássalhangzó követi
                                                       //   (szóhatáron át is; többjegyű betű = 1, kettőzött = 2);
                                                       //   a sorvégi szótag: ×
V.draw({x, y, s, show: {count, cut, beats, rhyme, qty}, hi, reveal, fade, a})
V.beats(i, {tempo}) → [{syl, t, strong}]               // ütemkezdetek; a felező 12-nél 6|6 (opcionálisan 3+3)
V.tapScore(events, t0, beats) → {hits, miss, ms: [...]} // L.pointer.events[].ts alapján
V.rhymes() → [{a, b, letter, kind: 'tiszta' | 'asszonánc' | '?'}]
V.feet(i, 'hexameter') → {feet: ['— ∪ ∪', …], ok}      // tartalék: időmérték
V.fade(u)                                              // memoriter: 0 teljes → 1 csak kezdőbetűk (a sorrend
                                                       //   determinisztikus: seedelt U.rng, szóhosszal súlyozva)
```

**D · MagHang**
```
MagHang.button(L, k, play)        // ▶ gomb (L.button); az AudioContext csak az első kattintáskor jön létre
MagHang.ready() → bool            // a rajz NEM függhet tőle (QA headless: nincs hang)
MagHang.hum(contour: [[t, Hz], …], {dur, vol})          // dúdolt dallam: háromszögjel + burkoló
MagHang.vowel({F1, F2, F3, f0, dur})                     // fűrészjel → 3 párhuzamos sáváteresztő szűrő
MagHang.noise({band: [lo, hi], voiced: bool, f0, dur})  // réshangok (sz/z, f/v)
MagHang.click(times, {strong: [...], vol})               // ütemkopogás (erős/gyenge)
MagHang.tract(c, {x, y, s, tongue: {fb: 0..1, hl: 0..1}, lips: 0..1, glottis: 0..1, t, hi, labels})
MagHang.vowelChart(c, box, {pt: [fb, hl], hi, k})        // a négyszög koordinátái a .md-ből
MagHang.formants(fb, hl, lips) → {F1, F2}                // a .md formánstáblájából interpolálva
```
A hang **sosem** indul magától (böngésző-szabály is), a hangerő alapból mérsékelt, a hang
nélküli képen ugyanaz az információ látszik (dallamvonal, pöttyök, kopogássáv).

**E · MagStory**
```
const S = MagStory.create(L, {units: [{id, name: {s, k}, t (történetidő: év/nap), n (szöveghossz)}],
                              chars: [{id, name: {s, k}, side?, real?}], places: [{id, name, x, y}]})
S.arc(c, box, {phases: [{at, name: {s, k}}], u, mark, a})   // szerkezeti görbe; mark: a diák jelölései
S.net(c, box, {at, edges: L.dat('kapcsolatok'), hi, a})     // az „at” időpontban élő élek; csomópont-elrendezés
                                                            //   determinisztikus (seed), a fejezetek között zárt
                                                            //   képlettel tűnik át
S.lanes(c, box, {from, to, u})                              // szereplők szálai az időben (Egri csillagok)
S.track(c, {path: [{at, char | place}], u})                 // tárgy útja (zászló, gyűrű) fénypontként
S.strip(c, box, {cells: [{name: {s, k}, icon}], u, hi})     // funkciósáv / énekek sávja
S.timing(c, box, {u})                                       // történetidő ↔ elbeszélési idő (visszatekintés: 11/14. fejezet)
S.slider(L, k, n) → csúszka a fejezetekhez/részekhez
```

### Referencialeckék (első kör)

1. **`04-toldalek` → MagText + MagMorph.** A nyelvtani gerinc; négy nyelvtanlecke épít rá, és a
   MagText minden leckében benne van. Itt dől el, hogy a `morph` adattípus és a csempék
   „átpattanása” tanár által javíthatóan működik-e.
2. **`10-janos-vitez-vers` → MagVers (+ MagHang `click`).** Öt irodalomlecke épít rá. Itt dől
   el, hogy a szótagolás és a hosszúság szóhatáron át helyes-e. A próba: a 1480 sorból 1478
   tizenkét szótagos (a build és a modul ugyanazt adja?). A dobbantós játék időmérése is itt
   dől el.
3. **`13-pal-utcai-fiuk` → MagStory.** Négy lecke épít rá. Itt dől el, hogy a szereplőháló
   időbeli átmenete és a tárgykövetés zárt képlettel, determinisztikusan (QA `--det`) megy-e.

A MagHang hangszintézise (`tract`, `vowel`, `noise`) a 2. körben, a `02-beszedhang`-ban épül.
Ez a legkockázatosabb hangmunka, de csak két lecke függ tőle, ezért nem kell az első körben.

### Gyártási sorrend

A másik sorozattal (Természettudomány 5–6.) együtt legfeljebb 5 al-ügynök fut; ebből a
sorozatból kötegenként legfeljebb 3 lecke. A koordinátor oszthatja 2 + 3-ra.

| Köteg | Leckék | Új modul | Újrahasznosított |
|---|---|---|---|
| 0 | build- és szerződés-előkészítés (5. fejezet, P-M) | – | – |
| 1 | **04-toldalek** (3), **10-janos-vitez-vers** (3), **13-pal-utcai-fiuk** (3) | MagText, MagMorph (04) · MagVers, MagHang-click (10) · MagStory (13) | TortBattle-minta |
| 2 | **02-beszedhang** (3), **05-hasonulas** (2), **11-janos-vitez-utja** (2) | MagHang-szintézis, -metszet (02) | MagText, MagMorph, TortCards, TortGlobe/TortMap, MagStory |
| 3 | **01-kommunikacio** (2), **07-dorlak** (2), **15-toldi** (2) | MagHang-hum (01) | MagText, MagMorph, TortCards, MagVers, MagStory, TortSource |
| 4 | **03-hang-betu-fonema** (2), **08-ige** (2), **16-himnusz-szozat** (2) | – | MagText, MagMorph, MagVers, TortTimeline |
| 5 | **06-kullog-lolab** (2), **09-nepmese** (2), **12-alfold** (2) | – | TortScene, TortCards, MagStory, TortMap, MagVers |
| 6 | **14-walesi-bardok** (2), **17-egri-csillagok** (3) | – | MagVers, MagText, MagStory, TortTimeline, TortSource, TortCards |

Az 1. köteg a három gerincmodul. A 2. kötegben van a hangszintézis és a két gerinc első
újrafelhasználása. A **15-toldi** és a **17-egri-csillagok** azért nem kerül előre, mert a
forráskezelés és az olvasat-jelölés (TortSource + `> értelmezés:`) addigra kiforr. A **14** és a
**16** (értelmezésre érzékeny, nemzeti jelkép) a tanári review-hoz a legkésőbbi kötegekbe kerül,
így a review-tapasztalat már beépülhet. A szófajlecke (07) a nyelvtan-gerinc után jön, mert
kitalált szavai külön review-t kérnek.

---

## 5. Build- és szerződés-kiegészítési igények

**Előfeltétel (0. köteg, „P-M”, kb. 30–40 perc, mint a korábbi P1): a build
(`tools/build_lesson.py`) bővítése.** Ha nem készül el időben, az 1. köteg a meglévő típusokkal
és `<!-- -->` megjegyzésekkel dolgozik, és a jelentésében jelzi, mire lenne szükség.

1. **Új blokk: `### Idézet`** (a `### Feliratok` mellett, bármely `##` alatt). Soronként
   `- kulcs: szöveg`, a kulcs olvasható (`jv 1/1`, `toldi I/2/3`). A blokk **előtt** kötelező a
   forrásmegjegyzés:
   `<!-- idézet: Petőfi Sándor: János vitéz (1844), 1. fejezet 1–4. sor · szöveg: MEK 01010 · szerző † 1849 · közkincs -->`.
   A build hibát ad, ha a megjegyzés hiányzik, vagy ha a † évszám + 70 ≥ az aktuális év
   („védett szerző: legfeljebb cím és saját szavas összefoglaló”). Ha a megjegyzés „népköltészet”
   vagy „jogszabály” (a kerettanterv szövege), a † év nem kell, de a **gyűjtő/kiadás** igen
   (`gyűjtő † 1898`). A blokk sorai a lecke számára `L.quote(k)`-ként érhetők el, a review mód is
   látja őket.
2. **Verssor-ellenőrzés** a specben: `"quotes": {"jv 1/1": {"syll": 12, "cut": 6}}` vagy egy
   blokkra: `"quoteSets": {"jv": {"syll": 12, "cut": 6, "rhyme": "aabb"}}`. A build megszámolja
   a magánhangzókat (a, á, e, é, i, í, o, ó, ö, ő, u, ú, ü, ű; az *y* csak akkor magánhangzó, ha
   a spec `"yVowel"` listája tartalmazza a szót – régi nevekben, pl. *Kölcsey*, nem az). Ha a
   szótagszám eltér, **hibát** ad, kivéve, ha a sor mellett ott a megjegyzés
   `<!-- szótagszám: 11, a forrásban is -->` – ilyenkor csak figyelmeztet. A sormetszet
   ellenőrzéséhez a sorban `|` állhat („Tüzesen süt le a | nyári nap sugára”). A build a `|`-t
   eltávolítja a megjelenített szövegből, és ellenőrzi, hogy előtte 6 szótag van. A rímképlet
   (`aabb`) sorainál a build megnézi, csengenek-e a sorvégek magánhangzói. Ha nem, csak
   figyelmeztet (a tanár dönt).
3. **Időmérték** (a tartaléklecke miatt, de a MagVers-szel együtt érdemes megírni):
   `metrum` adattípus, „— ∪ ∪ | — ∪ ∪ | — — | — — | — ∪ ∪ | — ×” → `{t: 'meter', feet: [...]}`. A
   build kiszámolja a sor hosszúsági mintáját (hosszú, ha hosszú a magánhangzó, vagy legalább két
   mássalhangzó követi, szóhatáron át is; a többjegyű betű egy, a kettőzött kettő), és
   figyelmeztet, ha eltér a megadottól. A teszteset: Kölcsey *Huszt*ja (8 sor, váltakozó
   hexameter és pentameter).
4. **`morph` adattípus** (szóelemek): „kert + ész (képző) + ek (jel) + nek (rag)” →
   `{t: 'morph', s: 'kertészeknek', parts: [{s: 'kert', k: 'tő'}, …]}`. A fajták zárt
   listából: tő, képző, jel, rag, kötőhangzó, előtag (összetett szóhoz: „virág (tő) + cserép
   (tő) + ben (rag)”). A build ellenőrzi a sorrendet (rag után nem jön jel vagy képző),
   figyelmeztet, ha a toldalék hangrendje nem illik a tőhöz (kivétel: `<!-- ingadozó -->`).
   Változatlista: „-ban/-ben (rag)” → `alt: ['ban', 'ben']`.
5. **`pron` adattípus** (írás + ejtés): „kútba [kúdba]” → `{t: 'pron', w: 'kútba', p: 'kúdba'}`.
   A build hibát ad, ha hiányzik a szögletes zárójel, és figyelmeztet, ha a kettő azonos.
6. **`rel` adattípus** (szereplőkapcsolat): „Gergely – Éva: szerelem (I–V)” → `{t: 'rel', a,
   b, kind, from, to}`. A `kind` zárt listából (barát, ellenség, család, szerelem, szolgál,
   vezet), a `from`/`to` egység-azonosító vagy római szám. A spec megadja az egységek listáját,
   és a build szól, ha egy hivatkozott szereplő vagy egység nem létezik.
7. **`> értelmezés:` doboz** a panelen (a `> megjegyzés:` mintájára), saját stílussal és a
   felirattal: „Egy lehetséges olvasat”. Beleszámít a szókorlátba. A spec `"interpretive": true`
   esetén a build figyelmeztet, ha a leckében nincs legalább egy ilyen doboz vagy egy kérdéssel
   végződő lépés.
8. **`"maxWords": 45`** minden leckében (meglévő kapcsoló).

**A QA (`tools/qa_lesson.py`) bővítése:**

9. **Hangpróba:** figyelmeztetés, ha az oldal felhasználói kattintás nélkül létrehoz egy
   `AudioContext`-et (a betöltéskor és minden lépésbelépéskor ellenőrizve).
10. **Glifpróba bővítése:** a ∪, —, ×, ‚ ’ (Ilosvai-jel), ő, ű és a „[ ]” mind meglegyen a
    fontokban. A ∪ valószínűleg csak az F1 matematikai fontkészletéből jön; a QA szóljon, ha
    tartalékfontra esik.
11. **Verssor-túlcsordulás:** a hosszú idézett sorok (a felező tizenkettes 26–28 px-en kb. 640–760
    px széles) a meglévő túlcsordulás-vizsgálattal megfognak. Nem kell új ellenőrzés, csak a
    `max` használata kötelező (7. fejezet).

**Közös könyvtár:** `shared/magyar/` (a modulok, az első két köteg átnézése után,
egyeztetve). A szövegforrásokat (MEK/Wikisource) **nem** tesszük a repóba fájlként: a
lecke `### Idézet` blokkjában csak a felhasznált sorok vannak.

**A szerződés kiegészítése:** a 7. fejezet kész szövege a `SZERZODES.md` új, 18. fejezeteként
(a 17. a Természettudomány-kiegészítés).

---

## 6. Lefedettség

| Témakör (óra) | Leckék | Fontos, **nem lefedett** fejlesztési feladat / altéma |
|---|---|---|
| 1. A kommunikáció alapjai (6) | 01 | a szerep- és drámajáték, az aktív részvétel kommunikációs helyzetekben (tanórai); a megszólítás, bemutatkozás, kérés illemszabályai csak a 01 csatorna-lépésében; országunk jelképei (ajánlott) |
| 2. Helyesírás, nyelvhelyesség (8) | 03, 05 | a helyesírási szótárak és portálok használata (gyakorlat); a „határozóragok megfelelő használata” (pl. *-ba/-ban*) csak példaként |
| 3. Állandósult szókapcsolatok (5) | 06 | a digitális kommunikáció szókapcsolatai; a szólások eredetének részletes története (védett forrásmunkák) |
| 4. Nyelvi szintek (20) | 02, 03, 04, 05 | a madárnevek és a madárhangok összevetése, a személynévadás (ajánlott); a szóalkotási módok közül csak az összetétel és a képzés; az idegen elemű összetett szavak |
| 5. Hangalak és jelentés (6) | 06 | a jelentésmező fogalma csak érintőlegesen; a nyelvi humor (szójáték) csak egy példában |
| 6. Szövegértés és szövegalkotás (13) | – (17: nézőpont-feladat; 13: jellemzés-szempontok) | **szándékosan nem animálva:** felelet, vázlat, leírás, elbeszélés, levél, e-mail, plakát, meghívó, könyvismertető – ezek írásgyakorlatok |
| 7. Könyv- és könyvtárhasználat (4) | – | **szándékosan kimarad:** a kerettanterv maga is gyakorlati foglalkozást (könyvtár, múzeum) javasol; a katalógus és a sajtótermékek szerkezete akár egy tartaléklecke témája lehet |
| 8. Szófajok (46) | 07, 08 | **a névszók helyesírása** (személynevek, földrajzi nevek, intézménynevek, címek, díjak), **a számnevek helyesírása**, a névmások fajtái egyenként, a viszonyszók és a mondatszók részletesen – arányaiban ez a legkevésbé lefedett témakör (3–5. tartalék) |
| 9. Család, otthon, nemzet (18) | 09 | **a lírai darabok** (Petőfi: *Egy estém otthon*, *Füstbe ment terv*, *Magyar vagyok*; Arany: *Családi kör*; Weöres, Kányádi – védettek), a bibliai történetek (csak a 09 monda/mítosz-összevetésében); a *Családi kör* „filmként” a 6. tartalék |
| 10. János vitéz (14) | 10, 11 | az alakzatok (párhuzam, ellentét) csak röviden; a más médiumbeli feldolgozások (rajzfilm, daljáték) összevetése csak említéssel, mert védettek |
| 11. Szülőföld, táj (8) | 12 | *Szülőföldemen*, *Úti levelek* (közkincs, nem animálva); Nagy László és Weöres verse (védett) |
| 12. A Pál utcai fiúk (10) | 13 | a jellemzés mint szövegalkotás (feladat a 13-ban); az erkölcsi vita (tanórai) |
| 13. Választott meseregény (4) | – | **szándékosan kimarad:** a tanár választ, és a felsorolt művek többsége védett (Szabó Magda, Fekete István); Móra *Csilicsali Csalavári Csalavér*ja közkincs – a MagStory-sablonnal később olcsón elkészíthető |
| 14. Hősök az irodalomban (10) | 14 | **az időmértékes verselés** (daktilus, spondeus, hexameter, epigramma) – 1. tartalék; a mondák (Csörsz árka, Lehel kürtje, Szent László); a *Lúdas Matyi* (Fazekas, közkincs) és a mozgókép (védett film) |
| 15. Toldi (16) | 15 (+10) | a késleltetés és az elbeszélési idő mérése (a `MagStory.timing` csak egy lépésben); a testvérviszály és a bosszú erkölcsi kérdései (tanórai beszélgetés, a lecke csak felveti); az allegória |
| 16. Szeretet, hazaszeretet, szerelem (11) | 16 | **a szerelmi líra és a népdal** (Csokonai: *Tartózkodó kérelem*, Petőfi: *Reszket a bokor, mert…*, Radnóti: *Bájoló*, népdalok), az **alliteráció** – 2. tartalék; a *Honfidal*; a karácsonyi bibliai történetek |
| 17. Egri csillagok (12) | 17 | az ostrom hadi eseményei a regény szerint (szándékosan: a 16-eger történelemlecke már bemutatja a történeti oldalt); a regény elbeszélőjének hangja csak egy lépésben |
| 18. Világirodalmi ifjúsági regény (5) | – | **szándékosan kimarad:** a választható művek közül Defoe eredetije közkincs, de magyar fordításai nem bizonyítottan azok, Saint-Exupéry magyar fordítása (Rónay György, †1978) védett; egy *Robinson naptára* lecke csak saját összefoglalóval lehetséges (7. tartalék) |

Jól lefedett: a nyelvi rendszer (hang, fonéma, szóelem, hasonulás, szófaj), a verselés
alapjai, a cselekményszerkezet, a tér és az idő az epikában, a szóképek, a forrás és az
átírás. Gyengén lefedett: a szövegalkotás, a vita és a véleményalkotás (tanórai tevékenységek;
a 13, 14 és 17 nyitott kérdései alapot adnak hozzájuk), valamint a lírai témák (szeretet,
szerelem).

**A forrásszöveg kinyerési hibái** (a `kerettanterv/magyar-nyelv-es-irodalom/5-6.md`-ben,
javítás nélkül):

- a 15. (Toldi) témakör fogalmai között egy csonka elem áll: „verses epika, elbeszélő költemény;
  **s,** előhang, epizód…” – valószínűleg a forrás hibája, vagy egy rövidített fogalom (pl.
  „strófa”?) maradt csonkán. Az eredeti DOCX-ben ellenőrizni kell;
- az 5. és a 14. témakörben a „### Fejlesztési feladatok” előtt egy magányos „-” sor áll
  (konverziós maradvány);
- az irodalmi tananyagtáblában a „VI. Hősök az irodalomban” alatt „*V.1. Hagyomány és
  irodalom*” és „*V.2. Irodalom és mozgókép*” szerepel (a forrás számozási hibája);
- elírások a forrásban (nem javítjuk): „Kitüntetetett cél”, „Az írásbeli magnyilatkozások”,
  „A szókincsfejlesztése”, „A szófajok felismerése helyes leírása”;
- a nyelvtani tananyagtábla celláiban több üres felsorolásjel (`<ul><li></li></ul>`) áll –
  ez a DOCX üres cellája, tartalmat nem érint;
- az áttekintő táblázat 216 órát összegez, a szöveg 272-t; a különbség a két 28 órás szabad
  keret (a README eltérés-oszlopa is jelzi).

**Tartalék-jelöltek**, ha a pilot után folytatódik a sor (fontossági sorrendben):

1. `idomertek` – **„Tá-ti-ti” – hosszú és rövid szótag, a hexameter.** A szótaghosszúság szabálya
   algoritmus: a gép kiszámolja, a diák meghallgatja (hosszú = két ütés, rövid = egy) és
   kopogja. Szöveg: Kölcsey *Huszt*ja („Bús düledékeiden, Husztnak romvára, megállék; / Csend
   vala, felleg alól szállt fel az éjjeli hold.” – disztichon, közkincs, ellenőrizve), és
   Vörösmarty *Zalán futása* első sora („Régi dicsőségünk, hol késel az éji homályban?”). A
   kerettanterv szimónidészi epigrammájának magyar fordítását csak akkor idézzük, ha a
   fordítója bizonyítottan közkincs *(ellenőrizendő)*. Modul: MagVers (`feet`), MagHang
   (`click`). (14. témakör.)
2. `szerelmi-dal` – **Reszket a bokor – dal, népdal, alliteráció.** A párhuzam (bokor ↔ lélek)
   két rétegben; Radnóti *Bájoló*ja (†1944, közkincs) az alliteráció hangjaival; a népdal
   versszakszerkezete (*Tavaszi szél vizet áraszt*). Modul: MagVers, MagText. (16. témakör.)
3. `szamnev-gep` – **Kétezer-egy vagy kétezeregy?** A számnevek helyesírása algoritmusként:
   2000-ig egybeírjuk, fölötte hármas csoportonként kötőjellel tagoljuk; dátumok: *1-jén*,
   *15-én* (hasonulás!) *(ellenőrizendő: AkH. 12.)*. Modul: MagText, MagMorph. (8. témakör.)
4. `foldrajzi-nevek` – **Kötőjel vagy egybe? – földrajzi nevek a térképen.** Döntési fa a
   TortMap-en (*Gellért-hegy*, *Balaton-felvidék*, *Balatonfüred*, *Duna–Tisza köze*). (8.
   témakör.)
5. `nevmas-mutatok` – **Ki az az ő? – névmások a szövegben.** A névmás nyíllal mutat a
   szövegelőzményére egy *Pál utcai fiúk*-részletben; névmások nélkül a szöveg ismétlődik,
   csupa névmással kétértelművé válik. (8. témakör.)
6. `csaladi-kor` – **A vers mint film – Arany: Családi kör.** Versszakonként egy
   „kameraállás” (totál → közeli), a felező tizenkettes refrénnel. (9. témakör.)
7. `robinson-naptara` – **28 év egy szigeten.** Saját összefoglaló, a sziget térképe és a
   napló idővonala; idézet nélkül. (18. témakör.)
8. `ikarosz` – **Se túl magasan, se túl alacsonyan – mítosz és tanulság.** Repülőjáték (a nap
   olvasztja a viaszt, a tenger nedvesíti a tollat), saját összefoglalóval. (9. témakör.)

**Meglévő anyagok** (saját ismeret, nincs ellenőrizve): a Nemzeti Köznevelési Portál (NKP)
5–6. osztályos digitális magyar nyelvi és irodalomtankönyvei; a Petőfi Irodalmi Múzeum
digitális gyűjteményei; a MEK és a Digitális Irodalmi Akadémia szövegei; a HUN-REN Nyelvtudományi
Kutatóközpont helyesírási portálja és tanácsadója; a Jankovics-féle *János vitéz* (1973), a
Fábri-féle *Pál utcai fiúk* (1969) és a Várkonyi-féle *Egri csillagok* (1968) film. A filmek
védettek, ezért csak hivatkozhatók; az átfedést és a kiegészítést a tanári review döntse el.

---

## 7. Javasolt szerződés-kiegészítés (kész szöveg a `leckek/SZERZODES.md`-hez)

A következő fejezet változtatás nélkül beilleszthető a `SZERZODES.md` végére, a 17.
(Természettudomány-kiegészítés) után.

```markdown
## 18. Magyar nyelv és irodalom-kiegészítés (5–6. évfolyam)

Magyarleckénél a fenti szabályok ezekkel együtt érvényesek. **Kötelező olvasmány:**
`pilot/magyar-5-6/terv.md` – a saját briefed (3. fejezet), a modulok API-vázlata (4. fejezet)
és a build-jelölések (5. fejezet).

- **Mappa, fejléc:** `leckek/magyar-5-6/NN-slug.{html,md,content.js}`; metaadat-sor:
  `tantárgy: Magyar nyelv és irodalom · évfolyam: 5–6. · témakör: N. <a kerettanterv témakörének címe>`.
  Spec: `"maxWords": 45`. Rövid mondatok, tegező hang, új fogalom **félkövéren**, egy mondattal
  megmagyarázva.
- **Szerzői jog – kötelező (a repó nyilvános).**
  - Szó szerint csak **közkincs** szöveg idézhető: a szerző halálát követő év január 1-jétől
    számított 70 év letelt (Szjt. 31. §), vagyis 2026-ban a legkésőbb 1955-ben elhunyt
    szerzőké. Közkincs például Petőfi (†1849), Arany (†1882), Kölcsey (†1838), Vörösmarty
    (†1855), Csokonai (†1805), Fazekas (†1828), Jókai (†1904), Ady (†1919), Gárdonyi (†1922),
    Móra (†1934), Juhász Gyula és József Attila (†1937), Karinthy és Dsida (†1938), Reményik
    (†1941), Radnóti (†1944), Molnár Ferenc (†1952), Ilosvai, Tinódi, Szendrey Júlia.
  - **Védett**, tehát legfeljebb címmel, egy-két mondatos saját szavas tartalmi utalással
    jelenhet meg: Weöres Sándor, Kányádi Sándor, Nemes Nagy Ágnes, Nagy László, Ágh István,
    Szabó Magda, Fekete István, Lázár Ervin, Kittenberger Kálmán (†1958, 2029-től közkincs),
    Széchenyi Zsigmond, O. Nagy Gábor, Illyés Gyula (népmese-feldolgozásai is!), és **minden
    mai vagy 70 éven belül elhunyt fordító fordítása** (Ovidius, Saint-Exupéry, Defoe, a
    görög mítoszok, a Biblia modern fordításai). Bibliai szöveg csak Károli Gáspár 1590-es
    fordításából idézhető, egyébként saját összefoglaló kell, leíró keretben („a Biblia szerint”).
  - A **népköltészet** (mese, monda, népdal, ballada, szólás, közmondás) közkincs, de a
    szöveg csak közkincs **gyűjtésből vagy kiadásból** vehető át (pl. Arany László, Benedek
    Elek, Kriza János). A gyűjtő nevét és halálozási évét a forrásmegjegyzés tartalmazza.
  - Minden idézet a `### Idézet` blokkban áll, előtte a kötelező forrásmegjegyzés:
    `<!-- idézet: <szerző>: <mű> (<év>), <hely a műben> · szöveg: <kiadás/MEK-szám/URL> · szerző † <év> · közkincs -->`.
    A szöveget **két független kiadásból** vesd össze (pl. MEK + Wikisource), és az eltérést a
    megjegyzésben jelezd. Emlékezetből soha ne idézz.
  - Filmet, rajzfilmet, színházi előadást, illusztrációt (Jankovics, Fábri, Várkonyi stb.) csak
    címmel említs. Kép csak saját canvas-rajz lehet; közkincs festmény legfeljebb hivatkozásként
    szerepelhet. Térképhez a `shared/tort/` adatait használd; utcatérkép csak saját, „vázlatos”
    bélyegű rajz lehet (OpenStreetMap-adat nem, mert ODbL-licencű).
- **A szöveg hűsége.** Az idézett szöveg a forráskiadás írásmódjával marad (*Kukoricza*,
  *Taljánország*, *kislyány*); ne modernizáld és ne „javítsd”. Ahol a régi írásmód zavaró, a
  „régi írásmód” bélyeget tedd mellé (felirat-kulcs). A versszakot ne rövidítsd kipontozás
  nélkül; kihagyást „[…]” jelöljön. A szótagszám-eltérést (pl. egy 11 szótagos sor a felező
  tizenkettesben) ne simítsd el: mutasd meg, és mondd ki, hogy a költő nem gép.
- **Helyesírás:** *A magyar helyesírás szabályai* (AkH.), 12. kiadás (2015) – vagy az épp
  érvényes kiadás (gyártás előtt ellenőrizd); vitás esetben a HUN-REN NYTI helyesírási
  portálja. Szabályt csak a pontszámával együtt idézz a `.md` megjegyzésében
  (`<!-- AkH. 12. § … -->`). Kiejtést mindig szögletes zárójelben írj, a betűk szerint (ejtés:
  [kúdba]), IPA-jelek nélkül.
- **Nyelvtani rendszer.** A szófajok csoportosítása, a magánhangzók besorolása és a szóelemek
  elnevezése tankönyvenként eltér. A lecke a briefben megadott rendszert kövesse, a `.md` egy
  megjegyzésben rögzítse, melyik ez, és a panel egyszer mondja ki: „Más tankönyvben ezt másképp
  is csoportosíthatják.” A modul nem ragoz és nem elemez szabadon: minden alakot, szóelemzést
  és kivételt a `.md` ad meg (`morph`, `pron`), a kód csak mutat és ellenőriz.
- **Nyelvi sokszínűség.** A köznyelvi normát mutatjuk be, de a nyelvjárás, a természetes
  kiejtés ([kúdba]) és a beszélt nyelv nem „hiba”. „Helytelen” helyett „a köznyelvben / a
  helyesírásban így írjuk” forma kell. Nyelvjárást, beszédhibát, akcentust nem teszünk
  nevetségessé. Kitalált szavaknál (pl. `07`) egy második ember nézze át, hogy ne hasonlítson
  durva, csúfolódó vagy létező szóra.
- **Értelmezési sokszínűség.** Egy műnek nincs egyetlen „helyes” olvasata. Ami értelmezés (a
  rejtett üzenet, a szerkezeti besorolás, egy motívum jelentése, a „világfa”), az `> értelmezés:`
  dobozban vagy „egy lehetséges olvasat” felirattal jelenik meg; tényként csak a szövegből
  ellenőrizhető állítás szerepel. Ne írd, hogy „a költő ezt akarta mondani”. Értelmező
  feladatnál (szereposztás, tetőpont kijelölése, hézag kitöltése) a gép **nem pontoz** hibának
  egy eltérő, de védhető választ: összeveti a `.md` olvasatával, és kérdést tesz fel. Minden
  irodalomleckében van legalább egy nyitott kérdés („Te hogyan döntenél?”, „Megérte?”).
- **Irodalom és történelem.** Ha egy mű történeti eseményhez kapcsolódik (*Egri csillagok*,
  *Toldi*, *A walesi bárdok*, *Himnusz*), a lecke választja el a regényt/mondát a történeti
  ténytől (a 11. fejezet „forrás / rekonstrukció / monda” jelöléseivel), és ne ismételje meg a
  történelemleckét: hivatkozz rá (`leckek/tortenelem-5-6/16-eger`). A háború, a halál
  (Nemecsek, Iluska, a bárdok) és a kegyetlenség jelzésszerű: nincs vér, nincs égő alak; a
  veszteséget szöveg és csend mutatja. Nemzeti jelképet (Himnusz, Szózat) nem teszünk
  játékká, és nem torzítunk.
- **Hang.** Hang csak a `MagHang` modulon át szólhat: szintetizált dallam, magánhangzó, zörej
  vagy kopogás. Nincs felvett emberi hang, nincs gépi felolvasás (TTS), nincs zene más
  szerzőtől. A hang csak kattintásra indul (▶), mérsékelt hangerővel, és **a lecke hang
  nélkül is teljes**: a dallamvonal, a szótagpöttyök és a kopogássáv ugyanazt mutatja. A QA
  headless, tehát hang nélkül fut; ez nem hiba.
- **Színkódok** (minden leckében egységesek):
  | mit | szín |
  |---|---|
  | tő | tinta `#1c2440` keret, kártya-kitöltés |
  | képző | kékeszöld `#0a6f86` |
  | jel | okker `#8f5a0c` |
  | rag | cinóber `#c8401c` |
  | kötőhangzó | halvány tinta `#565d72`, kisebb betű |
  | rímpárok | a: cinóber · b: kékeszöld · c: okker · d: lila `#7b4fa0` |
  | magas / mély hangrend | kékeszöld / okker (vegyes: mindkettő csíkban) |
  | szófajok (a szó aláhúzása) | ige `#c8401c` · főnév `#0a6f86` · melléknév `#7b4fa0` · számnév `#8f5a0c` · határozószó `#2a4d9b` · névmás `#6b6a12` · igenév: az ige színe szaggatva · viszonyszó, mondatszó `#565d72` |
  A szóelemek kitöltött csempék, a szófajok aláhúzások, így egy leckében mindkettő
  használható. A rímszín a sorvég utolsó magánhangzójától a sor végéig tart.
- **Verssor a vásznon:** idézett sor legalább 26 px, a szótagpötty és az ütemjel felirata
  legalább 22 px. Hosszú sornál mindig adj `max`-ot; ha egy versszak nem fér ki, inkább lapozz
  (versszakonként), mint hogy kicsinyítsd. A sortördelés a verssor határát kövesse, sort ne
  törj két képernyősorra jelölés nélkül (ha kell: behúzott folytatás + „↩” jel).
- **Új közös modulok leckén belül:** a `MagText`, `MagMorph`, `MagVers`, `MagHang` és
  `MagStory` (terv.md 4. fejezet) először a referencialeckében készül, külön blokkban
  (`/* ── MODUL: Verstan (MagVers) · forrás: magyar-5-6/10-janos-vitez-vers, <dátum> ── */ … /* ── MODUL VÉGE ── */`),
  `Mag…` névtérrel és API-leírással, hogy változtatás nélkül átemelhető legyen a
  `shared/magyar/` alá. A történelemmodulokat (TortMap, TortGlobe, TortTimeline, TortSource,
  TortCards, TortScene) bájtra azonosan vedd át a legfrissebb leckéből.
- **Minden `.md`** végén `<!-- Vitatott / bizonytalan pontok: … -->` blokk a tanári
  review-hoz: a szövegforrás(ok) és az eltéréseik, a választott tankönyvi rendszer, az
  értelmezésként jelölt állítások, a kitalált szavak listája (ha van).
```
