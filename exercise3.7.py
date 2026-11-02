guests = ["salsa", "Revan Askar", "nabila", "Razandhika", "Sahana", "ipul"]
print("\nMohon maaf, meja baru tidak datang tepat waktu. Hanya 2 tamu yang dapat diundang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Mohon maaf {removed_guest}, kami tidak dapat mengundang kamu ke makan malam.")

for guest in guests:
    print(f"Hi {guest}, kamu masih terdaftar dalam undangan makan malam.")

del guests[0]
del guests[0]

print("Daftar tamu akhir :", guests)