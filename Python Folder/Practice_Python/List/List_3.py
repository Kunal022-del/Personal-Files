class IntersectionSuM:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def intersection(self):
        total_Sum_Matrix = 0
        for value in self.list1:
            if value in self.list2:
                total_Sum_Matrix += value
        return total_Sum_Matrix


list1 = [40, 90, 11, 58, 31, 66, 28, 54, 79]
list2 = [58, 90, 54, 31, 45, 11, 66, 28, 26]
common_Sum_Matrix = IntersectionSuM(list1, list2).intersection()
print("Sum of common values:", common_Sum_Matrix)
