import tkinter as tk
from tkinter import ttk
import math

def hitung():
    # Ambil nilai dari Entry
    jari_jari = float(entry_jari_jari.get())

    # Hitung volume dan luas permukaan
    volume = (4/3) * math.pi * jari_jari**3
    luas_permukaan = 4 * math.pi * jari_jari**2

    # Tampilkan hasil
    label_hasil.config(text=f"Volume: {volume:.2f} \nLuas Permukaan: {luas_permukaan:.2f}")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Volume dan Luas Permukaan Bola")

# Label dan Entry untuk jari-jari
label_jari_jari = ttk.Label(root, text="Jari-Jari:")
label_jari_jari.grid(row=0, column=0, padx=10, pady=10, sticky="W")
entry_jari_jari = ttk.Entry(root)
entry_jari_jari.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk menghitung
tombol_hitung = ttk.Button(root, text="Hitung", command=hitung)
tombol_hitung.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = ttk.Label(root, text="")
label_hasil.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
