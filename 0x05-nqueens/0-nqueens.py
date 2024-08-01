#!/usr/bin/python3
"""
N Queens problem: Place N non-attacking queens on an N×N chessboard.
Usage: nqueens N
"""
import sys

def print_board(board):
    """
    Prints the board in the required format.
    Args:
        board (list): 2D list representing the board.
    """
    solution = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 1:
                solution.append([i, j])
    print(solution)

def is_safe(board, row, col, size):
    """
    Checks if placing a queen at (row, col) is safe.
    Args:
        board (list): 2D list representing the board.
        row (int): Row index.
        col (int): Column index.
        size (int): Size of the board.
    Returns:
        bool: True if safe, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, size):
    """
    Utilizes backtracking to solve the N Queens problem.
    Args:
        board (list): 2D list representing the board.
        col (int): Current column index.
        size (int): Size of the board.
    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col == size:
        print_board(board)
        return True

    res = False
    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, size) or res
            board[i][col] = 0  # BACKTRACK

    return res

def validate_and_solve():
    """
    Validates input arguments and solves the N Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(size)] for _ in range(size)]
    solve_nqueens(board, 0, size)

if __name__ == "__main__":
    validate_and_solve()

