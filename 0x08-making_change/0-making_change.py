#!/usr/bin/python3
"""
Making Change module.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    change = total, count = 0, idx = 0
    sorted = sorted(coins, reverse=True)
    length = len(coins)
    while change > 0:
        if idx >= length:
            return -1
        if change - sorted[idx] >= 0:
            change -= sorted[idx]
            count += 1
        else:
            idx += 1
    return count
