person1 = {"first_name": "putri", "last_name": "ayu", "age": 18, "city": "bandung"}
person2 = {"first_name": "revan", "last_name": "askar", "age": 21, "city": "tangerang"}
person3 = {"first_name": "razan", "last_name": "dhika", "age": 16, "city": "Surabaya"}

people = [person1, person2, person3]

for person in people:
    print(f"\nNama: {person['first_name']} {person['last_name']}")
    print(f"Usia: {person['age']}")
    print(f"Kota: {person['city']}")