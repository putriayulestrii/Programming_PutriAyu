guests = ["Revan Askar", "Razandhika", "Sahana"]
print("\nKabar gembira! Meja makan yang lebih besar telah ditemukan.")

guests.insert(0, "salsa")
guests.insert(2, "nabila")
guests.append("ipul")

for guest in guests:
   print(f"hi {guest}, Anda diundang untuk makan malam bersama.")