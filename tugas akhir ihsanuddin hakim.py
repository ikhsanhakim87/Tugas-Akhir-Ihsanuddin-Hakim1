import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan daftar produk
def display_products():
    products = {
        "1": {"nama": "Laptop", "harga": 8000000},
        "2": {"nama": "Smartphone", "harga": 3000000},
        "3": {"nama": "Smart TV", "harga": 6000000},
        "4": {"nama": "Kamera DSLR", "harga": 7000000},
    }

    product_list = "=== Daftar Produk ===\nKode |   Produk   |   Harga\n"
    for key, value in products.items():
        product_list += f"{key}    | {value['nama']:10} | Rp {value['harga']:,}\n"
    return product_list

# Fungsi saat tombol "Lihat Daftar Produk" ditekan
def show_products():
    product_window = tk.Toplevel(root)
    product_window.title("Daftar Produk")
    product_label = tk.Label(product_window, text=display_products(), padx=20, pady=20)
    product_label.pack()

# Fungsi saat tombol "Beli Produk" ditekan
def buy_products():
    def add_to_cart():
        choice = entry.get()
        nonlocal total_harga

        if choice.lower() == "selesai":
            messagebox.showinfo("Pembelian Selesai", f"Total belanja Anda adalah: Rp {total_harga:,}")
            buy_window.destroy()
        elif choice in products:
            cart.append(products[choice])
            total_harga += products[choice]["harga"]
            messagebox.showinfo("Produk Ditambahkan", f"{products[choice]['nama']} telah ditambahkan ke keranjang belanja.")
        else:
            messagebox.showerror("Kesalahan", "Kode produk tidak valid!")

    buy_window = tk.Toplevel(root)
    buy_window.title("Beli Produk")
    products = {
        "1": {"nama": "Laptop", "harga": 8000000},
        "2": {"nama": "Smartphone", "harga": 3000000},
        "3": {"nama": "Smart TV", "harga": 6000000},
        "4": {"nama": "Kamera DSLR", "harga": 7000000},
        "5": {"nama": "Air Conditioner", "harga": 2500000},
    }

    cart = []
    total_harga = 0

    label = tk.Label(buy_window, text="Pilih produk yang ingin dibeli (Ketik 'selesai' untuk mengakhiri):")
    label.pack()
    entry = tk.Entry(buy_window)
    entry.pack()

    add_button = tk.Button(buy_window, text="Tambahkan ke Keranjang", command=add_to_cart)
    add_button.pack()

    finish_button = tk.Button(buy_window, text="Selesai", command=add_to_cart)
    finish_button.pack()

# Fungsi untuk menampilkan menu
def display_menu():
    menu_label = tk.Label(root, text="=== Selamat Datang di Toko Elektronik ===")
    menu_label.grid(row=0, column=0, columnspan=2)

    show_button = tk.Button(root, text="Lihat Daftar Produk", command=show_products)
    show_button.grid(row=1, column=0, padx=10, pady=5)

    buy_button = tk.Button(root, text="Beli Produk", command=buy_products)
    buy_button.grid(row=1, column=1, padx=10, pady=5)

# Membuat window utama
root = tk.Tk()
root.title("Toko Elektronik Hakim")

display_menu()

root.mainloop()
