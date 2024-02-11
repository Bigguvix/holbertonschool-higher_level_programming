#!/usr/bin/python3
# 14-pascal_triangle.
"""Returns a list of lists of integers
representing the Pascal’s triangle of n."""


def pascal_triangle(n):
    """Returns the pascal triangle of n."""

    if n <= 0:
        return []

    a = [[0 for x in range(i + 1)] for i in range(n)]
    a[0] = [1]

    for i in range(1, n):
        a[i][0] = 1
        for j in range(1, i + 1):
            if j < len(l[i - 1]):
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
            else:
                a[i][j] = a[i - 1][0]
    return a
