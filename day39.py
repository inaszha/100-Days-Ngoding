penghasilan = float(input("masukkan penghasilan anda :"))
zakat = 2.5/100

if penghasilan >= 5000240:
    YgDiBayar = penghasilan * zakat
    print("anda wajib zakat dengan total zakat",YgDiBayar)
else:
    print("anda tidak wajib zakat")
