"""Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def add_children(array, tree, low, high):
    if high < low:
        return None

    middle = (high + low) // 2

    tree = TreeNode(array[middle])

    tree.left = add_children(array, tree.left, low, middle - 1)
    tree.right = add_children(array, tree.right, middle + 1, high)
    return tree


class Solution:
    def sortedListToBST(self, head):
        numbers = []

        # TC: O(N), where N is the length of the linked list
        while head:
            numbers.append(head.val)
            head = head.next

        head = add_children(numbers, None, 0, len(numbers) - 1)

        return head
