from pprint import pprint

FILE_COMUNI = 'elenco-comuni-italiani.csv'

f = open(FILE_COMUNI, 'r', encoding='utf-8')

_ = f.readline()

nomi_comuni = []

for riga in f:
    campi = riga.rstrip('\n').split(';')
    nome_comune = campi[6]
    nomi_comuni.append(nome_comune)

nomi_comuni.sort()

# pprint(nomi_comuni)

for nome in nomi_comuni:
    print(nome)

f.close()
