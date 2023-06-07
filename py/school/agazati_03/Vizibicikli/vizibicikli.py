def beolvas_allomany(file_nev):
    adatok = []
    with open(file_nev) as file:
        sorok = file.read().splitlines()
        for sor in sorok:
            adatok.append(sor.split(';'))
    return adatok


def keres_nev(adatok):
    keresett_nev = input('Kérem a kölcsönző nevét: ')
    talalat = False
    for adat in adatok:
        nev = adat[0]
        if nev == keresett_nev:
            talalat = True
            elvitel_ora = adat[2]
            elvitel_perc = adat[3]
            visszahoz_ora = adat[4]
            visszahoz_perc = adat[5]
            print(
                f'{nev} aznap {elvitel_ora}:{elvitel_perc} - {visszahoz_ora}:{visszahoz_perc} között vette igénybe a kölcsönző szolgáltatásait.')
    if not talalat:
        print('Nem volt ilyen nevű kölcsönző!')


def keres_idopont(adatok):
    ora_perc = input('Kérem az időpontot óra:perc formátumban: ')
    ora, perc = ora_perc.split(':')
    ora = int(ora)
    perc = int(perc)
    jarmuvek = []
    for adat in adatok:
        elvitel_ora = int(adat[2])
        elvitel_perc = int(adat[3])
        visszahoz_ora = int(adat[4])
        visszahoz_perc = int(adat[5])
        if (elvitel_ora < ora or (elvitel_ora == ora and elvitel_perc <= perc)) and (
                visszahoz_ora > ora or (visszahoz_ora == ora and visszahoz_perc >= perc)):
            jarmuvek.append(adat[1])
    if len(jarmuvek) > 0:
        print(f'A(z) {ora}:{perc} időpontban vízen voltak a következő járművek: {", ".join(jarmuvek)}.')
    else:
        print(f'A(z) {ora}:{perc} időpontban nem voltak járművek vízen.')


def napi_bevetel(adatok):
    bevetelek = {}
    for adat in adatok:
        elvitel_ora = int(adat[2])
        elvitel_perc = int(adat[3])
        visszahoz_ora = int(adat[4])
        visszahoz_perc = int(adat[5])
        ido = (visszahoz_ora * 60 + visszahoz_perc) - (elvitel_ora * 60 + elvitel_perc)
        if ido > 0:
            felperc_ar = 1500 / 30
            fizetendo = int(ido / 30) * 1500
            if ido % 30 != 0:
                fizetendo += felperc_ar
            if adat[1] in bevetelek:
                bevetelek[adat[1]] += fizetendo
            else:
                bevetelek[adat[1]] = fizetendo
    osszeg = sum(bevetelek.values())
    print(f'A napi bevétel: {osszeg} Ft.')


def kolcsonzes_gyakorisag(adatok):
    kolcsonzesek = {}
    for adat in adatok:
        if adat[1] in kolcsonzesek:
            kolcsonzesek[adat[1]] += 1
        else:
            kolcsonzesek[adat[1]] = 1
    for k, v in kolcsonzesek.items():
        print(f'{k} járművet {v} alkalommal kölcsönözték ki aznap.')


def legnagyobb_dij(adatok):
    legnagyobb_dij = 0
    legnagyobb_jarmu = []
    for adat in adatok:
        elvitel_ora = int(adat[2])
        elvitel_perc = int(adat[3])
        visszahoz_ora = int(adat[4])
        visszahoz_perc = int(adat[5])
        ido = (visszahoz_ora * 60 + visszahoz_perc) - (elvitel_ora * 60 + elvitel_perc)
        if ido > 0:
            felperc_ar = 1500 / 30
            fizetendo = int(ido / 30) * 1500
            if ido % 30 != 0:
                fizetendo += felperc_ar
            if fizetendo > legnagyobb_dij:
                legnagyobb_dij = fizetendo
                legnagyobb_jarmu = [adat[1]]
            elif fizetendo == legnagyobb_dij:
                legnagyobb_jarmu.append(adat[1])
    for jarmu in legnagyobb_jarmu:
        print(f'A legnagyobb kölcsönzési díjat ({legnagyobb_dij} Ft) a(z) {jarmu} jármű után fizették.')


def keres_hianyzo_idopontok(adatok):
    idopontok = []
    for adat in adatok:
        elvitel_ora = int(adat[2])
        elvitel_perc = int(adat[3])
        visszahoz_ora = int(adat[4])
        visszahoz_perc = int(adat[5])
        idopontok.append((elvitel_ora, elvitel_perc))
        idopontok.append((visszahoz_ora, visszahoz_perc))
    idopontok.sort()
    hianyzo_idopontok = []
    for i in range(len(idopontok) - 1):
        kezdo_ora, kezdo_perc = idopontok[i]
        veg_ora, veg_perc = idopontok[i + 1]
        if veg_ora > kezdo_ora or (veg_ora == kezdo_ora and veg_perc - kezdo_perc > 30):
            hianyzo_idopontok.append((kezdo_ora, kezdo_perc, veg_ora, veg_perc))
    for idopont in hianyzo_idopontok:
        print(f'{idopont[0]}:{idopont[1]} - {idopont[2]}:{idopont[3]}')


def rongalas_jelentes(adatok):
    rongalasok = {}
    for adat in adatok:
        if adat[1] == 'FF':
            elvitel_ora = int(adat[2])
            elvitel_perc = int(adat[3])
            visszahoz_ora = int(adat[4])
            visszahoz_perc = int(adat[5])
            rongalasok[adat[0]] = f'{elvitel_ora}:{elvitel_perc}-{visszahoz_ora}:{visszahoz_perc}'
    with open('fjarmu.txt', 'w') as file:
        for nev, idoszak in rongalasok.items():
            file.write(f'{idoszak} : {nev}\n')


adatok = beolvas_allomany('vizdat.csv')

# Feladat 2
keres_nev(adatok)

# Feladat 3
keres_idopont(adatok)

# Feladat 4
napi_bevetel(adatok)

# Feladat 5
kolcsonzes_gyakorisag(adatok)

# Feladat 6
legnagyobb_dij(adatok)

# Feladat 7
keres_hianyzo_idopontok(adatok)

# Feladat 8
rongalas_jelentes(adatok)
