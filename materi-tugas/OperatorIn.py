# operator in
fruits_list = ["apple", "semangka", "anggur", "salak", "pisang", "jeruk"]

# perulahan while
while True:
    # menampilkan buah
    print("Daftar buah tersedia:")
    print(fruits_list) 

    # input
    pilihanBuah = input("\nMau beli buah apa? (ketik 'exit' untuk berhenti): ").lower()

    # opsi jika sudah ingin program selesai
    if pilihanBuah == "exit":
        print("Terima kasih sudah berbelanja!")
        break

    # di cek stok buah nya
    if pilihanBuah in fruits_list:
        print(f"{pilihanBuah} berhasil dibeli!")
        
        # buah di hapus dari daftar
        fruits_list.remove(pilihanBuah)
    else:
        print("Maaf, Buah tidak tersedia")

print("Akhir dari program")