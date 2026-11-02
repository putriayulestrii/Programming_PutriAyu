active = True
while active:
    topping = input("Masukkan topping (ketik 'quit' untuk keluar): ")
    if topping == 'quit':
        active = False
    else:
        print(f"Menambahkan {topping}.")