a = int(input("Masukkan nilai a: "))

# Hitung penjumlahan bilangan ganjil
total_ganjil = 0
for i in range(1, n + 1, 2):
    total_ganjil += i

# Hitung penjumlahan bilangan genap
total_genap = 0
for i in range(2, n + 1, 2):
    total_genap += i

# Tampilkan bilangan yang dijumlahkan
print("Ganjil:", total_ganjil)
print("Genap:", total_genap)
