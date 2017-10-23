"""Find the number of unique substrings from a string."""

import sys
import time


def lcp(s1, s2):
    """Return the length of the longest common prefix
    between strings `s1` and `s2`."""
    comp = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            break
        comp += 1
    return comp


def unique_substrings(text):
    """Return the longest repeated substring using a Suffix Array."""
    # Step 1: create the suffixes array.
    suffixes = []
    for i in range(len(s)):
        suffixes.append(s[i:])

    # Step 2: sort the suffixes array.
    sorted_suffixes = sorted(suffixes)

    # Step: common prefixes between suffixes.
    lcp_array = [0] * len(suffixes)
    for i in range(len(sorted_suffixes) - 1):
        lcp_array[i + 1] = (lcp(sorted_suffixes[i], sorted_suffixes[i + 1]))

    # Compute the number of unique substrings.
    all_substrings = len(s) * (len(s) + 1) // 2
    return all_substrings - sum(lcp_array)


if __name__ == "__main__":
    s = ""
    t0 = time.time()
    for line in sys.stdin:
        s += line
    s = s.rstrip()
    t1 = time.time()
    print("################################################################################")
    print('-> Took {:.3f}ms to read the file.'.format((t1 - t0) * 1000))

    t0 = time.time()
    r = unique_substrings(s)
    t1 = time.time()
    print('-> Took {:.3f}ms to find all unique substrings.'.format((t1 - t0) * 1000))
    print("################################################################################")
    print("Number of substrings: {:,d}".format(len(s) * (len(s) + 1) // 2))
    print("Number of unique substrings are: {:,d}".format(r))
