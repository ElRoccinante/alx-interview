#!/usr/bin/python3
"""
pascal
"""


def pascal_triangle(n):
    """
    function
    """
    if n <= 0:
        return []

    x = []
    y = []

    for i in range(n):
        y = []
        for j in range(i+1):
            if j == 0 or i == j:
                y.append(1)
            else:
                y = x[i-1]
                x.append(pvs[j-1]+pvs[j])
        x.append(prp)

    return x
