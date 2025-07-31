def main():
    '''Your main code goes here'''
    while True:
        greeting = input("Greeting: ").strip().lower()
        print(cash(greeting))

def cash(greeting):
    '''The criteria for receiving 100 $ goes here'''
    if greeting == "hello":
        output = "$0"
    elif greeting[0] == "h":
        output = "$20"
    else:
        output = "$100"

    return output


if __name__ == "__main__":
    main()