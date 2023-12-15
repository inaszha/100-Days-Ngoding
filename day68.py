batas = int(input("batas: "))
if batas %2==0:
	print("angka genap")
else:
	for i in range(batas):
		if i %2 == 1:
			print(i)
	
