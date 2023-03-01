# kepernyo torles
import os
os.system("cls")

# az input lista
l = [11,12,13,14,15,16,17,18,19,20,21,22,23]
print("Az input lista:", l)
print("A lista hossza:", len(l))

# emlek: lista elemek indexe, es az elem: az enumerate -felsorol- fuggveny hasznalataval
for index, elem in enumerate(l):
    print("index: ", index, ", az elem:", elem)
print("\n")

# 1.) osszegzes: hatarozzuk meg a tomb elemeinek osszeget
#
# osszeg = 0
# ciklus i = 0 .. n -1
#   osszeg = osszeg + l[i]
# ciklus vege
# ki osszeg

print("Osszegzes tetel:\n===============")

# algoritmus szerinti megoldas
def osszegzes_kl(lst):
    ossz = 0
    for elem in lst:
        ossz = ossz + elem
    print("Az adatok osszege algoritmus szerint:", ossz)

osszegzes_kl(l)

# megoldas beepitett fuggvennyel 
def osszegzes_fv(lst):
    ossz = sum(lst)
    print("Az adatok osszege sum fuggvennyel:", ossz)

osszegzes_fv(l)
print("\n")

### Orai feladat:  - ird meg az "osszeg_fajlbol" parametres fuggvenyt,
### =============  ami ket parameterrel rendelkezik: "bemenet", "mod"
###                - olvasd be az "input.txt" allomanyt egy listaba
###                - ird ki a listaelemek oszeget a kepernyore


def osszeg_fajlbol(bemenet, mod):

    ### beolvasas, "\n" csereje ","-re, hasitas "," szerint
    adatok = open(bemenet, mod).read().replace("\n", ",").split(",")

    ### adatok listaba, listaelemek konverzioja stringbol-bol egeszre
    ## mag fuggveny, lasd: https://www.w3schools.com/python/ref_func_map.asp
    lista = list(map(int, adatok))
    print("A fajl adatai listaba olvasva: ", lista)
    osszeg = sum(lista)
    return osszeg

print("Az input.txt fajl adatainak osszege:", osszeg_fajlbol("input.txt", "r"))
print("\n")
        

# 2.) Megszamolas: Adott feltetelek alapjan a tomb
# ===============  bizonyos elemeit megszamoljuk.
# pl.: megszamoljuk mennyi negativ szam van a tomben
#
# szamlalo = 0
# ciklus i = 0 .. n - 1
#   ha t[i] < 0 akkor
#       szamlalo = szamlalo + 1
#   ha vege
# ciklus vege
# ki szamlalo

print("Megszamolas tetel:\n=================")

# algoritmus szerinti megoldas
def megszamol_kl(miben, mit):
        szamlalo = 0
        for elem in miben:
            if elem < mit:
                szamlalo = szamlalo + 1
        print("Megszamolas algoritmussal: a listaban ", szamlalo, " darab negativ szam van")

megszamol_kl(l,0)

# megoldas beepitett fuggvennyel
def megszamol_fv(miben, mit):
    darab = miben.count(mit)
    print("Megszamolas algoritmussal, alapbol korlatos: a listaban ", darab," darab", mit, "-as/es szam van")

# ez NEM tudja igy megszamolni az osszes negativ/pozitiv szamot
# csak konkretan az adott szamot
megszamol_fv(l, -8)

# megoldas beepitett fuggvennyel, kiterjesztett megoldas
def megszamol_fv_kit(miben):
    neg_list = [n<0 for n in miben]
    darab = neg_list.count(True)
    print("Megszamolas algoritmussal, kiterjesztett megoldas: a listaban ", darab, " darab negativ szam van")

megszamol_fv_kit(l)
print("\n")

# 3.) Eldontes: Szeretnenk tudni , hogy egy ertek megtalalhato-e egy tomben,
# ===========   ha igen megallunk a futtatassal
#
# van = 0
# ciklus i = 0 .. n-1
#   ha tomb[i] = keresett_ertek akkor
#       van = 1
#   ha vege
#   ciklus futtatasanak vege
# ciklus vege

print("Eldontes tetel:\n===============")
def eldontes(lst, ker_ertek):
    van = False
    for elem in lst:
        if elem == ker_ertek:
            van = True
        break
    return van

eredmeny = eldontes(l, 18)
print("A keresett ertek benne van a listaban")
print("\n")

# 4.) Kivalasztas: Adott elem a tomb
# ===============  hanyadik helyen van.
# A kivalasztas tetelt akkor hasznaljuk, ha tudjuk,
# hogy a keresett erteket tartalmazza a tomb.
# Ezert azt nem vizsgaljuk, hogy vege van-e a tombnek.
#
# i = 0
# ciklus amig tomb[i] <> ker
#   i = i + 1
# ciklus vege
# ki i + i

# algoritmus szerinti megoldas
print("Kivalasztas tetel\n==================")
def kivalasztas(lst):
    for index,elem in enumerate(lst):
    #minden pozitiv szam
        if elem > 0:
            print("A lsitaban ", index," indexen all a pozitiv szam a lista ", elem,". helyen.")

kivalasztas(l)
print("\n")