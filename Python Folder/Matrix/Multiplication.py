import Matrix as ms

m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))
obj = ms.Matrix(m, n)
print("Matrix 1:")
matrix1 = obj.matrix()
print("Matrix 2:")
matrix2 = obj.matrix()
result = obj.multiply(matrix1, matrix2)
for row in result:
    print(row)

# Output:
# Enter the number of rows:2
# Enter the number of columns:2
# Matrix 1:
# Enter element [1][1] :1
# Enter element [1][2] :2
# Enter element [2][1] :3
# Enter element [2][2] :4
# Matrix 2:
# Enter element [1][1] :5
# Enter element [1][2] :6
# Enter element [2][1] :7
# Enter element [2][2] :8
# Multiplication of two matrices is :
# [19, 22]
# [43, 50]
