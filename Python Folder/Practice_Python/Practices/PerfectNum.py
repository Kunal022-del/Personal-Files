class PerfectNumber:
    def __init__(self, n):
        self.n = n

    def checkperfect(self):
        Sum_Matrixs = 0
        for i in range(1, self.n):
            div = self.n % i
            if div == 0:
                Sum_Matrixs += i
        if Sum_Matrixs == self.n:
            print("It is a perfect number")
        else:
            print("It is not a perfect number")


class Ranges(PerfectNumber):
    def __init__(self, n, n2):
        super().__init__(n)
        self.n2 = n2

    def perfect(self):
        for num in range(self.n, self.n2 + 1):
            Sum_Matrixs = 0
            for i in range(1, num):
                if num % i == 0:
                    Sum_Matrixs += i
            if Sum_Matrixs == num:
                print(f"{num}")


Num1 = int(input("Enter starting number :"))
Num2 = int(input("Enter Ending Number :"))
PerfectNumber(Num1).checkperfect()
Ranges(Num1, Num2).perfect()
