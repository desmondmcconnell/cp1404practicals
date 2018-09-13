from prac_06.guitar import Guitar

TITLE = "My guitars!"


def main():
    print(TITLE)
    guitars = create_guitar_list()
    print_guitars(guitars)


def create_guitar_list():
    guitars = []
    finished = False
    while not finished:
        guitar = new_guitar()
        if guitar.name == "":
            finished = True
        guitars.append(guitar)
    return guitars


def new_guitar():
    name = input("Name: ")
    if name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
    else:
        guitar = Guitar(name)
    return guitar


def print_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        if guitar.name == "":
            break
        vintage_string = (" (vintage)" if guitar.is_vintage() else "")
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()
