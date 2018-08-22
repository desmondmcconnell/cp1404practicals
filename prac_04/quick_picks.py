import random
error_flag = 0

while error_flag == 0:
    try:
        number_of_picks = int(input("How many quick picks? "))
        error_flag = 1
    except ValueError:
        print("Please enter a number")

for number in range(number_of_picks):
    count = 0
    quick_list = []
    while count < 6:
        pick = random.randint(1, 45)
        while pick in quick_list:
            pick = random.randint(1, 45)
        quick_list.append(pick)
        count += 1
    print(quick_list)
