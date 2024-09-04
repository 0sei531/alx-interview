#!/usr/bin/python3

"""Prime Game Algorithm in Python."""


def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve


def isWinner(x, nums):
    """
    Determine who is the winner after x rounds of the game.
    Maria always goes first. Return the name of the player with the most wins.
    If the winner is undetermined, return None.
    """

    if not nums or x <= 0:
        return None

    max_num = max(nums)
    sieve = sieve_of_eratosthenes(max_num)

    # Precompute the number of primes up to each number i <= max_num
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    # Track the wins of Maria and Ben
    players_wins = {"Maria": 0, "Ben": 0}

    # Determine the winner for each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            players_wins["Maria"] += 1
        else:
            players_wins["Ben"] += 1

    # Determine the overall winner
    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"
    else:
        return None
