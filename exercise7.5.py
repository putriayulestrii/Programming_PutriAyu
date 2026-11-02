while True:
    age_input = input("\nMasukkan usia kamu (atau ketik 'quit' untuk keluar): ")
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"Harga tiket Anda adalah ${price}.")