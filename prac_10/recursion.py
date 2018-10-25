"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))
print()

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
    else:
        return
    do_something(n - 1)


# TODO: 3. write down what you think the output of do_something(4) will be,
# TODO: 4. use the debugger to step through and see what's actually happening


do_something(4)
print()
# TODO: 5. fix do_something() so that it works according to the docstring


def do_something_else(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        do_something_else(n - 1)

    else:
        return
    print(n ** 2)


do_something_else(4)


number = int(input("Please enter a number:"))


def create_pyramid_scheme(n):
    if n < 2:
        return 1
    return n + create_pyramid_scheme(n-1)


print("{} blocks required to build {} layer pyramid".format(create_pyramid_scheme(number), number))
