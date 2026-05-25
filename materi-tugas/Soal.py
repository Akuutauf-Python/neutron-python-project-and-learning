# soal tugas

# data yang di filter (mencurigakan)
scam_keywords = ["hadiah", "menang", "klik link", "login", "verifikasi", "transfer"]

# data kalimat / pesan yang mencurigakan
messages = [
    "Saldo e-wallet kamu akan hangus, segera isi ulang di sini",
    "Besok kita rapat OSIS jam 7 pagi di ruang multimedia.",
    "Selamat ulang tahun! Semoga sukses selalu 🎉",
    "Saldo e-wallet kamu akan hangus, segera isi ulang di sini.",
    "Hadiah uang tunai Rp10.000.000 menantimu! Cek di www.hadiahinstan.com"
]

# hasil pesan mencurigakan atau tidak
result = []

# mengecek seluruh pesan
for data_pesan in messages:
    
    # konversi data pesan ke bentuk lowercase
    data_pesan = data_pesan.lower()
    
    # membuat variabel baru untuk pengecekan flag
    isScam = False
    
    # melakukan perulangan seluruh keywoard
    for keyword in scam_keywords:
    # untuk melakukan pengecekan kata scam di satu kalimat pada pesan
        if keyword in data_pesan:
            isScam = True
            break

    # tambahkan hasil pengecekan ke list result
    result.append(isScam)
        
print(result)

# melakukan perulangan untuk menampilkan hasil
for hasil in result:
    if hasil == True:
        print("⚠️ Pesan ini mencurigakan. Jangan klik tautan apapun!")
    else:
        print("✅ Pesan ini tampak aman, tetapi tetap berhati-hati.")
        
print("Akhir dari program")