
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam cm): "))
kesibukan = input("apakah anda masih sibuk  ?")

# Operasi Aritmatika
tahun_lahir = 2023 - umur
panjang_setengah_tinggi = tinggi_badan / 2

# Output perkenalan
print("\n===== Perkenalan Diri =====")
print("Nama: {}".format(nama))
print("Umur: {}".format(umur))
print("Tahun Lahir: {}".format(tahun_lahir))
print("Tinggi Badan: {} cm".format(tinggi_badan))
print("Setengah dari Tinggi Badan: {} cm".format(panjang_setengah_tinggi))

# Kondisi untuk pendaftaran CPNS
if kesibukan == "iya":
    print("\nkamu tidak harus mengumpulkan codingan yang wah banget di 100 days ngoding ini")
else:
    print("\nyang lebih lagi lah masa begini begini trus ji bisa nu bikin dari semester 1")
