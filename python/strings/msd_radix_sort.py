"""MSD (most significant digit) string sort algorithm.
This sorting algorithm works sorting strings character by character
from left to right.

This is a different implementation than the one found in the
file msd_string_sort.py. It has less LOC because it makes use
of list comprehensions. Also, instead of just counting the frequencies,
it keeps the whole strings inside 'buckets'.
"""

# R = radix. The number of characters of the alphabet supported
# by this implementation of Radix Sort. It won't work with Unicode.
R = 256  # -> Extended ASCII.


def msd_radix_sort(data, digit=0):
    """Recursively sort a list of strings. Strings are sorted char by char
    from left to right. `digit` marks the current char by which their are
    going to be sorted.
    :param data: list of strings to be sorted.
    :param digit: string position by which strings are going to be sorted.
    :return: list of strings
    """

    # print("\t\t" * digit, "->", data, digit)

    # If the list contains just one string, return it.
    if len(data) <= 1:
        return data

    # Create a bucket for every possible character.
    buckets = [[] for _ in range(R)]
    complete_bucket = []

    # Locate every string in a bucket according to the character of it
    # that is being processed (`digit` points to a position in the string).
    for s in data:
        if len(s) > digit:
            buckets[ord(s[digit])].append(s)
        else:
            complete_bucket.append(s)

    # For every bucket, run radix sort on the next digit.
    buckets = [msd_radix_sort(buckets[r], digit + 1) for r in range(R) if len(buckets[r]) > 0]

    # Flatten `buckets` and concat with `complete_bucket`.
    return complete_bucket + [bucket for bucket_list in buckets for bucket in bucket_list]


if __name__ == "__main__":
    unsorted_data = [
        "b",
        "ab",
        "ca",
        "aaa",
        "c"
    ]
    print("-> ", msd_radix_sort(unsorted_data))
