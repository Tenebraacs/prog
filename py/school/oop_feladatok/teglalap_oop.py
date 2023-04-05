# Feladat: OOP szemlelettel irj python kodot.
#          amivel meghatorozod egy teglalap kerultet es teruletet.
#          irj kerulet es terulet metodusokat is.
import os

os.system("cls")


class teglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kerulet(self):
        ker = (2 * self.a) + (2 * self.b)
        print("A teglalap oldalai", self.a, self.b)
        print("A kerulete:", ker)

    def terulet(self):
        ter = self.a * self.b
        print("A teglalap oldalai", self.a, self.b)
        print("A terulete:", ter)


tegla = teglalap(7, 3)
tegla.kerulet()
tegla.terulet()
