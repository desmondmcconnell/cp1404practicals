"""Desmond McConnell"""


def main():

    min_length = 6

    password = get_password(min_length)

    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password(min_length):
    password = input("Please enter a password: ")
    while len(password) < min_length:
        print("Please enter at least 6 characters")
        password = input("Please enter a password: ")
    return password


main()
