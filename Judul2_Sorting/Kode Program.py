def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j][1] > temp[1]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah tugas: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan data tugas (nama dan deadline YYYY-MM-DD):")

    for i in range(n):
        nama = input(f"Nama tugas ke-{i+1}: ")
        
        while True:
            deadline = input("Deadline (YYYY-MM-DD): ")
            if len(deadline) == 10 and deadline[4] == '-' and deadline[7] == '-':
                break
            else:
                print("Format salah! Gunakan YYYY-MM-DD")

        arr.append((nama, deadline))

    print("\nData sebelum diurutkan:")
    for tugas in arr:
        print(f"{tugas[0]} - {tugas[1]}")

    insertion_sort(arr, n)

    print("\nData setelah diurutkan (berdasarkan deadline):")
    for i in range(n):
        print(f"{arr[i][0]} - {arr[i][1]}")


if __name__ == "__main__":
    main()
