"""Given an array A with unique elements (a set), find all possible
subsets of A.

The number of subsets is 2^N, where N is the number of
elements in A.

Example:
    A = [1, 3]
    subsets = [[], [1], [2]]


    {1, 2}
    op1 {}
        op1.1 {}
        op1.2 {2}
    op2 {1}
        op2.1 {1}
        op2.1 {1,2}

    {}, {2}, {1}, {1,2}

"""


def all_subsets(s):
    subsets = []

    def _find_subsets(current_set, choices, index):
        if index == len(s):
            subsets.append(current_set)
            return

        # Recurse without adding to current_set
        _find_subsets(current_set, choices, index + 1)

        # Recurse add the current element to the subset
        _find_subsets(current_set + [choices[index]], choices, index + 1)

    _find_subsets([], s, 0)

    return subsets


if __name__ == "__main__":
    test_cases = [
        ([], [[]]),
        ([1], [[], [1]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
    ]

    for input_set, expected in test_cases:
        result = all_subsets(input_set)
        assert sorted(result) == sorted(expected)
