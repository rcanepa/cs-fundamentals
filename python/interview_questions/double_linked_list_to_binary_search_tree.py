"""Implement an algorithm that transform, in place, a sorted double
linked list into a balance binary search tree.

Examples:

    Input:  Doubly Linked List 1  2  3
    Output: A Balanced BST
         2
       /  \
      1    3


    Input: Doubly Linked List 1  2 3  4 5  6  7
    Output: A Balanced BST
            4
          /   \
         2     6
       /  \   / \
      1   3  4   7

    Input: Doubly Linked List 1  2  3  4
    Output: A Balanced BST
          3
        /  \
       2    4
     /
    1

    Input:  Doubly Linked List 1  2  3  4  5  6
    Output: A Balanced BST
          4
        /   \
       2     6
     /  \   /
    1   3  5
"""


class DLLNode(object):
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        return "DLLNode[{}]".format(self.value)


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode[{}]".format(self.value)


def size_of_dll(dll):
    if dll is None:
        return 0
    size = 0
    ptr = dll
    while ptr:
        ptr = ptr.next
        size += 1
    return size


def build_bst(dll):
    """Return a BST from sorted DLL.
    Time complexity: O(N), where N = len(dll).
    Space complexity: O(log(N)) ~ recursive stack calls (where log N is the height of the tree).
    :param dll: DLLNode
    :return: root: TreeNode
    """
    n = size_of_dll(dll)

    if n == 0:
        return None

    def build_subtree(subtree_nodes):
        if subtree_nodes <= 0:
            return None

        # Construct recursively the left subtree first.
        left_subtree_nodes = subtree_nodes // 2
        left_node = build_subtree(left_subtree_nodes)

        # Create the Tree Node.
        nonlocal dll
        tree_node = TreeNode(dll.value)

        # Advance the DLL pointer to the next element.
        dll = dll.next
        tree_node.left = left_node

        # Construct the right subtree. The total number of nodes in the right
        # subtree is equal to: total nodes - nodes in the left subtree - root node.
        right_subtree_nodes = subtree_nodes - left_subtree_nodes - 1
        tree_node.right = build_subtree(right_subtree_nodes)

        return tree_node

    root = build_subtree(n)

    return root


if __name__ == "__main__":
    head = DLLNode(1)
    ptr = head
    for value in range(2, 8):  # Create a DLL with 7 elements: 1-2-3-4-5-6-7
        ptr.next = DLLNode(value)
        ptr = ptr.next

    print("The DLL has", size_of_dll(head), "elements.")

    tree = build_bst(head)
    print(tree)
