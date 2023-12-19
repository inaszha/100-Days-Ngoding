array1 = [6, 8, 6, 8]
array2 = [1, 3, 5, 7]

hasil = [a * b for a, b in zip(array1, array2)]
print("Array 1:", array1)
print("Array 2:", array2)
print("Hasil Perkalian:", hasil)
