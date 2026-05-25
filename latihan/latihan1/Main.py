# program menghitung luas lingkaran
print("==== Program Menentukan Luas Lingkaran Dimulai ====")
phi = 3.14;

# melihat tipe data dari suatu variabel
print("Tipe data phi adalah", type(phi))

# memberikan nilai inputan dari terminal
jari_jari = input("Masukkan jari-jari lingkaran: ")

# coba lihat tipe data yang berhasil diperoleh dari inputan
print("Tipe data jari_jari adalah", type(jari_jari))

# karena bertipe string, maka perlu di konversi ke dalam bentuk angka
jari_jari = int(jari_jari)

# coba lihat tipe data yang berhasil dikonversi
print("Tipe data jari_jari yang baru adalah", type(jari_jari))

# tampilkan nilai jari-jari yang sudah di input
print("Nilai jari jari adalah: ", jari_jari);

# menghitung luas lingkaran
luas = phi * (jari_jari ** 2)

# atau bisa menggunakan rumus berikut
luas_lingkaran = phi * jari_jari * jari_jari

# tampilkan hasil luas lingkaran
print("Luas lingkaran dengan jari-jari", jari_jari, "adalah: ", luas)

# tampilkan hasil luas lingkaran dengan cara kedua
print("Luas lingkaran dengan jari-jari (cara kedua)", luas_lingkaran, "adalah: ", luas)

# menampilkan tipe data luas
print("Tipe data luas adalah", type(luas))
print("Tipe data luas lingkaran adalah", type(luas_lingkaran))

print("==== Program Menentukan Luas Lingkaran Selesai ====")