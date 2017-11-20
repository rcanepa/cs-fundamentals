"""Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.
"""


def find_paths(grid):
    if grid[0][0] == 1:
        return 0

    rows = len(grid)
    columns = len(grid[0])

    dp_paths = [[0] * columns for _ in range(rows)]
    dp_paths[0][0] = 1

    for row in range(1, rows):
        if grid[row][0] == 1:
            dp_paths[row][0] = 0
        else:
            dp_paths[row][0] = dp_paths[row - 1][0]

    for column in range(1, columns):
        if grid[0][column] == 1:
            dp_paths[0][column] = 0
        else:
            dp_paths[0][column] = dp_paths[0][column - 1]

    for row in range(1, rows):
        for column in range(1, columns):
            if grid[row][column] != 1:
                dp_paths[row][column] = dp_paths[row - 1][column] + dp_paths[row][column - 1]

    return dp_paths[rows - 1][columns - 1]


if __name__ == "__main__":
    test_cases = [
        (
            [
                [0]
            ],
            1
        ),
        (
            [
                [1]
            ],
            0
        ),
        (
            [
                [0, 1],
                [1, 0]
            ],
            0
        ),
        (
            [
                [0, 1],
                [0, 1],
                [0, 0]
            ],
            1
        ),
        (
            [
                [0, 0],
                [0, 0],
                [0, 0]
            ],
            3
        ),
        (
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            2
        ),
        (
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 0, 0]
            ],
            1
        ),
        (
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            1
        ),
        (
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 0, 0]
            ],
            0
        )
    ]

    for test_grid, expected_result in test_cases:
        result = find_paths(test_grid)
        assert result == expected_result