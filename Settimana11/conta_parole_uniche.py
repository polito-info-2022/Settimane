import operator

TESTO = 'mary.txt'

def estrai_frequenza(coppia):
    return coppia[1]

def lunghezza_parola(coppia):
    return len(coppia[0])

parole_uniche = set()
frequenza_parole = dict()

with open(TESTO, 'r', encoding='utf-8') as f:
    for riga in f:
        parole = riga.rstrip('\n').split()
        for i in range(len(parole)):
            parole[i] = parole[i].lower().strip('.,"?;')

        parole_uniche = parole_uniche.union(set(parole))

        for parola in parole:
            if parola in frequenza_parole:
                frequenza_parole[parola] = frequenza_parole[parola]+1
            else: # prima volta
                frequenza_parole[parola] = 1


print(f'Le parole uniche presenti sono {len(parole_uniche)}')
print('Frequenze delle parole')
print(frequenza_parole)

for parola, frequenza in sorted(frequenza_parole.items(), key=operator.itemgetter(1), reverse=True):
    print(f'{parola:15s} {frequenza:2d}')
