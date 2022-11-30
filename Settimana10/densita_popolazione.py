FILE_POPOLAZIONE = 'worldpop.txt'
FILE_AREA = 'worldarea.txt'
FILE_DENSITA = 'world_pop_density.txt'


def separa(riga):
    riga = riga.rstrip('\n')
    campi = riga.rsplit(maxsplit=1)
    nazione = campi[0]
    valore = int(campi[1])
    return nazione, valore


f_pop = open(FILE_POPOLAZIONE, 'r', encoding='utf-8')
f_area = open(FILE_AREA, 'r', encoding='utf-8')
f_densita = open(FILE_DENSITA, 'w', encoding='utf-8')


riga_pop = f_pop.readline()
riga_area = f_area.readline()


while riga_pop!='' and riga_area!='':

    # elabora
    # print(riga_pop)
    # print(riga_area)

    nazione1, popolazione = separa(riga_pop)
    nazione2, area = separa(riga_area)

    if nazione1==nazione2:
        if area!=0:
            densita = popolazione/area
            print(nazione1, f'{densita:.2f}', file=f_densita)
        else:
            print(nazione1, 'n.d.', file=f_densita)

    else:
        exit("File non sincronizzati")

    riga_pop = f_pop.readline()
    riga_area = f_area.readline()


f_pop.close()
f_area.close()
f_densita.close()
