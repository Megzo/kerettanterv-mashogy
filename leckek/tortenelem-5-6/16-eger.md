# Hogyan tarthatott ki Eger? – a végvári harcok
tantárgy: Történelem · évfolyam: 5–6. · témakör: 8. Portrék és történetek Magyarország kora újkori történetéből

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/tortenelem-5-6/16-eger.md

  Kerettanterv (8. Portrék és történetek Magyarország kora újkori történetéből): Altéma: „A várháborúk
  hősei (pl. Dobó; Zrínyi, a szigetvári hős).” · „Buda visszavétele: a török kiűzése.” · Fogalmak:
  „szultán, janicsár, török hódoltság, …” · Személyek: „… Dobó István, …” · Kronológia: „1526 a mohácsi
  csata, 1541 Buda eleste, 1552 Eger védelme, 1686 Buda visszafoglalása, …” · Topográfia: „Mohács, Eger,
  …” · Fejlesztési feladat: „A török- és Habsburg-ellenes harcok hőseiről szóló történetek elbeszélése,
  irodalmi szövegek felidézése.”, „Annak a bemutatása, hogy milyen hatással volt a török uralom
  Magyarország fejlődésére.” · Javasolt tevékenység: „Képek, ábrázolások gyűjtése magyar végvárakról,
  kiállítás rendezése.”

  Formátum-megjegyzések:
  – Az 1. lépés térképe a Natural Earth közkincs adataiból készül („Made with Natural Earth”). A folyók
    a mai állapotot mutatják. Országhatárt a lecke nem rajzol; a „mai határok” réteg kikapcsolható
    tájékozódási segítség. A két sereg útvonala VÁZLAT (csak a fő irány), a nyilak haladása a várak
    elestének dátumaihoz igazodik, a köztes napok nem forrásból valók.
  – A 2. lépés metszete ILLUSZTRÁCIÓ: nem az egri vár hű képe, hanem egy végvár jellemző részei.
  – A 4–5. lépés alaprajza VÁZLAT: az egri vár körvonala, a belső és a külső vár, a patak, a város és a
    dombok helye erősen egyszerűsített. A geometria a kódban van, az Eger helye koordináta mozgatja.
    Az ágyúállások, a rohamok iránya és az egységek helye jelképes (rekonstrukció), nem pontos.
  – Az 5. lépés aknajátéka szemléltető modell: a rezgés a távolsággal gyengül (a sáv a legerősebb
    tálhoz mért arány). A kódban rögzített: 5 tál a fal mentén, az „Új akna” gomb sorrendje.
  – A 6. lépés a nappal hosszát csillagászati képlettel számolja Eger szélességére. 1552-ben még a
    Julián-naptár járt: a dátumokat a forrás szerint (régi naptár) írjuk, a számítás a naptár
    eltérésével (10 nap) a mai naptárra váltja át őket.
  – A 7. lépés kártyáinak helyes oszlopa a kódban van (Dobó, asszonyok, aknák → Tinódi éneke;
    bikavér, Jumurdzsák, festmény → később született).
  – A két sereg színe szándékosan semleges (indigó és szilva), nincs „jó” és „rossz” szín.
  – A felirat-sablonokban a # jel helyére a lecke számot ír (pl. „# évvel később” → „1 évvel később”).
-->

## Közös

### Feliratok
- forrás jel: forrás
- rekonstrukció jel: rekonstrukció
- monda jel: monda
- vázlatos: vázlatos
- becslés: becslés
- illusztráció: illusztráció
- mai határok: mai határok
- lépték: # km
- Kr. e.: Kr. e.
- Kr. u.: Kr. u.
- század: század
- év sablon: # év
- június: június
- július: július
- augusztus: augusztus
- szeptember: szeptember
- október: október
- jelmagyarázat: jelmagyarázat

### Adatok
- Eger helye: 47,904° É, 20,378° K
- hadjárat éve: 1552
- ostrom kezdete: 1552. szeptember 9.
- ostrom vége: 1552. október 18.

## 1. Sorra estek a várak
Buda {Buda eleste} óta oszmán kézen volt. {hadjárat éve} nyarán két oszmán sereg indult a **végvárak**, vagyis a határt védő várak ellen. Sorra elesett Drégely, Temesvár és Szolnok. ==Szeptemberben Eger következett.==

> megjegyzés: Húzd a Dátum csúszkát!

### Feliratok
- csúszka dátum: Dátum
- gomb mai határok: mai határok
- térkép cím: Sorra esnek el a várak
- Duna: Duna
- Tisza: Tisza
- Ahmed serege: Ahmed pasa serege
- Ali serege: Ali pasa serege
- út észak felé: Felső-Magyarország felé
- Buda: Buda
- Nándorfehérvár: Nándorfehérvár
- Nándorfehérvár ma: ma Belgrád
- Drégely: Drégely
- Temesvár: Temesvár
- Temesvár ma: ma Timișoara
- Szolnok: Szolnok
- Eger: Eger
- Kassa: Kassa
- Kassa ma: ma Košice
- óta oszmán: # óta oszmán
- elesett: elesett:
- ostrom: ostrom:
- jel oszmán vár: oszmán kézen
- jel magyar vár: magyar kézen
- jel oszmán út: oszmán sereg útja
- cél oszmán cím: Az oszmánok célja
- cél oszmán 1: az oszmán uralom bővítése
- cél oszmán 2: Eger után nyitva az út észak felé
- cél magyar cím: A magyarok célja
- cél magyar 1: a végvárak megtartása
- cél magyar 2: a hódítás megállítása

### Adatok
- Buda helye: 47,50° É, 19,04° K
- Nándorfehérvár helye: 44,823° É, 20,450° K
- Temesvár helye: 45,754° É, 21,226° K
- Szolnok helye: 47,172° É, 20,191° K
- Drégely helye: 48,060° É, 19,046° K
- Kassa helye: 48,72° É, 21,26° K
- Buda eleste: 1541. augusztus 29.
- Drégely eleste: 1552. július 9.
- Temesvár eleste: 1552. július 27.
- Szolnok eleste: 1552. szeptember 4.

## 2. Az egri vár
Eger vára domb tetején állt, a város fölött. Kőfalak és **bástyák** védték. A bástya a falból kiugró erős rész: innen oldalról is lőhettek a falhoz érő ellenségre.

A várban nem lovagok, hanem fizetett katonák, **zsoldosok** szolgáltak. ==Ember, élelem, víz és lőpor kellett a kitartáshoz.==

### Feliratok
- vár cím: Eger vára, #
- vár alcím: egy végvár részei – egyszerűsített metszet
- kattints: Kattints a pontokra!
- kell cím: Mi kellett a kitartáshoz?
- kell 1: elég katona
- kell 2: élelem és víz
- kell 3: lőpor
- kell 4: erős falak, bástyák
- pont bástya: bástya
- pont bástya szöveg: A falból kiugró, erős rész. Innen oldalról is lőhettek a falhoz érő ostromlókra.
- pont puskások: puskások
- pont puskások szöveg: Fizetett gyalogos katonák puskával. A végvárakban zsoldosok szolgáltak, nem lovagok.
- pont rés: betömött rés
- pont rés szöveg: Ahol az ágyú rést ütött a falon, a védők éjjel kővel, földdel, gerendával betömték.
- pont asszonyok: asszonyok
- pont asszonyok szöveg: Asszonyok is voltak a várban: követ, vizet, élelmet hordtak, és a falakon is harcoltak.
- pont huszár: huszár
- pont huszár szöveg: Könnyű lovas katona. A végvárakból portyázni jártak, ostromkor gyalog is harcoltak.
- pont raktár: raktár
- pont raktár szöveg: Gabona, liszt, bor: ebből kellett hetekig megélni, mert az ostrom alatt nem jött utánpótlás.
- pont kút: víz
- pont kút szöveg: Víz nélkül nincs kitartás: a várnak saját vízre volt szüksége, például kútra vagy ciszternára.
- pont lőpor: lőporraktár
- pont lőpor szöveg: Lőpor nélkül hallgatnak az ágyúk és a puskák. Biztos helyen kellett őrizni, a tűztől távol.

## 3. A két sereg
A várat {védők száma} védte: katonák, de polgárok, parasztok és asszonyok is. Vezetőik: **Dobó István** és **Mekcsey István** várkapitány.

Az oszmán sereget **Ahmed pasa** és **Ali pasa** vezette. Létszámát csak becsülni tudjuk. ==Sokszoros túlerő állt a vár előtt.==

> megjegyzés: Nézd meg a régebbi becslést!

### Feliratok
- gomb régi becslés: régebbi becslés
- két sereg cím: Hányan voltak?
- pötty jel: 1 pötty = # fő
- védők cím: A vár védői
- védők kik: katonák, nemesek, polgárok,
- védők kik 2: parasztok és asszonyok
- védők forrás: Tinódi adatai alapján
- ostromlók cím: Az oszmán sereg
- régi becslés jel: régebbi becslés:
- arány: 1 védőre kb. # ostromló
- vezetők magyar: Dobó István, Mekcsey István
- vezetők magyar 2: a két várkapitány
- cél védők: Céljuk: kitartani, amíg az ostromlók elvonulnak
- vezetők oszmán: Ahmed pasa, Ali pasa
- vezetők oszmán 2: a sereg fővezére és Buda kormányzója
- cél ostromlók: Céljuk: Eger elfoglalása, út észak felé
- pasa: pasa: magas rangú oszmán vezető, hadvezér

### Adatok
- pötty értéke: 100 fő
- védők száma: 2000–2100 fő (becslés)
- oszmán sereg létszáma: 35–40 ezer fő (becslés)
- régi becslés: 70–80 ezer fő (becslés)

## 4. Az ostrom napjai
Az ostromlók hetekig ágyúzták a falakat. A védők éjjel kővel, földdel, gerendával betömték a réseket.

**Roham** idején, amikor sok katona egyszerre támadt a falra, mindenki harcolt. ==Minden rohamot visszavertek.==

> megjegyzés: Húzd a csúszkát napról napra!

### Feliratok
- csúszka nap: Az ostrom napjai
- húzd: húzd a csúszkát!
- belső vár: belső vár
- külső vár: külső vár
- város: a város
- Eger-patak: Eger-patak
- dombok: dombok
- ágyúk: ágyúk
- oszmán tábor: oszmán tábor
- védők: védők
- betömött rés: betömött rés
- e érkezés: Megérkezik az oszmán sereg
- e érkezés 2: tábort vernek a vár körül
- e körülzárás: Körbezárják a várat
- e körülzárás 2: megszólalnak az ágyúk
- e ágyúzás: Napról napra ágyúzás
- e ágyúzás 2: éjjel a védők betömik a réseket
- e nagy roham: Nagy roham
- e nagy roham 2: a védők visszaverik
- e aknák: Ágyúzás és aknák
- e aknák 2: a védők ellenaknát ásnak
- e utolsó roham: Az utolsó nagy roham
- e utolsó roham 2: ezt is visszaverik
- e ősz: Hidegebb lesz, fogy az élelem
- e ősz 2: az ostromló sereg ereje fogy
- e elvonulás: Az oszmán sereg elvonul
- e elvonulás 2: Eger kitartott!
- eltelt napok: eltelt napok
- jel védők: védők
- jel ostromlók: ostromlók
- s érkezés: érkezés
- s roham: roham
- s roham 2: roham
- s elvonulás: elvonulás

### Adatok
- körülzárás: 1552. szeptember 11.
- nagy roham: 1552. október 4.
- utolsó roham: 1552. október 12.

## 5. Aknák a föld alatt
Az ostromlók **aknákat** is ástak: föld alatti folyosót a fal alá, hogy puskaporral felrobbantsák. A védők **ellenaknát** ástak elébe. De hol?

Egy régi módszer: ==ahol alatta ásnak, ott rezeg a tál vize.==

> megjegyzés: Kattints a tálra, ahol ásnál!

### Feliratok
- gomb mutasd: Mutasd az aknát
- gomb új akna: Új akna
- akna cím: Aknaharc a fal alatt
- akna alcím: felülnézet: a fal egy szakasza
- rezgés: rezgés
- fal: fal
- bent: a vár belseje
- kint: kint: az ostromlók
- futóárok: futóárok
- vizes tál: vizes tál
- oszmán akna: az ostromlók aknája
- oldalnézet: Oldalnézetben
- o fal: fal
- o tál: tál
- o akna: akna
- o lőpor: lőpor
- o ellenakna: ellenakna
- akna talált: Megtaláltátok az aknát!
- akna talált 2: A védők tönkretették, mielőtt a falhoz ért.
- akna nincs: Itt nincs akna – próbálj másik tálat!
- kattints tál: Kattints egy tálra!

## 6. Miért vonultak el?
Az ostrom alatt beköszöntött az ősz: rövidültek a nappalok, hidegebb lett. Fogyott az élelem és a lovak takarmánya. Sok katona megsebesült vagy megbetegedett.

A sereg nagy részének télre haza kellett érnie. ==Az ostromlók ideje véges volt.==

> megjegyzés: Húzd a csúszkát: hány óra a nappal?

### Feliratok
- csúszka nap 6: Melyik nap?
- nap cím: Milyen hosszú volt a nappal Egerben?
- óra: óra
- nappal sablon: # óra # perc nappal
- rövidebb sablon: # óra # perccel rövidebb, mint az első napon
- naptár megjegyzés: Akkor még a régi naptár járt: ez a mai naptárban # nappal későbbi nap. A görbe így számol.
- ok 1: Ősz: rövid nappalok, hideg éjszakák
- ok 2: Kevés élelem és takarmány a környéken
- ok 3: Sok sebesült és beteg katona
- ok 4: Télen nem lehet szabad ég alatt táborozni
- ok vég: Elvonulás

### Adatok
- naptár eltérése: 10 nap

## 7. Forrás vagy regény?
Sokan az *Egri csillagok* című **regényből** ismerik az ostromot. A regény kitalált történet, igaz eseményekre építve.

Mi szerepel a korabeli forrásban, és mi született később? ==A regény nem forrás.==

> megjegyzés: Húzd a kártyákat a helyükre!

### Feliratok
- gomb megoldás: Megoldás
- gomb újra: Újra
- kérdés: Mit írt le a forrás, és mi született később?
- jó helyen: # / # jó helyen
- eredmény: A regény, a monda és a festmény jóval később született!
- zóna forrás: Tinódi éneke
- zóna forrás 2: korabeli forrás, #
- zóna később: Később született
- zóna később 2: regény, monda, festmény
- kártya Dobó: Dobó István vezette a védelmet
- kártya asszonyok: Asszonyok is harcoltak a falakon
- kártya aknák: Az ostromlók aknákat ástak
- kártya bikavér: A törökök bikavérnek hitték a vörösbort
- kártya Jumurdzsák: Jumurdzsák gyűrűje
- kártya festmény: Festmény a szurkot öntő nőkről (#)
- mikor cím: Mikor keletkezett?
- r ostrom: ostrom
- r tinódi: Tinódi
- r festmény: festmény
- r regény: regény

### Adatok
- festmény éve: 1867

## 8. Honnan tudjuk? Tinódi éneke
**Tinódi Lantos Sebestyén** énekmondó volt: lantkísérettel énekelte el a híreket. Nem harcolt Egerben, de kikérdezte a védőket, és már {Tinódi éneke}‑ban megírta az ostromot.

==Ő a legfontosabb forrásunk.== Gárdonyi Géza {Egri csillagok}-ben regényt írt belőle.

### Feliratok
- gomb forrás: forrás
- gomb rekonstrukció: rekonstrukció
- gomb monda: monda
- gomb mind: mind
- esemény 1552: az ostrom
- tinódi típus: forrás · históriás ének
- tinódi cím: Eger vár viadaljáról való ének
- ki írta: Ki írta?
- tinódi ki: Tinódi Lantos Sebestyén, énekmondó
- mikor: Mikor?
- nyomtatva: nyomtatva: #
- ott volt: Ott volt?
- tinódi ott: nem, de a védőket kérdezte ki
- tinódi lejegyzés: megírja
- később év: # évvel később
- gárdonyi típus: regény · kitalált történet, igaz alapon
- gárdonyi cím: Egri csillagok
- gárdonyi ki: Gárdonyi Géza, író
- könyvként: könyvként: #
- gárdonyi ott: nem: forrásokat olvasott, és sokat kitalált
- gárdonyi lejegyzés: a regény
- regény jel: regény
- réteg cím: Mi honnan való ebben a leckében?
- forrás 1: Tinódi éneke az ostromról
- forrás 2: a védők száma Tinódi szerint
- rekonstrukció 1: az oszmán sereg létszáma (becslés)
- rekonstrukció 2: a vár alaprajza, az ostrom vázlata
- rekonstrukció 3: az aknák figyelése vizes tállal
- monda 1: a bikavér története

### Adatok
- Tinódi éneke: 1553
- Cronica nyomtatása: 1554
- Egri csillagok: 1899
- Egri csillagok könyvként: 1901

## 9. Összefoglalás
- {hadjárat éve} őszén Eger sokszoros túlerővel szemben kitartott.
- A védők betömték a réseket, ellenaknát ástak, visszaverték a rohamokat.
- ==Az ostromlók ideje véges volt: ősszel elvonultak.==
- A fő forrás Tinódi éneke; az *Egri csillagok* regény.
- Eger {Eger eleste}-ban elesett. Buda visszafoglalása: {Buda visszafoglalása}

### Feliratok
- ö cím: Eger előtt és után
- ö 1526: mohácsi csata
- ö 1541: Buda eleste
- ö 1552: Eger kitart
- ö 1552 2: Dobó István
- ö 1566: Szigetvár ostroma
- ö 1566 2: Zrínyi Miklós hősi védelme
- ö 1596: Eger eleste
- ö 1686: Buda visszafoglalása
- ö hódoltság: # évig volt Buda oszmán kézen
- ö kitartott: Eger # napig kitartott

### Adatok
- mohácsi csata: 1526. augusztus 29.
- Szigetvár ostroma: 1566
- Eger eleste: 1596
- Buda visszafoglalása: 1686. szeptember 2.

<!--
  Vitatott / bizonytalan pontok (tanári és szakmai review-hoz):
  – Az ostrom kezdete: a szakirodalom szeptember 9-ét (az első oszmán csapatok megérkezése) vagy
    szeptember 11-ét (a vár teljes körülzárása) adja; a lecke szeptember 9-től számol, és a 11-ét
    „körülzárás”-ként mutatja. Az elvonulás október 17–18-a (éjjel indultak, 18-án ment el az utolsó
    csapat); a lecke október 18-at használ. Így „kb. 39 nap”. A dátumok a régi (Julián-) naptár szerint.
  – A nagy rohamok napjai (október 4. és október 12.) a magyar összefoglalókból valók, Tinódi alapján –
    ellenőrizendő (egyes összefoglalók szeptember végén is említenek általános rohamot). A lecke csak
    a két legismertebbet mutatja, az ágyúzás és a kisebb harcok folyamatosak voltak.
  – A védők száma: Tinódi felsorolása alapján kb. 2000–2100 fő (egyes összefoglalók 2100–2300-at
    írnak, a katonák mellett nemesekkel, polgárokkal, parasztokkal). Forrásérték, de nem pontos szám.
  – Az oszmán sereg létszáma BECSLÉS: a mai magyar szakirodalom kb. 35–40 ezret ír (a hadsereg
    harcoló része, a kiszolgálók nélkül – a tartomány ellenőrizendő); a régebbi irodalom 70–80 ezret,
    Gárdonyi regénye még többet. A „becslés” bélyeg és az üres pöttyök ezt jelzik.
  – A hadvezérek: Kara Ahmed pasa (másodvezír, a hadjárat fővezére) és Hadim Ali pasa (Buda
    beglerbégje, azaz kormányzója). A lecke a rövid nevüket használja.
  – 1552 nyarának várai: Drégely 1552. július 9-én esett el (Szondi György hősi halála). FIGYELEM: a
    terv.md briefje „augusztus 9.”-et írt – szerintünk ez elírás, a szakirodalomban július 9. szerepel;
    ellenőrizendő. Temesvár július 26–27-én esett el (Losonczy István); a lecke július 27-et mutat.
    Szolnok szeptember 4-én esett el (a védők elhagyták). Ugyanebben a hadjáratban elesett Veszprém,
    Lippa és több nógrádi vár is (Szécsény, Hollókő, Buják, Ság) – a lecke ezeket nem mutatja.
  – Az útvonalak vázlatosak: Ahmed pasa Temesvár után a Tisza mentén ment Szolnokig, Ali pasa a
    nógrádi várak után csatlakozott hozzá; Szolnoktól együtt vonultak Eger alá.
  – Az oszmán cél („Eger után nyitva az út észak felé”) egyszerűsítés: Eger a Felső-Magyarország
    (Kassa, a bányavárosok) felé vezető utat védte. A hódítás indítékai (uralkodói, katonai, vallási
    – gázi-hagyomány) a lecke szintjén „az oszmán uralom bővítése”.
  – Miért vonultak el? A szakirodalom több okot említ: a közelgő tél és a hadjárati idény vége (az
    oszmán lovasság nagy része, a szpáhik, ősszel hazatérhetett; a hagyományos határnap a Kászim-nap,
    október 26. – ellenőrizendő), az ellátási nehézségek, a súlyos veszteségek és a járványok. A lecke
    ezeket egyszerűsítve, „rekonstrukció” jelöléssel mutatja; egyetlen okot nem emel ki.
  – A nappal hossza: csillagászati közelítő képlet (Nap deklinációja, −0,833° légköri fénytörés),
    Eger szélességére; percre pontos lehet ±2–3 perc. Az időjárásról (eső, hőmérséklet) 1552-ből
    nincs adatunk, ezért a lecke számot nem ír, csak „hidegebb lett”.
  – Az aknák: Tinódi és a későbbi összefoglalók szerint az ostromlók aknákat ástak, a védők
    ellenaknákkal feleltek. Az aknafigyelés vizes tállal (vagy borsóval teli dobbal – ezt Gárdonyi
    írja le a regényben) régi, más ostromokból is ismert módszer; hogy Egerben pontosan hogyan
    figyeltek, ELLENŐRIZENDŐ. Ezért „rekonstrukció” és „illusztráció” jelölés.
  – Az asszonyok: Tinódi több helyen említi az egri asszonyok harcát (pl. aki elesett férje helyén
    harcolt tovább). A híres jelenet – asszonyok forró szurkot öntenek az ostromlókra – Székely
    Bertalan „Egri nők” című festményéről (1867) és a regényből lett közismert; hogy így történt-e, a
    forrás nem bizonyítja. A festmény évszáma ellenőrizendő.
  – A bikavér: monda. A történet (a védők vörösbort ittak, az ostromlók bikavérnek hitték) és az „egri
    bikavér” bornév a 19. században terjedt el; korabeli forrás nem említi.
  – Tinódi: az „Eger vár viadaljáról való ének” 1553-ban készült, nyomtatásban a Cronica-ban jelent meg
    (Kolozsvár, 1554). Tinódi nem volt jelen az ostromnál; a résztvevők elbeszélése alapján írt.
  – Gárdonyi Géza: Egri csillagok – folytatásokban 1899-ben (Pesti Hírlap), könyvként 1901-ben.
    Jumurdzsák és a gyűrű története kitalált; Bornemissza Gergely valós személy, de a regénybeli
    élettörténete nagyrészt kitalált.
  – A 2. lépés metszete nem az egri vár 1552-es képe (a mai kazamaták és bástyák nagy része az ostrom
    után épült); a végvár jellemző részeit mutatja.
  – Szigetvár: 1566-ban I. Szulejmán serege ostromolta; Zrínyi Miklós a vár elestekor (szeptember 7.)
    kitörésben halt meg. Eger 1596-ban esett el (III. Mehmed hadjárata), és 1687-ben került vissza.
    Buda visszafoglalása 1686. szeptember 2. A „145 év” ebből számolt (1541–1686).
-->
