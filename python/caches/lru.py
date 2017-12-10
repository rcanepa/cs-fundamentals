"""LRU Cache.
This implementation guaranteed O(1) time complexity for
get and put operations.

The underlaying structure uses a dictionary and a double
linked list.
"""


class LRUCache(object):
    class LinkedListNode(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.previous = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self._lru_list = None
        self._lhead = None
        self._ltail = None

    def __add
