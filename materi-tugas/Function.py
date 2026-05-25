# # soal tugas

# # data yang di filter (mencurigakan)
# scam_keywords = ["hadiah", "menang", "klik link", "login", "verifikasi", "transfer"]

# # "Saldo e-wallet kamu akan hangus, segera isi ulang di sini",
# #  "Besok kita rapat OSIS jam 7 pagi di ruang multimedia.",
# #  "Selamat ulang tahun! Semoga sukses selalu 🎉",
# #  "Saldo e-wallet kamu akan hangus, segera isi ulang di sini.",
# #  "Hadiah uang tunai Rp10.000.000 menantimu! Cek di www.hadiahinstan.com"

# # membuat function
# def CheckScamMessage(pesan):
#     # melakukan perulangan seluruh keywoard
#     for keyword in scam_keywords:
#     # untuk melakukan pengecekan kata scam di satu kalimat pada pesan
#         if keyword in pesan:
#             # kalau scam maka tampilkan pesan berikut
#             print("⚠️ Pesan ini mencurigakan. Jangan klik tautan apapun!") # true
            
#             # kalau ada stop (untuk scam)
#             break
#         else:
#             print("✅ Pesan ini tampak aman, tetapi tetap berhati-hati.") # false
#             break # stop kalau pesan nya engga scam (untuk scam)
        
# # ----------------------------------------------------------------------------

# # data kalimat / pesan yang mencurigakan
# messages = [
#     "Saldo e-wallet kamu akan hangus, segera isi ulang di sini",
#     "Besok kita rapat OSIS jam 7 pagi di ruang multimedia.",
#     "Selamat ulang tahun! Semoga sukses selalu 🎉",
#     "Saldo e-wallet kamu akan hangus, segera isi ulang di sini.",
#     "Hadiah uang tunai Rp10.000.000 menantimu! Cek di www.hadiahinstan.com"
# ]

# messagesSecond = [
#     "Saldo e-wallet kamu akan hangus, segera isi ulang di sini",
#     "Besok kita rapat OSIS jam 7 pagi di ruang multimedia.",
#     "Selamat ulang tahun! Semoga sukses selalu 🎉",
#     "Saldo e-wallet kamu akan hangus, segera isi ulang di sini.",
#     "Hadiah uang tunai Rp10.000.000 menantimu! Cek di www.hadiahinstan.com"
# ]
   
# # perulangan for
# for data_pesan in messages:
#     CheckScamMessage(data_pesan)

# for data_pesan in messagesSecond:
#     CheckScamMessage(data_pesan)
        
# print("Akhir dari program")

# def Penjumlahan(a, b):
#     return a + b

# x = Penjumlahan(10, 5)

# print(x)

# print(Penjumlahan(50, 86))
# print(Penjumlahan(50, 86))
# print(Penjumlahan(50, 86))
# print(Penjumlahan(50, 86))
# print(Penjumlahan(50, 86))

# def LuasLingkaran(r):
#     phi = 3.14
    
#     # rumus
#     print(phi * r**2)
    
# LuasLingkaran(10)
# LuasLingkaran(12)
# LuasLingkaran(100)
# LuasLingkaran(65)