pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]
friend_pizzas = pizzas[:]

pizzas.append("Supreme")
friend_pizzas.append("Hawaiian")

print("My favorite pizzas are:")
for p in pizzas:
    print(f"- {p}")

print("\nMy friend's favorite pizzas are:")
for p in friend_pizzas:
    print(f"- {p}")