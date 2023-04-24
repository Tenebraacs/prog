def karakterek(lista):
    if not lista:
        pass
    else:
        legtobb = [0, 0]  # 1. az index, 2. a karakter szam
        for i, x in enumerate(lista):
            szoveg = x
            karaktr_szam = 0
            for _ in szoveg:
                karaktr_szam += 1
            if karaktr_szam > legtobb[1]:
                legtobb = [i, karaktr_szam]
        return legtobb


ext = True
karaktr = []

print("Adjon meg egy mondatot vagy szot. Az ENTER gomb lenyomasaval lephet tovabb.")

while ext:
    temp = input("Szoveg:")
    if temp == "":
        ext = False
    else:
        karaktr.append(temp)

if karakterek(karaktr) is None:
    print("\nNem adott meg semmit!")
elif karakterek(karaktr)[1] > 15:
    print("\nA leghosszabb ´" + karaktr[karakterek(karaktr)[0]] + "´ mondat vagy szo tobb karakterrel rendelkezik "
                                                                  "mint 15. Karakterek szama:", karakterek(karaktr)[1])
else:
    print("\nA leghosszabb ´" + karaktr[karakterek(karaktr)[0]] + "´ mondat vagy szo kevesebb karakterrel rendelkezik "
                                                                  "mint 15. Karakterek szama:", karakterek(karaktr)[1])
