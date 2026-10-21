# 1
# n = int(input("Masukkan angka: "))
#
# for i in range(10):
#     print(f"{n} x {i+1} = {(i+1)*n}")

# 2
# angka_rahasia = 15
# tebakan = int(input("Masukkan Tebakan Kamu: "))
#
#
# while tebakan != angka_rahasia:
#     if angka_rahasia > tebakan:
#         print("Tebakan kamu kurang besar. Coba lagi.")
#     elif angka_rahasia < tebakan:
#         print("Tebakan kamu terlalu besar. Coba lagi.")
#     tebakan = int(input("Masukkan Tebakan Kamu: "))
#
# print("Selamat, Tebakan Benar!")

# 3
kata = input("Masukkan kata: ")
vokal = "AIUEO"

for i in range(len(kata)):
    for j in range(len(vokal)):
        if kata[i].upper() == vokal[j]:
            print(kata[i])
