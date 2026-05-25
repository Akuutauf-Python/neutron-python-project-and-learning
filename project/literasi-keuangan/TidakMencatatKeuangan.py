# aplikasi pencatatan uang sederhana
# studi kasus : Tidak mencatat keuangan

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

# fitur 3 : Riwayat transaksi
def lihat_riwayat():
    print("\n----- MENU RIWAYAT >>>>>")
    
    # jika data riwayat transaksi kosong
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return
    
    # jika tidak kosong untuk riwayat transaksi
    print("Nama - Tipe - Jumlah - Kategori")
    print("-------------------------------")
    for riwayat in transaksi:
        print(f"{riwayat['nama']} - {riwayat['tipe']} - {riwayat['jumlah']} - {riwayat['kategori']}")
        
# fitur 4 : Menampilkan saldo
def lihat_saldo():
    print("\n----- MENU SALDO >>>>>")
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
    
# fitur 5 : Kategori pengeluaran
def filter_kategori_pengeluaran():
    print("\n----- MENU KATEGORI PENGELUARAN >>>>>")
    cari = input("Masukkan nama kategori pengeluaran: ").lower()

    # persiapan logic pengkondisian jika data transaksi ditemukan/tidak
    ditemukan = False
    counter = 1 # untuk penomoran

    # jika data transaksi ditemukan, maka akan ditampilkan
    for riwayat in transaksi:
        if riwayat["tipe"] == "pengeluaran" and riwayat["kategori"].lower() == cari:
            print(f"{counter}. {riwayat['nama']} - {riwayat['jumlah']} ({riwayat['kategori']})")
            counter+= 1 # dijumlahkan satu untuk setiap data yang telah ditampilkan
            ditemukan = True

    # jika data transaksi tidak ada, maka menampilkan pesan
    if not ditemukan:
        print("Tidak ada transaksi pengeluaran dengan kategori tersebut.")
        
# fitur 6 : ringkasan keuangan
def ringkasan():
    print("\n----- MENU RINGKASAN KEUANGAN >>>>>")
    
    total_pemasukan = 0
    total_pengeluaran = 0

    # melakukan perulangan untuk menghitung seluruh pemasukan dan pengeluaran
    for t in transaksi:
        if t["tipe"] == "pemasukan":
            total_pemasukan += t["jumlah"]
        else:
            total_pengeluaran += t["jumlah"]

    # menampilkan total pemasukan dan pengeluaran
    print("Total Pemasukan: ", total_pemasukan)
    print("Total Pengeluaran: ", total_pengeluaran)

# awal program utama
print("===== SELAMAT DATANG DI CASH FLOW =====")

# melakukan perulangan, agar fitur bisa digunakan secara berulang
while True:
    # akan berulang terus, hingga pengguna memilih keluar
    print("")
    print("===== PILIH MENU =====")
    print("1. Pemasukan")
    print("2. Pengeluaran")
    print("3. Riwayat")
    print("4. Saldo")
    print("5. Kategori Pengeluaran")
    print("6. Ringkasan Keuangan")
    print("7. Keluar")
    
    pilihMenu = input("Pilih menu: ")
    
    # menggunakan percabangan untuk proses setiap menu-nya
    if pilihMenu == "1":
        tambah_pemasukan()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "2":
        tambah_pengeluaran()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "3":
        lihat_riwayat()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "4":
        lihat_saldo()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "5":
        filter_kategori_pengeluaran()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "6":
        ringkasan();
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "7":
        print("===== SAMPAI JUMPA LAGI =====")
        break # program perulangan selesai
    
# akhir program utama