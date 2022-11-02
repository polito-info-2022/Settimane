import random

print("PARTITA A BLACK JACK")

# Computer si dà una carta
# salvala in 'carta_computer'
carta_computer = random.randint(1, 10)
print(f'Il computer ha estratto un {carta_computer}')

# Diamo 2 carte al giocatore
# Facciamo giocare il giocatore
# (finché decide di fermarsi oppure supera 21)
# determina variabile 'punti_giocatore'
carta_giocatore_1 = random.randint(1, 10)
carta_giocatore_2 = random.randint(1, 10)
punti_giocatore = carta_giocatore_1 + carta_giocatore_2
print(f"Le tue carte sono: {carta_giocatore_1} e {carta_giocatore_2}")

risposta = input("Vuoi un'altra carta? (s/n) ")
while risposta == 's' and punti_giocatore < 21:
    carta_giocatore = random.randint(1, 10)
    print(f'È uscito un {carta_giocatore}')
    punti_giocatore = punti_giocatore + carta_giocatore

    if punti_giocatore > 21:
        print("Hai superato il 21")
    elif punti_giocatore == 21:
        print("Complimenti, hai raggiunto 21")
    else:
        risposta = input("Vuoi un'altra carta? (s/n) ")

# Facciamo giocare il computer (strategia da definire)
# partendo dalla 'carta_computer' già estratta
# (finché 'decide' di fermarsi oppure supera 21)
# determina variabile 'punti_computer'
punti_computer = carta_computer

if punti_giocatore > 21:
    print("Passo")
else:
    # IPOTESI: Il computer può vedere tutte le carte del giocatore
    while punti_computer < punti_giocatore and punti_computer < 21:
        carta_computer = random.randint(1, 10)
        print(f'Ho estratto un {carta_computer}')
        punti_computer = punti_computer + carta_computer
        if punti_computer > 21:
            print("Ho superato il 21...")

    # IPOTESI: Il computer non può vedere  le carte del giocatore, e mira
    # a raggiungere il 17
    # modificare come segue:
    # while punti_computer<17 and punti_computer<21:

# Verifica chi ha vinto
# sulla base di punti_giocatore e punti_computer
print(f'Punti giocatore={punti_giocatore}, computer={punti_computer}')
if punti_giocatore > 21:
    print('Hai perso')
elif punti_computer > 21:
    print('Hai vinto')
elif punti_giocatore > punti_computer:
    print('Hai vinto')
else:
    print('Hai perso')
