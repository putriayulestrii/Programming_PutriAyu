import json
from pathlib import Path

path = Path('favorite_number.json')

if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"Saya tahu angka favoritmu! Angkanya adalah {number}.")
else:
    number = input("Berapa angka favoritmu? ")
    path.write_text(json.dumps(number))
    print("Angka favoritmu berhasil disimpan!")