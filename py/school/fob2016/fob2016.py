import os
import codecs
import math

os.system("cls")

def fob2016 (bemenet, mod):

    data = open(bemenet, mod, encoding = "utf-8").read().replace("\n", ";").split(";")
    lista = list(data) #listaba olvasas
    #print("A fajl listaba olvasva: ", lista)


    indulok = [lista[i] for i in range(0, len(lista), 11)]      # kulon listaba irjuk az indulokat 
    #print("Az indulok: ", indulok)

    print("Az indulok szama: ", len(indulok))


    no = 0
    for nem in lista:
        if nem == "Noi":                                        # megnezzuk hogy a listaban, hanyszor szerepel a 'Noi' szo, hogy kesobb tudjunk szazalekot szamolni a szammal
            no += 1
    no_szazalek = no / (len(indulok) / 100)
    no_szazalek_formazott = "{:.2f}".format(no_szazalek)

    print("A nok szazaleka: ", no_szazalek_formazott, "%")
    print("\n")


    legjobb = [0, 0]                                            # itt taroljuk a legjobb noi versenyzo adatait. elso helyen az ossz pontok, masodik helyen az indexe a listaban
    temp = 0                                                    # pillanatnyi valtozo, ezt hasonlitjuk majd kesobb a legjobb ossz ponttal
    for index,e in enumerate(lista):                            #  V
        if e == "Noi":                                          # lecsekkoljuk, hogy az 'e' helyen no van-e, ha igen akkor az indexevel dolgozunk
            temp = 0
            for pont in lista[index + 2:index + 10]:            # osszeadjuk a pontokat a 'temp' valtozoba
                temp += int(pont)
            if temp > legjobb[0]:                               # megnezzuk, hogy a jelenleg vizsgalt vagy a jelenlegi legjobb jatekosnak van tobb pontja
                legjobb.clear()
                legjobb = [temp, index - 1]                     # eltavolitjuk a jelenlegi legjobbat majd a pontjait taroljuk az elso helyen es a nevenek az indexet a maaodikban

    print("A bajnok noi versenyzo")
    print("Nev:         ", lista[legjobb[1]])
    print("Egyesulet:   ", lista[legjobb[1] + 2])
    print("Osszpont:    ", legjobb[0])





fob2016("fob2016.txt", "r")