"""Longest repeated substring (or LCP = longest common prefix in a suffix array).
Problem: find the longest repeated substring inside a string.

Steps:
    1. Create suffixes. This should be linear in time and space, but it isn't.
        Slicing strings in Python (with slice or [a:b]) is a linear operation
        with regard to the size of the string. In the end, this implementation
        provides a quadratic time O(N^2).
    2. Sort suffixes. This should be N * log(N) in time.
    3. Find LCP between adjacent suffixes.

Usage:
    This script can be use reading data from the standard input. Example:

    cat ~/manifesto.txt | python3 -m interview_questions.longest_repeated_substring
"""
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


def lrs(text):
    """Return the longest repeated substring using a Suffix Array."""
    # Step 1: create the suffixes array.
    suffixes = []
    for i in range(len(s)):
        suffixes.append(s[i:])

    # Step 2: sort the suffixes array.
    sorted_suffixes = sorted(suffixes)

    # Step: find the longest repeated substring.
    result = ""
    for i in range(len(sorted_suffixes) - 1):
        l = lcp(sorted_suffixes[i], sorted_suffixes[i + 1])
        if l > len(result):
            result = sorted_suffixes[i][:l]

    return result


if __name__ == "__main__":
    s = ""
    t0 = time.time()
    for line in sys.stdin:
        s += line
    t1 = time.time()
    print("################################################################################")
    print('-> Took {:.3f}ms to read the file.'.format((t1 - t0) * 1000))

    t0 = time.time()
    r = lrs(s)
    t1 = time.time()
    print('-> Took {:.3f}ms to find the longest repeated substring the file.'.format((t1 - t0) * 1000))
    print("################################################################################")
    print("The longest repeated substring is:")
    print(r)
