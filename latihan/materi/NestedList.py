# nested list
data_0 = [1,2]
data_1 = [3,4]

# data list 1D
data_list_normal = [1,2,3,4]
print(f"Data list biasa = {data_list_normal}")

# data list 2D 
data_list_2d = [data_0, data_1, data_list_normal]
print(f"Data list 2D = {data_list_2d}")

# contoh penerapan
print()
data_peserta_0 = ["Taufik", 25, "Laki-laki"]
data_peserta_1 = ["Ilham", 17, "Laki-laki"]
data_peserta_2 = ["Dwi", 20, "Perempuan"]
data_list_peserta = [data_peserta_0, data_peserta_1, data_peserta_2]

# tampilkan menggunakan perulangan
for peserta in data_list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")