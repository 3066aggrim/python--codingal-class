def hotel_cost(nights):
    return 140*nights


def plane_ride_cost(city):
    if "kathmandu" == city:
        return 20000

    elif "pokhara" == city:
        return 30000

    if "chitwan" == city:
        return 10000


def rental_car_cost(days):
    if days >= 7:
        return 40 * days-50
    elif days >= 5:
        return 40 * days-20

    elif days >= 3:
        return 40*days


def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money


print("Cost of car rental: ", rental_car_cost(5))

print("Cost of plane ride: ", plane_ride_cost("pokhara"))

print("Cost of hotel room: ", hotel_cost(7))

print("Total cost of the trip:", trip_cost("chitwan", 10, 500))
