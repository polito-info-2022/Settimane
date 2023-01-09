def leggi_auto(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')
    f.readline()
    auto = []
    for riga in f:
        campi = riga.rstrip('\n').split(',')
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
    categoria = campi_richiesta[0]
    giorni_richiesti = [int(c) for c in campi_richiesta[1:]]
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
        prenotare = int(input('Quale vuoi prenotare? '))
        auto_scelta = auto_disponibili[prenotare - 1]
        for g in giorni_richiesti:
            auto_scelta['disponibile'][g - 1] = 'A'

    for veicolo in auto:
        print(f'{veicolo["categoria"]},{veicolo["marca"]},{veicolo["modello"]},{veicolo["colore"]},', end='')
        print(','.join(veicolo['disponibile']))


main()
