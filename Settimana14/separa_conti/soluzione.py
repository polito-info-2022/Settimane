# { nome prodotto: [quantità, prezzo], nome prodotto: [quantità, prezzo] , ... }
def leggi_scontrino(nome_file):
    scontrino = dict()
    with open(nome_file, 'r', encoding='utf=8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            prodotto = campi[0]
            prezzo = float(campi[1])

            if prodotto in scontrino:
                scontrino[prodotto][0] = scontrino[prodotto][0] + 1
            else:
                scontrino[prodotto] = [ 1, prezzo ]
    return scontrino

def leggi_lista(nome_file):
    lista = dict()
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            lista[ campi[0] ] = int(campi[1])
    return lista

def main():
    scontrino = leggi_scontrino('scontrino.csv')
    # print(scontrino)
    lista = leggi_lista('lista.csv')
    # print(lista)

    totale = 0.0
    for prodotto in scontrino:
        totale = totale + scontrino[prodotto][1] * scontrino[prodotto][0]

    print(f'Totale speso: {totale:.2f} euro')

    dovuto = 0.0
    for prodotto in lista:
        if prodotto in scontrino:
            qta = min(lista[prodotto], scontrino[prodotto][0])
            dovuto = dovuto + qta * scontrino[prodotto][1]

    print(f'Totale dovuto: {dovuto:.2f} euro')

    print('Prodotti mancanti:')
    for prodotto in lista:
        if prodotto not in scontrino:
            print(f'{lista[prodotto]} {prodotto}')
        else:
            if scontrino[prodotto][0] < lista[prodotto]:
                manca = lista[prodotto] - scontrino[prodotto][0]
                print(f'{manca} {prodotto}')

main()
