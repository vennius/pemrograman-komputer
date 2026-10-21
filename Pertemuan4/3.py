username = input("Masukkan username kamu: ")
usia = int(input("Masukkan usia kamu: "))

if username != "admin" and usia >= 17:
    print("Pendaftaran diterima")
else:
    print("Pendaftaran ditolak")
