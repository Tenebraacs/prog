"""2.) Készítsd el az "szamol.py" python programot, amiben töltsön fel egy listát 100 elemmel, 1 és 500 közötti
értékkel. Írjon függvényt, ami a listát várja paraméterül. Ennek visszatérési értéke az, hogy hány darab 3-al
osztható szám van a listában, írja ki a lista 3-al osztható elemeit.
"""
import random


def oszthatoe(lista):
    oszthato = 0
    for elem in lista:
        if elem % 3 == 0:
            oszthato += 1
    return oszthato


szamok = []
for _ in range(100):
    szamok.append(random.randint(1, 500))

print("A random szamos listaban", oszthatoe(szamok), "szam oszthato 3-al")
