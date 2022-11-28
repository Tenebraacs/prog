print("Hello Phyton!")
ido = "Ma reggel"
szep = "szép az idő"
print(ido)
print(szep)
print(ido + " " + szep)
eso = "Ha esik"
esernyo = "viszek esernyőt"
print(eso + " " + esernyo)
x = 12
print("x értéke: " + str(x))
a = 4
b = 7
c = a + b
print("a értéke: " + str(a))
print("b értéke: " + str(b))
print("c értéke: " + str(c))
#A python - ban nem léteznek konstansok.
print("Adjon meg egy számot:")
szam = int(input())
print("A bekért szám: " + str(szam))
print("A bekért szám típusa: " + str(type(szam)))
import math
pi_erteke = math.pi
print("Add meg a kör sugarát:")
r = float(input())
ker = 2 * r * pi_erteke
ter = r * r * pi_erteke
print("A kör kerülete: " + str(ker))
print("A kör területe: " + str(ter))
gyumolcs = "alma"
print("A gyümölcs neve: " + gyumolcs)
egesz = 10
if egesz == 10:
    print("A szám értéke: " + str(egesz))
kedv = "vidám"
if kedv == "vidám":
    print("A kedvem: " + kedv)
else:
    print("Nem vagyok vidám")
egesz_szam = 12
if egesz_szam == 10:
    print("A szám értéke 10")
elif egesz_szam == 12:
    print("A szám értéke 12")
else:
    print("A szám értéke sem 10 sem 12")
auto = "Volvo"
match auto:
    case "BMW":
        print("Az autó BMW")
    case "Volvo":
        print("Az autó Volvo")
    case other:
        print("Az autó se nem BMW se nem Volvo")
for x in range(x):
    print("A ciklusváltozó: " + str(x))
j = 12
while j < 24:
    print("2... A ciklusváltozó: " + str(j))
    j += 2