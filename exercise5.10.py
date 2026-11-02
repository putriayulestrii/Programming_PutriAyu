current_users = ["john", "salsa", "sarah", "mike", "alice"]
new_users = ["frank", "brian", "daniel", "david", "kevin"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Nama '{new_user}' sudah digunakan, silakan masukkan nama lain.")
    else:
        print(f"Nama '{new_user}' masih tersedia.")