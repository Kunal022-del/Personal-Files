class PrimeChecker:
    def __init__(self):
        pass

    def is_check(self, n):
        if n < 2:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    def prime_interval(self, num1, num2):
        primes = []
        for i in range(num1, num2):
            if self.is_check(i):
                primes.append(i)
        return primes
prime_checker = PrimeChecker()
print(prime_checker.prime_interval(10, 50))
