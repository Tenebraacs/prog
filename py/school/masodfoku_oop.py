# Feladat: OOP szemlelettel irj pytho kodot,
#          amivel meghatarozzuk a masodfoku egyenlet gyoket.
#          altalanos alak: f(x) = a*x2 + b*x + c
#          gyokok: x1 = (-b+sqrt(b2 - 4*a*c))/2*a
#                  x2 = (-b-sqrt(b2 - 4*a*c))/2*a

import os
import math

os.system("cls")


class Masodfok:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def gyok(self):
        if self.a == 0:
            print("Az 'a' ertek nem lehet nulla!")
        else:
            x1 = (-self.b + math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / (2 * self.a)
            print("A megadott ertekek:", self.a, self.b, self.c, "(a,b,c)")
            print("\nA gyokok: - x1:", x1, "\n          - x2:", x2)


masodfok = Masodfok(2, 8, 6)
masodfok.gyok()
