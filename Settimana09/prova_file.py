

f = open("storia.txt", "r", encoding='utf-8')
g = open("storia_big.txt", "w", encoding='utf-8')

# i = 1
#
# storia = f.read(20)
#
# while len(storia)>0:
#     print(i, storia)
#     i = i+1
#     storia = f.read(20)

g.write("*** La mia Storia ***\n")

line = f.readline()
while line:

    line = line.rstrip('\n')

    print(line)
    g.write(line[::-1]+'\n')

    line = f.readline()

f.close()
