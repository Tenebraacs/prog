def karakterek(lista):
    legtobb = [0, 0]  # 1. az index, 2. a karakter szam
    index = -1
    for x in lista:
        szoveg = x
        index += 1
        karaktr_szam = 0
        for _ in szoveg:
            karaktr_szam += 1
        if karaktr_szam > legtobb[1]:
            legtobb = [index, karaktr_szam]
    if legtobb[1] > 15:
        print("A leghosszabb ´" + lista[legtobb[0]] + "´ mondat vagy szo tobb karakterrel rendelkezik mint 15. "
                                                      "Karakterek szama:", legtobb[1])
    else:
        print("A leghosszabb ´" + lista[legtobb[0]] + "´ mondat vagy szo kevesebb karakterrel rendelkezik mint 15. "
                                                      "Karakterek szama:", legtobb[1])


ext = True
karaktr = []

print("Adjon meg egy mondatot vagy szot. Az ENTER gomb lenyomasaval lephet tovabb.")

while ext:
    temp = input("Szoveg:")
    if temp == "":
        ext = False
    else:
        karaktr.append(temp)

karakterek(karaktr)
