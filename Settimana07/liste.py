esempio = [ 3, 7, 9, 33 ]

print(esempio)

for i in range(len(esempio)):
    v = esempio[i]
    print(i, v)

for v in esempio:
    print(v)

for i, v in enumerate(esempio):
    print(i, v)

esempio.insert
