bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))
bilangan3 = float(input("Masukkan bilangan ketiga: "))

if bilangan1 > bilangan2 and bilangan1 > bilangan3:
    print("Bilangan pertama ({}) lebih besar dari bilangan kedua ({}) dan bilangan ketiga ({})".format(bilangan1, bilangan2, bilangan3))
elif bilangan2 > bilangan1 and bilangan2 > bilangan3:
    print("Bilangan kedua ({}) lebih besar dari bilangan pertama ({}) dan bilangan ketiga ({})".format(bilangan2, bilangan1, bilangan3))
elif bilangan3 > bilangan1 and bilangan3 > bilangan2:
    print("Bilangan ketiga ({}) lebih besar dari bilangan pertama ({}) dan bilangan kedua ({})".format(bilangan3, bilangan1, bilangan2))
else:
    print("Semua bilangan ({}, {}, {}) sama besar".format(bilangan1, bilangan2, bilangan3))
