def batas(batasAngka):
	if batasAngka %2 == 0:
		print(batasAngka)
	else:
		for i in range(1,batasAngka +1):
			if i %2 !=0:
				print(i)
batasAngka = int(input("masukkan batas angka:"))
batas(batasAngka)
