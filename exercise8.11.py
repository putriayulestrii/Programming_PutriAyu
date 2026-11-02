def send_messages(messages_list, sent_list):
    while messages_list:
        current_msg = messages_list.pop(0)
        print(f"Mengirim pesan: {current_msg}")
        sent_list.append(current_msg)

messages = ["Hi!", "how your day?", "bye!"]
sent_messages = []

send_messages(messages[:], sent_messages)

print("\nDaftar pesan asli (tetap utuh):", messages)
print("Daftar pesan terkirim:", sent_messages)