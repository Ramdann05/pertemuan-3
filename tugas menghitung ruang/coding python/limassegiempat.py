import tkinter as tk
from tkinter import ttk

def hitung():
    # Ambil nilai dari Entry
    panjang_alas = float(entry_panjang_alas.get())
    lebar_alas = float(entry_lebar_alas.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    # Hitung volume dan luas permukaan
    volume = (panjang_alas * lebar_alas * tinggi_limas) / 3
    luas_permukaan = panjang_alas * lebar_alas + panjang_alas * (tinggi_limas**2 + lebar_alas**2)**0.5 + lebar_alas * (tinggi_limas**2 + panjang_alas**2)**0.5

    # Tampilkan hasil
    label_hasil.config(text=f"Volume: {volume:.2f} \nLuas Permukaan: {luas_permukaan:.2f}")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Volume dan Luas Permukaan Limas Segiempat")

# Label dan Entry untuk panjang alas
label_panjang_alas = ttk.Label(root, text="Panjang Alas:")
label_panjang_alas.grid(row=0, column=0, padx=10, pady=10, sticky="W")
entry_panjang_alas = ttk.Entry(root)
entry_panjang_alas.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk lebar alas
label_lebar_alas = ttk.Label(root, text="Lebar Alas:")
label_lebar_alas.grid(row=1, column=0, padx=10, pady=10, sticky="W")
entry_lebar_alas = ttk.Entry(root)
entry_lebar_alas.grid(row=1, column=1, padx=10, pady=10)

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
