"""Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
    Can you solve it without using extra space?
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head):
    """If head is a linked list with a cycle, its entry point node is returned. If not,
    None is returned.
    Time Complexity: O(N), where N is the number of nodes of the linked list.
    Space Complexity: O(1).
    :param head: ListNode
    :return: entry: ListNode
    """
    slow = head
    fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        # If there is a cycle, at some point slow and fast should be equal.
        if slow == fast:

            # In that case, move head and slow until there are equal. That
            # node is the entry node.
            while slow != head:
                slow = slow.next
                head = head.next
            return slow

    return None


if __name__ == "__main__":
    """
    Linked list with a cycle starting at node "b"
            c - d
          /      \
     a - b        e
          \      /
           g - f 
    """
    a = ListNode("a")
    b = ListNode("b")
    c = ListNode("c")
    d = ListNode("d")
    e = ListNode("e")
    f = ListNode("f")
    g = ListNode("g")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = b

    entry_node = detect_cycle(a)
    assert entry_node == b

    ll = ListNode("a")
    ll.next = ListNode("b")
    ll.next.next = ListNode("c")
    assert detect_cycle(ll) is None

    ll = ListNode("a")
    ll.next = ListNode("b")
    ll.next.next = ListNode("c")
    ll.next.next.next = ll
    assert detect_cycle(ll) == ll
