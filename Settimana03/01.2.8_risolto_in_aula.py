# Esercizio 01.2.8

# risoluzione in aula

# Display an animal speaking a greeting.

print(" /\\_/\\    ________________")
print("( o o )  /                \\")
print("==_Y_== < Computer Science >")
print("  '-'    \\________________/")


# La stessa cosa si può fare in modo più compatto, usando l'elaborazione di stringhe

print(" /\\_/\\   ", 16*"_")
print("( o o ) ", "/",14*" ", " \\")
print("==_Y_== < Computer Science >")
print("  '-'    \\", 16*"_", "/", sep='')

# Facciamo decidere la dimensione della nuvoletta dall'utente.
# Usiamo un modificatore che consenta di usare lo scaling factor ai lati della stringa
# notiamo però che non sempre la stringa è centrata...

scalingFactor = int(input('Dimensioni della nuvoletta: '))

print(" /\\_/\\   ", scalingFactor*"_", sep='')
print("( o o ) ", "/", scalingFactor*" ", "\\", sep='')
print("==_Y_== ", "<", int(scalingFactor/3)*" ", "Computer Science", int(scalingFactor/3)*" ", ">", sep='')
print("  '-'   \\", scalingFactor*"_", "/", sep='')


# la lunghezza della stringa deve essere considerata nell'adattare la dimensione della nuvoletta
# non è sufficiente inserire un "modificatore" allo scaling factor
# soprattutto se la stringa è fornita in input dall'utente
# in questo caso, possiamo far dipendere la dimansione della nuvoletta direttamente dalla lunghezza
# della stringa fornita in input

messaggio = input("Messaggio del gatto: ")
scalingFactor = int(len(messaggio))


print(" /\\_/\\   ", scalingFactor*"_", sep='')
print("( o o ) ", "/ ", scalingFactor*" ", " \\", sep='')
print("==_Y_== ", "< ", messaggio, " >", sep='')
print("  '-'   \\ ", scalingFactor*"_", " /", sep='')
