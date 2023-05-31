class KosarlabdaMerkozesek:
    def __init__(self, txt):
        data = open(txt, "r", encoding="utf-8").read().replace("\n", " ").split(" ")
        merkozes_adatok = list(data)
        self.merkozes_adatok = merkozes_adatok
        # print(merkozes_adatok)

        otthon = [merkozes_adatok[i] for i in range(2, len(merkozes_adatok), 4)]
        self.otthon = otthon
        # print(otthon)

        vendeg = [merkozes_adatok[i] for i in range(3, len(merkozes_adatok), 4)]
        self.vendeg = vendeg
        # print(vendeg)

        nap_sorszam = [int(merkozes_adatok[i]) for i in range(4, len(merkozes_adatok), 4)]
        self.nap_sorszam = nap_sorszam
        # print(nap_sorszam)

        ar = [int(merkozes_adatok[i]) for i in range(5, len(merkozes_adatok), 4)]
        self.ar = ar
        # print(ar)

    def csapat_ossz(self):
        alkalom_ar = [0, 0]
        for otthon, vendeg, ar in zip(self.otthon, self.vendeg, self.ar):
            if otthon == "Voros_Rokak" or vendeg == "Voros_Rokak":
                alkalom_ar[0] += 1
                alkalom_ar[1] += ar
        return alkalom_ar

    def elso_utolso(self):
        elso = 0
        for otthon, nap in zip(self.otthon, self.nap_sorszam):
            if otthon == "Voros_Rokak":
                elso = nap
                break
        utolso = 0
        for otthon, nap in zip(reversed(self.otthon), reversed(self.nap_sorszam)):
            if otthon == "Voros_Rokak":
                utolso = nap
                break
        return elso, utolso

    def utolso_kedvenc_merkozes(self):
        kedvencek = ["Voros_Rokak", "Computerbontok", "Bohocok"]
        for otthon, vendeg, nap in zip(reversed(self.otthon), reversed(self.vendeg), reversed(self.nap_sorszam)):
            if otthon in kedvencek and vendeg in kedvencek:
                return nap

    def jegyvasarlas_napok(self):
        penz = int(self.merkozes_adatok[1])
        napok = []

        for otthon, vendeg, nap, ar in zip(self.otthon, self.vendeg, self.nap_sorszam, self.ar):
            if otthon == "Voros_Rokak" or vendeg == "Voros_Rokak":
                penz -= ar
                if penz <= 0:
                    penz += ar
                    break
                napok.append(nap)

        rendezes = []
        for otthon, nap, ar in zip(self.otthon, self.nap_sorszam, self.ar):
            if otthon == "Computerbontok":
                temp = [ar, nap]
                rendezes.append(temp)
            if otthon == "Bohocok":
                temp = [ar, nap]
                rendezes.append(temp)
        rendezes.sort()
        for ar, nap in rendezes:
            penz -= ar
            if penz <= 0:
                penz += ar
                break
            napok.append(nap)

        napok.sort()
        """
        for i, nap in enumerate(napok):
            if nap == napok[i+1]:
                napok.pop(i+1)
        """
        napok_string = ""
        for x in napok:
            napok_string += str(x) + " "
        return napok_string, napok

    def kedvenc_csapatok(self):
        napok = self.jegyvasarlas_napok()[1]
        rokak, bontok, bohocok = 0, 0, 0
        tobbiek = ["Computerbontok", "Bohocok"]
        for otthon, vendeg, nap in zip(self.otthon, self.vendeg, self.nap_sorszam):
            if otthon == "Voros_Rokak" or vendeg == "Voros_Rokak":
                rokak += 1
            if otthon in tobbiek and nap in napok:
                if otthon == "Bohocok":
                    bontok += 1
                if otthon == "Computerbontok":
                    bohocok += 1
        return rokak, bontok, bohocok


kosar = KosarlabdaMerkozesek("naptar.txt")
print("1.feladat:")
print("A Voros_Rokak", kosar.csapat_ossz()[0], "mérkőzést játszik, a jegyárak összege", kosar.csapat_ossz()[1], "Ft")
print("\n")
print("2.feladat")
print("Először:", kosar.elso_utolso()[0], ". napon, utoljára:", kosar.elso_utolso()[1], ". napon")
print("\n")
print("3.feladat")
print("Utolsó mérkőzés napja:", kosar.utolso_kedvenc_merkozes())
print("\n")
print("4.feladat")
print("A következő napokra vesz jegyet:", kosar.jegyvasarlas_napok()[0])
print("\n")
print("5.feladat")
print("Voros_Rokak:", kosar.kedvenc_csapatok()[0])
print("Computerbontok:", kosar.kedvenc_csapatok()[1])
print("Bohocok:", kosar.kedvenc_csapatok()[2])
