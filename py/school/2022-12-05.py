import math
import random


#1. feladat
print("1.)  Kérj be egy egész számot, és írd ki a kétszeresét, a heted részét (2 tizedes jegyre kerekítve), a négyzetgyökét (0.5-ödik hatvány), 3-mal osztva a hányados egész részét és a maradékot, és hogy páros vagy páratlan. (Tipp: egy szám egész, ha egyenlő az egészrészével.)")

fel1 = int(input("Írja be az egész számot: "))
print("A szám 2-szerese: " + str(2* fel1))
print("A szám heted része (2 tizedes jegy pontossággal):  " + str(round(fel1 / 7, 2)))
print("A szám négyzetgyöke:  " + str(math.sqrt(fel1)))
print("3-mal osztva az egész része: " + str((fel1 - fel1 % 3) / 3))
print("3-mal osztva a maradék: " + str(fel1 % 3))
if fel1 % 2 == 0:
    print("Ez egy páros szám")
else:
    print("Ez egy páratlan szám")


#2. feladat
print("2.) Írasd ki a következő értékek típusát: ’anya’     5      3.14     [1,2,3]")

print(type('anya'))
print(type(5))
print(type(3.14))
print(type([1,2,3]))


#3. feladat
print("3.) Kérj be a felhasználótól két számot, amely egy közönséges tört számlálója és nevezője! A program döntse el, hogy az így bevitt tört felírható-e egész számként! Ha igen, írja ki a tört értékét egész számként, ha nem, írja ki: „Nem egész”!")

szamlalo = int(input("Adja meg a tört számlálóját: "))
hanyados = int(input("Adja meg a tört hányadosát: "))
if szamlalo % hanyados == 0:
    print("Ez egy egész szám. Természetes szám formájában így néz ki: " + str(int(szamlalo / hanyados)))
else:
    print("Nem egész!")


#4. feladat
print("4.) Vesszővel és szóközzel elválasztva írasd ki a képernyőre a 100000-nél kisebb négyzetszámokat!")

x = 0
y = 1
z = ""
first = True
while x < 100000:
    if first:
        first = False
    else:
        z += str(x) + ", "  
    x = y ** 2
    y += 1
print(z[:-2])


#5. feladat
print("5.) Egy listában tároljuk, hogy a focicsapatunk az egyes meccsein nyert, vesztett, vagy döntetlent játszott: [‘ny’, ‘ny’, ‘v’, ‘d’, ‘d’, ‘d’, ‘v’, ‘v’, ‘ny’, ‘ny’, ‘d’]. A győzelemért három, a döntetlenért egy pont jár. Írd ki a képernyőre, hány pontja van a bajnokságban?")

foci = ['ny', 'ny', 'v', 'd', 'd', 'd', 'v', 'v', 'ny', 'ny', 'd']
pont = 0
for e in foci:
    if e == "ny":
        pont += 3
    elif e == "d":
        pont += 1
    else:
        pont += 0
print("A foci csapat pontjai a bajnokságban: " + str(pont))


#6. feladat
print("6.) Kérd be a és b egész számokat, és írd ki a/b és b/a hányadosokat és azt is, hogy a hányadosok egész számok-e (pl. 3.45 nem egész 7 egész; a törteket a feladatban két tizedes jegyre kerekítve jelenítsd meg), az a hány százaléka b-nek és fordítva.")

a = int(input("Adja meg az 'a' egész számot: "))
b = int(input("Adja meg a 'b' egész számot: "))
print("Az a/b eredménye: " + str(a/b))
print("Ez egy egész szám: " + str(int(a/b) - a/b == 0))
print("Az b/a eredménye: " + str(b/a))
print("Ez egy egész szám: " + str(int(b/a) - b/a == 0))
print("Az 'a' " + str(a / (b /100)) + "%-a a 'b'-nek")
print("A 'b' " + str(b / (a /100)) + "%-a az 'a'-nak")


#7. feladat
print("7.) Hozz létre egy listát, amelynek elemszáma véletlenszerű 20-40 között, és a lista elemei 1 és 10 közötti véletlen számok (1 és 10 is lehet benne)! Írd ki a lista elemeinek a számát, a legkisebb és a legnagyobb számot, és hogy milyen elemből hány darab van a listában.")

listahossz = random.randint(20, 40)
lista1 = []
for x in range(listahossz):
    lista1.append(random.randint(1, 10))


#8. feladat
print("8.) Írj programot, amely bekér 8 osztályzatot, eltárolja őket egy listában, majd kiírja őket egy sorban, vesszővel elválasztva. Új sorokba kiírja az összegüket, szorzatukat, átlagukat (két tizedes jegyre kerekítve)!")

jegy = []
ir = ""
osszeg = 0
szorzat = 0
first = True

for j in range(7):
    jegy += input("Adjon meg egy osztályzatot: ")

for o in jegy:
    ir += str(o) + ", "
print(ir[:-2])

for o in jegy:
    osszeg += o
print(osszeg)

for o in jegy:
    if first:
        szorzat += o
        first = False
    else:
        szorzat *= o
print(szorzat)

print(round(osszeg / len(jegy), 2))
