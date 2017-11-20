"""Given a matrix M of NxN, implement a function that
can rotate M clockwise and in place.

Example:
    M = 1    => 1

    M = 1 2  => 3 1
        3 4     4 2

    M = 1 2 3       7 4 1
        4 5 6  =>   8 5 2
        7 8 9       9 6 3

    M = 1  2  3  4          13  9  5  1
        5  6  7  8      =>  14 10  6  2
        9 10 11 12          15 11  7  3
       13 14 15 16          16 12  8  4

       i=0
        1  2  3  4 j=0
        5  6  7  8
        9 10 11 12
       13 14 15 16 k=n-i
       l=n-j
"""


def rotate_clockwise_matrix(matrix):
    """Rotate `matrix` 90 degrees clockwise. The rotation is in place,
    so the space complexity of this algorithm is O(1)."""
    if len(matrix) < 2:
        return matrix

    layers = len(matrix) // 2

    for offset in range(layers):
        matrix_limit = len(matrix) + offset + (offset * 2) - 1

        for i in range(offset, offset + len(matrix) - (offset * 2) - 1):

            tl = matrix[offset][i]
            tr = matrix[i][matrix_limit]
            br = matrix[matrix_limit][matrix_limit - i + offset]
            bl = matrix[matrix_limit - i + offset][offset]

            matrix[i][matrix_limit] = tl
            matrix[matrix_limit][matrix_limit - i + offset] = tr
            matrix[matrix_limit - i + offset][offset] = br
            matrix[offset][i] = bl

    return matrix


if __name__ == "__main__":
    test_cases = [
        (
            [[1]],
            [[1]]
        ),
        (
            [[1, 2],
             [3, 4]],
            [[3, 1],
             [4, 2]]
        ),
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]
        ),
        (
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]],
            [[13, 9, 5, 1],
             [14, 10, 6, 2],
             [15, 11, 7, 3],
             [16, 12, 8, 4]]
        )
    ]

    for matrix, expected in test_cases:
        rotated_matrix = rotate_clockwise_matrix(matrix)
        print("N =", len(matrix))
        for line in rotated_matrix:
            print(line)
        print()
        assert str(rotated_matrix) == str(expected)
