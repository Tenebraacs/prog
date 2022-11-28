#A lista az egyik leggyakrabban használt adattároló típus. Értékei változtathatóak, számozottak és duplikálhatóak.

#A listára kapcsos zárójellel hivatkozunk
lista1 = ["alma", "banán", "meggy", "ananász", "körte", "dinnye", "alma"]
print(lista1)

#A listának az elemeihez több féle képpen férhetünk hozzá. Most a fent létrehozott listát használom példának.

print(lista1[0]) #A lista 1. eleméhez férünk hozzá
print(lista1[-1]) #A lista utolsó eleméhez férünk hozzá
#Ez mind műdökik negatív indexeléssel is \/
print(lista1[2:5]) #A 3.-tól az 5.-ig elemig íratjuk ki. Az utolsó 5 (az az a 6. elem) NEM lesz kiírva
print(lista1[:5]) #Az elejétől az 5.-ig elemig ír ki mindent. (6. elem NEM része, az az az 5-ös sorszám)
print(lista1[2:]) #A 3. elemtől a végéig írja ki.

#A lista elemeinek megváltoztatásához meg kell idézni a változtatni kívánt elemet
lista1[0] = "gránátalma" #Az 1. elemet cseréljük ki
lista1[2:4] = ["cseresznye", "kiwi"] #A 3. és a 4. elemet cseréljük ki a megadott elemekkel
lista1[4:] = ["mangó"] #2 értéket cserélünk ki 1 értékre

#A listába lehetőségünk van beilleszteni dolgokat anélkül, hogy valamit átírnánk
lista1.insert(2, "mandarin") #A 3. helyre illesztjük be az elemet

#A lista végére az 'append()' parancsal tudunk beilleszteni dolgokat
lista1.append("kifli")

#Az 'extend()' paranccsal nem csak listákat de tuple, dictionary, set és lista elemeket is be tudunk illeszteni listánba
tuple1 = ("datolya", "mangó")
lista1.extend(tuple1)
print(lista1)

#A 'remove()' paranccsal egy megadott elemt tudunk eltávolítani a listából (az első eshetőséget amit talál a sorrendben, azt fogja törölni)
lista1.remove("mangó") 
print(lista1)

#A 'pop()' parancs sorszám szerint töröl ezért sokkal pontosabb mint a 'remove()'
lista1.pop(5) #A 6. elem után töröl mindent
lista1.pop() #Az utolsó elemet törli ki

#A 'del' parancs ugyan azzal a tulajdonságokkal bír mint a 'pop()', csak ezzel az egész listát törlöd (nem csak a tartalmát)
del lista1[0] #Az 1. elemet törli ki
lista2 = [1, 2, 3]
del lista2 #Létrehoztam még egy listát, hogy ne a fő listánkat töröljük, de a 'lista2' már nem létezik

#A 'clear()' parancs az egész lista tartalmát kitörli
lista1.clear()

#Lehetőségünk van a listákat rendezni (CSAK AKKOR HA UGYAN AZ AZ ÉRTÉK TÍPUS):

#ABC sorrend szerint
list3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(list3)
list3.sort()
print(list3)

#Matematikailag (növekvő sorrend)
list4 = [100, 50, 65, 82, 23]
print(list4)
list4.sort()
print(list4)

#Megfordított logike
list5 = [100, 50, 65, 82, 23]
print(list5)
list5.sort(reverse = True)
print(list5)

#Egyedi logika (ez esetben, hogy melyik szám van közelebb 50-hez)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#A sorrendbe rakás érzékeny a nagybetűkre. Erre egy egyszerű megoldás, hogy csak a betűket vegye figyelembe:
thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort()
print(thislist2)
thislist2.sort(key = str.lower)
print(thislist2)

#A lista teljes megfordítása: 'reverse()'
thislist3 = [1, 2, 3, 7, 5, 3, 3]
thislist3.reverse()
print(thislist3)

#A 'copy()' paranccsal teljes le tudjuk másolni a listát. Azért nem elég az '=' mert ha az egyik lista változik akkor a másik is megfog
my_list = ['cat', 0, 6.7]
new_list = my_list.copy()

#Az 'index()' parancs vissza adja az adott elem sorszámát
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#A 'count()' parancs ugyan úgy működik mint a 'Tuple'-nél

"""
Van a listának egy kissé komplexebb és helyenként jobb változata.
Az 'Array'-eket a nagyobb adatmennyiségekhez használjuk. Az 'Array' lényegében egy egy adattípust
tartalmazó lista, amivel könnyebbek a matematikai műveletek és nagyobb mennyiségeket jobban kezel.
Ahhoz, hogy működjön importálnunk kell egy array könyvtárat. Erre a W3schools a NumPy-t ajánlja.
"""