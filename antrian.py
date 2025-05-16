from collections import deque

# Inisialisasi antrian pasien
pasien = deque()

print("=== APLIKASI ANTRIAN PASIEN ===")

while True:
    print("\nSilakan pilih perintah:")
    print("1. Menambah pasien")
    print("2. Memanggil pasien")
    print("3. Melihat daftar pasien")
    print("4. Keluar")

    perintah = input("Masukkan perintah (1/2/3/4): ")

    if perintah == '1':
        nama = input("Masukkan nama pasien: ")
        pasien.append(nama)
        print(f"Pasien '{nama}' berhasil ditambahkan ke antrian.")
    elif perintah == '2':
        if pasien:
            dipanggil = pasien.popleft()
            print(f"Pasien '{dipanggil}', silakan masuk ke ruang dokter.")
        else:
            print("Tidak ada pasien dalam antrian.")
    elif perintah == '3':
        if pasien:
            print("Daftar pasien dalam antrian:")
            for i, p in enumerate(pasien, start=1):
                print(f"{i}. {p}")
        else:
            print("Belum ada pasien dalam antrian.")
    elif perintah == '4':
        print("Terima kasih telah menggunakan aplikasi antrian.")
        break
    else:
        print("Perintah tidak dikenali, silakan coba lagi.")
