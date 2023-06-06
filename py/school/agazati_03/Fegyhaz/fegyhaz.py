# 1. feladat
fegyorok = []
with open('fegyorok.txt') as fajl:
    forras = fajl.read().splitlines()
    for sor in forras:
        fegyorok.append(sor.split(' '))

rabok = []
with open('rabok.txt') as fajl:
    forras = fajl.read().splitlines()
    for sor in forras:
        rabok.append(sor.split(' '))

# 2. feladat
print('\n2. feladat\nFegyőrök száma:', len(fegyorok), '\nRabok száma:', len(rabok))

# 3. feladat
print('\n3. feladat')
rab = input('Kérem egy rab azonosítóját: ')
lista = []
for adat in rabok:
    if adat[0] == rab:
        lista.append(adat[1])
if lista:
    print('Bicepsz méret:', lista[0])
else:
    print('Nincs ilyen azonosítójú rab.')

# 4. feladat
print('\n4. feladat')
fegyor = input('Kérem egy fegyőr azonosítóját: ')
lista = []
for adat in fegyorok:
    if adat[0] == fegyor:
        lista.append(adat[1])
if lista:
    meret = lista[0]
    kiserheti = []
    for adat in rabok:
        if adat[1] < meret:
            kiserheti.append(1)
    if kiserheti:
        print(str(len(kiserheti)) + ' rabot vihet sétálni')
    else:
        print('Nem kísérhet rabot.')
else:
    print('Nincs ilyen fegyőr.')

# 5. feladat
print('\n5. feladat')
max_fegyor = float(fegyorok[0][1].replace(',', '.'))
for adat in fegyorok:
    meret = float(adat[1].replace(',', '.'))
    if meret > max_fegyor:
        max_fegyor = meret
nem_mehet = []
for adat in rabok:
    if float(adat[1].replace(',', '.')) >= max_fegyor:
        nem_mehet.append(adat[0])
if nem_mehet:
    print('Nem mehet levegőzni:', ', '.join(nem_mehet))
else:
    print('Minden rab mehet levegőzni.')

# 6. feladat
for rab in rabok:
    csere = ''
    for karakter in rab[1]:
        if karakter == ',':
            csere += '.'
        else:
            csere += karakter
    rab[1] = float(csere)

rabok.sort(key=lambda e: e[1], reverse=True)
tagok = []
for i in range(3):
    tagok.append(rabok[i][0])
print('\n6. feladat\nA tanács tagjainak azonosítója:', ', '.join(tagok))
