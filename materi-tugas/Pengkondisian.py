# # pengkondisian

# rumus
# if kondisi:
    # aksi
    
# program login
# username = input("Username ? : ")
# password = input("Password ? : ")

# indentasi

# if username == "Taufik" and password == "rahasia":
#     print("Selamat datang Taufik 1") # true
# elif username == "taufik" and password == "rahasia":
#     print("Selamat datang taufik 2") # true
# elif username == "Yumna" and password == "123":
#     print("Selamat datang Yumna 1") # true
# elif username == "yumna" and password == "123":
#     print("Selamat datang yumna 2") # true
# else:
#     print("Anda belum terdaftar")
    
# print("Akhir dari program")

nilai_rata = 75
nilai_siswa = float(input("Masukkan nilai siswa : "))

# pengkondisian
if nilai_siswa < nilai_rata:
    print("kamu harus remidi!")
else:
    print("Kamu lulus, selamat yaa~")