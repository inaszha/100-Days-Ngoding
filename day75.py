angka = int(input("masukkan angka: "))
jumlah = 0
arr =[]
for i in range(1,angka):
    if i % 3 == 0:
        arr.append(i)
        print(arr)
        jumlah+=i
        print("-------")
print("total penjumlahan:  ",jumlah)
