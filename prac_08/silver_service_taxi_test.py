from prac_08.silver_service_taxi import SilverServiceTaxi


humvee = SilverServiceTaxi("Hummer", 100, 2)

humvee.drive(18)

print(humvee)
print("The fare is ${:.2f}".format(humvee.get_fare()))
