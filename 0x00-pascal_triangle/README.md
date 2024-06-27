# Pascal's Triangle

This repository contains a Python implementation of a function that generates Pascal's Triangle up to a specified number of rows.

## Description

Pascal's Triangle is a triangular array of the binomial coefficients. Each number is the sum of the two directly above it. This implementation provides a function that returns a list of lists of integers representing Pascal's Triangle of a given number of rows.

## Function

The main function in this repository is `pascal_triangle(n)`. It takes an integer `n` and returns a list of lists of integers, where each list represents a row in Pascal's Triangle.

### Usage

The function is defined as follows:

```python
def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle

    parameters:
        n [int]: the number of rows of Pascal's triangle to recreate

    return:
        [list of lists of ints]: representation of Pascal's triangle
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    
    if n <= 0:
        return []

    triangle = [[1]]
    
    for row_index in range(1, n):
        row = [1]
        row.extend([triangle[row_index - 1][i - 1] + triangle[row_index - 1][i] for i in range(1, row_index)])
        row.append(1)
        triangle.append(row)

    return triangle
