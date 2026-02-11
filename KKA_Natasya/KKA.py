nama = input("Masukkan nama pembeli: ")
total_belanja = float(input("Masukkan total belanja: "))
status_member = input("Apakah pembeli member? (ya/tidak): ").lower()

if status_member == "ya":
    total_bayar = total_belanja * 0.5
else:
    total_bayar = total_belanja

print("Nama Pembeli:", nama)
print("Total yang harus dibayar: Rp", total_bayar)
