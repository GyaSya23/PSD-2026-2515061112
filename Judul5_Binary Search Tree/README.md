# Sistem Penyimpanan Nilai Mahasiswa Menggunakan Binary Search Tree

## a. Judul Program
**Sistem Penyimpanan Nilai Mahasiswa Menggunakan Binary Search Tree (BST)**

## b. Deskripsi Singkat
Tujuan program ini dibuat adalah untuk menyimpan dan mengelola data nilai mahasiswa menggunakan struktur data **Binary Search Tree (BST)**. Program dapat melakukan penambahan data nilai, penghapusan nilai, menampilkan data, mencari successor dan predecessor, serta mengetahui tinggi tree.

Binary Search Tree digunakan karena mampu menyimpan data secara terurut otomatis. Nilai yang lebih kecil akan ditempatkan di sebelah kiri node, sedangkan nilai yang lebih besar ditempatkan di sebelah kanan node.

Program ini memiliki beberapa fungsi yang dapat berjalan yaitu:
- menambah nilai mahasiswa,
- menghapus nilai,
- menampilkan data secara level-order,
- mencari nilai setelahnya *(successor)*,
- mencari nilai sebelumnya *(predecessor)*,
- dan menghitung tinggi tree.


## c. Source Code

<img width="537" height="666" alt="Screenshot 2026-05-26 194200" src="https://github.com/user-attachments/assets/4229f18c-19d2-4c64-a516-df2bb507218f" />
<img width="608" height="633" alt="Screenshot 2026-05-26 194214" src="https://github.com/user-attachments/assets/fa7dc7a9-c381-4e09-8661-e8b4e4ed87f5" />
<img width="439" height="627" alt="Screenshot 2026-05-26 194228" src="https://github.com/user-attachments/assets/c811457a-3f85-4b6b-8ba8-a3fab7b71d56" />
<img width="515" height="627" alt="Screenshot 2026-05-26 194241" src="https://github.com/user-attachments/assets/0cdd5a73-9759-42fd-8061-e3805cd4fe74" />
<img width="526" height="625" alt="Screenshot 2026-05-26 194304" src="https://github.com/user-attachments/assets/2a845af6-ffe4-4cb4-80c2-a472caaee29a" />
<img width="625" height="647" alt="Screenshot 2026-05-26 194319" src="https://github.com/user-attachments/assets/b0e8cd5c-9ccd-4c64-99c8-9fcedc976042" />
<img width="574" height="640" alt="Screenshot 2026-05-26 194359" src="https://github.com/user-attachments/assets/93f02685-78cf-4d1e-81c0-ad1e4e101dfd" />
<img width="273" height="52" alt="Screenshot 2026-05-26 194404" src="https://github.com/user-attachments/assets/bb826097-46ab-4c2a-a238-00b21a792df8" />

# Penjelasan Kode

## 1. Class Node
Digunakan untuk membuat node pada Binary Search Tree.

Setiap node memiliki:
- key = menyimpan nilai mahasiswa
- left = pointer ke anak kiri
- right = pointer ke anak kanan

## 2. Class BSTNilaiMahasiswa
Digunakan untuk mengelola seluruh operasi pada Binary Search Tree.

Class ini memiliki:
- root = akar dari tree
- fungsi insert
- fungsi delete
- fungsi traversal
- fungsi successor dan predecessor

## 3. Fungsi insert_node()
Digunakan untuk menambahkan data nilai ke dalam tree.

### Cara kerja:
- jika tree kosong maka dibuat node baru
- jika nilai lebih kecil maka masuk ke kiri
- jika nilai lebih besar maka masuk ke kanan

BST akan menjaga data tetap terurut secara otomatis.

## 4. Fungsi delete_node()
Digunakan untuk menghapus data nilai dari tree.

Terdapat 3 kondisi:
- node tidak memiliki anak
- node memiliki satu anak
- node memiliki dua anak

Jika node memiliki dua anak, program akan mencari successor untuk menggantikan node yang dihapus.

## 5. Fungsi find_min_node()
Digunakan untuk mencari node dengan nilai terkecil.

Fungsi ini berjalan terus ke kiri hingga menemukan node paling kiri.

Biasanya digunakan saat proses penghapusan node yang memiliki dua anak.


## 6. Fungsi level_order()
Digunakan untuk menampilkan data nilai secara level-order traversal.

Traversal dilakukan menggunakan queue.

Data akan ditampilkan dari atas ke bawah dan dari kiri ke kanan.

## 7. Fungsi height()
Digunakan untuk menghitung tinggi tree.

Tinggi tree menunjukkan kedalaman struktur Binary Search Tree.

Semakin tinggi tree, maka proses pencarian bisa menjadi lebih lama.

## 8. Fungsi find_successor()
Digunakan untuk mencari nilai setelah suatu nilai tertentu.

Successor adalah nilai yang lebih besar terdekat dalam BST.

### Contoh:
- successor dari 70 adalah 75

## 9. Fungsi find_predecessor()
Digunakan untuk mencari nilai sebelum suatu nilai tertentu.

Predecessor adalah nilai yang lebih kecil terdekat dalam BST.

### Contoh:
- predecessor dari 70 adalah 65

## 10. Fungsi main()
Digunakan untuk menjalankan seluruh program.

### Menu yang tersedia:
1. Tambah nilai mahasiswa
2. Hapus nilai mahasiswa
3. Tampilkan data
4. Lihat tinggi tree
5. Cari successor
6. Cari predecessor
7. Keluar program

## 11. Input Data
User memasukkan nilai mahasiswa dalam bentuk angka integer.

Data akan langsung dimasukkan ke Binary Search Tree sesuai aturan BST.

## 12. Validasi Input
Program menggunakan try-except untuk menangani kesalahan input.

Jika user memasukkan selain angka:
- program akan menampilkan pesan error
- input diminta ulang

## 13. Kompleksitas Algoritma

### Best Case
- Insert = O(log n)
- Search = O(log n)
- Delete = O(log n)

### Worst Case
- O(n)

Worst case terjadi jika tree tidak seimbang.

## d. Output Program

<img width="320" height="607" alt="Screenshot 2026-05-26 201754" src="https://github.com/user-attachments/assets/bddfa076-6731-41f2-8548-6e5b9976c9a7" />
<img width="310" height="589" alt="Screenshot 2026-05-26 201809" src="https://github.com/user-attachments/assets/f50ac596-f331-4007-91b3-18f72db4a536" />
<img width="316" height="606" alt="Screenshot 2026-05-26 201822" src="https://github.com/user-attachments/assets/08f4053e-083c-4ff3-8250-f585f0523400" />
<img width="306" height="178" alt="Screenshot 2026-05-26 201830" src="https://github.com/user-attachments/assets/56055655-3f4a-4840-a091-5f26cf7ff2b3" />

# Penjelasan Output
Saat program dijalankan, user akan melihat menu utama Binary Search Tree.

User dapat:
- menambahkan nilai mahasiswa,
- menghapus nilai,
- melihat isi tree,
- mencari successor,
- mencari predecessor,
- dan melihat tinggi tree.

Data nilai akan tersimpan secara terurut otomatis sesuai konsep Binary Search Tree.

Jika input tidak valid, program akan menampilkan pesan error.

Program akan berhenti ketika user memilih menu keluar.

## e. Link YouTube
