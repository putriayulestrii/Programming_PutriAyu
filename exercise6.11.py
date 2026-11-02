cities = {
    "Tokyo": {
        "country": "Jepang",
        "population": "14 juta",
        "fact": "Kota terpopuler di dunia."
    },
    "Paris": {
        "country": "Prancis",
        "population": "2.1 juta",
        "fact": "Dikenal sebagai Kota Cahaya."
    }
}

for city, info in cities.items():
    print(f"\nKota: {city}")
    print(f"  Negara: {info['country']}")
    print(f"  Populasi: {info['population']}")
    print(f"  Fakta: {info['fact']}")