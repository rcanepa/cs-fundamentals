"""Write a function that can decode a string pattern like the following:

    Examples:

        pattern: ab2[xy]
        decoded: abxyxy

        pattern: abc2[xy3[rt]wv]xyz
        decoded: abcxyrtrtrtwvxyrtrtrtwvxyz

        pattern: ab2[xy]tv3[a2[e]]
        decoded: abxyxytvaeeaeeaee"

        pattern: ab10[x]
        decoded: abxxxxxxxxxx
"""

from string import ascii_letters, digits


def decode(pattern, index=0):
    current_string = ""
    multiplier = 1
    while index < len(pattern):
        c = pattern[index]
        index += 1
        if c in ascii_letters:
            current_string += c
        elif c in digits:
            start = index - 1
            while index < len(pattern) and pattern[index] in digits:
                index += 1
            multiplier = int(pattern[start:index])
        elif c == "]":
            return index, current_string
        elif c == "[":
            sub_index, sub_pattern = decode(pattern[index:])
            index += sub_index
            current_string += sub_pattern * multiplier
    return current_string


if __name__ == "__main__":
    test_cases = [
        (
            "ab2[xy]rg",
            "abxyxyrg"
        ),
        (
            "ab2[xy]rg",
            "abxyxyrg"
        ),
        (
            "abc2[xy3[rt]wv]xyz",
            "abcxyrtrtrtwvxyrtrtrtwvxyz"
        ),
        (
            "ab2[xy]tv3[a2[e]]",
            "abxyxytvaeeaeeaee"
        ),
        (
            "ab10[x]",
            "abxxxxxxxxxx"
        ),
        (
            "10[x]",
            "xxxxxxxxxx"
        ),
        (
            "10[x1[a]]",
            "xaxaxaxaxaxaxaxaxaxa"
        ),
        (
            "3[a]2[bc]",
            "aaabcbc"
        ),
        (
            "3[a2[c]]",
            "accaccacc"
        ),
        (
            "2[abc]3[cd]ef",
            "abcabccdcdcdef"
        )
    ]

    for input_pattern, expected_result in test_cases:
        result = decode(input_pattern)
        print(input_pattern, expected_result, result)
        assert result == expected_result
