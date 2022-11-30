import random
from pprint import pprint
from csv import reader

FILE_COMUNI = 'elenco-comuni-italiani.csv'

f = open(FILE_COMUNI, 'r', encoding='utf-8')
f_csv = reader(f, delimiter=';')

next(f_csv)  # salta la prima riga

# nomi_comuni = []
#
# for campi in f_csv:
#     nome_comune = campi[6]
#     nomi_comuni.append(nome_comune)
#
# nomi_comuni.sort()
#
# # pprint(nomi_comuni)
#
# for nome in nomi_comuni:
#     print(nome)

# Quanti comuni ci sono per ciascuna provincia?
# costruisco una lista di liste (2 colonne, comune e provincia)

tabella = []
for campi in f_csv:
    tabella.append([campi[6], campi[11]] )

pprint(tabella)


n_comune = 0
while n_comune<len(tabella):
    provincia = tabella[n_comune][1]
    n_comune = n_comune + 1
    conta = 1
    while n_comune<len(tabella) and tabella[n_comune][1] == provincia:
        n_comune = n_comune+1
        conta = conta + 1
    print(provincia, conta)


# e se le province non fossero in ordine???
random.shuffle(tabella)
pprint(tabella)

viste = []
for i in range(len(tabella)):
    provincia = tabella[i][1]
    if provincia not in viste:
        conta = 0
        for j in range(len(tabella)):
            if tabella[j][1]==provincia:
                conta = conta + 1
        print(provincia, conta)
        viste.append(provincia)


# [
#     [ "Torino", ["Torino", "Moncalieri", "Collegno", "Ivrea"] ],
#     [ "Vercelli", ["Vercelli", "Cavaglià"]],
#     [ "Cuneo",  ["Alba"] ]
# ]


f.close()
