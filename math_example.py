import math


class results:
    def __init__(self, wynik1, wynik2):
        self.wynik1 = wynik1
        self.wynik2 = wynik2


def main():
    results = Results(x1, x2)


def oblicz_rownanie(a: float, b: float, c: float):
    delta = (b ** 2) - (4 * a * c)

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return Results(x1, x2)

    elif delta == 0:
        x = -b / (2 * a)
        return Results(x, x)

    else:
        return None


print("Równianie: a*x**2 + bx + c = 0")

a = float(input("podaj wartość parametru a: "))
b = float(input("podaj wartość parametru b: "))
c = float(input("podaj wartość parametru c: "))

result = oblicz_rownanie(a, b, c)

if result is None:
    print("Brak pierwiastków")
else:
    print(f"x1={result.wynik1}")
    print(f"x2={result.wynik2}")
