panjang = int(input("panjang: "))
angka = []
for i in range(panjang):
	nilai = int(input("nilai: "))
	if nilai %2 == 0:
		angka.append(nilai)
print("genap: ",angka)
