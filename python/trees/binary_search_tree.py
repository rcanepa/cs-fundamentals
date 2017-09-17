class BSTNode(object):

    def __init__(self, value):
        self.value = value
        self.size = 1
        self.left = None
        self.right = None

    def compute_size(self):
        self.size = 1
        if self.left:
            self.size = self.size + self.left.size
        if self.right:
            self.size = self.size + self.right.size


class BSTree(object):
    def __init__(self):
        self.__root = None
        self.__size = 0

    def __pre_order_traversal(self, node, fn):
        if node is None:
            return
        fn(node.value)
        if node.left:
            self.__pre_order_traversal(node.left, fn)
        if node.right:
            self.__pre_order_traversal(node.right, fn)

    def pre_order_traversal(self, fn=None):
        if fn is None:
            def fn(x): return print(x)
        self.__pre_order_traversal(self.__root, fn)

    def __in_order_traversal(self, node, fn):
        if node is None:
            return
        if node.left:
            self.__in_order_traversal(node.left, fn)
        fn(node.value)
        if node.right:
            self.__in_order_traversal(node.right, fn)

    def in_order_traversal(self, fn=None):
        if fn is None:
            def fn(x): return print(x)
        self.__in_order_traversal(self.__root, fn)

    def __post_order_traversal(self, node, fn):
        if node is None:
            return
        if node.left:
            self.__post_order_traversal(node.left, fn)
        if node.right:
            self.__post_order_traversal(node.right, fn)
        fn(node.value)

    def post_order_traversal(self, fn=None):
        if fn is None:
            def fn(x): return

            print(x)
        self.__pre_order_traversal(self.__root, fn)

    def __insert(self, node, value):
        if node is None:
            return BSTNode(value)
        if node.value > value:
            node.left = self.__insert(node.left, value)
        elif node.value < value:
            node.right = self.__insert(node.right, value)
        node.compute_size()
        return node

    def insert(self, value):
        if self.__root is None:
            self.__root = BSTNode(value)
        else:
            self.__root = self.__insert(self.__root, value)
        self.__size = self.__root.size

    def __remove(self, node, value):
        if node.value == value:

            # Case 1
            if node.left is None and node.right is None:
                return None

            # Case 2
            elif node.left and node.right is None:
                return node.left

            # Case 2
            elif node.left is None and node.right:
                return node.right

            # Case 3
            else:
                parent_node = node
                smallest_node = node.right
                while smallest_node.left:
                    parent_node = smallest_node
                    smallest_node = smallest_node.left

                # The right Node is the smallest one
                if parent_node == node:
                    smallest_node.left = node.left

                # The smallest Node was found to the left of its right branch
                else:
                    parent_node.left = smallest_node.right
                    smallest_node.left = node.left
                    smallest_node.right = node.right
                return smallest_node

        elif node.value > value and node.left:
            node.left = self.__remove(node.left, value)

        elif node.value < value and node.right:
            node.right = self.__remove(node.right, value)

        node.compute_size()
        return node
    
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
        if self.__root:
            self.__root = self.__remove(self.__root, value)

    def __contains(self, node, value):
        if node.value == value:
            return True
        if node.value > value and node.left:
            return self.__contains(node.left, value)
        if node.value < value and node.right:
            return self.__contains(node.right, value)
        return False

    def contains(self, value):
        return self.__contains(self.__root, value)

    def size(self):
        return self.__size


if __name__ == "__main__":
    tree = BSTree()

    values = [100, 50, 150, 25, 75, 120, 200, 110, 115]

    for v in values:
        tree.insert(v)

    print("####")
    tree.pre_order_traversal()

    tree.remove(100)

    print("####")
    tree.pre_order_traversal()

