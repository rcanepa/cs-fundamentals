"""Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
    Given n will always be valid.
    Try to do this in one pass.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head, n):
    ptr0 = head
    ptr1 = head
    ptr2 = head
    ptr2_steps = 0

    while ptr2.next:
        ptr2 = ptr2.next
        ptr2_steps += 1

        if ptr2_steps >= n:
            ptr0 = ptr1
            ptr1 = ptr1.next

    ptr0.next = ptr1.next

    if ptr0 == ptr1:
        head = head.next

    return head


if __name__ == "__main__":
    n = 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    source = []
    ptr = head
    while ptr:
        source.append(ptr.val)
        ptr = ptr.next

    print(source)

    head = remove_nth_from_end(head, n)
    ptr = head
    result = []
    while ptr:
        result.append(ptr.val)
        ptr = ptr.next
    print(result)
