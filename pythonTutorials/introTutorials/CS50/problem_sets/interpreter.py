def main():
    while True:
        prompt = input("Expression: ")
        print(solve(prompt))


def solve(expression):
    num1, operator, num2 = expression.split()
    num1, num2 = float(num1), float(num2)
    match operator:
        case "+":
            result =  num1 + num2
        case "-":
            result =  num1 - num2
        case "*":
            result =  num1 * num2
        case "/":
            result =  num1 / num2

    return round(result, 1)

if __name__ == "__main__":
    main()