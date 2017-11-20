"""Traverse a binary tree in order, without using a stack or recursion.
It must be done in place.

Steps:
1. Initialize current as root
2. While current is not NULL
   If current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as right child of the rightmost
         node in current's left subtree
      b) Go to this left child, i.e., current = current->left
"""


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def morris_traversal(root):
    if root is None:
        return

    current = root
    while current:
        if current.left is None:
            print(current.value)
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

            # Make current as right child of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left
            # Revert the changes made in if part to restore the original
            # tree i.e., fix the right child of predecessor
            else:
                pre.right = None
                print(current.value)
                current = current.right


if __name__ == "__main__":
    """ 
    Constructed binary tree is
                1
              /   \
            2      3
          /  \
        4     5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    morris_traversal(root)
