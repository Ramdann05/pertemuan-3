import tkinter as tk
from tkinter import ttk

def hitung():
    # Ambil nilai dari Entry
    sisi = float(entry_sisi.get())

    # Hitung volume dan luas permukaan
    volume = sisi**3
    luas_permukaan = 6 * sisi**2

    # Tampilkan hasil
    label_hasil.config(text=f"Volume: {volume:.2f} \nLuas Permukaan: {luas_permukaan:.2f}")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Volume dan Luas Permukaan Kubus")

# Label dan Entry untuk panjang sisi
label_sisi = ttk.Label(root, text="Panjang Sisi:")
label_sisi.grid(row=0, column=0, padx=10, pady=10, sticky="W")
entry_sisi = ttk.Entry(root)
entry_sisi.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk menghitung
tombol_hitung = ttk.Button(root, text="Hitung", command=hitung)
tombol_hitung.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = ttk.Label(root, text="")
label_hasil.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
