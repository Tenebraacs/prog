"""
1.) Készítsd el az "eletkor.py" python programot, ami kérjen be két és a névhez tartozó életkort.
     Döntse el, ki idősebb, illetve egykorúak-e?
"""
eletkor = []
for _ in range(2):
    eletkor.append(input("Irja be a szemely nevet:"))
    eletkor.append(int(input("Irja be az eletkorat:")))

print("\n")

if eletkor[1] == eletkor[3]:
    print("A ket szemely ugyan annyi idos.")
elif eletkor[1] > eletkor[3]:
    print(eletkor[0], "idosebb, mint", eletkor[2])
else:
    print(eletkor[2], "idosebb, mint", eletkor[0])
