import re


def main():
    regex = re.compile("^\\s*(\\d+\\s*[\\+\\-\\*\\/]\\s*)*\\d+\\s*$")
    while True:
        user_input = input("Enter your expression > ")
        if user_input == "quit":
            break
        elif regex.match(user_input):
            # TODO decimal numbers
            try:
                print(user_input.lstrip().rstrip() + " = " + str(eval(user_input)))
            except ZeroDivisionError:
                print("ERROR Division by zero!")

        else:
            print("Invalid Expression!")


if __name__ == '__main__':
    main()
