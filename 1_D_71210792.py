def aritmatika(awal, selisih, suku):
    an = awal + (suku-1)*selisih
    total = suku/2 * (awal + an)
    return total

print("="*20,"BARIS ARITMATIKA","="*20)
a = float(input("Masukkan bilangan awal : "))
b = float(input("Masukkan selisih bilangan : "))
s = float(input("Masukkan banyaknya suku : "))

hasil = aritmatika(a, b, s)
print("Total dari deret aritmatika tersebut adalah:", hasil)
