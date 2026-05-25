# program hitung gaji karyawan
print("----------------------------------")
print("PROGRAM HITUNG GAJI KARYAWAN")
print("----------------------------------")

# input
nama_karyawan = input("NAMA KARYAWAN : ")
gol_jabatan = input("GOLONGAN JABATAN : ")
pendidikan = input("GOLONGAN PENDIDIKAN : ")
jmlh_jam_kerja = int(input("JUMLAH JAM KERJA : "))
jmlh_jam_lembur = int(input("JUMLAH JAM LEMBUR : "))

# proses
tunjangan_jbtn = 100000
gaji_pokok = jmlh_jam_kerja * 130000
honor_lembur = jmlh_jam_lembur * 100000
total_gaji = tunjangan_jbtn + gaji_pokok + honor_lembur

# output
print("----------------------------------")
print("HONOR YANG DITERIMA")
print(f"GAJI POKOK {gaji_pokok}")
print(f"TUNJANGAN JABATAN {tunjangan_jbtn}")
print(f"HONOR LEMBUR {honor_lembur}")
print("----------------------------------")
print(f"TOTAL GAJI {total_gaji}")
