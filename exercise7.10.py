responses = {}
polling_active = True

while polling_active:
    name = input("\nSiapa nama kamu? ")
    place = input("Jika kamu bisa mengunjungi satu tempat di dunia, ke mana kamu ingin pergi? ")
    
    responses[name] = place
    
    repeat = input("Apakah ada orang lain yang ingin menjawab? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Hasil Survei ---")
for name, place in responses.items():
    print(f"{name} ingin mengunjungi {place}.")