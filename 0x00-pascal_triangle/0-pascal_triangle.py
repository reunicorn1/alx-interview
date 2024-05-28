#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    This functio returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    list = []

    for i in range(n):
        sublist = []
        for j in range(i + 1):
            if j == 0 or j == i:
                sublist.append(1)
            else:
                sublist.append(list[i - 1][j - 1] + list[i - 1][j])
        list.append(sublist)

    return list
