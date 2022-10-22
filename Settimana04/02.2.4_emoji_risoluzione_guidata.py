# Ipotizziamo che le mie Emoji più frequenti siano le seguenti:
" 👍 🙂 😲 "

# NOTA: Per conoscere il codice Unicode si può usare la funzione ord()
# ord('👍') --> 128077
# Nelle tabelle Unicode solitamente si usa il valore espresso in base 16
# che si può ottenere dalla funzione hex()
# hex(128077) --> '0x1f44d'
# o direttamente: hex(ord('👍')) --> '0x1f44d'

# raccogliamo le informazioni che ci servono
# al link indicato nel testo:
# https://docs.google.com/spreadsheets/d/1Zs13WJYdZL1pNZP0dCIXkWau_tZOjK3mmJz0KNq4I30/edit#gid=196891844

# assegnamo i valori richiesti a delle variabili
# specifiche per ciascuna emoji

emoji1 = '👍'
rank1 = 4 # from https://home.unicode.org/emoji/emoji-frequency/
unicode1 = '1F44D' # from https://unicode-table.com/en/1F44D/
name1 = 'Thumbs Up Sign'

emoji2 = '🙂'
rank2 = 28 # from https://home.unicode.org/emoji/emoji-frequency/
unicode2 = '1F642' # from https://unicode-table.com/en/1F642/
name2 = 'Slightly Smiling Face'

emoji3 = '😲'
rank3 = 111 # from https://home.unicode.org/emoji/emoji-frequency/
unicode3 = '1F632' # from https://unicode-table.com/en/1F632/
name3 = 'Astonished Face'

# il passo successivo è visualizzare le informazioni raccolte
# esistono diversi modi per farlo

# ad esempio:
print("Modo 1:")
print("Emoji 1", emoji1)
print(f'Posizione={rank1}, numero={unicode1}, nome={name1}')

print("Emoji 2", emoji2)
print(f'Posizione={rank2}, numero={unicode2}, nome={name2}')

print("Emoji 3", emoji3)
print(f'Posizione={rank3}, numero={unicode3}, nome={name3}')

# oppure:
print("\nModo 2:")

print('Emoji 1: ', emoji1)
print('Rank: ', rank1)
print('Nome: ', name1)
print('Codice: ', unicode1)

print('Emoji 2: ', emoji2)
print('Rank: ', rank2)
print('Nome: ', name2)
print('Codice: ', unicode2)

print('Emoji 3: ', emoji3)
print('Rank: ', rank3)
print('Nome: ', name3)
print('Codice: ', unicode3)

# il testo dell'esercizio richiede di allineare verticalmente i valori mostrati per ciascuna emoji
# ci sono diversi modi per farlo

# ad esempio:
print("\nModo 3:")
print(f'La emoji 1 è: %38s'%(emoji1))
print(f'La sua posizione in classifica è: %19s'%(rank1))
print(f'Il suo Numero Unicode è: %28s'%(unicode1))
print(f'Il suo Nome Unicode è: %30s'%(name1))

print(f'La emoji 2 è: %38s'%(emoji2))
print(f'La sua posizione in classifica è: %19s'%(rank2))
print(f'Il suo Numero Unicode è: %28s'%(unicode2))
print(f'Il suo Nome Unicode è: %30s'%(name2))

print(f'La emoji 3 è: %38s'%(emoji3))
print(f'La sua posizione in classifica è: %19s'%(rank3))
print(f'Il suo Numero Unicode è: %28s'%(unicode3))
print(f'Il suo Nome Unicode è: %30s'%(name3))

# oppure:
print("\nModo 4:")
print(
    f"{'La emoji 1 è: ':<15}{emoji1:>37}",
    f"\n{'La sua posizione in classifica è: ':<15}{rank1:>19}",
    f"\n{'Il suo Numero Unicode è: ':<15}{unicode1:>28}",
    f"\n{'Il suo Nome Unicode è: ':<15}{name1:>30}",
    f"\n{'La emoji 2 è: ':<15}{emoji2:>37}",
    f"\n{'La sua posizione in classifica è: ':<15}{rank2:>19}",
    f"\n{'Il suo Numero Unicode è: ':<15}{unicode2:>28}",
    f"\n{'Il suo Nome Unicode è: ':<15}{name2:>30}",
    f"\n{'La emoji 3 è: ':<15}{emoji3:>37}",
    f"\n{'La sua posizione in classifica è: ':<15}{rank3:>19}",
    f"\n{'Il suo Numero Unicode è: ':<15}{unicode3:>28}",
    f"\n{'Il suo Nome Unicode è: ':<15}{name3:>30}",
)
