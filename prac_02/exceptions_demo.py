"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("This is an invalid denominator, please enter any number that is not 0")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#     ValueError occurs when the input is not a number
except ZeroDivisionError:
    print("Cannot divide by zero!")
#     ZeroDivisionError occurs when the denominator input is 0
print("Finished.")

#  The code could be modified with an "if" statement to not accept non-numeric inputs or denominators of 0
