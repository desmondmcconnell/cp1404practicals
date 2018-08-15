"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 10 / 100
    else:
        bonus = sales * 15 / 100

    print('\nThe sales are ${:.2f} and the bonus is ${:.2f}\n'.format(sales, bonus))
    print('Please enter a new sales amount')
    sales = float(input("Enter sales: $"))

print('\nNegative sales are invalid')
