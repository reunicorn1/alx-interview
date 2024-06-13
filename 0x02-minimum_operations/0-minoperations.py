#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
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
    if type(n) is not int or n < 1:
        return 0

    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        else:
            done += clipboard
            ops_count += 1

    return ops_count
