# ALAPFOGALMAK
#
# osztaly letrehozasa "class" kulcsszoval, ez az OOP szemlelet
# OOP: objektum orientalt paradigma
# A mindennapi eletben osztalyokba soroljuk a dolgokat
# pl.: emberek - nok - ferfiak
#      allatok - emlosok - vizi - szarazfoldi
#      , stb.
# Alapfogalmak: az osztalyok tagjait a kozos TULAJDONSAGOK es
# ============= a kozos VISELKEDES kapcsolja ossze
#   pl.: - kozos tulajdonsag: a szarazfoldi jarmuveknek altalaban van kereke
#        - kozos viselkedes: a nok altalaban sminkelik magukat
#                            a ferfiak altalaban borotvalkoznak (KIVEVE SZABO!!!)
# Osztaly: azonos tulajdonsagokkal, jellemzokkel es viselkedessel rendelkezo
# ======== egyedeket tartalmaz.
# Tulajdonsagokat erteke: adatokban tarolodik
# =======================
# Viselkedes: metodusok, fuggvenyek irjak le.
# ===========
# Osztaly = Adatok(tulajdonsagok ertekei) + Metodusok(viselkedesek)
# =======
# Objektum: az osztaly egy peldanya, pl.: ferfiak kozul a Jozsi
# =========                               nok kozul a Gizi
# Peldanyositas: az a folyamat, amiben az osztalybol objektumot hivunk elo
# ==============


# osztaly letrehozasa "class" kulcsszoval
class MyClass:
    #osztaly szintu adattag, osztaly szintu valtozo
    x = 5

# osztalybol objektumot hozok letre, a folyamat neve: peldanyositas, konstrukcio
p1 = MyClass()
# meghivom az objektumot, hivatkozok "."-al az osztaly valtozojara, az osztaly szintu adattagra
print(p1.x)

#__init__ beepitett fv-t hasznalunk ertekek hozzarendelesehez
# A self parameter az osztaly aktualis peldanyara valo hivatkozas,
# es az osztalyhoz tartozo valtozok eleresere szolgal.
class Person:
    #osztaly szintu metodus
    def __init__(self, name, age):
        self.name = name
        self.age = age

# peldanyositas parameterekkel
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1.name, p1.age)

#__str__ beepitett fv. string tipust allit
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)
print(p1)

#osztaly sajat metodussal, fuggvennyel
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

#peldanyositas: osztalybol objektus jon letre
p1 = Person("John", 36)

#meghivom a sajat metodusomat
p1.myfunc()

#self parameter helyett sajat elso parameter nevet is hasznalhatok az __init__-ben
class Person:
    def __init__(elso_par, name, age):
        elso_par.name = name
        elso_par.age = age

    def myfunc(elso_par):
        print("Hello my name is " + elso_par.name + " my age is ", elso_par.age)

#peldanyositas: osztalybol objektum jon letre
p1 = Person("John", 36)

#meghivom a sajat metodusomat
p1.myfunc()

#objektum tulajdonsaganak modositasa
p1.age = 48
p1.myfunc()
p1.name = "Mike"
p1.myfunc()

#objektum tulajdonsaganak torlese
#   del p1.age
#   p1.myfunc()

#objektum torlese
#   del p1
#   p1.myfunc()