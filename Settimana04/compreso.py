val_min = 10
val_max = 20

numero = int(input(f"Dammi un numero tra {val_min} e {val_max}: "))

if numero < val_min:
    print('Escluso')
elif numero > val_max:
    print('Escluso')
else:
    print('Compreso')

if numero >= val_min:
    if numero <= val_max:
        print('Compreso')
    else:
        print('Escluso')
else:
    print('Escluso')

if numero >= val_min and numero <= val_max:
    print('Compreso')
else:
    print('Escluso')

# if numero >= val_min and <= val_max:
