piano = int(input("A quale piano vuoi andare? "))

if piano!=13:

    if piano <= 12:
        # l'utente ha chiesto un piano basso
        piano_vero = piano
        print('piano basso')
    else:
        # piano alto
        piano_vero = piano - 1
        print('piano alto')

    print('Hai chiesto di andare al piano', piano)
    print('In realtà si tratta del piano "vero"', piano_vero)

else:
    print("Il piano 13 non esiste")
