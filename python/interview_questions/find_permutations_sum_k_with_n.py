"""Write a function that returns every permutation of n numbers that
add up to k.

Examples:
    k = 4, n = 2
    result: [[2, 2], [2, 2], [1, 3], [3, 1]]

    k = 5, n = 2
    result: [[3, 2], [2, 3], [1, 4], [4, 1]]
"""


def find_n_sum_k(k, n):
    return []


if __name__ == "__main__":
    test_cases = [
        (
            4,
            2,
            [[2, 2], [2, 2], [1, 3], [3, 1]]
        ),
        (
            5,
            2,
            [[3, 2], [2, 3], [1, 4], [4, 1]]
        )
    ]

    print(find_n_sum_k(4, 2))
