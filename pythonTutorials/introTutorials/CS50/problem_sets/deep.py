def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    respond(question)

def respond(question):
    if question == "42" or question == "forty two" or question == "forty-two":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()