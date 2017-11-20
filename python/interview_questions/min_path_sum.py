"""Given a m x n grid filled with non-negative numbers, find a path from
top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum."""


def find_min_path(grid):
    rows = len(grid)
    columns = len(grid[0])

    dp = [[0] * columns for _ in range(rows)]

    dp[0][0] = grid[0][0]
    for row in range(1, rows):
        dp[row][0] = grid[row][0] + dp[row - 1][0]

    for column in range(1, columns):
        dp[0][column] = grid[0][column] + dp[0][column - 1]

    for row in range(1, rows):
        for column in range(1, columns):
            dp[row][column] = grid[row][column] + min(dp[row - 1][column], dp[row][column - 1])

    return dp[rows - 1][columns - 1]


if __name__ == "__main__":
    test_cases = [
        (
            [[1]],
            1
        ),
        (
            [[1, 0],
             [2, 0]],
            1
        ),
        (
            [[1, -1],
             [2, 0]],
            0
        ),
        (
            [[1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]],
            7
        ),
        (
            [[1, 1, 1],
             [1, 5, 1],
             [1, 1, 1]],
            5
        ),

    ]
    for index, (input_grid, expected_result) in enumerate(test_cases):
        print("Running test case number:", index + 1)
        print("\t", input_grid)
        result = find_min_path(input_grid)
        print("\t Result:", result)
        print("\t Expected result:", expected_result)
        assert result == expected_result