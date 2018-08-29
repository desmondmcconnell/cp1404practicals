name = input("Please Enter Your Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


in_file = open("name.txt", "r")
your_name = in_file.readline()
print("Your name is {}".format(your_name))
in_file.close()


numbers = []
number_file = open("numbers.txt", "r")
for line in number_file:
    line = line.strip()
    numbers.append(int(line))

print("The numbers are {}".format(numbers))
total = sum(numbers)
print("The total is {}".format(total))
