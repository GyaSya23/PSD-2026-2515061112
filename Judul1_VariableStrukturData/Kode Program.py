def menu():
    print("\n=== SISTEM NILAI MAHASISWA ===")
    print("1. Input nilai")
    print("2. Tampilkan semua nilai")
    print("3. Rata-rata per mahasiswa")
    print("4. Rata-rata per mata kuliah")
    print("5. Cari nilai tertinggi")
    print("6. Keluar")


def main():
    mahasiswa = 3
    matkul = 3

    nilai = [[0 for j in range(matkul)] for i in range(mahasiswa)]

    while True:
        menu()
        pilihan = input("Pilih: ")

        if pilihan == '1':
            for i in range(mahasiswa):
                for j in range(matkul):
                    nilai[i][j] = int(input(f"Nilai Mhs-{i+1} MK-{j+1}: "))

        elif pilihan == '2':
            print("\nData Nilai:")
            for i in range(mahasiswa):
                print(f"Mhs-{i+1}: {nilai[i]}")

        elif pilihan == '3':
            print("\nRata-rata per Mahasiswa:")
            for i in range(mahasiswa):
                rata = sum(nilai[i]) / matkul
                print(f"Mhs-{i+1}: {rata}")

        elif pilihan == '4':
            print("\nRata-rata per Mata Kuliah:")
            for j in range(matkul):
                total = 0
                for i in range(mahasiswa):
                    total += nilai[i][j]
                print(f"MK-{j+1}: {total / mahasiswa}")

        elif pilihan == '5':
            maks = nilai[0][0]
            pos = (0, 0)

            for i in range(mahasiswa):
                for j in range(matkul):
                    if nilai[i][j] > maks:
                        maks = nilai[i][j]
                        pos = (i, j)

            print(f"Nilai tertinggi: {maks} (Mhs-{pos[0]+1}, MK-{pos[1]+1})")

        elif pilihan == '6':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
