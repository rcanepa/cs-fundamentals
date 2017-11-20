"""Implement an algorithm that takes a BST and transform it into a
circular double linked list. The transformation must be done in place.

BST:
            4
        2       6
    1         5    10

CDLL:
      ______________________
     /                      \
    1 <> 2 <> 4 <> 5 <> 6 <> 10
     \______________________/
    (1 is connected to 10)
"""


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def make_double_linked_list(tree):
    """Return a circle double linked list from a binary search tree.
    The space complexity of this algorithm is O(N) in the worst case,
    and O(log(N)) in the case of a balanced tree.
    The time complexity is O(N).
    :param tree: TreeNode
    :return: TreeNode
    """
    tail = None
    previous = None

    def _traverse_inorder(node):
        if node is None:
            return

        _traverse_inorder(node.left)

        nonlocal previous

        if previous:
            node.left = previous
            previous.right = node
        previous = node

        nonlocal tail
        if tail is None:
            tail = node

        _traverse_inorder(node.right)

    _traverse_inorder(tree)

    print("At the end of the process, tail points to:", tail.value)
    print("At the end of the process, previous points to:", previous.value)

    tail.left = previous
    previous.right = tail

    return previous


if __name__ == "__main__":
    """ 
    Constructed binary tree is
                10
              /   \
            6     15
          /  \      \
        4     7     20
         \
          5
    """

    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(15)
    root.right.right = TreeNode(20)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.right = TreeNode(7)

    head = make_double_linked_list(root)

    ptr = head.right
    c = 10
    while c > 0:
        print(ptr.value)
        ptr = ptr.right
        c -= 1

    ll = make_double_linked_list(TreeNode(10))

    assert ll.left == ll and ll.right == ll

