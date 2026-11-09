penjualan = [120, 150, 135, 180, 160]

print("\n========================================================\n")
print("1. Owner mengganti data penjualan hari ketiga dari 135 menjadi 140")
penjualan[2] = 140
print("Data penjualan setelah diganti:", penjualan)

print("\n========================================================\n")
print("2. Owner menambahkan data penjualan hari keenam sebesar 175")
penjualan.append(175)
print("Data penjualan setelah ditambahkan:", penjualan)

print("\n========================================================\n")
print("3. Owner menambahkan data penjualan hari ketiga sebesar 155")
penjualan.insert(2, 155)
print("Data penjualan setelah ditambahkan:", penjualan)

print("\n========================================================\n")
print("4. Owner menghapus data penjualan hari kedua")
penjualan.pop(1)
print("Data penjualan setelah dihapus:", penjualan)

print("\n========================================================\n")

print("5. Hitung:\n- Total produk yang terjual.\n- Total pendapatan kotor.\n- Biaya platform yang merupakan 5% dari pendapatan.\n- Pendapatan bersih.\n- Penjualan tertinggi.\n- Penjualan terendah.\n")

# Total produk yang terjual
total_produk = sum(penjualan)
print("- Total produk yang terjual:", total_produk)

# Total pendapatan kotor
total_pendapatan = sum(penjualan) * 75000
print("- Total pendapatan kotor: Rp. ", total_pendapatan)

# Biaya platform yang merupakan 5% dari pendapatan
biaya_platform = total_pendapatan * 0.05
print("- Biaya platform (5% dari pendapatan): Rp.", int(biaya_platform))

# Pendapatan bersih
pendapatan_bersih = total_pendapatan - biaya_platform
print("- Pendapatan bersih: Rp.", int(pendapatan_bersih))

# Penjualan tertinggi
penjualan_tertinggi = max(penjualan)
print("- Penjualan tertinggi:", penjualan_tertinggi)

# Penjualan terendah
penjualan_terendah = min(penjualan)
print("- Penjualan terendah:", penjualan_terendah)

# Selisih antara penjualan tertinggi dan terendah
selisih_penjualan = penjualan_tertinggi - penjualan_terendah
print("- Selisih antara penjualan tertinggi dan terendah:", selisih_penjualan)

print("\n========================================================\n")