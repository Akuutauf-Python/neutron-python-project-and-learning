# fungsi dengan return
# fungsi dengan implementasi return code akan mengembalikan nilai
# ketika memanggil fungsi yang memiliki return disarankan di simpan ke dalam variabel

# fungsi dengan single return
def perkalian(bil_a, bil_b):
    # proses aritmatika perkalian
    return bil_a * bil_b
    
print(perkalian(10, 4))

hasilPerkalian = perkalian(10, 5)
print(f"Hasil Perkalian = {hasilPerkalian}")

# fungsi dengan multiple return
def operasi_aritmatika(x, y):
    # proses aritmatika: penjumlahan, pengurangan, perkalian dan pembagian
    hasilPenjumlahan = x + y
    hasilPengurangan = x - y
    hasilPerkalian = x * y
    hasilPembagian = x / y
    
    return hasilPenjumlahan, hasilPengurangan, hasilPerkalian, hasilPembagian

a, b, c, d = operasi_aritmatika(10,2)

print()
print(f"Hasil penjumlahan = {a}")
print(f"Hasil pengurangan = {b}")
print(f"Hasil perkalian = {c}")
print(f"Hasil pembagian = {d}")