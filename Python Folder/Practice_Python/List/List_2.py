# Function to find the intersection of two lists using for loops
class Intersection:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def intersection_list(self):
        intersection = []
        for value in list1:
            if value in list2:
                intersection.append(value)
        return intersection


list1 = [45, 90, 11, 58, 31]
list2 = [58, 90, 54, 31, 45]
print("Intersection from the list is ", Intersection(list1, list2).intersection_list())
