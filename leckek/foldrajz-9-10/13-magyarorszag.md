# Hol nő és hol fogy Magyarország? – területi különbségek a 21. században
tantárgy: Földrajz · évfolyam: 9–10. · témakör: 8. Magyarország és Kárpát-medence a 21. században

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/foldrajz-9-10/13-magyarorszag.md
  A megyei adatok (19 megye és Budapest) a „Közös” rész Adatok pontja alatt vannak, mutatónként és
  megyénként egy-egy sorban; a térképek, a rangsor, a hasábok, a mérleg és a szórásdiagram ezekből
  rajzolódik. Ha egy számot átírsz, a lecke ellenőrzi, hogy a panelen kimondott összesítő számok
  (pl. Budapest népességaránya) még egyeznek-e vele (eltérésnél a QA hibát jelez).
  Megyehatárok: Natural Earth 1:10m (közkincs, „Made with Natural Earth”), shared/foldrajz/megyek.js;
  háttértérkép: shared/tort/map-karpat.js (Natural Earth, közkincs). A „megye” szót a kerettanterv
  írásmódja szerint használjuk; 2023 óta a hivatalos neve „vármegye” (a KSH is így közli).
-->

## Közös

### Feliratok
- vázlatos: vázlatos
- ország: Magyarország
- átlag: országos átlag = 100
- kártya GDP: GDP/fő (átlag = 100)
- kártya népesség: népesség
- kártya sűrűség: népsűrűség
- kártya változás: változás 2012 óta
- kártya öregedés: öregedési index
- kártya székhely: székhely: #
- kártya főváros: főváros
- érték fő: # fő
- érték sűrűség: # fő/km²
- érték százalék: # %
- kattints: Kattints egy megyére!
<!-- a megyék neve (m: teljes, r: rövid – a térképen és a rangsorban) -->
- m Budapest: Budapest
- r Budapest: Budapest
- m Pest: Pest
- r Pest: Pest
- m Fejér: Fejér
- r Fejér: Fejér
- m Komárom-Esztergom: Komárom-Esztergom
- r Komárom-Esztergom: Komárom-E.
- m Veszprém: Veszprém
- r Veszprém: Veszprém
- m Győr-Moson-Sopron: Győr-Moson-Sopron
- r Győr-Moson-Sopron: Győr-M.-S.
- m Vas: Vas
- r Vas: Vas
- m Zala: Zala
- r Zala: Zala
- m Baranya: Baranya
- r Baranya: Baranya
- m Somogy: Somogy
- r Somogy: Somogy
- m Tolna: Tolna
- r Tolna: Tolna
- m Borsod-Abaúj-Zemplén: Borsod-Abaúj-Zemplén
- r Borsod-Abaúj-Zemplén: Borsod-A.-Z.
- m Heves: Heves
- r Heves: Heves
- m Nógrád: Nógrád
- r Nógrád: Nógrád
- m Hajdú-Bihar: Hajdú-Bihar
- r Hajdú-Bihar: Hajdú-Bihar
- m Jász-Nagykun-Szolnok: Jász-Nagykun-Szolnok
- r Jász-Nagykun-Szolnok: Jász-N.-Sz.
- m Szabolcs-Szatmár-Bereg: Szabolcs-Szatmár-Bereg
- r Szabolcs-Szatmár-Bereg: Szabolcs-Sz.-B.
- m Bács-Kiskun: Bács-Kiskun
- r Bács-Kiskun: Bács-Kiskun
- m Békés: Békés
- r Békés: Békés
- m Csongrád-Csanád: Csongrád-Csanád
- r Csongrád-Csanád: Csongrád-Cs.

### Adatok
<!-- forrás (az alábbiakra): a megyei táblák évei (KSH STADAT, lekérdezve: 2026-11-24); megyehatárok: Natural Earth 1:10m, shared/foldrajz/megyek.js, közkincs -->
- megyehatárok: Natural Earth
- népesség első éve: 2012
- népesség utolsó éve: 2026
- GDP éve: 2024
- népmozgalom első éve: 2012
- népmozgalom utolsó éve: 2025
- öregedési évek: 2001; 2012; 2026
<!-- forrás (az alábbiakra): KSH STADAT 22.1.2.1. (nep0034), a „Ország összesen” sor, január 1., lekérdezve: 2026-11-24 -->
- Magyarország népessége 2012: 9 931 925 fő (2012)
- Magyarország népessége 2026: 9 488 428 fő (2026, frissítendő)
- Magyarország területe: 93 025 km²
<!-- forrás: KSH STADAT 8.1.2.1. (fol0006), lekérdezve: 2026-11-24 -->
<!-- forrás (az alábbiakra): KSH STADAT 22.1.2.1. „A lakónépesség nem, vármegye és régió szerint, január 1.” (ksh.hu/stadat_files/nep/hu/nep0034.html), lekérdezve: 2026-11-24. 2012–2022: a 2022-es népszámlálásból visszaszámított, 2023-tól továbbszámított adat. Sorrend: 2012. január 1. … 2026. január 1. (15 érték) -->
- népesség · Budapest: 1 727 495; 1 730 350; 1 733 837; 1 741 601; 1 738 570; 1 728 929; 1 723 033; 1 722 363; 1 717 144; 1 690 503; 1 672 443; 1 671 004; 1 686 222; 1 685 209; 1 675 777 fő (2026, frissítendő)
- népesség · Pest: 1 213 323; 1 216 562; 1 217 628; 1 221 637; 1 228 755; 1 240 780; 1 254 436; 1 270 416; 1 287 734; 1 300 389; 1 315 964; 1 328 790; 1 333 257; 1 336 134; 1 338 870 fő (2026, frissítendő)
- népesség · Fejér: 421 927; 421 073; 419 416; 417 571; 418 365; 416 062; 416 567; 417 568; 418 418; 418 634; 418 542; 419 565; 419 490; 418 562; 416 993 fő (2026, frissítendő)
- népesség · Komárom-Esztergom: 303 864; 302 839; 301 450; 300 331; 299 591; 299 204; 299 445; 301 371; 303 341; 302 138; 300 869; 301 492; 301 834; 299 262; 297 853 fő (2026, frissítendő)
- népesség · Veszprém: 353 798; 351 115; 348 934; 346 619; 344 350; 342 550; 341 437; 341 367; 341 223; 341 207; 339 498; 338 342; 335 979; 333 345; 330 401 fő (2026, frissítendő)
- népesség · Győr-Moson-Sopron: 444 935; 446 692; 447 111; 447 743; 448 633; 449 751; 452 770; 457 331; 462 254; 467 419; 468 465; 471 309; 473 246; 471 648; 470 174 fő (2026, frissítendő)
- népesség · Vas: 256 215; 254 583; 253 121; 251 762; 250 783; 249 811; 249 590; 249 429; 249 572; 248 920; 248 909; 249 812; 248 199; 245 598; 243 728 fő (2026, frissítendő)
- népesség · Zala: 283 249; 281 379; 278 914; 276 249; 273 750; 271 348; 269 037; 266 827; 265 260; 263 120; 262 370; 261 803; 260 124; 257 371; 255 696 fő (2026, frissítendő)
- népesség · Baranya: 380 904; 377 565; 374 805; 372 465; 370 021; 367 848; 366 033; 363 203; 361 766; 359 529; 357 066; 355 315; 353 331; 351 158; 348 781 fő (2026, frissítendő)
- népesség · Somogy: 318 778; 317 703; 314 691; 310 937; 307 590; 304 892; 301 799; 299 253; 297 492; 298 505; 296 422; 295 316; 292 691; 290 245; 286 675 fő (2026, frissítendő)
- népesség · Tolna: 231 533; 229 632; 227 360; 224 998; 222 431; 220 523; 217 968; 215 946; 213 839; 211 692; 209 569; 208 044; 206 398; 204 567; 202 161 fő (2026, frissítendő)
- népesség · Borsod-Abaúj-Zemplén: 688 922; 682 753; 675 767; 668 706; 662 223; 656 394; 650 520; 644 955; 639 793; 635 644; 629 621; 624 219; 617 800; 610 927; 604 493 fő (2026, frissítendő)
- népesség · Heves: 309 175; 306 031; 302 963; 300 485; 298 213; 295 829; 294 477; 293 185; 291 827; 290 396; 288 430; 287 533; 285 058; 282 490; 280 211 fő (2026, frissítendő)
- népesség · Nógrád: 202 734; 200 310; 197 533; 194 627; 192 232; 190 669; 188 851; 187 045; 185 635; 185 153; 183 318; 182 038; 180 469; 178 815; 176 903 fő (2026, frissítendő)
- népesség · Hajdú-Bihar: 543 452; 540 881; 538 607; 535 929; 533 324; 530 531; 528 397; 525 661; 524 151; 523 648; 521 802; 520 656; 520 550; 520 129; 519 652 fő (2026, frissítendő)
- népesség · Jász-Nagykun-Szolnok: 390 026; 386 359; 382 898; 378 984; 375 242; 372 454; 369 996; 368 531; 365 252; 362 084; 358 883; 356 388; 353 511; 349 726; 346 466 fő (2026, frissítendő)
- népesség · Szabolcs-Szatmár-Bereg: 565 317; 562 220; 558 502; 558 310; 557 823; 556 145; 551 798; 545 799; 541 289; 537 757; 531 855; 527 968; 524 513; 520 551; 516 799 fő (2026, frissítendő)
- népesség · Bács-Kiskun: 521 852; 519 514; 516 084; 512 470; 509 935; 506 266; 503 788; 501 836; 500 040; 497 956; 495 675; 494 563; 491 632; 488 547; 485 336 fő (2026, frissítendő)
- népesség · Békés: 362 662; 358 267; 353 448; 348 577; 343 771; 338 809; 333 967; 329 742; 325 590; 321 661; 318 081; 314 380; 310 912; 307 112; 303 119 fő (2026, frissítendő)
- népesség · Csongrád-Csanád: 411 764; 409 422; 407 148; 405 857; 404 050; 401 062; 399 746; 398 444; 397 756; 395 106; 392 621; 391 207; 389 411; 388 106; 388 340 fő (2026, frissítendő)
<!-- forrás (az alábbiakra): KSH STADAT 8.1.2.1. „Terület, településsűrűség, népsűrűség, 2026. január 1.” (ksh.hu/stadat_files/fol/hu/fol0006.html), lekérdezve: 2026-11-24 -->
- terület · Budapest: 525 km²
- terület · Pest: 6392 km²
- terület · Fejér: 4359 km²
- terület · Komárom-Esztergom: 2264 km²
- terület · Veszprém: 4463 km²
- terület · Győr-Moson-Sopron: 4208 km²
- terület · Vas: 3336 km²
- terület · Zala: 3784 km²
- terület · Baranya: 4430 km²
- terület · Somogy: 6065 km²
- terület · Tolna: 3703 km²
- terület · Borsod-Abaúj-Zemplén: 7247 km²
- terület · Heves: 3637 km²
- terület · Nógrád: 2544 km²
- terület · Hajdú-Bihar: 6210 km²
- terület · Jász-Nagykun-Szolnok: 5582 km²
- terület · Szabolcs-Szatmár-Bereg: 5936 km²
- terület · Bács-Kiskun: 8445 km²
- terület · Békés: 5630 km²
- terület · Csongrád-Csanád: 4265 km²
<!-- forrás (az alábbiakra): KSH STADAT 21.1.2.2. „Egy főre jutó bruttó hazai termék vármegye és régió szerint” – az országos átlag százalékában (ksh.hu/stadat_files/gdp/hu/gdp0078.html), lekérdezve: 2026-11-24. A megyei GDP becslés, a KSH utólag módosíthatja. -->
- GDP/fő · Budapest: 220,8 % (2024, frissítendő)
- GDP/fő · Pest: 84,1 % (2024, frissítendő)
- GDP/fő · Fejér: 87,7 % (2024, frissítendő)
- GDP/fő · Komárom-Esztergom: 95,5 % (2024, frissítendő)
- GDP/fő · Veszprém: 75,9 % (2024, frissítendő)
- GDP/fő · Győr-Moson-Sopron: 101,1 % (2024, frissítendő)
- GDP/fő · Vas: 79,7 % (2024, frissítendő)
- GDP/fő · Zala: 67,8 % (2024, frissítendő)
- GDP/fő · Baranya: 67,1 % (2024, frissítendő)
- GDP/fő · Somogy: 60,0 % (2024, frissítendő)
- GDP/fő · Tolna: 71,5 % (2024, frissítendő)
- GDP/fő · Borsod-Abaúj-Zemplén: 62,7 % (2024, frissítendő)
- GDP/fő · Heves: 71,0 % (2024, frissítendő)
- GDP/fő · Nógrád: 45,7 % (2024, frissítendő)
- GDP/fő · Hajdú-Bihar: 74,4 % (2024, frissítendő)
- GDP/fő · Jász-Nagykun-Szolnok: 63,6 % (2024, frissítendő)
- GDP/fő · Szabolcs-Szatmár-Bereg: 57,9 % (2024, frissítendő)
- GDP/fő · Bács-Kiskun: 73,4 % (2024, frissítendő)
- GDP/fő · Békés: 57,2 % (2024, frissítendő)
- GDP/fő · Csongrád-Csanád: 72,5 % (2024, frissítendő)
<!-- forrás (az alábbiakra): KSH STADAT 22.1.2.5. „Eltartottsági ráták, öregedési index vármegye és régió szerint, január 1.” (ksh.hu/stadat_files/nep/hu/nep0038.html), lekérdezve: 2026-11-24. Sorrend: 2001; 2012; 2026 (január 1.). Öregedési index = a 65 éves és idősebbek száma 100 fő 0–14 évesre. -->
- öregedési index · Budapest: 138,3; 149,1; 172,9 (2026, frissítendő)
- öregedési index · Pest: 74,1; 89,0; 111,5 (2026, frissítendő)
- öregedési index · Fejér: 77,7; 110,0; 142,4 (2026, frissítendő)
- öregedési index · Komárom-Esztergom: 80,7; 112,0; 141,5 (2026, frissítendő)
- öregedési index · Veszprém: 86,0; 124,3; 171,0 (2026, frissítendő)
- öregedési index · Győr-Moson-Sopron: 91,2; 112,6; 134,3 (2026, frissítendő)
- öregedési index · Vas: 94,4; 129,4; 167,3 (2026, frissítendő)
- öregedési index · Zala: 102,1; 141,2; 211,2 (2026, frissítendő)
- öregedési index · Baranya: 92,2; 124,2; 180,5 (2026, frissítendő)
- öregedési index · Somogy: 91,6; 125,0; 184,9 (2026, frissítendő)
- öregedési index · Tolna: 90,4; 125,3; 170,3 (2026, frissítendő)
- öregedési index · Borsod-Abaúj-Zemplén: 76,0; 101,0; 124,4 (2026, frissítendő)
- öregedési index · Heves: 100,8; 125,0; 155,0 (2026, frissítendő)
- öregedési index · Nógrád: 94,7; 126,0; 156,1 (2026, frissítendő)
- öregedési index · Hajdú-Bihar: 73,4; 99,6; 132,6 (2026, frissítendő)
- öregedési index · Jász-Nagykun-Szolnok: 88,1; 118,5; 147,2 (2026, frissítendő)
- öregedési index · Szabolcs-Szatmár-Bereg: 63,1; 79,9; 115,6 (2026, frissítendő)
- öregedési index · Bács-Kiskun: 90,3; 121,5; 153,2 (2026, frissítendő)
- öregedési index · Békés: 100,3; 136,6; 185,3 (2026, frissítendő)
- öregedési index · Csongrád-Csanád: 96,8; 130,5; 170,4 (2026, frissítendő)
<!-- forrás (az alábbiakra): KSH STADAT 22.1.2.7. „A népmozgalmi események vármegye és régió szerint” (ksh.hu/stadat_files/nep/hu/nep0040.html), lekérdezve: 2026-11-24; a 2012–2025 közötti évek összege (saját számítás). Sorrend: természetes szaporodás/fogyás; belföldi vándorlási különbözet; nemzetközi vándorlási különbözet. A három összege pontosan a népesség változása 2012. január 1. és 2026. január 1. között (a lecke ellenőrzi). -->
- népmozgalom · Budapest: −93 349; −8513; 50 144 fő (2025, frissítendő)
- népmozgalom · Pest: −38 998; 153 172; 11 373 fő (2025, frissítendő)
- népmozgalom · Fejér: −25 431; 13 694; 6803 fő (2025, frissítendő)
- népmozgalom · Komárom-Esztergom: −21 140; 3811; 11 318 fő (2025, frissítendő)
- népmozgalom · Veszprém: −26 444; 3499; −452 fő (2025, frissítendő)
- népmozgalom · Győr-Moson-Sopron: −20 270; 40 332; 5177 fő (2025, frissítendő)
- népmozgalom · Vas: −21 109; 8535; 87 fő (2025, frissítendő)
- népmozgalom · Zala: −27 975; −1366; 1788 fő (2025, frissítendő)
- népmozgalom · Baranya: −31 792; −8467; 8136 fő (2025, frissítendő)
- népmozgalom · Somogy: −29 892; −5014; 2803 fő (2025, frissítendő)
- népmozgalom · Tolna: −19 200; −10 192; 20 fő (2025, frissítendő)
- népmozgalom · Borsod-Abaúj-Zemplén: −38 789; −53 893; 8253 fő (2025, frissítendő)
- népmozgalom · Heves: −25 192; −5543; 1771 fő (2025, frissítendő)
- népmozgalom · Nógrád: −18 912; −6227; −692 fő (2025, frissítendő)
- népmozgalom · Hajdú-Bihar: −19 641; −24 614; 20 455 fő (2025, frissítendő)
- népmozgalom · Jász-Nagykun-Szolnok: −31 241; −13 850; 1531 fő (2025, frissítendő)
- népmozgalom · Szabolcs-Szatmár-Bereg: −16 273; −54 794; 22 549 fő (2025, frissítendő)
- népmozgalom · Bács-Kiskun: −37 550; −6591; 7625 fő (2025, frissítendő)
- népmozgalom · Békés: −40 484; −18 921; −138 fő (2025, frissítendő)
- népmozgalom · Csongrád-Csanád: −30 719; −5058; 12 353 fő (2025, frissítendő)
<!-- forrás (az alábbiakra): a megyeszékhelyek központjának közismert koordinátái, két tizedesre kerekítve (a pontosságuk térképen ellenőrizendő; a lecke ellenőrzi, hogy a pont a saját megyéje sokszögébe esik). Pest vármegye székhelye Budapest. -->
- Budapest helye: 47,50° É, 19,04° K
- székhely · Fejér: 47,19° É, 18,42° K
- székhely · Komárom-Esztergom: 47,57° É, 18,40° K
- székhely · Veszprém: 47,09° É, 17,91° K
- székhely · Győr-Moson-Sopron: 47,69° É, 17,65° K
- székhely · Vas: 47,23° É, 16,62° K
- székhely · Zala: 46,84° É, 16,84° K
- székhely · Baranya: 46,07° É, 18,23° K
- székhely · Somogy: 46,36° É, 17,80° K
- székhely · Tolna: 46,35° É, 18,71° K
- székhely · Borsod-Abaúj-Zemplén: 48,10° É, 20,78° K
- székhely · Heves: 47,90° É, 20,38° K
- székhely · Nógrád: 48,09° É, 19,80° K
- székhely · Hajdú-Bihar: 47,53° É, 21,63° K
- székhely · Jász-Nagykun-Szolnok: 47,16° É, 20,18° K
- székhely · Szabolcs-Szatmár-Bereg: 47,96° É, 21,72° K
- székhely · Bács-Kiskun: 46,90° É, 19,69° K
- székhely · Békés: 46,67° É, 21,09° K
- székhely · Csongrád-Csanád: 46,25° É, 20,14° K

## 1. Egy ország, sok sebesség
Az **egy főre jutó GDP** Budapesten az országos átlag {GDP/fő · Budapest}-a, Nógrádban {GDP/fő · Nógrád}-a. Ez **területi fejlettségi különbség**. **Tévhit:** a határ egyetlen kelet–nyugati vonal. ==A legnagyobb a szakadék a főváros és a vidék között:== Budapest felhúzza az átlagot, fölötte csak Győr-Moson-Sopron van még.

> megjegyzés: Kattints egy megyére! A GDP az ott megtermelt érték, nem a lakók jövedelme.

### Feliratok
- cím 1: Egy főre jutó GDP megyénként, #
- leg 1: az országos átlag %-ában
- rangsor: rangsor (átlag = 100)
- forrás 1: Forrás: KSH, egy főre jutó GDP vármegyénként, # · Natural Earth

### Adatok
- GDP osztályközök: 55; 65; 75; 90; 110; 150 %
<!-- forrás: a lecke saját osztályközei (az átlag körül 90–110 % semleges), a tanár átírhatja -->
- átlag fölötti megyék: 2
<!-- forrás: saját számítás a fenti GDP/fő-adatokból (az országos átlagnál nagyobb értékű területi egységek száma) -->

## 2. Hol élnek az emberek?
A **népsűrűség** az egy km²-re jutó lakók száma: az országos átlag {országos népsűrűség}, Budapesten {Budapest népsűrűsége}. A hasáb alapja a terület, magassága a népsűrűség, ==így a térfogata éppen a népesség==. Budapest az ország területének csak {Budapest területaránya}-a, mégis itt él a lakók {Budapest népességaránya}-a.

> megjegyzés: Kapcsolj a térkép és a hasábok között!

### Feliratok
- cím 2: Hol élnek az emberek? #
- gomb térkép: Térkép
- gomb hasábok: Hasábok
- hasáb jel: alap = terület · magasság = népsűrűség · térfogat = népesség
- leg 2: népsűrűség, fő/km²
- Bp terület: a terület #-a
- Bp népesség: a népesség #-a
- forrás 2: Forrás: KSH, lakónépesség és terület vármegyénként, # · Natural Earth

### Adatok
- népsűrűség osztályközök: 55; 70; 85; 100; 150; 1000 fő/km²
<!-- forrás: a lecke saját osztályközei, a tanár átírhatja -->
<!-- forrás (az alábbiakra): KSH STADAT 8.1.2.1. (fol0006): Budapest 3191,35, ország 102,00 fő/km² (2026. január 1.); az arányok saját számítás a fenti megyei adatokból, lekérdezve: 2026-11-24 -->
- országos népsűrűség: 102 fő/km² (2026, frissítendő)
- Budapest népsűrűsége: 3191 fő/km² (2026, frissítendő)
- Budapest területaránya: 0,6 %
- Budapest népességaránya: 17,7 % (2026, frissítendő)

## 3. Minden út Budapestre vezet?
Budapest adja az ország GDP-jének {Budapest GDP-aránya}-át. A fő autópályák sugarasan futnak ki belőle, mellettük **ipari parkok** és **logisztikai központok** települtek. A főváros körül {agglomeráció települései} településből álló **agglomeráció** nőtt, innen sokan ingáznak Budapestre. ==A budapesti agglomerációban él az ország lakóinak {agglomeráció népességaránya}-a.==

> megjegyzés: Kapcsold a rétegeket! Az autópálya-hálózat vázlatos.

### Feliratok
- cím 3: Minden út Budapestre vezet?
- gomb autópályák: Autópályák
- gomb agglomeráció: Agglomeráció
- autópályák: fő autópályák (vázlatos)
- agglomeráció: budapesti agglomeráció
- Budapest: Budapest
- Bécs: Bécs
- sáv cím: Budapest részesedése az országból
- sáv terület: terület
- sáv népesség: népesség
- sáv agglo: népesség az agglomerációval
- sáv GDP: GDP
- M1: M1
- M3: M3
- M5: M5
- M6: M6
- M7: M7
- M0: M0
- M30: M30
- M35: M35
- M43: M43
- forrás 3: Forrás: KSH (GDP 2024, népesség 2026, agglomeráció 2026) · autópályák: vázlatos

### Adatok
- Budapest GDP-aránya: 38,9 % (2024, frissítendő)
<!-- forrás: KSH STADAT 21.1.2.1. „A bruttó hazai termék (GDP) vármegye és régió szerint” (gdp0077), 2024: Budapest 31 703 324 / ország 81 447 664 millió Ft, lekérdezve: 2026-11-24 -->
<!-- forrás (az alábbiakra): KSH STADAT 8.1.2.11. „Agglomerációkban, agglomerálódó térségekben, településegyüttesekben élők száma, 2026. január 1.” (fol0016; a lehatárolás a 2022-es népszámlálás alapján), lekérdezve: 2026-11-24; az arány saját számítás (2 589 311 / 9 488 428) -->
- agglomeráció települései: 81
- agglomeráció népessége: 2 589 311 fő (2026, frissítendő)
- agglomeráció népességaránya: 27,3 % (2026, frissítendő)
- Bécs helye: 48,21° É, 16,37° K
<!-- forrás: Bécs belvárosának közismert koordinátája, két tizedesre kerekítve -->

## 4. Hol nő és hol fogy a népesség?
Az ország népességének változása {népesség első éve} és {népesség utolsó éve} között: {országos népességváltozás}. **Tévhit:** mindenhol fogy a népesség. ==Pest megye {Pest népességváltozása}-kal nőtt==, és Győr-Moson-Sopron is gyarapodott. A legnagyobb a fogyás Békésben: {Békés népességváltozása}. A népesség a főváros körül és északnyugaton gyűlik össze.

> megjegyzés: Húzd a csúszkát, vagy játszd le!

### Feliratok
- cím 4: Népességváltozás, 2012 → #
- csúszka év: Év (január 1.)
- gomb lejátszás: Lejátszás
- leg 4: változás 2012. január 1. óta
- ország változás: Magyarország: #
- forrás 4: Forrás: KSH, lakónépesség vármegyénként, január 1., 2012–#

### Adatok
- változás osztályközök: −12; −8; −4; 0; 4; 8; 12 %
<!-- forrás: a lecke saját osztályközei (0 körül szimmetrikus), a tanár átírhatja -->
<!-- forrás (az alábbiakra): saját számítás a fenti megyei népességsorokból (2012. január 1. → 2026. január 1.) -->
- országos népességváltozás: −4,5 % (2026)
- Pest népességváltozása: +10,3 % (2026)
- Békés népességváltozása: −16,4 % (2026)

## 5. Születés, halálozás, költözés
A népesség változása: **természetes szaporodás** vagy fogyás (születések − halálozások), plusz a vándorlás. ==2012 óta minden megyében több a halálozás, mint a születés.== Pest megye a beköltözőkből nő: belföldi vándorlási többlete {Pest belföldi vándorlása}.

> megjegyzés: Kattints egy megyére!

### Feliratok
- cím 5: Mi változtatja a népességet? 2012–#
- gomb természetes: Születés − halálozás
- gomb belföldi: Belföldi vándorlás
- gomb nemzetközi: Nemzetközi vándorlás
- gomb összesen: Összesen
- leg 5: 2012–#, a 2012-es népesség %-ában
- mérleg cím: # népességmérlege
- mérleg alcím: 2012. január 1. → #. január 1., ezer fő
- m természetes: születés − halálozás
- m belföldi: belföldi vándorlás
- m nemzetközi: nemzetközi vándorlás
- m összesen: változás összesen
- forrás 5: Forrás: KSH, népmozgalom vármegyénként, 2012–#

### Adatok
- mozgás osztályközök: −9; −6; −3; 0; 3; 6; 9 %
<!-- forrás: a lecke saját osztályközei (0 körül szimmetrikus), a tanár átírhatja -->
- Pest belföldi vándorlása: 153 172 fő (2025, frissítendő)
<!-- forrás: a fenti „népmozgalom · Pest” sor második eleme (KSH, 2012–2025 összesen) -->

## 6. Öregedő megyék
Az **öregedési index** megmutatja, hány 65 éves és idősebb lakó jut 100 gyerekre (0–14 évesre). 100 fölött több az idős, mint a gyerek. 2001-ben még {gyerekesebb megyék 2001} megyében több volt a gyerek, ==ma már egyben sem==. A **korszerkezet** öregszik: kevesebb gyerek születik, és tovább élünk.

> megjegyzés: Válts évet! Hol legfiatalabb a népesség?

### Feliratok
- cím 6: Öregedési index, #. január 1.
- leg 6: 65 évesek és idősebbek 100 gyerekre (0–14 év)
- több gyerek: ← több a gyerek
- több idős: több az idős →
- számláló: # megyében több a gyerek, mint az idős
- forrás 6: Forrás: KSH, eltartottsági ráták, öregedési index vármegyénként, #

### Adatok
- öregedési osztályközök: 80; 100; 130; 160; 190
<!-- forrás: a lecke saját osztályközei (a 100 a határ: ennél több idős jut 100 gyerekre), a tanár átírhatja -->
- gyerekesebb megyék 2001: 16
<!-- forrás: saját számítás a fenti öregedési indexekből (2001-ben 100 alatti megyék és Budapest száma) -->

## 7. Fejlettebb, ami közelebb van Bécshez?
Minden pont egy megye (Budapest nélkül). ==Minél közelebb van a székhely Bécshez, annál nagyobb általában az egy főre jutó GDP.== Nyugaton közel van a nagy európai piac, és ide települt sok külföldi gyár. Ez összefüggés, nem törvény: Nógrád közel van Budapesthez, mégis itt a legkisebb az egy főre jutó GDP.

> megjegyzés: Mérj Budapesttől is!

### Feliratok
- cím 7: Fejlettebb, ami közelebb van Bécshez?
- gomb Bécs: Bécstől
- gomb Budapest: Budapesttől
- x 7 Bécs: a megyeszékhely távolsága Bécstől (km, légvonalban)
- x 7 Budapest: a megyeszékhely távolsága Budapesttől (km, légvonalban)
- y 7: egy főre jutó GDP, átlag = 100
- trend: illesztett egyenes
- Bp kilóg: Budapest: # – a skála fölött
- forrás 7: Forrás: KSH, egy főre jutó GDP vármegyénként, # · távolság: saját számítás

## 8. Magyarország az EU-ban
Magyarország {EU-csatlakozás} óta az Európai Unió tagja. Az egy főre jutó GDP vásárlóerőn az uniós átlag {EU · Magyarország}-a. A **régiók** között itt is nagy a különbség: Budapest {EU · Budapest}, Észak-Magyarország {EU · Észak-Magyarország}. Az EU **kohéziós politikája** ==a {kohéziós határ} alatti régióknak adja a legtöbb támogatást==.

> megjegyzés: Az EU-támogatás nem ajándék: a tagállam be is fizet. Nézd meg a többi fővárost!

### Feliratok
- cím 8: Egy főre jutó GDP vásárlóerőn, #
- gomb régiók: Magyar régiók
- gomb fővárosok: Fővárosok
- EU = 100: EU-átlag = 100
- határ 75: kohéziós határ: #
- jel ország: ország
- jel főváros: fővárosi régió
- e Magyarország: Magyarország
- e Budapest: Budapest
- e Pest: Pest
- e Közép-Dunántúl: Közép-Dunántúl
- e Nyugat-Dunántúl: Nyugat-Dunántúl
- e Dél-Dunántúl: Dél-Dunántúl
- e Észak-Magyarország: Észak-Magyarország
- e Észak-Alföld: Észak-Alföld
- e Dél-Alföld: Dél-Alföld
- e Ausztria: Ausztria
- e Bécs: Bécs
- e Csehország: Csehország
- e Prága: Prága
- e Lengyelország: Lengyelország
- e Varsó: Varsó és környéke
- e Szlovákia: Szlovákia
- e Pozsony: Pozsonyi kerület
- e Románia: Románia
- e Bukarest: Bukarest és Ilfov
- forrás 8: Forrás: Eurostat, nama_10r_2gdp (GDP/fő vásárlóerő-egységben, EU-27 = 100), #

### Adatok
<!-- forrás (az alábbiakra): Eurostat, „Gross domestic product (GDP) at current market prices by NUTS 2 region” (nama_10r_2gdp, egység: PPS_HAB_EU27_2020 – egy főre jutó GDP vásárlóerő-egységben, az EU-27 átlagának %-ában), frissítve: 2026-02-10, lekérdezve: 2026-11-24, CC BY 4.0 (Eurostat). A NUTS 2-régiók 2018 óta: Budapest és Pest külön régió. -->
- EU-adat éve: 2024
- EU · Magyarország: 76 % (2024, frissítendő)
- EU · Budapest: 168 % (2024, frissítendő)
- EU · Pest: 64 % (2024, frissítendő)
- EU · Közép-Dunántúl: 66 % (2024, frissítendő)
- EU · Nyugat-Dunántúl: 66 % (2024, frissítendő)
- EU · Dél-Dunántúl: 50 % (2024, frissítendő)
- EU · Észak-Magyarország: 47 % (2024, frissítendő)
- EU · Észak-Alföld: 50 % (2024, frissítendő)
- EU · Dél-Alföld: 52 % (2024, frissítendő)
- EU · Ausztria: 119 % (2024, frissítendő)
- EU · Bécs: 137 % (2024, frissítendő)
- EU · Csehország: 91 % (2024, frissítendő)
- EU · Prága: 192 % (2024, frissítendő)
- EU · Lengyelország: 78 % (2024, frissítendő)
- EU · Varsó: 157 % (2024, frissítendő)
- EU · Szlovákia: 75 % (2024, frissítendő)
- EU · Pozsony: 153 % (2024, frissítendő)
- EU · Románia: 77 % (2024, frissítendő)
- EU · Bukarest: 188 % (2024, frissítendő)
- kohéziós határ: 75 %
<!-- forrás: Az Európai Parlament és a Tanács (EU) 2021/1060 rendelete, 108. cikk: „kevésbé fejlett régiók” – az egy főre jutó GDP (vásárlóerőn) az uniós átlag 75 %-a alatt; a 2021–2027-es besorolás a 2015–2017-es átlagból készült, nem a 2024-es adatból -->
- EU-csatlakozás: 2004. május 1.
<!-- forrás: Magyarország az Európai Unió tagja 2004. május 1. óta (csatlakozási szerződés, Athén, 2003) -->

## 9. Összefoglalás
A **területi fejlettségi különbség** a főváros és a vidék között a legnagyobb; az északnyugat jobb helyzetben van, mint a kelet és a dél. ==A népesség fogy, öregszik, és a főváros körül gyűlik össze.== Okai: földrajzi helyzet, közlekedés, tőke, költözés. A felzárkózást az EU is segíti.

> megjegyzés: Válts mutatót, és kattints egy megyére!

### Feliratok
- cím 9: Magyarország megyéi – négy térkép
- gomb GDP: GDP/fő
- gomb változás: Népességváltozás
- gomb öregedés: Öregedés
- gomb sűrűség: Népsűrűség
- honnan típus: Honnan tudjuk?
- honnan cím: Népszámlálás és becslés
- honnan 1: Népesség:
- honnan 1 v: népszámlálás (utoljára 2022. október 1.), utána továbbvezetik
- honnan 2: Továbbvezetés:
- honnan 2 v: születések, halálozások, be- és kiköltözések nyilvántartása
- honnan 3: Megyei GDP:
- honnan 3 v: becslés a vállalkozások telephelyi adataiból
- ö 1: A legnagyobb különbség: főváros és vidék.
- ö 2: Az északnyugat előrébb jár, mint a kelet és a dél.
- ö 3: A népesség fogy, és a főváros körül gyűlik össze.
- ö 4: Minden megyében több a halálozás, mint a születés.
- ö 5: Mindenütt több az idős, mint a gyerek.
- ö 6: Az EU kohéziós politikája a felzárkózást segíti.
- forrás 9: Forrás: KSH · Eurostat · Natural Earth

<!--
  Vitatott / bizonytalan pontok (tanári / szakértői review):
  - A megyei GDP becslés (KSH regionális számlák): a vállalkozások értékét a telephelyek szerint osztják el;
    Budapest értékét felhúzza, hogy sok cég központja és sok ingázó munkahelye ott van (a GDP a megtermelt
    érték helye szerint számol, nem a lakóhely szerint). A KSH az utolsó éveket utólag módosíthatja.
  - A népességsor 2012–2022 között a 2022-es népszámlálásból visszaszámított, 2023-tól továbbszámított
    adat (KSH). A 2001–2011-es évek a 2001-es népszámlálásra épülnek, ezért a lecke a változást 2012-től
    mutatja (a 2011/2012-es váltásnál a sor ugrik).
  - A népmozgalmi mérleg (természetes fogyás + belföldi + nemzetközi vándorlás) 2012–2025 összege a KSH
    adataiban pontosan egyezik a népesség változásával; a nemzetközi vándorlás becsült adat.
  - Az autópálya-hálózat kézzel rajzolt, vázlatos (a fő sugaras vonalak és néhány összekötő); nem teljes,
    és nem mutatja az épülő szakaszokat (pl. M4, M44, M2). Az agglomeráció határa szintén vázlatos folt.
  - A „Bécshez közelebb = fejlettebb” összefüggés megyei szinten laza (19 pont); több tényező együtt hat
    (piacok közelsége, közlekedés, ipari hagyomány, külföldi működőtőke). A lecke nem állít oksági láncot.
  - A kohéziós politika régiós besorolása (75 %-os határ) a 2015–2017-es adatokon alapul; a 2024-es
    értékek csak a mai helyzetet mutatják. Az uniós befizetések és kifizetések mérlegét a lecke nem
    számszerűsíti.
  - A környezeti állapot (Tisza 2000, vörösiszap 2010) ebben a leckében nem szerepel (külön lecke témája).
  - A KSH-adatok a forrás megjelölésével szabadon felhasználhatók (a pontos felhasználási feltétel
    ellenőrizendő); az Eurostat-adatok CC BY 4.0 alatt.
-->
