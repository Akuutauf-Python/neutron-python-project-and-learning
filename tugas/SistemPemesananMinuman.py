# =====================================
# Latihan Coding: Sistem Pemesanan Minuman
# =====================================

# Fungsi untuk menghitung total harga semua minuman
def hitung_total(menu_pesanan):
    total = 0
    # TODO: jumlahkan semua harga dalam menu_pesanan
    # for nama, harga in menu_pesanan:
    #     total += ...
    
    # perulangan for
    for pesanan in menu_pesanan:
        total += pesanan[1]
    
    return total

# Fungsi untuk menghitung diskon
def hitung_diskon(total):
    # TODO: berikan diskon 10% jika total > 50000
    diskon = 0
    
    # pengecekan
    if total > 50000:
        # lakukan pemberian diskon
        diskon = total * 10 / 100
    
    return diskon

# Fungsi untuk menampilkan ringkasan pesanan
def tampilkan_ringkasan(nama, menu, total, diskon):
    print(f"Pesanan untuk: {nama}")
    # TODO: tampilkan semua item dengan nomor urut
    # Gunakan enumerate(menu, 1) agar ada nomor 1, 2, 3, ...
    
    # enumerate
    for index, data in enumerate(menu):
        print(f"{index+1}. {data[0]} - Rp{data[1]}")   
    
    print(f"Total: Rp{total}")
    print(f"Diskon: Rp{diskon}")
    print(f"Harga Final: Rp{total - diskon}")

# ===============================
# Program Utama
# ===============================

# TODO: buat list pesanan contoh, misalnya:
# menu = [("Es Teh Manis", 8000), ("Kopi Susu", 18000), ("Jus Mangga", 20000)]
menu = [["Es Teh Manis", 20000], ["Kopi Susu", 20000], ["Jus Mangga", 20000]]

nama = input("Masukkan nama Anda : ")

# TODO: panggil fungsi hitung_total dan hitung_diskon
total = hitung_total(menu)
diskon = hitung_diskon(total)

# TODO: panggil fungsi tampilkan_ringkasan dengan nama pelanggan
tampilkan_ringkasan(nama, menu, total, diskon)
