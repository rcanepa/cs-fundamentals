import unittest
from strings.three_way_quicksort import sort


class ThreeWayStringQuickSort(unittest.TestCase):
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
        licenses_copy = list(self.licenses)
        sort(licenses_copy)
        manually_sorted_data = sorted(self.licenses)
        self.assertEqual(licenses_copy, manually_sorted_data)

    def test_variable_length_strings_are_sorted(self):
        licenses_copy = list(self.unsorted_strings)
        sort(licenses_copy)
        manually_sorted_data = sorted(self.unsorted_strings)
        self.assertEqual(licenses_copy, manually_sorted_data)
