print("="*30)
print("Peminjaman Buku Perpustakaan")
print("="*30)

print()

books = [
    # Judul , Penulis, Kategori
    ["Laskar Pelangi", "Andrea Hirata", "Fiksi"],
    ["Bumi Manusia", "Pramoedya Ananta Toer", "Sastra"],
    ["Pemrograman Python", "Wahana Komputer", "Teknologi"],
    ["Matematika Dasar", "H. Sugiarto", "Pendidikan"],
    ["Kisah 25 Nabi dan Rasul", "Ibnu Katsir", "Agama"],
    ["Logika Informatika", "Rinaldi Munir", "Teknologi"]
]

print("[1] Catat Peminjaman")
print("[2] Catat Pengembalian")
print("[3] Cek Ketersediaan Buku")
print("[4] Hitung Denda")
print("[5] Rekap Peminjaman")
print("[6] Tutup Program")

print()

choice = int(input("Pilih menu (1-6) > "))
# choice = 0

nama = ""
nim = ""
judul_buku = ""
tgl_pinjam = ""
tgl_kembalian = ""

while choice != 6:
    
    print()
    if choice == 1:
        print("-"*50)
        print("\t\tCATAT PEMINJAMAN")
        print("-"*50)
        nama = input("Masukkan nama\t\t: ")
        nim = input("Masukkan NIM\t\t: ")
        judul_buku = input("Masukkan judul buku\t: ")
        tgl_pinjam = input("Tanggal peminjaman\t: ")
        tgl_kembalian = input("Tanggal pengembalian\t: ")
        print()
        
        print("-"*55)
        print("\t\tBUKU BERHASIL DIPINJAM")
        print("-"*55)
    elif choice == 2:
        if len(nama) > 0:
            catatan="Buku Dikembalikan Dengan Bagus"
            print()
            print("-" * 50)
            print("\t\tCATATAN PENGEMBALIAN")
            print("-" * 50)
            print("Nama\t\t:", nama)
            print("NIM\t\t:", nim)
            print("Judul buku\t:", judul_buku)
            print("Tanggal pinjam\t:", tgl_pinjam) 
            print("Tanggal kembali\t:", tgl_kembalian)
            print("Catatan\t\t:", catatan)
            print("-" * 50)
        else:
            print("Data peminjamam belum dimasukkan.")

    print()
    choice = int(input("Pilih menu (1-6) > "))

