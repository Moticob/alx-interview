#!/usr/bin/env python3
from typing import List


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows (n).

    Args:
    - n (int): Number of rows for Pascal's triangle.

    Returns:
    - list of lists of integers: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# Test the function with the provided main script
if __name__ == "__main__":
    # Test case with n = 5
    triangle_5_rows = pascal_triangle(5)
    for row in triangle_5_rows:
        print(row)

