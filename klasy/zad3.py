class ElectricCar:
    def __init__(self, range):
        self.range = range
        self.distance=0

    def charge(self, units):

        self.range += units
        if self.

    def drive(self, distance):
        distance+=
        if self.range < 0:
            self.range += distance
            print("Low battery")


car = ElectricCar(100)
car.drive(70)
print(car.range)
car.charge(50)
print(car.range)
car.drive(100)