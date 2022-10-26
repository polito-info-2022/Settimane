# Data una stringa inserita dall'utente, costruire e stampare una seconda
# stringa che contenga solo le consonanti.

riga = input("Inserisci una stringa: ")

nuova = ''

i = 0
while i<len(riga):
    if riga[i].lower() not in 'aeiou':
        nuova = nuova + riga[i]
    i = i + 1

print(nuova)

nuova = ''
for i in range(len(riga)):
    if riga[i].lower() not in 'aeiou':
        nuova = nuova + riga[i]

print(nuova)

nuova = ''
for ch in riga:
    if ch.lower() not in 'aeiou':
        nuova = nuova+ch

print(nuova)
