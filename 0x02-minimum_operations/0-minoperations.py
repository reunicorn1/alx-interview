#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    This function calculates the fewest number of operations needed
    to exactly n H characters in a text file using Copy, Paste
    operations.

    -----------------------
    Parameters:
    n (int)

    -----------------------
    Returns:
    the minimum number of operations
    """
    if n < 1 or type(n) is not int:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if (i % j == 0):
                dp[i] = min(dp[i], (dp[j] + i // j))
    return int(dp[n])
