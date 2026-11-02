messages = ["Hi!", "how your day?", "bye!"]
sent_messages = []

def send_messages(msgs, sent_list):
    while msgs:
        current_msg = msgs.pop(0)
        print(f"Sending: {current_msg}")
        sent_list.append(current_msg)

send_messages(messages, sent_messages)
print("Original list:", messages)
print("Sent list:", sent_messages)