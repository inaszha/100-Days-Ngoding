angka = []

def tambah(data):
    angka.append(data)

def delete(select, data):
    if select == 1:
        angka.pop(data)
    if select == 2:
        angka.remove(data)

while True:
    print('''
1. Tambah Data
2. Delete
3. Exit       
          ''')

    print(angka)
    pilihan = int(input("Pilih Menu : "))
    if pilihan == 1:
        data = int(input("Masukkan Angka : "))
        tambah(data)
    elif pilihan == 2:
        pilih = int(input('''
1. Berdasarkan index
2. Berdasarkan Value
                        \n
Masukkan Pilihan menu :                                     
'''))
        data = int(input("Masukkan Angka : "))
        if pilih == 1:
            delete(1, data)
        else :
            delete(2, data)
    else:
        break
