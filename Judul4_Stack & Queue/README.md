# Sistem Antrean Printer Menggunakan Queue Array
## a. Judul Program

**Sistem Antrean Printer Menggunakan Queue Array dengan Circular Queue**

## b. Deskripsi Singkat

Tujuan program ini dibuat adalah untuk mensimulasikan sistem antrean printer menggunakan struktur data Queue berbasis array. Program digunakan untuk mengatur dokumen yang akan dicetak berdasarkan urutan kedatangan dokumen.

Konsep yang digunakan adalah Queue dengan prinsip FIFO (*First In First Out*), yaitu dokumen yang pertama masuk ke antrean akan dicetak lebih dahulu.

Implementasi queue menggunakan array dengan metode Circular Queue agar penggunaan memori lebih efisien dan posisi array dapat digunakan kembali setelah proses dequeue.

Program mampu melakukan:
- menambahkan dokumen ke antrean
- mencetak dokumen
- melihat dokumen terdepan
- menampilkan seluruh antrean dokumen

# c. Source Code
<img width="535" height="665" alt="Screenshot 2026-05-19 214730" src="https://github.com/user-attachments/assets/38290b38-076d-4f2b-aa2c-5febebc13513" />
<img width="538" height="614" alt="Screenshot 2026-05-19 214904" src="https://github.com/user-attachments/assets/f5c11049-696c-4b3b-a6a0-9c0bd8367872" />
<img width="458" height="597" alt="Screenshot 2026-05-19 214917" src="https://github.com/user-attachments/assets/5aad0748-3447-49a0-8707-cdd471ef8378" />
<img width="364" height="136" alt="Screenshot 2026-05-19 214924" src="https://github.com/user-attachments/assets/4b271297-f078-486b-974f-59897d28646c" />

### 1. Inisialisasi Data

Digunakan untuk membuat struktur penyimpanan antrean printer.

Memiliki komponen:
- MAX : kapasitas maksimum queue
- queue : array penyimpanan data dokumen
- front : penunjuk data paling depan
- rear : penunjuk data paling belakang

### 2. Struktur Data

python
queue[i]

i → indeks array queue

Isi setiap elemen berupa:
- nama dokumen yang akan dicetak

Contoh:

python
queue[0] = "Laporan.pdf"

### 3. Fungsi `is_empty()`

Digunakan untuk mengecek apakah antrean kosong.

Kondisi queue kosong:

python
front == -1


Jika kosong:
- proses cetak tidak dapat dilakukan

### 4. Fungsi `is_full()`

Digunakan untuk mengecek apakah antrean penuh.

Menggunakan konsep Circular Queue:

python
(rear + 1) % MAX == front

Jika penuh:
- dokumen baru tidak dapat ditambahkan

### 5. Fungsi `tambah_dokumen()`

Digunakan untuk menambahkan dokumen ke antrean printer.

Proses:
- mengecek queue penuh atau tidak
- menambahkan dokumen ke posisi rear
- rear akan bergeser ke indeks berikutnya

Data dimasukkan menggunakan:
python
self.queue[self.rear] = dokumen

### 6. Fungsi `cetak_dokumen()`

Digunakan untuk mencetak dokumen paling depan.

Proses:
- mengambil data pada posisi front
- menampilkan dokumen yang dicetak
- front bergeser ke data berikutnya

Jika antrean habis:

python
front = -1
rear = -1

### 7. Fungsi `dokumen_terdepan()`

Digunakan untuk melihat dokumen yang berada di posisi paling depan tanpa menghapus data dari queue.

Data yang ditampilkan:

python
queue[front]

### 8. Fungsi `lihat_antrean()`

Digunakan untuk menampilkan seluruh isi antrean printer.

Penampilan data dilakukan dari:
- posisi front
- hingga rear

Menggunakan perulangan:

python
while True

Karena queue menggunakan Circular Queue, indeks akan kembali ke awal array jika mencapai batas maksimum.

### 9. Fungsi `main()`

Digunakan untuk mengatur jalannya program.

Fungsi ini menggabungkan:
- menu program
- input user
- pemanggilan fungsi queue

Menu yang tersedia:
1. Tambah Dokumen
2. Cetak Dokumen
3. Lihat Dokumen Terdepan
4. Tampilkan Antrean
5. Keluar


### 10. Validasi Input

Digunakan untuk memastikan input menu berupa angka.

Menggunakan:

python
try-except

Jika input salah:

Input harus angka


### 11. Proses Queue

Program menggunakan prinsip:

FIFO (First In First Out)

Artinya:
- dokumen pertama masuk
- akan dicetak pertama kali

Contoh:


Dokumen A masuk dulu
Dokumen A dicetak dulu

### 12. Kompleksitas Algoritma

#### Enqueue

O(1)
#### Dequeue

O(1)
#### Display Queue

O(n)
Queue array sangat efisien digunakan untuk proses antrean sederhana dengan jumlah data yang relatif stabil.

## d. Output Program
<img width="248" height="502" alt="Screenshot 2026-05-19 231055" src="https://github.com/user-attachments/assets/44c05e44-270d-40d1-a371-506a327fb796" />
<img width="198" height="518" alt="Screenshot 2026-05-19 231152" src="https://github.com/user-attachments/assets/1fe69e1e-0288-4734-98f3-0ec78e959b95" />
<img width="195" height="620" alt="Screenshot 2026-05-19 231222" src="https://github.com/user-attachments/assets/cdf50cc6-fa2d-4b7e-a2e4-d87e57556dcd" />

### Penjelasan Output

Saat program dijalankan:
- user memilih menu sesuai kebutuhan

Jika memilih:

#### Tambah Dokumen

User memasukkan nama dokumen lalu data masuk ke antrean printer.

#### Cetak Dokumen

Dokumen paling depan akan dicetak dan dihapus dari queue.

#### Lihat Dokumen Terdepan

Program menampilkan dokumen yang akan dicetak berikutnya.

#### Tampilkan Antrean

Program menampilkan seluruh daftar dokumen dalam antrean.

Jika antrean kosong:

Queue printer kosong

Jika antrean penuh:

Antrean printer penuh



## e. Link YouTube
https://youtu.be/gVdQ5cE-Djw
