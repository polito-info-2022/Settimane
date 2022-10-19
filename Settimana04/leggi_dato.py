# l'utente deve inserire una stringa di 4 caratteri

# s = input("Stringa: ")
# if len(s) != 4:
#     print("Errore")
#     s = input("Stringa: ")
#     if len(s) != 4:
#         print("Errore")
#         s = input("Stringa: ")

s = input("Stringa: ")
while len(s)!=4:
    print('Errore')
    s = input("Stringa: ")
