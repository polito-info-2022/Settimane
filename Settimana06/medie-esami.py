# 1.) chiedi quanti esami devono essere considerati per ciascuno
# studente
# memorizzalo in n_esami, che deve essere >= 1

n_esami = int(input("Quanti esami ci sono? "))
while n_esami < 1:
    print("Valore non valido")
    n_esami = int(input("Quanti esami ci sono? "))

# 2.) Acquisisci i voti e calcola le medie
# RIPETI PER CIASCUNO STUDENTE
# Variabile di controllo: 'ancora' Booleana  (scelgo questa)
# Variabile di controllo: 'risposta' Stringa ('S', "N")
ancora = True
while ancora:
    #     2.1) Leggi i suoi voti per calcolare somma_voti
    #     2.1.0) inizializza somma_voti a 0
    #     RIPETI PER n_esami VOLTE
    #         2.1.1) Leggi un voto
    #         2.1.2) aggiornare somma_voti

    print("Inserisci i voti dello studente")
    somma_voti = 0
    for i in range(n_esami):
        voto = int(input(f'Voto numero {i + 1} = '))
        while voto < 18 or voto > 30:
            print("Voto errato")
            voto = int(input(f'Voto numero {i + 1} = '))
        somma_voti = somma_voti + voto

    #     2.2) Calcola e stampa la media
    #     somma_voti / n_esami
    media = somma_voti / n_esami
    print(f"La media è {media}")

    #     2.3) Chiedi se ci sono altri studenti da elaborare
    #         aggiorna 'ancora' in funzione della risposta
    risposta = input("Ci sono ancora studenti? (S/N) ").upper().strip()
    while risposta != 'S' and risposta != 'N':  # risposta in 'SN'
        risposta = input("Ci sono ancora studenti? (S/N) ").upper().strip()
    if risposta == 'S':
        ancora = True
    else:
        ancora = False

#
# VOti esame 1:
#   18
#   25
#   30
# Voti esame 2:
#   28
#   25
#   19
#
# Voti dello Studente 1:
#  18
#  28
#  -> calcola e stampa media
# Voti dello Studente 2:
#  25
#  25
#  -> calcola e stampa media
# Voti dello Studente 3:
#  30
#  19
#  -> calcola e stampa media
#
#
