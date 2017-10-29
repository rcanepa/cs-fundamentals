"""Implement an algorithm that takes an array A and randomly
reorder all of its elements."""

import random


def random_pos(min_pos, max_pos):
    """Return an integer between `min_pos` and `max_pos`."""
    return int(min_pos + (random.random() * (max_pos + 1 - min_pos)))


def shuffle_array(a):
    """If the number of elements of `a` is N, then for this solution
    we have:
        Time Complexity: O(N)
        Space Complexity: O(1)
    """
    if a is None:
        raise Exception("None was received instead of a list")

    n = len(a)
    for index in range(n - 1):
        new_pos = random_pos(index + 1, n - 1)
        a[new_pos], a[index] = a[index], a[new_pos]

    return a


if __name__ == "__main__":
    a = list(range(13))
    print(shuffle_array(a))

