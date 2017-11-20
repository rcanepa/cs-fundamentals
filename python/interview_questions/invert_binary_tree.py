"""Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


def invert_binary_tree(node):
    if node is None:
        return node

    new_right_subtree = invert_binary_tree(node.left)
    new_left_subtree = invert_binary_tree(node.right)

    node.left = new_left_subtree
    node.right = new_right_subtree

    return node
