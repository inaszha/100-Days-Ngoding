angka = []

for i in range(10):
    angka.append(i)

print(angka)
# Menghapus
angka.pop(-1)
angka.remove(8)

# Menambahkan
angka.append(20)

# Edit index ke 2
angka[2] = 10

print(angka)
