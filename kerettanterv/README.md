# Kerettantervek (NAT 2020) – Markdown

- **Forrás:** Oktatási Hivatal – [A 2020-as NAT-hoz illeszkedő tartalmi szabályozók](https://www.oktatas.hu/kozneveles/kerettantervek/2020_nat)
- **Letöltve:** 2026-11-12 · az eredeti fájlok: `sources/oktatas.hu_2020_nat/` (`manifest.json`: URL + SHA-256)
- **Hatály:** a kerettantervek 2020. szeptember 1-jétől felmenő rendszerben (1., 5., 9., ill. a 6 évfolyamos gimnáziumok 7. évfolyamán) bevezetett Nat 2020-hoz tartoznak (OH tájékoztató). A 8 évfolyamos gimnáziumoknak nincs külön kerettanterve (az 5–8. és 9–12. évfolyamosakat használják); a technikum a gimnáziumi kerettanterveket használja.
- **Nem része:** szakképző iskola, felnőttoktatás, nemzetiségi, SNI- és két tanítási nyelvű kerettantervek, a „7. melléklet” szerinti választható kerettantervek.
- **Konverzió:** `tools/build_kerettanterv.py` (pandoc). A szöveg a forrásé; a tagolás egységesített. Ellenőrzési napló: [`ellenorzes.txt`](ellenorzes.txt).

Összesen **1091 témakör**. A „táblázat” oszlop a dokumentum saját áttekintő táblázata, ezzel vetettük össze a szövegből kinyert témaköröket.

### Az ellenőrzés eltéréseinek tipikus okai

Az eltérések többsége **a forrásdokumentumon belüli** (táblázat ≠ részletes szöveg), nem konverziós hiba:

- A táblázatban olyan sor van, amihez nincs kifejtett témakör: „Évente két mélységelvű téma” (történelem), „Rendszerező összefoglalás” (matematika 11–12.), „Ismétlés, felkészülés az érettségire”, „Téli tevékenységek” (technika C modul).
- A témakör címe a táblázatban és a szövegben kicsit más (pl. „A dualizmus kori Magyarország” ↔ „A dualizmus kora”), vagy egy táblázatsor a szövegben két témakörre bomlik (földrajz 7–8.: Európa / Európán kívüli kontinensek).
- Óraszám: hiányzó vagy eltérő érték a táblázatban (pl. fizika 9–10. hat évf.: üres cella), változatonként megadott óraszám (dráma: „A változat: 3 óra, B változat: 1 óra”; ének-zene: osztályonként), vagy nem számszerű (gyógytestnevelés).
- **Magyar nyelv és irodalom:** hierarchikus szerkezet (nagy témakör → szerzők/művek saját óraszámmal); a résztémák a témakör szövegében megvannak, de az áttekintő táblázat sorai nem feleltethetők meg 1:1-ben. Ezt a tárgyat érdemes külön átnézni.
- Latin nyelv, mozgóképkultúra: régi .doc, régi típusú szerkezet – csak nyers szövegként.

## Általános iskola

| Tantárgy | Sáv | Témakör | Óraszám | Táblázat | Ellenőrzés |
|---|---|---|---|---|---|
| Biológia | [7–8](biologia/7-8.md) | 13 | 102 | 13 / 102 óra | eltérés: táblázat 13 / szöveg 13 |
| Digitális kultúra | [3–4](digitalis-kultura/3-4.md) | 6 | 68 | 6 / 68 óra | OK |
| Digitális kultúra | [5–6](digitalis-kultura/5-6.md) | 8 | 68 | 8 / 68 óra | OK |
| Digitális kultúra | [7–8](digitalis-kultura/7-8.md) | 9 | 68 | 9 / 68 óra | OK |
| Dráma és színház | [5–8](drama-es-szinhaz/5-8.md) | 9 | 34 | 9 / 34 óra | OK |
| Etika | [1–2](etika/1-2.md) | 6 | 68 | 6 / 68 óra | OK |
| Etika | [3–4](etika/3-4.md) | 6 | 68 | 6 / 68 óra | OK |
| Etika | [5–6](etika/5-6.md) | 6 | 68 | 6 / 68 óra | OK |
| Etika | [7–8](etika/7-8.md) | 6 | 68 | 6 / 68 óra | OK |
| Fizika | [7–8](fizika/7-8.md) | 10 | 102 | 10 / 102 óra | OK |
| Földrajz | [7–8](foldrajz/7-8.md) | 8 | 102 | 7 / 60 óra | eltérés: táblázat 7 / szöveg 8 |
| Hon- és népismeret | [5–8](hon-es-nepismeret/5-8.md) | 3 | 34 | 3 / 34 óra | OK |
| Kémia | [7–8](kemia/7-8.md) | 6 | 102 | 6 / 102 óra | OK |
| Környezetismeret | [3–4](kornyezetismeret/3-4.md) | 7 | 68 | 7 / 68 óra | OK |
| Közösségi nevelés (osztályfőnöki) | [5–6](kozossegi-neveles/5-6.md) | 5 | 68 | 5 / 68 óra | OK |
| Közösségi nevelés (osztályfőnöki) | [7–8](kozossegi-neveles/7-8.md) | 5 | 68 | 5 / 68 óra | OK |
| Magyar nyelv és irodalom | [1–2](magyar-nyelv-es-irodalom/1-2.md) | 15 | 504 | 17 / 476 óra | eltérés: táblázat 17 / szöveg 15 |
| Magyar nyelv és irodalom | [3–4](magyar-nyelv-es-irodalom/3-4.md) | 17 | 360 | 19 / 340 óra | eltérés: táblázat 19 / szöveg 17 |
| Magyar nyelv és irodalom | [5–6](magyar-nyelv-es-irodalom/5-6.md) | 18 | 216 | 18 / 207 óra | eltérés: táblázat 18 / szöveg 18 |
| Magyar nyelv és irodalom | [7–8](magyar-nyelv-es-irodalom/7-8.md) | 13 | 61 | 26 / 257 óra | eltérés: táblázat 26 / szöveg 13 |
| Matematika | [1–2](matematika/1-2.md) | 22 | 272 | 22 / 272 óra | OK |
| Matematika | [3–4](matematika/3-4.md) | 26 | 272 | 26 / 272 óra | OK |
| Matematika | [5–6](matematika/5-6.md) | 18 | 272 | 18 / 272 óra | OK |
| Matematika | [7–8](matematika/7-8.md) | 12 | 204 | 12 / 204 óra | OK |
| Technika és tervezés | [1–2](technika-es-tervezes/1-2.md) | 5 | 68 | 5 / 68 óra | OK |
| Technika és tervezés | [3–4](technika-es-tervezes/3-4.md) | 5 | 68 | 5 / 68 óra | OK |
| Technika és tervezés | [5–6 (Modul „A”: Épített környezet – tárgyalkotás technológiái)](technika-es-tervezes/5-6-modul-a.md) | 9 | 68 | 9 / 68 óra | OK |
| Technika és tervezés | [5–6 (Modul „B”: Háztartásökonómia – életvitel technológiái)](technika-es-tervezes/5-6-modul-b.md) | 5 | 68 | 5 / 68 óra | OK |
| Technika és tervezés | [5–6 (Modul „C”: Kertészeti technológiák)](technika-es-tervezes/5-6-modul-c.md) | 7 | 48 | 9 / 68 óra | eltérés: táblázat 9 / szöveg 7 |
| Technika és tervezés | [5–6 (Modul „D”: Modellezés – tárgyalkotás technológiái)](technika-es-tervezes/5-6-modul-d.md) | 9 | 68 | 9 / 68 óra | OK |
| Technika és tervezés | [7 (Modul „A”: Épített környezet – tárgyalkotás technológiái)](technika-es-tervezes/7-modul-a.md) | 5 | 34 | 5 / 34 óra | OK |
| Technika és tervezés | [7 (Modul „B”: Háztartásökonómia – életvitel technológiái)](technika-es-tervezes/7-modul-b.md) | 5 | 34 | 5 / 34 óra | OK |
| Technika és tervezés | [7 (Modul „C”: Kertészeti technológiák)](technika-es-tervezes/7-modul-c.md) | 4 | 24 | 5 / 34 óra | eltérés: táblázat 5 / szöveg 4 |
| Technika és tervezés | [7 (Modul „D”: Modellezés – tárgyalkotás technológiái)](technika-es-tervezes/7-modul-d.md) | 6 | 34 | 6 / 34 óra | OK |
| Természettudomány | [5–6](termeszettudomany/5-6.md) | 16 | 136 | 16 / 136 óra | OK |
| Testnevelés | [1–2](testneveles/1-2.md) | 12 | 340 | 11 / 340 óra | eltérés: táblázat 11 / szöveg 12 |
| Testnevelés | [3–4](testneveles/3-4.md) | 12 | 340 | 11 / 340 óra | eltérés: táblázat 11 / szöveg 12 |
| Testnevelés | [5–6](testneveles/5-6.md) | 9 | 340 | 8 / 340 óra | eltérés: táblázat 8 / szöveg 9 |
| Testnevelés | [7–8](testneveles/7-8.md) | 9 | 340 | 8 / 340 óra | eltérés: táblázat 8 / szöveg 9 |
| Történelem | [5–6](tortenelem/5-6.md) | 11 | 119 | 12 / 136 óra | eltérés: táblázat 12 / szöveg 11 |
| Történelem | [7–8](tortenelem/7-8.md) | 14 | 124 | 15 / 136 óra | eltérés: táblázat 15 / szöveg 14 |
| Vizuális kultúra | [1–2](vizualis-kultura/1-2.md) | 7 | 136 | 7 / 136 óra | OK |
| Vizuális kultúra | [3–4](vizualis-kultura/3-4.md) | 6 | 102 | 6 / 102 óra | OK |
| Vizuális kultúra | [5–6](vizualis-kultura/5-6.md) | 7 | 68 | 7 / 68 óra | OK |
| Vizuális kultúra | [7–8](vizualis-kultura/7-8.md) | 7 | 68 | 7 / 68 óra | OK |
| Állampolgári ismeretek | [8](allampolgari-ismeretek/8.md) | 8 | 34 | 8 / 34 óra | OK |
| Élő idegen nyelv (első) | [4 (Angol)](idegen-nyelv-elso/4-angol.md) | 8 | 68 | 8 / 68 óra | OK |
| Élő idegen nyelv (első) | [4 (Német)](idegen-nyelv-elso/4-nemet.md) | 8 | 68 | 8 / 68 óra | OK |
| Élő idegen nyelv (első) | [5–6 (Angol)](idegen-nyelv-elso/5-6-angol.md) | 9 | 204 | 9 / 204 óra | OK |
| Élő idegen nyelv (első) | [5–6 (Német)](idegen-nyelv-elso/5-6-nemet.md) | 9 | 204 | 9 / 204 óra | OK |
| Élő idegen nyelv (első) | [7–8 (Angol)](idegen-nyelv-elso/7-8-angol.md) | 9 | 204 | 9 / 204 óra | OK |
| Élő idegen nyelv (első) | [7–8 (Német)](idegen-nyelv-elso/7-8-nemet.md) | 9 | 204 | 9 / 204 óra | OK |
| Ének-zene | [1–2](enek-zene/1-2.md) | 5 | 136 | 5 / 136 óra | OK |
| Ének-zene | [3–4](enek-zene/3-4.md) | 5 | 136 | 5 / 136 óra | OK |
| Ének-zene | [5–6](enek-zene/5-6.md) | 5 | 0 | – | nincs áttekintő táblázat |
| Ének-zene | [7–8](enek-zene/7-8.md) | 5 | 68 | – | nincs áttekintő táblázat |

## Gimnázium (4 évfolyamos)

| Tantárgy | Sáv | Témakör | Óraszám | Táblázat | Ellenőrzés |
|---|---|---|---|---|---|
| Biológia | [9–10](biologia/9-10.md) | 18 | 170 | 16 / 142 óra | eltérés: táblázat 16 / szöveg 18 (2 táblázat közül a legjobb) |
| Digitális kultúra | [11](digitalis-kultura/11.md) | 8 | 68 | 8 / 68 óra | OK |
| Digitális kultúra | [9–10](digitalis-kultura/9-10.md) | 11 | 102 | 11 / 102 óra | OK |
| Dráma és színház | [12](drama-es-szinhaz/12.md) | 12 | 0 | 12 / 30 óra | óraszám-eltérés: táblázat 30 / szöveg 0 |
| Fizika | [9–10](fizika/9-10.md) | 15 | 170 | 15 / 170 óra | OK |
| Földrajz | [9–10](foldrajz/9-10.md) | 10 | 102 | 10 / 102 óra | OK |
| Kémia | [9–10](kemia/9-10.md) | 7 | 102 | 7 / 102 óra | OK |
| Közösségi nevelés (osztályfőnöki) | [11–12](kozossegi-neveles/11-12.md) | 4 | 68 | 4 / 68 óra | OK |
| Közösségi nevelés (osztályfőnöki) | [9–10](kozossegi-neveles/9-10.md) | 4 | 68 | 4 / 68 óra | OK |
| Latin nyelv | [7–12](latin-nyelv/7-12.md) | – | – | – | nyers szöveg (.doc) |
| Latin nyelv | [9–12](latin-nyelv/9-12.md) | – | – | – | nyers szöveg (.doc) |
| Magyar nyelv és irodalom | [11–12](magyar-nyelv-es-irodalom/11-12.md) | 15 | 140 | 75 / 465 óra | eltérés: táblázat 75 / szöveg 15 |
| Magyar nyelv és irodalom | [9–10](magyar-nyelv-es-irodalom/9-10.md) | 15 | 129 | 62 / 545 óra | eltérés: táblázat 62 / szöveg 15 |
| Matematika | [11–12](matematika/11-12.md) | 11 | 148 | 12 / 186 óra | eltérés: táblázat 12 / szöveg 11 |
| Matematika | [9–10](matematika/9-10.md) | 17 | 204 | 17 / 204 óra | OK |
| Mozgóképkultúra és médiaismeret | [11–12](mozgokepkultura-es-mediaismeret/11-12.md) | – | – | – | nyers szöveg (.doc) |
| Második élő idegen nyelv | [11–12 (Angol)](idegen-nyelv-masodik/11-12-angol.md) | 12 | 186 | 12 / 186 óra | eltérés: táblázat 12 / szöveg 12 |
| Második élő idegen nyelv | [11–12 (Német)](idegen-nyelv-masodik/11-12-nemet.md) | 12 | 186 | 12 / 186 óra | OK |
| Második élő idegen nyelv | [9–10 (Angol)](idegen-nyelv-masodik/9-10-angol.md) | 11 | 204 | 11 / 204 óra | OK |
| Második élő idegen nyelv | [9–10 (Német)](idegen-nyelv-masodik/9-10-nemet.md) | 11 | 204 | 11 / 204 óra | OK |
| Természettudomány | [11 (Biológia)](termeszettudomany/11-biologia.md) | 11 | 68 | 11 / 68 óra | OK |
| Természettudomány | [11 (Fizika)](termeszettudomany/11-fizika.md) | 7 | 68 | 7 / 68 óra | OK |
| Természettudomány | [11 (Földrajz)](termeszettudomany/11-foldrajz.md) | 9 | 68 | 9 / 68 óra | OK |
| Természettudomány | [11 (Kémia)](termeszettudomany/11-kemia.md) | 5 | 68 | 5 / 68 óra | OK |
| Természettudomány | [11 (Természettudomány)](termeszettudomany/11-termeszettudomany.md) | 8 | 68 | 8 / 68 óra | OK |
| Testnevelés | [11–12](testneveles/11-12.md) | 10 | 310 | 9 / 310 óra | eltérés: táblázat 9 / szöveg 10 |
| Testnevelés | [9–10](testneveles/9-10.md) | 10 | 340 | 9 / 340 óra | eltérés: táblázat 9 / szöveg 10 |
| Történelem | [11–12](tortenelem/11-12.md) | 16 | 154 | 18 / 192 óra | eltérés: táblázat 18 / szöveg 16 |
| Történelem | [9–10](tortenelem/9-10.md) | 13 | 121 | 14 / 136 óra | eltérés: táblázat 14 / szöveg 13 |
| Vizuális kultúra | [9–10](vizualis-kultura/9-10.md) | 6 | 68 | 6 / 68 óra | OK |
| Állampolgári ismeretek | [12](allampolgari-ismeretek/12.md) | 9 | 29 | 9 / 28 óra | óraszám-eltérés: táblázat 28 / szöveg 29 |
| Élő idegen nyelv (első) | [11–12 (Angol)](idegen-nyelv-elso/11-12-angol.md) | 14 | 272 | 14 / 248 óra | óraszám-eltérés: táblázat 248 / szöveg 272 |
| Élő idegen nyelv (első) | [11–12 (Német)](idegen-nyelv-elso/11-12-nemet.md) | 14 | 272 | 14 / 248 óra | óraszám-eltérés: táblázat 248 / szöveg 272 |
| Élő idegen nyelv (első) | [9–10 (Angol)](idegen-nyelv-elso/9-10-angol.md) | 11 | 204 | 11 / 204 óra | OK |
| Élő idegen nyelv (első) | [9–10 (Német)](idegen-nyelv-elso/9-10-nemet.md) | 11 | 204 | 11 / 204 óra | OK |
| Ének-zene | [9–10](enek-zene/9-10.md) | 3 | 68 | – | nincs áttekintő táblázat |

## Gimnázium (6 évfolyamos)

| Tantárgy | Sáv | Témakör | Óraszám | Táblázat | Ellenőrzés |
|---|---|---|---|---|---|
| Biológia | [7–8](biologia/7-8-hatosztalyos.md) | 11 | 102 | 11 / 102 óra | OK (2 táblázat közül a legjobb) |
| Biológia | [9–10](biologia/9-10-hatosztalyos.md) | 20 | 170 | – | nincs áttekintő táblázat |
| Fizika | [7–8](fizika/7-8-hatosztalyos.md) | 10 | 102 | 10 / 102 óra | OK |
| Fizika | [9–10](fizika/9-10-hatosztalyos.md) | 15 | 170 | 15 / 158 óra | óraszám-eltérés: táblázat 158 / szöveg 170 |
| Kémia | [7–8](kemia/7-8-hatosztalyos.md) | 7 | 102 | 7 / 102 óra | eltérés: táblázat 7 / szöveg 7 |
| Kémia | [9–10](kemia/9-10-hatosztalyos.md) | 8 | 102 | 8 / 102 óra | OK |
| Magyar nyelv és irodalom | [11–12](magyar-nyelv-es-irodalom/11-12-hatosztalyos.md) | 18 | 161 | 73 / 425 óra | eltérés: táblázat 73 / szöveg 18 |
| Magyar nyelv és irodalom | [7–8](magyar-nyelv-es-irodalom/7-8-hatosztalyos.md) | 16 | 116 | 28 / 179 óra | eltérés: táblázat 28 / szöveg 16 |
| Magyar nyelv és irodalom | [9–10](magyar-nyelv-es-irodalom/9-10-hatosztalyos.md) | 13 | 115 | 9 / 68 óra | eltérés: táblázat 9 / szöveg 13 |
| Matematika | [11–12](matematika/11-12-hatosztalyos.md) | 11 | 150 | 12 / 186 óra | eltérés: táblázat 12 / szöveg 11 |
| Matematika | [7–8](matematika/7-8-hatosztalyos.md) | 12 | 204 | 12 / 204 óra | OK |
| Matematika | [9–10](matematika/9-10-hatosztalyos.md) | 17 | 204 | 17 / 204 óra | OK |
| Speciális matematika tagozat | [11–12](matematika-specialis/11-12-hatosztalyos.md) | 11 | 316 | 12 / 372 óra | eltérés: táblázat 12 / szöveg 11 |
| Speciális matematika tagozat | [7–8](matematika-specialis/7-8-hatosztalyos.md) | 12 | 408 | 12 / 408 óra | OK |
| Speciális matematika tagozat | [9–10](matematika-specialis/9-10-hatosztalyos.md) | 17 | 408 | 17 / 408 óra | OK |
| Történelem | [11–12](tortenelem/11-12-hatosztalyos.md) | 15 | 146 | 17 / 186 óra | eltérés: táblázat 17 / szöveg 15 |
| Történelem | [7–8](tortenelem/7-8-hatosztalyos.md) | 12 | 126 | 13 / 136 óra | eltérés: táblázat 13 / szöveg 12 |
| Történelem | [9–10](tortenelem/9-10-hatosztalyos.md) | 12 | 119 | 13 / 136 óra | eltérés: táblázat 13 / szöveg 12 |
