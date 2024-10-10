x = input("What would you like your first number to be: ")
y = input("What would you like your second number to be: ")
print("X is less than Y ", int(x) < int(y))
print("X is more than Y ", int(x) > int(y))
print("X is less or equal to Y ", int(x) <= int(y))
print("X is more or equal to Y ", int(x) >= int(y))
print("X is equal to Y ", int(x) == int(y))
print("X is not equal to Y ", int(x) != int(y))
has_driving_license = True
car_age = int(x) > 18 and has_driving_license
print("Can they drive a car? ", car_age)

can_drink_alcohol = False
legal_age = int(y) > 18 or can_drink_alcohol
print("Is legal age ", legal_age)

is_an_adult = True
adult = int(x) > 20 or is_an_adult
print("Is adult ", adult)