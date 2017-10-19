"""Trie Data Structure
"""


class Trie(object):

    class Node(object):
        def __init__(self, value=None):
            self.value = value
            self.links = [None] * Trie.R

        def __repr__(self):
            return "[Node {}]".format(self.value)

        def __str__(self):
            return self.__repr__()

    R = 256

    def __init__(self):
        self._root = Trie.Node("")

    def insert(self, key, value):
        def _insert(node, position):

            # The path isn't complete -> add a new Node.
            # The new node isn't necessary the end of the string.
            if node is None:
                node = Trie.Node()

            # This is the end of the path. Add value and return.
            if len(key) == position:
                node.value = value
                return node

            # Keep searching in the right link of the tree.
            next_link = Trie._get_char_code(key[position])
            node.links[next_link] = _insert(node.links[next_link], position + 1)
            return node

        self._root = _insert(self._root, 0)
        return self

    def get(self, key):
        if not key:
            raise Exception(
                "get requires a string key to perform a search."
            )

        def _get(node, position):
            if len(key) == position:
                return node.value
            next_link = Trie._get_char_code(key[position])
            return _get(node.links[next_link], position + 1) if node.links[next_link] else None
        return _get(self._root, 0)

    def contains(self, key):
        pass

    def remove(self, key):
        pass

    @staticmethod
    def _get_char_code(char):
        code = ord(char)
        if 256 < code or code < 0:
            raise Exception(
                "Char {} isn't allowed in this Trie. You must only"
                "use characters from the extended ASCII alphabet.".format(
                    char
                )
            )
        return code


if __name__ == "__main__":
    trie = Trie()
    trie.insert("a", 10)
    assert trie.get("a") == 10
    trie.insert("a", 11)
    assert trie.get("a") == 11
    trie.insert("b", 1)
    assert trie.get("b") == 1
    assert trie.get("c") == None
    trie.insert("ab", 50)
    assert trie.get("ab") == 50