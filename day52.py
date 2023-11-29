panjang = int(input("panjang :"))
array = []
genap = []
ganjil = []

for i in range (panjang):
    nilai = int (input("nilai :"))
    array.append (nilai)
    print (array)
    if nilai %2 == 0:
        genap.append(nilai)
        print ("jumlah bilangan genap :", len(genap))
    else:
        ganjil.append(nilai)
        print ("jumlah bilangan ganjil :",len(ganjil))
