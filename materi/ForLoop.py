# Perulangan (loop)

# for kondisi:
#     aksi

# penerapan dengan list
angka_list = [0,1,2,3,4]
print(angka_list)
print(type(angka_list))
print(len(angka_list))

# lakukan perulangan
for i in angka_list:
    print(f"Nilai i sekarang adalah : {i}")
    
print("Akhir dari program 1 \n")

# penerapan dengan range
angka_range = range(1,10)
print(angka_range)
print(type(angka_range))

for i in angka_range:
    print(f"i sekarang adalah : {i}")
    
print("Akhir dari program 2 \n")

# menggunakan string
data_str = "Belajar Python"

for huruf in data_str:
    print(f"{huruf}")
    
print("Akhir dari program 3 \n")