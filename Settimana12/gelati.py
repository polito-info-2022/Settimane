def leggi_gelati(nome_file):
    # costruisce un dizionario
    # chiave : gusto del gelato
    # valore : lista di float corrispondenti alle vendite
    gelati = dict()
    f = open(nome_file, 'r', encoding='utf-8')
    for line in f:
        campi = line.rstrip('\n').split(':')
        gusto = campi[0]
        valori = campi[1:]
        valori = [ float(v) for v in valori ]
        gelati[gusto] = valori
    f.close()
    return gelati

def stampa_tabella(gelati):
    for gusto in sorted(gelati):
        print(f'{gusto:20s}', end='')
        for val in gelati[gusto]:
            print(f'{val:10.2f}', end='')
        print(f'   {sum(gelati[gusto]):10.2f}')

    colonne = len(list(gelati.values())[0])
    print(' '*20, end='')
    for col in range(colonne):
        somma = 0.0
        for gusto in gelati:
            somma = somma + gelati[gusto][col]
        print(f'{somma:10.2f}', end='')

def main():
    gelati = leggi_gelati('icecream.txt')
    print(gelati)
    stampa_tabella(gelati)
main()
