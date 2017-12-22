"""Write a function that returns every permutation of n numbers that
add up to k.

Examples:
    k = 4, n = 2
    result: [[2, 2], [2, 2], [1, 3], [3, 1]]

    k = 5, n = 2
    result: [[3, 2], [2, 3], [1, 4], [4, 1]]
"""


def find_n_sum_k(k, n):
    space = list(range(1, k))
    solutions = set()

    def _find_n_sum_k(k_left, n_left, numbers):
        if k_left == 0 and n_left == 0:
            solutions.add(numbers)

        if k_left < 0 or n_left < 0:
            return

        for curr in space:
            _find_n_sum_k(k_left - curr, n_left - 1, numbers + (curr,))

    _find_n_sum_k(k, n, ())
    return solutions


if __name__ == "__main__":
    test_cases = [
        (
            4,
            2,
            { ( 2, 2 ), ( 2, 2 ), ( 1, 3 ), ( 3, 1 ) }
        ),
        (
            5,
            2,
            { ( 3, 2 ), ( 2, 3 ), ( 1, 4 ), ( 4, 1 ) }
        ),
    ]

    for k, n, expected_result in test_cases:
        result = find_n_sum_k(k, n)
        print(result, expected_result)
        assert result == expected_result
