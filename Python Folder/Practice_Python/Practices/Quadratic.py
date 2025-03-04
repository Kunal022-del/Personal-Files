import cmath
import math


def find_roots(a, b, c):
    D1 = cmath.sqrt(b**2 - 4 * a * c)
    D = b**2 - 4 * a * c
    if D == 0:
        x = -b / (2 * a)
        print("Roots are:", (x, x))
    elif D > 0:
        sqrt_D = math.sqrt(D)  # Calculate the square root of the discriminant
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        print("Roots are:", (x1, x2))
    else:
        real_part = -b / (2 * a)
        imaginary_part = D1 / (2 * a)
        print("Roots are:", real_part + imaginary_part, ",", real_part - imaginary_part)


a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
c = int(input("Enter value c: "))
find_roots(a, b, c)
