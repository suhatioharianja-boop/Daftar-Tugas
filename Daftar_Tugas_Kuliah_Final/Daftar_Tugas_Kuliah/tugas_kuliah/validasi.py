# Memeriksa data tugas sebelum disimpan.
def validasi_data(nama_tugas, mata_kuliah, tenggat, status):
    # Menolak isian wajib yang kosong.
    if not nama_tugas.strip() or not mata_kuliah.strip() or not tenggat.strip():
        raise ValueError("Nama tugas, mata kuliah, dan tenggat wajib diisi.")
    # Menerima hanya status yang dikenal program.
    if status not in ("Belum selesai", "Selesai"):
        raise ValueError("Status harus 'Belum selesai' atau 'Selesai'.")
    return True
