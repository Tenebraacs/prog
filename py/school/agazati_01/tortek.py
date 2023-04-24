def tort(szamlalo, nevezo):
    if nevezo == 0:
        print("A nevezo nem lehet nulla!")
    else:
        x = szamlalo / nevezo
        if x > 1:
            print("Ez a tort nagyobb mint egy egesz.")
        elif x == 1:
            print("Ez a tort pontosan egy egesz.")
        else:
            print("Ez a tort kisebb mint egy egesz")


szamlal = int(input("Kerem a szamalot: "))
print("\n")
nevez = int(input("Kerem a nevezot: "))
print("\n")

tort(szamlal, nevez)
print("\n")
