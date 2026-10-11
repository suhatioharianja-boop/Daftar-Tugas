# Pengujian unit untuk program daftar tugas.
import unittest
from . import processing, validasi


class TestDaftarTugas(unittest.TestCase):
    # Menguji fungsi penghitungan jumlah tugas.
    def test_hitung_status(self):
        self.assertEqual(processing.hitung_jumlah("Belum selesai", "Selesai"), 1)

    # Menguji hasil saat belum ada status yang diberikan.
    def test_hitung_tanpa_status(self):
        self.assertEqual(processing.hitung_jumlah(), 0)

    # Menguji kwargs untuk status dan catatan tambahan.
    def test_buat_record_dengan_kwargs(self):
        hasil = processing.buat_record("Baca Bab 1", "Petruk", "2026-10-20", status="Selesai", catatan="Bab pertama")
        self.assertEqual(hasil, "Baca Bab 1,Petruk,2026-10-20,status=Selesai,catatan=Bab pertama")

    # Menguji pembacaan atribut dari satu baris file.
    def test_baca_record_membaca_atribut(self):
        hasil = processing.baca_record("Tugas A,Python,2026-10-21,status=Selesai,catatan=Bab satu")
        self.assertEqual(hasil["status"], "Selesai")
        self.assertEqual(hasil["catatan"], "Bab satu")

    # Menguji analisis status tugas yang berbeda.
    def test_analisis_status(self):
        baris = ["Tugas A,Python,2026-10-20,status=Belum selesai", "Tugas B,Matematika,2026-10-21,status=Selesai"]
        daftar_tugas, jumlah = processing.analisis_data(baris)
        self.assertEqual(len(daftar_tugas), 2)
        self.assertEqual(jumlah, 1)

    # Menguji penolakan data dengan nama yang kosong.
    def test_validasi_nama_kosong(self):
        with self.assertRaises(ValueError):
            validasi.validasi_data("", "Petruk", "2026-10-20", "Belum selesai")


if __name__ == "__main__":
    unittest.main()
