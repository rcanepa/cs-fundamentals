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

    def test_size_return_the_number_of_keys(self):
        trie = Trie()
        trie.insert("a", 10)
        self.assertEqual(trie.size, 1)
        trie.insert("b", 5)
        self.assertEqual(trie.size, 2)
        trie.insert("ab", 15)
        self.assertEqual(trie.size, 3)

    def test_is_empty(self):
        trie = Trie()
        self.assertTrue(trie.is_empty())
        trie.insert("a", 10)
        self.assertFalse(trie.is_empty())
        trie.insert("b", 5)
        self.assertFalse(trie.is_empty())
        trie.insert("ab", 15)
        self.assertFalse(trie.is_empty())

    def test_contains_return_true_on_success(self):
        trie = Trie()
        trie.insert("a", 10)
        self.assertTrue(trie.contains("a"))
        self.assertFalse(trie.contains("ab"))
        trie.insert("b", 5)
        self.assertFalse(trie.contains("ab"))
        self.assertTrue(trie.contains("b"))
        trie.insert("ab", 15)
        self.assertTrue(trie.contains("ab"))
        self.assertFalse(trie.contains("qwerty"))
        self.assertFalse(trie.contains("aa"))
        self.assertFalse(trie.contains("ac"))
        trie.insert("qwerty", 100)
        self.assertTrue(trie.contains("qwerty"))
        self.assertFalse(trie.contains("qwertyx"))
        self.assertFalse(trie.contains("qwert"))

    def test_keys_return_all_words(self):
        trie = Trie()
        words = ["a", "haus", "straße", "mann", "frau", "kinder", "bier"]
        for i, w in enumerate(words):
            trie.insert(w, i)
        words_found = trie.keys()
        self.assertEqual(set(words), set(words_found))

    def test_keys_return_all_words_sorted(self):
        trie = Trie()
        words = [
            "flughafen",
            "a",
            "haus",
            "straße",
            "schwarz",
            "kindergarten",
            "berlin",
            "bär",
            "mann",
            "frau",
            "flugzeug",
            "kinder",
            "bier",
            "bahnhof"
        ]
        for i, w in enumerate(words):
            trie.insert(w, i)
        keys = trie.keys()
        self.assertEqual(keys, sorted(words))

    def test_find_keys_with_prefix(self):
        trie = Trie()
        words = [
            "flughafen",
            "a",
            "haus",
            "straße",
            "schwarz",
            "kindergarten",
            "berlin",
            "bär",
            "mann",
            "frau",
            "flugzeug",
            "kinder",
            "bier",
            "bahnhof"
         ]
        for i, w in enumerate(words):
            trie.insert(w, i)
        self.assertTrue(len(trie.keys_with_prefix("s")) == 2)
        self.assertEqual(trie.keys_with_prefix("s"), ["schwarz", "straße"])
        self.assertTrue(len(trie.keys_with_prefix("f")) == 3)
        self.assertEqual(trie.keys_with_prefix("f"), ["flughafen", "flugzeug", "frau"])
        self.assertTrue(len(trie.keys_with_prefix("x")) == 0)
        self.assertEqual(trie.keys_with_prefix("x"), [])
