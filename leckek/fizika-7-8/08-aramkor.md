# Mi folyik a drótban? – töltés, áram, Ohm-törvény
tantárgy: Fizika · évfolyam: 7–8. · témakör: 6. Elektromosság a háztartásban

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/08-aramkor.md
  A képletekben az aláhúzás alsó indexet jelent: U_LED → U (alsó indexben: LED).

  A rajzon a pöttyök az ELEKTRONOK: a telep − pólusától a külső körön át a + pólus felé
  haladnak. A piros nyíl a megállapodás szerinti áramirány (+ → −), ezzel ellentétes.
  Modell: ideális telep és vezetékek; az izzó ellenállása állandó (U/I a névleges adatokból),
  a LED feszültsége vezetéskor állandó. A pöttyök sebessége arányos az áramerősséggel
  (felgyorsítva; a 8. lépésben más léptékben).

  Források, értékek:
  - 1 C töltés = 1 / (1,602·10⁻¹⁹ C) ≈ 6,24·10¹⁸ elektron töltése (kerekítve 6,25·10¹⁸).
  - Sodródási sebesség rézben: v = I / (n·e·A), n ≈ 8,5·10²⁸ /m³ → 1 A, 1 mm²: ≈ 0,07 mm/s.
  - Zsebizzó: 4,5 V / 0,3 A (E10 foglalat) → kb. 15 Ω üzemi (meleg) ellenállás.
  - Grafitbél (0,5 mm, HB): néhány tized ohm centiméterenként; a pontos érték a keménységtől
    és a gyártótól függ (0,7 mm-es HB bél 6 cm-en ≈ 2 Ω mérés alapján becsülve). Érdemes megmérni!
  - Piros LED: nyitófeszültség ≈ 1,8–2,2 V, üzemi áram 20 mA, abszolút maximum ≈ 30 mA.
-->

## Közös

### Feliratok
- atommag: atommag (+)
- elektron: elektron (−)
- elektronok mozgása: elektronok mozgása
- áram iránya: az áram iránya (megállapodás szerint)
- felgyorsítva: a pöttyök mozgása felgyorsítva
- izzó: izzó
- telep: telep
- ampermérő: ampermérő
- feszültségmérő: feszültségmérő
- áramerősség: áramerősség
- feszültség: feszültség
- ellenállás: ellenállás
- grafitbél: grafitbél (0,5 mm, HB)

### Adatok
- ceruzaelem feszültsége: 1,5 V
- laposelem feszültsége: 4,5 V
- 9 voltos elem feszültsége: 9,0 V
- izzó névleges feszültsége: 4,5 V
- izzó névleges árama: 0,30 A
- grafitbél ellenállása centiméterenként: 0,7 Ω
- grafitbél hossza: 12 cm

## 1. Dörzsöléskor elektronok vándorolnak
Dörzsölj meg egy gumilufit gyapjúval! Közben ==elektronok vándorolnak át== a gyapjúról a lufira.

Töltés nem keletkezik és nem tűnik el, csak átkerül. A lufin **elektrontöbblet** van: negatív lett. A gyapjún **elektronhiány**: pozitív. Ez az *elektromos állapot*.

> megjegyzés: Egy pötty itt sok milliárd elektront jelent.

### Feliratok
- atommag marad: atommag (+) – a helyén marad
- elektron vándorol: elektron (−) – átvándorolhat
- gyapjú: gyapjú
- lufi: gumilufi
- semleges: semleges
- elektronhiány: pozitív: elektronhiány
- elektrontöbblet: negatív: elektrontöbblet
- dörzsölés gomb: Dörzsöld még!

## 2. Vezető és szigetelő
A **fémben** az elektronok egy része szabad: a rögzített atomtörzsek között cikázik. A **műanyagban** minden elektron a saját atomjához kötött.

Kapcsold rá a telepet! A fémben az elektronok lassan elsodródnak: ez az ==elektromos áram==. A műanyag szigetel.

> megjegyzés: Rézdrótban (1 mm², 1 A) a sodródás csak kb. {sodródási sebesség}: egy csiga gyorsabb!

### Feliratok
- fém: réz – vezető
- műanyag: műanyag – szigetelő
- szabad elektron: szabad elektron
- kötött elektron: kötött elektron
- atomtörzs: atomtörzs (+)
- cikázás: cikázás + lassú sodródás
- van áram: folyik az áram
- nincs áram: nincs áram
- telep gomb: Telep be / ki

### Adatok
- sodródási sebesség: 0,07 mm/s

## 3. Zárt áramkör
Az elektronok **már ott vannak** a drótban, nem a telepből jönnek. Zárd a kapcsolót: ==mindenhol egyszerre indulnak el==, mint egy kerékpárlánc. Ezért gyullad fel azonnal az izzó.

Áram csak **zárt körben** folyik – egy vezeték nem elég!

> megjegyzés: A pöttyök az elektronok: a − pólustól a + felé haladnak. A megállapodás szerinti áramirány ezzel ellentétes.

### Feliratok
- kapcsoló: kapcsoló
- kapcsoló gomb: Kapcsoló be / ki
- egy vezeték gomb: Csak egy vezeték?
- már ott vannak: az elektronok már a drótban vannak
- egyszerre: Mind egyszerre indul – mint egy lánc!
- nyitott kör: nyitott kör – nincs áram
- zárt kör: zárt kör – folyik az áram
- hiányzó vezeték: hiányzik a visszavezető drót

## 4. Az áram nem fogy el
Tegyél ampermérőt az izzó **elé és mögé**! Mindkettő ugyanannyit mutat: ==amennyi töltés befolyik, annyi ki is jön==.

Az izzó nem az áramot használja el, hanem az **energiát** alakítja fénnyé és hővé. Az ampermérő azt méri, mennyi töltés halad át másodpercenként.

> megjegyzés: Húzd a harmadik ampermérőt bárhová a körben!

### Feliratok
- izzó előtt: az izzó előtt
- izzó után: az izzó után
- húzz: húzz el!
- másodpercenként: elektron halad át másodpercenként
- tévhit: „Az izzó elhasználja az áramot.”
- mindenhol ugyanannyi: Mindenhol ugyanannyi!

### Adatok
- elektronok száma 1 C töltésben: 6 250 000 000 000 000 000 db

## 5. Feszültség: a hajtóerő
A telep **hajtja körbe** az elektronokat. Hogy mennyire erősen, azt a **feszültség** mutatja; mértékegysége a volt (V).

Válts nagyobb feszültségű telepre: ==nagyobb lesz az áram==, gyorsabban haladnak a töltések, és fényesebb az izzó.

> megjegyzés: Az izzó {izzó névleges feszültsége}-ra készült, a 9 V kiégetné. Ellenállását állandónak vesszük.

### Feliratok
- ceruzaelem gomb: Ceruzaelem
- laposelem gomb: Laposelem
- 9 V gomb: 9 V-os elem
- a telepen: a telepen
- az izzón: az izzón
- kiégne: Túl nagy feszültség – kiégne!
- halvány: alig izzik

## 6. Ellenállás: a grafitbél
Kössünk az izzó elé egy **grafitbelet** (ceruzabelet)! A csipeszt húzva változik, mekkora darabon kell átjutniuk a töltéseknek.

Hosszabb grafiton ==nagyobb az ellenállás==: kisebb az áram, halványabb az izzó. A csipesz utáni részen nem folyik áram.

> megjegyzés: Az ellenállás mértékegysége az ohm (Ω). Itt 1 cm grafitbél kb. {grafitbél ellenállása centiméterenként}.

### Feliratok
- csipesz csúszka: A grafitbél hossza a csipeszig
- csipesz: csipesz – húzd!
- itt nem folyik: itt nem folyik áram
- a grafiton: a grafiton
- hossz: hossz
- feszültségek összege: telep = izzó + grafit

### Adatok
- csipesz helye: 10 cm

## 7. Ohm törvénye
Mérjük a grafitbél **feszültségét** és az **áramerősséget** 1, 2, majd 3 elemmel! A pontok egy origón átmenő egyenesre esnek.

Kétszer akkora feszültség ==kétszer akkora áramot== hajt át. Az U / I hányados állandó: ez a grafit **ellenállása**.

> megjegyzés: Húzd odébb a csipeszt, és mérj újra! Milyen lesz az egyenes?

### Feliratok
- 1 elem gomb: 1 elem
- 2 elem gomb: 2 elem
- 3 elem gomb: 3 elem
- tengely U: a grafiton mért feszültség (V)
- tengely I: áramerősség (A)
- hányados: U / I =

## 8. LED és potenciométer
A **LED** csak egy irányban vezet, és kb. {LED nyitófeszültsége} jut rá. A többi az ellenállásokra jut.

A **potenciométerrel** az áramot és a fényt szabályozzuk. ==Előtét-ellenállás nélkül a LED kiég!==

> megjegyzés: 9 V-ról {előtét-ellenállás} kell: 7 V : 330 Ω ≈ 21 mA.

### Feliratok
- pot csúszka: Potenciométer
- fordít gomb: Fordítsd meg a LED-et
- előtét gomb: Előtét-ellenállás be / ki
- új LED gomb: Új LED
- LED: LED
- előtét: előtét-ellenállás
- nincs előtét: nincs előtét-ellenállás
- potméter: potenciométer
- kiégett: A LED kiégett!
- záróirány: fordítva: nem vezet
- összesen: összesen
- gyorsítás: itt a pöttyök 20× gyorsabbak

### Adatok
- LED nyitófeszültsége: 2,0 V
- LED üzemi árama: 20 mA
- LED legnagyobb árama: 30 mA
- előtét-ellenállás: 330 Ω
- potenciométer legnagyobb értéke: 4700 Ω

## 9. Összefoglalás
- Elektromos állapot: **elektrontöbblet** (−) vagy **elektronhiány** (+).
- Áram: töltések áramlása **zárt körben**. Mindenhol egyszerre indulnak, de lassan haladnak.
- ==Az áram nem fogy el==: a kör minden pontján ugyanannyi.
- A feszültség hajtja, az ellenállás korlátozza: I = U / R.

> megjegyzés: Mekkora áram folyik át egy 23 Ω-os vasalón 230 V-on?

### Feliratok
- jelentés I: áramerősség – amper (A)
- jelentés U: feszültség – volt (V)
- jelentés R: ellenállás – ohm (Ω)
- ugyanannyi: ugyanannyi
- tanulság: Az áram nem fogy el: a feszültség hajtja, az ellenállás korlátozza.
