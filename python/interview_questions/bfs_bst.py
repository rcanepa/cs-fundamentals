"""Print a BST in the following way:

Example of a BST:
            10
        5       15
     1   7   12  20
  -1       11     300
 -5
-10

Output:
10
5 15
1 7 12 20
-1 11 300
-5
-10

This should be accomplished using a Breadth First Search algorithm.
"""

from queue import Queue
from trees.binary_search_tree import BSTree


def print_list(l):
    print(" ".join(map(str, l)))


if __name__ == "__main__":
    values = [10, 5, 15, 1, 7, 12, 20, -1, 11, 300, -5, -10]
    tree = BSTree()
    for v in values:
        tree.insert(v)

    root_node = tree._root
    q = Queue()

    q.put((root_node, 0))
    printing_row = 0
    row_values = []

    while not q.empty():
        current_node, current_level = q.get()

        # If where are one level deeper, print row an clean `row_values`.
        if current_level != printing_row:
            printing_row += 1
            print_list(row_values)
            row_values = []

        # Add current node to the list of values to be printed.
        row_values.append(current_node.value)

        # Add children to the queue.
        if current_node.left:
            q.put((current_node.left, current_level + 1))
        if current_node.right:
            q.put((current_node.right, current_level + 1))
    print_list(row_values)

