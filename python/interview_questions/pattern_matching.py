"""Given a pattern and a string, return True if the string
follows the pattern and False otherwise.

Example 1:
    pattern = "aabb"
    string  = "househousesunsun"
    result  = True

Example 2:
    pattern = "aab"
    string  = "greenbluegreenblue"
    result  = False

Example 3:
    pattern = "aab"
    string  = "blueblueblack"
    result  = True
"""


# Recursive solution
# Keep the value of every letter of the pattern in a dictionary
# For pattern "aab" and string "househousesunsun"
# {
#   "a": "hou",
#   "b": "sehousesunsun"
# }

# Test pattern against the dictionary on every iteration


def is_valid_pattern(pattern, target, solution):
    for i in range(len(solution)):
        if target[i] != solution[i]:
            return False
    return True


def construct_output_string(pattern, solution):
    output = ""
    for c in pattern:
        output += solution.get(c, "")
    return output


def unique_pattern_values(solution):
    values = list(solution.values())
    return len(set(values)) == len(values)


def string_follows_pattern(string, pattern):
    number_characters = len(set(list(pattern)))
    result = None

    if len(pattern) > len(string):
        return result

    def _find_solution(solution, pattern_chars, str_index):
        output_string = construct_output_string(pattern, solution)
        nonlocal result

        if result:
            return

        if output_string == string and number_characters == len(solution.keys()) and unique_pattern_values(solution):
            result = solution

        elif not pattern_chars or len(output_string) > len(string) or str_index >= len(string):
            return

        elif pattern_chars:
            current_pattern_char = pattern_chars[0]

            if len(solution.get(current_pattern_char, "")) > 0:
                _find_solution({**solution}, pattern_chars[1:], str_index)

            if string[str_index] == string[str_index - 1] and str_index > 0:
                _find_solution({**solution}, pattern_chars, str_index + 1)

            solution[current_pattern_char] = solution.get(current_pattern_char, "") + string[str_index]
            _find_solution({**solution}, pattern_chars, str_index + 1)

    _find_solution({}, sorted(list(set(pattern))), 0)

    return result


if __name__ == "__main__":
    test_cases = [
        ("ab", "dogdog", True),
        ("abba", "dogdogdogdog", False),
        ("a", "b", True),
        ("abc", "xyz", True),
        ("aabb", "x" + "x" + "y" + "y", True),
        ("aabbcc", "x" + "x" + "y" + "y" + "t" + "t", True),
        ("abb", "blue" + "black" + "black", True),
        ("abab", "redblueredblue", True),
        ("abba", "catdogdogcat", True),
        ("abab", "redblueredblue", True),
        ("abab", "cat" + "dog" + "cat" + "dog", True),
        ("aba", "cat" + "dog" + "cat", True),
        ("abba", "cat" + "dog" + "dog" + "cat", True),
        ("abcac", "cat" + "dog" + "mouse" + "cat" + "mouse", True),
        ("abcde", "efghi", True),
        ("a", "efghi", True),
        ("abab", "cat" + "dog" + "cat" + "cat", False),
        ("abab", "cat" + "dog" + "cat" + "dogg", False),
        ("abab", "cat" + "do" + "cat" + "dog", False),
        ("abab", "cat" + "dog" + "cat", False),
        ("abba", "red" + "blue" + "red" + "blue", False),
        ("aba", "patrpatrr", False),
        ("abcdefghi", "cat", False),
        ("ab", "xy", True),
        ("aab", "green" + "blue" + "green" + "blue", False),
    ]

    for pattern, string, expect in test_cases:
        match = string_follows_pattern(string, pattern)
        if bool(match) == expect:
            print("ok ->", match)
        else:
            print("nok ->", match)
            break
