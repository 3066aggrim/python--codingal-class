class vehicle:

    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage


class Bus(vehicle):
    pass


school_bus = Bus("school volvo", 180, 12)
print("vehicle name:", school_bus.name, "speed:",
      school_bus.maxspeed, "mileage", school_bus.mileage)
