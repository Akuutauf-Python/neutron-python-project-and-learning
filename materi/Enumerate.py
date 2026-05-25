# looping dari list & enumerate

# foor loop
print("For Loop ========")
# data list numbers
kumpulan_angka = [4,6,3,2,6,8,2,1]

for angka in kumpulan_angka:
    print(f"Angka = {angka}")
    
# data list string
print()
kumpulan_anggota = ["Taufik", "Wawan", "Bisma", "Handoko"]

for nama_anggota in kumpulan_anggota:
    print(f"Nama Anggota = {nama_anggota}")
    
# for loop range
print("\nFor Loop dan Range ========")
kumpulan_angka = [4,5,3,2,5,6,1]
panjang_data = len(kumpulan_angka)

for i in range(panjang_data):
    print(f"Angka = {kumpulan_angka[i]}")
    
# while loop
print("\nWhile Loop ========")
kumpulan_angka = [4,5,3,2,5,6,1]
panjang_data = len(kumpulan_angka)
i = 0

while i < panjang_data:
    print(f"Angka = {kumpulan_angka[i]}")
    i+= 1

# list comprehension
print("\nList Comprehension ========")
data = ["Taufik", 9, "True", False]

[print(f"Isi Data = {i}") for i in data]

# membuat angka di kuadratkan
kumpulan_angka = [4,5,3,2,5,6,1]
angka_kuadrat = [i**2 for i in kumpulan_angka]
print(angka_kuadrat)

# enumerate
# mendapatkan index dan isi sekaligus
print("\nEnumerate ========")
data_list = ["Taufik", 9, "Adit", False]

for index, data in enumerate(data_list):
    print(f"Index ke {index}, Nilainya adalah = {data}")   