numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]            ##Expected Output - 3
# numbers[-1]           ##Expected Output - 2
# numbers[3]            ##Expected Output - 1
# numbers[:-1]          ##Expected Output [3, 1, 4, 1, 5, 9]
# numbers[3:4]          ##Expected Output - [1]
# 5 in numbers          ##Expected Output - True
# 7 in numbers          ##Expected Output - False
# "3" in numbers        ##Expected Output - False
# numbers + [6, 5, 3]   ##Expected Output - [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(numbers)
numbers[0] = "ten"
print(numbers)
numbers[-1] = 1
print(numbers)
print(numbers[2:])
if 9 in numbers:
    print("True")
else:
    print("False")
