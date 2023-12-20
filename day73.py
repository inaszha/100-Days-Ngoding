def nilai_terkecil(array):
  terkecil = array[0]
  for i in range(1, len(array)):
    if array[i] < terkecil:
      terkecil = array[i]
  return terkecil
array = [1, 2, 9, 4, 7]
print(nilai_terkecil(array))
