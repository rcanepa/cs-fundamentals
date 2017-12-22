import unittest
from unittest.mock import patch
from oo.dictionary_with_expiration import DictWithExpiration


class TestDictionaryWithExpiration(unittest.TestCase):
    def setUp(self):
        self.dwe = DictWithExpiration()

    def tearDown(self):
        del self.dwe

    def test_put_and_get(self):
        self.dwe.put("abc", 123, 100000)
        self.assertEqual(self.dwe.get("abc"), 123)
        self.dwe.put("abc", 124, 100000)
        self.assertEqual(self.dwe.get("abc"), 124)

    def test_size(self):
        self.dwe.put("abc", 123, 100000)
        self.assertEqual(self.dwe.size, 1)
        self.dwe.put("abd", 124, 100000)
        self.dwe.put("abe", 125, 100000)
        self.dwe.put("abf", 126, 100000)
        self.assertEqual(self.dwe.size, 4)
        self.dwe.put("abf", 127, 100000)
        self.assertEqual(self.dwe.size, 4)

    def test_empty(self):
        self.assertTrue(self.dwe.empty())
        self.dwe.put("abf", 127, 100000)
        self.assertFalse(self.dwe.empty())

    # @patch('oo.dictionary_with_expiration.time.time')
    @patch('oo.dictionary_with_expiration.get_epoch_time')
    def test_expiration(self, get_epoch_time):
        get_epoch_time.return_value = 0
        self.dwe.put("a", 100, 100)
        self.assertEqual(self.dwe.get("a"), 100, "before expiration")
        self.assertEqual(self.dwe.size, 1)
        self.assertFalse(self.dwe.empty())

        get_epoch_time.return_value = 100
        self.assertEqual(self.dwe.get("a"), 100, "just on expiration")
        self.assertEqual(self.dwe.size, 1)
        self.assertFalse(self.dwe.empty())

        get_epoch_time.return_value = 101
        self.assertIsNone(self.dwe.get("a"), "after expiration")
        self.assertEqual(self.dwe.size, 0)
        self.assertTrue(self.dwe.empty())

    def test_put_duration_type_error(self):
        self.assertRaises(TypeError, self.dwe.put, "abc", 123, "duration")
        self.assertRaises(TypeError, self.dwe.put, "abc", 123, 12.3)
        self.assertRaises(TypeError, self.dwe.put, "abc", 123, {})
        self.assertRaises(TypeError, self.dwe.put, "abc", 123, None)

    def test_put_duration_value_error(self):
        self.assertRaises(ValueError, self.dwe.put, "abc", 123, -1)
        self.assertRaises(ValueError, self.dwe.put, "abc", 123, 0)


if __name__ == '__main__':
    unittest.main()
