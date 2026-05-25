import tkinter as tk
from tkinter import messagebox

# =========================
# DATA UTAMA
# =========================

budget = 0
transaksi = []

# =========================
# FUNGSI SUPPORT
# =========================

# menghitung total pemasukan
def hitung_total_pemasukan():
    total = 0

    for item in transaksi:
        if item["tipe"] == "pemasukan":
            total += item["jumlah"]

    return total

# menghitung total pengeluaran
def hitung_total_pengeluaran():
    total = 0

    for item in transaksi:
        if item["tipe"] == "pengeluaran":
            total += item["jumlah"]

    return total

# format rupiah sederhana
def format_rupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")

# validasi input nominal
def validasi_nominal(input_nominal):
    try:
        nominal = input_nominal.replace(".", "")
        nominal = int(nominal)

        if nominal <= 0:
            return None

        return nominal

    except:
        return None

# update dashboard
def update_dashboard():
    total_pemasukan = hitung_total_pemasukan()
    total_pengeluaran = hitung_total_pengeluaran()
    sisa_budget = budget - total_pengeluaran

    label_total_pemasukan.config(
        text=f"Total Pemasukan : {format_rupiah(total_pemasukan)}"
    )

    label_total_pengeluaran.config(
        text=f"Total Pengeluaran : {format_rupiah(total_pengeluaran)}"
    )

    label_budget.config(
        text=f"Budget : {format_rupiah(budget)}"
    )

    label_sisa_budget.config(
        text=f"Sisa Budget : {format_rupiah(sisa_budget)}"
    )

# =========================
# FITUR PEMASUKAN
# =========================

def input_pemasukan():
    nama = entry_nama.get()
    jumlah = validasi_nominal(entry_jumlah.get())
    kategori = entry_kategori.get()

    if nama == "" or kategori == "":
        messagebox.showwarning("Peringatan", "Semua input harus diisi.")
        return

    if jumlah is None:
        messagebox.showerror("Error", "Jumlah harus berupa angka.")
        return

    transaksi.append({
        "tipe": "pemasukan",
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori
    })

    messagebox.showinfo("Berhasil", "Pemasukan berhasil ditambahkan.")

    tampilkan_riwayat()
    update_dashboard()
    reset_input()

# =========================
# FITUR PENGELUARAN
# =========================

def input_pengeluaran():
    global budget

    total_pemasukan = hitung_total_pemasukan()

    if total_pemasukan == 0:
        messagebox.showwarning("Peringatan", "Pemasukan belum ditambahkan.")
        return

    if budget == 0:
        messagebox.showwarning("Peringatan", "Budget belum ditentukan.")
        return

    nama = entry_nama.get()
    jumlah = validasi_nominal(entry_jumlah.get())
    kategori = entry_kategori.get()

    if nama == "" or kategori == "":
        messagebox.showwarning("Peringatan", "Semua input harus diisi.")
        return

    if jumlah is None:
        messagebox.showerror("Error", "Jumlah harus berupa angka.")
        return

    transaksi.append({
        "tipe": "pengeluaran",
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori
    })

    total_pengeluaran = hitung_total_pengeluaran()

    if total_pengeluaran > budget:
        messagebox.showwarning(
            "Warning",
            "Pengeluaran melebihi budget!"
        )

    elif total_pengeluaran > budget * 0.8:
        messagebox.showwarning(
            "Warning",
            "Pengeluaran mencapai 80% budget!"
        )

    else:
        messagebox.showinfo(
            "Info",
            "Pengeluaran masih aman."
        )

    tampilkan_riwayat()
    update_dashboard()
    reset_input()

# =========================
# SET BUDGET
# =========================

def set_budget():
    global budget

    total_pemasukan = hitung_total_pemasukan()

    if total_pemasukan == 0:
        messagebox.showwarning(
            "Peringatan",
            "Tambahkan pemasukan terlebih dahulu."
        )
        return

    nominal_budget = validasi_nominal(entry_budget.get())

    if nominal_budget is None:
        messagebox.showerror("Error", "Budget harus berupa angka.")
        return

    if nominal_budget > total_pemasukan:
        messagebox.showwarning(
            "Peringatan",
            "Budget tidak boleh melebihi total pemasukan."
        )
        return

    budget = nominal_budget

    messagebox.showinfo("Berhasil", "Budget berhasil disimpan.")

    update_dashboard()

# =========================
# RIWAYAT TRANSAKSI
# =========================

def tampilkan_riwayat():
    listbox_riwayat.delete(0, tk.END)

    if len(transaksi) == 0:
        listbox_riwayat.insert(tk.END, "Belum ada transaksi")
        return

    for i, item in enumerate(transaksi, start=1):
        teks = (
            f"{i}. "
            f"{item['nama']} | "
            f"{item['tipe']} | "
            f"{format_rupiah(item['jumlah'])} | "
            f"{item['kategori']}"
        )

        listbox_riwayat.insert(tk.END, teks)

# =========================
# RESET INPUT
# =========================

def reset_input():
    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)
    entry_kategori.delete(0, tk.END)

# =========================
# WINDOW UTAMA
# =========================

window = tk.Tk()
window.title("BudgetIn App")
window.geometry("700x650")
window.resizable(False, False)

# =========================
# JUDUL
# =========================

judul = tk.Label(
    window,
    text="BUDGETIN APP",
    font=("Arial", 16, "bold")
)
judul.pack(pady=10)

# =========================
# DASHBOARD
# =========================

frame_dashboard = tk.Frame(window)
frame_dashboard.pack(pady=10)

label_total_pemasukan = tk.Label(
    frame_dashboard,
    text="Total Pemasukan : Rp0",
    font=("Arial", 11)
)
label_total_pemasukan.pack(anchor="w")

label_total_pengeluaran = tk.Label(
    frame_dashboard,
    text="Total Pengeluaran : Rp0",
    font=("Arial", 11)
)
label_total_pengeluaran.pack(anchor="w")

label_budget = tk.Label(
    frame_dashboard,
    text="Budget : Rp0",
    font=("Arial", 11)
)
label_budget.pack(anchor="w")

label_sisa_budget = tk.Label(
    frame_dashboard,
    text="Sisa Budget : Rp0",
    font=("Arial", 11)
)
label_sisa_budget.pack(anchor="w")

# =========================
# FORM INPUT
# =========================

frame_form = tk.Frame(window)
frame_form.pack(pady=15)

# nama transaksi
label_nama = tk.Label(frame_form, text="Nama Transaksi")
label_nama.grid(row=0, column=0, padx=5, pady=5)

entry_nama = tk.Entry(frame_form, width=30)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

# jumlah
label_jumlah = tk.Label(frame_form, text="Jumlah")
label_jumlah.grid(row=1, column=0, padx=5, pady=5)

entry_jumlah = tk.Entry(frame_form, width=30)
entry_jumlah.grid(row=1, column=1, padx=5, pady=5)

# kategori
label_kategori = tk.Label(frame_form, text="Kategori")
label_kategori.grid(row=2, column=0, padx=5, pady=5)

entry_kategori = tk.Entry(frame_form, width=30)
entry_kategori.grid(row=2, column=1, padx=5, pady=5)

# =========================
# TOMBOL FITUR
# =========================

frame_tombol = tk.Frame(window)
frame_tombol.pack(pady=10)

btn_pemasukan = tk.Button(
    frame_tombol,
    text="Tambah Pemasukan",
    width=20,
    command=input_pemasukan
)
btn_pemasukan.grid(row=0, column=0, padx=5, pady=5)

btn_pengeluaran = tk.Button(
    frame_tombol,
    text="Tambah Pengeluaran",
    width=20,
    command=input_pengeluaran
)
btn_pengeluaran.grid(row=0, column=1, padx=5, pady=5)

# =========================
# SET BUDGET
# =========================

frame_budget = tk.Frame(window)
frame_budget.pack(pady=15)

label_budget_input = tk.Label(frame_budget, text="Set Budget")
label_budget_input.grid(row=0, column=0, padx=5)

entry_budget = tk.Entry(frame_budget, width=25)
entry_budget.grid(row=0, column=1, padx=5)

btn_budget = tk.Button(
    frame_budget,
    text="Simpan Budget",
    command=set_budget
)
btn_budget.grid(row=0, column=2, padx=5)

# =========================
# RIWAYAT TRANSAKSI
# =========================

label_riwayat = tk.Label(
    window,
    text="Riwayat Transaksi",
    font=("Arial", 12, "bold")
)
label_riwayat.pack(pady=10)

listbox_riwayat = tk.Listbox(window, width=90, height=15)
listbox_riwayat.pack(pady=10)

# =========================
# TOMBOL KELUAR
# =========================

btn_keluar = tk.Button(
    window,
    text="Keluar Aplikasi",
    width=20,
    bg="red",
    fg="white",
    command=window.destroy
)
btn_keluar.pack(pady=10)

# update dashboard pertama kali
update_dashboard()

# menjalankan aplikasi
window.mainloop()
