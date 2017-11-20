"""Given a set of different coins denominations S and a total
T, find the smallest number of coins that sum T.

Example:
    S = {1, 5, 10, 25}, T = 40
    result = 3  # {5, 10, 25}

    S = {1, 5, 9, 20}, T = 27  <- Notice that a greedy algorithm would fail here
    result = 3  # {9, 9, 9}

For S = [1, 3, 5] and T = 7, the dp matrix is going to look
like this:

    0   1   2   3   4   5   6   7
 0  0   7   7   7   7   7   7   7
 1  0   1   2   3   4   5   6   7
 3  0   1   2   1   2   3   2   3
 5  0   1   2   1   2   1   2   3
"""


def find_minimum_coins(coins, target):
    if not coins:
        raise Exception("you must provide a set of coins")

    if target < 1:
        raise Exception("you cannot make change for an amount less than 1")

    rows = len(coins) + 1
    columns = target + 1

    dp = [[0] * columns for _ in range(rows)]

    for row in range(1, rows):
        cc = coins[row - 1]
        for column in range(1, columns):
            if row == 1:
                dp[row][column] = column // cc
            elif cc <= column:
                nc = column // cc  # number of coins cc that fit in column
                dp[row][column] = min(
                    nc + dp[row - 1][column - nc * cc],
                    dp[row - 1][column]
                )
            else:
                dp[row][column] = dp[row - 1][column]

            # Print the matrix on every iteration
            # print("row = ", row, "column = ", column, "cc = ", cc)
            # for line in dp:
            #     print(line)
            # print()

    return dp[rows - 1][columns - 1]


if __name__ == "__main__":
    test_cases = [
        ([1], 20, 20),
        ([1], 10, 10),
        ([2], 20, 10),
        ([1, 5, 6, 8], 11, 2),
        ([1, 2], 21, 11),
        ([1, 3, 5], 7, 3),          # [1, 3, 3] or [1, 1, 5]
        ([1, 5, 10, 25], 40, 3),    # [5, 10, 15]
        ([1, 5, 9, 20], 27, 3)      # [9,  9,  9]
    ]

    for input_coins, input_target, expected_output in test_cases:
        result = find_minimum_coins(input_coins, input_target)
        assert result == expected_output


