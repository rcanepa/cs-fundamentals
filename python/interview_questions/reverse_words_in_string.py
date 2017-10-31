"""Implement an algorithm which takes an string S and reverse the
order of all its words in linear time complexity.

Example:
    Input:  "my dog is awesome"
    Output: "awesome is dog my"

    Input:  "your algorithm is not fast enough"
    Output: "enough fast not is algorithm your"


    Step 1: Reverse the whole string. Time complexity: O(N), where
    N is the length of the string.

    "my dog is awesome"
     ^               ^
    "ey dog is awesomm"
      ^             ^
    "em dog is awesoym"
       ^           ^
    "emodog is awes ym"
        ^         ^
    "emosog is awed ym"
         ^       ^
    "emoseg is awod ym"
          ^     ^
    "emosew is agod ym"
           ^   ^
    "emosewais  god ym"
            ^ ^
    "emosewa si god ym"
             ^

    Step 2: Over the reversed string, reverse every word. A word
    is any group of characters separated by a space.

    "emosewa si god ym"
        ^
    "awesome si god ym"
             ^
    "awesome is god ym"
                 ^
    "awesome is dog ym"
                    ^
    "awesome is dog my"
"""


def reverse_string(s):
    """Return a new string with the content of `s` reversed."""
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)


def reverse_words(s):
    rw = ""
    rs = reverse_string(s)  # O(N), where N = len(s)
    last_space = 0

    # O(N) * O(W) ~ O(N^2), because sum(W1, ..., Wm) ~ N
    for index, char in enumerate(rs):  # O(N)
        if char == " ":
            # O(W), where W = len(rs[last_space: index])
            rw += reverse_string(rs[last_space: index]) + " "
            last_space = index + 1

    return rw + reverse_string(rs[last_space:])


if __name__ == "__main__":
    test_cases = [
        ("my dog is awesome", "awesome is dog my"),
        ("starbucks is not so good", "good so not is starbucks"),
        ("i like plain water", "water plain like i"),
        ("a", "a"),
        ("ab", "ab"),
        ("", "")
    ]

    for test_string, expected in test_cases:
        result = reverse_words(test_string)
        print("############## Test Case ##############")
        print("-> source:", test_string)
        print("-> result", result)
        assert result == expected
