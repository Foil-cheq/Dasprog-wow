# Tugas Mandiri Praktikum 

# 1
nilai = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

# 1. Nilai maksimum, minimun, dan rata-rata
nilai_maksimum = max(nilai)
nilai_minimum = min(nilai)
rata_rata = sum(nilai) / len(nilai)

print("1. Nilai maksimum, minimum, dan rata-rata dari daftar nilai:")
print("Nilai maksimum:", nilai_maksimum)
print("Nilai minimum:", nilai_minimum)
print("Rata-rata nilai:", rata_rata)

# 2. Angka terbesar kedua
nilai_terbesar_kedua = sorted(set(nilai))[-2]
print("\n2. Angka terbesar kedua dari daftar nilai:", nilai_terbesar_kedua)

print("\n========================================================\n")


# 2

# Daftar pasangan (latitude, longitude) dari beberapa kota
kota = [
    ("Jakarta", -6.2088, 106.8456),
    ("Bandung", -6.9175, 107.6191),
    ("Surabaya", -7.2575, 112.7521)]

# A. Menampilkan kordinat kita bandung
kordinat_bandung = kota[1]  # Index 1 untuk Bandung
print("\nA. Menampilkan koordinat kota Bandung:")
print("Latitude:", kordinat_bandung[1])
print("Longitude:", kordinat_bandung[2])

# B. Tampilkan jumlah lokasi yang tesimpan
jumlah_lokasi = len(kota)
print("\nB. Jumlah lokasi yang tersimpan:", jumlah_lokasi)

print("\n========================================================\n")

# 3

# Masukkan 10 nama dalam satu baris lalu simpan kedalam list
nama_input = input("Masukkan 10 nama (pisahkan dengan koma): ")
nama_list = [nama.strip() for nama in nama_input.split(",")]
print("\n3. List nama yang dimasukkan:", nama_list)