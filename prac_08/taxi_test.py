from prac_08.taxi import Taxi


# prius_taxi = Taxi("Prius1", 100, 1.23)
prius_taxi = Taxi("Prius1", 100)

prius_taxi.drive(40)
print(prius_taxi)
print("Current fare: ${:.2f}\n".format(prius_taxi.get_fare()))

prius_taxi.start_fare()
prius_taxi.drive(100)
print(prius_taxi)
print("Current fare: ${:.2f}\n".format(prius_taxi.get_fare()))
