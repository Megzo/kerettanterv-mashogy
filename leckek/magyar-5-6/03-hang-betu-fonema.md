# Kör, kőr, tőr – hang, betű, fonéma, ábécé
tantárgy: Magyar nyelv és irodalom · évfolyam: 5–6. · témakör: 4. A nyelvi szintek: a beszédhang, a fonéma, a szóelemek, a szavak, az összetett szavak

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/magyar-5-6/03-hang-betu-fonema.md

  A lecke NEM tud magától szavakat: minden szó, szópár és szólista ebből a fájlból jön.
  Amit a lecke maga számol (és piros sávval jelez, ha a fájl adata nem stimmel vele):
  – a betűk és a hangok száma (2. lépés; az ejtés: „taxi [takszi]”, szögletes zárójelben, IPA nélkül);
  – hogy a szócsillag (3. lépés) és a szólétra (4. lépés) minden szava pontosan EGY hangban tér el
    a szomszédjától (a betűk száma azonos, és egyetlen betű más);
  – a hosszú–rövid párokban (5. lépés) csak a hossz különbözik (ékezet vagy kettőzött betű);
  – az ábécé betűinek száma (6. lépés) a lecke 44 betűs ábécéjéből;
  – a betűrend (7. lépés) a helyesírási szabályzat szerint (AkH. 12. 14. pont), betűről betűre;
  – a szótagolás (8. lépés): a „szó = szó-tag” alak egyezik-e a lecke szótagolásával.
  A listákban a szavakat vessző választja el, a „… szabályok” listában pontosvessző.
  Feliratban a # jel helyére a lecke számot, betűt vagy szót ír.
-->

## Közös

### Feliratok
- adathiba felirat: Ellenőrizd a .md-t: #
- vázlat bélyeg: vázlat – nem mérés
- gépi hang bélyeg: gépi hang – egyszerűsített

## 1. Hallod vagy látod?
Amikor beszélünk, **hangokat** ejtünk ki: ezeket halljuk. Amikor írunk, **betűket** írunk le: ezeket látjuk. ==A betű a hang írott jele.== A *kör* szóban három hangot hallasz, és három betűt látsz.

> megjegyzés: Mondjátok ki lassan: k–ö–r. Számoljátok a hangokat az ujjatokon!

### Feliratok
- első szó: kör
- hallod felirat: Hallod: hangok
- látod felirat: Látod: betűk
- jele felirat: a betű a hang írott jele
- újra gomb: Mutasd újra!
<!-- AkH. 12. 3. pont: „A beszédhangok írott jeleit betűknek nevezzük.” -->

## 2. A betű nem mindig egy hang
Ugyanaz a betű és a hang? ==Nem mindig.== Az *sz* két jelből áll, mégis **egy betű**: **kétjegyű betű**, és egy hangot jelöl. Az *x* egy betű, de két hangot jelöl: [ksz]. Az *ly* és a *j* ugyanazt a hangot jelöli.

### Feliratok
- betű-hang szavak: szél, csacsi, taxi, folyó
- betűk sor: betűk
- hangok sor: hangok
- betűszám felirat: # betű
- hangszám felirat: # hang
- többjegyű jelvény: két jel, mégis egy betű: egy hang
- x jelvény: egy betű, két hang
- ly jelvény: az ly és a j ugyanaz a hang

### Adatok
- taxi: taxi [takszi]
<!-- AkH. 12. 228. pont: „az x pedig két hang (k + sz) jele, de egyetlen jegyű” -->
- folyó: folyó [fojó]
<!-- AkH. 12. 88. pont: „számos szóban hagyományosan ly a [j] hang jele” -->

## 3. Egy hang cseréje: új szó
Cseréld ki a *kör* egyik hangját! *Tör*, *kar*, *köd*: ==egyetlen hang, és más a szó jelentése.== Az ilyen, jelentést megkülönböztető hang a **fonéma**. Két szó, amely csak egy hangban tér el: **minimális pár** (*kör – tör*).

### Feliratok
- szócsillag közép: kör
- szócsillag szavak: tör, kar, kor, kér, kőr, köd, köt, köz
- első hang gomb: Az első hang
- második hang gomb: A második hang
- harmadik hang gomb: A harmadik hang
- mind gomb: Mind
- csere felirat: # → #
- fonéma felirat: más hang → más szó: ez a fonéma
- koppints felirat: Koppints a kör egyik betűjére!
- hossz megjegyzés: csak a hossz más – az is új szó!

## 4. A szólétra
Mássz fel a létrán! Minden fokon **egyetlen hang** cserélődik, és ==minden fokon új szó születik==. Tíz lépésben a *kör*-ből *kas* lesz. Figyeld meg: a *kör → kőr* lépésben csak a hang hossza változott.

> megjegyzés: Építsetek saját létrát, például a *bot* szóból!

### Feliratok
- létra szavak: kör, kőr, tőr, tör, tér, tél, tál, sál, sás, sas, kas
- létra jelentések: kerek forma, kártyaszín, vívófegyver, pálcát tör, városi tér, évszak, edény, nyakba való, vízparti növény, ragadozó madár, méhek otthona
- fel gomb: Egy fokkal feljebb
- le gomb: Egy fokkal lejjebb
- végig gomb: Az egész létra
- fok felirat: #. fok
- kezdet felirat: innen indulunk
<!-- A létra szavai köznyelvi szavak (Magyar értelmező kéziszótár szerinti alapszavak): kör, kőr (kártyaszín a francia
     kártyában), tőr (szúrófegyver, a vívásban is), tör, tér (főnév: városi tér), tél, tál, sál, sás (vízparti, fűféle
     növény), sas, kas (méhkas, kosár). A terv létrájában a sál → sas lépés KÉT hangot cserélt (á → a és l → s), ezért a
     lecke közé tette a „sás” szót: sál → sás (l → s), sás → sas (á → a). A lecke L.checks() próbája minden fokot ellenőriz. -->

## 5. A hossz is számít
A *kör* és a *kőr* csak a magánhangzó **hosszában** különbözik, mégis két szó. ==A magyarban a hang hossza is megkülönbözteti a jelentést.== A mássalhangzóé is: *kel – kell*, *hal – hall*. Írásban ékezet vagy kettőzött betű jelöli.

### Feliratok
- hossz párok: kör–kőr, kor–kór, öt–őt, kel–kell, hal–hall
- kör jelentés: kerek forma
- kőr jelentés: kártyaszín
- kor jelentés: életkor: hány éves?
- kór jelentés: betegség
- öt jelentés: a szám: 5
- őt jelentés: Őt keresem.
- kel jelentés: reggel felkel
- kell jelentés: szükséges
- hal jelentés: vízi állat
- hall jelentés: a fülével érzékel
- rövid gomb: Rövid
- hosszú gomb: Hosszú
- rövid hang gomb: ▶ rövid ö
- hosszú hang gomb: ▶ hosszú ő
- válassz felirat: Válassz egy párt!
- hossz felirat: a hangok hossza
- idő felirat: idő
- rövid felirat: rövid
- hosszú felirat: hosszú
<!-- A párok az AkH. 12. 6. pontjából (koros – kóros, öt – őt) és 9. pontjából (hal – hall), a terv briefjéből (kel – kell)
     valók; a kör – kőr a lecke címpárja. -->

### Adatok
<!-- A gépi hang a 02-beszedhang lecke formánsadatait használja: Gósy Mária: Fonetika, a beszéd tudománya
     (Osiris, 2004), 20. táblázat, tájékoztató adatok, felnőtt köznyelv. -->
- ö formánsai: 380; 1600; 2400 Hz
- ő formánsai: 400; 1550; 2500 Hz
- sávszélességek: 80; 90; 150 Hz
- gépi alaphang: 120 Hz
<!-- A hang hossza: a lecke a jól hallható különbség kedvéért lassított, kétszeres arányú hangot ad. Folyó beszédben
     mindkét magánhangzó jóval rövidebb, és az arány beszélőnként, helyzetenként változik (becslés: a hosszú kb.
     másfél–kétszer olyan hosszú; ellenőrizendő: Gósy 2004, a magánhangzók időtartamáról szóló fejezet).
     A 5. lépés hangsávjainak szélessége is ezt az arányt rajzolja („vázlat” bélyeg). -->
- rövid hang ideje: 0,2 s
- hosszú hang ideje: 0,4 s

## 6. 44 betű sorban
Az iskolai **ábécé** 44 betű. ==A többjegyű betű önálló betű, saját helye van:== a *cs* a *c* után, a *d* előtt jön.

> megjegyzés: A helyesírási szabályzat 40 magyar betűt sorol fel, plusz a *q, w, x, y*-t. Más tankönyvben ezt másképp is csoportosíthatják.

### Feliratok
- többjegyű gomb: Többjegyű betűk
- magánhangzó gomb: Magánhangzók
- idegen gomb: q, w, x, y
- egyjegyű felirat: # egyjegyű
- kétjegyű felirat: # kétjegyű
- háromjegyű felirat: # háromjegyű
- összesen felirat: = # betű
- c cs felirat: a cs önálló betű: a c után, a d előtt
- magánhangzó felirat: # magánhangzó
- idegen felirat: idegen szavakban, régi nevekben

### Adatok
<!-- AkH. 12. 10. pont: 40 magyar betű (a, á, b, c, cs, d, dz, dzs, e, é, f, g, gy, h, i, í, j, k, l, ly, m, n, ny, o, ó, ö,
     ő, p, r, s, sz, t, ty, u, ú, ü, ű, v, z, zs); 11. pont: a q, w, x, y helye: „… p, q, r … v, w, x, y, z, zs”.
     7. pont: 17 egyjegyű mássalhangzó-betű, 8 kétjegyű (cs, dz, gy, ly, ny, sz, ty, zs), 1 háromjegyű (dzs); 4. pont: 14
     magánhangzó. 14 + 17 + 4 (q, w, x, y) = 35 egyjegyű. A lecke a betűket a saját 44 betűs ábécéjéből számolja. -->
- betűk száma: 44
- egyjegyű betűk száma: 35
- kétjegyű betűk száma: 8
- háromjegyű betűk száma: 1
- magánhangzók száma: 14

## 7. A betűrend-gép
Melyik jön előbb: *cukor* vagy *csiga*? A gép betűről betűre halad: ==az első eltérő betű dönt.== A *cs* külön betű, ezért *cukor*, *csiga*. Az *a* és az *á* itt egyenértékű; csak ha minden más azonos, jön előbb a rövid: *kar*, *kár*, *karc*.

### Feliratok
- betűrend szavak: kassza, csiga, kár, cukor, karc, cica, kasza, kar
- húzd felirat: Húzd sorba a szavakat!
- pont felirat: # / # pár jó sorrendben
- kész felirat: Betűrendben!
- rendezd gomb: Rendezd a gép!
- keverd gomb: Keverd össze!
- betű ok: az ábécében # előbb van, mint #
- rövidebb ok: # véget ért: a rövidebb szó jön előbb
- hossz ok: csak a hossz más: a rövid jön előbb
- egyenlő felirat: = ugyanaz a betű
- egyenértékű felirat: # = #: itt egyenértékű
- kettőzött felirat: # = # + #
- előbb felirat: előbb
- aztán felirat: aztán
- engedd felirat: Engedd el ott, ahová illik!
- jel felirat: Koppints két szó közti jelre!
<!-- AkH. 12. 14. pont: a) az egyjegyű betű megelőzi a vele kezdődő többjegyűt (cudar, cukor, cuppant, csalit);
     b) az első nem azonos betű dönt; a kettőzött többjegyű betűt két betűre bontjuk (ccs = cs + cs, ggy = gy + gy;
     a pont példái: kasza, kaszinó, kassza, kaszt); c) a rövid és a hosszú magánhangzó egyenértékű, a rövid csak akkor
     kerül előbbre, ha a két szó betűsora csak a hosszúságban különbözik (kerek, kerék; koros, kóros);
     d) a szóközt, kötőjelet nem vesszük figyelembe. A kis- és nagybetűs alak közül a kisbetűs jön előbb (14. a).
     A helyes sorrend itt: cica, cukor, csiga, kar, kár, karc, kasza, kassza. -->

## 8. Szótag és elválasztás
**Ahány magánhangzó, annyi szótag.** Egy mássalhangzó a következő szótagba kerül: *ke-rék*. Ha több áll egymás mellett, csak az utolsó: *temp-lom*. ==A többjegyű betű nem válik szét== (*ma-dzag*), a kettőzött igen: *asz-szony*. A sor végén szótaghatáron választunk el.

### Feliratok
- szótag szavak: kerék = ke-rék, asztal = asz-tal, templom = temp-lom, madzag = ma-dzag, asszony = asz-szony
- szótag szabályok: egy mássalhangzó: átmegy a következő szótagba; két mássalhangzó: az első marad, a második átmegy; több mássalhangzó: csak az utolsó megy át; a dz egy betű: együtt marad; az ssz két sz: mindkét sorba jut egy
- szótag számláló: # magánhangzó → # szótag
- sor végén felirat: a sor végén:
- írva felirat: írva: #
<!-- AkH. 12. 224. pont: „Minden szó annyi szótagú, ahány magánhangzó van benne” (példa: asz-tal); 226. c) egy mássalhangzó
     a következő sorba (be-tű); d) két mássalhangzóból az első marad (am-per); g) kettőnél több mássalhangzóból csak az
     utolsó megy át (temp-lom, a pont saját példája); 227. pont: a dz többjegyű betű, nem válik szét (ma-dzag, a pont saját
     példája); 226. f) a kettőzött többjegyű betű elválasztáskor mindkét sorba teljesen kiírva kerül (a 7. b) pont példája:
     asz-szony). -->

## 9. Összefoglaló
A **hang** a beszédé, a **betű** az írásé, és nem mindig fedik egymást. ==Egy hang cseréje – vagy csak a hossza – új szót ad: ez a fonéma.== Az ábécé 44 betű, a többjegyű is önálló. A betűrendben az első eltérő betű dönt.

### Feliratok
- össz 1 cím: hang ≠ betű
- össz 1 példa: sz · x · ly
- össz 2 cím: fonéma
- össz 2 példa: kör → tör → tér
- össz 3 cím: a hossz is számít
- össz 3 példa: kor – kór · kel – kell
- össz 4 cím: betűrend
- össz 4 példa: cukor, csiga · kar, kár
- össz 5 cím: szótag
- össz 5 példa: asz-tal · temp-lom

<!-- Vitatott / bizonytalan pontok (tanári review):
  - Helyesírási forrás: A magyar helyesírás szabályai, 12. kiadás (2015), a HUN-REN NYTI helyesírási portálján
    (helyesiras.mta.hu, AkH12), letöltve: 2026-11-24. A pontszámok a sorok melletti megjegyzésekben.
  - Az ábécé betűinek száma: az AkH. 12. 10. pontja 40 magyar betűt sorol fel, a 11. pont a q, w, x, y helyét adja meg.
    Az iskolai „44 betűs ábécé” ezek összege; a lecke ezt követi, és a 6. lépés megjegyzése kimondja a különbséget.
  - A fonéma meghatározása egyszerűsített („jelentést megkülönböztető hang”). A szakirodalom a fonémát a nyelv
    hangrendszerének elvont egységének tekinti; a 10–12 éveseknek szóló tankönyvek a jelentésmegkülönböztető szerepet
    emelik ki. A „minimális pár” kifejezés nem szerepel a kerettanterv fogalmai között – a lecke egyszer, példával vezeti be.
  - A hosszúság: a lecke a magánhangzók hosszúságát (kör – kőr) és a mássalhangzókét (kel – kell) egyformán
    „hossznak” nevezi. Az a–á és az e–é pár hangszínben is különbözik (lásd 02-beszedhang); a lecke ezért a hossz
    bemutatásához az ö–ő párt szólaltatja meg, és a hangsávok rajza vázlat.
  - Az 5. lépés gépi hangja formánsszintézis (nem emberi hang, nem felolvasás), csak gombra szól; a „lassított” hossz
    (0,2 s és 0,4 s) szemléltetés.
  - A szólétra: a terv létráját (… sál → sas …) a lecke javította, mert az a lépés két hangot cserélt; a közbeiktatott
    „sás” (vízparti növény) talán nem minden diák számára ismert – a rajz és a felirat segít.
  - A 2. lépés ejtései (taxi [takszi], folyó [fojó]) a köznyelvi ejtést jelölik; a „szél” és a „csacsi” ejtése az
    írással azonos (a lecke ezeknél a betűket hangként is kiírja).
  - Elválasztás: a lecke a szótagolás szerinti elválasztás alapeseteit mutatja; az összetett szavak tagjai szerinti
    elválasztás (AkH. 12. 233–237.) és az egy magánhangzós szótag sorvégi szabálya (226. a) kimarad.
  - Saját példák, idézett szöveg nincs.
-->
