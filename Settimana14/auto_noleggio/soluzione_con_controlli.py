def leggi_auto(nome_file):
    try:
        f = open(nome_file, 'r', encoding='utf-8')
        f.readline()
        auto = []
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            if len(campi) != 11:
                exit("Numero di campi errato nella lettura del file")
            record = {
                'categoria': campi[0],
                'marca': campi[1],
                'modello': campi[2],
                'colore': campi[3],
                'disponibile': campi[4:11]
            }
            auto.append(record)
        f.close()
        return auto
    except OSError:
        exit("Errore nella lettura del file")


def ricerca_auto(auto, categoria, giorni):
    disponibili = []
    for veicolo in auto:
        if veicolo['categoria'] == categoria:
            # categoria ok, devo verificare i giorni
            ok = True
            for g in giorni:
                if veicolo['disponibile'][g - 1] != 'L':
                    ok = False
            if ok:
                disponibili.append(veicolo)
    return disponibili


def main():
    auto = leggi_auto('auto.csv')
    # print(auto)
    richiesta = input('Scegli categoria e giorni: ')
    campi_richiesta = richiesta.split()
    if len(campi_richiesta) < 2:
        exit("Errore: numero di campi insufficiente")
    categoria = campi_richiesta[0]
    try:
        giorni_richiesti = [int(c) for c in campi_richiesta[1:]]
    except ValueError:
        exit("Errore: campo non numerico")
    for g in giorni_richiesti:
        if g < 1 or g > 7:
            exit("Errore: numero del giorno non valido")
    # print(categoria, giorni_richiesti)
    auto_disponibili = ricerca_auto(auto, categoria, giorni_richiesti)
    # print(auto_disponibili)
    if len(auto_disponibili) == 0:
        print("Non ci sono auto disponibili")
    elif len(auto_disponibili) == 1:
        auto_scelta = auto_disponibili[0]
        for g in giorni_richiesti:
            auto_scelta['disponibile'][g - 1] = 'A'
    else:
        print('Le macchine disponibili sono:')
        for indice, macchina in enumerate(auto_disponibili):
            print(f'{indice + 1}) {macchina["marca"]} {macchina["modello"]} colore {macchina["colore"]}')
        try:
            prenotare = int(input('Quale vuoi prenotare? '))
        except ValueError:
            exit("Errore: valore non numerico")
        if prenotare < 1 or prenotare > len(auto_disponibili):
            exit("Errore: valore non valido")
        auto_scelta = auto_disponibili[prenotare - 1]
        for g in giorni_richiesti:
            auto_scelta['disponibile'][g - 1] = 'A'

    for veicolo in auto:
        print(f'{veicolo["categoria"]},{veicolo["marca"]},{veicolo["modello"]},{veicolo["colore"]},', end='')
        print(','.join(veicolo['disponibile']))


main()
