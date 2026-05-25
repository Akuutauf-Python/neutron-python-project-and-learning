# program menentukan bilangan ganjil genap
print("==== Program Menentukan Bilangan Ganjil Genap Dimulai =====")

# input bilangan langsung tanpa melalukan konversi
bilangan = int(input("Masukkan bilangan: "))

# menampilkan bilangan yang baru saja di input
print("Bilangan anda adalah", bilangan)

# melakukan pengecekan dengan pengkondisian
if bilangan % 2 == 0:
    print("Bilangan", bilangan , "merupakan Bilangan Genap")
else:
    print("Bilangan", bilangan, "anda merupakan Bilangan Ganjil")
    
print("==== Program Menentukan Bilangan Ganjil Genap Selesai =====")
    

