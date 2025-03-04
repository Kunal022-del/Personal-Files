class Multiples:
    def __init__(self, n):
        self.n = n

    def multiplies(self):
        for i in range(1, self.n + 1):
            with open(f"Table_{i}.txt", "w+") as f:
                f.write(f"Multiplication Table {i}\n")
                for j in range(1, 11):
                    f.write(f"{i} x {j} = {i*j}\n")


Nums = int(input("Enter Number :"))
Multiples(Nums).multiplies()
