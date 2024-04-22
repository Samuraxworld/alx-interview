#!/usr/bin/python3
"""implementation  function in Python to rotate the given 2D matrix\
    90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """This implementation first transposes the matrix and then\
        reverses each row to achieve the rotation effect.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)1
