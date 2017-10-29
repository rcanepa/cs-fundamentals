"""
Find all pairs from the array A that sum S.
Example:
    Input
        A = [5, 15, 8, 9, 3, 2, -1, 4]
        S = 7
    Output
        [(5, 2), (8, -1), (3, 4)]
"""
from collections import defaultdict


def find_pairs(numbers, target):
    d = defaultdict(int)
    r = []

    for n in numbers:
        d[n] += 1

    for n in numbers:
        complement = target - n
        if n in d and complement in d:
            if complement == n and d[complement] < 2:
                continue
            r.append((n, complement))
            d[n] -= 1
            d[complement] -= 1
            if d[n] < 1:
                d.pop(n)
            if d[complement] < 1:
                d.pop(complement)

    return r


if __name__ == "__main__":
    test_cases = [
        ([], 100, []),
        ([1, 2, 3, 4], 0, []),
        ([1, 1, 1, 1], 2, [(1, 1), (1, 1)]),
        ([0, 0, 1, 1], 0, [(0, 0)]),
        ([1, -1, 4, -4], 0, [(1, -1), (4, -4)]),
        ([5, 15, 8, 9, 3, 2, -1, 4], 1, [(2, -1)]),
        ([5, 15, 8, 9, 3, 2, -1, 4], 2, [(3, -1)]),
        ([5, 15, 8, 9, 3, 2, -1, 4], 3, [(-1, 4)]),
        ([5, 15, 8, 9, 3, 2, -1, 4], 4, [(5, -1)]),
        ([5, 15, 8, 9, 3, 2, -1, 4], 7, [(5, 2), (8, -1), (3, 4)]),
        ([4, 2, 2], 6, [(4, 2)]),
        ([4, 4, 2], 6, [(4, 2)]),
    ]

    for index, (numbers, target, expect) in enumerate(test_cases):
        result = find_pairs(numbers, target)
        print("Test {}:".format(index), "numbers", numbers, "target", target, "result", result)
        assert result == expect
