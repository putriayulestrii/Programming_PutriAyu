prompt = "\nMasukkan topping pizza yang diinginkan (ketik 'quit' untuk selesai): "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"Menambahkan topping {topping} ke pizza kamu!")