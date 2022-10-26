# Leggere da tastiera una serie di numeri interi positivi, terminando l'inserimento con il valore -1, e stampare la loro somma

somma = 0

# num = 0  # valore iniziale 'fasullo'
#
# while num != -1:
#     num = int(input("Numero: "))
#     if num != -1:
#         somma = somma + num
#

# ok = True
#
# while ok:
#     num = int(input("Numero: "))
#     if num == -1:
#         ok = False
#     else:
#         somma = somma + num


# num = int(input("Numero: "))
#
# while num != -1:
#     somma = somma + num
#
#     num = int(input("Numero: "))


# Variante: terminare l'inserimento inserendo una riga vuota

# num = int(riga)


# riga = input("Numero: ")
#
# while riga != '':
#     num = int(riga)
#     somma = somma + num
#
#     riga = input("Numero: ")

# Estensione: se il valore inserito non è valido (es. è negativo), ri-chiederlo

# riga = input("Numero: ")
#
# while riga != '':
#     num = int(riga)
#     #########
#
#     while num<0:
#         riga = input("Numero: ")
#         num = int(riga)
#         #TODO: se l'utente inserisce '' dopo un numero negativo, il programma dà errore
#
#     somma = somma + num
#
#     riga = input("Numero: ")


# Estensione: se il valore inserito non è valido (es. è negativo), ignorarlo


# riga = input("Numero: ")
#
# while riga != '':
#     num = int(riga)
#     if num >= 0:
#         somma = somma + num
#
#     riga = input("Numero: ")

# Estensione: alla fine del ciclo, dire se sono stati inseriti dei multipli di 3


trovato_multiplo = False
riga = input("Numero: ")

while riga != '':
    num = int(riga)
    if num >= 0: # numero è valido, deve essere elaborato (>=0)
        somma = somma + num
        if num%3==0:
            trovato_multiplo = True

    riga = input("Numero: ")

if trovato_multiplo:
    print('almeno un multiplo trovato')
else:
    print('nessun multiplo trovato')

print(somma)


