# 1. feladat
with open('vizdat.csv') as fajl:
    forras = fajl.read().splitlines()
adatok = [sor.split(';') for sor in forras]

# 2. feladat
print('2. feladat')
nev = input('Kérek egy nevet: ')
lista = [adat[2]+':'+adat[3]+'-'+adat[4]+':'+adat[5] for adat in adatok if adat[0]==nev]
print('Kölcsönzött: '+', '.join(lista) if lista else 'Nem volt ilyen nevű kölcsönző!')

# 3. feladat
print('\n3. feladat')
idopont = input('Kérek egy időpontot (óra:perc): ')
ido = int(idopont.split(':')[0])*60+int(idopont.split(':')[1])
lista = [adat[1]+', '+adat[0] for adat in adatok if int(adat[2])*60+int(adat[3])<=ido<=int(adat[4])*60+int(adat[5])]
print('Kikölcsönzött járművek: '+'; '.join(lista))

# 4. feladat
osszeg = 0
dijak = []  # érdemes összegyűjteni jármű-díj párosokat, az 5. feladatban kelleni fog
for adat in adatok:
    perc = int(adat[4])*60+int(adat[5]) - (int(adat[2])*60+int(adat[3]))
    if perc % 30 == 0:
        dij = 1500*(perc//30)
    else:
        dij = 1500*((perc//30)+1)
    osszeg += dij
    dijak.append([adat[1], dij])
#print(adat[1], perc, perc//30, perc%30, dij, osszeg)
print('\n4. feladat\nBevétel:', osszeg, 'Ft.')

# 5. feladat
print('\n5. feladat')
jarmuvek_lista = [adat[1] for adat in adatok]
jarmuvek = list(set(jarmuvek_lista))  # csak a járművek listája; az ABC kiírás miatt kell lista, hogy rendezhető legyen
jarmuvek.sort()
lista = [jarmu+' – '+str(jarmuvek_lista.count(jarmu)) for jarmu in jarmuvek]
print('\n'.join(lista))

# 6. feladat
print('\n6. feladat')
osszegek = []  # jármű, összeg
for jarmu in jarmuvek:
    osszeg = sum(dij[1] for dij in dijak if dij[0] == jarmu)
    osszegek.append([jarmu, osszeg])
max_osszeg = max([osszeg[1] for osszeg in osszegek])
lista = [osszeg[0] for osszeg in osszegek if osszeg[1] == max_osszeg]  # csak a legtöbbet fizetett járművek és összeg
print('Fizetett idő:', (max_osszeg/1500)/2, 'óra, járművek:', ', '.join(lista))

# 7. feladat
idok = [[int(adat[2])*60+int(adat[3]), int(adat[4])*60+int(adat[5])] for adat in adatok]  # jármű,kivisz,behoz
kezd = min(ido[0] for ido in idok)  # legelső kivitel
vege = max(ido[1] for ido in idok)  # legutolsó visszahozatal
#print(idok, kezd, vege)
kint = []
jo_percek = []  # azok a percek, amíg az összes jármű kint volt
for perc in range(kezd, vege):  # megnézzük, hogy minden percben hány jármű van kint
    hanyban = 0
    for ido in idok:
        if ido[0] <= perc <= ido[1]:
            hanyban += 1
    #print(perc, hanyban)
    if hanyban == len(jarmuvek):
        jo_percek.append(perc)
#print(jo_percek)
jo_idok = [jo_percek[0]]  # első időpont; a jo idok csak a jó perceket tartalmazzák
for index1 in range(1, len(jo_percek)-1):
    if jo_percek[index1] != jo_percek[index1-1]+1 or jo_percek[index1] != jo_percek[index1+1]-1:
        jo_idok.append(jo_percek[index1])
jo_idok.append(jo_percek[-1])  # utolsó időpont
#print(jo_idok)
kiir = [str(perc//60)+', '+str(perc%60) for perc in jo_idok]
print('\n7. feladat\nAz összes kint van:', ', '.join(kiir))

# 8. feladat
for adat in adatok:  # kellenek a bevezető nullák is, ha nincsenek
    for i in range(2, 6):
        if len(adat[i]) == 1:
            adat[i] = '0' + adat[i]
f_jarmu = [adat[2]+':'+adat[3]+'-'+adat[4]+':'+adat[5]+' : '+adat[0] for adat in adatok if adat[1] == 'F']
fajl = open('fjarmu.txt', 'w')
print('\n'.join(f_jarmu), file=fajl)
fajl.close()
print('\n8. feladat\nA fájl írása megtörtént.')
