#A fájl kezelés a Python-ban egy igen egyszerű dolog (ha txt-ről van szó)
#Ebben a jegyzetben csak magyarázat lesz és a többiben tesztelni fogom öket



#Fontos fogalmak a fájlkezeléshez:

# buffer - a buffer egy olyan átmeneti memória tárolási módszer (a számítógép RAM-jában történik ez) ahol a számítógép a változások adtait tárolja amíg az mozgatva/módosítva van. ez a folyamatban lévő folyamatokat drasztikusan felgyorsítja és biztosítja az adatok megmaradását, azonban ha túl magas a buffer a visszamaradt folyamatokból akkor a számítógép fizikai limitálásaiba ütközhetünk és az ellenkezője fog történni.
# tty - a tty egy olyan terminál eszköz mely karakterről-karakterre fogad be- és kimenetelt. (pl.: modem) 



#a fájlkezelésnél 16 alap metódust sorol fel a W3schools:

# open() - megnyitja a fájlt
# close() - bezárja a fájlt
# detach() - visszaadja a leválasztott nyers adatfolyamot a buffer-ből
# fileno() - visszadja a fájl helyének a sorszámát az operációs rendszer szemszögéből
# flush() - kiüríti a buffer-t
# isatty() - ellenőrzi, hogy az adott fájl hozzá van-e kapcsolva egy terminálhoz vagy egy tty eszközhöz (boolean)
# read() - visszadja a fájl tartalmát
# readable() - ellenőrzi, hogy az adott fájl 'olvasható'-e (boolean)
# readline() - egy sort fog vissza adni a fájlból
# readlines() - vissza ad egy listát a fájl soraiból
# seek() - megváltoztatja a fájl helyét
# seekable() - ellenőrzi, hogy meg-e lehet változtatni a fájl helyét (boolean)
# tell() - visszaadja a fájl helyét
# truncate() - átméretezi a fájlt a megadott méretre
# write() - egy megadott string-et 'ír' a fájlhoz
# writelines() - egy megadott string listát 'ír' a fájlhoz
# writable() - ellenőrzi, hogy 'írható'-e a fájl (boolean)


#az open() metódus 2 paramétert fogad be. fájlnév és mód
#a 4 különböző mód:

# 'r' - read. ez az alap érték. megnyitja 'olvasásra', errort dob ha nem létezik
# 'a' - append. megnyitja a fájlt hozzá-adásra, létrehozza a fájlt ha nem létezik
# 'w' - write. - megnyitja a fájlt 'írásra', létrehozza a fájlt ha nem létezik
# 'x' - create. - 'létrehozza' a megadott fájlt, errort dob ha már létezik


#2 opcionális érték van, hogy hogyan legyen a fájl kezelve ('szöveg mód', és 'bináris mód')

# 't' - text. ez az alap érték. 'szöveges' mód
# 'b' - binary. Bináris mód (pl.: képek)


#így néz ki az open() parancs teljes szintaktissal:

#open("file.tx", rt)
#az "rt"-ben az 'r' - mint 'olvasás', a 't' mint 'szöveges mód'