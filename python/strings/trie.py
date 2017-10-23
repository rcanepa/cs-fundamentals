"""Trie (radix tree / prefix tree).
"""

UPDATE = 2
INSERT = 1


class Trie(object):

    class Node(object):
        def __init__(self, value=None):
            self.value = value
            self.links = [None] * Trie.R

        def __repr__(self):
            return "[Node {}]".format(self.value)

        def __str__(self):
            return self.__repr__()

    R = 256  # radix / size of the alphabet allowed

    def __init__(self):
        self._root = Trie.Node(None)
        self._n = 0

    def insert(self, key, value):
        """Insert `value` associated with key `key` in the Trie. If `key` was
        already part of the Trie, its value gets replaced."""
        def _insert(node, position):

            # The path isn't complete -> add a new Node.
            # The new node isn't necessary the end of the string.
            if node is None:
                node = Trie.Node()

            # This is the end of the path. Add value and return.
            if len(key) == position:
                operation = UPDATE if node.value is not None else INSERT
                node.value = value
                return node, operation

            # Still not the end of the path, keep searching in the right link of the tree.
            next_link = Trie._get_char_code(key[position])
            node.links[next_link], operation = _insert(node.links[next_link], position + 1)
            return node, operation

        self._root, operation_performed = _insert(self._root, 0)
        if operation_performed == INSERT:
            self._n += 1
        return self

    @property
    def size(self):
        """Return the number of inserted keys."""
        return self._n

    def is_empty(self):
        """Return True if there is no key in the Trie."""
        return self.size == 0

    def get(self, key):
        """Return a node's value if the key exists in the Trie. None otherwise."""
        if not key:
            raise Exception(
                "get requires a string key to perform a search."
            )

        node = Trie._get(key, self._root, 0)
        return node.value if node else node

    def contains(self, key):
        """Return True is key is present on the Trie or false otherwise."""
        if not key:
            raise Exception(
                "contains requires a string key to perform a search."
            )

        def _contains(node, position):
            # There isn't a path for the key (=> the key doesn't exist).
            if node is None:
                return False

            # The end of the path was reached. If there is a value, the key exists.
            if len(key) == position:
                return True if node.value else False

            # The end of the path hasn't been reached (=> keep searching).
            return _contains(node.links[Trie._get_char_code(key[position])], position + 1)

        return _contains(self._root, 0)

    def keys(self):
        """Return a list with all keys present in the Trie."""
        return Trie._collect_keys(self._root)

    def keys_with_prefix(self, prefix):
        """Return a list with all keys prefixed by `prefix`."""
        keys = []
        prefix_root_node = Trie._get(prefix, self._root, 0)
        if prefix_root_node:
            keys = [prefix + key for key in Trie._collect_keys(prefix_root_node)]
        return keys

    @staticmethod
    def _get(key, node, position):
        """Return the node that match key `key`."""
        if len(key) == position:
            return node
        next_link = Trie._get_char_code(key[position])
        return Trie._get(key, node.links[next_link], position + 1) if node.links[next_link] else None

    @staticmethod
    def _collect_keys(root_node):
        """Return a list with all keys sorted alphabetically starting from `root_node`.
        The Trie is traversed in a in-order way using DFS. A string is a keys only if it
        has a value associated."""
        keys = []

        def _collect(node, path=""):
            if node.value is not None:
                keys.append(path)

            for r in range(Trie.R):
                next_node = node.links[r]
                if next_node:
                    _collect(next_node, path + chr(r))

        _collect(root_node)

        return keys

    def keys_that_match(self, pattern):
        """Return all keys that match `pattern`."""
        keys = []

        def _collect(node, path=""):
            if node.value is not None and len(path) == len(pattern):
                keys.append(path)

            if len(path) == len(pattern):
                return None

            current_char = pattern[len(path)]
            if current_char == ".":
                for r in range(Trie.R):
                    next_node = node.links[r]
                    if next_node:
                        _collect(next_node, path + chr(r))
            else:
                next_node = node.links[ord(current_char)]
                if next_node:
                    _collect(next_node, path + current_char)

        _collect(self._root)

        return keys

    def longest_prefix_key(self, key):
        """Return the longest key that is smaller than `key` (its longest
        prefix)."""
        prefix_keys = []

        def find_prefix_keys(node, position=0, path=""):
            if len(path) == len(key):
                return None

            if node.value is not None:
                prefix_keys.append(path)

            current_char = key[position]
            next_link = ord(current_char)

            if node.links[next_link]:
                find_prefix_keys(node.links[next_link], position + 1, path + current_char)

        find_prefix_keys(self._root)
        return prefix_keys.pop() if prefix_keys else ""

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
    words = ["a", "haus", "straße", "schwarz", "berlin", "bär", "mann", "frau", "flugzeug", "kinder", "bier"]
    for i, w in enumerate(words):
        trie.insert(w, i)
    print(trie.keys_with_prefix("s"))
