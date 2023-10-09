nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam cm): "))
kesibukan = input("apakah anda masih sibuk  ?")
tahun_lahir = 2023 - umur

print("\n===== Perkenalan Diri =====")
print("Nama: {}".format(nama))
print("Umur: {}".format(umur))
print("Tahun Lahir: {}".format(tahun_lahir))
print("Tinggi Badan: {} cm".format(tinggi_badan))


if kesibukan == "iya":
    print("\nkamu tidak harus mengumpulkan codingan yang wah banget di 100 days ngoding ini")
else:
    print("\nyang lebih lagi lah masa begini begini trus ji bisa nu bikin dari semester 1")
