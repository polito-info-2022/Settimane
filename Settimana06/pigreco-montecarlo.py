import random

# Decido quanti punti casuali generare : n_punti
n_punti = int(input("Numero di punti: "))

# RIPETI n_punti VOLTE
n_interni = 0
for i in range(n_punti):
    # Genera le coordinate (x,y) casuali nel range [-1, +1]
    x = random.random() * 2.0 - 1.0
    y = random.uniform(-1.0, 1.0)

    # Verifica se il punto cade all'interno del cerchio,
    # aggiornando n_interni
    if x * x + y * y <= 1.0:
        n_interni = n_interni + 1

# Fai i calcoli
area_quadrato = 4.0
area_cerchio = area_quadrato * (n_interni / n_punti)

print(f'Pi Greco vale {area_cerchio}')
