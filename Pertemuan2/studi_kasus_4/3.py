'''
Algoritma:
    1. Mulai
    2. Input budget awal
    3. Input berat belanjaan
    4. Hitung total harga
    5. Hitung harga diskon
    6. Kurangi budget dengan hasil kurang dari total harga dan harga didskon
    7. Cetak sisa uang
    8. Selesai
'''

budget = int(input("Masukkan total budget: "))
weight = int(input("Masukkan berat(kg): "))
price_per_kg = 50_000
total_price = weight * price_per_kg
discount = 2_000 * weight
budget_left = budget - (total_price - discount)

print("Sisa Uang: ", budget_left)
