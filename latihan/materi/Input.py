# input
# menghitung luas lingkaran
# rumus : phi x r2

# inisiasi / assign
phi = 3.14

# input - nilai yang diambil string
r = float(input("Masukkan nilai jari jari (angka) = "))
print(type(r))

# proses
luasLingkaran = phi * (r ** 2)

# print biasa
print("Luas lingkaran adalah ", luasLingkaran)

# output (f-string)
print(f"Luas lingkaran adalah {luasLingkaran} iya nilainya = {luasLingkaran}")