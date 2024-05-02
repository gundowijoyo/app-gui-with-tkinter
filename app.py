import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Fungsi untuk menambahkan barang
def tambah_barang():
    # Membuat pop up window
    global pop_up
    pop_up = tk.Toplevel(root)
    pop_up.title("Tambah Barang")
    
    # Menentukan ukuran pop up window dan posisinya di tengah layar
    pop_up_width = 300
    pop_up_height = 200
    #mendapatkan info lebar pop up
    root_width = root.winfo_width()
  #mendapatkan info tinggi pop up
    root_height = root.winfo_height()
   #menjumblah dan membagi dan mengurang
 x = (root.winfo_rootx() + root_width // 2) - (pop_up_width // 2)
    
    y = (root.winfo_rooty() + root_height // 2) - (pop_up_height // 2)
  pop_up.geometry(f"{pop_up_width}x{pop_up_height}+{x}+{y}")
    
    # Membuat label dan input fields untuk nama, stok, dan deskripsi barang
   label_nama = tk.Label(pop_up, text="Nama Barang:")
    label_nama.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_nama = tk.Entry(pop_up)
    entry_nama.grid(row=0, column=1, padx=5, pady=5)

    label_stok = tk.Label(pop_up, text="Stok Barang:")
    label_stok.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_stok = tk.Entry(pop_up)
    entry_stok.grid(row=1, column=1, padx=5, pady=5)

    label_deskripsi = tk.Label(pop_up, text="Deskripsi Barang:")
    label_deskripsi.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_deskripsi = tk.Entry(pop_up)
    entry_deskripsi.grid(row=2, column=1, padx=5, pady=5)

    # Membuat tombol untuk menyimpan dan membatalkan input barang
    button_simpan = ttk.Button(pop_up, text="Simpan", command=lambda: simpan_ke_database(entry_nama.get(), entry_stok.get(), entry_deskripsi.get()), style='TButton', cursor='hand2')
    button_simpan.grid(row=3, column=0, padx=5, pady=10, sticky="e")  # Sejajar ke kanan

    button_batal = ttk.Button(pop_up, text="Batal", command=pop_up.destroy, style='TButton', cursor='hand2')
    button_batal.grid(row=3, column=1, padx=5, pady=10, sticky="e")  # Sejajar ke kanan


# Fungsi untuk menyimpan data barang ke database
def simpan_ke_database(nama_barang, stok_barang, deskripsi_barang):
    try:
        # Buat koneksi ke database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",    # Ganti dengan username Anda
            password="",    # Ganti dengan password Anda
            database="db_barang"    # Ganti dengan nama database Anda
        )

        cursor = connection.cursor()

        # Buat query untuk menyimpan data ke dalam tabel
        query = "INSERT INTO barang (nama_barang, stok_barang, deskripsi_barang) VALUES (%s, %s, %s)"
        values = (nama_barang, stok_barang, deskripsi_barang)

        # Jalankan query
        cursor.execute(query, values)

        # Commit perubahan
        connection.commit()

        # Tampilkan popup berhasil menyimpan data
        messagebox.showinfo("Sukses", "Data berhasil disimpan!")

        # Perbarui tampilan tabel dengan data terbaru
        tampilkan_barang()

        # Tutup pop up window
        pop_up.destroy()
    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Koneksi ke database ditutup.")

# Fungsi untuk menampilkan data barang dari database ke Treeview
def tampilkan_barang():
    try:
        # Buat koneksi ke database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",    # Ganti dengan username Anda
            password="",    # Ganti dengan password Anda
            database="db_barang"    # Ganti dengan nama database Anda
        )

        cursor = connection.cursor()

        # Ambil data barang dari database
        cursor.execute("SELECT * FROM barang")
        rows = cursor.fetchall()

        # Bersihkan isi Treeview sebelum menampilkan data baru
        for row in treeview.get_children():
            treeview.delete(row)

        # Tampilkan data barang dalam Treeview
        for row in rows:
            treeview.insert("", "end", values=row)

        print("Data barang berhasil ditampilkan.")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Koneksi ke database ditutup.")

# Fungsi utama
def main():
    global root 
    root = tk.Tk()
    root.title('Aplikasi Tambah Barang')
    root.geometry('600x400')
    
    label = tk.Label(pady=20, text="Selamat datang Di Wahyu Store", font=('Poppins', 18, 'roman'))
    
    label.pack()

#membuat tombol tambah barang ke kanan 
    frame = tk.Frame(root)
    frame.pack(side="top", anchor="ne", padx=20, pady=10)
#tombol tambah barang
    button_green = tk.Button(frame, text="Tambah Barang", bg="green", fg="white", command=tambah_barang)
    button_green.pack()
    
    
    #style tulisan tebal pada kolom tabel
    style = ttk.Style()
    style.configure("Treeview.Heading",font=("Arial",10,"bold"))
    
  # Buat Treeview untuk menampilkan data barang dalam sebuah tabel menggunakan konsep Treeview
      global treeview
    treeview = ttk.Treeview(root, columns=("ID", "Nama Barang", "Stok", "Deskripsi"), show="headings")
    treeview.heading("ID", text="ID")
    treeview.heading("Nama Barang", text="Nama Barang")
    treeview.heading("Stok", text="Stok")
    treeview.heading("Deskripsi", text="Deskripsi")
    treeview.column("ID", width=50, anchor="center")
    treeview.column("Nama Barang", width=150, anchor="center")
    treeview.column("Stok", width=100, anchor="center")
    treeview.column("Deskripsi", width=200, anchor="center")
    treeview.pack()

    # Tampilkan data barang saat aplikasi dimulai
    tampilkan_barang()

    root.mainloop()

if __name__ == "__main__":
    main()
