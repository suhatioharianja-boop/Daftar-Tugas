# Program utama untuk mengelola daftar tugas kuliah.
from tugas_kuliah import DaftarTugas


def tampilkan_menu():
    # Menampilkan pilihan yang dapat digunakan pengguna.
    print("\n=== DAFTAR TUGAS KULIAH ===")
    print("1. Buat file data")
    print("2. Tambah tugas")
    print("3. Tampilkan tugas")
    print("4. Buat laporan")
    print("5. Keluar")


def main():
    # Membuat objek pengelola dan menjalankan menu sampai pengguna keluar.
    aplikasi = DaftarTugas(nama_file="data_tugas.txt")
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            aplikasi.buat_file()
        elif pilihan == "2":
            aplikasi.tambah_dari_input()
        elif pilihan == "3":
            aplikasi.tampilkan_tugas()
        elif pilihan == "4":
            aplikasi.buat_laporan()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia. Masukkan angka 1 sampai 5.")


if __name__ == "__main__":
    main()
