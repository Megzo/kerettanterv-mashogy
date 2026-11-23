# Milyen az atom belülről? – atommag, elektronhéjak, periódusos rendszer
tantárgy: Kémia · évfolyam: 7–8. · témakör: 3. Atomok, molekulák és ionok

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Feliratban a # jel helyére a lecke számot ír (pl. „#. héj” → „2. héj”).
  Újragenerálás: python3 tools/build_lesson.py leckek/kemia-7-8/05-atom-hejak.md
  Az elemtáblázat (vegyjel, magyar név, rendszám, csoport, periódus, atomtömeg) közös adat a
  lecke kódjában (KEM_ELEMEK) – a review módban „kódban rögzített”.
-->

## Közös

### Feliratok
- szemléltetés: szemléltetés – a méretek nem arányosak
- héj: #. héj
- periódus: #. periódus
- csoport: #. csoport
- héjak száma: # héj
- külső elektron: # külső elektron
- főcsoport 1: I.A
- főcsoport 2: II.A
- főcsoport 13: III.A
- főcsoport 14: IV.A
- főcsoport 15: V.A
- főcsoport 16: VI.A
- főcsoport 17: VII.A
- főcsoport 18: VIII.A

### Adatok
- 1. héj férőhelye: 2
- 2. héj férőhelye: 8
- 3. héj férőhelye: 8
<!-- A 3. héjon valójában legfeljebb 18 elektron lehet; a 20-as rendszámig (K, Ca) azonban már 8 után
     a 4. héj kezd telni – a 7–8. évfolyamos (Bohr-féle) modell ezt a 2, 8, 8, 2 szabályt tanítja. -->

## 1. Milyen kicsi az atom?
Egy sószem éle kb. {sókristály éle}. Nagyítsunk bele! Ezerszeres, milliószoros nagyításban is simának tűnik… aztán ==szabályos rendben sorakozó részecskék== jelennek meg.

A sóban ezek **ionok**: elektromos töltésű atomok (később tanuljuk). Két szomszéd távolsága csak {részecsketávolság a sóban}.

> megjegyzés: Húzd a csúszkát! Hányszoros nagyítás kell, hogy egy részecske ököl méretű legyen?

### Feliratok
- zoom cím: Milyen kicsi az atom?
- egy sószem: egy sószem
- kép szélessége: a kép szélessége:
- hajszál: hajszál
- baktérium: baktérium
- vírus: vírus
- atom: atom
- nagyítás csúszka: Nagyítás
- részecskeszám: egy sószem élén ≈ # részecske sorakozik
- még sima: még mindig sima felület…

### Adatok
- sókristály éle: 1 mm
- részecsketávolság a sóban: 0,282 nm
- nátriumion sugara: 0,102 nm
- kloridion sugara: 0,181 nm
- nátriumion jele: Na^+
- kloridion jele: Cl^-
- hajszál vastagsága: 70 µm
- baktérium hossza: 2 µm
- vírus átmérője: 100 nm
- atom átmérője: 0,1–0,5 nm
<!-- NaCl-rács: rácsállandó 0,564 nm, a szomszédos Na⁺ és Cl⁻ középpontja 0,282 nm-re van (CRC Handbook).
     Ionsugarak (Shannon, 6-os koordináció): Na⁺ 102 pm, Cl⁻ 181 pm – összegük ≈ a szomszédtávolság,
     ezért a rajzon a gömbök érintik egymást. 1 mm / 0,282 nm ≈ 3,5 millió részecske egy él mentén.
     Hajszál: 17–180 µm, átlag kb. 70 µm; baktérium (E. coli) kb. 2 µm hosszú; influenzavírus 80–120 nm.
     Atomátmérő: a definíciótól függően kb. 0,1–0,5 nm (a legnagyobb atomoké kb. 0,5 nm fölött is lehet). -->

## 2. Mag és burok: szinte üres
Az atom közepén az **atommag** van, körülötte az **elektronburok**.

Ha a hidrogénatom magja akkora lenne, mint egy mákszem, maga az atom egy fél focipályányi gömb lenne – és ==szinte teljesen üres==.

A tömeg mégis a magban van. Egy proton annyi, mint kb. {proton és elektron tömegaránya} elektron együtt.

### Feliratok
- mákszem cím: Ha az atommag egy mákszem lenne…
- focipálya: focipálya (105 m × 68 m)
- mákszem: mákszem = atommag
- az atom: …az atom ≈ # m átmérőjű lenne
- tömeg cím: Hol van a tömeg?
- egy proton: 1 proton
- elektronok tömege: # elektron
- tömeg a magban: a magban: több mint 99,9 %
- tömeg a magban 2: a burokban: kevesebb, mint 0,1 %

### Adatok
- hidrogénatom átmérője: 0,106 nm
- proton átmérője: 1,7 fm
- mákszem mérete: 1 mm
- focipálya hossza: 105 m
- focipálya szélessége: 68 m
- proton és elektron tömegaránya: 1836
<!-- Hidrogénatom: a Bohr-sugár kétszerese, 2 × 0,0529 nm. Proton: töltéssugár 0,84 fm → átmérő ≈ 1,7 fm
     (1 fm = egy femtométer = a nanométer milliomod része). Arány: 0,106 nm / 1,7 fm ≈ 62 000 → 1 mm-es
     mag mellett ≈ 62 m-es atom (a vásznon tízesre kerekítve: 60 m). Az arány a sugár definíciójától
     függ; a szénatomnál kb. 30 000–60 000. Tömegarány: mp/me = 1836,15 (CODATA). A hidrogénatom
     tömegének 99,95 %-a a mag; nehezebb atomoknál még több. Focipálya: FIFA-ajánlás 105 m × 68 m. -->

## 3. Proton, neutron, elektron – a rendszám
A magban **protonok** (+) és **neutronok**, a burokban **elektronok** (−): ezek az elemi részecskék.

==A protonok száma, a rendszám dönti el, melyik elem.==

Adj hozzá egy neutront! Mi változik? És ha egy protont?

### Feliratok
- protonok: protonok (+)
- neutronok: neutronok
- elektronok: elektronok (−)
- rendszám = protonszám: rendszám = a protonok száma
- semleges atom: semleges atom
- ion: ion (töltése van)
- új elem: Új elem!
- ugyanaz az elem: Ugyanaz az elem!
- ion lett: Ion lett belőle!
- újra semleges: Újra semleges atom!
- nem stabil: ilyen atommag nem stabil
- proton plusz: + proton
- proton mínusz: − proton
- neutron plusz: + neutron
- neutron mínusz: − neutron
- elektron plusz: + elektron
- elektron mínusz: − elektron

### Adatok
- kezdő protonszám: 3
- kezdő neutronszám: 4
- kezdő elektronszám: 3
<!-- Kezdőállapot: lítium-7 (3 p, 4 n, 3 e). A „nem stabil” jelzés a Z ≤ 20 elemek stabil izotópjainak
     listájából jön (kódban: KEM_ELEMEK[].stab, pl. Cl: 18 és 20 neutron). A kalcium-48-at (28 n)
     stabilnak vesszük: felezési ideje kb. 6·10¹⁹ év. Az izotóp fogalma nem 7–8. évfolyamos anyag,
     ezért a panel nem nevezi meg. -->

## 4. Héjak: 2, 8, 8
Az elektronok **héjakon** helyezkednek el. Az első héjon legfeljebb ==2==, a másodikon ==8== elektron fér el; a harmadikon (a 20-as rendszámig) 8. A nátrium tehát: 2, 8, 1.

A legkülső héj elektronjai a **külső elektronok**.

> megjegyzés: A körpálya csak modell: az elektron nem keringő bolygó. Nyomd meg a felhő gombot!

### Feliratok
- héjmodell: héjmodell (Bohr) – szemléltetés
- felhőkép: elektronfelhő – valósághűbb kép
- legfeljebb: legfeljebb #
- 20-as rendszámig: (a 20-as rendszámig)
- rendszám csúszka: Rendszám
- felhő gomb: Héjak ↔ elektronfelhő
<!-- A felhőkép is szemléltetés (a héjak sűrűsödési helyei elmosva); pontosabb kép a középiskolai
     anyag (atompályák). -->

## 5. Sor = héjak, oszlop = külső elektronok
Ez nem önkényes táblázat! A **sor** (periódus) száma megmutatja, ==hány héja== van az atomnak.

A főcsoportokban a római szám (I.A–VIII.A) azt, ==hány külső elektronja== van.

> megjegyzés: Kattints egy cellára! A 4. sor közepén a héjszerkezet bonyolultabb.

### Feliratok
- kattints: kattints egy elemre!
- elem csúszka: Rendszám
- hélium kivétel: a hélium kivétel: 2 külső elektron
- bonyolultabb: itt a héjszerkezet bonyolultabb –
- bonyolultabb 2: ez középiskolai anyag
<!-- Csoportszámozás: fent az IUPAC szerinti 1–18, alatta a hazai iskolai főcsoportjel (I.A–VIII.A).
     Ha csak az egyiket akarod, a másik feliratait töröld ki (üresen hagyni nem lehet – szólj a
     fejlesztőnek). -->

## 6. Elemcsaládok
Egy oszlopban ugyanannyi a külső elektron, ezért ezek az elemek ==hasonlóan viselkednek==: **elemcsaládot** alkotnak.

Az alkálifémek nagyon hevesen reagálnak, a nemesgázok szinte semmivel.

> megjegyzés: Válassz családot! A hidrogén az 1. oszlopban áll, mégsem alkálifém.

### Feliratok
- alkálifémek: alkálifémek
- alkáliföldfémek: alkáliföldfémek
- földfémek: földfémek
- halogének: halogének
- nemesgázok: nemesgázok
- alkálifémek 1: 1 külső elektron · puha, könnyű fémek
- alkálifémek 2: levegőn gyorsan átalakulnak
- alkáliföldfémek 1: 2 külső elektron · könnyű fémek
- alkáliföldfémek 2: vegyületeik: mészkő, gipsz, a csont
- földfémek 1: 3 külső elektron · fémek
- földfémek 2: a bór nem tartozik ide (nemfém)
- halogének 1: 7 külső elektron · nemfémek
- halogének 2: a nevük jelentése: „sóképző”
- nemesgázok 1: telített külső héj (8, a héliumnál 2)
- nemesgázok 2: szinte semmivel nem reagálnak
- konyhasó szóegyenlet: nátrium + klór → nátrium-klorid (só)
- magnézium szóegyenlet: magnézium + oxigén → magnézium-oxid
- nemesgáz példa: neon a reklámcsőben, argon az izzóban
- alumínium példa: alumínium: fólia, üdítősdoboz, repülő
- hidrogén nem alkálifém: H: az 1. oszlopban, de nem alkálifém

### Adatok
- konyhasó egyenlete: 2 Na + Cl2 -> 2 NaCl
- magnézium égésének egyenlete: 2 Mg + O2 -> 2 MgO
<!-- A halogén szó görög eredetű: hals = só, gennao = létrehoz. Az alkálifémeket (Na, K) petróleum vagy
     paraffinolaj alatt tárolják, mert a levegő oxigénjével és nedvességével gyorsan reagálnak.
     A vízzel való heves reakciót (nátrium vízben) szándékosan nem mutatjuk (biztonsági elv).
     Alkáliföldfém-vegyületek: mészkő CaCO₃, gipsz CaSO₄ · 2 H₂O, a csont ásványi része kalcium-foszfát
     (hidroxiapatit). A földfémek (III.A) közé a hazai tankönyvek a bórt nem sorolják. -->

## 7. Lángfestés és tűzijáték
Lángba tartott fémvegyület: ==a láng jellegzetes színű lesz==.

A hő a külső elektront magasabb energiájú állapotba emeli (a rajzon: kijjebb). Visszaeséskor fényt bocsát ki, mindig ugyanolyan színűt – ez a tűzijáték titka is.

> megjegyzés: Tanári bemutató! A báriumsók mérgezőek.

### Feliratok
- lángfestés: Lángfestés
- tanári bemutató: tanári bemutató
- ne próbáld ki: NE PRÓBÁLD KI otthon
- minta: fémsó a drót végén
- tűzijáték: tűzijáték
- felemeli: a hő felemeli
- visszaesik: visszaesik → fény
- látható fény: a látható fény színei
- belső héjak: belső héjak
- lítium: lítium
- nátrium: nátrium
- kálium: kálium
- kalcium: kalcium
- stroncium: stroncium
- bárium: bárium
- réz: réz
- lítium lángszíne: kárminvörös
- nátrium lángszíne: sárga
- kálium lángszíne: fakóibolya
- kalcium lángszíne: téglavörös
- stroncium lángszíne: bíborvörös
- bárium lángszíne: fakózöld
- réz lángszíne: kékeszöld

### Adatok
- lítium hullámhossza: 670,8 nm
- nátrium hullámhossza: 589 nm
<!-- Pontosítás a tanárnak: a nátrium sárga fénye (589,0 és 589,6 nm, a „D-vonalak”) a külső (3s)
     elektron 3p → 3s átmenete – a „kijjebb lépés” tehát nem egy új héjra ugrás, hanem magasabb
     energiájú állapot ugyanabban a héjban; a rajz ezt egyszerűsíti. A lítium vonala 670,8 nm (NIST ASD).
     A kalcium, a stroncium és a bárium lángszínét nagyrészt a lángban keletkező molekulák (pl. CaOH,
     SrOH, BaOH/BaCl) adják, a rézét CuCl/CuOH – ezért nekik nem adunk meg egy hullámhosszt.
     A Z > 20 elemeknél (Sr, Ba, Cu) a rajz csak „belső héjak + külső elektron” sémát mutat.
     A színnevek a hazai kémiatankönyvek szokásos kifejezései. Biztonság: a bárium- és a
     stronciumsók, illetve a rézsók egy része mérgező; a lángfestést tanár végzi, védőszemüvegben. -->

## 8. Összefoglalás
- Az atom apró, nehéz **atommagból** és szinte üres **elektronburokból** áll.
- A **rendszám** (a protonok száma) határozza meg, melyik elem.
- Az elektronok héjakon vannak: 2, 8, 8… A ==külső elektronok== szabják meg, hogyan viselkedik az atom.
- Sor = héjak száma, oszlop = külső elektronok száma.

> megjegyzés: Mengyelejev {Mengyelejev táblázata}-ben még csak {ismert elemek 1869-ben} elemet ismert – a hiányzók helyét üresen hagyta.

### Feliratok
- összefoglaló 1: atommag + szinte üres elektronburok
- összefoglaló 2: rendszám = protonszám → ez dönti el az elemet
- összefoglaló 3: héjak: 2, 8, 8 … – a külső számít
- összefoglaló 4: sor = héjak száma, oszlop = külső elektronok
- atommag részei: atommag: protonok + neutronok
- elemek: # elem
- periódusok és csoportok: 7 periódus · 18 csoport
- Mengyelejev: Mengyelejev, #: még csak # ismert elem
- f-mező nélkül: (a lantanoidák és aktinoidák sora nélkül)

### Adatok
- elemek száma: 118
- Mengyelejev táblázata: 1869
- ismert elemek 1869-ben: 63
<!-- 118 elem: az IUPAC 2016 óta elismert és elnevezett elemei (Og, 118). Mengyelejev 1869. március 1-jén
     (Julián-naptár szerint február 17.) tette közzé táblázatát; akkor 63 elemet ismertek. -->

<!-- Modell-egyszerűsítések és források:
  - A Bohr-féle héjmodell szemléltetés: az elektron nem kering körpályán (4. lépés: felhőkép).
  - A rajzokon a mag hatalmasra nagyított (valójában ~60 000-szer kisebb az atomnál, 2. lépés).
  - Az elektronok és a nukleonok golyói, színei kódok, nem valódi színek; a sókristály „színe” is az.
  - A zoom teraszos felülete (lépcsők a kristálylapon) illusztráció; a lépték (léptékcsík, létra)
    ugyanabból a nagyításból számolódik, mint a rajz, így pontos.
  - Lángfestés: a „kijjebb ugró” elektron egyszerűsítés (lásd a 7. lépés megjegyzését).
  - Források: CRC Handbook of Chemistry and Physics (NaCl-rács, ionsugarak), NIST Atomic Spectra
    Database (Li 670,8 nm, Na 589,0/589,6 nm), CODATA 2018 (mp/me), IUPAC (atomtömegek, 118 elem).
-->
