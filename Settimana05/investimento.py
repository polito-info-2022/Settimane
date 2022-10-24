"""
Partendo da un capitale iniziale di 10.000 euro, quanti anni sono necessari
per raddoppiare il capitale, se esso viene investito con un interesse fisso
composto pari al 5%?
"""

cap_iniziale = 10000
cap_finale = 2 * cap_iniziale

tasso_interesse = 0.05  # annuo

capitale = cap_iniziale
anni = 0

while capitale < cap_finale:
    interesse = capitale * tasso_interesse
    capitale = capitale + interesse
    anni = anni + 1
    # print(f'dopo {anni} anni hai {capitale} euro')

print(f'Hai raggiunto il capitale di {capitale:.2f} euro dopo {anni} anni')
