# Proviamo a gestire un mazzo di carte
from random import randint, shuffle

# mazzo = ['7Q', '3F', 'AP']

VALORI = "2456JQK3A"
SEMI = "PFQC"

print(len(VALORI))

# VALORI = [ '2', '4', '5', '6', 'J', 'Q', 'K', '3', 'A' ]
#
# VALORI[0]

# Crea un mazzo con tutte le carte possibili, inserite in ordine di valore e di seme
mazzo = []
for valore in VALORI:
    for seme in SEMI:
        carta = valore+seme
        mazzo.append(carta)

# Stesso risultato, utilizzando una Comprehension:
# mazzo = [ valore+seme for valore in VALORI for seme in SEMI ]

print(mazzo)


# genera un mazzo CASUALE
# Nota: questo algoritmo non è consigliabile, poiché per riuscire a sistemare gli
# ultimi elementi, bisogna estrarre numerosi valori casuali, finché non si trova
# proprio quello mancante

mazzo2 = []
estrazioni = 0
# for i in range(len(VALORI)*len(SEMI)):
while len(mazzo2) < len(VALORI)*len(SEMI):
    valore = VALORI[randint(0, len(VALORI)-1)]
    seme = SEMI[randint(0, len(SEMI)-1)]
    estrazioni += 1
    carta = valore+seme
    if carta not in mazzo2:
        mazzo2.append(carta)

print(estrazioni, mazzo2)


# provo a rimescolare un mazzo esistente
# L'algoritmo compie una numerosa serie di scambi casuali
# Più è alto il numero di scambi, più sarà mescolato il mazzo
# Il valore 1000 è stabilito "a naso"... non è un criterio esatto

mazzo3 = list(mazzo)

for scambi in range(1000):
    pos1 = randint(0, len(mazzo3)-1)
    pos2 = randint(0, len(mazzo3)-1)

    # scambio tra 2 posizioni utilizzando una variabile intermedia
    # temp = mazzo3[pos1]
    # mazzo3[pos1] = mazzo3[pos2]
    # mazzo3[pos2] = temp

    # scambio tra 2 posizioni scritto in modo "compatto"
    mazzo3[pos1], mazzo3[pos2] = mazzo3[pos2], mazzo3[pos1]

    # a, c = c, a
    # a=c
    # c=a

print(mazzo3)

# pos1 = 2
# pos2 = 6
# temp = '2Q'
# ['2P', '2F', '4Q', '2C', '4P', '4F', '2Q', '4C', '5P', '5F']


# provo a generare un mazzo casuale con solo 36 operazioni

mazzo_partenza = list(mazzo)
mazzo_arrivo = []

while len(mazzo_partenza)>0:
    # scelgo una carta a caso dal mazzo di partenza
    pos = randint(0, len(mazzo_partenza)-1)
    # aggiungo quella carta al mazzo destinazione
    mazzo_arrivo.append(mazzo_partenza[pos])
    # e la cancello dal mazzo iniziale
    mazzo_partenza.pop(pos)

print(mazzo_arrivo)

# uso la funzione random.shuffle()
shuffle(mazzo)
print(mazzo)

