import unittest
from strings.lsd_string_sort import lsd_sort


class LSDSort(unittest.TestCase):
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

    def test_strings_are_sorted(self):
        sorted_data = lsd_sort(self.licenses)
        manually_sorted_data = sorted(self.licenses)
        self.assertEqual(sorted_data, manually_sorted_data)