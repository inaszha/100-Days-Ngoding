noAtm = int(input("masukkan nomor atm anda :"))
pas = int(input("masukkan password anda :"))

if noAtm == 123 and pas ==1403:
    print ("LOGIN BERHASIL")
    print ("===============")
    print ("menu")
    print ("===============")
    print ("1. cek saldo")
    print ("2. transfer")
    print ("===============")
    pil = int (input("masukkan pilihan :"))
    if pil == 1:
        saldo = 100000000
        print ("saldo yang anda miliki",saldo,"rupiah")
    elif pil == 2:
        norek = int(input("masukkan rekening tujuan :"))
        nominal = int(input("masukkan nominal transfer :"))
        saldo = 100000000
        if saldo == 0:
            print ("saldo yang anda miliki tidak cukup")
        else:
            if nominal > 10000:
                print ("transfer senilai",nominal ,"berhasil")
            else:
                print ("TIDAK DAPAT MELAKUKAN TRANSAKSI")
    else:
        print ("pilihan yang anda masukkan salah.")
    
else:
    print ("LOGIN GAGAL")
