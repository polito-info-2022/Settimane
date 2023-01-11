def leggi_ospiti(nome_file):
    ospiti = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            ospiti.append( {
                'nome': campi[0],
                'tel': campi[1],
                'in': int(campi[2]),
                'out': int(campi[3])
            })
    return ospiti

def cerca_contatti(sospetto, ospiti):
    # cerca il sospetto tra gli ospiti
    ospite_sospetto = None
    for ospite in ospiti:
        if ospite['nome']==sospetto:
            ospite_sospetto = ospite
    if ospite_sospetto == None:
        print(f'{sospetto} non è mai stato nell\'hotel')
        return

    # controllo tutti gli altri
    print(f'Contatti sospetti di {sospetto}')
    trovato = False
    for ospite in ospiti:
        if ospite != ospite_sospetto:
            non_incontrati = ospite_sospetto['out']<ospite['in'] or ospite_sospetto['in']>ospite['out']
            if not non_incontrati:
                print(f'\tContatto con {ospite["nome"]}, tel {ospite["tel"]}')
                trovato = True
    if not trovato:
        print('\tNessun contatto')


def main():
    ospiti = leggi_ospiti('presenze.txt')
    print(ospiti)

    f = open('sospetti.txt', 'r', encoding='utf-8')
    sospetti = f.readlines()
    f.close()
    sospetti = [ s.rstrip('\n') for s in sospetti]
    print(sospetti)

    for sospetto in sospetti:
        cerca_contatti(sospetto, ospiti)

main()
