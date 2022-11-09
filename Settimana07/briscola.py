"""
Si scriva un programma Python che permetta di valutare il vincitore di una mano
di una partita a Briscola tra due giocatori.

Ipotizziamo che il programma decida automaticamente (in modo casuale) il "seme di briscola", e lo
stampi come informazione iniziale. Il seme è codificato da una delle lettere C, Q, F, P.

I due utenti inseriscono poi ciascuno la carta giocata, sotto forma di stringa, che contiene
il valore seguito dal seme. I valori delle carte sono: A 2 3 4 5 6 7 J Q K. Il valore delle carte
è crescente, con l'eccezione del 3 (che viene dopo il K) e dell'A (che vien dopo il 3).

Il primo giocatore gioca una carta, il cui seme definisce il seme della mano di gioco.
Il secondo giocatore può giocare una carta di un seme diverso (e quindi perde), oppure
una carta dello stesso seme (ed in tal caso vincerà colui che ha giocato la carta più alta).
Eccezione: le carte il cui seme è pari al "seme di briscola" vincono sempre sulle carte di ogni altro seme.

Il programma, dopo avere stampato il seme di briscola scelto, accetterà la giocata del primo giocatore e del
secondo giocatore. Ogni giocata sarà quindi una stringa di due caratteri (es.: 3Q, JF, ...).
Il programma accetterà sia lettere maiuscole che minuscole, e verificherà la correttezza del dato immesso.

Se i dati immessi sono corretti, il programma determinerà il vincitore della mano, stampando "Vince
giocatore 1" oppure "Vince giocatore 2".

"""
from random import random, randint

# definizione di costanti visibili globalmente
SEMI = "CQFP"
VALORI = "24567JQK3A"  # in ordine crescente di valore!!!
N_MANI = 3


def main():
    # 1. Scegli e stampa il seme di briscola
    briscola = scegli_seme_briscola()
    print(f'La briscola per questa mano è: {briscola}')

    vittorie1 = 0
    vittorie2 = 0
    punti1 = 0
    punti2 = 0

    for mano in range(N_MANI):

        print(f'Mano di gioco numero {mano+1}')

        # 2. Acquisisci e verifica la giocata 1
        giocata1 = leggi_giocata("Primo")

        # 3. Acquisisci e verifica la giocata 2
        giocata2 = leggi_giocata("Secondo")

        # 4. Determina e stampa chi ha vinto
        print(f'Avete giocato: {giocata1} e {giocata2}')
        vincitore = determina_vincitore(briscola, giocata1, giocata2)

        print(f'Ha vinto il giocatore {vincitore}')

        if vincitore==1:
            vittorie1 = vittorie1+1
            punti1 = punti1 + punti_carta(giocata1)+ punti_carta(giocata2)
        else:
            vittorie2 = vittorie2+1
            punti2 = punti2 + punti_carta(giocata1)+ punti_carta(giocata2)

    print(f'Punteggio finale: {punti1} a {punti2}')


def leggi_giocata(nome_giocatore):
    """
    Acquisisce una giocata di un giocatore, che deve immettere una carta valida. Se la carta non è valida,
    viene ri-chiesta ripetutatmente.

    :param nome_giocatore: nome descrittivo del giocatore
    :return: stringa di 2 caratteri che rappresenta la giocata
    """
    giocata = input(f'{nome_giocatore} giocatore: ')
    giocata = giocata.upper().strip()
    while not (len(giocata) == 2 and giocata[0] in VALORI and giocata[1] in SEMI):
        print(f"Giocata {giocata} non valida...")
        giocata = input(f'{nome_giocatore} giocatore: ')
        giocata = giocata.upper().strip()
    return giocata


def determina_vincitore(briscola, giocata1, giocata2):
    """
    Determina chi sia il vincitore di una determinata mano di gioco.

    :param briscola: stringa di 1 carattere che rappresenta il seme di briscola della partita
    :param giocata1: stringa di 2 caratteri che rappresenta la carta giocata dal primo giocatore
    :param giocata2: stringa di 2 caratteri che rappresenta la carta giocata dal secondo giocatore
    :return: il vincitore della mano, come valore intero 1 o 2
    """

    # se uno ha giocato briscola e l'altro no, vince
    if giocata1[1] == briscola and giocata2[1] != briscola:
        vincitore = 1
    elif giocata2[1] == briscola and giocata1[1] != briscola:
        vincitore = 2
    elif giocata1[1] != giocata2[1] and (giocata1[1] != briscola and giocata2[1] != briscola):
        # due semi diversi, nessuno briscola
        vincitore = 1
    else:
        # stesso seme (che sia briscola o no, non importa)

        # cerca la posizione della carta nell'elenco dei valori:
        # poiché tale elenco è ordinato per valori crescenti,
        # la posizione maggiore (più a destra) è vincente
        pos1 = VALORI.find(giocata1[0])
        pos2 = VALORI.find(giocata2[0])
        if pos1 > pos2:
            vincitore = 1
        else:
            vincitore = 2

    return vincitore


def scegli_seme_briscola():
    casuale = randint(0, 3)
    briscola = SEMI[casuale]
    return briscola


def punti_carta(carta):
    """
    Data una carta, determina il suo valore numerico in punti

    :param carta: stringa di 2 caratteri che contiene una carta giocata
    :return: il valore di tale carta (tra 0 e 11)
    """
    valore = carta[0]
    if valore=='J':
        return 2
    elif valore=='Q':
        return 3
    elif valore=='K':
        return 4
    elif valore=='3':
        return 10
    elif valore=='A':
        return 11
    else:
        return 0


main()
