class Node:
    def __init__(self, nilai):
        self.key = nilai
        self.left = None
        self.right = None


class BSTNilaiMahasiswa:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nilai):
        if root is None:
            return Node(nilai)

        if nilai < root.key:
            root.left = self.insert_node(root.left, nilai)
        elif nilai > root.key:
            root.right = self.insert_node(root.right, nilai)

        return root

    def insert(self, nilai):
        self.root = self.insert_node(self.root, nilai)

    def find_min_node(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    def delete_node(self, root, nilai):
        if root is None:
            return None

        if nilai < root.key:
            root.left = self.delete_node(root.left, nilai)

        elif nilai > root.key:
            root.right = self.delete_node(root.right, nilai)

        else:
            # Tidak punya anak
            if root.left is None and root.right is None:
                return None

            # Punya satu anak
            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Punya dua anak
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.right = self.delete_node(root.right, successor.key)

        return root

    def delete(self, nilai):
        self.root = self.delete_node(self.root, nilai)

    def height(self, root):
        if root is None:
            return -1

        tinggi_kiri = self.height(root.left)
        tinggi_kanan = self.height(root.right)

        return 1 + max(tinggi_kiri, tinggi_kanan)

    def level_order(self, root):
        if root is None:
            print("(data kosong)")
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            current = queue.pop(0)

            print(current.key, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        print()

    def find_successor(self, root, nilai):
        current = root
        successor = None

        while current is not None:
            if nilai < current.key:
                successor = current
                current = current.left

            elif nilai > current.key:
                current = current.right

            else:
                break

        if current is None:
            return None, False

        if current.right is not None:
            successor = self.find_min_node(current.right)

        if successor is None:
            return None, False

        return successor.key, True

    def find_predecessor(self, root, nilai):
        current = root
        predecessor = None

        while current is not None:
            if nilai > current.key:
                predecessor = current
                current = current.right

            elif nilai < current.key:
                current = current.left

            else:
                break

        if current is None:
            return None, False

        if current.left is not None:
            temp = current.left

            while temp.right is not None:
                temp = temp.right

            predecessor = temp

        if predecessor is None:
            return None, False

        return predecessor.key, True


def main():
    bst = BSTNilaiMahasiswa()
    pilih = 0

    while pilih != 7:
        print("\n=== Sistem Penyimpanan Nilai Mahasiswa ===")
        print("1. Tambah nilai mahasiswa")
        print("2. Hapus nilai mahasiswa")
        print("3. Tampilkan semua nilai (Level Order)")
        print("4. Lihat tinggi tree")
        print("5. Cari nilai setelahnya (Successor)")
        print("6. Cari nilai sebelumnya (Predecessor)")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            try:
                nilai = int(input("Masukkan nilai mahasiswa: "))
                bst.insert(nilai)

                print(f"Nilai {nilai} berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                nilai = int(input("Masukkan nilai yang ingin dihapus: "))
                bst.delete(nilai)

                print(f"Nilai {nilai} berhasil dihapus")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Daftar nilai mahasiswa:")
            bst.level_order(bst.root)

        elif pilih == 4:
            print(f"Tinggi tree: {bst.height(bst.root)}")

        elif pilih == 5:
            try:
                nilai = int(input("Cari nilai setelah: "))

                ans, found = bst.find_successor(bst.root, nilai)

                if found:
                    print(f"Nilai setelah {nilai} adalah {ans}")
                else:
                    print("Tidak ada successor")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 6:
            try:
                nilai = int(input("Cari nilai sebelum: "))

                ans, found = bst.find_predecessor(bst.root, nilai)

                if found:
                    print(f"Nilai sebelum {nilai} adalah {ans}")
                else:
                    print("Tidak ada predecessor")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 7:
            print("Program selesai")

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()
