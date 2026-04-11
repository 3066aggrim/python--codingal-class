class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage


class Bus(vehicle):

    def __init__(self, name, maxspeed, mileage, capacity):

        super().__init__(name, maxspeed, mileage)
        self.capacity = capacity

    def total_fare(self):
        fare_per_person = 100
        return self.capacity * fare_per_person


school_bus = Bus("School Volvo", 180, 12, 50)

print("Vehicle name:", school_bus.name)
print("Speed:", school_bus.maxspeed)
print("Mileage:", school_bus.mileage)
print("Capacity:", school_bus.capacity)
print("Total fare:", school_bus.total_fare())
