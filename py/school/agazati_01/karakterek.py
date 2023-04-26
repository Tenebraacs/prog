def karakterek(lista):
    if not lista:
        pass
    else:
        legtobb = [0, 0]  # 1. az index, 2. a karakter szam
        for i, x in enumerate(lista):
            if len(x) > legtobb[1]:
                legtobb = [i, len(x)]
        return legtobb


print("Adjon meg egy mondatot vagy szot. Az ENTER gomb lenyomasaval lephet tovabb.")

karaktr = []
while True:
    temp = input("Szoveg:")
    if temp != "":
        karaktr.append(temp)
    else:
        break

if karakterek(karaktr) is None:
    print("\nNem adott meg semmit!")
elif karakterek(karaktr)[1] > 15:
    print("\nA leghosszabb ´" + karaktr[karakterek(karaktr)[0]] + "´ mondat vagy szo tobb karakterrel rendelkezik "
                                                                  "mint 15. Karakterek szama:", karakterek(karaktr)[1])
else:
    print("\nA leghosszabb ´" + karaktr[karakterek(karaktr)[0]] + "´ mondat vagy szo kevesebb karakterrel rendelkezik "
                                                                  "mint 15. Karakterek szama:", karakterek(karaktr)[1])
