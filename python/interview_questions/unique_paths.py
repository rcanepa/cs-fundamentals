"""A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Grid of 3 x 7

    S # # # # # #
    # # # # # # #
    # # # # # # E
"""


# TC: O(2^N), SP: O(1)
def find_paths_recursive(m, n):
    paths = 0

    def _find_paths_recursive(curr_x, curr_y):
        if curr_x > m or curr_y > n:
            return

        nonlocal paths
        if curr_x == m - 1 and curr_y == n - 1:
            paths += 1

        _find_paths_recursive(curr_x + 1, curr_y)
        _find_paths_recursive(curr_x, curr_y + 1)

    _find_paths_recursive(0, 0)
    return paths


# TC: O(N * M), SP: O(N * M)
def find_paths(m, n):
    paths_dp = [[0] * m for _ in range(n)]

    for i in range(n):
        paths_dp[i][0] = 1

    for i in range(m):
        paths_dp[0][i] = 1

    for row in range(1, n):
        for column in range(1, m):
            paths_dp[row][column] = paths_dp[row - 1][column] + paths_dp[row][column - 1]

    return paths_dp[n - 1][m - 1]


if __name__ == "__main__":
    test_cases = [
        # (rows, columns, expected_result)
        (4, 5, 35),
        (3, 3, 6),
        (1, 2, 1),
        (4, 3, 10)
    ]
    for rows, columns, expected_result in test_cases:
        result = find_paths(columns, rows)
        assert result == expected_result
        assert result == find_paths_recursive(columns, rows)

    print(find_paths(100, 100))

