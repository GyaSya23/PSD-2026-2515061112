class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
            
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\n=== Kondisi Database (Loker Hash) ===")
        for i in range(self.SIZE):
            print(f"Loker {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"[{current.key} : {current.value}] -> ", end="")
                current = current.next
            print("Kosong")
        print("=====================================")


def main():
    db_mahasiswa = HashMapSeparateChaining(size=5)

    while True:
        print("\n" + "="*30)
        print("SISTEM DATABASE MAHASISWA")
        print("="*30)
        print("1. Tambah / Update Data")
        print("2. Cari Data")
        print("3. Hapus Data")
        print("4. Tampilkan Semua Loker")
        print("5. Keluar")
        print("="*30)
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            try:
                nim = int(input("Masukkan NIM (Angka): "))
                nama = input("Masukkan Nama Mahasiswa: ")
                db_mahasiswa.insert(nim, nama)
                print(f"Data '{nama}' dengan NIM {nim} berhasil disimpan!")
            except ValueError:
                print("Gagal: NIM harus berupa angka!")
                
        elif pilihan == '2':
            try:
                nim = int(input("Masukkan NIM yang dicari: "))
                hasil = db_mahasiswa.search(nim)
                if hasil is not None:
                    print(f"Ditemukan: NIM {nim} adalah milik {hasil.value}")
                else:
                    print(f"Tidak Ditemukan: NIM {nim} tidak ada di database.")
            except ValueError:
                print("Gagal: NIM harus berupa angka!")
                
        elif pilihan == '3':
            try:
                nim = int(input("Masukkan NIM yang akan dihapus: "))
                if db_mahasiswa.remove_key(nim):
                    print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")
                else:
                    print(f"Gagal: NIM {nim} tidak ditemukan di database.")
            except ValueError:
                print("Gagal: NIM harus berupa angka!")
                
        elif pilihan == '4':
            db_mahasiswa.display()
            
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem database ini. Sampai jumpa!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 5.")

if __name__ == "__main__":
    main()
