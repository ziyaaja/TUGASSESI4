bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))
bilangan3 = float(input("Masukkan bilangan ketiga: "))

if bilangan1 <= bilangan2 and bilangan1 <= bilangan3:
    print("Bilangan pertama ({}) lebih kecil atau sama dengan bilangan kedua ({}) dan bilangan ketiga ({})".format(bilangan1, bilangan2, bilangan3))
elif bilangan2 <= bilangan1 and bilangan2 <= bilangan3:
    print("Bilangan kedua ({}) lebih kecil atau sama dengan bilangan pertama ({}) dan bilangan ketiga ({})".format(bilangan2, bilangan1, bilangan3))
else:
    print("Bilangan ketiga ({}) lebih kecil atau sama dengan bilangan pertama ({}) dan bilangan kedua ({})".format(bilangan3, bilangan1, bilangan2))
