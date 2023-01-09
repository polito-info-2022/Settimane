# Memorizziamo i dati della classifica in un dizionario
# chiave : nome della squadra
# valore : dizionario usato come record { 'GIOCATE', 'PUNTI', 'Q', 'PF', 'PS' }
from pprint import pprint


def crea_risultati(nome_file):
    risultati = dict()

    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            nomi_squadre = riga.rstrip('\n').split(':')[0]
            punteggi = riga.rstrip('\n').split(':')[1]
            squadra1 = nomi_squadre.split('-')[0].strip()
            squadra2 = nomi_squadre.split('-')[1].strip()
            punti1 = int(punteggi.split('-')[0])
            punti2 = int(punteggi.split('-')[1])

            if punti1>punti2:
                pp1 = 3
                pp2 = 1
            elif punti1==punti2:
                pp1 = 2
                pp2 = 2
            else:
                pp1 = 1
                pp2 = 3

            if squadra1 in risultati:
                risultati[squadra1]['GIOCATE'] = risultati[squadra1]['GIOCATE']+1
                risultati[squadra1]['PUNTI'] = risultati[squadra1]['PUNTI']+pp1
                risultati[squadra1]['PF'] = risultati[squadra1]['PF']+punti1
                risultati[squadra1]['PS'] = risultati[squadra1]['PS']+punti2
            else:
                risultati[squadra1] = { 'GIOCATE': 1, 'PUNTI':pp1, 'PF':punti1, 'PS':punti2 }

            if squadra2 in risultati:
                risultati[squadra2]['GIOCATE'] = risultati[squadra2]['GIOCATE']+1
                risultati[squadra2]['PUNTI'] = risultati[squadra2]['PUNTI']+pp2
                risultati[squadra2]['PF'] = risultati[squadra2]['PF']+punti2
                risultati[squadra2]['PS'] = risultati[squadra2]['PS']+punti1
            else:
                risultati[squadra2] = { 'GIOCATE': 1, 'PUNTI':pp2, 'PF':punti2, 'PS':punti1 }

    for squadra in risultati:
        risultati[squadra]['Q'] = risultati[squadra]['PF']/risultati[squadra]['PS']

    return risultati

def main():
    risultati = crea_risultati('torneo.txt')
    pprint(risultati)

main()
