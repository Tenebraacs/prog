print("Válasszon az alábbi opciók közül")
print("1.) Derékszögű háromszög szerkezthető-e az adatokból?")
print("2.) Elsőfokú egyenlet megoldó program")
print("3.) Páros számok 1-121 között")
print("4.) 7-el osztható számok 71-200 között")
print("5.) 7-el osztható, páros számok 71-200 között")
opcio = float(input())
if opcio == 1:
    print("Derékszögű-e a háromszög?")
    A = float(input("Adja meg az 'a' oldal hosszát: "))
    B = float(input("Adja meg a 'b' oldal hosszát: "))
    C = float(input("Adja meg a 'c' oldal hosszát: "))
    if A > C:
        c = A
        b = B
        a = C
    elif B > C:
        c = B
        a = A
        b = C
    else:
        a = A
        b = B
        c = C
    derekszog = a * a + b * b
    if derekszog == c * c:
        print("Ez egy derékszögű háromszög")
    else:
        print("Ez nem egy derékszögű háromszög")
elif opcio == 2:
    print("Az X kiszámítása elsőfokú egyenletben")
    m = float(input("Adja meg az 'm' értéket: "))
    d = float(input("Adja meg az 'b' értéket: ")) #'b' helyett 'd'-t adtam meg hogy ne legyen zavar a kettő változó között
    x = -(d / m)
    print("Az 'x' értéke: " + str(x))
elif opcio == 3:
    print("Az 1 és 121 közötti páros számok:")
    for i in range(1, 121):
        if i % 2 == 0:
            print(i)
elif opcio == 4:
    print("A 71 és 200 között 7-el osztható számok:")
    for i in range(71, 200):
        if i % 7 == 0:
            print(i)
elif opcio == 5:
    print("A 71 és 200 között 7-el osztható, páros számok:")
    for i in range(71, 200):
        if i % 7== 0:
            if i % 2 == 0:
                print(i)
else:
    print("A megadott opció helytelen.")