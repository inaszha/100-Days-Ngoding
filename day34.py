tahun_lahir = int(input("Tahun kelahiran Anda: "))
bulan_lahir = int(input("Bulan kelahiran Anda: "))
hari_lahir = int(input("Hari kelahiran Anda: "))
tahun_sekarang = 2023  
bulan_sekarang = 12  
hari_sekarang = 26
usia_tahun = tahun_sekarang - tahun_lahir
usia_bulan = bulan_sekarang - bulan_lahir
usia_hari = hari_sekarang - hari_lahir
if usia_hari < 0:
    usia_bulan -= 1
    usia_hari += 30  
if usia_bulan < 0:
    usia_tahun -= 1
    usia_bulan += 12
print("kamu telah hidup selama", usia_tahun, "tahun,", usia_bulan, "bulan, dan", usia_hari, "hari.")
