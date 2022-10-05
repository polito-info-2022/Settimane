# DATI:
# una lattina contiene 12 once
# (12 oncia = 0.355 litri)
#
# Qual è la capacità totale di 6 lattine?
# Sarà più o meno di 2 litri?

# capacità in once = 12
# numero di lattine = 6
capacita_lattina_once = 12 # once
numero_lattine = 6

# fattore di conversione once->litri = 0.355 / 12
CONVERSIONE_ONCE_LITRI = 0.355 / 12

# capacità di una lattina in litri = capacità in once * fattore di conversione once->litri
capacita_lattina_litri = capacita_lattina_once * CONVERSIONE_ONCE_LITRI

# capacita totale = capacita di 1 lattina * numero di lattine (in litri!)
capacita_totale = capacita_lattina_litri * numero_lattine

print("Le lattine complessivamente contengono", capacita_totale, "litri")
print('Le lattine complessivamente contengono', capacita_totale, 'litri')



