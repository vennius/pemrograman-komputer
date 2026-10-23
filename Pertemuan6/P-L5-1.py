n = int(input("Masukkan jumlah baris dan kolom: "))

# test = []
#
# for i in range(n):
#     print(f"{" "* (n - (i+1))}", end="")
#     for j in range(n-(i+1), n):
#         print(j+1, end="")
#         test.append(str(j+1))
#     test.reverse()
#     print("".join(test), end="")
#     test = []
#     print()

for i in range(n):
    print(f"{" "* (n - (i+1))}", end="")
    for j in range(n-(i+1), n):
        print(j+1, end="")

    for j in range(n, n-i-1, -1):
        print(j, end="")
    print()

for i in range(n-1, -1, -1):
    print(f"{" "* (n - (i+1))}", end="")
    for j in range(n-(i+1), n):
        print(j+1, end="")

    for j in range(n, n-i-1, -1):
        print(j, end="")
    print()

#
# for i in range(n):
#     print(f"{" "* (n - (i+1))}", end="")
#     for j in range(n-(i+1), n):
#         print(j+1, end="")
#         test.append(str(j+1))
#     test.reverse()
#     print("".join(test), end="")
#     test = []
#     print()

#
# for i in range(n):
#     print(f"{" "* (n - (i+1))}", end="")
#     for j in range(n-(i+1), n):
#         print(j+1, end="")
#         test.append(str(j+1))
#     test.reverse()
#     print("".join(test), end="")
#     test = []
#  

# n = 5
# for i in range(1, n + 1): # Looping 5x karena dimulai dari 1 dan 5 + 1 = 6
#     print(" " * (n-i), end="") # 5 - 1 = 4, 5 - 2 = 3, 5 - 3 = 2, 5 - 4 = 1
#
#     for j in range(n-i+1, n + 1): 
#         # range(5-1+1=5, 5+1=6)
#         # range(5-2+1=4, 5+1=6)
#         # range(5-3+1=3, 5+1=6)
#         # range(5-4+1=2, 5+1=6)
#         # range(5-5+1=1, 5+1=6)
#         print(j, end="")
#
#     for j in range(n, n-i, -1):
#         # range(5, 5-1=4, -1)
#         # range(5, 5-2=3, -1)
#         # range(5, 5-3=2, -1)
#         # range(5, 5-4=1, -1)
#         # range(5, 5-5=0, -1)
#         print(j, end="")
#
#     print()
#
# for i in range(n, 0, -1): # 5, 4, 3, 2, 1
#     print(" " * (n-i), end="")
#
#     for j in range(n-i+1, n + 1): 
#         print(j, end="")
#
#     for j in range(n, n-i, -1):
#         print(j, end="")
#
#     print()
