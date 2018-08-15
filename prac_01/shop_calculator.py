price_list = []
number_of_items = int(input('Please enter the number of items:'))

while number_of_items < 0:
    print('Please enter a valid number of items')
    number_of_items = int(input('Please enter the number of items:'))

for i in range(1, number_of_items + 1):
    current_price = float(input('Please enter the price of item {}: $'.format(i)))
    price_list.append(current_price)

total_price = sum(price_list)

if total_price > 100:
    total_price = total_price - (total_price * 10 / 100)

print('\nThe number of items is {}\n'.format(number_of_items))
print('The total price is: ${:.2f}'.format(total_price))
