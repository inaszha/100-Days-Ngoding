buah = [None] * 5

for i in range(1, len(buah)):
    buah[i] = input("Buah ke " + str(i) + ": ")

for a in buah[1:]:
    print(a)
