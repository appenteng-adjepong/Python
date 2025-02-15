phone_number = input("Phone: ")

number_dictionary = {
"0": "zero",
"1": "one",
"2": "two",
"3": "three",
"4": "four",
"5": "five",
"6": "six",
"7": "seven",
"8": "eight",
"9": "nine"
}
output = " "
for number in phone_number:
   output += f"{number_dictionary.get(number, "!")} "
print(output)