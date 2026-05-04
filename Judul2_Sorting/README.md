# Sistem Pengurutan Prioritas Tugas Siswa Berdasarkan Deadline
## a. Judul Program
Sistem Pengurutan Prioritas Tugas Siswa Berdasarkan Deadline Menggunakan Insertion Sort
## b. Deskripsi Singkat
Tujuan program ini dibuat adalah untuk mengelola dan mengurutkan data tugas siswa berdasarkan deadline menggunakan algoritma Insertion Sort. Setiap data tugas terdiri dari nama tugas dan deadline yang diinput oleh user.

Algoritma yang digunakan adalah Insertion Sort dengan konsep pengurutan data berbasis perbandingan. Program mampu melakukan input data, menampilkan data sebelum diurutkan, melakukan proses pengurutan berdasarkan deadline, serta menampilkan hasil setelah diurutkan.
## c. Source Code
<img width="543" height="476" alt="Screenshot 2026-05-04 220817" src="https://github.com/user-attachments/assets/b27d7cab-67e4-4f05-848a-484117e08aa0" />
<img width="676" height="428" alt="Screenshot 2026-05-04 220833" src="https://github.com/user-attachments/assets/7359dc56-f3a6-4a4c-bcae-35aacd54bffd" />

### Penjelasan Kode

#### 1. Inisialisasi Data

Digunakan untuk membuat struktur penyimpanan data tugas

- Memiliki komponen:
  - `n` → jumlah tugas
  - `arr` → list untuk menyimpan data tugas
  - setiap data disimpan dalam bentuk tuple

### 2. Struktur Data

`arr[i]`

- `i` → indeks data tugas

Isi dari setiap elemen:
- `arr[i][0]` nama tugas
- `arr[i][1]` deadline

### 3. Fungsi `insertion_sort()`

- Digunakan untuk mengurutkan data berdasarkan deadline

- Algoritma bekerja dengan cara:
  - mengambil satu elemen sebagai kunci (`temp`)
  - membandingkan dengan elemen sebelumnya
  - menggeser elemen yang lebih besar
  - menyisipkan elemen ke posisi yang sesuai
 
### 4. Fungsi `main()`

- Mengatur jalannya program
- Menggabungkan seluruh proses:
  - input data
  - proses sorting
  - menampilkan hasil
 
### 5. Input Data

- Menggunakan perulangan sebanyak jumlah tugas

- Setiap iterasi:
  - input nama tugas
  - input deadline

- Data disimpan ke dalam:
  - `arr.append((nama, deadline))`

### 6. Validasi Input

- Digunakan untuk memastikan format deadline sesuai

- Format yang digunakan:
  - `YYYY-MM-DD`

- Jika tidak sesuai:
  - akan muncul pesan `"Format salah! Gunakan YYYY-MM-DD"`

### 7. Menampilkan Data Sebelum Sorting

- Menampilkan seluruh data tugas sesuai urutan input user

### 8. Proses Sorting

- Menggunakan algoritma Insertion Sort

- Proses:
  - membandingkan nilai deadline antar elemen
  - mengurutkan dari yang terkecil (terdekat)
 
### 9. Menampilkan Data Setelah Sorting

- Menampilkan data yang sudah diurutkan berdasarkan deadline

### 10. Kompleksitas Algoritma

- Best case O(n)
- Worst case O(n²)
- Cocok untuk data dalam jumlah kecil

 ## d. Output Program
<img width="446" height="334" alt="Screenshot 2026-05-04 221826" src="https://github.com/user-attachments/assets/80f3a686-d77c-4165-81d4-05c8c4c7b3a3" />

### Penjelasan Output

- Saat program dijalankan, user diminta memasukkan jumlah tugas  
- Saat input data, user memasukkan nama tugas dan deadline  
- Data awal ditampilkan sesuai urutan input  
- Setelah proses sorting, data diurutkan berdasarkan deadline terdekat  
- Tugas dengan deadline paling cepat akan berada di posisi pertama  
- Jika format deadline salah, program akan meminta input ulang  
- Jika jumlah tugas tidak valid, program menampilkan pesan error

## e. Link YouTube
