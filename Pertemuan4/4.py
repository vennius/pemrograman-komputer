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
