# Contoh sebelum refactoring: nama pendek dan alur panjang.
a = [
    ["Mengerjakan tugas Python", "Pemrograman", "2026-10-20", "Belum selesai"],
    ["Membaca Bab 2", "Matematika", "2026-10-18", "Selesai"],
]
b = []
for c in a:
    if c[0] != "" and c[1] != "" and c[2] != "":
        b.append(c)
b = sorted(b, key=lambda x: x[0])
d = 0
for e in b:
    if e[3] == "Belum selesai":
        d += 1
print("DAFTAR TUGAS KULIAH")
for g in b:
    print(g[0] + " | " + g[1] + " | Tenggat: " + g[2] + " | Status: " + g[3])
f = "LAPORAN DAFTAR TUGAS KULIAH\n"
f += "============================\n"
for g in b:
    f += g[0] + " | " + g[1] + " | Tenggat: " + g[2] + " | Status: " + g[3] + "\n"
f += "Jumlah tugas belum selesai: " + str(d) + "\n"
with open("laporan_refactoring.txt", "w") as h:
    h.write(f)
print(f)
