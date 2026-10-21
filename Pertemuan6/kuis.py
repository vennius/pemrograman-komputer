for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)


modify = input("Apakah anda ingin modifikasi tampilan deret? [Y/T] ").upper()

while modify == "Y":
    total = input("Tampilkan Total Ganjil atau Genap? ").lower()
    if total == "ganjil":
       for i in range(1, 6):
            for j in range(i + 1, 6):
                if (i + j) % 2 != 0:
                    print(i, j) 
    elif total == "genap":
        for i in range(1, 6):
            for j in range(i + 1, 6):
                if (i + j) % 2 == 0:
                    print(i, j)

    else:
        continue

    modify = input("Apakah anda ingin modifikasi tampilan deret? [Y/T] ").upper()

print("Terima kasih telah menggunakan program ini!")
