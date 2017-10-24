"""Return the first occurrence of a pattern in a string. Removing
the break statements will make both versions return all occurrences.
This two implementations are slow ~ O(N * M). N = length of the
string and M = length of the pattern."""


def find_pattern_v1(s, p):
    """Return the first position of `p` in `s` or the length
    of `s` if no match is found."""
    ls, lp = len(s), len(p)
    for i in range(ls - lp + 1):
        if p == s[i:i + lp]:
            return i
    return ls


def find_pattern_v2(s, p):
    """Return the first position of `p` in `s` or the length
    of `s` if no match is found."""
    ls, lp = len(s), len(p)
    j = 0
    for i in range(ls):
        for j in range(lp):
            if s[i + j] != p[j]:
                break
            if j == lp - 1:
                return i
    return ls


if __name__ == "__main__":
    text = "abracadabra"
    pattern = "bra"
    p1 = find_pattern_v1(text, pattern)
    print("-> Result v1:")
    print(text)
    print(" " * p1 + pattern)
    p2 = find_pattern_v2(text, pattern)
    print("-> Result v2:")
    print(text)
    print(" " * p2 + pattern)

