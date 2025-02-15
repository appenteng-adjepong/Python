def emoji_typer(message):
    words = message.split(" ")
    emojis = {
":(": "😞",
":)": "😊",
";)": "😉"
    }
    output = ""
    for word in words:
        output += f"{emojis.get(word, word)} "

    return output

message = input("> ")
print(emoji_typer(message))