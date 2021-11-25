#!/usr/bin/python3
"""
    pascal's triangle implementation
"""


def pascal_triangle(n):
    """
        n == number of rows
        Return: list of lists of integers representing pascal's triangle of n
    """
    if n <= 0:
        return []

    output = [[1]]

    for i in range(n - 1):
        temp = [0] + output[-1] + [0]
        row = []
        for j in range(len(output[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        output.append(row)

    return (output)
