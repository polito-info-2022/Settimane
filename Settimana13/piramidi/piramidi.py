# Struttura dati: tabella 2-D di numeri interi (lista di liste)
from pprint import pprint


def leggi_tabella(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')
    mappa = []
    for line in f:
        numeri = line.rstrip('\n').split(' ')
        numeri = [int(n) for n in numeri]
        mappa.append(numeri)
    f.close()
    return mappa


def cerca_vette(mappa):
    """
    Data una mappa, identifica tutte le vette
    :param mappa:
    :return: una lista di tuple corrispondenti alle vette, ciascuna tupla contiene (altezza, riga, colonna)
    """
    vette = []
    for riga in range(len(mappa)):
        for col in range(len(mappa[0])):
            if is_vetta_2(mappa, riga, col):
                vette.append((mappa[riga][col], riga, col))
    return vette


def is_vetta_2(mappa, riga, col):
    altezza = mappa[riga][col]

    if altezza == 0:
        return False

    for r in range(riga - 1, riga + 2):
        for c in range(col - 1, col + 2):
            if ((r != riga or c != col) and
                    0 <= r < len(mappa) and 0 <= c < len(mappa[0]) and
                    mappa[r][c] >= altezza):
                return False

    # riga+1 deve valere al max len()-1

    # for r in range(max(0, riga - 1), 1 + min(riga + 1, len(mappa) - 1)):
    #     for c in range(max(col - 1, 0), 1 + min(col + 1, len(mappa[0]) - 1)):
    #         if ((r != riga or c != col) and
    #                 mappa[r][c] >= altezza):
    #             return False

    return True

    # for dr in range(-1, 2):
    #     for dc in range(-1,2):
    #         mappa[riga+dr][col+dc]


def is_vetta(mappa, riga, col):
    altezza = mappa[riga][col]

    if altezza == 0:
        return False

    if riga > 0 and mappa[riga - 1][col] >= altezza:  # up
        return False
    if riga < len(mappa) - 1 and mappa[riga + 1][col] >= altezza:  # down
        return False
    if col > 0 and mappa[riga][col - 1] >= altezza:  # left
        return False
    if col < len(mappa[0]) - 1 and mappa[riga][col + 1] >= altezza:
        return False

    if riga > 0 and col > 0 and mappa[riga - 1][col - 1] >= altezza:  # up-left
        return False
    if riga > 0 and col < len(mappa[0]) - 1 and mappa[riga - 1][col + 1] >= altezza:  # up-right
        return False
    if riga < len(mappa) - 1 and col > 0 and mappa[riga + 1][col - 1] >= altezza:  # down-left
        return False
    if riga < len(mappa) - 1 and col < len(mappa[0]) - 1 and mappa[riga + 1][col + 1] >= altezza:  # down-right
        return False

    return True


def main():
    mappa = leggi_tabella('mappa.txt')
    # pprint(mappa)
    vette = cerca_vette(mappa)
    # pprint(vette)

    if vette:
        somma = 0
        for vetta in vette:
            print(f'{vetta[0]} {vetta[1]} {vetta[2]}')
            somma = somma + vetta[0]
        print(f'Altezza media: {somma / len(vette)}')
    else:
        print('Non abbiamo trovato vette')


main()
