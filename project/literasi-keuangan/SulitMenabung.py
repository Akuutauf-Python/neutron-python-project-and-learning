# aplikasi pencatatan uang sederhana
# studi kasus : Sulit Menabung

# menyiapkan tempat untuk menyimpan data target tabungan
target_tabungan = 0

# menyiapkan tempat untuk menyimpan data riwayat transaksi
transaksi = [
    # sengaja dikosongi sebagai template untuk pengguna nanti
    # {
    #     "nama": "Gaji minggu pertama",
    #     "tipe": "pemasukan",
    #     "jumlah": 100000,
    #     "kategori": "gaji"
    # },
]

# fitur 1 : input pemasukan
def input_pemasukan():
    nama = input("Nama pemasukan: ")
    jumlah = float(input("Jumlah: "))
    kategori = input("Kategori pemasukan: ")

    # tambah transaksi ke dalam jenis pemasukan
    transaksi.append({
        "tipe": "pemasukan",
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori,
    })
    
# fitur 2 : input pengeluaran
def input_pengeluaran():
    nama = input("Nama pengeluaran: ")
    jumlah = float(input("Jumlah: "))
    kategori = input("Kategori pengeluaran: ")
    
    # hitung saldo saat ini
    saldo = 0
    
    for item in transaksi:
        # jika data item (transaksi) saat ini adalah "pemasukan"
        if item["tipe"] == "pemasukan":
            # maka jumlahkan dengan saldo saat ini
            saldo += item["jumlah"]
        # namun, jika data item (transaksi) saat ini adalah selain "pemasukan" (pengeluaran)
        else:
            # maka kurangi dengan saldo saat ini
            saldo -= item["jumlah"]

    # cek apakah pengeluaran melebihi saldo
    if jumlah > saldo:
        print("❌ \tPengeluaran melebihi saldo! Transaksi dibatalkan.")
        # namun, jika pengeluaran tidak melebihi saldo
    else:
        # maka tambahkan data pengeluaran ke transaksi
        transaksi.append({
            "tipe": "pengeluaran",
            "nama": nama,
            "jumlah": jumlah,
            "kategori": kategori,
        })
    
# fitur 3 : hitung sisa uang
def hitung_sisa_uang():
    # menyiapkan data untuk menghitung sisa uang (total pemasukan - total pengeluaran)
    total_pemasukan = 0
    total_pengeluaran = 0

    for item in transaksi:
        # jika item (transaksi) saat ini adalah "pemasukan"
        if item["tipe"] == "pemasukan":
            total_pemasukan += item["jumlah"]
        # namun jika item (transaksi) saat ini selain "pemasukan" (pengeluaran)
        else:
            total_pengeluaran += item["jumlah"]

    # menghitung sisa uang
    sisa = total_pemasukan - total_pengeluaran
    
    # menampilkan sisa uang
    print("Sisa uang:", sisa)
    
    # dan fungsi mengembalikan data sisa uang
    return sisa

# fitur 4 : set target tabungan
def set_target():
    # menggunakan keywoard global, agar variabel bisa digunakan di fungsi yang lain
    # menggunakan variabel yang sudah ada, jika menggunakan keywoard 'global'
    global target_tabungan
    
    # menyimpan nominal tabungan
    target_tabungan = float(input("Masukkan target tabungan: "))
    
# fitur 5 : cek target tercapai / tidak
def cek_target():
    # menyimpan nilai sisa uang yang diperoleh dari fungsi 'hitung_sisa_uang()'
    sisa = hitung_sisa_uang()

    # mengecek jika target tabungan masih belum di tentukan
    if target_tabungan == 0:
        # maka tampilkan pesan dibawah
        print("Target tabungan belum ditentukan.")
    
    # namun jika sisa uang Anda, lebih dari target tabungan
    elif sisa >= target_tabungan:
        # maka tampilkan pesan berikut ini
        print("✅ \tTarget tabungan tercapai!")
        
    # jika kondisi sisa uang di bawah dari target tabungan
    else:
        # maka tampilkan pesan dibawah
        print("❌ \tTarget belum tercapai.")

# awal program utama
print("===== SELAMAT DATANG DI APLIKASI LITERASI KEUANGAN =====")

# melakukan perulangan, agar fitur bisa digunakan secara berulang
while True:
    # akan berulang terus, hingga pengguna memilih keluar
    print("")
    print("===== PILIH MENU =====")
    
    # fitur utama 
    print("1. Input Pemasukan")
    print("2. Input Pengeluaran")
    print("3. Hitung Sisa Uang")
    
    # fitur tambahan
    print("4. Set Target Tabungan")
    print("5. Cek Target Tercapai")
    print("6. Keluar")
    
    # input
    pilihMenu = input("Pilih menu: ")
    
    # menggunakan percabangan untuk proses setiap menu-nya
    if pilihMenu == "1":
        input_pemasukan()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "2":
        input_pengeluaran()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "3":
        hitung_sisa_uang()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "4":
        set_target()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "5":
        cek_target()
        print("<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "6":
        print("===== SAMPAI JUMPA LAGI =====")
        break # program perulangan selesai
        
# akhir program utama