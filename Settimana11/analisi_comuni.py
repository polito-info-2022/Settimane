from pprint import pprint

NOME_FILE = 'elenco-comuni-italiani.csv'

comuni = []  # lista di tutti i comuni
comuni_per_codice = dict() # array associativo : progressivo -> info comune

with open(NOME_FILE, 'r', encoding='utf-8') as f:
    f.readline()  # ignora la prima riga

    for riga in f:
        campi = riga.rstrip('\n').split(';')

        comune = {
            'progressivo': int(campi[3].strip()),
            'nome_comune': campi[6],
            'nome_provincia': campi[11],
            'nome_regione': campi[10]
        }

        comuni.append(comune)
        # print(comune)
        comuni_per_codice[comune['progressivo']] = comune

pprint(comuni)
pprint(comuni_per_codice)
