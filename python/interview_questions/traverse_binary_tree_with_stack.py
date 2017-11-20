"""Implement a binary tree traversal without using recursion.

Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N). This comes from the size of the stack."""


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse_with_stack(root):
    stack = [root]
    current = root.left
    while stack or current:
        # Traverse to the left
        while current:
            stack.append(current)
            current = current.left

        # Do the work
        current = stack.pop()
        yield current.value

        # Traverse to the right
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
    for value in traverse_with_stack(root):
        print("Visiting node =", value)

