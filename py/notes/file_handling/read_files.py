#ez egy kicsit másabb mint ahogy a 'file_handling.py' jegyzetben
#ez azért van mert a fájlunkban használunk különleges karaktereket
#ezért átkódoljuk egy olyan kódexre amely érti ezeket
x = open("demofile.txt", mode = "r", encoding = "utf-8")
print(x.read())
#zárjuk be a fájlt mert már "nem kell"
x.close()


#ha esetleg nem ugyan abban a mappában lenne a fájl mint a kód akkor a teljes elérési utat kell megadni
x = open("D:/kz_pa_10D/prog/py/notes/file_handling/demofile.txt", mode = "r", encoding = "utf-8")
print(x.read())
x.close()


#ha szeretnénk azt is meg lehet adni, hogy hány karaktert szeretnénk elolvasni
x = open("demofile.txt", mode = "r", encoding = "utf-8")
print(x.read(5))
x.close()


#arra is van lehetőség, hogy csak egy sort kérjünk be
x = open("demofile.txt", mode = "r", encoding = "utf-8")
print(x.readline().strip()) #a '.strip()' azért kell, hogy az eredeti fájlban a sor végén nyomott enter-t ne printelje
x.close()


#ha pl. 2-szer kérünk be sort akkor 2 sor lesz printelve
x = open("demofile.txt", mode = "r", encoding = "utf-8")
print(x.readline().strip())
print(x.readline().strip())
x.close()


#az összes sort egy loop-al iratjuk ki
x = open("demofile.txt", mode = "r", encoding = "utf-8")
for f in x:
  print(f) #itt látni a különbséget mert itt kiírja a sor végén a '\n'-t az az, az entert
x.close()


#adjunk hozzá a 'demofile2.txt'-hez valamit.
x = open("demofile2.txt", mode = "a", encoding = "utf-8")
x.write("\n Ezt a mondatot most hozzá-adtam! :)")
x.close()

#nyissuk meg és nézzük meg a hozzá adott mondatot
x = open("demofile2.txt", mode = "r", encoding = "utf-8")
print(x.read())
x.close()


#írjuk át a 'demofile3.txt' tartalmát
x = open("demofile3.txt", mode = "w", encoding = "utf-8")
x.write("Kicseréltem az eredeti mondatot erre, hehehehe")
x.close()

#nyissuk meg és nézzük meg, hogy át lett-e írva (először ajánlott megváltoztatni a 'demofile3.txt' tartalmát)
x = open("demofile3.txt", mode = "r", encoding = "utf-8")
print(x.read())
x.close()