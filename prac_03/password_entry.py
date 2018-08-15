"""Desmond McConnell"""

MIN_LENGTH = 6

password = input("Please enter a password: ")

while len(password) < MIN_LENGTH:
    print("Please enter at least 6 characters")
    password = input("Please enter a password: ")

print("*" * len(password))
