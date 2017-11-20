"""Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.

For example:
    Given the below binary tree,
       1
      / \
     2   3
    Return 6.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = None

    def find_max(self, root):
        """`max_node_in_path` holds the max value as if root is not the top
        most node of the path.
        On the other hand, `max_node_top` holds the max value as if root
        is the top most node of the path, meaning, all the other nodes of
        the path are below root."""
        if root is None:
            return 0

        left_tree_max = self.find_max(root.left)
        right_tree_max = self.find_max(root.right)
        node_in_path_max = max(left_tree_max + root.val, right_tree_max + root.val, root.val)
        node_top_max = max(node_in_path_max, left_tree_max + right_tree_max + root.val)
        if self.res is None:
            self.res = node_top_max
        else:
            self.res = max(self.res, node_top_max)
        return node_in_path_max

    def max_path_sum(self, root):
        self.find_max(root)
        return self.res


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    tm3 = TreeNode(-3)
    t1.left = t2
    t1.right = tm3

    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t2.left = t4
    t2.right = t5

    t6 = TreeNode(6)
    tm7 = TreeNode(-7)
    tm3.left = t6
    tm3.right = tm7

    t26 = TreeNode(6)
    tm1 = TreeNode(-1)
    t4.left = t26
    t4.right = tm1

    t2m3 = TreeNode(-3)
    t5.right = t2m3

    s = Solution()
    print(s.max_path_sum(t1))
