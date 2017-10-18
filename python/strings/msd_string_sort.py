"""MSD (most significant digit) string sort algorithm.
This sorting algorithm works sorting strings character by character
from left to right.


Characteristics:
    - Stable (preserves original order).

Main differences with the LSD string sort algorithm:
    - Runs from left to right.
    - It's recursive.
"""

# Radix: number of different possible characters.
# 256 -> Extended ASCII.
r = 256


def _initialize_list(size, default_value):
    return [default_value] * size


def _get_char(string, index):
    return ord(string[index]) if index < len(string) else -1


def _msd_sort(strings, low, high, digit, pstrings):
    if high <= low:
        return

    # Compute the frequency of each character.
    count = _initialize_list(r + 2, 0)
    for index in range(low, high + 1):
        count[_get_char(strings[index], digit) + 2] += 1

    # Compute the starting point for each character.
    for i in range(r + 1):
        count[i + 1] += count[i]

    for index in range(low, high + 1):
        ascii_code = _get_char(strings[index], digit)  # Transform character to int.
        s_position = count[ascii_code + 1]  # Find its starting point.
        count[ascii_code + 1] += 1  # Increment the starting position for that character.
        pstrings[s_position] = strings[index]  # Put string in its partially final position.

    for i in range(low, high + 1):
        strings[i] = pstrings[i - low]

    # For every 'bucket' run the algorithm.
    for i in range(r):
        _msd_sort(strings, low + count[i], low + count[i + 1] - 1, digit + 1, pstrings)

    return strings


def msd_sort(strings):
    if not isinstance(strings, list):
        raise Exception("A {} was provided instead of a list of strings.".format(type(strings)))

    partial_solution = _initialize_list(len(strings), None)
    return _msd_sort(strings, 0, len(strings) - 1, 0, partial_solution)


if __name__ == "__main__":
    unsorted_strings = [
        "are",
        "by",
        "sea",
        "seashells",
        "ar",
        "seashells",
        "sells",
        "sells",
        "she",
        "a",
        "she",
        "zorro",
        "shells",
        "shore",
        "surely",
        "the",
        "the",
    ]
    print(msd_sort(unsorted_strings))
