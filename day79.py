daftar_nama = []
while True:
    nama = input("nama: ")
    if nama == "":
        break
    daftar_nama.append(nama)
daftar_nama.sort()
print(daftar_nama)
