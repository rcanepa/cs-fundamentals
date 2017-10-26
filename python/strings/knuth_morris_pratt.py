#!/usr/bin/env python

"""Knuth-Morris-Pratt (KMP) text search algorithm.
This algorithm avoid going back and forth in the text for the search
of a pattern (it doesn't need a backup of the last K characters). That
means that its worst time is O(N), where N is the length of the text.

LPS Array for pattern "ABABX":
--------------------------
  i     0   1   2   3   4  <- array index
p(i)    A   B   A   B   X  <- pattern
f(i)    0   0   1   2   0  <- (*)
--------------------------

(*) f(i) represents the length of the longest proper prefix in the (sub)pattern [0:i]
that matches a proper suffix in the same (sub)pattern.

- Proper prefix: All the characters in a string, with one or more cut off the end.
"S", "Sn", "Sna", and "Snap" are all the proper prefixes of "Snape".

- Proper suffix: All the characters in a string, with one or more cut off the beginning.
"agrid", "grid", "rid", "id", and "d" are all proper suffixes of "Hagrid".



####################
 Visual walkthrough
####################

i = 0
j = 0
string  = "ABTABABYABABX"
           __x
pattern = "ABABX"

mismatch on i = j = 2, search on f(j-1) to find new position of j
f(j-1) = f(2-1) = f(1) = 0

i = 3
j = 0
string  = "ABTABABYABABX"
              ____x
pattern =    "ABABX"
mismatch on i = 7 and j = 4, search on f(j-1) to find new position of j
f(j-1) = f(4-1) = f(3) = 2 (new iteration starts from j = 2)

i = 7
j = 2
string  = "ABTABABYABABX"
                __x
pattern =      "ABABX"
mismatch on i = 7 and j = 2, search on f(j-1) to find new position of j
f(j-1) = f(2-1) = f(1) = 0

i = 8
j = 0
string  = "ABTABABYABABX"
                   _____
pattern =         "ABABX"

Pattern found!

"""
import sys


def compute_lps_array(pattern):
    """Return the `lps` array for given the string `pattern`.
    This means that `lps[i]` is the longest proper prefix of `pattern[0:i]`
    which is also a suffix of `pattern[0:i]`.

    The efficiency of this algorithm is O(M), where M is the length
    of pattern.

    Example:
        pattern:  | a | b | a | b | a | b | c | a |
        index:    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
        value:    | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |
    """
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern, start=0):
    n, m = len(text), len(pattern)
    lps = compute_lps_array(pattern)

    i = start
    j = 0
    occurrences = []

    while i < n:
        if pattern[j] == text[i]:
            j += 1
            i += 1
        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences


def main():
    # text = "abaxabcaabababcaaxczc sdas d abababca daskjdh awqu 6sdauy abababca cxzc xzc"
    # pattern = "abababca"
    text = ""
    pattern = "house"
    for line in sys.stdin:
        text += line
    found_occurrences = kmp(text, pattern, 30)
    for i, o in enumerate(found_occurrences):
        print("-> {}: {}".format(i, text[o - 10: o + 10].replace("\n", " ").replace("\r", "")))


if __name__ == "__main__":
    main()
