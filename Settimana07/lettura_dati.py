def leggi(messaggio, valore_min=1, valore_max=10):
    """
    Leggi un valore intero nell'intervallo specificato (estremi
    compresi). Se il valore non ricade nell'intervallo, viene
    richiesto ripetutamente il re-inserimento.

    :param messaggio: Messaggio da stampare come invito all'inserimento
    :param valore_min: Valore minimo accettabile (intero)
    :param valore_max: Valore massimo accettabile (intero)
    :return: Valore inserito dall'utente, che è garantito essere nell'intervallo richiesto
    """
    riga = input(messaggio)

    while riga=='' or int(riga)<valore_min or int(riga)>valore_max:
        print(f'Valore errato, deve essere tra {valore_min} e {valore_max}')
        riga = int(input(messaggio))

    return int(riga)


g = leggi('giorno: ', 1, 31)
m = leggi('mese: ', 1, 12)
a = leggi('anno: ', valore_min=0, valore_max=2500)
print(f'{g}/{m}')
