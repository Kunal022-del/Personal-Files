class Number:
    def __init__(self, value):
        self.value = value

    def factorial(self):
        if self.value < 0:
            return "Factorial is not defined for negative numbers."
        elif self.value == 0 or self.value == 1:
            return 1
        else:
            return self.value * Number(self.value - 1).factorial()


n = int(input("Enter number :"))
print(f"Factorial of {n} :", Number(n).factorial())
