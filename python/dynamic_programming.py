"""0/1 Knapsack Problem
Given a bag which can only hold a weight W and a list of items,
each one with a weight Wi and a price Pi, which items should be
put on the bag to maximize the total value?

Example:

    Input:
        W = 4
        i1 = (W1 = 2, P1 = 1)
        i2 = (W2 = 1, P2 = 2)
        i3 = (W3 = 3, P3 = 3)
        i4 = (W4 = 2, P4 = 3)

    Solutions:
        i2, i4 => (W = 3, P = 5)
        i2, i3 => (W = 4, P = 5)
"""


def knapsack(weight, items):
