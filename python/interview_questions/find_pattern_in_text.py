"""The exact matching problem. Given a string P called the pattern,
and a longer string T called the text, the exact matching problem is
to find all occurrences, if any, of pattern P in T.

Steps:
    1. Build a suffixes array.
    2. Sort suffixes.
    3. Find all occurrences of P in the sorted suffixes array.

Comments:
    - Slow solution. Step 1 takes O(N^2) because slicing is a quadratic
    operation.
    - Sort the suffixes is O(N * log(N)).
    - Find occurrences in the suffixes array is O(N * P), in which P
    is the length of the pattern.
"""


def have_prefix(s, p):
    if len(p) > len(s):
        return False
    for i in range(len(p)):
        if s[i] != p[i]:
            return False
    return True


if __name__ == "__main__":
    t = "hello world hello hello red button helo hell"
    p = "hello"

    # Step 1
    suffixes = (t[i:] for i in range(len(t)))

    # Step 2
    sorted_suffixed = sorted(suffixes)

    # Step 3
    occurrences = filter(lambda s: have_prefix(s, p), sorted_suffixed)

    print(len(list(occurrences)))

