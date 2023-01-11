'''
corse = [
    ['A012', (13,0), (13,0), (11,0), (9,0), (0,1), (0,1), (0,16), (0,26)],

    ['A012', [(13,0), (13,0), (11,0), (9,0), (0,1), (0,1), (0,16), (0,26)]],

    { 'autista': 'A012', 'passeggeri': [(13,0), (13,0), (11,0), (9,0), (0,1), (0,1), (0,16), (0,26)] }
]
'''
from operator import itemgetter
from pprint import pprint


def leggi_dati(nome_file):
    corse = []
    fermate = []

    with open(nome_file, 'r', encoding='utf-8') as f:
        prima_riga = f.readline()
        fermate = prima_riga.rstrip('\n').split(',')[2:]

        for riga in f:
            campi = riga.rstrip('\n').split(',')
            autista = campi[0]
            passeggeri = []
            for dato in campi[2:]:
                if dato == '--':
                    passeggeri.append((0, 0))
                elif '/' in dato:
                    numeri = dato.split('/')
                    passeggeri.append((int(numeri[0]), int(numeri[1])))
                elif dato[0] == '-':
                    passeggeri.append((0, int(dato[1:])))
                else:
                    passeggeri.append((int(dato), 0))
            record = {
                'autista': autista,
                'passeggeri': passeggeri
            }
            corse.append(record)
    return corse, fermate


def leggi_nomi(nome_file):
    nomi = {}
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(':')
            nomi[campi[0]] = campi[1].strip()
    return nomi


def calcola_passeggeri_per_autista(corse):
    # { autista: num_passeggeri }
    saliti = {}
    for corsa in corse:
        tot = 0
        for t in corsa['passeggeri']:
            tot = tot + t[0]

        autista = corsa['autista']

        if autista in saliti:
            saliti[autista] = saliti[autista] + tot
        else:
            saliti[autista] = tot

    saliti_ordinati = sorted(saliti.items(), key=itemgetter(1), reverse=True)
    return saliti_ordinati

def main():
    corse, fermate = leggi_dati('dati_aeroporto_torino.csv')
    # pprint(corse)
    nomi = leggi_nomi('database.txt')
    # pprint(nomi)

    saliti_max = 0
    scesi_max = 0

    for fermata in range(len(fermate)):
        saliti = 0
        scesi = 0
        for corsa in corse:
            saliti = saliti + corsa['passeggeri'][fermata][0]
            scesi = scesi + corsa['passeggeri'][fermata][1]

        if saliti > saliti_max:
            saliti_max = saliti
            fermata_saliti_max = fermate[fermata]
        if scesi > scesi_max:
            scesi_max = scesi
            fermata_scesi_max = fermate[fermata]

    print(f'Fermata con max di saliti ({saliti_max}) è {nomi[fermata_saliti_max]}')
    print(f'Fermata con max di scesi ({scesi_max}) è {nomi[fermata_scesi_max]}')

    saliti = calcola_passeggeri_per_autista(corse)
    for autista in saliti:
        print(f'{nomi[autista[0]]} {autista[1]}')

main()
