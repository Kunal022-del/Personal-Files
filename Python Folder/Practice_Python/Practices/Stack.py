class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if len(self.stack) != 0:
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty! Cannot pop.")

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Current stack:", self.stack)


if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")  # Added an option to exit
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            item = input("Enter item to push: ")
            stack.push(item)  # Use the created stack object
        elif choice == "2":
            stack.pop()  # Use the created stack object
        elif choice == "3":
            stack.display()  # Use the created stack object
        elif choice == "4":
            print("Exiting the program.")
            break  # Break the loop to exit the program
        else:
            print("Invalid choice.")
