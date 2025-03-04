import Matrix as ms

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
obj = ms.Matrix(m, n).matrix()
for row in obj:print(row)
ms.Matrix(m, n).diagonal(obj)
# ms.Matrix(m, n).sum_diagonal(obj)
ms.Matrix(m, n).non_diagonal(obj)
