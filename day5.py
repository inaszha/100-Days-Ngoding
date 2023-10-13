angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
jumlah = angka1 + angka2
print("Hasil penjumlahan:", jumlah)
selisih = angka1 - angka2
print("Hasil pengurangan:", selisih)
hasil_kali = angka1 * angka2
print("Hasil perkalian:", hasil_kali)
if angka2 != 0:
    hasil_bagi = angka1 / angka2
    print("Hasil pembagian:", hasil_bagi)
else:
    print("Pembagian dengan nol tidak diizinkan.")
