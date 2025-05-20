def cari_kedua_terkecil_terbesar(data):
    # Menghilangkan duplikat dan mengurutkan data
    data_unik = sorted(set(data))

    if len(data_unik) < 2:
        return "List harus memiliki minimal 2 bilangan yang berbeda."

    kedua_terkecil = data_unik[1]
    kedua_terbesar = data_unik[-2]
# Soal 1: Pangkat dua dari 1 sampai 20
list_pangkat_dua = [x**2 for x in range(1, 21)]

# Menampilkan 5 elemen pertama dan 5 elemen terakhir
print("Lima elemen pertama:", list_pangkat_dua[:5])
print("Lima elemen terakhir:", list_pangkat_dua[-5:])

print("\n--- Soal 2: Bilangan Kedua Terkecil dan Kedua Terbesar ---")

# Soal 2: Menentukan bilangan kedua terkecil dan kedua terbesar
def cari_kedua_terkecil_terbesar(data):
    data_unik = sorted(set(data))  # Menghilangkan duplikat dan mengurutkan
    if len(data_unik) < 2:
        return "Data tidak memiliki cukup bilangan unik."
    return data_unik[1], data_unik[-2]

# Contoh list bilangan
bilangan = [10, 4, 6, 8, 2, 8, 4, 10, 15]
hasil = cari_kedua_terkecil_terbesar(bilangan)

if isinstance(hasil, tuple):
    print(f"Bilangan kedua terkecil: {hasil[0]}")
    print(f"Bilangan kedua terbesar: {hasil[1]}")
else:
    print(hasil)

    return kedua_terkecil, kedua_terbesar

# Contoh list bilangan
bilangan = [10, 4, 6, 8, 2, 8, 4, 10, 15]

hasil = cari_kedua_terkecil_terbesar(bilangan)

if isinstance(hasil, tuple):
    print(f"Bilangan kedua terkecil: {hasil[0]}")
    print(f"Bilangan kedua terbesar: {hasil[1]}")
else:
    print(hasil)
