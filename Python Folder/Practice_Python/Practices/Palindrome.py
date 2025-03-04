class FindPalindrome:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_palindrome(self, number):
        s = str(number)
        return s == s[::-1]

    def check_single_number(self, number):
        if self.is_palindrome(number):
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome number.")

    def list_palindromes_in_range(self):
        print(f"Palindrome numbers between {self.start} and {self.end}:")
        for i in range(self.start, self.end + 1):
            if self.is_palindrome(i):
                print(i)


def main():
    a = int(input("Enter starting number: "))
    b = int(input("Enter ending number: "))
    finder = FindPalindrome(a, b)

    print("Choose an option:")
    print("1: Check if the starting number is a palindrome.")
    print("2: List all palindrome numbers in the given range.")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        finder.check_single_number(a)
    elif choice == "2":
        finder.list_palindromes_in_range()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
