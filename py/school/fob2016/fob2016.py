import os
import codecs
import math

os.system("cls")

def fob2016 (bemenet, mod):

    data = open(bemenet, mod, encoding = "utf-8").read().replace("\n", ";").split(";")
    lista = list(data) #listaba olvasas
    #print("A fajl listaba olvasva: ", lista)


    indulok = [lista[i] for i in range(0, len(lista), 11)]
    #print("Az indulok: ", indulok)

    print("Az indulok szama: ", len(indulok))


    nemek = [lista[i] for i in range(1, len(lista), 11)]
    no = 0
    for nem in nemek:
        if nem == "Noi":
            no += 1
    no_szazalek = no / (len(indulok) / 100)
    no_szazalek_formazott = "{:.2f}".format(no_szazalek)

    print("A nok szazaleka: ", no_szazalek_formazott, "%")
    print("\n")


    legjobb = [0, 0]
    temp = 0
    for index,e in enumerate(lista):
        if e == "Noi":
            temp = 0
            for pont in lista[index + 2:index + 10]:
                temp += int(pont)
            if temp > legjobb[0]:
                legjobb.clear()
                legjobb = [temp, index - 1]

    print("A bajnok noi versenyzo")
    print("Nev:         ", lista[legjobb[1]])
    print("Egyesulet:   ", lista[legjobb[1] + 2])
    print("Osszpont:    ", legjobb[0])





fob2016("fob2016.txt", "r")