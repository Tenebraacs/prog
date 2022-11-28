#Az 'a' változónak a 2, karakterét íratja ki mert a nulla az első
a = "Hello világ!"
print(a[1])

#Az 'ananasz' szó kiíratása betűnként
for x in "ananasz":
  print(x)

#Az 'a' változó hosszának kiírása
a = "Szia uram!"
print(len(a))

#Megnézi, hogy a 'free' szó van e a string-ben
#Azt fogja vissza adni, hogy true vagy false (boolean)
txt = "The best things in life are free!"
print("free" in txt)

#Megnézi, hogy a 'free' szó van e a string-ben és az alapján hajt végre egy feltételt
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Megnézi, hogy az 'expensive' szó nincs e jelen a string-ben 
#Azt fogja vissza adni, hogy true vagy false (boolean)
txt = "The best things in life are free!"
print("expensive" not in txt)

#Megnézi, hogy az 'expensive' szó nincs e jelen a string-ben és az alapján hajt végre egy feltételt
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Lekérdezi a 2. és az 5. pozíció közötti betűket. (a 2 és az 5 nem szerepel benne)
b = "Hello, World!"
print(b[2:5])

#Lekérdezi az elejétől az 5. pozícióig a betűket. (az 5 nem szerepel benne)
b = "Hello, World!"
print(b[:5])

#Lekérdezi a 2.-tól a végéig a betűket. (a második nem szerepel benne)
b = "Hello, World!"
print(b[2:])

#Ha negatív számmal adjuk meg a tartományt akkor a végéről indul
b = "Hello, World!"
print(b[-5:-2])

#Nagybetű
a = "Hello, World!"
print(a.upper())

#Kisbetű
a = "Hello, World!"
print(a.lower())

#Ezt fogja vissza adni: 'Hello, World!' (eltünteti a felesleges helyeket)
a = " Hello, World! "
print(a.strip())

#Ez kicseréli a stringet('H' - első) egy másikra('J' - második)
a = "Hello, World!"
print(a.replace("H", "J"))

#Ez szétválasztja a stringet, hogyha megtalálja az adott elválasztást
a = "Hello, World!"
print(a.split("," " "))

#Változókat egyszerűbben is be tudunk illeszteni string-ekbe behelyettesítéssel
darab_szam = 3
targy_szam = 567
ar = 49.95
rendeles = "Szeretnék kérni {} darab, {} számmal ellátott tárgyat {} dollárért."
print(rendeles.format(darab_szam, targy_szam, ar))

#Ha a {}-be beírjuk a változó sorszámát akkor azt fogja kiválasztani, a megadott sorrendből
darab_szam = 3
targy_szam = 567
ar = 49.95
rendeles = "Szeretnék fizetni {2} dollárt, {0} darab tárgyért amelyeket a {1} szám jelöli"
print(rendeles.format(darab_szam, targy_szam, ar))

#Ha egy string-ben szeretnénk amúgy nem megengedett karaktert használni akkor használjuk a \-et
txt = "Mi vagyunk az úgynevezett \"Vikingek\" Északról."
print(txt)

"""
Vannak további string műveletek:

capitalize()	Converts the first character to upper case

casefold()	Converts string into lower case

center()	Returns a centered string

count()	Returns the number of times a specified value occurs in a string

encode()	Returns an encoded version of the string

endswith()	Returns true if the string ends with the specified value

expandtabs()	Sets the tab size of the string

find()	Searches the string for a specified value and returns the position of where it was found

format()	Formats specified values in a string

format_map()	Formats specified values in a string

index()	Searches the string for a specified value and returns the position of where it was found

isalnum()	Returns True if all characters in the string are alphanumeric

isalpha()	Returns True if all characters in the string are in the alphabet

isdecimal()	Returns True if all characters in the string are decimals

isdigit()	Returns True if all characters in the string are digits

isidentifier()	Returns True if the string is an identifier

islower()	Returns True if all characters in the string are lower case

isnumeric()	Returns True if all characters in the string are numeric

isprintable()	Returns True if all characters in the string are printable

isspace()	Returns True if all characters in the string are whitespaces

istitle()	Returns True if the string follows the rules of a title

isupper()	Returns True if all characters in the string are upper case

join()	Joins the elements of an iterable to the end of the string

ljust()	Returns a left justified version of the string

lower()	Converts a string into lower case

lstrip()	Returns a left trim version of the string

maketrans()	Returns a translation table to be used in translations

partition()	Returns a tuple where the string is parted into three parts

replace()	Returns a string where a specified value is replaced with a specified value

rfind()	Searches the string for a specified value and returns the last position of where it was found

rindex()	Searches the string for a specified value and returns the last position of where it was found

rjust()	Returns a right justified version of the string

rpartition()	Returns a tuple where the string is parted into three parts

rsplit()	Splits the string at the specified separator, and returns a list

rstrip()	Returns a right trim version of the string

split()	Splits the string at the specified separator, and returns a list

splitlines()	Splits the string at line breaks and returns a list

startswith()	Returns true if the string starts with the specified value

strip()	Returns a trimmed version of the string

swapcase()	Swaps cases, lower case becomes upper case and vice versa

title()	Converts the first character of each word to upper case

translate()	Returns a translated string

upper()	Converts a string into upper case

zfill()	Fills the string with a specified number of 0 values at the beginning
"""