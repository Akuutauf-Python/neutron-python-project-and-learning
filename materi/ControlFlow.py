# control flow: pass, continue, dan break

# pass: mengabaikan dan tidak akan di jalankan (dummy)
angka = 0

while angka < 5:
    angka += 1
    
    if angka == 3:
        pass # tidak akan di eksekusi
    
    print(angka)  
    
print("Akhir dari Pass \n")

# continue: akan membuat perulangan yang sekarang, melanjutkan iterasi berikutnya
# tanpa melanjutkan aksi dibawah nya
angka = 0

while angka < 5:
    angka += 1
    print(angka)
    
    if angka == 3:
        print("Bagus")
        continue
    
    print("Lanjutkan perulangan...")
    
print("Akhir dari Continue \n")

# break : digunakan untuk menghentikan perulangan secara total
# studi kasus : untuk pencarian data
angka = 0

while angka < 5:
    angka += 1
    
    if angka == 3:
        break
    
    print(angka)

