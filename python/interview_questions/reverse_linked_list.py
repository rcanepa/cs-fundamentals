"""Reverse a linked list in place iteratively and recursively.

Example:
    LL          = 1 -> 2 -> 3 -> 4
    Reversed LL = 1 <- 2 <- 3 <- 4
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_recursively(ll):
    head = None

    def traverse(ll):
        if ll.next is None:
            nonlocal head
            head = ll
            return ll

        previous = traverse(ll.next)
        previous.next = ll

        return ll
    tail = traverse(ll)
    tail.next = None
    return head


def reverse_iteratively(ll):
    previous = None
    current = ll
    following = current.next
    while following:
        current.next = previous
        previous = current
        current = following
        following = current.next
    current.next = previous
    return current


if __name__ == "__main__":
    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(4)
    ll1.next.next.next.next = ListNode(5)
    ptr = reverse_recursively(ll1)
    while ptr:
        print(ptr.val)
        ptr = ptr.next

    ll2 = ListNode(1)
    ll2.next = ListNode(2)
    ll2.next.next = ListNode(3)
    ll2.next.next.next = ListNode(4)
    ll2.next.next.next.next = ListNode(5)
    ptr = reverse_iteratively(ll2)
    while ptr:
        print(ptr.val)
        ptr = ptr.next
