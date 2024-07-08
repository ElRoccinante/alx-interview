#!/usr/bin/python3
"""this is a method"""


def minOperations(n: int) -> int:
    """operations"""
    now = 1
    start = 0
    count_operations = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            count_operations += 2
        else:
            now += start
            count_operations += 1
    if now != n:
        return 0
    return count_operations
