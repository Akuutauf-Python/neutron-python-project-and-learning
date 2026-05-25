# function argument/parameter

# fungsi dengan 1 parameter
def say_hello_with_name(name):
    print(f"Haii {name}")
    
say_hello_with_name("Taufik")
say_hello_with_name("Ilham")

# fungsi dengan lebih dari 1 parameter
def perpangkatan(bil, pangkat):
    # perhitungan hasil eksponen
    hasil = bil**pangkat
    print(f"Hasil eksponen {bil} dipangkatkan {pangkat} = {hasil}")
    
perpangkatan(10, 3)
perpangkatan(5, 3)

# fungsi dengan parameter list
def absensi_peserta(kumpulan_peserta):
    # data_peserta = kumpulan_peserta.copy() # mengubah
    
    # perulangan untuk absensi
    for peserta in kumpulan_peserta:
        print(f"{peserta} Hadir...")
    
peserta = ["Taufik", "Ilham", "Dimas"]

absensi_peserta(peserta)