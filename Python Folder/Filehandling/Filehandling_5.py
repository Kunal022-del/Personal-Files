import pickle


class PickleFiles:
    def __init__(self, file):
        self.file = file

    def read_write(self):
        lists = [
            ["Name", "Age", "Country"],
            ["Raj", 23, "India"],
            ["Rahul", 24, "USA"],
            ["Kunal", 12, "Male"],
            ["Shyam", 12, "Male"],
            ["Samay", 12, "Male"],
            ["Jiya", 23, "Female"],
            ["Bebika", 28, "Female"],
        ]
        with open(self.file, "wb") as f:
            pickle.dump(lists, f)
        with open(self.file, "rb") as f:
            for row in pickle.load(f):
                print(row)


file = input("Enter Filename :")
PickleFiles(file).read_write()
