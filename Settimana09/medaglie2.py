medaglie = [
    [1, 3, 1],
    [0, 0, 1],
    [2, 2, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]

nazioni = ['Canada', 'Italia', 'Germania', 'Giappone', 'Kazakistan', 'Russia', 'Corea del Sud',
           'Stati Uniti d\'America']

# l'indice nella lista medaglie[] corrisponde all'indice nella lista nazioni[]
# le medaglie vinte dalla nazione nazioni[i] sono elencate nella riga medaglie[i]

# Stampiamo l'elenco delle medeglie vinte da ciascuno stato

for i in range(len(nazioni)):  # range(len(medaglie))
    print(f'{nazioni[i]:25s}', end='')
    print(f'{medaglie[i][0]:2d}', end='')
    print(f'{medaglie[i][1]:2d}', end='')
    print(f'{medaglie[i][2]:2d}', end='')
    print()

# Quale nazione ha il max numero di medaglie d'oro?
val_max = -1
for i in range(len(medaglie)):
    if medaglie[i][0] > val_max:
        val_max = medaglie[i][0]
        pos_max = i

print(f'Max medaglie d\'oro: {val_max} per la nazione {nazioni[pos_max]}')

medaglie_oro = [med[0] for med in medaglie]
val_max = max(medaglie_oro)
pos_max = medaglie_oro.index(val_max)
print(f'Max medaglie d\'oro: {val_max} per la nazione {nazioni[pos_max]}')

# Quale nazione ha il max numero di medaglie TOTALI?
val_max = -1
for i in range(len(medaglie)):
    if sum(medaglie[i]) > val_max:
        val_max = sum(medaglie[i])
        pos_max = i

print(f'Max totali: {val_max} per la nazione {nazioni[pos_max]}')

medaglie_tot = [sum(med) for med in medaglie]
val_max = max(medaglie_tot)
pos_max = medaglie_tot.index(val_max)

print("\nMassimi a pari merito")
# nazioni_max_totale = [ medaglie for medaglie in medaglie_tot if medaglie == val_max ]
# print(nazioni_max_totale)
# indici_nazioni_max_totale = [ i for i in range(len(medaglie_tot)) if medaglie_tot[i] == val_max ]
# print(indici_nazioni_max_totale)
nomi_nazioni_max_totale = [nazioni[i] for i in range(len(medaglie_tot)) if medaglie_tot[i] == val_max]
print(nomi_nazioni_max_totale)

for i in range(len(medaglie_tot)):
    if medaglie_tot[i] == val_max:
        print(nazioni[i])

print(f'Max totali: {val_max} per la nazione {nazioni[pos_max]}')

# Quale è la medaglia più vinta? In totale, ho dato più medaglie d'oro, argento, o bronzo?

tot_oro = sum([med[0] for med in medaglie])
tot_arg = sum([med[1] for med in medaglie])
tot_bro = sum([med[2] for med in medaglie])

print(f'Medaglie totali: {tot_oro}, {tot_arg}, {tot_bro}')

# Stampiamo la classifica in base al numero totale di medaglie

medaglie_tot = [sum(med) for med in medaglie]
copia_nazioni = list(nazioni)

while medaglie_tot:
    val_max = max(medaglie_tot)
    pos_max = medaglie_tot.index(val_max)
    print(f'{copia_nazioni[pos_max]}  {val_max}')

    medaglie_tot.pop(pos_max)
    copia_nazioni.pop(pos_max)

medaglie_tot = [sum(med) for med in medaglie]

# punti_e_nazioni = [
#     [medaglie_tot[0], nazioni[0]],
#     [medaglie_tot[1], nazioni[1]],
#     [medaglie_tot[2], nazioni[2]],
# ]

# punti_e_nazioni = []
# for i in range(len(nazioni)):
#     punti_e_nazioni.append([ medaglie_tot[i], nazioni[i]])

punti_e_nazioni = [[medaglie_tot[i], nazioni[i]] for i in range(len(nazioni))]

punti_e_nazioni.sort(reverse=True)

print(punti_e_nazioni)
