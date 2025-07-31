def word_scrambler(message):
    for word in message:
        if len(word) > 5:
            idx = message.index(word)
            message[idx] = word[::-1]

    output = " ".join(message)
    return output

message = input("").split()
scrambled = word_scrambler(message)
print(scrambled)

