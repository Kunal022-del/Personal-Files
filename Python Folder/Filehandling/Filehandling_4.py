import csv


class Writing:
    def __init__(self, filename):
        self.filename = filename

    def WritingCsv(self):
        csv_row = [
            ["Name", "Age", "Gender"],
            ["Kunal", 12, "Male"],
            ["Shyam", 12, "Male"],
            ["Samay", 12, "Male"],
            ["Rahul", 14, "Male"],
            ["Jiya", 23, "Female"],
            ["Bebika", 28, "Female"],
        ]
        with open(self.filename, "w") as f:
            csv.writer(f).writerows(csv_row)
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)


file = input("Enter Filepath:")
Writing(file).WritingCsv()
