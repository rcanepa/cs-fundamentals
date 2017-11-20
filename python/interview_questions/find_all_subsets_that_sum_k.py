"""Given an array of integers A and an integer K, find all subsets that
sum K.

Example:
    A = [1, 2, 1, 4, 3]
    K = 3
    subsets = [[1, 2], [2, 1], [3]]
"""


def all_subsets(s, target):
    """Return all subsets of `s` that sum `target`.
    TC: O(2^N), where N is number of elements in `s`."""

    if not s:
        return {}

    solutions = set()

    def _all_subsets(current_subset, index, current_sum):
        if current_sum == target:
            solutions.add(current_subset)

        if index == len(s):
            return

        _all_subsets(current_subset, index + 1, current_sum)
        _all_subsets(current_subset + (s[index],), index + 1, current_sum + s[index])

    _all_subsets((), 0, 0)

    return solutions


if __name__ == "__main__":
    test_cases = [
        ([], 100, {}),
        ([1, 2, 1, 4, 3], 3, {(1, 2), (2, 1), (3,)}),
        ([1], 0, {()}),
        ([1], 1, {(1,)}),
        ([1, 1], 1, {(1,), (1,)}),
        ([1, 2, 4, -1], 3, {(1, 2), (4, -1)})
    ]

    for subset, target, expected in test_cases:
        subsets_found = all_subsets(subset, target)
        print(subsets_found)
        assert subsets_found == expected