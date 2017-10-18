import unittest
from strings.msd_string_sort import msd_sort


class MSDSort(unittest.TestCase):
    def setUp(self):
        self.licenses = [
            "4PGC938",
            "2IYE230",
            "3CI0720",
            "1ICK750",
            "1OHV845",
            "4JZY524",
            "1ICK750",
            "3CI0720",
            "1OHV845",
            "1OHV845",
            "2RLA629",
            "2RLA629",
            "3ATW723"
        ]

        self.unsorted_strings = [
            "are",
            "by",
            "sea",
            "seashells",
            "ar",
            "seashells",
            "sells",
            "sells",
            "she",
            "a",
            "she",
            "zorro",
            "shells",
            "shore",
            "surely",
            "the",
            "the",
        ]

    def test_fixed_length_strings_are_sorted(self):
        sorted_data = msd_sort(self.licenses)
        manually_sorted_data = sorted(self.licenses)
        self.assertEqual(sorted_data, manually_sorted_data)

    def test_variable_length_strings_are_sorted(self):
        sorted_data = msd_sort(self.unsorted_strings)
        manually_sorted_data = sorted(self.unsorted_strings)
        self.assertEqual(sorted_data, manually_sorted_data)