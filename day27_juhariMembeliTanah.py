panjang_tanah = 10  
lebar_tanah = 15   

harga_per_meter_persegi = 500000
jumlah_kampling = 30


luas_tanah = panjang_tanah * lebar_tanah
total_harga_tanah = luas_tanah * harga_per_meter_persegi
total_harga_kampling = total_harga_tanah * jumlah_kampling


print("Luas Tanah:", luas_tanah, "meter persegi")
print("Harga per Meter Persegi:", harga_per_meter_persegi, "rupiah")
print("Total Harga Tanah (untuk 1 kampling):", total_harga_tanah, "rupiah")
print("Jumlah Kampling:", jumlah_kampling)
print("Total Harga untuk 30 Kampling:", total_harga_kampling, "rupiah")
