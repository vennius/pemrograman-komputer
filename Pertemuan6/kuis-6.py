jantan = 78
betina = 178

print("Masukkan data jual beli bulan ke-1 :")
persen_beli = float(input("Beli Betina Berapa % dari kambing jantan? "))
bagian_jual = float(input("Jual Berapa bagian dari kambing jantan? "))

beli_betina = jantan * persen_beli / 100
jual_betina = jantan * bagian_jual
betina = betina + beli_betina - jual_betina

print("\nMasukkan data jual beli bulan ke-2 :")
persen_jantan = float(input("Beli Jantan berapa % dari kambing betina? "))
jual_betina = float(input("Berapa jumlah betina yang akan dijual? "))

beli_jantan = betina * persen_jantan / 100
jantan = jantan + beli_jantan
betina = betina - jual_betina

print("\nMasukkan data jual beli bulan ke-3 :")
kali_lipat = float(input("Beli Betina Berapa kali lipat dari kambing jantan? "))
persen_retur = float(input("Retur berapa %? "))

beli_betina = jantan * kali_lipat
retur = beli_betina * persen_retur / 100
betina = betina + beli_betina - retur

print("-" * 45)
print("Total kambing jantan pak Aryo saat ini adalah :", int(jantan))
print("Total kambing betina pak Aryo saat ini adalah :", int(betina))
