#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for number in row:
            squared_number = number * number
            squared_row.append(squared_number)

        squared_matrix.append(squared_row)

    return (squared_matrix)
