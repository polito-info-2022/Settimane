# converti una lista di stringhe in una lista di numeri
# [ '3', '99']  --> [ 3, 99 ]

# MODIFICA LA LISTA RICEVUTA COME PARAMETRO
def str_to_int(valori):
    for i in range(len(valori)):
        valori[i] = int(valori[i])


# NON MODIFICA IL PARAMETRO, RESTITUISCE UNA NUOVA LISTA
def nuova_str_to_int(valori):
    nuova = []
    for v in valori:
        nuova.append(int(v))
    return nuova

    # oppure: nuova = [ int(v) for v in valori ]


dati = ['3', '99']
print(dati)
str_to_int(dati)
print(dati)

dati2 = ['3', '99']
print(dati2)
dati_nuovi = nuova_str_to_int(dati2)
print(dati2)
print(dati_nuovi)


# --------------------

# analizziamo le differenze tra "modificare la lista ricevuta" e "creare una lista diversa, 'perdendo' l'alias
def aggiungi(valori, numero):
    # valori = valori + [numero]
    valori.append(numero)


numeri = [1, 2, 3, 4]
aggiungi(numeri, 5)
print(numeri)
