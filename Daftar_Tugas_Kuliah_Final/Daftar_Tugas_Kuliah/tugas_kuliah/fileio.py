# Menangani operasi file menggunakan with open().
def buat_file(nama_file):
    # Mode x membuat file baru tanpa menimpa file yang sudah ada.
    try:
        with open(nama_file, "x") as file:
            file.write("")
        print("File tugas berhasil dibuat.")
    except FileExistsError:
        print("File tugas sudah ada. Data lama tetap aman.")


def tambah_baris(nama_file, baris):
    # Mode a menambahkan data baru pada akhir file.
    with open(nama_file, "a") as file:
        file.write(baris + "\n")


def baca_data(nama_file):
    # Mode r membaca file secara iteratif baris demi baris.
    daftar_baris = []
    with open(nama_file, "r") as file:
        for baris in file:
            if baris.strip():
                daftar_baris.append(baris.strip())
    return daftar_baris


def tulis_laporan(nama_file, isi_laporan):
    # Mode w menulis atau menimpa file laporan.
    with open(nama_file, "w") as file:
        file.write(isi_laporan)
