# Miért mindig derékszög? – Thalész-tétel, érintő, körív
tantárgy: Matematika · évfolyam: 9–10. · témakör: 14. A kör és részei

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/matematika-9-10/11-kor-thalesz.md
  A pontok betűi (A, B, C, C′, O, E, X, F, P, E₁, E₂) és a szögek betűi (α, β, γ, ψ) a vásznon kódban
  rögzítettek. Színek: α kékeszöld, β okker, γ (a C-nél lévő szög) cinóber – az 1–3. lépésben ugyanígy.
-->

## Közös

### Feliratok
- mérés: mérés
- bizonyítás: bizonyítás
- húzd a C-t: húzd a C-t!
- húzd a P-t: húzd a P-t!
- C csúszka: C helye a körön
- újra gomb: Újra
- Thalész-kör: Thalész-kör
- átmérő: átmérő

### Adatok
<!-- Az 5–7. lépés körének sugara és a 7. lépés példája (P a középponttól 13 cm-re). A lecke ellenőrzi,
     hogy az érintőszakasz = √(OP² − r²) (különben piros sáv jelez). -->
- kör sugara: 5 cm
- OP távolság: 13 cm
- érintőszakasz: 12 cm

## 1. Mérjük meg a szöget! (sejtés)
Az AB szakasz a kör **átmérője**, a C pont a körön mozog. Húzd a C-t! Az A-nál és a B-nél lévő szög változik, ==a C-nél lévő mindig 90°.== De ez csak mérés, néhány helyzetben.

> megjegyzés: A hagyomány szerint a tételt Thalész (Milétosz, Kr. e. 6. század) mondta ki – erről csak jóval későbbi szerzők írnak.

### Feliratok
- cím 1: Milyen szög van a C-nél?
- napló cím: Mérési napló
- feljegyzem gomb: Feljegyzem
- tévhit tető: A félkör tetején a legnagyobb a szög.
- cáfolat tető: Nem: mindenütt 90°!
- sejtés: Sejtés: a C-nél mindig derékszög van.
- félkör: félkör

## 2. Két egyenlő szárú háromszög (bizonyítás)
Húzzuk be az OC sugarat! `OA = OB = OC`, ezért az AOC és a BOC háromszög **egyenlő szárú**: alapjuknál α, α és β, β. A szögösszeg `2α + 2β = 180°`, tehát ==`γ = α + β = 90°`.== Bármely C-re igaz.

> megjegyzés: Kitekintés: az AOB középponti szög 180°, a C-nél lévő szög ennek a fele.

### Feliratok
- cím 2: Miért mindig derékszög?
- biz 1: `OA = OB = OC = r` (sugarak)
- biz 2: AOC és BOC egyenlő szárú,
- biz 3: alapjuknál egyenlő szögek: α és β
- biz 4: szögösszeg: `2α + 2β = 180°`
- biz 5: tehát `γ = α + β = 90°`
- minden C-re: Bármely C-re ugyanez a gondolatmenet.

## 3. A megfordítás: belül tompa, kívül hegyes
Fordítva is igaz: ha a C-nél derékszög van, a C az AB fölé írt körön van. Tükrözzük C-t az O-ra: `ACBC′` paralelogramma, mert átlói felezik egymást. Derékszöggel **téglalap**, így átlói egyenlők: `CC′ = AB`, vagyis `OC = OA`. ==A körön belül tompa, kívül hegyes a szög.==

### Feliratok
- cím 3: Ha derékszög, akkor a körön van?
- belül: a körön belül: tompaszög
- rajta: a körön: derékszög
- kívül: a körön kívül: hegyesszög
- megf 1: C tükörképe O-ra: C′
- megf 2: `ACBC′` paralelogramma,
- megf 3: mert átlói felezik egymást.
- megf 4: Ha `γ = 90°`, téglalap:
- megf 5: `CC′ = AB`, így `OC = r`.
- ponthalmaz: Ahonnan AB derékszögben látszik: a Thalész-kör (A és B nélkül).
- belül gomb: C belül
- körön gomb: C a körön
- kívül gomb: C kívül
- távolság csúszka: C távolsága O-tól

## 4. Ácstrükk: hol a kör középpontja?
Hol van egy kerek lap közepe? Az asztalos a **derékszögű vonalzó** csúcsát a lap szélére teszi. A két szár a peremet P-ben és Q-ban metszi – a megfordítás miatt ==PQ átmérő.== Két különböző átmérő metszéspontja a középpont. Forgasd el a vonalzót: a vonal mindig átmegy a középponton!

### Feliratok
- cím 4: Hol a kerek lap közepe?
- vonalzó: derékszögű vonalzó
- átmérő 1: 1. átmérő
- átmérő 2: 2. átmérő
- középpont: középpont
- körzővel: körzővel: pontosan a peremen fut
- forgatás csúszka: a vonalzó elforgatása
- áthelyezés gomb: Máshová teszem
- ács 1: A vonalzó csúcsa a peremen, a szög 90°,
- ács 2: így a megfordítás miatt PQ átmérő.

## 5. Szelőből érintő
Az egyenes az E pont körül forog. Általában két közös pontja van a körrel, E és X: ez **szelő**. `OE = OX`, ezért O vetülete, az F felezi EX-et. X csak akkor esik E-re, ha F = E: ==az érintő merőleges az érintési pontba húzott sugárra.==

### Feliratok
- cím 5: Mikor lesz a szelőből érintő?
- szelő: szelő
- érintő: érintő
- szög csúszka: az egyenes és a sugár szöge
- majdnem gomb: 88°: majdnem
- érintő gomb: 90°: érintő
- nagyítás: nagyítás 10×
- tévhit súrol: Ami a rajzon súrolja a kört, az érintő.
- cáfolat súrol: Nagyítva még két közös pont: szelő!
- biz e1: O vetülete az egyenesre: F
- biz e2: `OE = OX = r`, így `EF = FX`
- biz e3: `X = E` pontosan akkor, ha `F = E`,
- biz e4: vagyis ha `OE ⊥ e`.
- közös pont: közös pont

## 6. Érintő szerkesztése külső pontból
Hol érinti a P-ből húzott érintő a k kört? Az E érintési pontban `OE ⊥ PE`, vagyis E-ből az OP szakasz derékszögben látszik. ==E tehát az OP fölé írt Thalész-körön van.== Felezzük meg OP-t, rajzoljuk meg a Thalész-kört: ahol k-t metszi, ott vannak az érintési pontok.

### Feliratok
- cím 6: Érintő szerkesztése külső pontból
- szerk cím: A szerkesztés lépései
- szerk 1: 1. Kössük össze O-t és P-t.
- szerk 2: 2. Felezzük meg OP-t: F.
- szerk 3: 3. Kör F körül, OP átmérővel (Thalész-kör).
- szerk 4: 4. A két kör metszéspontjai: E₁ és E₂.
- szerk 5: 5. A PE₁ és a PE₂ egyenes az érintő.
- kör k: k

## 7. Két egyenlő érintőszakasz
Az `OE_1P` és az `OE_2P` háromszög derékszögű, átfogójuk közös (OP), és `OE_1 = OE_2 = r`. Pitagorasz-tétellel `PE = √(OP^2 − r^2)` – mindkettőre ugyanaz: ==a külső pontból húzott két érintőszakasz egyenlő hosszú.== Például {kör sugara} sugárnál, `OP =` {OP távolság} esetén `PE =` {érintőszakasz}.

### Feliratok
- cím 7: Két egyenlő érintőszakasz
- tükrös: OP-re tükrözve fedik egymást
- távolság csúszka 7: P távolsága O-tól
- példa gomb: 13 cm-es példa
- tükrözés gomb: Tükrözés OP-re
- biz t1: `OE ⊥ PE`, OP közös
- biz t2: `OE_1 = OE_2 = r`
- biz t3: `PE = √(OP^2 - r^2)`

## 8. Ív és körcikk: arányos a szöggel
Ha a középponti szög (α) kétszeres, az **ív** és a **körcikk** is kétszeres: arányosak a szöggel.

képlet: i = 2rπ · (α) / (360°)

{cikk sugara} sugárnál, {középponti szög}-nál `i ≈` {ív hossza}, `t ≈` {körcikk területe}. ==A húr nem arányos!==

> megjegyzés: Feladat: a {gyűrű külső sugara} és {gyűrű belső sugara} sugarú körgyűrű területe? (≈ {körgyűrű területe})

### Feliratok
- cím 8: Ív és körcikk: arányos a szöggel
- ív: ív
- körcikk: körcikk
- húr: húr
- szög csúszka 8: középponti szög
- alap gomb: 72°
- dupla gomb: kétszeres szög
- tévhit húr: Kétszeres szöghöz kétszeres húr tartozik.
- cáfolat húr: Az ív kétszeres, a húr nem!
- hányad: a teljes kör része:
- arány fej: a 72°-hoz képest

### Adatok
<!-- Számpélda (terv, 11. brief): r = 10 cm, α = 72° → i = 2π · 10 · 72/360 = 4π ≈ 12,57 cm;
     t = π · 10² · 72/360 = 20π ≈ 62,83 cm². A lecke a sugárból és a szögből számolja és ellenőrzi. -->
- cikk sugara: 10 cm
- középponti szög: 72°
- ív hossza: 12,57 cm
- körcikk területe: 62,83 cm²
<!-- Körgyűrű: π · (10² − 6²) = 64π ≈ 201,06 cm² (a lecke ellenőrzi). -->
- gyűrű külső sugara: 10 cm
- gyűrű belső sugara: 6 cm
- körgyűrű területe: 201,06 cm²

## 9. Összefoglaló
- Thalész-tétel: ha AB átmérő és C a körön van, a C-nél derékszög van
- megfordítva: a derékszög csúcsa az átfogó fölé írt körön van
- az érintő merőleges az érintési pontba húzott sugárra
- külső pontból két egyenlő hosszú érintőszakasz húzható
- az ív és a körcikk egyenesen arányos a középponti szöggel

==Derékszöget látsz? Keresd a Thalész-kört!==

### Feliratok
- össz th cím: Thalész-tétel
- össz th 1: AB átmérő, C a körön ⇒ `γ = 90°`
- össz th 2: és megfordítva
- össz é cím: Érintő
- össz é 1: merőleges a sugárra
- össz é 2: szerkesztés: Thalész-körrel
- össz sz cím: Érintőszakaszok
- össz sz 1: `PE_1 = PE_2`
- össz sz 2: `PE = √(OP^2 - r^2)`
- össz ív cím: Ív és körcikk
- össz ív 1: `i = 2rπ · α/360°`
- össz ív 2: `t = r^2π · α/360°`

<!-- Matematikai ellenőrzés (Python 3, 2026-11-24):
  - Thalész-tétel (2. lépés): OA = OB = OC ⇒ az AOC és a BOC háromszög egyenlő szárú; szögösszeg
    2α + 2β = 180° ⇒ α + β = 90°. A lecke a rajzolt C minden helyzetében ellenőrzi, hogy ACB∢ = 90° (1e−6°)
    és hogy OAC∢ = OCA∢, OBC∢ = OCB∢.
  - Megfordítás (3. lépés): C′ = C tükörképe O-ra; az ACBC′ négyszög átlói (AB és CC′) felezik egymást ⇒
    paralelogramma; egy derékszöggel téglalap ⇒ átlói egyenlők ⇒ OC = AB/2. A lecke ellenőrzi:
    γ > 90° ⇔ OC < r ⇔ CC′ < AB, γ < 90° ⇔ OC > r (A és B kivételével, az AB egyenesén kívül).
  - Ácstrükk (4. lépés): a derékszögű vonalzó csúcsa a körön, szárai a peremet P-ben és Q-ban metszik ⇒
    PCQ∢ = 90° ⇒ (megfordítás) C a PQ fölé írt Thalész-körön van; a P, Q, C-n átmenő kör egyértelmű, így
    ez maga a lap pereme, és PQ az átmérője. A lecke ellenőrzi, hogy mindkét PQ átmegy a középponton.
  - Érintő (5. lépés): F = O vetülete az e egyenesre; E tükörképe F-re (X) is a körön van (OX = OE);
    X = E ⇔ F = E ⇔ OE ⊥ e. A húr hossza EX = 2r · cos ψ (ψ: az egyenes és az EO sugár szöge);
    r = 5 cm, ψ = 88°: EX ≈ 0,35 cm – a vásznon 10×-es nagyításban látszik.
  - Érintő szerkesztése (6. lépés): az E pont az OP fölé írt Thalész-körön van ⇒ OEP∢ = 90° ⇒ PE ⊥ OE.
    A lecke a MatSzerk Z.tangent-jével számolja az érintési pontokat, és ellenőrzi, hogy (1) a k körön
    vannak, (2) OE ⊥ PE, (3) egyeznek a Thalész-kör és a k kör metszéspontjaival.
  - Érintőszakaszok (7. lépés): PE = √(OP² − r²); r = 5 cm, OP = 13 cm → √(169 − 25) = √144 = 12 cm.
  - Ív és körcikk (8. lépés): i = 2rπ · α/360°, t = r²π · α/360°; r = 10 cm, α = 72°: i = 4π ≈ 12,566 cm,
    t = 20π ≈ 62,832 cm². Húr: h = 2r · sin(α/2): 72°-nál ≈ 11,76 cm, 144°-nál ≈ 19,02 cm (aránya ≈ 1,618,
    nem 2 – érdekesség: ez éppen az aranymetszés aránya, a szabályos ötszög átlója : oldala). A szinusz
    a vásznon nem szerepel, a lecke a húrt a rajzolt végpontok távolságából méri.
    Körgyűrű: π · (10² − 6²) = 64π ≈ 201,06 cm².
  - Történeti adat: a tételt a hagyomány Thalésznek (Milétoszi Thalész, kb. Kr. e. 624 – kb. 546) tulajdonítja;
    a forrás Diogenész Laertiosz (Kr. u. 3. század), aki Pamphilére hivatkozik – ezért „a hagyomány szerint”.
    Ellenőrizendő tankönyvi forrással.
  - Tankönyvi jelölés: a C-nél lévő szög γ, a középponti szög α (a 8. lépésben új jelentéssel – a tanár
    jelezze, ha zavaró); a körív hossza i, a körcikk területe t (tankönyvenként: i/l, t/T).
-->
