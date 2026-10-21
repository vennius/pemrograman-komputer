from prettytable import PrettyTable
# print("Masukkan Data Kamu")
# nama = input("Masukkan nama kamu: ")
# nim = input("Masukkan NIM kamu: ")
# dosen_wali = input("Masukkan dosen wali kamu: ")
#
# print("\n")
#
# hari = input("Masukkan Hari: ")
# kode = input("Masukkan Kode: ")
# nama_matkul = input("Masukkan Nama Mata Kuliah: ")
# kelas = input("Masukkan Kelas: ")
# ruangan = input("Masukkan Ruangan: ")
# pukul = input("Masukkan Pukul Berapa: ")
# sks = input("Masukkan jumlah SKS: ")
#
nama = "Stevennius Chandra"
nim = "221111436"
dosen_wali = "Sunario Megawan"

hari = "Senin"
kode = "IF.20309"
nama_matkul = "Pemrograman Komputer"
kelas = "IFB Sore"
ruangan = "T4.L4"
pukul = "20:00"
sks = "4"

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

table = PrettyTable()

print(f"Nama\t\t: {nama}\t\tProgram Studi\t: {prodi}")
print(f"NIM\t\t: {nim}\t\t\tAngkatan\t: 20{kode_angkatan}")
print(f"Dosen Wali\t: {dosen_wali}\t\tSemester\t: {semester}\n")

table.field_names = ["Hari", "Kode", "Nama Mata Kuliah", "Kelas", "Ruangan", "Pukul", "SKS"]
table.add_row([hari, kode, nama_matkul, kelas, ruangan, pukul, sks])
table.add_row([hari, kode, nama_matkul, kelas, ruangan, pukul, sks])
print(table)

# print("-"*100)
# print("Hari\tKode\t\tNama Mata Kuliah\t\tKelas\t\tRuangan\t\tPukul\t\tSKS")
# print("-"*100)
# print(f"{hari}\t{kode}\t{nama_matkul}\t\t{kelas}\t{ruangan}\t\t{pukul}\t\t{sks}")
