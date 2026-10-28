'''

print("="*30)
print("Peminjaman Buku Perpustakaan")
print("="*30)

print("[1] Catat Peminjaman")
print("[2] Catat Pengembalian")
print("[3] Cek Ketersediaan Buku")
print("[4] Hitung Denda")
print("[5] Rekap Peminjaman")
print("[6] Tutup Program")

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

choice = int(input("Pilih menu (1-6) > "))

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


    print()
    choice = int(input("Pilih menu (1-6) > "))

# while choice != 6:
#     if choice == 1:
#         nama = input("Masukkan nama peminjam\t\t\t: ")
#         tgl_pinjam = input("Masukkan tanggal pinjam (dd/mm/yyyy)\t: ")
#         tgl_pinjam = tgl_pinjam.split("/")
#         judul = ""
#
#         again = True
#         books_cart = []
#
#         while again:
#             is_book_exist = False
#
#             while not is_book_exist:
#                 judul = input("Masukkan judul buku\t\t\t: ")
#                 for book in books:
#                     if judul.lower() == book[0].lower():
#                         is_book_exist = True
#                 # print("-"*60)
#                 if not is_book_exist:
#                     print("Judul buku tidak ditemukan!\n")
#
#
#             date_pinjam = dt.datetime(int(tgl_pinjam[2]), int(tgl_pinjam[1]), int(tgl_pinjam[0]))
#             date_denda = date_pinjam + dt.timedelta(days=7)
#             books_cart.append([nama, judul, date_pinjam, date_denda])
#             again = True if input("Apakah ingin menambahkan buku lagi? (y/t) ").lower() == "y" else False
#             print()
#
#         invoice_table = PrettyTable()
#         invoice_table.field_names = ["No","Judul Buku", "Tanggal Pengembalian"]
#
#         # for book in books_cart:
#         for i in range(len(books_cart)):
#             data_peminjaman.append(books_cart[i])
#             invoice_table.add_row([str(i+1), books_cart[i][1].title(), f"{books_cart[i][3].day}/{books_cart[i][3].month}/{books_cart[i][3].year}"])
#
#         print("\n\nPerpustakaan")
#         print("Sistem Peminjaman Buku")
#         print("-"*70)
#         print("\t\t\tBukti Peminjaman")
#         print("-"*70)
#         print(f"Nama Peminjam\t\t:{nama}")
#         print(f"Tanggal Peminjaman\t: {'/'.join(tgl_pinjam)}")
#         print()
#         print(invoice_table)
#         print()
#         print("Terima kasih telah meminjam buku di perpustakaan.")
#         print("Jaga dan kembalikan tepat waktu.")
#         # print("-"*70)
#
#     print()
#     choice = int(input("> "))

# print(data_peminjaman)
'''

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

