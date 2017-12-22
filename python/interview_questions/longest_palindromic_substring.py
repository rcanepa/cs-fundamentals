"""Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.

Example:
    Input: "babad"
    Output: "bab"

Note: "aba" is also a valid answer.

Example:
    Input: "cbbd"
    Output: "bb"
"""


def is_palindrome(string, low, high):
    i = low
    j = high
    while j > i:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def longest_palindrome(string):
    if len(string) < 2:
        return string

    n = len(string)
    longest_palindrome_size = 0
    longest_palindrome_start = 0
    longest_palindrome_end = 0

    # TC: O(N^3), where N = len(string)
    for i in range(n):  # TC: O(N)
        for j in range(i, n):  # TC: O(N)
            if is_palindrome(string, i, j) and j - i + 1 > longest_palindrome_size:  # TC: O(N)
                longest_palindrome_size = j - i + 1
                longest_palindrome_start = i
                longest_palindrome_end = j
    return string[longest_palindrome_start:longest_palindrome_end + 1]


def longest_palindrome_dp(string):
    n = len(string)

    if n < 2:
        return string

    dp = [[False] * n for _ in range(n)]

    # All substring of length 1 are palindromes
    # TC: O(N)
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    # TC: O(N)
    for i in range(n - 1):
        dp[i][i + 1] = string[i] == string[i + 1]

    # Check the rest of the substrings
    m = 2
    # TC: O(N^2), where N = len(string)
    while m < n:  # TC: O(N)
        for i in range(n - m):  # TC: O(N / 2) = O(N)
            j = i + m
            dp[i][j] = string[i] == string[j] and dp[i + 1][j - 1]
        m += 1

    longest_palindrome_size = 1
    longest_palindrome_start = longest_palindrome_end = 0

    # TC: O(N^2), where N = len(string)
    for i in range(n):  # TC: O(N)
        for j in range(i + 1, n):  # TC: O(N / 2) = O(N)
            if dp[i][j] and j - i + 1 > longest_palindrome_size:
                longest_palindrome_size = j - i + 1
                longest_palindrome_start = i
                longest_palindrome_end = j
    return string[longest_palindrome_start:longest_palindrome_end + 1]


def _expand_around_center(string, low, high):
    l, r = low, high

    # TC: O(N)
    while l >= 0 and r < len(string) and string[l] == string[r]:
        l -= 1
        r += 1
    return r - l - 1


def longest_palindrome_expand_around_center(string):
    start = end = 0

    # TC: O(N^2), where N = len(string)
    for i in range(len(string) - 1):  # TC: O(N) * O(N + N) = O(N^2)
        lp1 = _expand_around_center(string, i, i)  # TC: O(N)
        lp2 = _expand_around_center(string, i, i + 1)  # TC: O(N)
        max_length = max(lp1, lp2)
        if max_length > end - start + 1:
            start = i - ((max_length - 1) // 2)
            end = i + (max_length // 2)
    return string[start:end + 1]


if __name__ == "__main__":
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("aa", "aa"),
        ("abaabc", "baab"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("abaabc", "baab"),
        ("madama", "madam"),
        ("jklollolkidding", "klollolk")
    ]

    for string, expected_result in test_cases:
        result = longest_palindrome_expand_around_center(string)
        print(string, result)
        assert result == expected_result
