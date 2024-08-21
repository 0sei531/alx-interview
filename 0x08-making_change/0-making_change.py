#!/usr/bin/python3
"""
Task: Change comes from within
Given a pile of coins of different values,
determine the fewest number of coins needed to
meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of integers representing the coin denominations.
    total (int): The total amount of money to be made up with the coins.

    Returns:
    int: The fewest number of coins needed to meet the total. Returns
         - 0 if total is 0 or less,
         - -1 if total cannot be met by any number of coins available,
         - Otherwise, returns the minimum number of coins required.
    """
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the DP array
    newVal = total + 1
    store = [newVal] * (total + 1)
    store[0] = 0

    # Fill the DP array
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                store[i] = min(store[i], store[i - coin] + 1)

    # Return the result
    return store[total] if store[total] <= total else -1
