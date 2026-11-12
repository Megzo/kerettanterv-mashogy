# Hová lesz az energia? – energiaátalakulások
tantárgy: Fizika · évfolyam: 7–8. · témakör: 2. Az energia

<!--
  Tanári szerkesztés: csak a kettőspont UTÁNI részt írd át!
  A kulcs (a kettőspont előtti rész) a lecke kódjához köt, azt ne változtasd.
  Újragenerálás: python3 tools/build_lesson.py leckek/fizika-7-8/02-energia.md

  A modell egyszerűsítései (a panel is kimondja):
  - nincs légellenállás; a golyót pontszerűnek, csúszónak vesszük (a gördülő golyó
    forgási energiáját nem számoljuk – egy valódi tömör golyó ezért kb. 15 %-kal lassabb);
  - a súrlódási erő a pályát nyomó erővel arányos (a kanyarban a nagyobb nyomóerőt is
    figyelembe vesszük); a melegedést felnagyítva színezzük (19,6 J egy acélpályát csak
    ezredfokokkal melegít);
  - g = 9,81 m/s² (Magyarországon 9,808 m/s²).
  Hatásfokok: kerekített, tipikus értékek (hőerőmű 35–40 %, atomerőmű ≈ 33 %,
  vízerőmű 85–90 %, szélturbina 35–45 % a rotoron átáramló szél energiájából, elméleti
  felső határ 59 % (Betz-határ), napelem 18–23 %). Évente érdemes ellenőrizni.
  Bőr–bőr súrlódási együttható: a mérések 0,2 és 1 között szórnak; 0,5 kerekített érték.
-->

## Közös

### Feliratok
- rugalmas: rugalmas
- helyzeti: helyzeti
- mozgási: mozgási
- belső: belső
- összesen: összesen
- lassítva: lassítva {lassítás}×
- magasság: magasság
- sebesség: sebesség
- kéz: a kezed
- tömeg: tömeg

### Adatok
- nehézségi gyorsulás: 9,81 m/s²
- golyó tömege: 1 kg
- lassítás: 2

## 1. Hová lesz az energia?
Elengedjük a golyót a félcső pereméről. Ide-oda gurul, de **minden alkalommal kicsit lejjebb** jut, végül megáll.

Hová lett az energiája? Sokan mondják: ==elfogyott==. Ebben a leckében utánajárunk, igaz-e.

> megjegyzés: Szavazzatok, mielőtt továbblépsz: elfogyott, elhasználódott vagy átalakult?

### Feliratok
- indulási magasság: indulási magasság
- kérdés: Hová lett az energiája?
- tévhit elfogyott: Elfogyott?
- tévhit elhasználódott: Elhasználódott?
- tévhit átalakult: Átalakult?
- megállt: megállt

## 2. Rugós kilövő
Ha összenyomod a rugót, **rugalmas energiát** tárolsz benne. Elengedve a rugó meglöki a golyót: a rugalmas energia ==mozgási energiává alakul==.

Minél jobban összenyomod, annál több energiát tárol, és annál gyorsabb lesz a golyó.

> megjegyzés: A rugó energiája a kezed munkájából jön. Érdekesség: E_r = ½ · D · x², ahol D a rugóállandó.

### Feliratok
- összenyomás csúszka: A rugó összenyomása
- összenyomás: összenyomás
- elengedve: elengedve!

### Adatok
- rugóállandó: 250 N/m
- rugó összenyomása: 28 cm

## 3. Fel a lejtőn
A lejtőn fölfelé a golyó lassul: a mozgási energiája **helyzeti energiává** alakul.

képlet: E_h = m · g · h

Ahol megáll, ott minden energiája helyzeti. Tedd meredekebbé a lejtőt: ==ugyanolyan magasra jut fel==!

> megjegyzés: Egyszerűsítés: nincs súrlódás, és a golyó forgását nem számoljuk.

### Feliratok
- lejtő csúszka: A lejtő hajlásszöge
- ide jut fel: ide jut fel
- hajlásszög: hajlásszög

### Adatok
- lejtő hajlásszöge: 40°

## 4. Zuhanás
Most ejtsük le a golyót! Esés közben a helyzeti energiája **mozgási energiává** alakul: ==ami az egyikből fogy, az a másikhoz adódik==.

képlet: E_m = ½ · m · v²

A homokba csapódva a mozgási energia **belső energia** lesz: a homok és a golyó kicsit felmelegszik.

> megjegyzés: Légellenállás nélkül számoltunk.

### Feliratok
- ejtés csúszka: Ejtési magasság
- homok: homokos láda
- fent: fent
- leérkezéskor: leérkezéskor
- melegszik: kicsit melegszik

### Adatok
- ejtési magasság: 2 m

## 5. Nehéz és könnyű golyó
Sokan gondolják: ==a nehezebb test gyorsabban esik==.

A nehezebb golyónak több a helyzeti energiája, de több tömeget is kell felgyorsítania. **Kilogrammonként ugyanannyi** energia jut, ezért egyszerre érnek le.

képlet: v = √(2 · g · h)

> megjegyzés: A tollat a levegő fékezi, nem a tömege.

### Feliratok
- tévhit nehéz: A nehezebb gyorsabban esik?
- tömeg csúszka: A nehezebb golyó tömege
- újra gomb: Ejtsd le újra!
- egyszerre: egyszerre érnek le!
- kilogrammonként: kilogrammonként

### Adatok
- nehéz golyó tömege: 5 kg

## 6. Súrlódás: a dörzsölt tenyér
Dörzsöld össze a tenyered! A **súrlódás** fékezi a mozgást, és a mozgási energia ==belső energiává alakul==: a tenyered felmelegszik.

Ha erősebben szorítod, nagyobb a súrlódási erő: ugyanannyi dörzsöléstől melegebb lesz.

> megjegyzés: A színek csak szemléltetnek. A bőr súrlódási együtthatóját {bőr súrlódási együtthatója} körülinek vettük.

### Feliratok
- szorítás csúszka: Milyen erősen szorítod össze?
- dörzsöld gomb: Dörzsöld!
- lánc kémiai: kémiai energia
- izmaid: az izmaidban
- lánc mozgási: mozgási energia
- mozgó kéz: a mozgó kezed
- lánc belső: belső energia
- meleg tenyér: meleg tenyér
- súrlódási erő: súrlódási erő
- dörzsölés útja: a dörzsölés útja
- erő × út: erő × út
- szemléltetés: hőkamera-szerű szemléltetés

### Adatok
- bőr súrlódási együtthatója: 0,5
- szorítóerő: 20 N
- dörzsölés hossza: 10 cm

## 7. Az összeg állandó
Súrlódás nélkül a golyó **mindig ugyanolyan magasra** jut vissza.

Súrlódással a belső energia nő, a pálya melegszik, de ==az összeg állandó==: az energia nem fogy el, csak átalakul.

> megjegyzés: Húzd a golyót! Válts tömeget: a mozgás nem változik.

### Feliratok
- magasság csúszka: Indítási magasság
- súrlódás csúszka: Súrlódás
- tömeg csúszka 7: A golyó tömege
- nincs: nincs
- húzd: húzd!
- pálya melegszik: a pálya melegszik
- felnagyítva: (a melegedést felnagyítottuk)
- idő tengely: idő (s)
- energia tengely: energia (J)

### Adatok
- indítási magasság: 1,6 m
- súrlódási együttható: 0,05

## 8. Erőművi lánc
Az erőmű sem „gyártja” az energiát, hanem **átalakítja** elektromos energiává.

Ami nem lesz elektromos, az sem vész el: hőerőműben nagyrészt ==belső energia lesz a környezetben==. A **hatásfok** megmutatja, hány százalék lesz hasznos.

> megjegyzés: Kerekített, tipikus értékek. A szélturbina elméleti felső határa {szélturbina felső határa}.

### Feliratok
- hőerőmű gomb: Hőerőmű
- atomerőmű gomb: Atomerőmű
- vízerőmű gomb: Vízerőmű
- szélerőmű gomb: Szélerőmű
- napelem gomb: Napelem
- hőerőmű: hőerőmű (szén, földgáz)
- atomerőmű: atomerőmű
- vízerőmű: vízerőmű
- szélerőmű: szélerőmű
- napelem: napelem
- kémiai energia: kémiai energia
- nukleáris energia: nukleáris energia
- napfény: napfény
- elektromos energia: elektromos energia
- kazán: kazán
- reaktor: reaktor
- turbina: turbina
- generátor: generátor
- gát: duzzasztógát
- lapátok: lapátok
- napcella: napcella
- veszteség hő: hő a környezetben (belső energia)
- veszteség víz: hő (belső energia)
- veszteség szél: a szél tovább fúj (mozgási)
- veszteség nap: a panel melegszik, visszaver
- hatásfok: hatásfok
- bemenet: minden 100 J-ból

### Adatok
- hőerőmű hatásfoka: 38 %
- atomerőmű hatásfoka: 33 %
- vízerőmű hatásfoka: 88 %
- szélerőmű hatásfoka: 40 %
- napelem hatásfoka: 21 %
- szélturbina felső határa: 59 %

## 9. Összefoglalás
- Az energia egyik formából a másikba **alakul**: rugalmas, helyzeti, mozgási, belső…
- ==Az összeg mindig ugyanannyi==: az energia nem fogy el, nem vész el.
- Amit „elveszni” látunk, az a súrlódás miatt **belső energia** lesz (melegedés).
- Leérkezéskor a sebesség nem függ a tömegtől.

> megjegyzés: Hol alakul át energia a konyhában? Gyűjtsetek példákat!

### Feliratok
- súrlódás: súrlódás
- magától nem: magától nem alakul vissza
- példa: például
- pl rugalmas: összenyomott rugó
- pl helyzeti: magasan lévő test
- pl mozgási: mozgó test
- pl belső: melegedés
- tanulság: Az energia nem vész el, csak átalakul.
