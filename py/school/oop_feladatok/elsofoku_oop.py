# Feladat: OOP szemlelettel irj python kodot,
#          amivel meghatarozod az elsofoku egyenlet gyoket.
#          altalanos alak: f(x) = m*x + b
#          gyok: x = -b/m

import os

os.system("cls")


class Elsofok:
    def __init__(self, b, m):
        self.b = b
        self.m = m

    def gyok(self):
        if self.m == 0:
            print("Az 'm' nem lehet nulla!")
        else:
            x = -self.b / self.m
            print("A 'b' erteke:", self.b, "\nAz 'm' erteke:", self.m)
            print("\nAz x erteke:", x)


elsofoku = Elsofok(5, 8)
elsofoku.gyok()
