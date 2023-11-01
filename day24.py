# bu kartini menyuruh ucup membeli buah apel di toko buah SEJAHTERA sebanyak 20kg, anggur 18kg, rambutan 17kg dan  jeruk 29kg

# Harga 1 buah apel 5ribu rupiah, berat 1 buah apel rata2 adalah 200gram
# Harga anggur 100gram = 3ribu, Harga rambutan 1kg 15.000, Harga jeruk per 3 kilo adalah 45ribu

# karena si ucup membeli banyak buah - buahan maka ia diberikan tambah setiap 5kg dari buah tersebut maka akan mendapat tambahan bonus 0.5Kg (hitung total bonus dari masing2 buah-buahan)

# dan ucup juga mendapatkan diskon sebesar 0.2% untuk pembelian buah yang melebihi 20kg buah

# hitung total ucup membayar pada toko buah SEJAHTERA

# Jelaskan secara rinci untuk output program yakni Harga dari masing2 buah, Harga total, total Diskon, total Bonus
def getBonus(jumlahBuah):
    bonus = (jumlahBuah // 5) * 0.5
    return bonus

def getHarga(jumlahBuah, hargaBuah):
    if jumlahBuah > 20 :
        diskon = hargaBuah * 0.2
    else :
        diskon = 0
    hargaTotal = jumlahBuah * hargaBuah - diskon
    return hargaTotal

jumlahApel = 20
jumlahAnggur = 18
jumlahRambutan = 17
jumlahJeruk = 29

bonusApel = getBonus(jumlahApel)
bonusAnggur = getBonus(jumlahAnggur)
bonusRambutan = getBonus(jumlahRambutan)
bonusJeruk = getBonus(jumlahJeruk)

SatuApel =  5000
satuKilo = 1000
sekiloApel = satuKilo / 200 * SatuApel
hargaAnggur100Gr = 3000
sekiloAnggur = hargaAnggur100Gr + 10
sekiloRambutan =  15000
sekiloJeruk = 45000 / 3

totalHargaApel = getHarga(jumlahApel, sekiloApel)
totalHargaAnggur = getHarga(jumlahAnggur, sekiloAnggur)
totalHargaRambutan = getHarga(jumlahRambutan, sekiloRambutan)
totalHargaJeruk = getHarga(jumlahJeruk, sekiloJeruk)

totalBayar = totalHargaApel + totalHargaAnggur + totalHargaRambutan + totalHargaJeruk

print("Total harga Apel",totalHargaApel)
print("Total harga Anggur",totalHargaAnggur)
print("Total harga Rambutan",totalHargaRambutan)
print("Total harga Jeruk",totalHargaJeruk)
print("Total Bayar : ",totalBayar)

jumlahApelWithBonus = 20 + bonusApel
jumlahAnggurWithBonus = 18 + bonusAnggur
jumlahRambutanWithBonus = 17 + bonusRambutan
jumlahJerukWithBonus = 29 + bonusJeruk
print("Jumlah Buah Apel",jumlahApelWithBonus, "Kg")
print("Jumlah Buah Anggur",jumlahAnggurWithBonus, "Kg")
print("Jumlah Buah Rambutan",jumlahRambutanWithBonus, "Kg")
print("Jumlah Buah Jeruk",jumlahJerukWithBonus, "Kg")
