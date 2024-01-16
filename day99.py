x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))
if x == 1:
    if y == 2:
        if z == 3:
            print("Semua bilangan sama")
        else:
            print("Hanya dua bilangan pertama yang sama")
    else:
        print("Hanya bilangan pertama yang sama")
else:
    print("Tidak ada bilangan yang sama")

w = (x + y) ** z
print("w = ", w)
