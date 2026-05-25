# aplikasi pencatatan uang sederhana
# studi kasus : Tidak Punya Budgeting

# membuat tempat untuk menyimpan budget / saldo
budget = 0

# membuat tempat untuk menyimpan seluruh data transaksi
transaksi = [
    # template data transaksi
    # {
    #     "nama": "Gaji minggu pertama",
    #     "tipe": "pemasukan",
    #     "jumlah": 100000,
    #     "kategori": "gaji",
    # },
]

# penambahan :
# 1. try except dan perbaikan untuk fitur pemasukan dan pengeluaran (fitur nomor 1 dan 2)
# 2. perbaikan dan menambahkan presentase untuk kondisi budget (fitur nomor 4 dan 5)
# 3. menu tidak valid
# 4. menambahkan fitur riwayat transaksi
# 5. menambahkan fungsi untuk hitung total pemasukan
# 6. try except dan perbaikan untuk fitur set budget (fitur nomor 3)

# alur program utama
# - pemasukan (ada pemasukan, saldo nambah)
# - set budget (set budget mengambil nominal dari pemasukan)
# - pengeluaran (menggunakan melakukan perbandingan dengan budget bukan pemasukan)

# fungsi untuk konversi ke format nominal rupiah
def format_rupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")

# fungsi support untuk menghitung total pemasukan
def hitung_total_pemasukan():
    # menyiapkan variabel untuk menghitung seluruh total pemasukan
    total_pemasukan = 0

    # menghitung total pemasukan dengan perulangan for
    for item in transaksi:
        # jika item (transaksi) saat ini adalah tipe "pemasukan"
        if item["tipe"] == "pemasukan":
            # maka jumlahkan nominal pemasukan ke total_pemasukan
            total_pemasukan += item["jumlah"]
            
    # mengembalikan hasil dari total pengeluaran
    return total_pemasukan

# fungsi support untuk menghitung total pengeluaran
def hitung_total_pengeluaran():
    # menyiapkan variabel untuk menghitung seluruh total pengeluaran
    total_pengeluaran = 0

    # menghitung total pengeluaran dengan perulangan for
    for item in transaksi:
        # jika item (transaksi) saat ini adalah tipe "pengeluaran"
        if item["tipe"] == "pengeluaran":
            # maka jumlahkan nominal pengeluaran ke total_pengeluaran
            total_pengeluaran += item["jumlah"]
            
    # mengembalikan hasil dari total pengeluaran
    return total_pengeluaran

# fitur 1 - input pemasukan
def input_pemasukan():
    print("\n--- INPUT PEMASUKAN ---")
    
    try:
        nama = input("Nama pemasukan: ")
        jumlah = int(input("Jumlah: Rp"))
        kategori = input("Kategori pemasukan: ")
        
        # menambahkan data transaksi untuk pemasukan
        transaksi.append({
            "tipe": "pemasukan",
            "nama": nama,
            "jumlah": jumlah,
            "kategori": kategori
        })
        
        print("- Pemasukan berhasil ditambahkan.")
    except ValueError:
            # menangani ketika error untuk input nominal
            print("Input harus berupa angka.")
            print("Transaksi Dibatalkan")

# fitur 2 - input pengeluaran
def input_pengeluaran():
    print("\n--- INPUT PENGELUARAN ---")
    
    # menyiapkan data untuk menghitung total pemasukan
    total_pemasukan = hitung_total_pemasukan()
    
    # melakukan pengecekan untuk pemasukan dan budget
    if total_pemasukan == 0 or budget == 0:
        print("⚠️  Pemasukan atau budget belum ditambahkan.")
        return # keluar dari fitur (kembali ke beranda)
    
    try:
        nama = input("Nama pengeluaran: ")
        jumlah = int(input("Jumlah: Rp"))
        kategori = input("Kategori pengeluaran: ")

        # menambahkan data transaksi untuk pengeluaran
        transaksi.append({
            "tipe": "pengeluaran",
            "nama": nama,
            "jumlah": jumlah,
            "kategori": kategori,
        })

        print("- Pengeluaran berhasil ditambahkan.")

        # langsung cek kondisi setelah input
        cek_budget() # memanggil fitur 4
        
    except ValueError:
        # menangani ketika error untuk input nominal
        print("Input harus berupa angka.")
        print("Transaksi Dibatalkan")
    
# fitur 3 - set budget
def set_budget():    
    print("\n--- SET BUDGET ---")
    
    # menyiapkan data untuk menghitung total pemasukan
    total_pemasukan = hitung_total_pemasukan()

    # melakukan pengecekan untuk pemasukan wajib ditambahkan diawal
    if total_pemasukan == 0:
        print("⚠️  Pemasukan belum ditambahkan.")
        return # keluar dari fitur (kembali ke beranda)
    
    try:
        # menggunakan keywoard 'global' supaya isi variabel bisa diubah dan digunakan ke fungsi lain
        global budget
    
        # input budget (batas pengeluaran)
        budget = int(input("Masukkan batas pengeluaran: Rp"))
        
        # melakukan pengecekan batas nominal budget
        if budget > total_pemasukan:
            print("⚠️  Budget tidak boleh melebihi total pemasukan.")
            budget = 0 # set budget ke 0, kalau melebihi pemasukan
            return # keluar dari fitur (kembali ke beranda)
            
        print("✅  Budget berhasil disimpan.")
        
    except ValueError:
        # menangani ketika error untuk input nominal
        print("Input harus berupa angka.")
        print("Set Budget Dibatalkan")

# fitur 4 - cek dan sisa budget
def cek_budget():
    print("\n--- CEK BUDGET ---")

    # menghitung total pengeluaran dari fungsi hitung_total_pengeluaran()
    total_pengeluaran = hitung_total_pengeluaran()

    # jika budget belum di set
    if budget == 0:
        print("⚠️  Budget belum ditentukan.")
        return # keluar dari fitur (kembali ke beranda)

    # kalau misalnya budget sudah ditentukan, maka hitung sisa budget
    sisa = budget - total_pengeluaran

    # menampilkan total pengeluaran dan sisa budget
    print("Total Pengeluaran:", format_rupiah(total_pengeluaran))
    print("Sisa Budget:", format_rupiah(sisa))

    # mengecek kondisi budget
    if total_pengeluaran >= budget:
        print("===== ❌  Pengeluaran Melebihi Budget! =====")
    # untuk pengeluaran yang melebihi 80% dari budget
    elif total_pengeluaran > budget * 0.8: 
        print("===== ⚠️  Pengeluaran mencapai 80% dari Total Budget! =====")
    elif total_pengeluaran > budget * 0.5: 
        print("===== ⚠️  Pengeluaran mencapai 50% dari Total Budget! =====")
    elif total_pengeluaran > budget * 0.2: 
        print("===== ⚠️  Pengeluaran mencapai 20% dari Total Budget! =====")
    else:
        print("===== ✅  Pengeluaran Masih Aman. =====")
       
# fitur 5 - rekomendasi sederhana (saran) berdasarkan data
def rekomendasi_data():
    print("\n--- REKOMENDASI BERDASARKAN DATA ---")

    # menghitung total pengeluaran dari fungsi hitung_total_pengeluaran()
    total_pengeluaran = hitung_total_pengeluaran()

    # jika budget belum di set
    if budget == 0:
        print("⚠️  Budget belum ditentukan.")
        return # keluar dari fitur (kembali ke beranda)

    # menghitung presentase budget dari pengeluaran yang sudah ditambahkan
    # contoh : pengeluaran = 600.000 / 800.000 = 0,75
    persentase = total_pengeluaran / budget

    # menampilkan penggunaan budget sudah berapa persen
    # contoh : 0,75 x 100  75.0, dan
    # :.0f "digunakan untuk menghilangkan angka dibalik koma"
    print(f"Penggunaan budget: {persentase * 100:.0f}%")

    # melakukan pengecekan untuk rekomendasi status budgeting
    # jika presentase mencapai 100%, maka
    if persentase >= 1:
        # menampilkan pesan berikut ini
        print("💡 Rekomendasi: Pengeluaran sudah melewati batas! Kurangi pengeluaran tidak penting.")
    elif persentase > 0.8: # jika pengeluaran mencapai diatas 80%, maka
        # menampilkan pesan dibawah ini
        print("💡 Rekomendasi: Hampir habis, sebaiknya hemat.")
    elif persentase > 0.5: # jika pengeluaran mencapai diatas 50%, maka
        # menampilkan pesan berikut
        print("💡 Rekomendasi: Pengeluaran Anda sudah mencapai setengah dari budget.")
    elif persentase > 0.2: # jika pengeluaran mencapai diatas 20%, maka
        # menampilkan pesan berikut
        print("💡 Rekomendasi: Mulai kontrol pengeluaran.")
        
    else: # dan kalau 3 kondisi diatas tidak terpenuhi, maka budgeting masih aman
        # dan menampilkan pesan dibawah ini
        print("💡 Rekomendasi: Keuangan masih aman.")
        
# fitur 6 : Pengeluaran terbesar
def pengeluaran_terbesar():
    print("\n----- MENU PENGELUARAN TERBESAR >>>>>")

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
        print(f"Jumlah    : {format_rupiah(data_terbesar['jumlah'])}")
        print(f"Kategori  : {data_terbesar['kategori']}")
        
# fitur 7 : Riwayat transaksi
def riwayat_transaksi():
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
        print(f"{i}. {riwayat['nama']} - {riwayat['tipe']} - {format_rupiah(riwayat['jumlah'])} - {riwayat['kategori']}")

# awal program utama
print("===== SELAMAT DATANG DI APLIKASI LITERASI KEUANGAN =====")

# melakukan perulangan, agar fitur bisa digunakan secara berulang
while True:
    # akan berulang terus, hingga pengguna memilih keluar
    print("")
    print("===== DASHBOARD =====")
    print("Total Transaksi \t:", len(transaksi))
    print("Budget \t\t\t:", format_rupiah(budget))
    print("Total Pemasukan \t:", format_rupiah(hitung_total_pemasukan()))
    print("Total Pengeluaran \t:", format_rupiah(hitung_total_pengeluaran()))
    print("")
    
    # fitur utama
    print("===== PILIH MENU =====")
    print("1. Input Pemasukan")
    print("2. Input Pengeluaran")
    print("3. Set Budget")
    print("4. Cek Budget")
    
    # fitur tambahan
    print("5. Rekomendasi Berdasarkan Data")
    print("6. Pengeluaran Terbesar")
    print("7. Riwayat Transaksi")
    print("8. Keluar")
    
    # input menu
    pilihMenu = input("Pilih menu: ")
    
    # menggunakan percabangan untuk proses setiap menu-nya
    if pilihMenu == "1":
        input_pemasukan();
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "2":
        input_pengeluaran()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "3":
        set_budget()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "4":
        cek_budget()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "5":
        rekomendasi_data()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "6":
        pengeluaran_terbesar()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "7":
        riwayat_transaksi()
        print("\n<<<<< KEMBALI KE BERANDA -----")
    elif pilihMenu == "8":        
        # melakukan konfirmasi untuk keluar dari aplikasi
        konfirmasi = input("Tekan y untuk keluar, atau tombol lain untuk kembali: ").lower()

        # jika konfirmasi nya "y"
        if konfirmasi == "y":
            # maka program akan berhenti atau keluar
            print("\n===== SAMPAI JUMPA LAGI =====")
            break # program perulangan selesai
    else:
        print("\n===== MENU TIDAK VALID =====")
    
# akhir program utama