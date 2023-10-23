umur = int(input("Masukkan umur Anda: "))
if umur < 17:
    print("Anda termasuk dalam kategori 'dibawah umur'.")
elif 17 <= umur <= 20:
    print("Anda termasuk dalam kategori 'remaja'.")
else:
    print("Anda termasuk dalam kategori 'dewasa'.")
