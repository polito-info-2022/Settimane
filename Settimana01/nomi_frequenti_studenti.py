import csv
import operator

from matplotlib import pyplot

FILENAME = '14BHDOA_2023_shuffled.csv'


# Leggi l'elenco degli studenti e salvalo in una lista di liste
def leggi(nome_file):
    with open(nome_file, 'r', newline='') as file:
        reader = csv.reader(file)
        prima_riga = next(reader)  # contiene i titoli -> ignoriamola
        studenti = []
        for line in reader:
            studenti.append(line)
    return studenti


# estrai i nomi (first name) da un elenco di studenti
def estrai_nomi(elenco):
    lista_nomi = []
    for riga in elenco:
        lista_nomi.append(riga[2])
    return lista_nomi


# Calcola le frequenze dei vari nomi presenti in un array
def frequenze(tokens):
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


# calcola il massimo valore presente nelle frequenze
def max_frequenza(freq):
    return max(freq.values())


def nomi_piu_frequenti(freq, maxx):
    return [nome for (nome, frequenza) in freq.items() if frequenza == maxx]


def main():
    stud = leggi(FILENAME)
    nomi = estrai_nomi(stud)
    print(f"Nella classe ci sono {len(stud)} studenti")
    freq = frequenze(nomi)
    max_freq = max_frequenza(freq)
    print(f"Il nome più frequente compare {max_freq} volte")
    nomi_max = nomi_piu_frequenti(freq, max_freq)
    print(f"Si tratta di : {', '.join(nomi_max)}")
    # estrai solo i nomi che compaiono almeno 3 volte
    freq2 = {k: v for (k, v) in freq.items() if v >= 3}
    print(
        f"I nomi che compaiono almeno 3 volte sono {', '.join(sorted(list(freq2.keys())))}."
    )

    hist = list(sorted(list(freq2.items()), key=operator.itemgetter(1), reverse=True))
    pyplot.barh(y=[h[0] for h in hist], width=[h[1] for h in hist])
    pyplot.show()


main()
