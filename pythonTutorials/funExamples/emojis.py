def main():
    output = emojis(message)
    print(output)

def emojis(message):
    if ":)" in message:
        text = message.replace(":)", "😊")
    elif ":(" in message:
        text = message.replace(":(", "😞")
    return text

message = input(" ")

main()