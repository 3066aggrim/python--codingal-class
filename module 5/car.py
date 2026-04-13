class BMW_M5:

    def mileage(self):
        print("it's mileage is 9 to 10")

    def top_speed(self):
        print("its top speed is 250 km/h")

    def seats(self):
        print("it has 5 seats")


class Lamborghini_Huracán:

    def mileage(self):
        print("it's mileage is 12 to 15 km")

    def top_speed(self):
        print("its top speed is 325 km/h")

    def seats(self):
        print("it has 2 seats ")


class Audi_R8:
    def mileage(self):
        print("it's mileage is 11 to 13")

    def top_speed(self):
        print("its top speed is 235km/h")

    def seats(self):
        print("it has 5 seats")


class mercedes_s7_series:
    def mileage(self):
        print("it's mileage is 11km")

    def top_speed(self):
        print("its top speed is 250km/h")

    def seats(self):
        print("it has 5 seats ")


obj_mercedes = mercedes_s7_series()
obj_Audi = Audi_R8()
obj_lambo = Lamborghini_Huracán()
obj_BMW = BMW_M5()

for car in (obj_mercedes, obj_Audi, obj_lambo, obj_BMW):
    car.mileage()
    car.top_speed()
    car.seats()
