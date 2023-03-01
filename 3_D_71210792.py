def kata_terpanjang(kata):
    kata = kata.strip()
    kalimat = kata.split()
    kata_terpanjang = max(kalimat, key=len)
    return kata_terpanjang

kata = input("Masukkan sebuah kalimat: ")
kata_terpanjang = kata_terpanjang(kata)
print("Kata terpanjang dalam kalimat tersebut adalah:", kata_terpanjang)