# Contoh sesudah refactoring: fungsi terpisah dan format dipakai ulang.
def saring_tugas(daftar_tugas):
    # Mengambil tugas dengan kolom wajib yang terisi.
    tugas_valid = []
    for tugas in daftar_tugas:
        if tugas[0] != "" and tugas[1] != "" and tugas[2] != "":
            tugas_valid.append(tugas)
    return tugas_valid


def format_tugas(tugas):
    # Membentuk satu baris dengan format yang dipakai di dua tempat.
    return tugas[0] + " | " + tugas[1] + " | Tenggat: " + tugas[2] + " | Status: " + tugas[3]


def buat_laporan(daftar_tugas, jumlah_belum_selesai):
    # Menyusun isi laporan secara terpisah dari alur utama.
    isi_laporan = "LAPORAN DAFTAR TUGAS KULIAH\n"
    isi_laporan += "============================\n"
    for tugas in daftar_tugas:
        isi_laporan += format_tugas(tugas) + "\n"
    isi_laporan += "Jumlah tugas belum selesai: " + str(jumlah_belum_selesai) + "\n"
    return isi_laporan


def main():
    # Nama variabel menjelaskan data yang disimpan.
    daftar_tugas = [
        ["Mengerjakan tugas Python", "Pemrograman", "2026-10-20", "Belum selesai"],
        ["Membaca Bab 2", "Matematika", "2026-10-18", "Selesai"],
    ]
    tugas_valid = saring_tugas(daftar_tugas)
    tugas_urut = sorted(tugas_valid, key=lambda tugas: tugas[0])
    jumlah_belum_selesai = 0
    for tugas in tugas_urut:
        if tugas[3] == "Belum selesai":
            jumlah_belum_selesai += 1
    print("DAFTAR TUGAS KULIAH")
    for tugas in tugas_urut:
        print(format_tugas(tugas))
    isi_laporan = buat_laporan(tugas_urut, jumlah_belum_selesai)
    with open("laporan_refactoring.txt", "w") as file:
        file.write(isi_laporan)
    print(isi_laporan)


if __name__ == "__main__":
    main()
