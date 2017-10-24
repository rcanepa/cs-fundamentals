import unittest
from strings.find_pattern_in_text_bruteforce import find_pattern_v1, find_pattern_v2


class FindPatternBruteForce(unittest.TestCase):
    def test_return_the_position_of_first_occurrence_v1(self):
        test_cases = [
            ("abracadabra", "bra"),
            ("aaaaaaab", "ab"),
            ("cxccc", "c"),
            ("this pattern is not a common pattern!", "!")
        ]
        for string, pattern in test_cases:
            self.assertEqual(find_pattern_v1(string, pattern), string.find(pattern))

    def test_return_the_position_of_first_occurrence_v2(self):
        test_cases = [
            ("abracadabra", "bra"),
            ("aaaaaaab", "ab"),
            ("cxccc", "c"),
            ("this pattern is not a common pattern!", "!")
        ]
        for string, pattern in test_cases:
            self.assertEqual(find_pattern_v2(string, pattern), string.find(pattern))

    def test_return_the_length_of_the_string_on_no_match_v1(self):
        test_cases = [
            ("abracadabra", "zbra"),
            ("aaaaaaab", "zab"),
            ("cxccc", "zc"),
            ("this pattern is not a common pattern!", "z!")
        ]
        for string, pattern in test_cases:
            self.assertEqual(find_pattern_v1(string, pattern), len(string))

    def test_return_the_length_of_the_string_on_no_match_v2(self):
        test_cases = [
            ("abracadabra", "zbra"),
            ("aaaaaaab", "zab"),
            ("cxccc", "zc"),
            ("this pattern is not a common pattern!", "z!")
        ]
        for string, pattern in test_cases:
            self.assertEqual(find_pattern_v2(string, pattern), len(string))
