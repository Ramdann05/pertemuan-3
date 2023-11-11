import tkinter as tk
from tkinter import ttk
import math

def hitung():
    # Ambil nilai dari Entry
    alas_limas = float(entry_alas_limas.get())
    tinggi_alas_limas = float(entry_tinggi_alas_limas.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    # Hitung volume dan luas permukaan
    volume = (alas_limas * tinggi_alas_limas * tinggi_limas) / 3
    luas_permukaan = (alas_limas * tinggi_limas) + (3 * alas_limas * tinggi_alas_limas)

    # Tampilkan hasil
    label_hasil.config(text=f"Volume: {volume:.2f} \nLuas Permukaan: {luas_permukaan:.2f}")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Volume dan Luas Permukaan Limas Segitiga")

# Label dan Entry untuk alas limas
label_alas_limas = ttk.Label(root, text="Alas Limas:")
label_alas_limas.grid(row=0, column=0, padx=10, pady=10, sticky="W")
entry_alas_limas = ttk.Entry(root)
entry_alas_limas.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi alas limas
label_tinggi_alas_limas = ttk.Label(root, text="Tinggi Alas Limas:")
label_tinggi_alas_limas.grid(row=1, column=0, padx=10, pady=10, sticky="W")
entry_tinggi_alas_limas = ttk.Entry(root)
entry_tinggi_alas_limas.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi limas
label_tinggi_limas = ttk.Label(root, text="Tinggi Limas:")
label_tinggi_limas.grid(row=2, column=0, padx=10, pady=10, sticky="W")
entry_tinggi_limas = ttk.Entry(root)
entry_tinggi_limas.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung
tombol_hitung = ttk.Button(root, text="Hitung", command=hitung)
tombol_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = ttk.Label(root, text="")
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
