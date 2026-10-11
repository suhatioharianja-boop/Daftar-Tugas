# Mengatur alur aplikasi daftar tugas.
from . import fileio, processing, validasi


class DaftarTugas:
    # Mengelola file dan daftar tugas.
    def __init__(self, nama_file):
        # Menyimpan nama file data yang dipakai aplikasi.
        self.nama_file = nama_file

    def buat_file(self):
        # Membuat file data dengan mode x.
        fileio.buat_file(self.nama_file)

    def tambah_data(self, nama_tugas, mata_kuliah, tenggat, **kwargs):
        # Memvalidasi tugas sebelum membuat dan menyimpan record.
        status = kwargs.get("status", "Belum selesai")
        validasi.validasi_data(nama_tugas, mata_kuliah, tenggat, status)
        baris = processing.buat_record(nama_tugas, mata_kuliah, tenggat, **kwargs)
        fileio.tambah_baris(self.nama_file, baris)
        print("Tugas berhasil disimpan.")

    def tambah_dari_input(self):
        # Membaca input dan menampilkan pesan saat input tidak valid.
        try:
            nama_tugas = input("Nama tugas: ")
            mata_kuliah = input("Mata kuliah: ")
            tenggat = input("Tenggat (contoh 2026-10-20): ")
            status = input("Status (Belum selesai/Selesai): ")
            catatan = input("Catatan (boleh kosong): ")
            self.tambah_data(nama_tugas=nama_tugas, mata_kuliah=mata_kuliah, tenggat=tenggat, status=status, catatan=catatan)
        except ValueError as error:
            print("Data tidak valid:", error)

    def ambil_data(self):
        # Membaca dan menganalisis file, termasuk saat file belum ada.
        try:
            daftar_baris = fileio.baca_data(self.nama_file)
        except FileNotFoundError:
            print("File data belum ada. Pilih menu 1 untuk membuatnya.")
            return [], 0
        return processing.analisis_data(daftar_baris)

    def tampilkan_tugas(self):
        # Menampilkan daftar tugas dan jumlah yang belum selesai.
        daftar_tugas, jumlah_belum_selesai = self.ambil_data()
        if not daftar_tugas:
            print("Belum ada data tugas untuk ditampilkan.")
            return
        print("\nDaftar tugas:")
        for tugas in daftar_tugas:
            print(tugas["nama_tugas"], "|", tugas["mata_kuliah"], "| Tenggat:", tugas["tenggat"], "| Status:", tugas["status"], "| Catatan:", tugas["catatan"])
        print("Jumlah tugas belum selesai:", jumlah_belum_selesai)
        print("Jumlah seluruh tugas:", len(daftar_tugas))

    def buat_laporan(self):
        # Menulis daftar dan ringkasan ke file laporan.
        daftar_tugas, jumlah_belum_selesai = self.ambil_data()
        if not daftar_tugas:
            return
        isi_laporan = "LAPORAN DAFTAR TUGAS KULIAH\n"
        isi_laporan += "============================\n"
        for tugas in daftar_tugas:
            isi_laporan += tugas["nama_tugas"] + " | " + tugas["mata_kuliah"] + " | Tenggat: " + tugas["tenggat"] + " | Status: " + tugas["status"] + " | Catatan: " + tugas["catatan"] + "\n"
        isi_laporan += "Jumlah tugas belum selesai: " + str(jumlah_belum_selesai) + "\n"
        fileio.tulis_laporan("laporan_tugas.txt", isi_laporan)
        print("Laporan tersimpan di laporan_tugas.txt")
