import time


class Employee:
    company1 = "Google"

    def __init__(self, salary):
        self.salary = salary

    @staticmethod
    def greet():
        print("Good morning Sir!")

    @classmethod
    def get(cls1):
        return cls1.company1

    def getSalary(self, signature):
        print(f"Salary is ${self.salary}.")
        print(f"Thanks! {signature}")

    def company(self):
        print(f"The company which you are working is {self.company1}")

    def time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Current date and time is {current_time}")

    def improvement(self):
        print(f"Salary improvement is ${self.salary + 23300}")


Employee.get()
Emp = Employee(1000)
Emp.greet()
Emp.company()
Emp.time()
Emp.getSalary("Thanks!")
Emp.improvement()
