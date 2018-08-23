import random

NUMBER_OF_NUMBERS_IN_PICK = 5
MINIMUM = 1
MAXIMUM = 45

is_error_found = True


while is_error_found:
    try:
        number_of_picks = int(input("How many quick picks? "))
        is_error_found = False
    except ValueError:
        print("Please enter a number")

for number in range(number_of_picks):
    count = 0
    quick_list = []
    for i in range(NUMBER_OF_NUMBERS_IN_PICK):
        pick = random.randint(MINIMUM, MAXIMUM)
        while pick in quick_list:
            pick = random.randint(MINIMUM, MAXIMUM)
        quick_list.append(pick)

    quick_list.sort()
    print("{:2} {:2} {:2} {:2} {:2}".format(quick_list[0], quick_list[1], quick_list[2], quick_list[3], quick_list[4],))
