"""
This file contains the implementation of a 'left-leaning'
Red Black Binary Search Tree (LLRBT). The implementation is based
on the one described on the book 'Algorithms Fourth Edition'
by Robert Sedgewick and Kevin Wayne.

A LLRBT is a Tree in which every Node have one of
two colors: red or black. The color of a Node represents
the color of the link between the Node and its parent.

Also, a LLRBT must satisfy the following conditions:
- Red links lean left (right red links are not allowed.)
- No node has two red links connected to it.
- The Tree has perfect black balance: every path from the
  root to a null link has the same number of black links.

http://algs4.cs.princeton.edu/33balanced/
"""

RED = True
BLACK = False


# Used to print trees in colors
TERM_RESET_COLOR = '\033[00m'
TERM_RED_COLOR = '\033[01;31m'


def is_red(node):
    """Return if `node` is red. None nodes considered black."""
    return False if node is None else node.color == RED


def is_black(node):
    """Return if `node` is black. None nodes considered black."""
    return True if node is None else node.color == BLACK


def _node_size(node):
    """Return the `node` size."""
    size = 0
    if node:
        size += 1
        if node.left:
            size += node.left.size
        if node.right:
            size += node.right.size
        return size
    return size


class LLRBT(object):

    class LLRBTNode(object):
        def __init__(self, value):
            self.value = value
            self.size = 1
            self.left = None
            self.right = None
            self.color = RED

        def __str__(self):
            def _print_value(node):
                """Return `node` value as a string. If the node is red,
                the value is represented as red."""
                if is_red(node):
                    return "{red_color}{value}{reset_color}".format(
                        red_color=TERM_RED_COLOR,
                        value=node.value,
                        reset_color=TERM_RESET_COLOR
                    )
                else:
                    return str(node.value)

            def _print(node, depth=0):
                """Recursively create a string representation of `node`. The
                representation flows from left to right.
                        300
                    200
                        150
                100
                        80
                    50
                        30
                """
                ret = ""
                if node.right:
                    ret += _print(node.right, depth + 1)
                ret += "\n" + ("    " * depth) + _print_value(node)
                if node.left:
                    ret += _print(node.left, depth + 1)
                return ret
            return _print(self, 0)

    def __init__(self, initialization_list=None):
        """Initialize the Tree and insert Nodes if an initialization list was given."""
        self._root = None
        self._size = 0
        if initialization_list:
            for v in initialization_list:
                self.insert(v)

    def __str__(self):
        return self._root.__str__() if self._root else ""

    def insert(self, value):
        """Return True if `value` was inserted, False otherwise.
        On repeated values it doesn't do anything.
        """
        def _insert(node):
            if node is None:
                return LLRBT.LLRBTNode(value), True
            if node.value > value:
                node.left, inserted = _insert(node.left)
            elif node.value < value:
                node.right, inserted = _insert(node.right)
            else:
                inserted = False
            node = LLRBT._balance(node)
            return node, inserted
        self._root, inserted = _insert(self._root)
        self._size = self._root.size
        self._root.color = BLACK
        return inserted

    def remove(self, value):
        """Remove a Node which contains the value `value` and return True
        if the value was found. It must handle three cases:
        Case 1: leaf node
                    -> delete it
        Case 2: one child
                    -> delete node and put its child in its place
        Case 3: two children
                    -> delete node and put its successor in its place
        """
        def _remove(node):
            if node.value == value:
                # Cases 1 and 2
                if not (node.left and node.right):
                    return node.left or node.right, True
                # Case 3
                else:
                    successor_parent, successor = node, node.right
                    while successor.left:
                        successor_parent, successor = successor, successor.left
                    successor.left = node.left
                    # The successor was found to the left of its right branch
                    if not successor_parent == node:
                        successor_parent.left = successor.right
                        successor.right = node.right
                    return successor, True
            elif node.value > value and node.left:
                node.left, removed = _remove(node.left)
            elif node.value < value and node.right:
                node.right, removed = _remove(node.right)
            else:
                removed = False
            node = LLRBT._balance(node)
            return node, removed
        if self._root:
            self._root, removed = _remove(self._root)
            self._size -= int(removed)
            return removed

    def remove_min(self):
        """Delete the smallest key from the tree and return True if succeeded.
        Deleting a black node could break the tree invariant, so we need to
        push down a red node until we get to the leaf node (the one to be deleted)."""
        def _remove_min(node):
            # This is the smallest key -> delete it
            if node.left is None:
                return None

            # Force left child to be red
            if is_black(node.left) and is_black(node.left.left):
                node = LLRBT._move_red_left(node)

            node.left = _remove_min(node.left)

            # On the way up, fix right leaning trees and 4-nodes
            return LLRBT._balance(node)

        if self._root:
            self._root = _remove_min(self._root)
            if self._root:
                self._size = self._root.size
                self._root.color = BLACK
            return True
        else:
            return False

    def remove_max(self):
        def _remove_max(node):
            # Make the left red node the root (move upwards the red)
            if is_red(node.left):
                node = LLRBT._rotate_right(node)

            # This is the greatest key -> delete it
            if node.right is None:
                return None

            if is_black(node.right) and node.right and is_black(node.right.left):
                node = LLRBT._move_red_right(node)

            node.right = _remove_max(node.right)

            return LLRBT._balance(node)
        if self._root:
            self._root = _remove_max(self._root)
            if self._root:
                self._size = self._root.size
                self._root.color = BLACK
            return True
        else:
            return False

    def contains(self, value):
        """Return True if `value` exists in the Tree."""
        def _contains(node):
            if node.value == value:
                return True
            if node.value > value and node.left:
                return _contains(node.left)
            if node.value < value and node.right:
                return _contains(node.right)
            return False
        if self._root:
            return _contains(self._root)
        return False

    def max(self):
        """Return the biggest value of the Tree."""
        node = self._root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.value

    def min(self):
        """Return the smallest value of the Tree."""
        node = self._root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.value

    def floor(self, value):
        """Return the floor element of `value`."""
        def _floor(node):
            if node is None:
                return None
            if node.value == value:
                return value
            if node.value > value:
                return _floor(node.left)
            if node.value < value:
                successor = _floor(node.right)
                return node if successor is None else successor
        return _floor(self._root)

    def ceiling(self, value):
        """Return the ceiling element of `value`."""
        def _ceiling(node):
            if node is None:
                return None
            if node.value == value:
                return value
            if node.value < value:
                return _ceiling(node.right)
            if node.value > value:
                ancestor = _ceiling(node.left)
                return node if ancestor is None else ancestor
        return _ceiling(self._root)

    def select(self, rank):
        """Return the key/value of rank k such that precisely k other
        keys in the BST are smaller than it."""
        def _select(node, rank):
            if node is None:
                return None
            if _node_size(node.left) == rank:
                return node.value
            if _node_size(node.left) > rank:
                return _select(node.left, rank)
            if _node_size(node.left) < rank:
                return _select(node.right, rank - _node_size(node.left) - 1)
        return _select(self._root, rank)

    def rank(self, value):
        """Return the rank of `value` in the Tree."""
        def _rank(node):
            if node is None:
                return 0
            if node.value == value:
                return _node_size(node.left)
            if node.value > value:
                return _rank(node.left)
            if node.value < value:
                return 1 + _node_size(node.left) + _rank(node.right)
        return _rank(self._root)

    def pre_order_traversal(self):
        """Return a generator to traverse the Tree in pre-order."""
        def _pre_order_traversal(node):
            if node is None:
                return
            yield node
            yield from _pre_order_traversal(node.left)
            yield from _pre_order_traversal(node.right)
        yield from _pre_order_traversal(self._root)

    def in_order_traversal(self):
        """Return a generator to traverse the Tree in in-order."""
        def _in_order_traversal(node):
            if node is None:
                return
            yield from _in_order_traversal(node.left)
            yield node
            yield from _in_order_traversal(node.right)
        yield from _in_order_traversal(self._root)

    def post_order_traversal(self):
        """Return a generator to traverse the Tree in post-order."""
        def _post_order_traversal(node):
            if node is None:
                return
            yield from _post_order_traversal(node.left)
            yield from _post_order_traversal(node.right)
            yield node
        yield from _post_order_traversal(self._root)

    @staticmethod
    def _rotate_left(node):
        """Perform a left rotation. Fix a right red link."""
        right_node = node.right
        node.right = right_node.left
        right_node.left = node
        right_node.color = node.color
        node.color = RED
        right_node.size = node.size
        node.size = _node_size(node)
        return right_node

    @staticmethod
    def _rotate_right(node):
        """Perform a left rotation. Fix a double left red link."""
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        left_node.color = node.color
        node.color = RED
        left_node.size = node.size
        node.size = _node_size(node)
        return left_node

    @staticmethod
    def _flip_colors(node):
        """Flip colors of `node` and its children."""
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    @staticmethod
    def _move_red_left(node):
        """Move a red child from the right to the left sub tree."""
        # Merge parent and children into a 4-node making their links red
        LLRBT._flip_colors(node)

        # Move red child from right branch to the left branch
        if node.right and is_red(node.right.left):
            node.right = LLRBT._rotate_right(node.right)
            node = LLRBT._rotate_left(node)
            LLRBT._flip_colors(node)
        return node

    @staticmethod
    def _move_red_right(node):
        # Merge parent and children into a 4-node making their links red
        LLRBT._flip_colors(node)
        if node.left and is_red(node.left.left):
            node = LLRBT._rotate_right(node)
            LLRBT._flip_colors(node)
        return node

    @staticmethod
    def _balance(node):
        """Restore LLRBT invariant by applying rotations and flipping colors."""
        # Fix a right leaning tree -> rotate left
        if is_black(node.left) and is_red(node.right):
            node = LLRBT._rotate_left(node)

        # 4-node on the left -> rotate right and flip colors
        if is_red(node.left) and is_red(node.left.left):
            node = LLRBT._rotate_right(node)

        # Split 4-node -> flip colors
        if is_red(node.left) and is_red(node.right):
            LLRBT._flip_colors(node)

        node.size = _node_size(node)
        return node

    def _validate_bst_invariant(self):
        """Validate that keys from left sub Tree are smaller than the key from the
        current node, and that keys from the right sub Tree are greater than the key
        from the current node."""
        def _validate_node(node):
            if node.left:
                if node.left.value < node.value:
                    _validate_node(node.left)
                else:
                    raise Exception(
                        "Invalid tree. root={}, left={}".format(
                            node.value,
                            node.left.value
                        )
                    )

            if node.right:
                if node.right.value > node.value:
                    _validate_node(node.right)
                else:
                    raise Exception(
                        "Invalid tree. root={}, right={}".format(
                            node.value,
                            node.right.value
                        )
                    )
            return True
        return _validate_node(self._root)

    @property
    def size(self):
        """Return the number of Nodes."""
        return self._size


if __name__ == "__main__":
    tree = LLRBT(["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"])
    print(tree)
