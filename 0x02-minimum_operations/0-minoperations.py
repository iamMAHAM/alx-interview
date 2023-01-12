#!/usr/bin/python3
"""
module: calculates the fewest number of
operations needed
to result in exactly n H characters
in the file
"""
from typing import List


def minOperations(n: int):
    """
    methods to count nomber of operations (copy and paste)
    """
    if n < 2:
        return 0
    factor_list: List[int] = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
