uang_harian = 2000  
tabungan_awal = 5000  
target_uang = 10000 

hari = 0  

while tabungan_awal < target_uang:
    tabungan_awal += uang_harian
    hari += 1

print(f"Dibutuhkan {hari} hari untuk mengumpulkan {target_uang} rupiah.")
