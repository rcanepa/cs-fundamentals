"""Implement an algorithm that takes a string which represent
an integer, and return that integer as a number.

Examples:
    Input:  "123"
    Output: 123

    Input:  "-9023"
    Output: -9023

    Input:  "0"
    Output: 0

    Input:  "-0"
    Output: 0
"""


def stoi(s=""):

    n = len(s)

    if n == 0:
        raise Exception("you cannot transform an empty string to an integer")

    is_negative = s[0] == "-"
    starting_position = 1 if is_negative else 0

    result = 0

    for i in range(starting_position, n):
        result += (10 ** (n - i - 1)) * int(s[i])

    return result * -1 if is_negative else result


if __name__ == "__main__":
    test_cases = [
        ("123", 123),
        ("-9023", -9023),
        ("0", 0),
        ("-0", 0),
        ("9999999", 9999999),
        ("1", 1)
    ]

    for sn, expected in test_cases:
        assert stoi(sn) == expected
