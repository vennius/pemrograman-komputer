n = int(input("Masukkan jumlah baris: "))

for i in range(n):
    for j in range(n):
        if j <= i:
            print("o", end="")
        else:
            print("+", end="")
    print()
