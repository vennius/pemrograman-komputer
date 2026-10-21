'''
Algoritma:
    1. Mulai
    2. Input jari jari (dalam cm)
    3. Input tinggi (dalam cm)
    4. Hitung volume kerucut
    5. Tampilkan volume kerucut (dalam cm^3)
    6. Selesai
'''

print("="*10 + "VOLUME KERUCUT" + "="*10)
jari_jari = int(input("Masukkan jari-jari kerucut (cm): "))
tinggi = int(input("Masukkan tinggi kerucut (cm): "))

volume = 1/3 * 3.14 * jari_jari**2  * tinggi

print("Volume Kerucut adalah: ", volume, "cm^3")
