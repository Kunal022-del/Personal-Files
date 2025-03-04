class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def matrix(self):
        o = []
        for i in range(self.m):
            data = []
            for j in range(self.n):
                content = int(input(f"Enter element [{i+1}][{j+1}] :"))
                data.append(content)
            o.append(data)
        return o
    # //dont copy this code
    def diagonal(self, matrix):
        if self.m == self.n:
            print("Diagonal elements:")
            for i in range(min(self.m, self.n)):
                print(f"A[{i+1}][{i+1}] :{matrix[i][i]}", end="\n")

    def sum_diagonal(self, matrix):
        if self.m == self.n:
            sum_diag = 0
            for i in range(min(self.m, self.n)):
                sum_diag += matrix[i][i]
            print(f"Sum of diagonal elements: {sum_diag}")

    def non_diagonal(self, matrix):
        if self.m == self.n:
            rows = len(matrix)
            cols = len(matrix[0]) if rows > 0 else 0
            print("Non-diagonal elements:")
            for i in range(rows):
                for j in range(cols):
                    if i != j:
                        print(f"A[{i+1}][{j+1}] :{matrix[i][j]}", end=" ")
                print()
        else:
            print("Diagonal elements are not possible for this matrix.")

    def multiply(self, matrix1, matrix2):
        print("Multiplication of two matrices is :")
        if len(matrix1[0]) != len(matrix2):
            return "Matrix multiplication is not possible."

        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result

    def Sum_Matrix(self, matrix1, matrix2):
        result = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        return result


class IdentityMatrix:
    def __init__(self, m):
        self.m = m

    def is_identity_matrix(self):
        A = Matrix(self.m, self.m).matrix()
        check = 1
        for i in range(self.m):
            for j in range(self.m):
                if i == j:
                    if A[i][j] != 1:
                        check = 0
                        break
                else:
                    if A[i][j] != 0:
                        check = 0
                        break
            if check == 0:
                break
        if check == 1:
            print("It is a Identity matrix.")
        else:
            print("It is not an identity matrix.")
        for A in A:
            print(A)

    def identity(self):
        A = []
        for i in range(self.m):
            data = []
            for j in range(self.m):
                data.append(1 if i == j else 0)
            A.append(data)
        print("Identity matrix:")
        for i in A:
            print(i)


class Transpose:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0]) if rows > 0 else 0
        B = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                B[j][i] = self.matrix[i][j]
        return B


class Subtraction:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def subtraction(self):
        B = [[0 for _ in range(len(self.matrix1[0]))] for _ in range(len(self.matrix1))]
        for i in range(len(self.matrix1)):
            for j in range(len(self.matrix1[0])):
                B[i][j] = self.matrix1[i][j] - self.matrix2[i][j]
        return B


class Addition:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def addition(self):
        B = [[0 for _ in range(len(self.matrix1[0]))] for _ in range(len(self.matrix1))]
        for i in range(len(self.matrix1)):
            for j in range(len(self.matrix1[0])):
                B[i][j] = self.matrix1[i][j] + self.matrix2[i][j]
        return B


class Scalar_Multiplication:
    def __init__(self, matrix, scalar):
        self.matrix = matrix
        self.scalar = scalar

    def scalar_multiplication(self):
        B = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                B[i][j] = self.matrix[i][j] * self.scalar
        return B


class Adjoint:
    def __init__(self, matrix):
        self.matrix = matrix

    def adjoint(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0]) if rows > 0 else 0
        B = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                B[j][i] = self.matrix[i][j]
        return B
