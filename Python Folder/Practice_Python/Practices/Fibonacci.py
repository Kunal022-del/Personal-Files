class Fibonnaci:
    def __init__(self, n):
        self.n = n

    def fibonacci(self):
        blop1, blop2 = 0, 1
        for _ in range(self.n):
            print(blop1)
            blop1, blop2 = blop2, blop1 + blop2


class FibonacciValues(Fibonnaci):
    def showfibonacci(self):
        blop = self.n + 1
        print("Fibonacci series")
        for _ in range(self.n):
            print(self.n)
            self.n, blop = blop, self.n + blop


n = int(input("Enter the number of terms: "))
choice = int(
    input(
        """Enter your choice(1/2):
        \n1. Print the fibonacci series\n
        2. Print the fibonacci values\n
"""
    )
)
if choice == 1:
    fib = Fibonnaci(n)
    fib.fibonacci()
elif choice == 2:
    fib = FibonacciValues(n)
    fib.showfibonacci()
