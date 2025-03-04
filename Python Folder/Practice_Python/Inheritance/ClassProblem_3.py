class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person")

    def takeBreak(self):
        print("I am breathing")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee")

    def getSalary(self, salary):
        print(f"Salary is {salary}")

    def takeBreak(self):
        super().takeBreak()
        print("I am an Employee, so I am breathing")


class Programmer(Employee):
    company = "Fibre"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer")

    def getSalary(self):
        print("No salary for programmer")

    def takeBreak(self):
        super().takeBreak()
        print("I am a programmer, I am breathing")


p = Person()
e = Employee()
pr = Programmer()

p.takeBreak()
e.takeBreak()
pr.takeBreak()

e.getSalary(1010)
print(e.company)
print(pr.company)
