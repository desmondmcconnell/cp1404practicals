from prac_08.unreliable_car import UnreliableCar

old_ford = UnreliableCar("XE Falcon", 100, 35)

distance_driven = old_ford.drive(45)
print("The distance driven was {}\n".format(distance_driven))

print(old_ford)
