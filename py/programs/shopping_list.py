print("Üdvözlöm a Naza által kifejlesztett hiper-szuper bevásárló lista programban")
print("Ebben a programban lehetősége lesz bármilyen hiper-szuper bevásárló listát létre hozni.")
print("Először ismerje meg a lista kezeléshez használandó parancsokat")
print("!!!FONTOS!!!")
print("Először írja be a parancsot, nyomjon egy entert és utána írja be a kívánt műveletet")
print("'list' - lekéri a lista tartalmát")
print("'add' - hozzá tud adni a listához")
print("'remove' - el tudja távolítani a lista egyik elemét (utána a program megkérdezi, hogy sorszám vagy név alapján)")
print("'change' - meg tudja változtatni a lista egyik elemét")
print("'clear' - ki tudja törölni az egész lista tartalmát")
print("'exit' - kilépés a programból")

nazalist = []
exit = False
while exit == False:
    print("Írja be a kívánt parancsot")
    choice = input(">  ")
    if choice == "list":
        print("Az ön listájának a tartalma:")
        for x in nazalist:
            print(x)
    elif choice == "add":
        print("A végére vagy a lista közé szeretne beilleszteni?")
        print("1.) Végére")
        print("2.) Közé")
        add_choice = int(input(">  "))
        if add_choice == 1:
            add_exit = False
            while add_exit == False:
                print("Írja be a hozzáadni kívánt dolgot a listához")
                add = input(">  ")
                nazalist.append(add)
                print("Sikeresen hozzáadva!")
                print("Szeretne hozzáadni még a listához? (igen/nem)")
                add_choice2 = input(">  ")
                if add_choice2 == "igen":
                    add_exit = False
                elif add_choice2 == "nem":
                    add_exit = True
                else:
                    print("A megadott opció helytelen")
        elif add_choice == 2:
            add_exit = False
            while add_exit == False:
                print("Írja be a lista sorszámát ahova be szeretné illeszteni.")
                add_num = int(input(">  ")) - 1
                print("Írja be a hozzáadni kívánt dolgot a listához")
                add = input(">  ")
                nazalist.insert(add_num, add)
                print("Sikeresen hozzáadva!")
                print("Szeretne hozzáadni még a listához? (igen/nem)")
                add_choice2 = input(">  ")
                if add_choice2 == "igen":
                    add_exit = False
                elif add_choice2 == "nem":
                    add_exit = True
                else:
                    print("A megadott opció helytelen")
        else:
            print("A megadott opció helytelen")
    elif choice == "remove":
        print("Sorszám vagy név alapján szeretne elemeket eltávolítani?")
        print("1.) Sorszám")
        print("2.) Név")
        remove_choice = int(input(">  "))
        if remove_choice == 1:
            remove_exit = False
            while remove_exit == False:
                print("Írja be az eltávolítani kívánt elem sorszámát")
                remove = int(input(">  ")) - 1
                nazalist.pop(remove)
                print("Sikeresen eltávolítva!")
                print("Szeretne még eltávolítani a listából? (igen/nem)")
                remove_choice2 = input(">  ")
                if remove_choice2 == "igen":
                    remove_exit = False
                elif remove_choice2 == "nem":
                    remove_exit = True
                else:
                    print("A megadott opció helytelen")
        elif remove_choice == 2:
            remove_exit = False
            while remove_exit == False:
                print("Írja be az eltávolítani kívánt elemet")
                remove = input(">  ")
                if remove in nazalist:
                    nazalist.remove(remove)
                    print("Sikeresen eltávolítva!")
                    print("Szeretne még eltávolítani a listából? (igen/nem)")
                    remove_choice2 = input(">  ")
                    if remove_choice2 == "igen":
                        remove_exit = False
                    elif remove_choice2 == "nem":
                        remove_exit = True
                    else:
                        print("A megadott opció helytelen")
                else:
                    print("A megadott elem nem létezik ebben a listában")
                    remove_exit = True
        else:
            print("A megadott opció helytelen")
    elif choice == "change":
        change_exit = False
        while change_exit == False:
            print("Adja meg a változtatni kívánt elem sorszámát!")
            change_num = int(input(">  ")) - 1
            print("Adja meg, hogy mit szeretne a(z) '" + nazalist[change_num] + "' helyére írni!")
            print("Nem ezt akarta kiválasztani? Csak írjon egy '!' és előröl kezdheti")
            change = input(">  ")
            if change == "!":
                print("Írja be a parancsot újra az újrakezdéshez!")
            else:
                nazalist[change_num] = change
                print("Sikeres megváltoztatás!")
                print("Szeretne még eltávolítani a listából? (igen/nem)")
                change_choice = input(">  ")
                if change_choice == "igen":
                    change_exit = False
                elif change_choice == "nem":
                    change_exit = True
                else:
                    print("A megadott opció helytelen")
                
    elif choice == "clear":
        x = 10
    elif choice == "exit":
        exit = True
    else:
        print("A megadott opció helytelen")
