favorite_places = {
    "rev": ["Bali", "Yogyakarta"],
    "rzn": ["Tokyo", "Seoul", "Paris"],
    "ayu": ["Bandung"]
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name}:")
    for place in places:
        print(f"- {place}")