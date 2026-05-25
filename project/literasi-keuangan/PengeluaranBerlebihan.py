# aplikasi pencatatan uang sederhana
# studi kasus : Pengeluaran Berlebihan

# menyiapkan tempat untuk menyimpan data
transaksi = [
    # sengaja dikosongi sebagai template untuk pengguna nanti
    # {
    #     "nama": "Gaji minggu pertama",
    #     "tipe": "pemasukan",
    #     "jumlah": 100000,
    #     "kategori": "gaji"
    # },
]

# fitur 1 : Input pemasukan
def tambah_pemasukan():
    print("\n----- MENU PEMASUKAN >>>>>")
    nama = input("Masukkan nama pemasukan: ")
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    kategori = input("Kategori (contoh gaji, dll): ")

    # akan menambahkan data baru di belakang pada dictionary
    transaksi.append({
        "tipe": "pemasukan", # tipe pemasukan
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori
    })

# fitur 2 : Input pengeluaran
def tambah_pengeluaran():
    print("\n----- MENU PENGELUARAN >>>>>")
    nama = input("Masukkan nama pengeluaran: ")
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    kategori = input("Kategori: (contoh makan, transport, dll): ")

    # akan menambahkan data baru di belakang pada dictionary
    transaksi.append({
        "tipe": "pengeluaran", # tipe pengeluaran
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori
    })
    
    # logika peringatan
    total_pemasukan = 0
    total_pengeluaran = 0

    # menghitung (pemasukan - pengeluaran)
    for riwayat in transaksi:
        if riwayat["tipe"] == "pemasukan":
            total_pemasukan += riwayat["jumlah"]
        else:
            total_pengeluaran += riwayat["jumlah"]
            
    # cek kondisi pengeluaran berlebihan (boros)
    if total_pengeluaran > total_pemasukan:
        print("\n===================================================")
        print("⚠️\tPengeluaran Anda melebihi pemasukan!")
        print("===================================================")
    elif total_pengeluaran > total_pemasukan * 0.8:
        print("\n===================================================")
        print("⚠️\tPengeluaran sudah lebih dari 80% pemasukan!")
        print("===================================================")
    elif total_pengeluaran > total_pemasukan * 0.5:
        print("\n===================================================")
        print("⚠️\tPengeluaran sudah lebih dari 50% pemasukan!")
        print("===================================================")

# fitur 3 : Menampilkan saldo
def lihat_saldo():
    print("\n----- MENU SALDO >>>>>")
    
    # menyiapkan variabel untuk menghitung sisa saldo (pemasukan - pengeluaran)
    saldo = 0
    
    # melakukan perulangan pada riwayat / transaksi
    for riwayat in transaksi:
        # menjumlahkan semua transaksi yang berjenis pemasukan
        if riwayat["tipe"] == "pemasukan":
            saldo += riwayat["jumlah"]
        # mengurangi semua transaksi yang berjenis pengeluaran
        else:
            saldo -= riwayat["jumlah"]

    print("Saldo Anda saat ini: Rp.", saldo)
    
# fitur 4 : Riwayat transaksi
def lihat_riwayat():
    print("\n----- MENU RIWAYAT >>>>>")
    
    # jika data riwayat transaksi kosong
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return
    
    # jika tidak kosong untuk riwayat transaksi
    print("Nama - Tipe - Jumlah - Kategori")
    print("-------------------------------")
    
    # melakukan perulangan untuk menampilkan seluruh transaksi
    for i, riwayat in enumerate(transaksi, start=1):
        print(f"{i}. {riwayat['nama']} - {riwayat['tipe']} - {riwayat['jumlah']} - {riwayat['kategori']}")
        
# fitur 5 : ringkasan analisis keuangan
def ringkasan_analisis():
    print("\n----- MENU RINGKASAN ANALISIS >>>>>")
    
    # menyiapkan variabel perhitungan
    total_pemasukan = 0
    total_pengeluaran = 0

    # menghitung total pemasukan dan pengeluaran
    for t in transaksi:
        if t["tipe"] == "pemasukan":
            total_pemasukan += t["jumlah"]
        else:
            total_pengeluaran += t["jumlah"]

    # menampilkan hasil
    print("Total Pemasukan:", total_pemasukan)
    print("Total Pengeluaran:", total_pengeluaran)
    
    # analisis keuangan sederhana
    
    # mengecek apakah ada pemasukan sebelumnya
    if total_pemasukan == 0:
        print("\n=================================")
        print("\tBelum ada pemasukan.")
        print("=================================")
        return # akan kembali ke beranda

    # menghitung presentase (contoh 500.000 / 1.000.000 = 0.5)
    persentase = total_pengeluaran / total_pemasukan

    # menampilkan presentase ke dalam bentuk yang bisa dibaca oleh pengguna
    # contoh (0.5 * 100 = 50.0), dan
    # :.0f "digunakan untuk menghilangkan angka dibalik koma"
    print(f"Persentase Pengeluaran: {persentase * 100:.0f}%")

    # menampilkan hasil kondisi analisis keuangan
    if total_pengeluaran > total_pemasukan:
        print("\n===================================================")
        print("Status: ❗\tPengeluaran melebihi pemasukan!") # pengeluaran 100% 
        print("===================================================")
    elif persentase > 0.8:
        print("\n===================================================")
        print("Status: ⚠️\tSangat boros (lebih dari 80%)") # pengeluaran 80%
        print("===================================================")
    elif persentase > 0.5:
        print("\n===================================================")
        print("Status: ⚠️\tMulai boros (lebih dari 50%)") # pengeluaran 50%
        print("===================================================")
    else:
        print("\n===================================================")
        print("Status: ✅\tKeuangan masih aman") # pengeluaran masih diatas 80%
        print("===================================================")

# fitur 6 : Kategori pengeluaran
def filter_kategori_pengeluaran():
    print("\n----- MENU KATEGORI PENGELUARAN >>>>>")
    cari = input("Masukkan nama kategori pengeluaran: ").lower()

    # persiapan logic pengkondisian jika data transaksi ditemukan/tidak
    ditemukan = False
    counter = 1 # untuk penomoran
    total = 0 # untuk menghitung total pengeluaran pada kategori yang dicari
    
    print(f"\nKategori: {cari}")
    print("-------------------------")

    # jika data transaksi ditemukan, maka akan ditampilkan
    for riwayat in transaksi:
        if riwayat["tipe"] == "pengeluaran" and riwayat["kategori"].lower() == cari:
            # menampilkan setiap transaksi
            print(f"{counter}. {riwayat['nama']} - Rp.{riwayat['jumlah']} ({riwayat['kategori']})")
            
            # menghitung total dan penomoran
            total += riwayat["jumlah"]
            counter += 1 # dijumlahkan satu untuk setiap data yang telah ditampilkan
            ditemukan = True

    if ditemukan:
        print("\n===========================================================")
        print(f"Total pengeluaran kategori '{cari}': Rp.{total}")
        print("===========================================================")
    else:
        # jika data transaksi tidak ada, maka menampilkan pesan
        print("\n===========================================================")
        print("Tidak ada transaksi pengeluaran dengan kategori tersebut.")
        print("===========================================================")
        
# fitur 7 : Analisis pengeluaran terbesar
def analisis_pengeluaran_terbesar():
    print("\n----- MENU ANALISIS PENGELUARAN >>>>>")

    # menyiapkan variabel untuk perhitungan
    terbesar = 0
    data_terbesar = None

    # mencari pengeluaran terbesar
    for riwayat in transaksi:
        # apakah riwayat transaksi termasuk ke dalam pengeluaran
        if riwayat["tipe"] == "pengeluaran":
            # apakah riwayat transaksi saat ini lebih besar jumlahnya
            if riwayat["jumlah"] > terbesar:
                # jika iya, data transaksi dijadikan sebagai pengeluaran yang paling besar
                terbesar = riwayat["jumlah"]
                data_terbesar = riwayat 

    # jika tidak ada data pengeluaran
    if data_terbesar is None:
        print("\n=================================")
        print("Belum ada data pengeluaran.")
        print("=================================")
    else:
        # jika ketemu, tampilkan data transaksi pengeluaran yang terbesar
        print("Pengeluaran terbesar:")
        print("----------------------------------------------")
        print(f"Nama      : {data_terbesar['nama']}")
        print(f"Jumlah    : Rp.{data_terbesar['jumlah']}")
        print(f"Kategori  : {data_terbesar['kategori']}")

# awal program utama
print("===== SELAMAT DATANG DI CASH FLOW =====")

# melakukan perulangan, agar fitur bisa digunakan secara berulang
while True:
    # akan berulang terus, hingga pengguna memilih keluar
    print("")
    print("===== PILIH MENU =====")
    print("1. Pemasukan")
    print("2. Pengeluaran")
    print("3. Saldo")
    print("4. Riwayat Transaksi")
    print("5. Ringkasan & Analisis Keuangan")
    print("6. Kategori Pengeluaran")
    print("7. Analisis Pengeluaran terbesar")
    print("8. Keluar")
    
    pilihMenu = input("Pilih menu: ")
    
    # menggunakan percabangan untuk proses setiap menu-nya
    if pilihMenu == "1":
        tambah_pemasukan()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "2":
        tambah_pengeluaran()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "3":
        lihat_saldo()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "4":
        lihat_riwayat()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "5":
        ringkasan_analisis();
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "6":
        filter_kategori_pengeluaran()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "7":
        analisis_pengeluaran_terbesar()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "8":
        print("\n===== SAMPAI JUMPA LAGI =====")
        break # program perulangan selesai
    
# akhir program utama