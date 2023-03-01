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
lista = []
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
        





"""
def osszeg_fajlbol(bemenet, mod):
    # Olvassuk be az input.txt fájlt listába
    with open(bemenet, mod) as file:
        lista = [int(x.strip()) for x in file.readlines()]
    
    # Számítsuk ki a lista elemeinek összegét
    osszeg = sum(lista)
    
    # Írjuk ki a képernyőre az összeget
    print(osszeg)

osszeg_fajlbol("input.txt", "r") # futtatjuk a fuggvenyt
"""