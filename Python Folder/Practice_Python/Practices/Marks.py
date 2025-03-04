class Marksheet:
    def __init__(self, mark):
        self.mark = mark

    def marks(self):
        Sum_Matrix1 = 0
        for i in range(len(self.mark)):
            Sum_Matrix1 += self.mark[i]
        count = Sum_Matrix1 / (len(self.mark))
        print(f"Percentage of marks is {count}")


marks1 = list(map(int, input("Enter marks: ").split()))
Marksheet(marks1).marks()
