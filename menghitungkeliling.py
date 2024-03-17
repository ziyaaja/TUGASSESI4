import math

def hitung_luas(sisi_a, sisi_b, sisi_c):
    s = (sisi_a + sisi_b + sisi_c) / 2

    luas = math.sqrt(s * (s - sisi_a) * (s - sisi_b) * (s - sisi_c))
    return luas

def hitung_keliling(sisi_a, sisi_b, sisi_c):
    keliling = sisi_a + sisi_b + sisi_c
    return keliling

sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))
sisi_c = float(input("Masukkan panjang sisi c: "))

luas = hitung_luas(sisi_a, sisi_b, sisi_c)
keliling = hitung_keliling(sisi_a, sisi_b, sisi_c)

print("Luas segitiga: {:.2f}".format(luas))
print("Keliling segitiga: {:.2f}".format(keliling))
