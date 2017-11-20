"""Given a string S, find the character which appear most times
in a consecutive way.

Example:
    input   "acswsaabcwabbbc"
    output  ("b", 3)

    input   "abcaa"
    output  ("a", 2)

    input   "a"
    output  ("a", 1)
"""


def consecutive_char(string):

    back = 0
    times = 1
    selected_char = string[back]
    selected_char_times = 1
    for front in range(1, len(string)):
        if string[back] == string[front]:
            times += 1
        else:
            if times > selected_char_times:
                selected_char_times = times
                selected_char = string[back]
        times = 1
        back += 1

    return selected_char, selected_char_times


if __name__ == "__main__":
    test_cases = [
        ("acswsaabcwabbbc", ("b", 3)),
        ("abcaa", ("a", 2)),
        ("a", ("a", 1))
    ]

    for input_string, expected_result in test_cases:
        result = consecutive_char(input_string)
        assert result == expected_result