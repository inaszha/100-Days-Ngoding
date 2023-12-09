nama = input("nama pengirim : ")
no = input("No Telepon :")
print("==pilihan tujuan===")
print("1. bandung")
print("2. Jakarta")
print("3. Semarang")
print("==================")
tujuan = input("tujuan pengiriman : ")
print("==jenis pengiriman===")
print("REGULER")
print("EKSPRES")
print("=====================")
jenis = input("jenis pengiriman : ")
berat = int(input("berat barang : "))
print("==asuransi===")
print("YA")
print("TIDAK")
print("=====================")
asuransi = input("asuransi : ")

if jenis == "reguler":
    if asuransi == "ya":
        if tujuan == "bandung":
            bayar = 10000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : Rp. ", biaya_asuransi)
            print("TOTAL BAYAR : Rp. ", total)
        elif tujuan == "jakarta":
            bayar = 20000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : Rp. ", biaya_asuransi)
            print("TOTAL BAYAR : Rp. ", total)
        elif tujuan == "semarang":
            bayar = 30000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : Rp. ", biaya_asuransi)
            print("TOTAL BAYAR : Rp. ", total)
        else:
            print("Lokasi yang anda masukkan tidak tersedia")
    elif asuransi == "tidak":  
        if tujuan == "bandung":
            bayar = 10000 * berat
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : TIDAK DIKENAKAN ASURANSI")
            print("TOTAL BAYAR : Rp. ", bayar)
        elif tujuan == "jakarta":
            bayar = 20000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : TIDAK DIKENAKAN ASURANSI")
            print("TOTAL BAYAR : Rp. ", total)
        elif tujuan == "semarang":
            bayar = 30000 * berat
            biaya_asuransi = bayar * 0.07
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : TIDAK DIKENAKAN ASURANSI")
            print("TOTAL BAYAR : Rp. ", bayar)
        else:
            print("Lokasi yang anda masukkan tidak tersedia")
elif jenis == "ekspres": 
    if asuransi == "ya":
        if tujuan == "bandung":
            bayar = 12000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : Rp. ", biaya_asuransi)
            print("TOTAL BAYAR : Rp. ", total)
        elif tujuan == "jakarta":
            bayar = 24000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : Rp. ", biaya_asuransi)
            print("TOTAL BAYAR : Rp. ", total)
        elif tujuan == "semarang":
            bayar = 35000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : Rp. ", biaya_asuransi)
            print("TOTAL BAYAR : Rp. ", total)
        else:
            print("Lokasi yang anda masukkan tidak tersedia")
    elif asuransi == "tidak":  
        if tujuan == "bandung":
            bayar = 12000 * berat
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : TIDAK DIKENAKAN ASURANSI")
            print("TOTAL BAYAR : Rp. ", bayar)
        elif tujuan == "jakarta":
            bayar = 24000 * berat
            biaya_asuransi = bayar * 0.07
            total = biaya_asuransi + bayar
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : TIDAK DIKENAKAN ASURANSI")
            print("TOTAL BAYAR : Rp. ", total)
        elif tujuan == "semarang":
            bayar = 35000 * berat
            biaya_asuransi = bayar * 0.07
            print("BAYAR : Rp. ", bayar)
            print("BIAYA ASURANSI : TIDAK DIKENAKAN ASURANSI")
            print("TOTAL BAYAR : Rp. ", bayar)
        else:
            print("Lokasi yang anda masukkan tidak tersedia")
