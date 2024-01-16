def persamaan_kuadrat(a, b, c):
  d = b**2 - 4 * a * c
  if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2
  else:
    return None, None


a = int(input("Angka a: "))
b = int(input("Angka b: "))
c = int(input("Angka c: "))

x1, x2 = persamaan_kuadrat(a, b, c)

if x1 is not None:
  print("Hasil Persamaan Kuadrat adalah {0} dan {1}".format(x1, x2))
else:
  print("Persamaan Kuadrat tidak memiliki akar real")
