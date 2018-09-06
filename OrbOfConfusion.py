from math import pi
try:
    radius = float(input("Enter the radius of the circle: "))
    volume = (4 / 3) * pi * (radius ** 3)
    print("It's actually a... SPHERE. With a volume of " + str(round(volume, 2)))
except ValueError:
    print("IT'S AN IMPOSSIBLE OBJECT. THAT'S AN IMPOSSIBLE OBJECT. (a.k.a. doesn't work here)")