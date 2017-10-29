"""Given an array and a number k where k is smaller than size of array,
find the k’th smallest element in the given array."""


def _partition(array, low, high):
    """Choose the first element of `array`, put to the left of it
    all elements which are smaller, and to the right all elements which
    are bigger than it.

    Return the final position of this element.
    """
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
    return j


def find_kth_smallest_element(array, kth):
    if kth >= len(array):
        raise Exception("kth is greater than the number of array's elements")

    low, high = 0, len(array) - 1
    pivot = _partition(array, low, high)
    while pivot != kth:
        if pivot > kth:
            pivot = _partition(array, low, pivot - 1)
        else:
            pivot = _partition(array, pivot + 1, high)
    return array[kth]


if __name__ == "__main__":
    test_cases = [
        (
            [34, 10, 20, 4, 20, -3, 21],
            2,
            sorted([34, 10, 20, 4, 20, -3, 21])[2]
        ),
        (
            [3, 10, 20, 4, 20, -3, 21, -1, 100],
            1,
            sorted([3, 10, 20, 4, 20, -3, 21, -1, 100])[1]
        ),
        (
            [3, 10, 20, 4, 20, -3, 21, -1, 100],
            8,
            sorted([3, 10, 20, 4, 20, -3, 21, -1, 100])[8]
        ),
        (
            [3, 10, 20, 4, 20, -3, 21, -1, 100],
            0,
            sorted([3, 10, 20, 4, 20, -3, 21, -1, 100])[0]
        ),

    ]

    for test, kth, expected in test_cases:
        assert find_kth_smallest_element(test, kth) == expected
