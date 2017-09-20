class _BSTNode(object):
    """ Node class used by the Binary Search Tree. """
    def __init__(self, value):
        self.value = value
        self.size = 1
        self.left = None
        self.right = None


def _node_size(node):
    """ Computes `node`'s size. """
    if node:
        return 1 + _node_size(node.left) + _node_size(node.right)
    else:
        return 0


class BSTree(object):
    """ Binary Search Tree implementation which doesn't allow repeated Nodes. """
    def __init__(self, initialization_list=None):
        self._root = None
        self._size = 0
        if initialization_list:
            for element in initialization_list:
                self.insert(element)

    def pre_order_traversal(self):
        """ Traverse tree in pre-order and apply `fn` to every Node value. """
        def _pre_order_traversal(node):
            if node is None:
                return
            yield node.value
            yield from _pre_order_traversal(node.left)
            yield from _pre_order_traversal(node.right)
        yield from _pre_order_traversal(self._root)

    def in_order_traversal(self):
        """ Traverse tree in in-order and apply `fn` to every Node value. """
        def _in_order_traversal(node):
            if node is None:
                return
            yield from _in_order_traversal(node.left)
            yield node.value
            yield from _in_order_traversal(node.right)
        yield from _in_order_traversal(self._root)

    def post_order_traversal(self):
        """ Traverse tree in post-order and apply `fn` to every Node value. """
        def _post_order_traversal(node):
            if node is None:
                return
            yield from _post_order_traversal(node.left)
            yield from _post_order_traversal(node.right)
            yield node.value
        yield from _post_order_traversal(self._root)

    @property
    def size(self):
        """ Returns the number of elements inside the BST. """
        return self._size

    def insert(self, value):
        """ Insert a Node. It Doesn't allow duplicated values. """
        def _insert(node):
            if node is None:
                return _BSTNode(value), True
            if node.value > value:
                node.left, inserted = _insert(node.left)
            elif node.value < value:
                node.right, inserted = _insert(node.right)
            else:
                inserted = False
            node.size = _node_size(node)
            return node, inserted
        self._root, inserted = _insert(self._root)
        self._size = self._root.size
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
            node.size = _node_size(node)
            return node, removed

        if self._root:
            self._root, removed = _remove(self._root)
            self._size -= int(removed)
            return removed

    def min(self):
        """ Returns the smallest element of the tree. """
        if self._root:
            node = self._root
            while node.left:
                node = node.left
            return node.value
        else:
            return None

    def max(self):
        """ Returns the biggest element of the tree. """
        if self._root:
            node = self._root
            while node.right:
                node = node.right
            return node.value
        else:
            return None

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


if __name__ == "__main__":
    tree = BSTree([100, 75, 150, 25, 90, 200, 120, 110, 125])
    print("Tree size:", tree.size)
    print("Inserting 20...", tree.insert(20))
    print("Inserting 20...", tree.insert(20))
    print("Tree size:", tree.size)
    print("Removing 20...", tree.remove(100))
    print("Tree size:", tree.size)

    traversal_generator = tree.pre_order_traversal()

    print("Value={}".format(next(traversal_generator)))
    print("Value={}".format(next(traversal_generator)))
    print("Value={}".format(next(traversal_generator)))
    print("Value={}".format(next(traversal_generator)))
    print("Value={}".format(next(traversal_generator)))


