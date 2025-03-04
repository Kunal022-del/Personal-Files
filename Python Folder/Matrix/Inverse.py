import numpy as np


def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return "Matrix is singular and cannot be inverted."


# Example usage
matrix = np.array([[1, 0], [0, 1]])
inv_matrix = inverse_matrix(matrix)
print("Inverse of the matrix:")
for row in inv_matrix:
    print(row)
