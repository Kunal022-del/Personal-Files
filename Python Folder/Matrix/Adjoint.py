import Matrix as ms

m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))
matrix1 = ms.Matrix(m, n).matrix()
print("Matrix is:")
for i in matrix1:
    print(i)
object = ms.Adjoint(matrix1).adjoint()
print("Adjoint of the matrix is:")
for i in object:
    print(i)
