from random import shuffle

VALORI = "2456JQK3A"
SEMI = "PFQC"

mazzo = []
for valore in VALORI:
    for seme in SEMI:
        carta = valore + seme
        mazzo.append(carta)

shuffle(mazzo)
print(mazzo)

# distribuisci le carte
# ad ogni mano, ciascuno dei due giocatori riceve 3 carte
# Ipotizziamo che ad ogni turno si giochino tutte e 3 le carte, e poi ne vengono distribuite altre 3 "nuove"

while len(mazzo) > 0:
    mano1 = mazzo[0:6:2]  # estrae le carte di posizione 0, 2, 4
    mano2 = mazzo[1:6:2]  # estrae le carte di posizione 1, 3, 5
    mazzo[0:6] = [] # cancella dal mazzo le prime 5 carte (dalla posizione 0 alla posizione 5)

    print('-'.join(mano1), '-'.join(mano2))

# --------------------------------------------------
# Variante : in questo caso si distribuisce una
# sola carta per volta ad ogni mano
# (nota: non gestisce gli "scarti" ma solo la "pesca")
# --------------------------------------------------

# ad inizio partita, distribuisco 3 carte ciascuno
# mano1 = mazzo[0:6:2]
# mano2 = mazzo[1:6:2]
# mazzo[0:6] = []
#
# # while len(mazzo)>0:
# while mazzo:
#     mano1.append(mazzo.pop(0))
#     mano2.append(mazzo.pop(0))
#     print('-'.join(mano1), '-'.join(mano2))
