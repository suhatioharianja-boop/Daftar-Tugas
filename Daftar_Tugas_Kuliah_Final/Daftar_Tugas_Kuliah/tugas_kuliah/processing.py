# Membentuk dan menganalisis data tugas.
class Tugas:
    # Menyimpan satu tugas beserta atribut tambahannya.
    def __init__(self, nama_tugas, mata_kuliah, tenggat, **kwargs):
        # Menyimpan informasi wajib dan atribut fleksibel.
        self.nama_tugas = nama_tugas
        self.mata_kuliah = mata_kuliah
        self.tenggat = tenggat
        self.atribut = kwargs
        if "status" not in self.atribut:
            self.atribut["status"] = "Belum selesai"

    def buat_baris(self):
        # Mengubah semua atribut tugas menjadi satu baris file.
        bagian = [self.nama_tugas, self.mata_kuliah, self.tenggat]
        for kunci, nilai in self.atribut.items():
            bagian.append(kunci + "=" + str(nilai))
        return ",".join(bagian)


def buat_record(nama_tugas, mata_kuliah, tenggat, **kwargs):
    # kwargs menerima atribut beragam seperti status dan catatan.
    tugas = Tugas(nama_tugas, mata_kuliah, tenggat, **kwargs)
    return tugas.buat_baris()


def baca_record(baris):
    # Membaca kolom utama dan semua atribut key=value.
    bagian = baris.split(",")
    if len(bagian) < 3:
        raise ValueError("Format data tugas tidak lengkap.")
    tugas = {
        "nama_tugas": bagian[0].strip(),
        "mata_kuliah": bagian[1].strip(),
        "tenggat": bagian[2].strip(),
        "status": "Belum selesai",
        "catatan": "",
    }
    for atribut in bagian[3:]:
        if "=" not in atribut:
            raise ValueError("Format atribut tugas tidak valid.")
        kunci, nilai = atribut.split("=", 1)
        tugas[kunci.strip()] = nilai.strip()
    return tugas


def hitung_jumlah(*status_tugas):
    # args menerima sejumlah status untuk dihitung.
    jumlah_belum_selesai = 0
    for status in status_tugas:
        if status == "Belum selesai":
            jumlah_belum_selesai += 1
    return jumlah_belum_selesai


def analisis_data(daftar_baris):
    # Melewati baris rusak dan mengolah baris yang valid.
    daftar_tugas = []
    for baris in daftar_baris:
        try:
            tugas = baca_record(baris)
            if tugas["status"] not in ("Belum selesai", "Selesai"):
                raise ValueError("Status tugas tidak valid.")
            daftar_tugas.append(tugas)
        except (ValueError, IndexError) as error:
            print("Baris dilewati:", error, "->", baris)
    # Lambda mengurutkan tugas berdasarkan nama.
    daftar_tugas = sorted(daftar_tugas, key=lambda tugas: tugas["nama_tugas"])
    status_tugas = [tugas["status"] for tugas in daftar_tugas]
    jumlah_belum_selesai = hitung_jumlah(*status_tugas)
    assert jumlah_belum_selesai <= len(daftar_tugas), "Jumlah tugas tidak sesuai."
    return daftar_tugas, jumlah_belum_selesai
