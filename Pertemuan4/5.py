nilai_tugas = int(input("Masukkan nilai tugas: "))
nilai_uts = int(input("Masukkan nilai UTS: "))
nilai_uas = int(input("Masukkan nilai UAS: "))
rata_rata = (nilai_tugas + nilai_uts + nilai_uas) / 3
nilai_huruf = ""

if rata_rata >= 85:
    nilai_huruf = "Nilai kamu A"
elif rata_rata >= 70:
    nilai_huruf = "Nilai kamu B"
elif rata_rata >= 55:
    nilai_huruf = "Nilai kamu C"
elif rata_rata >= 40:
    nilai_huruf = "Nilai kamu D"
elif rata_rata >= 25:
    nilai_huruf = "Nilai kamu E"
else:
    nilai_huruf = "Nilai kamu F"

if rata_rata >= 55:
    print(f"Kamu lulus dengan nilai rata-rata {rata_rata:.2f}")
else:
    print(f"Kamu tidak lulus dengan nilai rata-rata {rata_rata:.2f}")
print(nilai_huruf)
