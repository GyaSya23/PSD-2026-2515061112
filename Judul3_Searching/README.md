# Sistem Pencarian Nomor Telepon pada Kontak

## a. Judul Program

Sistem Pencarian Nomor Telepon pada Kontak Menggunakan Binary Search

## b. Deskripsi Singkat

Tujuan program ini dibuat adalah untuk melakukan pencarian nomor telepon pada daftar kontak menggunakan algoritma Binary Search. Setiap data kontak terdiri dari nama dan nomor telepon yang diinput oleh user.

Algoritma yang digunakan adalah Binary Search dengan konsep pencarian data secara efisien pada data yang telah diurutkan. Program mampu melakukan input data kontak, menampilkan daftar kontak, melakukan proses pencarian nama kontak, serta menampilkan hasil pencarian nomor telepon.

## c. Source Code
<img width="489" height="648" alt="Screenshot 2026-05-07 215233" src="https://github.com/user-attachments/assets/67730ac4-1c6b-4b2e-847b-f113072fb357" />
<img width="497" height="629" alt="Screenshot 2026-05-07 215244" src="https://github.com/user-attachments/assets/d62b1ce9-627b-4b83-b5d0-744047c034b7" />
<img width="359" height="130" alt="Screenshot 2026-05-07 215252" src="https://github.com/user-attachments/assets/2ecf5403-5561-4f64-a978-e59bfab5971c" />

## Penjelasan Kode

### 1. Inisialisasi Data

Digunakan untuk membuat struktur penyimpanan data kontak.

Memiliki komponen:

- `jumlah` → jumlah kontak
- `kontak` → list untuk menyimpan data kontak
- setiap data disimpan dalam bentuk list

### 2. Struktur Data

`kontak[i]`

- `i` → indeks data kontak

Isi dari setiap elemen:

- `kontak[i][0]` → nama kontak
- `kontak[i][1]` → nomor telepon

### 3. Fungsi binary_search_kontak()

Digunakan untuk mencari nama kontak menggunakan algoritma Binary Search.

Algoritma bekerja dengan cara:

- menentukan posisi tengah data
- membandingkan nama target dengan data tengah
- jika lebih besar mencari ke kanan
- jika lebih kecil mencari ke kiri
- proses dilakukan berulang hingga data ditemukan

### 4. Fungsi main()

Mengatur jalannya program.

Menggabungkan seluruh proses:

- input data kontak
- menampilkan daftar kontak
- proses pencarian
- menampilkan hasil pencarian

### 5. Input Data

Menggunakan perulangan sebanyak jumlah kontak.

Setiap iterasi:

- input nama kontak
- input nomor telepon

Data disimpan ke dalam:

python
kontak.append([nama, nomor])

### 6. Pengurutan Data

Sebelum proses Binary Search dilakukan, data kontak diurutkan terlebih dahulu menggunakan:

python
kontak.sort()


Pengurutan dilakukan berdasarkan nama kontak secara alfabetis.

### 7. Menampilkan Data Kontak

Menampilkan seluruh data kontak yang sudah diurutkan.

Tujuannya agar user dapat melihat daftar kontak sebelum melakukan pencarian.

### 8. Proses Pencarian

Menggunakan algoritma Binary Search.

Proses:

- mencari elemen tengah
- membandingkan dengan target
- menentukan arah pencarian
- dilakukan hingga data ditemukan atau tidak ditemukan

### 9. Menampilkan Hasil Pencarian

Jika data ditemukan:

- nama kontak ditampilkan
- nomor telepon ditampilkan
- posisi indeks ditampilkan

Jika tidak ditemukan:

- program menampilkan pesan “Kontak tidak ditemukan”

### 10. Kompleksitas Algoritma

- Best Case, O(1)
- Worst Case, O(log n)

Binary Search sangat efisien digunakan untuk pencarian data pada kumpulan data yang sudah terurut.

## d. Output Program
<img width="277" height="496" alt="Screenshot 2026-05-07 224124" src="https://github.com/user-attachments/assets/c9d26f59-ccee-460a-a6aa-fc906666d243" />
<img width="208" height="89" alt="Screenshot 2026-05-07 224131" src="https://github.com/user-attachments/assets/60a3e1a1-c0fe-499b-891e-96a100501ad1" />

## Penjelasan Output
Saat program dijalankan, user diminta memasukkan jumlah kontak.
Saat input data, user memasukkan nama dan nomor telepon kontak.
Data kontak akan diurutkan secara alfabetis sebelum proses pencarian dilakukan.
Program menggunakan Binary Search untuk mencari nama kontak yang dimasukkan user.
Selama proses pencarian, program menampilkan posisi tengah dan arah pencarian.
Jika kontak ditemukan, program menampilkan:
- nama kontak
- nomor telepon
- posisi indeks
Jika kontak tidak ditemukan, program menampilkan pesan:
Kontak tidak ditemukan

## e. Link YouTube

https://youtu.be/4AXquBs_Ejg?si=k0hVsxyDI5e2cskL
