"""Quicksort

Time Complexity:
    Best case: O(N * log(N))
    Worst case: O(N^2)

Space Complexity:
    O(1)
"""


def _partition(array, low, high):
    if low >= high:
        return

    i = low + 1
    j = high
    while i <= j:
        if array[i] <= array[low]:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1

    array[low], array[j] = array[j], array[low]
    _partition(array, low, j - 1)
    _partition(array, j + 1, high)


def quicksort(array):
    if len(array) <= 1:
        return
    low, high = 0, len(array) - 1
    _partition(array, low, high)


if __name__ == "__main__":
    test_cases = [
        ([34, 10, 20, 4, 20, -3, 21], sorted([34, 10, 20, 4, 20, -3, 21])),
        ([3, 10, 0, 4, 20, -3, 1], sorted([3, 10, 0, 4, 20, -3, 1])),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([2, 3, 1], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        (sorted(list(range(199)), reverse=True), sorted(list(range(199))))
    ]

    for test, expected in test_cases:
        quicksort(test)
        assert test == expected
