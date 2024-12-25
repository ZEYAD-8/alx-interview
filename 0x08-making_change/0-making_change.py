#!/usr/bin/python3
"""
Making Change module.
This module contains the makeChange function.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    # Nothing to calculate
    if total <= 0:
        return 0

    # set up the variables
    change = total, count = 0, idx = 0

    # Sort the coins for indexed addressing
    sorted = sorted(coins, reverse=True)
    length = len(coins)

    # loop to calculate
    while change > 0:
        # out of range
        if idx >= length:
            return -1
        # if the current coin can be subtracted from the change
        if change - sorted[idx] >= 0:
            # do so and add 1 to the count
            change -= sorted[idx]
            count += 1
        # if not, then this coin will no longer be used, move to a smaller one.
        else:
            idx += 1

    return count
