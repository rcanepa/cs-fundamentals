"""Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square
brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square
brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k. For example, there won't be input
like 3a or 2[4].

Examples:

    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Ref:
    https://leetcode.com/contest/leetcode-weekly-contest-3/problems/decode-string/
"""


def decode_string(s):
    return s


if __name__ == "__main__":
    test_cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef")
    ]

    for encoded_s, decoded_s in test_cases:
        result = decode_string(encoded_s)
        assert result == decoded_s
