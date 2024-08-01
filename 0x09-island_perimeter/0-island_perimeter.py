#!/usr/bin/python3
"""
0x09. Island Perimeter
"""


def island_perimeter(grid):
    """
    This function returns the perimeter of the island descibed
    in grid.

    Arguments:
    ----------
    grid (List(int))

    Returns:
    --------
    An integer representing the perimeter of the island.
    """
    if not grid:
        return 0

    # increasing the size of the grid so we don't go out of range
    grid.append([0] * len(grid[0]))
    for g in grid:
        g.append(0)

    perimeter = 0

    for y in range(len(grid) - 1):
        for x in range(len(grid[0]) - 1):
            if grid[y][x]:
                # check down and right directions
                # if one directions is shared with a cube
                # subtract common sides
                if not grid[y][x + 1] and not grid[y + 1][x]:
                    perimeter += 4
                elif not grid[y][x + 1] or not grid[y + 1][x]:
                    perimeter += 2

                # if both sides are common, the cube worth zero

    return perimeter
