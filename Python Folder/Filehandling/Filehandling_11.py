class Primenum:
    def __init__(self, file):
        self.file = file

    def isprime(self, n):
        if n < 2:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    def primeinterval(self, num1, num2):
        prime = []
        for i in range(num1, num2):
            if self.isprime(i):
                prime.append(i)
        return prime

    def writing(self):
        with open(self.file, "a+") as f:
            prime = self.primeinterval(2, 100)
            for i in prime:
                f.write(str(i) + "\n")


file = input("Enter Filepath :")
Primenum(file).writing()
