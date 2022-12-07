TESTO = 'mary.txt'

parole_uniche = set()

with open(TESTO, 'r', encoding='utf-8') as f:
    for riga in f:
        parole = riga.rstrip('\n').split()
        for i in range(len(parole)):
            parole[i] = parole[i].lower().strip('.,"?;')
        # print(parole)
        # print(set(parole))

        parole_uniche = parole_uniche.union(set(parole))
        # parole_uniche = parole_uniche.union(parole)

        # for parola in parole:
        #     parole_uniche.add(parola)

        # print(parole_uniche)


print(f'Le parole uniche presenti sono {len(parole_uniche)}')
