# 1

buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

print("Ganti nama ceri jadi cherry")
print("Sebelum diganti:", buah)
buah[2] = "cherry"
print("Sesudah diganti:", buah)

# 2
print("\nMasukkan nama buah baru dan indeksnya untuk menambahkannya ke list.")
nama_buah = input("Masukkan nama buah: ")
index = int(input("Masukkan indeks (0-6): "))
buah.insert(index, nama_buah)
print("List buah setelah diperbarui:", buah)

# 3
print("\nMengurutkan list buah secara alfabet.")
print(buah) #list sebelum diurutkan
buah.sort()
print(buah) #list setelah diurutkan