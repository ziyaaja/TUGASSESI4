def celsius_ke_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_ke_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan jenis satuan (C untuk Celsius, F untuk Fahrenheit): ").upper()

if satuan == 'C':
    fahrenheit = celsius_ke_fahrenheit(suhu)
    print("{:.2f} Celsius setara dengan {:.2f} Fahrenheit".format(suhu, fahrenheit))
elif satuan == 'F':
    celsius = fahrenheit_ke_celsius(suhu)
    print("{:.2f} Fahrenheit setara dengan {:.2f} Celsius".format(suhu, celsius))
else:
    print("Jenis satuan yang dimasukkan tidak valid. Masukkan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")
