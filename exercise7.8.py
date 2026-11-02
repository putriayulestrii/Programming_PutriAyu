sandwich_orders = ['tuna', 'turkey', 'egg salad', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya telah membuatkan {current_sandwich} sandwich Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang selesai dibuat:")
for s in finished_sandwiches:
    print(f"- {s}")