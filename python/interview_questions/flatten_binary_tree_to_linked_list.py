"""Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_ll(ll):
    values = []
    ptr = ll
    while ptr:
        values.append(ptr.val)
        ptr = ptr.right
    print(values)


def build_linked_list(binary_tree):
    """Transform a binary tree in a linked list. The transformation is made
    traversing the binary tree pre order. We keep track of the previous node,
    so we can link the previous node to the current node by the right pointer
    of the previous node.

    previous node --- right --> current node

    Time Complexity: O(N), where N is the number of nodes in the binary tree.
    Space Complexity: O(N) in the worst case and O(log(N)) in the best case (balanced BT).

    :param binary_tree: TreeNode
    :return: head: TreeNode
    """
    previous = None  # reference to the last visited node.

    def pre_order(node):
        if node is None:
            return

        # Node's links are going to be mutated so we save a reference.
        node_left = node.left
        node_right = node.right
        node.left = None

        # Make the previous node right pointer point to the current.
        nonlocal previous
        if previous:
            previous.right = node

        # Set the previous as the current after all work is done.
        previous = node

        # Recurse to the left node using the node_left reference.
        pre_order(node_left)

        # Recurse to the right node using the node_right reference.
        pre_order(node_right)

    pre_order(binary_tree)


def flatten_binary_tree(binary_tree):
    """Flatten a binary tree into a linked list by taking the
    left right most node, and then connecting it to the right node of the
    head.

    Time Complexity: O(N), where N is the number of nodes in the tree.
    Space Complexity: O(1).

    Initial tree
                1
            2       5
          3  4       6
    
    First iteration (head on node 1)
                1
                  2
                3   4
                      5
                        6
    Last iteration (head on node 2)
                1
                  2
                    3
                      4
                        5
                          6
    """
    head = binary_tree

    while head:

        if head.left:
            target = head.left

            while target.right:
                target = target.right

            target.right = head.right
            head.right = head.left
            head.left = None

        head = head.right


if __name__ == "__main__":
    bt1 = TreeNode(1)
    bt1.left = TreeNode(2)
    bt1.right = TreeNode(5)
    bt1.left.left = TreeNode(3)
    bt1.left.right = TreeNode(4)
    bt1.right.right = TreeNode(6)

    build_linked_list(bt1)
    print_ll(bt1)

    bt2 = TreeNode(1)
    bt2.left = TreeNode(2)
    build_linked_list(bt2)
    print_ll(bt2)

    bt3 = TreeNode(1)
    bt3.left = TreeNode(2)
    bt3.right = TreeNode(5)
    bt3.left.left = TreeNode(3)
    bt3.left.right = TreeNode(4)
    bt3.right.right = TreeNode(6)
    flatten_binary_tree(bt3)
    print_ll(bt3)

    bt4 = TreeNode(1)
    bt4.left = TreeNode(2)
    flatten_binary_tree(bt4)
    print_ll(bt4)
