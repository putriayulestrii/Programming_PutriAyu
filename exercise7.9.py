sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'turkey', 'pastrami', 'cheese']
finished_sandwiches = []

print("Maaf, kedai kami kehabisan pastrami hari ini.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang berhasil dibuat:", finished_sandwiches)