### Órai feladat: - írd meg az "SuperBowl" paraméteres függvényt,
### =============   ami két paraméterrel rendelkezik: "bemenet", "mod"
###               - olvasd be a "SuperBowl.txt" állományt egy listába, majd ezt dolgozd fel:
###               - írd ki a a képernyőre, hogy a "Washington Redskins" hányszor győzött
###               - írd ki a a képernyőre, hogy a "Dallas Cowboys" hányszor vesztett
###               - írd ki a a képernyőre, hogy a "Kansas City Chiefs" győzött-e
###               - válaszd ki, hogy a "Tampa Stadium" hanyadik helyen van a listában
###               állományod neve: "superbowl.py", ezt kell feltöltened ide

import os
import codecs
import math

os.system("cls")

def SuperBowl (bemenet, mod):
    ########################################################################
    # I. Input fajl beolvasas, a feladatoknak megfelelo listak elkeszitese #
    ########################################################################

    ### 1.) beolvasas, magyar karaktertabla, "\n" csereje ","-re, hasitas ";" szerint
    data = open(bemenet, mod, encoding = "utf-8").read().replace("\n", ";").split(";")
    lista = list(data)
    #print("A fajl adatai listaba olvasva: ", lista)

    # 2.) a gyoztesek listaja
    gyoztes_lista = [lista[i] for i in range(10, len(lista), 8)]
    #print("A gyoztesek listaja: ", gyoztes_lista)

    # 3.) a vesztesek listaja
    vesztes_lista = [lista[i] for i in range(12, len(lista), 8)]
    #print("A vesztesek listaja: ", vesztes_lista)

    print("==================================================")

    # 4.) az eredmeny, gyoztes pont, vesztes pont listak:
    # ===================================================
    # 4.1 eredmeny lista:
    # ===================
    eredmeny_lista = [lista[i] for i in range(11, len(lista), 8)]
    #print("Az eredmenyek listaja: ", eredmeny_lista)

    # 4.2 gyoztes pont lista:
    # =======================
    # 4.2.1 eredmeny lista hasitasa "-" szerint
    eredmeny_lista_hasitott = []
    for i in eredmeny_lista:
        eredmeny_lista_hasitott.append(i.split("-"))
    #print("Az eredmenyek hasitott listaja: ", eredmeny_lista_hasitott)

    # 4.2.2 A hasitassal listak listaja keletkezik, ennek elemere hivatkozas:
    #    peldaul a 0. indexu lista 0. indexu eleme:
    #print("A 0. indexu, es 0. indexu gyoztes pont: ", eredmeny_lista_hasitott[0][0])

    # 4.2.3 gyoztes pont lista:
    gyoztes_pontok_lista = []
    for i in eredmeny_lista_hasitott:
        gyoztes_pontok_lista.append(i[i])
    #print("A gyoztes pontok listaja: ", gyoztes_pontok_lista)

    # 4.2.4 vesztes pont lista:
    # =========================
    vesztes_pontok_lista = []
    for i in eredmeny_lista_hasitott:
        vesztes_pontok_lista.append(i[i])
    #print("A vesztes pontok listaja: ", vesztes_pontok_lista)

    print("==================================================")

    # Nezoszam es sorszam lista:
    # ==========================
    nezoszam_lista = [lista[i] for i in range(15, len(lista), 8)]
    #print("nezoszam_lista", nezoszam_lista)
    sorszam_lista = [lista[i] for i in range(8, len(lista), 8)]
    #print("sorszam_lista", sorszam_lista)

    print("==================================================")

    ###############################
    # II. A feladatok elkeszitese #
    ###############################

    # 1.) a "Washington Redskins" hanyszor gyozott
    WR_gyoz_darab = gyoztes_lista.count("Washingtons Redskins")
    print("A Washington Redskins ", WR_gyoz_darab, " alkalommal gyozott.")

    print("==================================================")

    # 2.) a "Dallas Cowboys" hanyszor vesztett
    DC_veszit_darab = vesztes_lista.count("Dallas Cowboys")
    print("A Dallas Cowboys ", DC_veszit_darab, " alkalommal veszitett.")

    print("==================================================")

    # 3.) a "Kansas City Chiefs" gyozott-e
    van = False
    for i in gyoztes_lista:
        if i == "Kansas City Chiefs":
            van = True
            #print("van", van)
            break
    if van == True:
        print("A Kansas City Chiefs-nek van gyoztes meccse.")

    print("==================================================")

    # 4.) a "Tampa Stadium" hanyadik helyen vam a listaban
    for index, elem, in enumerate(lista):
        if elem == "Tampa Stadium":
            print("A listaban ", index, " indexen all a ", elem, ", a lista ", index + 1, ". helyen")

    print("==================================================")

    # 5.) az atlagos pontkulonbseg a ket csapat kozott
    gyoztes_pontok_osszege = sum(map(int, gyoztes_pontok_lista))
    vesztes_pontok_osszege = sum(map(int, vesztes_pontok_lista))
    pontkulonbseg          = gyoztes_pontok_osszege - vesztes_pontok_osszege
    listahossz             = len(gyoztes_pontok_lista)
    atlagos_pontkulonbseg  = round(pontkulonbseg / listahossz, ndigits = 1)
    print("Az atlagos pontkulonbseg a ket csapat kozott: ", atlagos_pontkulonbseg)

    print("==================================================")

    # 6.) melyik donton volt a legtobb nezo
    max_nezoszam = max(map(int,nezoszam_lista))
    print("A maximalis nezoszam: ", max_nezoszam)

    print("==================================================")

SuperBowl("SuperBowl.txt", "r")
print("\n")