"""Given a word W, find all anagrams of W. Consider that
you have access to a dictionary with all words.

Steps:
    1. Pre process the list of words:
        1.1 For each word W, sort W alphabetically
        1.2 Insert the sorted version of W in the dictionary along
            with its 'unsorted' version.
    2. For every anagram search, sort de input word and check if the
        sorted version exists in the anagrams dictionary.
"""

from collections import defaultdict


class Anagrams(object):
    def __init__(self, words=None):
        """The pre-processing step have a time complexity of
        O(N * W * log(W)), where N is the number of words and
        W is the average length of every word."""
        self._anagrams = defaultdict(list)
        if words is not None:
            for word in words:  # O(N)
                sw = "".join(sorted(word))  # O(W * log(W))
                if sw != word:
                    self._anagrams[sw].append(word)

    def get_anagrams(self, word):
        """Time complexity: O(W * log(W)), where W is the
        length of word."""
        return self._anagrams["".join(sorted(word))]

    def add_word(self, word):
        """Time complexity: O(W * log(W)), where W is the
        length of word."""
        self._anagrams["".join(sorted(word))].append(word)
        return self


if __name__ == "__main__":
    words = [
        "angel",
        "angle",
        "glean",
        "hoes",
        "hose",
        "shoe",
        "blue",
        "lube",
        "earn",
        "gear",
        "near",
        "rage",
    ]
    anagrams = Anagrams(words)
    anagrams.add_word("with").add_word("whit")

    test_cases = [
        ("angel", {"angel", "angle", "glean"}),
        ("abc", set([])),
        ("hose", {"hose", "hoes", "shoe"})
    ]

    for w, expected in test_cases:
        assert set(anagrams.get_anagrams(w)) == expected
