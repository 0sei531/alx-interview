#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given
total using dynamic programming.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Parameters:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount of change to make.

    Returns:
        int: The fewest number of coins needed to make the change,
              or -1 if the total change cannot be made with the given coins.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Initialize the DP array with infinity, except dp[0] which should be 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
