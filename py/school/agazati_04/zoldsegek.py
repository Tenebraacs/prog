"""
A program a raktáron levő zöldségekkel foglalkozik.
Bizonyos feladatokat kell ellátnia a feldolgozott szövegállományból (adatok.txt).
A feladat megoldásokhoz használja a programozási tételeket!
a) Írjon programot zoldsegek.py néven!
b) Hozzon létre egy osztályt, majd végezze el a beolvasást és eltárolja az adatokat
   egy megfelelő adatszerkezetben. A kódolást állítsa utf-8-ra.
c) Határozza meg és írja ki a képernyőre, a termékek számát a raktáron.
d) Számítsa ki, melyik termékből van a legtöbb. A kiíratásnál szerepeljen a termék neve és mennyisége.
e) Írassa ki, hogy mennyi az átlag termék ár.
f) Számolja ki a raktáron található termékek összértékét. A kapott értéket millióban jelenítse meg.
g) Az átlag feletti termékeket írassa ki a képernyőre. A kiírtatásban szerepeljen az ára és a termék neve.
"""


class ZoldsegRaktar:
    def __init__(self, bemenet):

        # Az adatok beolvasasa:
        data = open(bemenet, "r", encoding="utf-8").read().replace("\n", ";").split(";")
        adatok = list(data)
        self.adatok = adatok
        # print(adatok)

        # A termekek kulonvalogatasa:
        termekek = [adatok[i] for i in range(1, len(adatok), 3)]
        self.termekek = termekek
        # print(termekek)

        # A termekek mennyisegenek kulonvalogatasa
        dl = [float(adatok[i]) for i in range(0, len(adatok), 3)]
        self.dl = dl
        # print(dl)

        # Az ar kulonvalogatasa, atlag kiszamitasa
        ar = [float(adatok[i]) for i in range(2, len(adatok), 3)]
        self.ar = ar
        # print(ar)
        atlag_ossz = sum(ar)
        self.atlag = atlag_ossz / len(termekek)
        # print(self.atlag)

    def termek_szam(self):
        print("\nA termekek szama:", len(self.termekek))

    def legtobb_termek(self):
        legtobb = [0, 0]  # Az elso az index a masodik a legnagyobb mennyiseg
        for i, mennyiseg in enumerate(self.dl):
            if mennyiseg > legtobb[1]:
                legtobb = [i, mennyiseg]
        print("\nA legtobb a(z)", self.termekek[legtobb[0]] + "-bol van es", legtobb[1], "darab van belole")

    def atlagar(self):
        print("\nAz atlagar:", round(self.atlag), "Ft")

    def keszlet_ertek(self):
        keszlet_ertek = 0
        for dl, ar in zip(self.dl, self.ar):
            keszlet_ertek += ar * dl
        print("\nA keszlet erteke:", round(keszlet_ertek / 1000000, 2), "millio forint")

    def atlag_feletti(self):
        print("\nAz atlag aron feluli termekek:")
        for i, ar in enumerate(self.ar):
            if self.atlag < ar:
                print(ar, "Ft   -   ", self.termekek[i])


zoldseg = ZoldsegRaktar("adatok.txt")
zoldseg.termek_szam()
zoldseg.legtobb_termek()
zoldseg.atlagar()
zoldseg.keszlet_ertek()
zoldseg.atlag_feletti()
