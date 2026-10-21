# 1
# tahun = int(input("Masukkan tahun: "))
#
# if tahun % 4 == 0:
#     if tahun % 100 == 0:
#         if tahun % 400 == 0:
#             print(f"{tahun} adalah tahun kabisat.")
#         else:
#             print(f"{tahun} bukan tahun kabisat.")
#     else:
#         print(f"{tahun} adalah tahun kabisat.")
# else:
#     print(f"{tahun} bukan tahun kabisat.")


# 2
# berat_badan = int(input("Masukkan berat badan kamu(kg): "))
# tinggi_badan = int(input("Masukkan tinggi badan kamu(cm): "))
# tinggi_badan = tinggi_badan / 100
# bmi = berat_badan / tinggi_badan ** 2
#
# if bmi < 18.5:
#     print("kamu kekurangan berat badan.")
# elif bmi >= 18.5 and bmi <= 24.9:
#     print("Berat badan kamu normal / ideal.")
# elif bmi >= 25 and bmi <= 29.9:
#     print("Kamu kelebihan berat badan.")
# else:
#     print("Kamu obesitas.")


# 3
sisi1 = int(input("Sisi-1: "))
sisi2 = int(input("Sisi-2: "))
sisi3 = int(input("Sisi-3: "))

if sisi1 == sisi2:
    if sisi2 == sisi3:
        print("Segitiga sama sisi")
    else:
        print("Segitiga sama kaki")
elif sisi1 == sisi2 or sisi2 == sisi3 or sisi3 == sisi1:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")
