"""
3.)  A program a raktáron levő autókkal foglalkozik.
Bizonyos feladatokat kell ellátnia a feldolgozott szövegállományból (adatok.txt).
A feladat megoldásokhoz használja a programozási tételeket!
a) Írjon programot auto.py néven!
b) Hozzon létre egy osztályt, majd végezze el a beolvasást és eltárolja az adatokat
   egy megfelelő adatszerkezetben. A kódolást állítsa utf-8-ra.
c) Határozza meg és írja ki a képernyőre, a termékek számát a raktáron.
d) Számítsa ki, melyik autó típusból van a legtöbb. A kiíratásnál szerepeljen az autó típusa és mennyisége.
e) Írassa ki, hogy mennyi az átlag autó ár.
f) Számolja ki a raktáron található autók összértékét. A kapott értéket százmillióban jelenítse meg.
g) Az átlag feletti autókat írassa ki a képernyőre. A kiírtatásban szerepeljen az ára és a típusa.
"""

class AutoRaktar:
    def __init__(self, bemenet):
        beolvas = open(bemenet, "r", encoding="utf-8").read().replace("\n", ",").split(",")
        adatok = list(beolvas)
        self.adatok = adatok

        autok = [adatok[i] for i in range(1, len(adatok), 3)]
        self.autok = autok
        print(autok)

        darab = [int(adatok[i]) for i in range(0, len(adatok), 3)]
        self.darab = darab
        print(darab)

        ar = [int(adatok[i]) for i in range(2, len(adatok), 3)]
        self.ar = ar
        print(ar)

        ar_ossz = 0
        for x in ar:
            ar_ossz += x
        atlag_ar = ar_ossz / len(ar)
        self.ar_ossz = ar_ossz
        self.atlag_ar = int(atlag_ar)

    def termek_szam(self):
        print("A raktaron levo termekek szama:", len(self.autok))

    def termek_legtobb(self):
        index = 0
        for i, darab in enumerate(self.darab):
            if darab > self.darab[index]:
                index = i
        print("A legtobb a", self.autok[index], "-bol van es", self.darab[index], "darab van belole")

    def termek_atlag(self):
        print("Az autok atlag ara:", self.atlag_ar, "forint")

    def termek_ossz_ar(self):
        print("A raktaron levo autok ossz ara:", round(self.ar_ossz / 1000000), "millio forint")

    def atlag_feletti_termekek(self):
        print("Atlagon feluli termekek:")
        for i, ar in enumerate(self.ar):
            if ar > self.atlag_ar:
                print(self.autok[i], "    -   ", ar, "Ft")


autok = AutoRaktar("adatok.txt")
autok.termek_szam()
autok.termek_legtobb()
autok.termek_atlag()
autok.termek_ossz_ar()
autok.atlag_feletti_termekek()
