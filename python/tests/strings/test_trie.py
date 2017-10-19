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
