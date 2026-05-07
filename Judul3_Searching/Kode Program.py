def binary_search_kontak(data, jumlah, target):
    kiri = 0
    kanan = jumlah - 1
    posisi = -1

    while kiri <= kanan:
        tengah = kiri + (kanan - kiri) // 2

        print(f"\nPosisi tengah: {tengah}")
        print(f"Nama tengah : {data[tengah][0]}")

        if data[tengah][0].lower() == target.lower():
            posisi = tengah
            break

        elif data[tengah][0].lower() < target.lower():
            print("Mencari di sebelah kanan")
            kiri = tengah + 1

        else:
            print("Mencari di sebelah kiri")
            kanan = tengah - 1

    return posisi


def main():

    try:
        jumlah = int(input("Masukkan jumlah kontak: "))

    except ValueError:
        print("Input harus berupa angka!")
        return

    kontak = []

    print("\nMasukkan data kontak:")

    for i in range(jumlah):

        print(f"\nKontak ke-{i+1}")

        nama = input("Nama            : ")
        nomor = input("Nomor Telepon   : ")

        kontak.append([nama, nomor])

    kontak.sort()

    print("\n=== DAFTAR KONTAK ===")

    for item in kontak:
        print(f"{item[0]} - {item[1]}")

    target = input("\nMasukkan nama yang ingin dicari: ")

    hasil = binary_search_kontak(kontak, jumlah, target)

    print("\n=== HASIL PENCARIAN ===")

    if hasil != -1:
        print("Kontak ditemukan")
        print(f"Nama   : {kontak[hasil][0]}")
        print(f"Nomor  : {kontak[hasil][1]}")
        print(f"Indeks : {hasil}")

    else:
        print("Kontak tidak ditemukan")


if __name__ == "__main__":
    main()
