# Fungsi untuk membalik kata atau kalimat
def balik_teks(teks):
    return teks[::-1]

# Input dari pengguna
input_teks = input("Masukkan kata atau kalimat: ")

# Output hasil pembalikan
print("Hasil dibalik:", balik_teks(input_teks))


def balik_teks(teks):
    return teks[::-1]

# Contoh langsung
input_teks = "informatika"
output_teks = balik_teks(input_teks)

print("Input  :", input_teks)
print("Output :", output_teks)
