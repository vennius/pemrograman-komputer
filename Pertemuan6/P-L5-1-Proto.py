n = int(input("Masukkan N: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(n - (i-1), n+1):
        print(j, end="")

    for j in range(n, n - i, -1):
        print(j, end="")

    print()

for i in range(n, 0, -1):
    print(" " * (n - i), end="")

    for j in range(n - (i-1), n+1):
        print(j, end="")

    for j in range(n, n - i, -1):
        print(j, end="")

    print()
