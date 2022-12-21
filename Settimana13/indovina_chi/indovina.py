# I dati dei personaggi sono memorizzati in una lista di dizionari (24 elementi della lista)
# Ciascun dict avrà le chiavi (ti dipo stringa) corrispondenti alle colonne del file personaggi.txt
# [ {'Nome': 'Alex', 'Sesso': 'Uomo', ...} , { } ... { } ]
# I valori del dizionario sono tutte stringhe.
import csv
from pprint import pprint


# I dati delle mosse del giocatore saranno memorizzati in un dict() che ha come chiave l'attributo
# del personaggio (stringa) e come valore il valore specificato dall'utente (stringa)
# La chiave dovrà coincidere con una chiave del dizionario dei personaggi.


# Durante la partita, partiamo da una lista che contiene TUTTI i personaggi, e poi ad ogni
# mossa cancelliamo da questa lista gli elenti che non soddisfano la proprietà.

def leggi_personaggi(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')
    reader = csv.DictReader(f, delimiter=';')
    # personaggi = []
    # for personaggio in reader:
    #     personaggi.append(personaggio)
    personaggi = list(reader)
    f.close()
    return personaggi


def leggi_personaggi_stupida(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')

    titoli = f.readline().rstrip('\n').split(';')

    personaggi = []
    for line in f:
        campi = line.rstrip('\n').split(';')

        record = dict()
        for i in range(len(titoli)):
            record[titoli[i]] = campi[i]

        personaggi.append(record)

    f.close()
    return personaggi


def leggi_mosse(nome_file):
    try:
        f = open(nome_file, 'r', encoding='utf-8')
        mosse = {}
        for line in f:
            campi = line.rstrip('\n').split('=')
            mosse[campi[0]] = campi[1]
        f.close()
        return mosse
    except OSError:
        print("File inesistente")
        return None


def stampa_personaggi(personaggi):
    for personaggio in personaggi:
        print(f"{personaggio['Nome']} - ", end='')

        for proprieta in personaggio:
            if proprieta!= 'Nome':
                print(f"{proprieta}: {personaggio[proprieta]}, ", end='')

        print()


def partita(personaggi, mosse):

    print('Elenco dei personaggi')
    stampa_personaggi(personaggi)

    rimasti = list(personaggi)

    for proprieta_mossa, valore_mossa in mosse.items():
        print(f'Mossa: {proprieta_mossa}={valore_mossa}')

        # eseguo la mossa
        # cancello da 'rimasti[]' che che hanno proprità diversa da valore
        # for rimasto in rimasti[::-1]:
        #     if rimasto[proprieta_mossa]!=valore_mossa:
        #         rimasti.remove(rimasto)

        validi = []
        for rimasto in rimasti:
            if rimasto[proprieta_mossa]==valore_mossa:
                validi.append(rimasto)
        rimasti = validi

        # rimasti = [ rimasto for rimasto in rimasti if rimasto[proprieta_mossa]==valore_mossa ]

        print("Sono rimasti:")
        stampa_personaggi(rimasti)

    if len(rimasti)==1:
        print('Congratulazioni, hai vinto!')
    else:
        print('Hai perso, mi spiace...')


def main():
    personaggi = leggi_personaggi('personaggi.txt')
    nome_file_mosse = input('Quale file contiene le tue mosse?')
    while nome_file_mosse!='':
        mosse = leggi_mosse(nome_file_mosse)
        if mosse != None:
            partita(personaggi, mosse)
        nome_file_mosse = input('Quale file contiene le tue mosse?')

main()
