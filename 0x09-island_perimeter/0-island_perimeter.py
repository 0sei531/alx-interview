#!/usr/bin/python3
"""Optimized function to find perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
    grid (list of list of int): 2D grid where 0 represents
    water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid
    cols = len(grid[0]) if rows else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 1 for each neighboring land cell (up, down, left, right)
                if row > 0 and grid[row - 1][col] == 1:  # Up
                    perimeter -= 2  # Subtract 2 as both cells share a side
                if col > 0 and grid[row][col - 1] == 1:  # Left
                    perimeter -= 2  # Subtract 2 as both cells share a side

    return perimeter
