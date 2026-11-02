pet1 = {"animal": "Anjing", "owner": "revan"}
pet2 = {"animal": "Kucing", "owner": "puyes"}
pet3 = {"animal": "Kelinci", "owner": "ayu"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Jenis Hewan: {pet['animal']}, Pemilik: {pet['owner']}")