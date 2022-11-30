NOME_INPUT = "mary.txt"
NOME_OUTPUT = "mary_elaborata.txt"

f_in = open(NOME_INPUT, "r", encoding="utf-8")
f_out = open(NOME_OUTPUT, "w", encoding="utf-8")

for riga in f_in:
    # dividi in parole
    riga = riga.rstrip('\n')
    if riga:
        parole = riga.split(' ')

        for i in range(len(parole)):
            parole[i] = parole[i].strip(',."?')

        # NOOOO
        # for parola in parole:
        #     parola = parola.strip(',."?')
        #     print(parola)

        # Alternativa OK
        # for i, parola in enumerate(parole):
        #     parole[i] = parola.strip(',."?')

        # print(parole)
        # Stampa le parole sul file di uscita

        # for parola in parole:
        #     f_out.write(parola+'\n')

        # f_out.writelines([parola + '\n' for parola in parole])

        for parola in parole:
            print(parola, file=f_out)

        # print('\n'.join(parole), file=f_out)

        # f_out.write('\n'.join(parole) + '\n')

f_in.close()
f_out.close()
