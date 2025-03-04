n = int(input("Enter size of stack: "))
stack = []


def push():
    if len(stack) < n:
        book = input("Enter the name of the book to add: ")
        stack.append(book)
        print(f"Adding book to stack: {stack}")
    else:
        print("Stack is full")


def pop():
    if len(stack) != 0:
        removed_book = stack.pop()
        print(f"Removing book from stack: {removed_book}")
        print(f"Current stack: {stack}")
    else:
        print("Stack is empty")


def display():
    if len(stack) != 0:
        print("Books in stack:")
        for book in stack:
            print(book)
    else:
        print("Stack is empty")


dict1 = {1: push, 2: pop, 3: display}
flag = 1

while flag == 1:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    choice = int(input("Enter your choice: "))
    if choice in dict1:
        dict1[choice]()
    else:
        print("Invalid choice")
    flag = int(input("Do you want to continue (1/0): "))
else:
    print("Exiting the program")
