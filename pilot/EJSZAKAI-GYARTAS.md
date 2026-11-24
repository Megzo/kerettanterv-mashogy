# Éjszakai gyártás: 5 sorozat (2026-11-23/24)

Öt leckesor készült egy éjszaka alatt, a felhasználó távollétében: a terveket a koordinátor
hagyta jóvá, egyszerre legfeljebb 5 al-ügynök futott (a sorozatok között megosztva). A számok
a sorozatok `METRIKAK.md`-jéből valók (szkripttel számolva); a token az al-ügynökök saját,
Claude Code által jelentett fogyasztása (a leckéknél ezresre kerekítve), a koordináló fő
munkamenet nélkül.

| Sorozat | Leckék | Lépések | Al-ügynök-idő (terv + leckék) | Token (terv + leckék) | Lecke átlag (idő / token) | Új modulok | Review-pontok | Kötelező lektor |
|---|---|---|---|---|---|---|---|---|
| [Matematika 5–6.](matematika-5-6/METRIKAK.md) | 18 | 160 | 10,0 óra | ~3 726 ezer | 32 p 16 mp / ~192 ezer | 10 | 87 | 0 |
| [Kémia 7–8.](kemia-7-8/METRIKAK.md) | 14 | 121 | 9,2 óra | ~3 338 ezer | 38 p 5 mp / ~221 ezer | 13 | 84 | 0 |
| [Biológia 7–8.](biologia-7-8/METRIKAK.md) | 17 | 153 | 10,6 óra | ~3 589 ezer | 36 p 11 mp / ~196 ezer | 10 | 97 | 3 |
| [Földrajz 9–10.](foldrajz-9-10/METRIKAK.md) | 15 | 135 | 11,3 óra (+ G2 előkészítés) | ~4 116 ezer | 41 p 45 mp / ~239 ezer | 5 | 98 | 0 |
| [Matematika 9–10.](matematika-9-10/METRIKAK.md) | 15 | 135 | 8,7 óra | ~3 208 ezer | 33 p 35 mp / ~198 ezer | 7 | 66 | 0 |
| **Összesen** | **79** | **704** | **49,8 óra** | **~17 978 ezer** | 36 p 12 mp / ~208 ezer | **45** | **432** | **3** |

- Egy lecke: átlag **36 p 12 mp**, medián 35 p 19 mp; átlag **~208 ezer**, medián ~213 ezer token (a fizika-pilotban ~31 perc / ~315 ezer, a történelemben ~38 perc volt).
- Falióra: az első terv commitjától (11-23 20:41) az utolsó lecke commitjáig (11-24 07:02): **10,3 óra**; ez alatt 51,5 óra al-ügynök-munka (átlagosan 5,0 párhuzamos al-ügynök).
- Minden al-ügynök együtt (tervek, leckék, G2, kész közös munkák): **51,5 óra**, **~18 805 ezer token**.
- QA: mind a 79 lecke 0 JS-hibával, 0 túlcsordulással/átfedéssel zárt; minden sorozat commitolva.

## Közös munkák

| # | Feladat | Kész | Időtartam | Token | Érintett sorozatok |
|---|---|---|---|---|---|
| F1 | Fontkészlet: matematikai és kémiai jelek (STIX Two, Noto Sans Math) | 11-23 20:53 | 13 p 37 mp | 159 515 | mind az 5 |
| P1 | Build, QA és szerződés: jelölések, adattípusok, `shared/matek/mtext.js` | 11-23 21:13 | 29 p 5 mp | 161 100 | mind az 5 |
| J1 | MatText: görög kisbetűk dőlt változóként | 11-23 22:28 | 5 p 52 mp | ~115 ezer | Matematika 5–6., Matematika 9–10. |
| J2 | Motorjavítás: gyors kattintás, `slider.set` fire, QA-ugrópróba, build: képlet a címben, ion a feliratban | 11-24 00:07 | 37 p 49 mp | ~245 ezer | mind az 5 |
| J3 | Ugrópróba-javítás 7 leckében (állapot az `init()`-ben is) | 11-24 00:24 | 16 p 21 mp | ~147 ezer | Biológia 7–8., Matematika 5–6., Matematika 9–10. (és 3 fizika-, 1 történelem-lecke) |
| E1 | Matek-modulok egységesítése | folyamatban (indult 11-24 06:35) | – | – | Matematika 5–6., Matematika 9–10. |
| E2 | Kémia- és biológia-modulok egységesítése | folyamatban (indult 11-24 06:37) | – | – | Kémia 7–8., Biológia 7–8. |
| M1 | Metrikák összesítése (ez a dokumentum) | folyamatban (indult 11-24 07:01) | – | – | mind az 5 |
| G2 | Földrajzi adatfájlok (13 fájl, Equal Earth) – a Földrajz 9–10 sorozathoz számolva | 11-23 21:14 | 31 p 29 mp | 266 291 | Földrajz 9–10. (a biológia 05, 08 is használja) |

Kész közös munkák összesen: 1,7 óra, ~828 ezer token.

## Tanulságok

1. **A modulöröklés működik.** 45 új modul épült. A 77 metrikasorból 67 jelzi, hogy egy korábbi lecke blokkját bájtra azonosan (diff/md5/cmp) vette át; a kémia 12-viztisztitas például 11 modult örökölt, köztük két földrajzit. A modulhibákat a másoló nem javítja a blokkban, csak jelzi (→ E1/E2 egységesítés).
2. **Egységes modulhatárok kellenek.** A blokkvég-jelölő nem egységes (`MODUL VÉGE: …` vs. `MODUL VÉGE ──`, 3 metrikasor említi); egy szkriptes másolás emiatt két fölösleges blokkot is bemásolt. A TortSource idővonal nélkül `ReferenceError`-t dob, ezért 6 lecke `TortTimeline`-csonkot tesz be.
3. **A tartalomfájl buktatói ismétlődnek.** A Feliratok és az Adatok kulcsai közös névtérben vannak, ezért ütköznek (6 metrikasor). Más kis hibák is ismétlődnek: kettőspont a kulcsban, `^`-os ion a feliratban, képlet a `#` címsorban, sima szóköz a „105 : 100”-ban és a „%” előtt, `dim` + `int` SI-egységben. A build hibaüzenete jó, a szerződésbe érdemes felvenni a szabályokat.
4. **A QA-állapotok és a vezérlők nincsenek szinkronban.** A `slider.set()` nem hívta az `onInput`-ot (J2 javította), a `--states` a lépés elején állít, de settle-kor fotóz, a `__qaStates` kulcsa 1-alapú. 8 metrikasor ír külön kerülőútról. Egy „radio” gombcsoport és egy csendes `slider.set` sok kódot spórolna.
5. **A 22 px-es alsó határ a képleteknél csúszik el.** A MatText kitevője, indexe és törtje (0,65×, 0,8×), meg a `max`-szal kicsinyített képletsor könnyen 22 px alá esik (6 metrikasor). Ugyanez a buktató a mono alapfont folyó szövegnél és a dőlt mértékegység. A MatText-be kell a javítás, nem leckénként.
6. **Az áttűnés és a visszaugrás külön próbát kér.** A közvetlen lépésugrásnál a köztes jelenetek is rajzolódnak, ezért az állapotot az `init()`-ben is be kell állítani (J3: 7 lecke javítva). A `globalAlpha`-t egyes modulok abszolút állítják, mások szorozzák (2 metrikasor). Az ugrópróba a J2 óta a QA része.
7. **Az al-ügynökök a briefet is ellenőrzik.** 10 metrikasor ír tudatos eltérést a brieftől vagy hibát a briefben. Példák: a Thalész-kör belül tompa, kívül hegyes (a brief fordítva írta); 12 %-os bornál nincs 78 °C-os plató; az újraélesztésnél az ERC 2025 sorrendje; Semmelweis 9,9/3,9 %-a. A koordinátori brief tehát nem megbízható forrás: a tanári review-nak ezeket kell először látnia.
8. **A review lett a szűk keresztmetszet.** 432 review-pont gyűlt össze (5,5/lecke). 3 lecke (újraélesztés, járvány, magzat) szakmai lektor nélkül nem használható. Licenckérdés: a GFN-adatok CC BY-SA 4.0 licencűek (15-okologiai-labnyom: csak kerekített értékek; a felhasználó döntése (2026-11-24): külön adatfájl nem kell, maradnak a kerekített értékek), a WUP 2018 licence (CC BY 3.0 IGO, 10-nepesseg) ellenőrizendő. Működési tanulság még: két al-ügynök ugyanazt a scratchpad-almappát használta, és felülírták egymás félkész kódját – ügynökönként egyedi munkamappa kell.

## Kerethasználat (előfizetési limit)

Mérés a felhasználó becslése alapján (2026-11-24): a gyártás előtt heti limit-reset volt, egy este után
a heti keret **41 %**-on állt; párhuzamos egyéb munkák mellett ebből legalább **~35 %** ez a projekt.
Előfizetés: Claude Ultra (200 $/hó), modell: Opus 5.5, high thinking. Ebbe beletartozik minden: az 5 terv,
a közös előkészítés (fontok, build, geoadat, motor), a 79 lecke, a javító- és egységesítő körök és a
koordinátor.

| Egység | Heti keret (kb.) |
|---|---|
| 1 lecke | **~0,45 %** (35 % / 79) |
| 1 sorozat (15–18 lecke, tervvel, közös modulokkal) | **~7 %** |
| 10 % keret | ~22 lecke |

Ökölszabály a folytatáshoz: a reset környékén megmaradó szabad keretből egy-egy sorozat (vagy néhány
lecke) gyártható; egy új sorozat ~7 %, egy meglévő sorozat további leckéje (kész modulokkal) ennél
olcsóbb. A becslés egyetlen mérésből és a felhasználó kerekítéséből származik – a következő
gyártásoknál érdemes újra mérni (keret % a gyártás előtt és után).
