nim = input("Masukkan NIM\t: ")
nama = input("Masukkan Nama\t: ")

len_nama = len(nama)
len_nim = len(nim)

for i in range(len_nama):
    print("| ", end="")
    for j in range(len_nama):
        if i >= (len_nama - j) - 1:
            print(nama[j], end="")
            continue
        print("_", end="")
    if i + 1 >= len_nim:
        print(f" | {nim[(i+1) - len_nim * ((i+1) // len_nim)]}")
        continue

    print(f" | {nim[i]}")
