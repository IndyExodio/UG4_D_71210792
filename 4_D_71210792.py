bilangan = input("Masukkan sekumpulan bilangan (pisahkan dengan koma): ")
list = list(map(int, bilangan.split(',')))

terbesar = max(list, key=lambda x: x)
terkecil = min(list, key=lambda x: x)

print(f"Bilangan terbesar dari kumpulan bilangan yang di input adalah {terbesar}")
print(f"Bilangan terkecil dari kumpulan bilangan di input adalah {terkecil}")
