"""
This file contains the implementation of a 'left-leaning'
Red Black Binary Search Tree. The implementation is based
on the one described on the book 'Algorithms Fourth Edition'
by Robert Sedgewick and Kevin Wayne.

A Red Black BST is a Tree in which every Node have one of
two colors: red or black. The color of a Node represents
the color of the link between the Node and its parent.

Also, a Red Black BST must satisfy the following conditions:
- Red links lean left (right red links are not allowed.)
- No node has two red links connected to it.
- The Tree has perfect black balance: every path from the
  root to a null link has the same number of black links.

http://algs4.cs.princeton.edu/33balanced/
"""
from enum import Enum


class NodeColor(Enum):
    BLACK = 0
    RED = 1


class RedBlackBSTNode(object):
    def __init__(self, value):
        self.value = value
        self.size = 1
        self.left = None
        self.right = None
        self.color = NodeColor.RED

    def is_red(self):
        return self.color == NodeColor.RED


def _node_size(node):
    """ Computes `node`'s size. """
    if node:
        return 1 + _node_size(node.left) + _node_size(node.right)
    else:
        return 0


class RedBlackBSTree(object):
    def __init__(self, initialization_list=None):
        self._root = None
        self._size = 0
        if initialization_list:
            for v in initialization_list:
                self.insert(v)

    def insert(self, value):
        def _insert(node):
            if node is None:
                return RedBlackBSTNode(value), True
            if node.value > value:
                node.left, inserted = _insert(node.left)
            elif node.value < value:
                node.right, inserted = _insert(node.right)
            else:
                inserted = False
            node = RedBlackBSTree._balance(node)
            return node, inserted
        self._root, inserted = _insert(self._root)
        self._size = self._root.size
        self._root.color = NodeColor.BLACK
        return inserted

    def remove(self, value):
        """
        Removes a Node which contains the value `value`.
        To remove a Node, three cases must be handled.
        Case 1: leaf node
                    -> delete it
        Case 2: node has one child
                    -> delete node and put its child in its place
        Case 3: node has two children
                    -> delete node and put its smallest child from its right branch in its place
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
            node = RedBlackBSTree._balance(node)
            return node, removed
        if self._root:
            self._root, removed = _remove(self._root)
            self._size -= int(removed)
            return removed

    def contains(self, value):
        """ Return True if `value` is found. """
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
        node = self._root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.value

    def min(self):
        node = self._root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.value

    def floor(self, value):
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
        """ Returns the key of rank k such that precisely k other
        keys in the BST are smaller. """
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
        """ Traverse tree in pre-order and apply `fn` to every Node value. """
        def _pre_order_traversal(node):
            if node is None:
                return
            yield node
            yield from _pre_order_traversal(node.left)
            yield from _pre_order_traversal(node.right)
        yield from _pre_order_traversal(self._root)

    def in_order_traversal(self):
        """ Traverse tree in in-order and apply `fn` to every Node value. """
        def _in_order_traversal(node):
            if node is None:
                return
            yield from _in_order_traversal(node.left)
            yield node
            yield from _in_order_traversal(node.right)
        yield from _in_order_traversal(self._root)

    def post_order_traversal(self):
        """ Traverse tree in post-order and apply `fn` to every Node value. """
        def _post_order_traversal(node):
            if node is None:
                return
            yield from _post_order_traversal(node.left)
            yield from _post_order_traversal(node.right)
            yield node
        yield from _post_order_traversal(self._root)

    @staticmethod
    def _rotate_left(node):
        right_node = node.right
        node.right = right_node.left
        right_node.left = node
        right_node.color = NodeColor.BLACK
        node.color = NodeColor.RED
        right_node.size = node.size
        node.size = _node_size(node)
        return right_node

    @staticmethod
    def _rotate_right(node):
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        left_node.color = NodeColor.BLACK
        node.color = NodeColor.RED
        left_node.size = node.size
        node.size = _node_size(node)
        return left_node

    @staticmethod
    def _flip_colors(node):
        node.color = NodeColor.RED
        node.left.color = NodeColor.BLACK
        node.right.color = NodeColor.BLACK

    @staticmethod
    def _balance(node):
        # Right child is red -> rotate left
        if node.right and node.right.is_red():
            node = RedBlackBSTree._rotate_left(node)

        # Two consecutive left children are red -> rotate right and flip colors
        if node.left and node.left.left and node.left.is_red() and node.left.left.is_red():
            node = RedBlackBSTree._rotate_right(node)
            RedBlackBSTree._flip_colors(node)

        # Children are red -> flip colors
        if node.left and node.right and node.left.is_red() and node.right.is_red():
            RedBlackBSTree._flip_colors(node)

        node.size = _node_size(node)
        return node

    def _validate_bstree(self):
        def _validate_node(node):
            if node.left:
                if node.left.value < node.value:
                    _validate_node(node.left)
                else:
                    raise Exception("Invalid tree. Parent={}, LeftChild={}".format(node.value, node.left.value))

            if node.right:
                if node.right.value > node.value:
                    _validate_node(node.right)
                else:
                    raise Exception("Invalid tree. Parent={}, RightChild={}".format(node.value, node.right.value))
            return True
        return _validate_node(self._root)

    @property
    def size(self):
        return self._size


if __name__ == "__main__":
    pass
