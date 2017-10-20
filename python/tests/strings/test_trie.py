import unittest
from strings.trie import Trie


class TrieTest(unittest.TestCase):
    def test_insert_and_get_return_the_correct_value(self):
        trie = Trie()
        trie.insert("a", 10)
        self.assertEqual(trie.get("a"), 10)
        self.assertEqual(trie.get("ab"), None)
        trie.insert("b", 5)
        self.assertEqual(trie.get("ab"), None)
        self.assertEqual(trie.get("b"), 5)
        trie.insert("ab", 15)
        self.assertEqual(trie.get("ab"), 15)
        self.assertEqual(trie.get("qwerty"), None)
        self.assertEqual(trie.get("aa"), None)
        self.assertEqual(trie.get("ac"), None)
        trie.insert("qwerty", 100)
        self.assertEqual(trie.get("qwerty"), 100)
        self.assertEqual(trie.get("qwertyx"), None)
        self.assertEqual(trie.get("qwert"), None)

    def test_contains_return_true_on_success(self):
        trie = Trie()
        trie.insert("a", 10)
        self.assertTrue(trie.contains("a"))
        self.assertFalse(trie.contains("ab"))
        trie.insert("b", 5)
        self.assertFalse(trie.get("ab"))
        self.assertTrue(trie.get("b"))
        trie.insert("ab", 15)
        self.assertTrue(trie.get("ab"))
        self.assertFalse(trie.get("qwerty"))
        self.assertFalse(trie.get("aa"))
        self.assertFalse(trie.get("ac"))
        trie.insert("qwerty", 100)
        self.assertTrue(trie.get("qwerty"))
        self.assertFalse(trie.get("qwertyx"))
        self.assertFalse(trie.get("qwert"))