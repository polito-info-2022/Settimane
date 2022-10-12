piano = int(input("A quale piano vuoi andare? "))

if piano == 13:
    print('Errore, il piano 13 non esiste')
elif piano <= 12:
    piano_vero = piano
else:
    piano_vero = piano - 1

if piano!=13:
    print('Hai chiesto di andare al piano', piano)
    print('In realtà si tratta del piano "vero"', piano_vero)
