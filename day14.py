print ("=====nomor 1=====")
nilai = int(input("Masukkan nilai integer: "))
if nilai % 2 == 0:
    print("Nilai", nilai, "adalah bilangan genap.")
else:
    print("Nilai", nilai, "adalah bilangan ganjil.")



print ("=====nomor 2=====")
hargaPcGaming = 150000000
penghasilan = 13000000
biayaAnak1 = 2000000
biayaAnak2 = 1000000
rumah = 4000000
tabungan = 5000000
pengeluaran = biayaAnak1 + biayaAnak2 + rumah
istri = penghasilan - tabungan - pengeluaran
lamaYgDiperlukan = 150000000 / 5000000
hitungan_Thn = lamaYgDiperlukan / 12

print ("harga pc gaming adalah" ,hargaPcGaming)
print ("penghasilan sambo perbulan" ,penghasilan)
print("pengeluaran sambo perbulan" ,pengeluaran)
print ("uang untuk istri", istri)
print ("waktu yang diperlukan sambo untuk bisa membeli pc tersebut adalah" , lamaYgDiperlukan,"bulan atau",hitungan_Thn, "tahun")
