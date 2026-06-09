# Sistem Database Mahasiswa Menggunakan Hash Map (Separate Chaining)

## a. Judul Program

Sistem Database Mahasiswa Menggunakan Hash Map dengan Metode Separate Chaining

## b. Deskripsi Singkat

Tujuan program ini dibuat adalah untuk menyimpan dan mengelola data mahasiswa menggunakan struktur data Hash Map dengan teknik Separate Chaining. Data mahasiswa disimpan menggunakan NIM sebagai key dan nama mahasiswa sebagai value.

Algoritma yang digunakan adalah Hash Map dengan metode Separate Chaining untuk menangani collision. Program mampu melakukan penambahan data, pencarian data, penghapusan data, pembaruan data, serta menampilkan seluruh isi Hash Table.

## c. Source Code

*(Masukkan screenshot source code di sini)*

### Penjelasan Kode

#### 1. Class `Node`

* Digunakan untuk membuat node pada Linked List
* Memiliki atribut:

  * `key` → menyimpan NIM mahasiswa
  * `value` → menyimpan nama mahasiswa
  * `next` → menunjuk ke node berikutnya

#### 2. Class `HashMapSeparateChaining`

* Digunakan untuk mengelola seluruh operasi Hash Map
* Memiliki komponen:

  * `SIZE` → ukuran Hash Table
  * `table` → array yang menyimpan bucket

#### 3. Fungsi `hash_function()`

* Digunakan untuk menentukan indeks penyimpanan data
* Mengubah key menjadi indeks bucket
* Menggunakan operasi modulus (`%`)

#### 4. Fungsi `insert()`

* Digunakan untuk menambah data mahasiswa
* Jika key sudah ada maka data diperbarui
* Jika key belum ada maka dibuat node baru
* Menangani collision menggunakan Separate Chaining

#### 5. Fungsi `search()`

* Digunakan untuk mencari data berdasarkan NIM
* Menelusuri Linked List pada bucket yang sesuai
* Mengembalikan data jika ditemukan

#### 6. Fungsi `remove_key()`

* Digunakan untuk menghapus data mahasiswa
* Mencari node yang sesuai dengan key
* Menghapus node dari Linked List

#### 7. Fungsi `display()`

* Menampilkan seluruh isi Hash Table
* Menampilkan setiap bucket beserta data yang tersimpan
* Mempermudah melihat collision yang terjadi

#### 8. Fungsi `main()`

* Menggunakan perulangan `while True`
* Menampilkan menu utama program
* Program berjalan sampai user memilih keluar

#### 9. Menu Program

* Tambah / Update Data Mahasiswa
* Cari Data Mahasiswa
* Hapus Data Mahasiswa
* Tampilkan Semua Data
* Keluar

#### 10. Input Data

* User memasukkan NIM mahasiswa
* User memasukkan nama mahasiswa
* Data disimpan ke dalam Hash Map

#### 11. Penanganan Collision

* Program menggunakan metode Separate Chaining
* Data yang memiliki indeks hash sama akan disimpan dalam satu bucket menggunakan Linked List

Contoh:

* `101 % 5 = 1`
* `106 % 5 = 1`
* `111 % 5 = 1`

Ketiga data tersebut akan masuk ke bucket yang sama.

#### 12. Validasi Input

* Menggunakan `try-except`
* Jika NIM bukan angka maka program menampilkan pesan error
* Input diminta kembali sampai valid

#### 13. Kompleksitas Algoritma

##### Best Case

* Insert = O(1)
* Search = O(1)
* Delete = O(1)

##### Worst Case

* Insert = O(n)
* Search = O(n)
* Delete = O(n)

Worst case terjadi ketika banyak data berada dalam bucket yang sama sehingga Linked List menjadi panjang.

## d. Output Program

*(Masukkan screenshot output program di sini)*

### Penjelasan Output

* Saat program dijalankan, user akan melihat menu utama Hash Map
* Saat memilih tambah data, user dapat memasukkan NIM dan nama mahasiswa
* Saat memilih cari data, program akan mencari mahasiswa berdasarkan NIM
* Saat memilih hapus data, program akan menghapus data mahasiswa yang dipilih
* Saat memilih tampilkan data, seluruh isi Hash Table akan ditampilkan
* Saat terjadi collision, data tetap tersimpan menggunakan Linked List pada bucket yang sama
* Saat memilih keluar, program akan berhenti

## e. Link YouTube
