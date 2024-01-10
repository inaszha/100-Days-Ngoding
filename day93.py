import random

nomor_rahasia = random.randint(1, 100)

while True:
    tebakan = int(input("Tebak angka antara 1 dan 100: "))
    
    if tebakan == nomor_rahasia:
        print("Anda berhasil menebak ")
        break
    elif tebakan < nomor_rahasia:
        print("Terlalu rendah, Coba lagi.")
    else:
        print("Terlalu tinggi, Coba lagi.")
