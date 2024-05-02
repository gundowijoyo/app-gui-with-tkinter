CREATE DATABASE ;
USE db_barang;

CREATE TABLE barang(
id INT AUTO_INCREMENT PRIMARY KEY,
nama_barang VARCHAR(255) NOT NULL,
stok_barang INT NOT NULL,
deskripsi_barang VARCHAR(255) NOT NULL
) 