"""Implement an algorithm to find the sum of contiguous subarray
within a one-dimensional array of numbers which has the largest sum.

    Example:
        A = [1, -2, 5, -4, 9, 1, 2, 7]
                    ^               ^
        Sum = 20
"""


def find_max_contiguous_sum(numbers):
    if not numbers:
        return 0

    max_sum = 0
    running_sum = 0
    running_sum_start = 0
    running_sum_end = 0
    max_start = 0
    max_end = 0

    for pos, n in enumerate(numbers):
        running_sum += n
        if running_sum < 0:
            running_sum = 0
            running_sum_start = pos + 1
            running_sum_end = pos

        running_sum_end += 1

        if max_sum < running_sum:
            max_start = running_sum_start
            max_end = running_sum_end
            max_sum = running_sum

    print(numbers[max_start:max_end])
    return max_sum


if __name__ == "__main__":
    test_cases = [
        (
            [],
            0
        ),
        (
            [-1],
            0
        ),
        (
            [1, -2, 5, -4, 9, 1, 2, 7],
            20
        ),
        (
            [1, -3, 5, -2, 9, -8, -6, 4],
            12
        )
    ]

    for input_array, expected_result in test_cases:
        result = find_max_contiguous_sum(input_array)
        print(result)
        assert result == expected_result
