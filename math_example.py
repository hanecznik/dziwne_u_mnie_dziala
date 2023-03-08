import math

print("Równianie: a*x**2 + bx + c = 0")

a = float(input("podaj wartość parametru a: "))
b = float(input("podaj wartość parametru b: "))
c = float(input("podaj wartość parametru c: "))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print('x1 = ', x1)
    print('x2 = ', x2)
elif delta == 0:
    x = -b / (2 * a)
    print('x0 = ', x)
else:
    print("nie liczymy miejsc zerowych")
