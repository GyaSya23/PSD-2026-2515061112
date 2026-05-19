class QueuePrinter:
    def __init__(self, max_size=10):
        self.MAX = max_size
        self.queue = [None] * self.MAX
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.MAX == self.front

    def tambah_dokumen(self, dokumen):
        if self.is_full():
            print("Antrean printer penuh")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.MAX

        self.queue[self.rear] = dokumen
        print(f"Dokumen '{dokumen}' masuk ke antrean")

    def cetak_dokumen(self):
        if self.is_empty():
            print("Tidak ada dokumen untuk dicetak")
            return

        print(f"Mencetak dokumen: {self.queue[self.front]}")

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX

    def lihat_antrean(self):
        if self.is_empty():
            print("Antrean printer kosong")
            return

        print("Daftar antrean dokumen:")
        i = self.front

        while True:
            print("-", self.queue[i])

            if i == self.rear:
                break

            i = (i + 1) % self.MAX

    def dokumen_terdepan(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print(f"Dokumen berikutnya: {self.queue[self.front]}")


def main():
    printer = QueuePrinter()
    pilih = 0

    while pilih != 5:
        print("\n=== ANTREAN PRINTER ===")
        print("1. Tambah Dokumen")
        print("2. Cetak Dokumen")
        print("3. Lihat Dokumen Terdepan")
        print("4. Tampilkan Antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka")
            continue

        if pilih == 1:
            nama = input("Masukkan nama dokumen: ")
            printer.tambah_dokumen(nama)

        elif pilih == 2:
            printer.cetak_dokumen()

        elif pilih == 3:
            printer.dokumen_terdepan()

        elif pilih == 4:
            printer.lihat_antrean()

        elif pilih == 5:
            print("Program selesai")

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()
