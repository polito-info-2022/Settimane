"""
TESTA O CROCE

Sviluppare un programma per permettere ad un utente di giocare una partita a "Testa o croce".

L'utente dovrà inizialmente inserire il proprio tentativo, inserendo un carattere 'T' o 'C'.
Il programma in seguito simulerà casualmente il lancio della moneta, determinando se è
uscito 'T' o 'C'.
Infine, sulla base del valore estratto, il programma comunicherà all'utente se ha vinto o perso.
"""

from random import random

# 1. LEGGI IL TENTATIVO DELL'UTENTE
# Output di questa fase: variabile: tentativo 'T' oppure 'C'
tentativo = input("Cosa uscirà (T/C)? ")
tentativo = tentativo.strip().upper()

# controlla che sia T oppure C, altrimenti fermati


# 2. SIMULA IL LANCIO DELLA MONETA
# Output di questa fase: variabile: moneta 'T' oppure 'C'

caso = random()
if caso < 0.5:
    moneta = 'T'
else:
    moneta = 'C'


# 3. DETERMINA SE L'UTENTE HA VINTO

print('Tentativo =', tentativo, 'Moneta =', moneta)

if tentativo == moneta:
    print("Hai vinto!")
else:
    print("Hai perso!")

## ALTERNATIVA  ##

if tentativo == 'T':
    # il giocatore ha detto TESTA
    if moneta == 'T':
        # anche la moneta è TESTA
        print("Hai vinto")
    else: # moneta 'C'
        # purtroppo è uscito CROCE
        print("Hai perso")
else: # 'C'
    if moneta == 'T':
        print("Hai perso")
    else:
        print("hai vinto")

