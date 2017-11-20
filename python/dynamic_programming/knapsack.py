"""0/1 Knapsack Problem (0/1 means that items cannot be divided)
Given a bag which can only hold a weight W and a list of items,
each one with a weight Wi and a price Pi, which items should be
put on the bag to maximize the total value of the bag?

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

from collections import namedtuple


def knapsack(max_weight, items):
    """
                    0   1   2   3   ...   w
    0   no item
    1   item 1
    2   item 2
        ...
    n   item n

    """
    n = len(items) + 1
    m = max_weight + 1
    dp = [[0] * m for _ in range(n)]

    for i_index in range(1, n):

        current_item = items[i_index - 1]
        for current_weight in range(1, m):
            if current_item.w <= current_weight:
                dp[i_index][current_weight] = max(
                    current_item.v + dp[i_index - 1][current_weight - current_item.w],
                    dp[i_index - 1][current_weight]
                )
            else:
                dp[i_index][current_weight] = dp[i_index][current_weight - 1]

    return dp[n - 1][m - 1]


Item = namedtuple("Item", ["w", "v"])  # w = weight, v = value


if __name__ == "__main__":
    max_weight = 7
    items = [
        Item(1, 1),
        Item(3, 4),
        Item(4, 5),
        Item(5, 7)
    ]

    max_value = knapsack(max_weight, items)
    print("Max value = ", max_value)
    assert max_value == 9
