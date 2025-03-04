import Matrix as ms

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
print("Matrix A :")
matrix1 = ms.Matrix(m, n).matrix()
print("Matrix B :")
matrix2 = ms.Matrix(m, n).matrix()
print("Addition of two matrices:")
Summatrix = ms.Matrix(m, n).Sum_Matrix(matrix1, matrix2)
for i in Summatrix:
    print(i)
