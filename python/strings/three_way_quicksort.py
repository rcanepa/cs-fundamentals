""" 3-way String Quicksort.
An excellent algorithm to sort any kind of strings. In most cases,
it will perform better than LSD and MSD radix sorts.

Characteristics:
    - O(W * N * log(N)).
    - Extra memory usage: log(N) + W.
    - It isn't stable.
    - Has a short inner loop.
    - Is cache-friendly (MSD Radix Sort isn't).
    - Is in place (MSD Radix Sort uses extra memory on each recursive iteration).
"""


def _get_char_code(string, position):
    """Return an int representation of the character of `string`
    in position `position`. E.g.: string[position]. If the position
    doesn't exist in the string, return -1.
    :return: an integer representing a position in a string."""
    return ord(string[position]) if position < len(string) else -1


def _sort(strings, low, high, digit):
    """Sort strings of `strings` between low and high according to character
    in position `digit`.
    :param strings: list with all strings to be sorted.
    :param low: lower limit of the part of the array to be sorted.
    :param high: upper limit of the part of the array to be sorted.
    :param digit: position of the string that is going to be used to sort the strings.
    :return: None (sort is made in place).
    """

    # Boundaries crossed -> no strings to sort.
    if high <= low:
        return

    lt, gt = low, high
    v = _get_char_code(strings[low], digit)
    i = low + 1

    while i <= gt:
        t = _get_char_code(strings[i], digit)
        if t < v:
            strings[i], strings[lt] = strings[lt], strings[i]
            lt += 1
            i += 1
        elif t > v:
            strings[i], strings[gt] = strings[gt], strings[i]
            gt -= 1
        else:
            i += 1

    _sort(strings, low, lt - 1, digit)
    if v >= 0:
        _sort(strings, lt, gt, digit + 1)
    _sort(strings, gt + 1, high, digit)


def sort(strings):
    _sort(strings, 0, len(strings) - 1, 0)


if __name__ == "__main__":
    unsorted_strings = [
        "are",
        "by",
        "sea",
        "seashells",
        "ar",
        "seashells",
        "z",
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
    sort(unsorted_strings)
    print(unsorted_strings)
