import regex
from math import sqrt, sin, cos, tan, log, pi, e


def main():
    pattern = regex.compile(r"^\s*(?<rec>((?<exp>(?<num>-?\d+(\.\d+)?)|(\(\s*((?&num)|(?&rec))\s*\))|((sqrt|sin|cos|tan)\s*\(\s*((?&num)|(?&rec))\s*\))|((log)\s*\(\s*((?&num)|(?&rec))\s*,\s*((?&num)|(?&rec))\s*\))|(pi|e))\s*[+\-*\/\^]\s*)*(?&exp)\s*)$")
    print("Type 'help' for help and 'quit' to exit.")
    print("Enter your expression:")
    while True:
        raw_user_input = input(">> ").strip().lower()
        if raw_user_input == "quit":
            break
        elif raw_user_input == "help":
            calc_help()
        elif pattern.match(raw_user_input):
            try:
                expression = raw_user_input.replace("^", "**")
                user_input = regex.sub(r"\s+", " ", raw_user_input)
                print(user_input + " = " + str(eval(expression)))
            except ZeroDivisionError:
                print("ERROR Division by zero!")
            except:
                print("Arnaldo's fault!")
        else:
            print("Invalid Expression!")


def calc_help():
    print("Available operations:")
    print("+ -> Sum")
    print("- -> Subtraction")
    print("* -> Multiplication")
    print("/ -> Division")
    print("^ -> Exponentiation")
    print("sqrt(n) -> Square root of n")
    print("sin(n) -> Sine")
    print("cos(n) -> Cosine")
    print("tan(n) -> Tangent")
    print("log(n, b) -> Logarithm of n to base b")
    print("pi -> Constant Pi")
    print("e -> Constant e")
    print("Example: '(1 + 2) * 3^4 + sqrt(3 * 2) + cos(pi) / log(10, e)'")


if __name__ == '__main__':
    main()
