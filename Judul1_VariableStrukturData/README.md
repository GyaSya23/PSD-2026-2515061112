# Sistem Penilaian Mahasiswa per Mata Kuliah Menggunakan (List 2D)
## a. Judul Program
Sistem Penilaian Mahasiswa per Mata Kuliah Menggunakan List 2 Dimensi
## b. Deskripsi Singkat
Tujuan program ini dibuat adalah untuk mengelola data nilai mahasiswa dalam beberapa mata kuliah menggunakan struktur data List 2 Dimensi. Setiap baris merepresentasikan mahasiswa, sedangkan setiap kolom merepresentasikan mata kuliah.

Algoritma yang digunakan adalah struktur data array 2 dimensi (List 2D) dengan konsep pengolahan data berbasis indeks. Program mampu melakukan input data, menampilkan data, menghitung rata-rata per baris (mahasiswa), rata-rata per kolom (mata kuliah), serta mencari nilai maksimum dalam seluruh data.
## c. Source Code
<img width="531" height="265" alt="Screenshot 2026-04-29 224808" src="https://github.com/user-attachments/assets/9839b65a-2260-41e1-bb7f-27ca4d58427e" />
<img width="634" height="404" alt="Screenshot 2026-04-29 233623" src="https://github.com/user-attachments/assets/851d829a-8752-48bb-b572-618498f2989d" />
<img width="478" height="343" alt="Screenshot 2026-04-29 224252" src="https://github.com/user-attachments/assets/c4cdfa80-5723-430c-8104-b60cc28d69e4" />
<img width="642" height="252" alt="Screenshot 2026-04-29 224311" src="https://github.com/user-attachments/assets/46b61371-f6ea-4df8-b73c-58e7ca95151a" />

### Penjelasan Kode

#### 1. Inisialisasi Data

- Digunakan untuk membuat struktur List 2D
- Memiliki komponen:
  - `mahasiswa` → jumlah baris (data mahasiswa)
  - `matkul` → jumlah kolom (mata kuliah)
  - `nilai` → array 2 dimensi untuk menyimpan nilai

#### 2. Struktur List 2D

- `nilai[i][j]`
  - `i` → indeks mahasiswa (baris)
  - `j` → indeks mata kuliah (kolom)

#### 3. Fungsi `menu()`

- Menampilkan pilihan menu kepada user:
  - Input nilai
  - Tampilkan data
  - Rata-rata mahasiswa
  - Rata-rata mata kuliah
  - Nilai tertinggi
  - Keluar

#### 4. Fungsi `main()`

- Menggunakan perulangan `while True`
- Program akan terus berjalan sampai user memilih keluar

#### 5. Input Nilai

- Menggunakan nested loop:
  - Loop pertama → mahasiswa
  - Loop kedua → mata kuliah
- Data disimpan ke dalam:
  - `nilai[i][j]`

#### 6. Menampilkan Data

- Menampilkan isi array per baris
- Setiap baris merepresentasikan satu mahasiswa

#### 7. Rata-rata per Mahasiswa

- Menggunakan:
  - `sum(nilai[i]) / matkul`
- Menghitung rata-rata nilai dalam satu baris

#### 8. Rata-rata per Mata Kuliah

- Menggunakan loop kolom
- Menjumlahkan semua nilai pada kolom tertentu
- Dibagi jumlah mahasiswa

#### 9. Mencari Nilai Tertinggi

- Membandingkan seluruh elemen dalam array
- Menyimpan nilai terbesar dan posisinya `(i, j)`

#### 10. Validasi Input

- Input menu menggunakan `input()`
- Jika pilihan tidak sesuai:
  - akan muncul pesan `"Pilihan tidak valid!"`

 ## d. Output Program
 <img width="222" height="294" alt="Screenshot 2026-04-29 225924" src="https://github.com/user-attachments/assets/bd93e0a5-aaec-408a-9f9f-bacd11bb9c1e" />
<img width="223" height="229" alt="Screenshot 2026-04-29 225942" src="https://github.com/user-attachments/assets/4630fd0f-518f-4648-9fcf-912022176e21" />
<img width="226" height="227" alt="Screenshot 2026-04-29 230001" src="https://github.com/user-attachments/assets/294d11b0-f29c-4a29-9f1a-ec7265ec93f9" />
<img width="226" height="225" alt="Screenshot 2026-04-29 230022" src="https://github.com/user-attachments/assets/c4249d19-1107-4fdc-bfde-0c072fb10f66" />
<img width="248" height="161" alt="Screenshot 2026-04-29 230035" src="https://github.com/user-attachments/assets/a75064ad-bf6a-459c-961f-cd61de0e077e" />
<img width="217" height="154" alt="Screenshot 2026-04-29 230048" src="https://github.com/user-attachments/assets/c5ce7900-0aa8-4ea7-ac22-976c76fdf72a" />

### Penjelasan Output
- Saat user memilih menu → program menampilkan opsi yang tersedia  
- Saat memilih input nilai → user diminta mengisi nilai untuk setiap mahasiswa dan mata kuliah  
- Saat menampilkan data → seluruh nilai ditampilkan dalam bentuk array 2D  
- Saat menghitung rata-rata mahasiswa → muncul nilai rata-rata per baris  
- Saat menghitung rata-rata mata kuliah → muncul nilai rata-rata per kolom  
- Saat mencari nilai tertinggi → ditampilkan nilai terbesar beserta posisinya  
- Saat memilih menu tidak valid → muncul pesan "Pilihan tidak valid!"  
- Saat memilih keluar → program berhenti

## e. Link YouTube
