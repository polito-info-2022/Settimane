from operator import itemgetter


def leggi_tassi_cambio(nome_file):
    cambi = {}
    with open( nome_file, "r", encoding='utf-8') as f:
        for riga in f:
            valuta = riga.rstrip('\n').split()[0]
            tasso = float(riga.rstrip('\n').split()[1])
            cambi[valuta] = tasso
    cambi["EUR"] = 1.0
    return cambi


# [ {'nazione', 'valuta', 'prezzo'} , {}, {} ]
def leggi_prezzi(nome_file):
    prezzi = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(';')
            record = {
                'nazione': campi[0],
                'valuta': campi[1],
                'prezzo': float(campi[2])
            }
            prezzi.append(record)
    return prezzi


def main():
    cambi = leggi_tassi_cambio('exchange.txt')
    # print(cambi)

    file_prezzi = input("Nome del file contenente i prezzi: ")
    # file_prezzi= 'iphone13mini.txt'

    prezzi = leggi_prezzi(file_prezzi)
    # print(prezzi)

    # calcolo i prezzi in EUR aggiungendoli ai record della lista
    for prezzo in prezzi:
        prezzo["prezzo_EUR"] = prezzo["prezzo"] * cambi[prezzo["valuta"]]

    # print(prezzi)

    prezzo_minimo = min(prezzi, key=itemgetter('prezzo_EUR'))

    # print(prezzo_minimo)

    print(f'Il paese dove il prodotto costa meno è: {prezzo_minimo["nazione"]}')
    print(f'Prezzo in Euro: {prezzo_minimo["prezzo_EUR"]}')


main()
