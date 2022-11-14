n = int(input('N = '))
quadrati = []

for i in range(0, n+1):
    quadrati.append(i*i)

print(quadrati)

for i, v in enumerate(quadrati):
    if i != len(quadrati)-1:
        print(f'{v}, ', end='')
    else:
        print(f'{v}', end='')
print()

for v in quadrati[:-1]:
    print(f'{v}, ', end='')
print(quadrati[-1])

stampa = ""
for v in quadrati[:-1]:
    stampa = stampa + f'{v}, '
stampa = stampa + str(quadrati[-1])
print('**', stampa, '**')

quadrati_s = [] # il contenuto di quadrati, ma come valori stringa
for v in quadrati:
    quadrati_s.append(str(v))

stampa = ', '.join(quadrati_s)
print('!!', stampa, '!!')
print(len(stampa))
print(len(quadrati))


# L'utente inserisce un numero per volta, terminando con ''

numeri=[]
s = input('numero: ')
while s!='' :
    n = int(s)
    numeri.append(n)
    s = input('numero: ')

print(numeri)

# L'utente inserisce i numeri tutti insieme, separandoli con virgole

serie = input('Serie di numeri: ')
serie2 = serie
# "3, 4, 88"

numeri = []
while ',' in serie:
    pos = serie.index(',')
    num = int(serie[0:pos])
    numeri.append(num)
    serie = serie[pos+1:]

numeri.append(int(serie))

print(numeri)


# Proviamo con split
numeri2 = serie2.split(',')
for i in range(len(numeri2)):
    numeri2[i] = int(numeri2[i])
print(numeri2)
