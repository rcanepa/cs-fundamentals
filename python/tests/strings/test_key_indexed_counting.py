import unittest
from collections import namedtuple
from strings.key_indexed_counting import key_indexed_counting_sort


Student = namedtuple("Student", ["name", "section"])


class KeyIndexedCountingTest(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student("Anderson", 2),
            Student("Brown", 3),
            Student("Davis", 3),
            Student("Garcia", 4),
            Student("Harris", 1),
            Student("Jackson", 3),
            Student("Johnson", 4),
            Student("Jones", 3),
            Student("Martin", 1),
            Student("Martinez", 2),
            Student("Miller", 2),
            Student("Moore", 1),
            Student("Robinson", 2),
            Student("Smith", 4),
            Student("Taylor", 3),
            Student("Thomas", 4),
            Student("Thompson", 4),
            Student("White", 2),
            Student("Williams", 3),
            Student("Wilson", 4)
        ]

    def test_items_are_sorted_by_key(self):
        sorted_data = key_indexed_counting_sort(self.students, "section")
        keys = [getattr(x, "section") for x in sorted_data]
        manually_sorted_keys = sorted([getattr(x, "section") for x in self.students])
        self.assertEqual(keys, manually_sorted_keys)

    def test_is_stable(self):
        sorted_data = key_indexed_counting_sort(self.students, "section")
        values = [getattr(x, "name") for x in sorted_data]

        # Sort data with the built-in Python sorting algorithm and compare results.
        self.students.sort(key=lambda s: s.section)

        # Get names.
        original_values = [s.name for s in self.students]
        self.assertEqual(values, original_values)
