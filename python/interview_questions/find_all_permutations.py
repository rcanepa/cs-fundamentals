"""Given an string S, find all its permutations.

Example:
    S = "abc"
    Permutations found = ["abc", "cab", "bac", "acb", "bac", "cba"]
"""


def find_permutations(s):
    if len(s) <= 1:
        return [s]

    permutations = []

    def _find_permutations(partial, rest, permutations):
        if len(rest) == 0:
            permutations.append(partial)

        for i in range(len(rest)):
            _find_permutations(partial + rest[i], rest[:i] + rest[i+1:], permutations)

    _find_permutations("", s, permutations)
    return permutations


if __name__ == "__main__":
    test_cases = [
        ("", [""]),
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("abc", ["abc", "acb", "cab", "bac", "bca", "cba"]),
        ("abcd", [
            "abcd", "abdc", "adbc", "dabc",
            "acbd", "acdb", "adcb", "dacb",
            "cabd", "cadb", "cdab", "dcab",
            "bacd", "badc", "bdac", "dbac",
            "bcad", "bcda", "bdca", "dbca",
            "cbad", "cbda", "cdba", "dcba"
        ]),
    ]

    for s, expected in test_cases:
        found_permutations = find_permutations(s)
        print(found_permutations)
        assert set(found_permutations) == set(expected)
