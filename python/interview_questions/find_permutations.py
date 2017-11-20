"""Given two strings S1 and S2, find all permutations
of S1 in S2.

Example:
    S1 = "ab"
    S2 = "babero"

    Permutations found: ["ba", "ab"]
"""
from collections import defaultdict


def all_permutations(s1, s2):
    permutations = []

    required_chars = defaultdict(int)

    # TC = O(N), where N = len(s1)
    for c in s1:
        required_chars[c] += 1

    n = len(s1)
    back = 0
    current_chars = defaultdict(int)

    # TC = O(M * K), where M = len(s2) and K = len(required_chars.keys())
    for front, c in enumerate(s2):
        current_chars[c] += 1

        distance = front - back + 1
        if distance == n:
            if current_chars == required_chars:
                permutations.append(s2[back:distance + back])
            current_chars[s2[back]] -= 1
            if current_chars[s2[back]] == 0:
                current_chars.pop(s2[back])
            back += 1

    return permutations


if __name__ == "__main__":
    test_cases = [
        (
            "ab",
            "babero",
            ["ba", "ab"]
        ),
        (
            "acr",
            "my car was crashed yesterday",
            ["car", "cra"]
        ),
        (
            "a",
            "my car was crashed yesterday",
            ["a", "a", "a", "a"]
        ),
        (
            "sa",
            "my car was crashed yesterday",
            ["as", "as"]
        )
    ]
    for s1, s2, expected in test_cases:
        result = all_permutations(s1, s2)
        assert result == expected
