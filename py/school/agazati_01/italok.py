class ItalRaktar:
    def __init__(self, bemenet):

        # Az adatok beolvasasa:
        data = open(bemenet, "r", encoding="utf-8").read().replace("\n", ";").split(";")
        adatok = list(data)
        self.adatok = adatok
        # print(adatok)

        # A termekek kulonvalogatasa:
        termekek = [self.adatok[i] for i in range(1, len(self.adatok), 3)]
        self.termekek = termekek
        # print(termekek)

        # A termekek mennyisegenek kulonvalogatasa
        dl = [float(self.adatok[i]) for i in range(0, len(self.adatok), 3)]
        self.dl = dl
        # print(dl)

        # Az ar kulonvalogatasa, atlag kiszamitasa
        ar = [float(self.adatok[i]) for i in range(2, len(self.adatok), 3)]
        self.ar = ar
        # print(ar)
        atlag_ossz = 0
        for x in ar:
            atlag_ossz += x
        self.atlag = atlag_ossz / len(self.termekek)
        # print(self.atlag)

    def termek_szam(self):
        print("A termekek szama:", len(self.termekek))

    def legtobb_termek(self):
        legtobb = [-1, 0]
        for i, mennyiseg in enumerate(self.dl):
            if mennyiseg > legtobb[1]:
                legtobb = [i, mennyiseg]
        print("A legtobb a(z)", self.termekek[legtobb[0]] + "-bol van es", legtobb[1] / 10, "liter van belole")

    def atlagar(self):
        print("Az atlagar:", self.atlag, "Ft")

    def keszlet_ertek(self):
        keszlet_ertek = 0
        for liter, ar in zip(self.dl, self.ar):
            if liter == 0:
                pass
            else:
                keszlet_ertek += ar * liter
        print(keszlet_ertek)


szorp = ItalRaktar("adatok.txt")
szorp.termek_szam()
szorp.legtobb_termek()
szorp.atlagar()
szorp.keszlet_ertek()
