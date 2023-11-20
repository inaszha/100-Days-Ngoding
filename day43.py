a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

total_genap =  0
total_ganjil = 0
for i in range (a, b):
    if i % 2 == 0:
        total_genap += i

    else:
        total_ganjil += i
print ("genap :",total_genap)
print ("ganjil :",total_ganjil)
