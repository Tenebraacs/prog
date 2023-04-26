class ItalRaktar:
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
        print("\nA legtobb a(z)", self.termekek[legtobb[0]] + "-bol van es", legtobb[1] / 10, "liter van belole")

    def atlagar(self):
        print("\nAz atlagar:", self.atlag, "Ft")

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


szorp = ItalRaktar("adatok.txt")
szorp.termek_szam()
szorp.legtobb_termek()
szorp.atlagar()
szorp.keszlet_ertek()
szorp.atlag_feletti()
