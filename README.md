# Panduan Instalasi Tkinter, mysql-connector-python, dan cx_Freeze

## Deskripsi
Repo ini berisi aplikasi Python yang menggunakan Tkinter untuk antarmuka pengguna, mysql-connector-python untuk menghubungkan ke database MySQL, dan cx_Freeze untuk mengonversi aplikasi menjadi file eksekusi yang dapat dijalankan di berbagai platform.

### Fungsi-fungsi Utama:
1. **Tkinter**: Modul untuk pembuatan antarmuka grafis pengguna (GUI) pada Python.
2. **mysql-connector-python**: Modul untuk menghubungkan aplikasi Python dengan database MySQL.
3. **cx_Freeze**: Modul untuk mengonversi aplikasi Python menjadi file eksekusi (executable) yang dapat dijalankan di berbagai platform.

## Langkah-langkah Instalasi

1. **Instalasi Tkinter**
   - Jika menggunakan Python versi 3.x, Tkinter biasanya sudah terpasang secara default.
   - Jika tidak terpasang, Anda dapat menginstalnya menggunakan manajer paket Python seperti pip:
     ```
     pip install tk
     ```

2. **Instalasi mysql-connector-python**
   - Anda dapat menginstal mysql-connector-python menggunakan pip:
     ```
     pip install mysql-connector-python
     ```

3. **Instalasi cx_Freeze**
   - Anda dapat menginstal cx_Freeze menggunakan pip:
     ```
     pip install cx-Freeze
     ```

## Impor Database ke phpMyAdmin

1. **Buka phpMyAdmin**
   - Buka phpMyAdmin melalui browser Anda.

2. **Login ke phpMyAdmin**
   - Masukkan kredensial login Anda untuk mengakses phpMyAdmin.

3. **Buat Database Baru**
   - Buat database baru dengan nama yang diinginkan.

4. **Impor Database db.sql**
   - Pilih database yang baru dibuat.
   - Pilih opsi "Impor" di panel atas.
   - Pilih file db.sql dari direktori proyek Anda.
   - Klik tombol "Impor" untuk memulai proses impor database.

## Menjalankan Aplikasi
- Setelah langkah-langkah instalasi selesai, Anda dapat menjalankan aplikasi Python yang menggunakan Tkinter, mysql-connector-python, dan cx_Freeze sesuai dengan instruksi yang disediakan dalam proyek.

Selamat menggunakan!
