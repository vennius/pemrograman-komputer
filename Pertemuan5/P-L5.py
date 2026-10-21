baris_kolom = int(input("Masukkan baris dan kolom: "))
for i in range(baris_kolom):
    print("*"*(i+1))

print()

for i in range(baris_kolom):
    print("*"*(baris_kolom-i))

print()

for i in range(baris_kolom):
    print(f"{" "*(baris_kolom-(i+1))}{"*"*(i+1)}")

print()

for i in range(baris_kolom):
    print(f"{" "*(baris_kolom-(i+1))}{"*"*(i+1)*2}")
