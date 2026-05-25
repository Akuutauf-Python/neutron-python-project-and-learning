# menyiapkan data riwayat_transaksi 
transaksi = []

# format data transaksi nya
# nama_transaksi (contoh: gaji januari 2026/liburan ke bali)
# tipe (pemasukan/pengeluaran)
# jumlah (nominal uang, tanpa titik)
# kategori (nama kategori nya apa)

def tambah_pemasukan():
    nama = input("Masukkan nama pemasukan: ")
    jumlah = int(input("Masukkan jumlah nominal: "))
    kategori = input("Masukkan Kategori (contoh gaji, dll): ")

    # akan menambahkan data baru di belakang pada dictionary
    transaksi.append({
        "tipe": "pemasukan", # tipe pemasukan
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori
    })

def tambah_pengeluaran():
    nama = input("Masukkan nama pengeluaran: ")
    jumlah = int(input("Masukkan jumlah nominal: "))
    kategori = input("Masukkan Kategori (contoh gaji, dll): ")

    # akan menambahkan data baru di belakang pada dictionary
    transaksi.append({
        "tipe": "pengeluaran", # tipe pengeluaran
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori
    })
    
def lihat_saldo():
    # membuat variabel untuk menghitung sisa saldo
    saldo = 0
    
    # melakukan perulangan pada riwayat / transaksi
    for item in transaksi:
        # menjumlahkan semua transaksi yang berjenis pemasukan
        if item["tipe"] == "pemasukan":
            saldo += item["jumlah"]
        # mengurangi semua transaksi yang berjenis pengeluaran
        else:
            saldo -= item["jumlah"]

    print("Saldo Anda saat ini: Rp.", saldo)

while True:
    print("===== SELAMAT DATANG =====")
    print("1. Input Pemasukan")
    print("2. Input Pengeluaran")
    print("3. Lihat Saldo")
    print("4. Keluar")

    menu = input("Silahkan Pilih Menu (nomor) : ")

    # implementasi percabangan
    if menu == "1":
        # memanggil dan menjalankan fungsi input pemasukan
        tambah_pemasukan()
        
        print("Kembali Ke Beranda >>>")
    elif menu == "2":
        # memanggil dan menjalankan fungsi input pengeluaran
        tambah_pengeluaran()
        
        print("Kembali Ke Beranda >>>")
    elif menu == "3":
        # memanggil dan menjalankan fungsi lihat saldo
        lihat_saldo()
        
        print("Kembali Ke Beranda >>>")
    elif menu == "4":
        # memanggil dan menjalankan break, untuk keluar program
        print("===== SAMPAI JUMPA LAGI =====")
        break # false