import operator
from pprint import pprint
from csv import DictReader

NOME_FILE = 'elenco-comuni-italiani.csv'

comuni = []  # lista di tutti i comuni
comuni_per_codice = dict() # array associativo : progressivo -> info comune

with open(NOME_FILE, 'r', encoding='utf-8') as f:
    reader = DictReader(f, delimiter=';')
    for record in reader:
        comuni.append(record)

def estrai_nome_comune(record):
    return record['Denominazione in italiano']

comuni.sort(key=estrai_nome_comune)

# comuni.sort(key=lambda record: record['Denominazione in italiano'])

comuni.sort(key=operator.itemgetter('Denominazione in italiano'))

pprint(comuni)
