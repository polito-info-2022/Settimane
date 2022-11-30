ok = False
while not ok:
    try:
        n = int(input("Dato: "))
        ok = True
    except ValueError:
        print("Dato non valido")

print("Fine")
