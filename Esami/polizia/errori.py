# ERRORI FREQUENTI

line = 'si ma non trovo un pezzo    non posso procedere finché non me lo procuro\n'
parole = line.rstrip('\n').split(' ')
# Dividere le righe in parole
# => inutile perché il testo dice "non ci sono parole composte che contengano 'bob', 'arctor' o 'polizia'"
# Non è sbagliato, ma fa perdere tempo inutilmente



riga = [ 'si', 'ma', 'non', 'trovo', 'un', 'pezzo']
# non scrivere:
for parola in riga:
    if parola=='bob':
        ...
# ma scrivere (ricerca se un elemento specifico è presente in una lista)
if 'bob' in riga:
    ...
# Non è sbagliato, ma è più macchinoso




# Questo non ha senso, non serve a niente, se non a creare una lista di 1 elemento
line = 'si ma non trovo un pezzo    non posso procedere finché non me lo procuro\n'
line.split('\n')
[ ['xxx'], ['yyy'] ]





### OPERATORI BOOLEANI ###
if ('bob') or ('arctor' in line):   # SEMPRE True!!
    ...
if ('bob' in line) or ('arctor' in line):
    ...





### SULLA CANCELLAZIONE ###

for i in range(len(testo)):
for line in testo:
    if 'bob' in line:
        testo.remove(line)
        testo.pop(i)
        testo[i] = ''

        # peggio: pop(i+1)
        #
        # peggio peggio: pop(i-1)

"MAI MODIFICARE LA LISTA SU CUI SI STA ITERANDO"
"MAI TAGLIARE IL RAMO SU CUI SI STA SEDUTI"
# ->>> CI SONO SEMPRE SOLUZIONI MIGLIORI <<<-



# ERRORE LOGICO
# Volere cancellare le righe prima di avere conosciuto tutte le posizioni dei nomi
'x'
'bob'
'arctor'
'y'
'z' # <- questa la devo cancellare!!





## NELLA RICERCA DELLA POLIZIA

if 'bob' in line or 'arctor' in line and 'polizia' in line:
    ... # precedenza errata operatori

if ('bob' in line or 'arctor' in line) and 'polizia' in line:
    ... # richiede che siano sulla STESSA riga, caso inutile







## IPOTESI ERRATE NELLA RICERCA
'''
- c'è una sola volta 'polizia'
- 'polizia' viene sempre DOPO i nomi di Bob
- mi interessa solo l'ultima volta che vedo 'bob' o 'arctor'
'''
## CONSEGUENZE
'''
Potendo avere N occorrenze di bob e arctor
e potendo avere M occorrenze di polizia
che possono alternarsi in qualsiasi ordine
-> devo calcolare NxM distanze e prendere la minima
'''