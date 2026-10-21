baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

print("MULTIPLICATION TABLE: ")

for i in range(baris):
    for j in range(kolom):
        print((i+1) * (j+1), end="\t")
    print()
    print("-"*80)
