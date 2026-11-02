favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'budi', 'phil', 'citra']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} telah berpartisipasi dalam survei!")
    else:
        print(f"Halo {person.title()}, silakan ikuti survei kami!")