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

    def test_remove_and_size(self):
        trie = Trie()
        trie.insert("a", 10)
        trie.insert("b", 5)
        trie.insert("ab", 15)
        trie.insert("qwerty", 100)
        self.assertEqual(trie.size, 4)
        trie.remove("b")
        self.assertFalse(trie.contains("b"))
        self.assertEqual(trie.size, 3)
        trie.remove("b")
        self.assertEqual(trie.size, 3)
        self.assertTrue(trie.contains("a"))
        trie.remove("a")
        self.assertFalse(trie.contains("a"))
        self.assertEqual(trie.size, 2)
        self.assertTrue(trie.contains("ab"))
        trie.remove("qwert")
        self.assertEqual(trie.size, 2)
        trie.remove("qwerty")
        self.assertEqual(trie.size, 1)
        self.assertEqual(trie.keys(), ["ab"])

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

    def test_find_keys_that_match(self):
        trie = Trie()
        trie.insert("abc", 1)
        self.assertEqual(trie.keys_that_match("abc"), ["abc"])
        self.assertEqual(trie.keys_that_match("abcx"), [])
        self.assertEqual(trie.keys_that_match("ab"), [])
        self.assertEqual(trie.keys_that_match("ab."), ["abc"])
        self.assertEqual(trie.keys_that_match("a.."), ["abc"])
        self.assertEqual(trie.keys_that_match("..."), ["abc"])
        self.assertEqual(trie.keys_that_match(".b."), ["abc"])
        self.assertEqual(trie.keys_that_match(".bc"), ["abc"])
        self.assertEqual(trie.keys_that_match("..c"), ["abc"])
        trie.insert("axc", 10)
        self.assertEqual(trie.keys_that_match("ab."), ["abc"])
        self.assertEqual(trie.keys_that_match("a.c"), ["abc", "axc"])
        self.assertEqual(trie.keys_that_match("..c"), ["abc", "axc"])
        trie.insert("txc", 100)
        self.assertEqual(trie.keys_that_match("..c"), ["abc", "axc", "txc"])
        self.assertEqual(trie.keys_that_match("..."), ["abc", "axc", "txc"])
        self.assertEqual(trie.keys_that_match("..."), ["abc", "axc", "txc"])
        self.assertEqual(trie.keys_that_match(".x."), ["axc", "txc"])
        self.assertEqual(trie.keys_that_match("t.."), ["txc"])

    def test_longest_prefix_key(self):
        trie = Trie()
        trie.insert("abc", 1)
        self.assertEqual(trie.longest_prefix_key("abc"), "")
        self.assertEqual(trie.longest_prefix_key("ab"), "")
        trie.insert("abcdefg", 10)
        self.assertEqual(trie.longest_prefix_key("abcdefg"), "abc")
        self.assertEqual(trie.longest_prefix_key("abc"), "")
        trie.insert("abcdefghi", 100)
        self.assertEqual(trie.longest_prefix_key("abcdefghi"), "abcdefg")
        trie.insert("abcdefgh", 200)
        self.assertEqual(trie.longest_prefix_key("abcdefghi"), "abcdefgh")
        trie.insert("abcx", 300)
        self.assertEqual(trie.longest_prefix_key("abcx"), "abc")