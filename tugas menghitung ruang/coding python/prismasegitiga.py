import tkinter as tk
from tkinter import ttk
import math

def hitung():
    # Ambil nilai dari Entry
    alas_prisma = float(entry_alas_prisma.get())
    tinggi_alas_prisma = float(entry_tinggi_alas_prisma.get())
    tinggi_prisma = float(entry_tinggi_prisma.get())

    # Hitung volume dan luas permukaan
    volume = (alas_prisma * tinggi_alas_prisma * tinggi_prisma) / 2
    luas_permukaan = (alas_prisma * tinggi_prisma) + (3 * alas_prisma * tinggi_alas_prisma)

    # Tampilkan hasil
    label_hasil.config(text=f"Volume: {volume:.2f} \nLuas Permukaan: {luas_permukaan:.2f}")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Volume dan Luas Permukaan Prisma Segitiga")

# Label dan Entry untuk alas prisma
label_alas_prisma = ttk.Label(root, text="Alas Prisma:")
label_alas_prisma.grid(row=0, column=0, padx=10, pady=10, sticky="W")
entry_alas_prisma = ttk.Entry(root)
entry_alas_prisma.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi alas prisma
label_tinggi_alas_prisma = ttk.Label(root, text="Tinggi Alas Prisma:")
label_tinggi_alas_prisma.grid(row=1, column=0, padx=10, pady=10, sticky="W")
entry_tinggi_alas_prisma = ttk.Entry(root)
entry_tinggi_alas_prisma.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi prisma
label_tinggi_prisma = ttk.Label(root, text="Tinggi Prisma:")
label_tinggi_prisma.grid(row=2, column=0, padx=10, pady=10, sticky="W")
entry_tinggi_prisma = ttk.Entry(root)
entry_tinggi_prisma.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung
tombol_hitung = ttk.Button(root, text="Hitung", command=hitung)
tombol_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = ttk.Label(root, text="")
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
