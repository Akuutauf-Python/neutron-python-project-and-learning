# Program Menghitung Luas Persegi
print("===== Program Menghitung Luas Persegi =====")

while True:
    # Input nilai sisi persegi
    try:
        sisi = int(input("Masukkan nilai jari-jari: "))
    except ValueError:
        print("Input harus angka!")
        continue
    
    # Proses perhitungan luas persegi
    luas_persegi = sisi * sisi

    # Menampilkan hasil luas persegi
    print("Hasil Luas Persegi:", luas_persegi)
    
    while True:
        # Menanyakan apakah ingin lanjut atau tidak
        lanjut = input("Apakah ingin melanjutkan perhitungan lagi? (Y/T): ").strip().lower()
        
        if lanjut == "y":
            # melanjutkan ke perhitungan lagi
            break 
        elif lanjut == "t":
            # menghentikan program sepenuhnya\
            print("===== Program Selesai =====")
            exit()
        else:
            print("Input yang anda berikan tidak valid")
        