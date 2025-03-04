class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def get_info(self):
        print(f"My name is {self.name} and the product name is {self.product}")


class Employee:
    company = "Google"
    language = "Twitter"

    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"{self.name} is an Employee from the company {self.company}")

    def get_language(self):
        print(f"The language {self.name} knows is {self.language}\n")


class ProgrammerEmployee(Employee):
    company = "YouTube"
    language = "Java"


# Using the Programmer class
emp = Programmer("Harry", "Skye")
emp.get_info()
print(f"The company I am currently working on is {Programmer.company}")

# Using the Employee and ProgrammerEmployee classes
e = Employee("Harry")
e.show_details()
e.get_language()

p = ProgrammerEmployee("Sreejita")
p.show_details()
p.get_language()
print(f"The company I am currently working on is {ProgrammerEmployee.company}")
