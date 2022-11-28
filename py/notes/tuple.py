#A 'Tuple' egy olyan lista típus a 4 közül amely nem változtatható, viszont számozott

#A 'Tuple'-re kerek zárójellel hivatkozunk
tuple1 = ("alma", "banán", "meggy", "alma") #megfigyelhetjük, hogy ebben a lista típusban lehetség van duplikált elemeket megadni
print(teszt)

#Az egy értékkel rendelkező 'Tuple'-k első értéke után minednképpen kell egy vessző
tuple2 = ("egy elem",)

#A 'Tuple' értékekre ugyan úgy hivatkozunk mint a listáknál (A zárójel típusa más csak)
print(tuple1[1:3]) #A 2. és a 3. elemet adja vissza

#Ha nagyon muszáj, van lehetőség a 'Tuple'-k megváltoztatására. 

#Megváltoztatjuk az egyik elemet
x = ("apple", "banana", "cherry")
y = list(x) #Itt lemásoljuk a 'Tuple'-t lista formában az 'y' változóra
y[1] = "kiwi" #Itt lista formában megváltoztatjuk a 2. elemet az 'y' változóban
x = tuple(y) #Itt az 'x' változónak megadjuk az 'y' értékét.
#Az eredeti 'Tuple' elveszett és kipótóltuk egy másikkal
print(x)

#Elemek hozzáadása
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) #lemásoljuk lista formában a 'thistuple' változót az 'y'-ra
y.append("orange") #Hozzá adjuk a kívánt elemet
thistuple = tuple(y) #Itt a 'thistuple' változónak megadjuk az 'y' értékét.
#Az eredeti 'Tuple' elveszett és kipótóltuk egy másikkal
#A logika mindegyik változtatásnál ugyan az. Lemásoljuk az eredetit és valamilyen módosított formában helyettesítjük

#Amikor a 'Tuple'-t megalkotjuk azt 'packing'-nak hívjuk
#De a Python-ban lehetőségünk van az 'unpacking'-ra is
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #A '*'-al listaként rögzítünk több elemet. Ha a csillag mondjuk a 'yellow' változón lenne akkor csak addig pakolná az elemeket egy listába amíg a többinek csak 1-1 elem jut.

print(green)
print(yellow)
print(red)

#Lehetőség van a 'Tuple'-k összeadására (vagy szorzására) is
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Az 'index()' parancs ugyan úgy működik mint a listánál

#A 'count()' parancs megszámolja, hogy egy adott elem, hányszor fordul elő
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 8)
x = thistuple.index(8)
print(x)