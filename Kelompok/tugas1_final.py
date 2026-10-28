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
print("[2] Catatan Pengembalian")
print("[3] Cek Ketersediaan Buku")
print("[4] Hitung Denda")
print("[5] Rekap Peminjaman")
print("[6] Tutup Program")

print()

choice = int(input("Pilih menu (1-6) > "))

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
        while True:
            book_exist = False
            for buku in books:
                if judul_buku.lower() == buku[0].lower():
                    book_exist = True
                    break
            if book_exist: break
            print("Judul tidak ditemukan")
            judul_buku = input("Masukkan judul buku\t: ")

        tgl_pinjam = input("Tanggal peminjaman\t: ")
        tgl_kembalian = input("Tanggal pengembalian\t: ")
        print()
        
        print("-"*50)
        print("\t\tBUKU BERHASIL DIPINJAM")
        print("-"*50)
    elif choice == 2:
        if len(nama) > 0:
            catatan="Buku Dikembalikan Dengan Kondisi Bagus"
            print()
            print("-" * 50)
            print("\t\tCATATAN PENGEMBALIAN")
            print("-" * 50)
            print("Nama\t\t:", nama)
            print("NIM\t\t:", nim)
            print("Judul buku\t:", judul_buku.title())
            print("Tanggal pinjam\t:", tgl_pinjam) 
            print("Tanggal kembali\t:", tgl_kembalian)
            print("Catatan\t\t:", catatan)
            print("-" * 50)
        else:
            print("Belum ada data peminjaman.")
    elif choice == 3:
        print("-" * 50)
        print("\t\tCEK KETERSEDIAAN BUKU")
        print("-" * 50)
        judul_buku = input("Masukkan judul buku yang ingin cari: ")
        ditemukan = False
        for buku in books:
            if judul_buku.lower() == buku[0].lower():
                print("\nBuku telah ditemukan!")
                print("Judul     :", buku[0])
                print("Penulis   :", buku[1])
                print("Kategori  :", buku[2])
                ditemukan = True
                break
        if ditemukan == False:
            print("Maaf, buku ini tidak tersedia")
        print("-" * 50)
    elif choice == 4:
        print("-" * 50)
        print("\t\tHITUNG DENDA")
        print("-" * 50)
        ht = int(input("Berapa hari anda terlambat membayar denda: "))
        dph = 10000
        if ht > 0:
            denda = ht * dph
            print("Hari terlambat:", ht)
            print("Total denda: Rp.", denda)
        else:
            print("Anda tidak terlambat")
            print("Total denda Rp 0")
        print("-" * 50)
    elif choice == 5:
        if len(nama) <= 0:
            print("Belum ada data peminjaman.")
        else:
            print("-" * 50)
            print("\t\tREKAP PEMINJAMAN")
            print("-" * 50)
            print("Nama\t\t\t: ", nama)
            print("NIM\t\t\t: ", nim)
            print("Judul Buku\t\t: ", judul_buku)
            print("Tanggal Pinjam\t\t: ", tgl_pinjam)
            print("Tanggal Pengembalian\t: ", tgl_kembalian)
            print("-" * 50)
    print()
    choice = int(input("Pilih menu (1-6) > "))
