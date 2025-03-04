class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def herons_triangle(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


a = float(input("Enter the 1st side of the triangle: "))
b = float(input("Enter the 2nd side of the triangle: "))
c = float(input("Enter the 3rd side of the triangle: "))
if a + b > c and a + c > b and b + c > a:
    triangle = Triangle(a, b, c).herons_triangle()
    print(f"The area of the triangle is: {triangle:.2f}")
else:
    print("The given sides do not form a valid triangle.")
