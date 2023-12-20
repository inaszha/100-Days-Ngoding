nilai_ujian = []
for i in range(5):
  nilai = int(input("Masukkan nilai ujian siswa: "))
  nilai_ujian.append(nilai)
jumlah_lulus = 0
for nilai in nilai_ujian:
  if nilai >= 70:
    jumlah_lulus += 1
jumlah_tidak_lulus = 5 - jumlah_lulus
print("Jumlah siswa yang lulus:", jumlah_lulus)
print("Jumlah siswa yang tidak lulus:", jumlah_tidak_lulus)
