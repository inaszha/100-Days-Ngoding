daftar_nama=[]
while True:
    nama = input("nama: ")
    if nama == "":
        print("kosong")
    elif nama == "selesai":
        break
    else:
        print("nama saya: ",nama)
    daftar_nama.append(nama)
    print(daftar_nama)
        
