"""Language: Python 2.7.18"""

"""Calculates the cost for how many days the car has been rented. Also includes a dishonest depending on how many days the car has been rented."""
def rent_cost(days):
  cost = days * 100
  if days >= 7:
    cost -= 400
  elif days >= 3:
    cost -= 200
  return cost

"""Determines how much money will be spent initially depending on the type of car rented."""
def car_type_cost(car):
  if car == "Mazda3":
    return 1800
  elif car == "Kia Forte":
    return 1700
  elif car == "Toyota Yaris Hatchback":
    return 1600
  elif car == "Mitsubishi Mirage":
    return 1300

"""Adds up all of the costs to make the total amount."""
def trip_cost(car, days):
  return rent_cost(days) + car_type_cost(car)

"""Prints the total amount."""
print trip_cost("Kia Forte", 5)


