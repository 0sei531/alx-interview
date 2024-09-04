# 0x0A. Prime Game

## Description

This project involves implementing an algorithm in Python to simulate a competitive game between two players, Maria and Ben. Given a set of consecutive integers starting from 1 to `n`, Maria and Ben take turns picking a prime number from the set and removing that prime number along with its multiples. The player who cannot make a move loses the game. The goal of the project is to determine the winner after multiple rounds.

## Requirements

- **Editors allowed**: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.4.3**
- All Python files should start with exactly `#!/usr/bin/python3`
- All files must be executable
- Your code should use the PEP 8 style (version 1.7.x)
- A `README.md` file is mandatory at the root of the project
- You cannot import any external Python packages

## Game Rules

- The game is played for `x` rounds.
- In each round, a number `n` is chosen, and Maria and Ben play optimally, starting with Maria.
- Players take turns selecting prime numbers from the set of integers `[1, n]`.
- Once a prime number is chosen, it and all its multiples are removed from the set.
- The player who cannot make a move loses the round.
- The objective is to determine who wins the most rounds and declare them the overall winner.

## Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner after x rounds of the game.

    Parameters:
    x (int): The number of rounds.
    nums (List[int]): An array of n, representing the upper bounds for each round.

    Returns:
    str: The name of the player who won the most rounds, or None if no winner can be determined.
    """
