# MAP
# l = [1, 2, 3, 4, 5,4]
# newl=list(map(lambda x:x**3,l))
# print(newl)
# ---------------------
# FILTER
# l = [1, 2, 3, 4, 5,4]
# newnewl=list(filter(lambda x:x>3,l))
# print(newnewl)
# ---------------------
# REDUCE
# from functools import reduce
# l = [1, 2, 3, 4, 5]
# sum=reduce(lambda x,y:x+y,l)
# print(sum)
# ---------------------
# Practice
# 1.
# class Apply:
#     def __init__(self, fx, values):
#         self.fx = fx
#         self.values = values

#     double = lambda x: x * 2
#     avg = lambda x, y: (x + y) / 2
#     cube = lambda x: x**3

#     def apply(self):
#         return 6 + self.fx(self.values)
# print(Apply.avg(5, 10))
# print(Apply.double(5))
# print(Apply.cube(5))
# print(Apply(Apply.double, 5).apply())

# 2.
# l= [1, 2, 3, 4, 5,10,15,20,0,20]
# print(list(filter(lambda x:x%5==0,l)))

# 3.
# sum=lambda a,b,c:a+b+c
# print(sum(1,2,3))

# 4.
# name=input("Enter your name :")
# marks=float(input("Enter your marks :"))
# phone_no=input('Enter Your phone number :')
# print('My name is {} and marks he scored {}\nPhone no :{}'.format(name,marks,phone_no))

# 5.
# table=[str(7*i) for i in range(1,11)]
# print('\n'.join(table))

# 6.
# div5=[1,2,3,4,5,20,98,95]
# newl=list(filter(lambda x:x%5==0,div5))
# print(newl)

# 7.
# num = [1, 2, 3, 4, 5, 10, 15, 20, 0, 20]
# max_number = reduce(lambda x, y: x if x > y else y, num)
# print("The maximum number is:", max_number)

# 8.
# num = [1, 2, 3, 4, 5, 10, 15, 20, 0, 20]
# for index,numbers in enumerate(num):
#     print(index)
#     print(numbers)


