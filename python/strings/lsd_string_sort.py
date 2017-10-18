"""LSD (least significant digit) string sort algorithm.
This algorithm is based on the Key-indexed counting sorting algorithm. The
main difference is that LSD run the same operation for W characters instead
of just 1 integer. It is assumed that strings are fixed length and that W
is the length of them.

Characteristics:
    - Stable (preserves original order).
    - Linear time: O(N * W).

E.g.:

Given the strings:
    [
        "4PGC938",
        "2IYE230",
        "3CI0720"
    ]

The algorithm is going to sort them through 7 iterations (W = 7). The process
is going to sort them char by char starting from right to left (from the least
significant 'digit').

After the first iteration, the result is going to be:
    [
        "2IYE230",
        "3CI0720"
        "4PGC938",
    ]

After the second:
    [
        "3CI0720"
        "2IYE230",
        "4PGC938",
    ]

And so on until the end:
    [
        "2IYE230",
        "3CI0720"
        "4PGC938",
    ]
"""


def _initialize_list(size, default_value):
    return [default_value] * size


def lsd_sort(strings, key_length=None):
    if not isinstance(strings, list):
        raise Exception("A {} was provided instead of a list of strings.".format(type(strings)))

    if key_length is None:
        key_length = len(strings[0])

    r = 256

    # cn iterate on a string from right to left.
    for cn in reversed(range(key_length)):

        # Compute the frequency of each character.
        count = _initialize_list(r + 1, 0)
        for s in strings:
            count[ord(s[cn]) + 1] += 1

        # Compute the starting point for each character.
        for j in range(r - 1):
            count[j + 1] += count[j]

        # Distribute the date in a new list.
        partial_solution = _initialize_list(len(strings), None)

        for s in strings:
            ascii_code = ord(s[cn])  # Transform the character to its int representation.
            s_position = count[ascii_code]  # Find its starting point.
            count[ascii_code] += 1  # Increment the starting position for that character.
            partial_solution[s_position] = s  # Add the string in its partially final position.

        # Replace the original list with the partially sorted list.
        strings = partial_solution

    return strings


if __name__ == "__main__":
    licenses = [
        "4PGC938",
        "2IYE230",
        "3CI0720",
        "1ICK750",
        "1OHV845",
        "4JZY524",
        "1ICK750",
        "3CI0720",
        "1OHV845",
        "1OHV845",
        "2RLA629",
        "2RLA629",
        "3ATW723"
    ]
    print(lsd_sort(licenses))

