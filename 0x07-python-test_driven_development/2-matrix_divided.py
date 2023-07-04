#!/usr/bin/python3
"""
Division
"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.

    Args:
        matrix (list): The matrix to divide.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                    or if div is not a number.
        TypeError: If each row of the matrix doesn't have the same size.
        ZeroDivisionError: If div is equal to 0.

    Example:
        matrix = [[1, 2, 3], [4, 5, 6]]
        div = 2
        result = matrix_divided(matrix, div)
        print(result)
        # Output: [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
