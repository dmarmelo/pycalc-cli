def main():
    while True:
        user_input = input("Enter your expression > ")
        if user_input == "quit":
            break
        else:
            print(user_input + " = " + str(eval(user_input)))


if __name__ == '__main__':
    main()
