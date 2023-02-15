# 1) egy input fájlt (te írod az input.txt-t számok legyenek, vesszővel elválasztva) vár, beolvassa a fájlt egy listába, majd kiírja a lista elemeit.
# 2) az 1) feladat paraméteresen oldja meg
# 3) az 1) feladatot oldja meg a fájl közvetlen használatával, a "with" utasítással
# 4) írj függvényt, ami a másodfokú egyenlet együtthatóit várja paraméterül, és meghatározza a gyököket

def read_file2list(input, mode):
    file = open(input, mode)
    data = file.read()
    print("Adatok a fajlban: \n", data)
    lst = data.split(",")
    file.close()
    print("Adatok a listaban: \n", lst)

read_file2list()

