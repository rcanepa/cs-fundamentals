"""Return the first occurrence of a pattern in a string. Removing
the break statements will make both versions return all occurrences.
If N is the length of the string and M the length of the pattern,
brute force implementation run in O(N * M) time in the worst case.

The worst case is one in which the pattern resembles very closely
the string in multiple parts. For example:

- Pattern: AAAC
- String:  AAAAAAAAAAAAAAAAC

In this case, every character of the string has to be compared to
all the characters of the pattern. The mismatch is always at the
end of the comparison.

However, in some cases, this algorithm could perform close to
O(N). If the strings are uniformly distributed random letters, then the
chance that characters match is 1 in 26 (in most cases, the trial
check will reject the match at the initial letter). In this case the
expected complexity of searching string S[] of length N is on the
order of N comparisons or O(N). For example, if S[] is 1 billion
characters and W[] is 1000 characters, then the string search should
complete after about one billion character comparisons.
"""


def find_pattern_v1(s, p):
    """Return the first position of `p` in `s` or the length
    of `s` if no match is found. In this case `i` doesn't move
    forward until there is a mismatch between the pattern and
    the part of the string being examined. `j` moves back and
    forth for every value of `i`."""
    n, m = len(s), len(p)
    for i in range(n):
        for j in range(m):
            if s[i + j] != p[j]:
                break
            if j == m - 1:
                return i
    return n


def find_pattern_v2(s, p):
    """Return the first position of `p` in `s` or the length
    of `s` if no match is found. In this case `i` goes back and
    forth along with `j`. When there is a mismatch, `i` goes back
    `j` positions to the start of a new search."""
    n, m = len(s), len(p)
    i = j = 0
    while i < n and j < m:
        if s[i] == p[j]:
            j += 1
        else:
            i -= j  # Move back `i` `j` positions.
            j = 0
        i += 1  # Move `i` forward.
    # If `j == m` the pattern was found.
    return i - m if j == m else n


if __name__ == "__main__":
    test_cases = [
        ("abracadabra", "bra"),
        ("aaaaaaab", "ab"),
        ("cxccc", "c"),
        ("this pattern is not a common pattern!", "!")
    ]
    for test_case, (text, pattern) in enumerate(test_cases):
        print("############# Test case {} #############".format(test_case))
        p1 = find_pattern_v1(text, pattern)
        print("-> Result v1:")
        print(text)
        print(" " * p1 + pattern)
        p2 = find_pattern_v2(text, pattern)
        print("-> Result v2:")
        print(text)
        print(" " * p2 + pattern)
        print("#######################################")
