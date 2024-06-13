#!/usr/bin/python3
"""
0. Minimum Operations
"""
import random
from typing import List


def gcd(a: int, b: int) -> int:
    """
    The  greatest common divisor
    -----------------------
    Parameters:
    a (int)
    b (int)
    -----------------------
    Returns:
    The greatest common divisor between two numbers
    """
    while b:
        a, b = b, a % b
    return a


def pollards_rho(n: int) -> int:
    """
    This function uses the pollards rho algorithm to factorize
    a number
    -----------------------
    Parameters:
    n (int)
    -----------------------
    Returns:
    A prime factor of the number n
    """
    if n % 2 == 0:
        return 2

    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1

    def f(x: int) -> int:
        """
        A mini function to compute pollars rho theory
        """
        return (x**2 + c) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d


def factorize(n: int) -> List[int]:
    """
    Factorizes a number and return a list of all possible prime
    factors
    -----------------------
    Parameters:
    n (int)
    -----------------------
    Returns:
    A list of prime factors
    """
    factors = []

    while n > 1:
        factor = pollards_rho(n)
        factors.append(factor)
        n //= factor

    return factors


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
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        factors = set(factorize(i))
        factors.add(1)
        for j in factors:
            dp[i] = min(dp[i], (dp[j] + i // j))
    return dp[n]
