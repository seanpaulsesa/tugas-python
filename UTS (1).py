DaftarMenu = {"Kecap": 13000, "Teh Kotak": 7000, "Aqua": 5000, "Pensil": 2000, "Kopi": 12000, "Momogi": 5500, "Susu Beruang": 10500, "Coca-cola": 6000}

print("Daftar Menu")
print("..::=============================================::..")
for item, price in DaftarMenu.items():
    print(f"{item}: Rp{price}")

jumlah = input("Masukkan jumlah barang yang ingin dibeli: ")
TotalHarga = 0 
for i in range(int(jumlah)):
    pilihan = input(f"Masukkan nama barang {i+1}: ")
    if pilihan in DaftarMenu:
        print(f"{pilihan} = Rp{DaftarMenu[pilihan]}")
        TotalHarga += DaftarMenu[pilihan]
    else:
        print("Barang tidak tersedia")

print (f"Total Harga: Rp{TotalHarga}")
UangDibawa = int(input("Masukkan uang yang di bayar: "))
kembalian = UangDibawa - TotalHarga
print(f"Kembalian: Rp{kembalian}")