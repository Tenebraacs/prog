"""
3.) Készítsd el az "futball.py" python programot, amiben  írjon "Focista" osztályt, "__init__(") fv-el,
ami paraméterül a focista nevét, poszttját, csapatát(R/M) kapja, illetve tartalmazza a "csapat_neve" függvényt: ami R
estén a "Real Madrid", "M" esetén a "Manchester City" visszatérési értékkel rendelkezik.

Töltsön fel egy 3 elemű tömböt a usertől kért adatokkal(név/poszt/csapat), írja ki, a melyik csapat, melyik játékosa,
melyik poszton szerepe a listában.
"""


class Focista:
    def __init__(self, nev, poszt, csapat):
        self.nev = nev
        self.poszt = poszt
        self.csapat = csapat

    def csapat_neve(self):
        if self.csapat == 'R':
            return 'Real Madrid'
        elif self.csapat == 'M':
            return 'Manchester City'
        else:
            return 'Ismeretlen csapat'


jatekos_lista = []
for i in range(3):
    nev = input("Add meg a(z) {}. jatekos nevet: ".format(i + 1))
    poszt = input("Add meg a(z) {}. jatekos posztjat: ".format(i + 1))
    csapat = input("Add meg a(z) {}. jatekos csapatat (R/M): ".format(i + 1))

    jatekos = Focista(nev, poszt, csapat)
    jatekos_lista.append(jatekos)

for jatekos in jatekos_lista:
    csapat_nev = jatekos.csapat_neve()
    print(jatekos.nev, "nevu jatekos", csapat_nev, "nevu csapatban", jatekos.poszt, "-kent tevekenykedik")
