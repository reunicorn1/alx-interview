#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""
from typing import List

def rotate_2d_matrix(matrix: List[List[str]]) -> None:
    """
    In this method, a matrix is reotated 90 degrees clockwise
    Modifications to the matrix are made in-place.

    Parameters:
    matrix: List[List[str]]
    """
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            t, b = l, r
            # save the topleft value
            topleft = matrix[t][l + i]

            # move bottom left to top left
            matrix[t][l + i] = matrix[b - i][l]

            # move bottom right to bottom left
            matrix[b - i][l] = matrix[b][r - i]

            # move top right into bottom right
            matrix[b][r - i] = matrix[t + i][r]

            # move top left into top right
            matrix[t + i][r] = topleft

        r -= 1
        l += 1
