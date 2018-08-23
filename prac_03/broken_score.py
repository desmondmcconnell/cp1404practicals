"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))

    result = determine_results(score)
    print(result)


def determine_results(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"

    return result


main()
