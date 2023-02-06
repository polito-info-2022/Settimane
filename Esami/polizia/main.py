# Costruiamo una lista di stringhe:
# una stringa per ciascuna riga del file
# comprensiva del \n finale
def leggi_intercettazioni(nome_file):
    with open(nome_file, 'r', encoding='utf-8') as f:
        testo = f.readlines()
    return testo

# testo_censurato è una lista di stringhe contenenti \n
# contiene solo le righe che non sono state cancellate
def censura_testo(testo):
    # trova le righe che devo cancellare
    indici_cancellare = set()
    for i, riga in enumerate(testo):
        if 'bob' in riga or 'arctor' in riga:
            # aggiungi agli indici da cancellare
            # questa riga, le 2 precedenti e le
            # 2 successive: da i-2 a i+2
            for cancella in range(i-2, i+3):
                indici_cancellare.add(cancella)
    # print(indici_cancellare)

    # costruisci il testo censurato senza le righe da cancellare
    testo_censurato = []
    for i, riga in enumerate(testo):
        if i not in indici_cancellare:
            testo_censurato.append(riga)
    return testo_censurato

# calcola la distanza minima
def distanza_polizia(testo):
    indici_nomi = set()
    indici_polizia = set()
    for i,riga in enumerate(testo):
        if 'bob' in riga or 'arctor' in riga:
            indici_nomi.add(i)
        if 'polizia' in riga:
            indici_polizia.add(i)
    # print(indici_nomi, indici_polizia)

    if len(indici_nomi)==0 or len(indici_polizia)==0:
        return None

    distanza = len(testo)+1
    for i_n in indici_nomi:
        for i_p in indici_polizia:
            d = abs(i_n-i_p)
            if d<distanza:
                distanza = d
    return distanza


def main():
    testo = leggi_intercettazioni('intercettazione.txt')
    # print(testo)
    testo_censurato = censura_testo(testo)
    # print(testo_censurato)
    with open('censurato.txt', 'w', encoding='utf-8') as f:
        f.writelines(testo_censurato)
    distanza = distanza_polizia(testo)
    if distanza == None:
        print("Non sei in pericolo")
    else:
        print(f'La parola polizia è stata prounciata a {distanza} righe di distanza dal tuo nome')

main()