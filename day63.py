baris = int(input("Masukkan jumlah baris: "))
for i in range(1, baris + 1):
    for j in range(baris, i, -1):
        print(" ", end="")
    
    for k in range(1, i + 1):
        print(i, end="")
    
    print()
