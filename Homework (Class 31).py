class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "350 km/h"
    
def details(car):
    print("Fuel Type :", car.fuel_type())
    print("Max Speed :", car.max_speed())

bmw = BMW()
ferrari = Ferrari()

print("BMW Car Details:")
details(bmw)

print("\nFerrari Car Details:")
details(ferrari)