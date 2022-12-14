




def leggi_occorrenze(nome_file):
    # occorrenze = []
    # lista di tutte le occorrenze delle parole
    # ciascuna occorrenza è un dict con i campi 'pag' e 'parola'

    occorrenze = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for line in f:
            campi = line.rstrip('\n').split(':')
            occorrenza = {
                'pag': int(campi[0]),
                'parola': campi[1]
            }
            occorrenze.append(occorrenza)
    return occorrenze


def costruisci_indice(occorrenze):
    # indice
    # dizionario, con chiave: parola, e valore: set di numeri di pagina

    indice = {}

    for occorrenza in occorrenze:
        if occorrenza['parola'] not in indice:
            # parola vista per la prima volta
            indice[occorrenza['parola']] = { occorrenza['pag'] }
        else:
            # parola già vista
            indice[occorrenza['parola']].add(occorrenza['pag'])
    return indice


def stampa_indice(indice):
    for parola in sorted(indice):
        print(f'{parola}: ', end='')
        pagine = sorted(indice[parola])
        pagine_s = [ str(p) for p in pagine ]
        print(', '.join(pagine_s))




def main():
    occorrenze = leggi_occorrenze('indexdata.txt')
    print(occorrenze)

    indice = costruisci_indice(occorrenze)
    print(indice)

    stampa_indice(indice)

main()
