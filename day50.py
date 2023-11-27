angkaAwal = int(input("Masukkan angka awal: "))
angkaAkhir = int(input("Masukkan angka akhir: "))

for num in range(angkaAwal, angkaAkhir + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
