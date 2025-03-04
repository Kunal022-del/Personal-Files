class Armstrong:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def armstrong(self):
        if self.start < 0 or self.end < 0:
            print("Invalid input")
        else:
            print("\n--Armstrong Values:--")
            for i in range(self.start, self.end + 1):
                s = i
                Sum_Matrix = 0
                order = len(str(i))
                while i > 0:
                    digit = i % 10
                    Sum_Matrix += digit**order
                    i //= 10
                if s == Sum_Matrix:
                    print(s)


class ArmstrongValue(Armstrong):
    def is_armstrong(self):
        original = self.start
        Sum_Matrix = 0
        order = len(str(original))
        while original > 0:
            digit = original % 10
            Sum_Matrix += digit**order
            original //= 10
        if self.start == Sum_Matrix:
            print("It is an Armstrong Number")
        else:
            print("It is not an Armstrong Number")


def main():
    choice = int(
        input(
            """Enter your choice (1/2):\n1. Armstrong Values\n2. Check Armstrong Value\n"""
        )
    )
    if choice == 1:
        a = int(input("Enter starting Value: "))
        b = int(input("Enter ending Value: "))
        armstrong_instance = Armstrong(a, b)
        armstrong_instance.armstrong()
    elif choice == 2:
        a = int(input("Enter a number: "))
        armstrong_value_instance = ArmstrongValue(a, a)
        armstrong_value_instance.is_armstrong()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()
