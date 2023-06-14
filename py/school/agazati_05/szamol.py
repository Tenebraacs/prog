"""
2.) Készítsd el az "szamol.py" python programot, amiben töltsön fel egy listát 100 elemmel, 1 és 500 közötti
értékkel. Írjon függvényt, ami a listát, és az osztőt várja paraméterül. Ennek visszatérési értéke az,
hogy hány osztóval osztható szám van a listában, írja ki a lista osztóval osztható elemeit.
"""
import random


def oszthato(lista, oszto):
    oszthato_szamok = []
    for x in lista:
        if x % oszto == 0:
            oszthato_szamok.append(x)
    return oszthato_szamok


lista = []
for _ in range(0, 100):
    lista.append(random.randint(1, 500))

oszto = int(input("Kerem az osztot:"))

oszthato_szamok = oszthato(lista, oszto)
oszthato_szamok_string = ""

print("A listaban", len(oszthato_szamok), ",", oszto, "-al oszthato szam van")
print("Az oszthato szamok:")
for szam in oszthato_szamok:
    oszthato_szamok_string += str(szam) + ", "
print(oszthato_szamok_string)
