"""Given an integer S and unsorted array A, find out whether exists
a pair of integer from A that their sum add up to S.

Example:
    Input:  A = [7, 20, 4, 3, 5, 11, 10, 8], S = 17
    Output: True (7, 10)
"""


def can_make_target_sum(integers, target):
    """Return True if a pair of integers that add up to `target` are
    found. The time complexity of this algorithm is O(N), where
    N is the number of integers in `integers`."""
    complements = set()
    for i in integers:  # O(N)
        complement = target - i  # O(1)
        if complement in complements:  # O(1)
            return True
        complements.add(i)  # O(1)

    return False


if __name__ == "__main__":
    test_cases = [
        ([7, 20, 4, 3, 5, 11, 10, 8], 17, True),
        ([7, 20, 4, 3, 5, 11, 10, 8], 20, False),
        ([7, 20, 4, 3, 5, 11, 10, 8], 4, False),
        ([7, 20, 4, 3, 5, 11, 10, 8], 8, True),
        ([8], 8, False),
        ([8, 4], 8, False),
        ([8, 4, 4], 8, True),
        ([4, 8, 4, 2], 8, True),
        ([8, 0], 0, False),
        ([0], 0, False),
        ([0, 0], 0, True),
        ([4, 1, -2, -2], -1, True),
        ([4, 0, -2, -2], -1, False),
    ]

    for a, s, expected in test_cases:
        print("-> Testing target", s, "on array", a)
        assert can_make_target_sum(a, s) == expected
