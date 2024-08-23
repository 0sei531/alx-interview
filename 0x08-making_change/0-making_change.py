#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given
total using a combination of greedy and dynamic programming approaches.
"""


def makeChange(coins, total):
    
    """
    Determines the fewest number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Greedy approach for large values
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total == 0:
        return count
    
    # Dynamic programming for smaller remaining values
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                break  # No need to check larger coins

    if dp[total] == float('inf'):
        return -1

    return count + dp[total]
