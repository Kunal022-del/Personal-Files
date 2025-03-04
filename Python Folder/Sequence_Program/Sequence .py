### 1.
# 1
# 11
# 111
# 1111
# 11111
# for i in range(5 ):
#      for j in range(0,i+1):
#          print("1",end="")
#      print()
"----------------------"
###2.
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(0,5):
#      for j in range(i+1):
#          print("*",end=" ")
#      print()
"----------------------"
###3.
# ****
# ***
# **
# *
# for k in range(4,0,-1):
#     for l in range(k,0,-1):
#         print("*",end="")
#     print()
"----------------------"
###4.
# l = list(input("Enter List Values:"))
# num = input("Enter the number: ")
# Sum_Matrixs=0
# for x in l:
#     if num==x:
#         Sum_Matrixs+=1
# print(f"The number of occurrences of {num} is {Sum_Matrixs}")
"----------------------"
###5.
# 1
# 12
# 123
# 1234
# 12345
# for j in range(0,5):
#     for i in range(0,j+1):
#         print(i+1,end="")
#     print()
"----------------------"
###6.
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()
"----------------------"
###7.
# 1
# 23
# 345
# 4567
# num=int(input("enter the number"))
# for i in range(0,num):
#     for j in range(0,i):
#         print(i,end="")
#         i=i+1
#     print()
"----------------------"
###8.
# 1
# 22
# 333
# 4444
# 55555
# num=int(input("enter the number"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
"----------------------"
###9.
# 55555
# 4444
# 333
# 22
# 1
# num=int(input("enter number to series"))
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#         print(i,end="")
#     print()
"----------------------"
###10.
# 54321
# 4321
# 321
# 21
# 1
# num=int(input("enter number to series"))
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#          print(j,end="")
#          i=i-1
#     print()
"----------------------"
###11.
# ********
# *      *
# *      *
# *      *
# *      *
# *      *
# *      *
# ********
# row=8
# col=8
# for i in range(row):
#     if i==0 or i==row-1:
#         print("*"*col)
#     else:
#         print("*"+" "*(col-2)+"*")
"----------------------"
###12.
# *             *
# * *           *
# *   *         *
# *     *       *
# *       *     *
# *         *   *
# *           * *
# *             *
# num=8
# for i in range(num):
#     for j in range(num):
#         if j==0 or j==num-1 or i==j:
#              print("*",end=" ")
#         else:
#              print(" ",end=" ")
#     print()
"----------------------"
###13.
# # ****
# # ***
# # **
# # *
# for j in range(4,0,-1):
#     for i in range(0,j):
#         print("*",end="")
#     print()
"----------------------"
###14.
# #    *
# #   ***
# #  *****
# # *******
# def hollow_pyramid(n):
#     for i in range(1, n + 1):
#         for j in range(1, 2 * n):
#             if j <= n - i or j >= n + i:
#                 print(" ", end="")
#             else:
#                 print("*", end="")
#         print()
# f=hollow_pyramid(4)
# print(f)
"----------------------"
###15.
#       *
#      **
#     ***
#    ****
#   *****
#  ******
# def print_hollow_inverted_half_pyramid(rows):
#     for i in range(0, rows, 1):
#         for j in range(rows - i):
#             print(" ", end="")
#         for j in range(i):
#             if j == 0 or j == i - 1 or i == rows:
#                 print("*", end="")
#             else:
#                 print("*", end="")
#         print()
# num_rows = 7
# print_hollow_inverted_half_pyramid(num_rows)
"----------------------"
###16.
# # 1
# # 2 1
# # 3 2 1
# # 4 3 2 1
# # 5 4 3 2 1
# for r in range (6):
#     for c in range(r,0,-1):
#         print(c, end=' ')
#     print()
"----------------------"
###17.
# # Sum_Matrix=n+nn+nnn+nnnn....
# def calculate_Sum_Matrix(n, m):
#     total_Sum_Matrix = 0
#     current_term = 0
#     for _ in range(1, m + 1):
#         current_term = current_term * 10 + n
#         total_Sum_Matrix += current_term
#     return total_Sum_Matrix
# n = int(input("Enter the value of n: "))  # Input for n
# m = int(input("Enter the number of terms: "))  # Input for number of terms
# result = calculate_Sum_Matrix(n, m)
# print("Sum:", result)
"----------------------"
###18.
# def print_ser(n):
#     total_Sum_Matrix=0
#     for j in range(1,n+1,2):
#         total_Sum_Matrix+=j**2
#     return f"SUM OF ODD NUMBER SQUARE IS {total_Sum_Matrix}"
# n=int(input("Enter Sum_Matrix of odd number square :"))
# print(print_ser(n))
# # 1(sqr)+3(sqr)+5(sqr)+...n(sqr)
"----------------------"
###19.
# def print_ser(n):
#     total_Sum_Matrix = 0
#     for j in range(2, n + 1,2):
#         total_Sum_Matrix += j ** 2
#     return f"The Sum_Matrix of squares of  even.no  till {n} is {total_Sum_Matrix}"
# n = int(input("Enter a number: "))
# print(print_ser(n))
# # 2(sqr)+4(sqr)+6(sqr)+...n(sqr)
"----------------------"
###20.
# def print_ser(num):
#     import math
#     Sum_Matrix = 0
#     for i in range(1, num+1):
#         fact=math.factorial(i)
#         Sum_Matrix = Sum_Matrix + (i/ fact)
#     return Sum_Matrix
# n=int(input("Enter value :"))
# f=print_ser(n)
# print(f)
##1/1!+2/2!+3/3!+..n/n!
"----------------------"
###21.
# def print_ser(n):
#     total_Sum_Matrix = 0
#     for j in range(1, n + 1):
#         total_Sum_Matrix += j ** 2
#     print(f"The Sum_Matrix of squares of numbers till {n} is {total_Sum_Matrix}")
# n = int(input("Enter a number: "))
# print_ser(n)
##1+4+9+16....n
"----------------------"
###22.
# def print_ser(num):
#     for i in range(num,0,-1):
#         for j in range(i):
#             print("*",end=" ")
#         print()
# print_ser(4)
# # * * * *
# # * * *
# # * *
# # *
"----------------------"
###23.
# def treegenerator(height):
#     for i in range(height):
#         print(" "*(height-i+1)+"*"*(2*i+1))
#     print(" "*int(height+1)+"*")
# height=int(input("Enter Height of Tree :"))
# treegenerator(height)
# #        *
# #       ***
# #      *****
# #     *******
# #    *********
# #   ***********
# #        *
"----------------------"
###24.
# def tree_generator(height):
#     num = 1
#     for i in range(height):
#         print(" " * (height - i - 1), end=" ")
#         for j in range(i + 1):
#             print(num, end="")
#             num += 1
#         print()
# height = int(input("Enter the height of the tree: "))
# tree_generator(height)
# #        1
# #       23
# #      456
# #     78910
# #    1112131415
# #   161718192021
# #  22232425262728
"----------------------"
