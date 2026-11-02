def make_sandwich(*items):
    print("\nMembuat sandwich dengan topping berikut:")
    for item in items:
        print(f"- {item}")

make_sandwich("keju", "daging")
make_sandwich("telur", "tomat", "selada")