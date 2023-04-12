# Feladat: OOP szemlelet szerint irj python kodot,
#          amivel meghatarozod, hogy:
#          1.) harom adatbol szerkesztheto-e haromszog,
#          2.) ha igen, akkor mi a haromszog tipusa? :
#               - altalanos
#               - egyenlo szaru
#               - egyenlo oldalu
#               - derekszogu
#          A haromszog egyenlotlenseg algoritmusa: a - b < c ES b - c < a ES c - a < b

import os

os.system("cls")


class Haromszog:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def szerkesztheto_haromszog(self):
        if self.a - self.b < self.c and self.b - self.c < self.a and self.c - self.a < self.b:
            print("Az adatokbol szerkesztheto haromszog\n")
            szerkesztheto_haromszog = True
        else:
            print("Az adatokbol NEM szerkesztheto haromszog\n")
            szerkesztheto_haromszog = False
        return szerkesztheto_haromszog

    def haromszog_tipusa(self):
        if self.szerkesztheto_haromszog:
            if self.a**2 + self.b**2 == self.c**2 or self.a**2 + self.c**2 == self.b**2 or self.b**2 + self.c**2 == self.a**2:
                print("Ez egy derekszogu haromszog, pitagorsz tetellel meghatarozva")
            elif self.a != self.b and self.a != self.c and self.b != self.c:
                print("Ez egy altalanos haromszog, mert:")
                print("A háromszögnek nincs két egyenlő oldala vagy szöge. Az oldalak hossza különböző.")
            elif (self.a == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b) or (self.b == self.c and self.b != self.a):
                print("Ez egy egyenlo szaru haromszog, mert:")
                print("A háromszögnek két oldala egyenlő hosszúságú, és a harmadik oldaluk különbözik.")
            elif self.a == self.b == self.c:
                print("Ez egy egyenlo oldalu haromszog, mert:")
                print("A háromszögnek minden oldala egyenlő hosszúságú.")
            else:
                print("Sajnos nem tudom meghatarozni a haromszog tipusat")
        else:
            print("Ez nem egy haromszog, az az nem lehet a tipusat meghatarozni")
        print("\n")


haromszog = Haromszog(3, 3, 5)
haromszog.szerkesztheto_haromszog()
haromszog.haromszog_tipusa()

haromszog = Haromszog(4, 6, 8)
haromszog.szerkesztheto_haromszog()
haromszog.haromszog_tipusa()

haromszog = Haromszog(6, 6, 6)
haromszog.szerkesztheto_haromszog()
haromszog.haromszog_tipusa()

haromszog = Haromszog(3, 4, 5)
haromszog.szerkesztheto_haromszog()
haromszog.haromszog_tipusa()
