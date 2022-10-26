# riga == base
# colonna == esponente

EXP_MAX = 4
BASE_MAX = 10

for exp in range(1, EXP_MAX+1):
    print(f'{exp:6d}', end='')
print()

print('    x ' * EXP_MAX)
print('-' * (6*EXP_MAX))

for base in range(1, BASE_MAX+1):
    # print (f'riga con tutte le potenze di {base}')
    for exp in range(1, EXP_MAX+1):
        # print(f'{base}^{exp} = {base**exp}')
        print(f'{base**exp:6d}', end='')

    print()
