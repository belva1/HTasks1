# https://www.youtube.com/watch?v=wRLW-gjbQzk
# Code for quadratic equations

import math
# Float converts values into floating point numbers
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# math.pow analogue of exponentiation
delta = math.pow(b, 2) - (4 * a * c)
# condition
if delta > 0:
# math.sqrt analogue of root extraction
    x1 = (((-b) + math.sqrt(delta)) / (2 * a))
    x2 = (((-b) - math.sqrt(delta)) / (2 * a))
    print("There are 2 roots:%f and %f" % (x1, x2))
elif delta == 0:
    x = (-b) / 2 * a
    print("There is one root:", x)
else:
    print("No roots, delta<0")

