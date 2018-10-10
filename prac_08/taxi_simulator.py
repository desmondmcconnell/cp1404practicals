from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


MENU = "q)uit, c)hoose taxi, d)rive"
USER_PROMPT = ">>> "


def main():
    current_taxi = None
    bill = 0
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    menu_choice = input(USER_PROMPT).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            current_taxi = choose_taxi(taxis)
            print_bill(bill)
        elif menu_choice == "d":
            bill = drive_taxi(current_taxi, bill)
            print_bill(bill)
        else:
            print("Please enter a valid menu choice")
        print(MENU)
        menu_choice = input(USER_PROMPT).lower()
    print("Total trip cost: ${}".format(bill))
    print("Taxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    for i, taxi in enumerate(taxis, 0):
        print("{} - {}".format(i, taxi))


def choose_taxi(taxis):
    print_taxis(taxis)
    finished = False
    while not finished:
        try:
            taxi_choice = int(input("Choose taxi:"))
            current_taxi = taxis[taxi_choice]
            finished = True
        except ValueError:
            print("Invalid choice. Try again")
        except IndexError:
            print("Invalid choice. Try again")
    return current_taxi


def drive_taxi(current_taxi, bill):
    if current_taxi is None:
        print("No car chosen")
        bill = 0
    else:
        current_taxi.start_fare()
        finished = False
        while not finished:
            try:
                distance = int(input("Drive how far: "))
                finished = True
            except ValueError:
                print("Please input a valid number")
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
        bill += fare
    return bill


def print_bill(bill):
    print("Bill to date: ${:.2f}".format(bill))


if __name__ == '__main__':
    main()

