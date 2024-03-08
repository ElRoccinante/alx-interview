#!/usr/bin/python3
"""
pascal
"""


def pascal_triangle(n):
    """
    fun
    """
    if n <= 0:
        return []

    jd = []
    pv = []

    for i in range(n):
        prp = []
        for j in range(i+1):
            if j == 0 or i == j:
                prp.append(1)
            else:
                pv = jd[i-1]
                prp.append(pv[j-1]+pv[j])
        jd.append(prp)

    return jd
