"""Given an unsorted array of integers where every integer appears
exactly twice, except for one integer which appears only once. Implement
an algorithm that finds the integer that appears only once."""


def find_odd_integer(integers):
    """The time complexity of this algorithm is
    O(N), where N is the number of integers in
    `integers`."""
    odds = set()
    for i in integers:  # O(N)
        if i in odds:
            odds.remove(i)  # O(1)
        else:
            odds.add(i)  # O(1)
    return odds.pop() if len(odds) else None


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 2, 1], 3),
        ([1, 2, 1], 2),
        (list(range(100)) + [200] + list(range(100)), 200),
        # The next are edge cases, maybe they aren't even valid.
        ([], None),
        ([1], 1),
        ([1, 1], None),
    ]

    for array, expected in test_cases:
        print("Running test on integers", array)
        result = find_odd_integer(array)
        print("-> Result", result)
        assert result == expected
