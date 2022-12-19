exit = False
while exit == False:
    print("----Válasszon a feladatok közül!----")
    print("1.) Írj programot, amely bekér 8 osztályzatot, eltárolja őket egy listában, majd kiírja őket egy sorban, vesszővel elválasztva. Új sorokba kiírja az összegüket, szorzatukat, átlagukat (két tizedes jegyre kerekítve)!")
    print("2.) Kérj be egy nap nevét a felhasználótól és döntsd el, hogy tényleg egy nap nevét adta-e meg. (Segítségül: tárold el a hét napjait egy listában és vizsgáld meg, hogy amit a felhasználó megadott, az eleme-e ennek a listának.)")
    print("3.) Kérjél be öt számot szóközzel elválasztva a felhasználótól és döntsd el, hogy mennyi van 1 és 10 között!")
    print("4.) Döntsd el egy 100-nál kisebb bekért számról, hogy prímszám-e!")
    print("5.) Adott egy lista: [17, 74, 33, 28, 67, 12, 42, 63]. Írd ki a képernyőre a következő kérdésekre adott válaszokat: melyik az első és az utolsó páros szám, hányadik az első héttel osztható szám, melyik az első 60 és 70 közé eső szám, hányadik elem a 12?")
    print("6.) Ha egy szabályos pénzérmét feldobunk, akkor egyenlő eséllyel lehet fej (F) vagy írás (I) az eredmény. Szimulálj öt pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is! Az eredményt írasd ki a képernyőre a mintának megfelelően! Kérj be a felhasználótól egy tippet, majd szimulálj egy pénzfeldobást és írasd ki, hogy eltalálta-e vagy sem!")
    print("7.) Kérj be egy mondatot, cseréld le az ékezetes betűket az ékezet nélküli párjukra, ill. a hosszú í-t i-re, írasd ki az eredményt! Cseréld le a kisbetűket nagybetűkre, és azt is írasd ki! Töröld a nagybetűs verzióból az írásjeleket és a szóközöket, és az eredményt írasd ki a képernyőre!")
    print("8.) Kérj be a felhasználótól egy szót és döntsd el, hogy tartalmaz-e magánhangzót! Amennyiben tartalmaz, a program írja ki a „Van benne magánhangzó.” szöveget, különben azt, hogy „Nincs benne magánhangzó.” Figyelj az ékezetes kis- és nagybetűkre is!")
    print("09.) Tanulmányozd a print() használatának eseteit, és jelenítsd meg print függvénnyel 20 és 7 hányadosát a lenti minta szerint! Az elválasztók tabulátorok.")
    print("Írja be az 'exit' szót a kilépéshez")
    print()
    print("Írja be a választott feladat sorszámát!")
    menu = input(">   ")
    print()
    if menu == "1":
        jegyek = []
        for i in range(8):
            jegy = int(input(f"Adja meg a(z) {i+1}. osztályzatot: "))
            jegyek.append(jegy)
        kiir = ""
        jegyek.sort(reverse = True)
        for k in jegyek:
            kiir += str(k) + ", "
        print()
        print(f"Az osztályzatok: {kiir[:-2]}")
        print()
        print(f"Az osztályzatok összege: {sum(jegyek)}")
        print()
        szorzat = 1
        for s in jegyek:
            szorzat *= s
        print(f"Az osztályzatok szorzata: {szorzat}")
        print()
        print(f"Az osztályzatok átlaga: {(sum(jegyek) / len(jegyek)):.2f}")
        print()
    elif menu == "2":
        napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
        print("Adja meg az ellenőrizni kívánt napot!")
        nap = input(">  ")
        print()
        nap.lower()
        nem = True
        for n in napok:
            if nap == n:
                print(f"Igen! A {nap} egy nap!")
                nem = False
        if nem == True:
            print(f"Sajnos a(z) {nap} nem egy nap.")
        print()
    elif menu == "3":
        print("Adjon meg 5 számot szóközzel elválasztva!")
        szamok = input(">  ")
        print()
        szam = ""
        kozott = 0
        ot = 0
        for z in szamok:
            if z == " ":
                szam = int(szam)
                if 1 <= szam <= 10:
                    kozott += 1
                szam = ""
                ot += 1
            else:
                szam += z
        if ot != 4:
            print("Ez nem 5 szám!")
        else:
            print(f"{kozott} szám van 1 és 10 között.")
        print()
    elif menu == "4":
        print("Írja be az ellenőrizendő 100-nál kisebb számot!")
        prim = int(input(">  "))
        print()
        if prim < 100:
            prime = False
            if prim < 2:
                print("A 2 az első prímszám!")
                prime = True
            if prime == False:
                for p in range(2, prim):
                        if prim % p == 0 and prime != True:
                            print("Ez nem egy prímszám!")
                            prime = True
            if prime == False:
                print("Ez egy prím szám!")
        else:
            print("Ez a szám nem kisebb 100-nál!")
        print()
    elif menu == "5":
        lista = [17, 74, 33, 28, 67, 12, 42, 63]
        print(f"Ezt a listát fogjuk elemezni: {lista}")
        print()
        elso_p = 0
        utolso_p = 0
        for e in lista:
            if e % 2 == 0 and elso_p == 0:
                elso_p = e
        lista.reverse()
        for e in lista:
            if e % 2 == 0 and utolso_p == 0:
                utolso_p = e
        lista.reverse()
        print(f"Az első páros szám a(z) {elso_p} és az utolsó a(z) {utolso_p}.")
        print()
        elso_h = 0
        x = 1
        for e in lista:
            elso_h += x
            if e % 7 == 0:
                x = 0
        print(f"A(z) {elso_h}. szám az első 7-el osztható szám.")
        print()
        elso_k = 0
        for e in lista:
            if 60 < e < 70 and elso_k == 0:
                elso_k = e
        print(f"Az első 60 és 70 közé eső szám a {elso_k}.")
        print()
        tizenketto = 0
        x = 1
        for t in lista:
            tizenketto += x
            if e == 12:
                x = 0
        print(f"A(z) {tizenketto}. elem a 12.")
        print()
    elif menu == "6":
        pass
    elif menu == "7":
        pass
    elif menu == "8":
        pass
    elif menu == "9":
        pass
    elif menu == "exit":
        exit = True
    else:
        print("Érvénytelen menüpont!")
        print()