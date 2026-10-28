# FizzBUzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue

    print(i)

# Parkir
jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil): ")
jam = int(input("Berapa jam: "))
tarif_motor = 2000
tarif_mobil = 5000
tarif = 0

if jenis_kendaraan.lower() == "motor":
    tarif = tarif_motor
else:
    tarif = tarif_mobil

for i in range(1, jam+1):
    print(f"Jam ke {i}: {tarif}")
print(f"Total = {jam*tarif}")

# Vokal
kalimat = input("Masukkan kalimat: ")
vocals = ["a", "e", "i", "o", "u"]
jumlah_vocal = 0

for huruf in kalimat:
    for vocal in vocals:
        if huruf.lower() == vocal.lower():
            jumlah_vocal += 1

print("Total huruf vokal: ", jumlah_vocal)
