# soal tugas

# data yang di filter (mencurigakan)
scam_keywords = ["hadiah", "menang", "klik link", "login", "verifikasi", "transfer"]

# "Saldo e-wallet kamu akan hangus, segera isi ulang di sini",
#  "Besok kita rapat OSIS jam 7 pagi di ruang multimedia.",
#  "Selamat ulang tahun! Semoga sukses selalu 🎉",
#  "Saldo e-wallet kamu akan hangus, segera isi ulang di sini.",
#  "Hadiah uang tunai Rp10.000.000 menantimu! Cek di www.hadiahinstan.com"

while True:
    # input utama
    pesan = input("\nMasukkan kalimat / pesan (ketik 'exit' untuk berhenti): ").lower()
    
    # opsi jika sudah ingin program selesai
    if pesan == "exit":
        print("Terima kasih sudah mempercayakan pesan Anda ke kami!")
        break # stop untuk perulangan while

    # konversi data pesan ke bentuk lowercase
    # pesan = pesan.lower()

    # melakukan perulangan seluruh keywoard
    for keyword in scam_keywords:
    # untuk melakukan pengecekan kata scam di satu kalimat pada pesan
        if keyword in pesan:
            # kalau scam maka tampilkan pesan berikut
            print("⚠️ Pesan ini mencurigakan. Jangan klik tautan apapun!") # true
            
            # kalau ada stop (untuk scam)
            break
        else:
            print("✅ Pesan ini tampak aman, tetapi tetap berhati-hati.") # false
            break # stop kalau pesan nya engga scam (untuk scam)
        
    print("Akhir dari program")