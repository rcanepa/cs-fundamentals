"""Given an arbitrary ransom note string R and another string containing
all the contents of all the magazines M, write a function that will return
true if the ransom note can be made from the magazines; otherwise, it will
return false. In other words, return true if the string R can be made up
by the characters of the string M.

Example:
    R = "help me"
    M = "The metropolitan area will receive more than 1 million of tourists"
    => true

    R = "The wolf was called Alex"
    M = "The metropolitan area will receive more than 1 million of tourists"
    => false (there is no 'x' or 'd' in M)
"""

import collections


def ransom_note_from_magazines(text, note):
    """Return True if `note` can be constructed with the letters
    present in text.

    TC: O(N + M), where N = len(note) and M = len(text)
    SC: O(U), where U = len(set(note)) (unique letters on `note`)
    """
    if len(note) > len(text):
        return False

    letters_needed = collections.defaultdict(int)

    # TC: O(N), where N = len(note)
    # SC: O(U), where U = len(set(note))
    for c in note:
        letters_needed[c] += 1

    # TC: O(M), where M = len(text)
    for c in text:
        if c in letters_needed:
            letters_needed[c] -= 1
            if letters_needed[c] == 0:
                letters_needed.pop(c)
        if not letters_needed.keys():
            return True

    return False


if __name__ == "__main__":
    test_cases = [
        (
            "help me",
            "The metropolitan area will receive more than 1 million of tourists",
            True
        ),
        (
            "The wolf was called Alex",
            "The metropolitan area will receive more than 1 million of tourists",
            False
        ),
        (
            "",
            "The metropolitan area will receive more than 1 million of tourists",
            True
        ),
        (
            "The metropolitan area will receive more than 1 million of tourists",
            "The",
            False
        ),
        (
            "The metropolitan area will receive more than 1 million of tourists",
            "The metropolitan area will receive more than 1 million of tourists",
            True
        ),
        (
            "Xhe metropolitan area will receive more than 1 million of tourists",
            "The metropolitan area will receive more than 1 million of tourists",
            False
        )
    ]
    for ransom_note, magazine_text, expected in test_cases:
        assert ransom_note_from_magazines(magazine_text, ransom_note) == expected
