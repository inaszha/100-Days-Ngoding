batas = int(input("batas: "))
if batas == 1 or batas == 2:
    print("Kosong")
for i in range(1,batas):
    if i %3 == 0:
        print(i)
        
