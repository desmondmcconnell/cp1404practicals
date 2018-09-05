from prac_06.guitar import Guitar

TITLE = "My guitars!"


def main():
    print(TITLE)
    guitars = []
    guitars = new_guitar(guitars)
    print_guitars(guitars)


def new_guitar(guitars):
    finished = False
    while not finished:
        name = input("Name: ")
        if name == "":
            finished = True
        else:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def print_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = (" (vintage)" if guitar.is_vintage( ) else "")
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()
