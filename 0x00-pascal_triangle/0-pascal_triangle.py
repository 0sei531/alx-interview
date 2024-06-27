#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle

    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate

    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        return []

    triangle = [[1]]

    for row_index in range(1, n):
        row = [1]
        row.extend(
            [
                triangle[row_index - 1][i - 1] + triangle[row_index - 1][i]
                for i in range(1, row_index)
            ]
        )
        row.append(1)
        triangle.append(row)

    return triangle
