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

SEMI = "CQFP"
VALORI = "24567JQK3A"  # in ordine crescente di valore!!!

# 1. Scegli e stampa il seme di briscola
# definisce: briscola = 'C', 'Q', 'F', 'P'
#casuale = int(random()*4)
casuale = randint(0, 3)
briscola = SEMI[casuale]

print(f'La briscola per questa mano è: {briscola}')

# 2. Acquisisci e verifica la giocata 1
# definisce: giocata1 = '3F', 'JP' , 2 caratteri maiuscoli, di cui il primo tra VALORI ed il secondo tra SEMI ****

# IN ALTERNATIVA
# definisce: valore1 = '3', e seme1 = 'Q'
# definisce: valore1 = 2, seme1 = 1  -> SEMI[1]

giocata1 = input('Primo giocatore: ')
giocata1 = giocata1.upper().strip()
if not(len(giocata1) == 2 and giocata1[0] in VALORI and giocata1[1] in SEMI):
#if len(giocata1)!=2 or giocata1[0] not in VALORI or giocata1[1] not in SEMI:
    exit(f"Giocata {giocata1} non valida...")


# 3. Acquisisisci e verifica la giocata 2
# definisce: giocata2 = '3F', 'JP' , 2 caratteri maiuscoli, di cui il primo tra VALORI ed il secondo tra SEMI ****
giocata2 = input('Secondo giocatore: ')

giocata2 = giocata2.upper().strip()
if not(len(giocata2)==2 and giocata2[0] in VALORI and giocata2[1] in SEMI) or giocata2==giocata1:
    exit(f"Giocata {giocata2} non valida...")



# 4. Determina e stampa chi ha vinto
# riceve: briscola, giocata1, giocata2 (corrette e diverse tra loro)
# produce: il vincitore = (1 o 2)

print(f'Avete giocato: {giocata1} e {giocata2}')

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

    # cerca la posizione della carta nell'elenco dei valori
    # poiché tale elenco è ordinato per valori crescenti,
    # la posizione maggiore (più a destra) è vincente
    pos1 = VALORI.find(giocata1[0])
    pos2 = VALORI.find(giocata2[0])
    if pos1 > pos2:
        vincitore = 1
    else:
        vincitore = 2

print(f'Ha vinto il giocatore {vincitore}')

#     biscola = 'Q'
#     giocata1 = 'QP'
# if briscola in giocata1[1]
