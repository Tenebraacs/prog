def beolvas_allomany(file):
    adatok = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            adatok.append(line.split())
    return adatok

def szamol_fegyor_rab(adatok):
    fegyorok_szama = 0
    rabok_szama = 0
    for adat in adatok:
        azonosito = adat[0]
        if azonosito.startswith('F'):
            fegyorok_szama += 1
        else:
            rabok_szama += 1
    return fegyorok_szama, rabok_szama

def kiir_ltszam(fegyorok_szama, rabok_szama):
    print("2. feladat")
    print(f"Fegyőrök száma: {fegyorok_szama}")
    print(f"Rabok száma: {rabok_szama}\n")

def keres_bicepsz(adatok):
    print("3. feladat")
    azonosito = input("Kérjük be a rab azonosítóját: ")
    bicepsz = None
    for adat in adatok:
        if adat[0] == azonosito:
            bicepsz = float(adat[1].replace(',', '.'))
            break
    if bicepsz is not None:
        print(f"Bicepsz méret: {bicepsz}\n")
    else:
        print("Nincs ilyen azonosítójú rab.\n")

def szamol_elkiser(adatok):
    print("4. feladat")
    azonosito = input("Kérjük be a fegyőr azonosítóját: ")
    elkiser_szam = 0
    for adat in adatok:
        if adat[0].startswith("F") and float(adat[1].replace(',', '.')) > float(adatok[int(azonosito) - 1][1].replace(',', '.')):
            elkiser_szam += 1
    print(f"{azonosito} rabot vihet sétálni.\n")

def van_sosem_siet(adatok):
    print("5. feladat")
    nem_siet = []
    for adat in adatok:
        azonosito = adat[0]
        elkiser_szam = 0
        for adat2 in adatok:
            if adat2[0].startswith("F") and float(adat2[1].replace(',', '.')) <= float(adat[1].replace(',', '.')):
                elkiser_szam += 1
        if elkiser_szam == 0:
            nem_siet.append(azonosito)
    if nem_siet:
        print(f"Nem mehet levegőzni: {', '.join(nem_siet)}\n")
    else:
        print("Minden rab mehet levegőzni!\n")

def szokestanacs(adatok):
    print("6. feladat")
    bicepszek = {}
    for adat in adatok:
        if adat[0].startswith("F"):
            azonosito = adat[0]
            bicepsz = float(adat[1].replace(',', '.'))
            bicepszek[azonosito] = bicepsz
    legnagyobb_bicepszek = sorted(bicepszek.values(), reverse=True)[:3]
    tanacs_tagjai = [azonosito for azonosito, bicepsz in bicepszek.items() if bicepsz in legnagyobb_bicepszek]
    print(f"A tanács tagjainak azonosítója: {', '.join(tanacs_tagjai) if tanacs_tagjai else 'Nincs tanács tagja'}\n")

# Adatok beolvasása
fegyorok = beolvas_allomany('fegyorok.txt')
rabok = beolvas_allomany('rabok.txt')

# Feladat 1: Létszámok kiírása
fegyorok_szama, rabok_szama = szamol_fegyor_rab(fegyorok + rabok)
kiir_ltszam(fegyorok_szama, rabok_szama)

# Feladat 2: Rab bicepszének keresése és kiíratása
keres_bicepsz(rabok)

# Feladat 3: Elkísérhető rabok számának kiírása
szamol_elkiser(fegyorok)

# Feladat 4: Van-e olyan rab, aki soha nem mehet sétálni
van_sosem_siet(rabok)

# Feladat 5: Szökéselőkészítő Tanács tagjainak kiírása
szokestanacs(rabok)
