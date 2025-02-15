def main():
    num = int(input("What's x? "))
    
    if is_even(num):
        print("even")
    else:
        print("odd")


def is_even(x):
    return x % 2 == 0



main()