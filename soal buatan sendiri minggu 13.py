# Aloysius Gonzaga Ardhian Krisna Aji
# 71180298

# Referensi : https://jagongoding.com
# Bayu ingin membuat soal perpangkatan menggunakan rekursif,
# sebagai temannya bayu kamu harus membantunya.

# input : angka dan pangk
# output : hasil pangkat

def hitPangkat(bilangan,pangkat):
    if pangkat == 0:
        return 1
    else:
        return bilangan * hitPangkat(bilangan,pangkat -1)

bilangan = int(input("Masukan angka: "))
pangkat = int(input("Masukan pangkat: "))

print(hitPangkat(bilangan,pangkat))

