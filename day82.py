panjang_array = 10

nilai_array = []

for i in range(panjang_array):
    nilai_array.append(i * 2)

nilai_indeks_5 = nilai_array[4]
nilai_indeks_7 = nilai_array[6]

total_nilai = nilai_indeks_5 + nilai_indeks_7

print("array pada indeks 5:", nilai_indeks_5)
print("array pada indeks 7:", nilai_indeks_7)
print("Jumlah nilai pada indeks 5 dan 7:", total_nilai)
