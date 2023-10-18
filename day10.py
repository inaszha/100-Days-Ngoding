nama = input("masukkan nama anda :")
gaji = float(input ("masukkan gaji anda :"))
pekerjaan = input ("masukkan pekerjaan :")
lama_kerja = int(input ("lama kerja :"))

if pekerjaan == "PNS":
    tambahan_pekerjaan = -0.10
elif pekerjaan == "buruh":
    tambahan_pekerjaan = 0.10
else:
    tambahan_pekerjaan = 0.5

if lama_kerja < 1:
    tambahan = 0
elif lama_kerja > 5:
    tambahan = 200000
else:
    tambahan = 50000
    
if gaji > 10000000:
    pajak = 0.05
elif gaji < 3000000:
    pajak = -0.02
else:
    pajak = 0

gaji_kotor = gaji + tambahan + (gaji * tambahan_pekerjaan)
pajak_total =(gaji_kotor * pajak)
gaji_bersih = gaji_kotor - pajak_total

print("Gaji bersih anda: " + str(gaji_bersih))

