# medaglie_canada = [0, 3, 0]
# medaglie_italia = [0, 0, 1]
# ...
# medaglie_usa = [1, 0, 1]
#
# # chi ha vinto più medaglie d'oro?
#
# medaglie_oro = [0,0,0,1,0,3,0,1]
# val_max = max(medaglie_oro)
# pos_max = medaglie_oro.index(val_max)
# print(f'La nazione {pos_max} ha vinto {val_max} medaglie d\'oro')
#
# val_max = max(medaglie_canada[0], medaglie_italia[0], medaglie_usa[0])
# if val_max==medaglie_canada[0]:
#     ...
# elif val_max==medaglie_italia[0]:
#     ...


# medaglie = [
#     [0, 3, 0],
#     [0, 0, 1],
#     [1, 0, 1]
# ]



nazioni = [ 'Canada', 'Germania', 'Italia',  'USA' ]

# medaglie = []
#
# for nazione in nazioni:
#     print(f'Medaglie vinte da {nazione}?')
#     oro = int(input("Oro: "))
#     arg = int(input("Argento: "))
#     bro = int(input("Bronzo: "))
#
#     medaglie_nazione = [oro, arg, bro]
#     medaglie.append(medaglie_nazione)
#
#     print(medaglie_nazione)
#     print(medaglie)
#

medaglie = []

for nazione in nazioni:
    print(f'Medaglie vinte da {nazione}?')

    medaglie.append([])

    x = int(input("Oro: "))
    medaglie[-1].append(x)

    x = int(input("Argento: "))
    medaglie[-1].append(x)

    x = int(input("Bronzo: "))
    medaglie[-1].append(x)

    print(medaglie)

# chi ha vinto più medaglie d'oro?
max_val = 0
for riga in medaglie:
    if riga[0]>max_val:
        max_val=riga[0]


