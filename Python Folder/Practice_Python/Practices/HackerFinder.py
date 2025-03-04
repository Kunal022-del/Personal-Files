class User:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills

class HackerFinder:
    def __init__(self, users):
        self.users = users

    def find_hackers(self):
        hackers = [user for user in self.users if 'hacking' in user.skills]
        return hackers

# List of users
users = [
    User("Raj", 23, ["python", "hacking", "networking"]),
    User("Rahul", 24, ["java", "web development"]),
    User("Ravi", 25, ["hacking", "security"]),
    User("Dhoni", 26, ["data analysis"]),
    User("Sachin", 27, ["hacking", "machine learning"]),
]

finder = HackerFinder(users)
hackers = finder.find_hackers()

print("Hackers found:")
for hacker in hackers:
    print(f"Name: {hacker.name}, Age: {hacker.age}, Skills: {', '.join(hacker.skills)}")