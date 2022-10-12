# Bisogna posizionare lungo il muro una fila di piastrelle nere e bianche.
# Per ragioni estetiche l’architetto ha specificato che la prima e l’ultima piastrella devono essere nere.
# Il vostro compito è calcolare il numero di piastrelle necessarie e il vuoto a ciascuna delle due estremità della
# riga, dato lo spazio disponibile e la larghezza di ogni piastrella.

'''

| s [N][B][N][B][N][B][N][B][N][B][N] s |

Dati in ingresso:
- lunghezza del muro  (LUN)
- lunghezza del lato della piastrella  (LATO)
- informazioni sui vincoli di posizionamento

Dati in uscita:
- numero di [N] (num_nere)
- numero di [B] (num_bianche)
- lunghezza dello spazio 's' ai margini (spazio)

Strategia di risoluzione:

        LUN / LATO
            = 5.0  num_nere=3, num_bianche=2, spazio=0
            = 4.0,
            = 4.5  num_nere=2, num_bianche=1, spazio = ( LUN - LATO*(num_bianche+num_nere) ) / 2
            = 5.5  num_nere=3, num_bianche=2

        num_coppie = int( (LUN - LATO) / (2*LATO) )
        num_bianche = num_coppie
        num_nere = num_coppie + 1
'''

LUN = 400  # cm
LATO = 25  # cm

# TODO: Verificare che LUN >= LATO
# Garbage in, garbage out

num_coppie = int((LUN - LATO) / (2 * LATO))
num_bianche = num_coppie
num_nere = num_coppie + 1

spazio = (LUN - LATO * (num_bianche + num_nere)) / 2

print('Posare', num_nere, 'piastrelle nere e ', num_bianche,
      'bianche, lasciando uno spazio di', spazio, 'cm per lato')
