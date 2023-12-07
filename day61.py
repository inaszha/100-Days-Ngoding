data_nidn = []
while True:
    nidn = input("masukkan nidn: ")
    if nidn == "":
        break
    data_nidn.append(nidn)
data_nidn.sort()
print(data_nidn)
