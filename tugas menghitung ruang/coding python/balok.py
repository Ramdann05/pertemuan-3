import tkinter as tk
from tkinter import ttk

def hitung():
    # Ambil nilai dari Entry
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi = float(entry_tinggi.get())

    # Hitung volume dan luas permukaan
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

    # Tampilkan hasil
    label_hasil.config(text=f"Volume: {volume:.2f} \nLuas Permukaan: {luas_permukaan:.2f}")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Volume dan Luas Permukaan Balok")

# Label dan Entry untuk panjang
label_panjang = ttk.Label(root, text="Panjang:")
label_panjang.grid(row=0, column=0, padx=10, pady=10, sticky="W")
entry_panjang = ttk.Entry(root)
entry_panjang.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk lebar
label_lebar = ttk.Label(root, text="Lebar:")
label_lebar.grid(row=1, column=0, padx=10, pady=10, sticky="W")
entry_lebar = ttk.Entry(root)
entry_lebar.grid(row=1, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi
label_tinggi = ttk.Label(root, text="Tinggi:")
label_tinggi.grid(row=2, column=0, padx=10, pady=10, sticky="W")
entry_tinggi = ttk.Entry(root)
entry_tinggi.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung
tombol_hitung = ttk.Button(root, text="Hitung", command=hitung)
tombol_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = ttk.Label(root, text="")
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
