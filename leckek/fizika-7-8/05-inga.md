# Mitől függ a hinta lengésideje? – periodikus mozgás
tantárgy: Fizika · évfolyam: 7–8. · témakör: 4. Lendület és egyensúly

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/05-inga.md

  A modell: pontszerű test súlytalan fonálon, súrlódás és légellenállás nélkül.
  A lecke a lengést a pontos (nem csak kis kitérésre érvényes) mozgásegyenletből számolja,
  ezért nagy kitérésnél a lengésidő valóban hosszabb: 30° → +1,7 %, 60° → +7,3 %, 90° → +18 %
  a kis kitéréses T = 2π·√(l/g) értékhez képest.
-->

## Közös

### Feliratok
- méterskála: 1 m
- idő tengely: idő ↑
- kitérés tengely: kitérés
- lengésszámláló: # lengés

### Adatok
- nehézségi gyorsulás a Földön: 9,81 m/s²
- inga hossza: 1,00 m
- kitérés: 15°
- kis kitérés szöge: 7°

## 1. Ismétlődő mozgások
A hinta, az ingaóra és a fonálinga ugyanazt a mozgást ismétli újra és újra. Az ilyen mozgás **periodikus**.

Figyeld meg: nem egyforma ütemben lengenek! ==Mitől függ, milyen gyorsan leng egy inga?==

> megjegyzés: Szavaztasd meg az osztályt: a test tömege, a kötél hossza vagy a kitérés számít?

### Feliratok
- hinta: hinta
- ingaóra: ingaóra
- fonálinga: fonálinga
- kérdés: Mitől függ, milyen gyorsan leng?

### Adatok
- hinta hossza: 2,50 m
- ingaóra hossza: 0,994 m
- fonálinga hossza: 0,25 m
<!-- Az ingaóra „másodpercingája” 0,994 m hosszú: lengésideje 2 s, minden kilengése 1 s. -->

## 2. Periódusidő, rezgésszám, amplitúdó
Az **amplitúdó** a legnagyobb kitérés. A **periódusidő** (T) egy teljes lengés ideje: oda és vissza. A **rezgésszám** (f) megmutatja, hány lengés történik 1 másodperc alatt.

képlet: f = 1 / T

Az egyenletesen haladó papírcsíkra az inga ==kirajzolja a saját mozgását==.

> megjegyzés: A rezgésszám mértékegysége a hertz: 1 Hz = 1 lengés másodpercenként.

### Feliratok
- amplitúdó: amplitúdó
- amplitúdó magyarázat: a legnagyobb kitérés
- periódusidő: periódusidő
- periódusidő magyarázat: egy teljes lengés ideje: oda és vissza
- rezgésszám: rezgésszám
- rezgésszám magyarázat: hány lengés 1 másodperc alatt

## 3. Mérjünk 10 lengést!
Kézzel stopperezünk, és egy gombnyomás kb. {kézi mérés hibája} hibát okoz. Egyetlen lengésnél ez sok!

Ha **10 lengést** mérünk és tízzel osztunk, a hiba is ==a tizedére csökken==. Több mérés átlaga még pontosabb.

> megjegyzés: Nyomd meg többször mindkét gombot, és hasonlítsd össze a két sor pontjait!

### Feliratok
- stopper: stopper
- gyorsítva: #× gyorsítva
- mérések cím: Egy lengés ideje (T) – mérések
- 1 lengésből: 1 lengésből
- 10 lengésből: 10 lengésből
- mérésszám: # mérés
- átlag: átlag
- számolt érték: számolt érték
- utolsó mérés: Utolsó mérés
- eltérés: eltérés a számolttól
- mérj tipp: Nyomd meg a „Mérj!” gombot!
- mérj 1 gomb: Mérj 1 lengést!
- mérj 10 gomb: Mérj 10 lengést!
- törlés gomb: Törlés

### Adatok
- kézi mérés hibája: 0,1 s
<!-- Becslés: a kézi stopperes időmérés szokásos bizonytalansága gombnyomásonként 0,1–0,2 s
     (reakcióidő ingadozása). A lecke gombnyomásonként 0,1 s szórású véletlen hibával számol. -->

## 4. Nehezebb test?
Sokan gondolják, hogy a nehezebb test gyorsabban leng. Próbáld ki: állítsd be a jobb oldali golyó tömegét!

A két görbe ==pontosan együtt halad==. A nehezebb golyót erősebben húzza a Föld, de ugyanannyiszor nehezebb meglódítani is. A kettő kiegyenlíti egymást.

> megjegyzés: Ez légellenállás nélkül igaz – kicsi, tömör testekre jó közelítés.

### Feliratok
- könnyű golyó: könnyű golyó
- nehéz golyó: nehéz golyó
- tömeg csúszka: A nehéz golyó tömege
- együtt: Pontosan együtt lengenek!

### Adatok
- könnyű golyó tömege: 0,1 kg
- nehéz golyó tömege: 2,0 kg

## 5. Nagyobb kitérés?
Nagyobb kitérésnél hosszabb utat tesz meg a test, de meredekebbről indul, ezért gyorsabban is halad. A kettő majdnem kiegyenlíti egymást.

Kis kitérésnél a lengésidő ==gyakorlatilag ugyanannyi==. Még 90°-nál is csak kb. 18 %-kal hosszabb – nem kétszer annyi!

> megjegyzés: Húzd a csúszkát 90°-ig, és figyeld, hogyan csúszik szét a két görbe!

### Feliratok
- kis kitérés: kis kitérés
- nagy kitérés: nagy kitérés
- kitérés csúszka: A jobb oldali inga kitérése

### Adatok
- nagy kitérés szöge: 60°

## 6. Hosszabb kötél
A bal oldali inga {fonálinga hossza} hosszú. Állítsd be a jobb oldalit! ==Négyszer hosszabb inga kétszer annyi idő alatt== leng egyet.

képlet: T ≈ 2π · √(l / g)

Itt l az inga hossza: a felfüggesztéstől a test közepéig.

> megjegyzés: Ha a hintán felállsz, a tested közepe feljebb kerül: rövidebb lesz az inga, gyorsabb a lengés.

### Feliratok
- rövid inga: rövid inga
- hosszú inga: hosszú inga
- hossz csúszka: A jobb oldali inga hossza

## 7. A hinta a Holdon
A Hold gyengébben vonzza a testeket: a nehézségi gyorsulás (g) ott csak {nehézségi gyorsulás a Holdon}, a Földön {nehézségi gyorsulás a Földön}.

Az inga ezért gyengébben gyorsul vissza középre: ==lassabban leng==. A lengésidő ezért – bármilyen hosszú az inga – majdnem 2,5-szer akkora.

> megjegyzés: Egy földi ingaóra a Holdon késne. Próbáld ki más hosszal is!

### Feliratok
- a Földön: a Földön
- a Holdon: a Holdon
- Holdra gomb: Vidd a Holdra!
- Földre gomb: Hozd vissza a Földre!
- közös hossz csúszka: Mindkét inga hossza
- föld ikon: Föld
- hold ikon: Hold

### Adatok
- nehézségi gyorsulás a Holdon: 1,62 m/s²

## 8. Összefoglalás
- A lengésidő **nem függ** a test tömegétől.
- Kis kitérésnél a kitéréstől sem; nagynál kicsit hosszabb.
- ==A hossztól függ==: négyszer hosszabb inga → kétszer akkora lengésidő.
- Ahol kisebb a nehézségi gyorsulás, ott lassabban leng.

> megjegyzés: Feladat: mérd meg egy hinta lengésidejét 10 lengésből – ülve és állva is!

### Feliratok
- mitől függ: Mitől függ a lengésidő?
- tömegtől: a test tömegétől
- kitéréstől: a kitéréstől
- hossztól: az inga hosszától
- g-től: a nehézségi gyorsulástól
- nem: nem
- alig: kis kitérésnél nem
- igen: igen
- összefoglaló lengésidők: lengésidők # kitérésnél
- tanulság: 4× hosszabb inga → 2× akkora lengésidő
