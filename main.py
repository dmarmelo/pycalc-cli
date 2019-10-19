import re


def main():
    regex = re.compile("^\\s*(\\d+\\s*[\\+\\-\\*\\/]\\s*)*\\d+\\s*$")
    while True:
        user_input = input("Enter your expression > ")
        if user_input == "quit":
            break
        elif regex.match(user_input):
            # TODO division by 0
            print(user_input.lstrip().rstrip() + " = " + str(eval(user_input)))
        else:
            print("Invalid Expression!")


if __name__ == '__main__':
    main()
