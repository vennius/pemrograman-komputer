total_belanja = int(input("Masukkan total belanja\t:"))
jumlah_uang = int(input("Masukkan jumlah uang diberikan\t:"))
# total_belanja = 26500
# jumlah_uang = 100000

kembalian_dibayar = jumlah_uang - total_belanja
pecahan_kembalian = [50_000, 20_000, 10_000, 5_000, 2_000, 1_000, 500, 200, 100]

for kembalian in pecahan_kembalian:
    lembar = kembalian_dibayar // kembalian
    if(lembar >= 1): kembalian_dibayar -= kembalian * lembar
    print(f"{lembar} lembar pecahan uang Rp. {kembalian}")



# kembalian_20k = kembalian // 20_000
# if(kembalian_20k >= 1): kembalian -= 20_000 * kembalian_20k
#
# kembalian_10k = kembalian // 10_000
# if(kembalian_10k >= 1): kembalian -= 10_000 * kembalian_10k
#
# print(kembalian)
# print(kembalian_50k)
