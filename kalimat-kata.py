def hitung_huruf(teks):
    huruf_dict = {}

    for karakter in teks:
        if karakter.isalpha():  # Hanya menghitung huruf
            karakter = karakter.lower()  # Mengubah menjadi huruf kecil untuk konsistensi
            if karakter in huruf_dict:
                huruf_dict[karakter] += 1
            else:
                huruf_dict[karakter] = 1

    return huruf_dict

# Input dari pengguna
teks_input = input("Masukkan sebuah kata atau kalimat: ")

# Proses dan output
hasil = hitung_huruf(teks_input)
print("\nHuruf yang terdapat pada input dan jumlahnya:")
for huruf, jumlah in hasil.items():
    print(f"{huruf} : {jumlah}")

