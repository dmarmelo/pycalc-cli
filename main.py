import regex
from math import sqrt, sin, cos, tan, log, pi, e


def main():
    pattern = regex.compile(r"^\s*(?<rec>((?<exp>(?<num>\d+(\.\d+)?)|((sqrt|sin|cos|tan)\s*\(\s*((?&num)|(?&rec))\s*\))|((log)\s*\(\s*((?&num)|(?&rec))\s*,\s*((?&num)|(?&rec))\s*\))|(pi|e))\s*[+\-*\/\^]\s*)*(?&exp)\s*)$")
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
