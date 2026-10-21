nama = "Stevennius Chandra"
nim = "221111436"
dosen_wali = "Sunario Megawan"

kode_prodi = nim[2:5]
kode_angkatan = nim[0:2]

tahun_angkatan = int(f"20{kode_angkatan}")
tahun_ajaran = "2023/2024"

prodi = ""
semester = 2 * (int(tahun_ajaran[0:4]) - tahun_angkatan) + 1

if kode_prodi == "111":
    prodi = "Teknik Informatika"
elif kode_prodi == "112":
    prodi = "Sistem Informasi"
elif kode_prodi == "113":
    prodi = "Tekknologi Informasi"
else:
    prodi = "n/a"

print("Kartu Rencana Studi".capitalize())
print("fakultas informatika".capitalize())
print("universitas mikroskil\n".capitalize())


print(f"Nama\t\t: {nama}\t\tProgram Studi\t: {prodi}")
print(f"NIM\t\t: {nim}\t\t\tAngkatan\t: 20{kode_angkatan}")
print(f"Dosen Wali\t: {dosen_wali}\t\tSemester\t: {semester}\n")

print("-"*75)
print("Hari\tKode\tNama Mata Kuliah\t\tKelas\tRuangan\tPukul\tSKS")
print("-"*75)
