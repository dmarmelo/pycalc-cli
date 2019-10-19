import re


def main():
    regex = re.compile("^\\s*(\\d+(\\.\\d+)?\\s*[+\\-*/\\^]\\s*)*\\d+(\\.\\d+)?\\s*$")
    while True:
        user_input = input("Enter your expression > ").lstrip().rstrip()
        if user_input == "quit":
            break
        elif regex.match(user_input):
            try:
                expression = user_input.replace("^", "**")
                print(user_input + " = " + str(eval(expression)))
            except ZeroDivisionError:
                print("ERROR Division by zero!")

        else:
            print("Invalid Expression!")


if __name__ == '__main__':
    main()
