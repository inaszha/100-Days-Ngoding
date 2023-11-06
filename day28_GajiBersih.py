nama = input("masukkan nama :")
penghasilan = int(input ("masukkan penghasilan :"))
pekerjaan = input("masukkan pekerjaan :")
pajak1 = 15/100
pajak2 = 5/100

if penghasilan > 10000000:
    total_gaji = penghasilan - (penghasilan * pajak1)
    if pekerjaan == "petani":
        gaji_bersih = total_gaji + 1000000
        print ("anda mendapat potongan pajak 15% dan bantuan sebanyak 1jt, jadi gaji yang anda terima sebesar",gaji_bersih)
    elif pekerjaan == "pns":
        gaji_bersih = total_gaji
        print ("anda mendapat potongan pajak 15% jadi gaji bersih yang diterima sebesar",gaji_bersih)
    else:
        gaji_bersih = total_gaji + 200000
        print ("anda mendapat potongan pajak 15% dan bantuan sebanyak 200000, jadi gaji yang anda terima sebesar",gaji_bersih)
elif penghasilan > 3000000:
    total_gaji = penghasilan - (penghasilan * pajak2)
    if pekerjaan == "petani":
        gaji_bersih = total_gaji + 1000000
        print ("anda mendapat potongan pajak 5% dan bantuan sebanyak 1jt, jadi gaji yang anda terima sebesar",gaji_bersih)
    elif pekerjaan == "pns":
        gaji_bersih = total_gaji
        print ("anda mendapat potongan pajak 5% jadi gaji bersih yang diterima sebesar",gaji_bersih)
    else:
        gaji_bersih = total_gaji + 200000
        print ("anda mendapat potongan pajak 5% dan bantuan sebanyak 200000, jadi gaji yang anda terima sebesar",gaji_bersih)
else:
    print("anda tidak mendapat potongan ataupun bantuan dana")
