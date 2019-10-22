import regex
from math import sqrt, sin, cos, tan, log


def main():
    pattern = regex.compile(r"^\s*((?<exp>(?<dig>\d+(\.\d+)?)|((sqrt|sin|cos|tan)\s*\(\s*((?&dig)|(?&exp))\s*\))|((log)\s*\(\s*(?&dig)\s*,\s*(?&dig)\s*\)))\s*[+\-*\/\^]\s*)*(?&exp)\s*$")
    while True:
        raw_user_input = input("Enter your expression > ").strip()
        if raw_user_input == "quit":
            break
        elif pattern.match(raw_user_input):
            try:
                expression = raw_user_input.replace("^", "**")
                user_input = regex.sub(r"\s+", " ", raw_user_input)
                print(user_input + " = " + str(eval(expression)))
            except ZeroDivisionError:
                print("ERROR Division by zero!")

        else:
            print("Invalid Expression!")


if __name__ == '__main__':
    main()
