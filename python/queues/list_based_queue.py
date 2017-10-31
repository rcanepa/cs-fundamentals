"""Queue implementation using a list as the storage mechanism guaranteeing
that enqueueing and dequeueing have a time complexity of O(1).

To offer a time complexity of O(1) for enqueue and dequeue operations
a pointer to the current head of the queue is used, with that is it
unnecessary to perform a shift operation every time an element is
dequeued.
"""

MAX_GARBAGE_ITEMS = 200


class Queue(object):
    def __init__(self):
        self._storage = []
        self._head = 0
        self._size = 0

    def enqueue(self, item):
        if item is None:
            raise Exception("you cannot enqueue None")

        self._storage.append(item)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("you cannot dequeue from an empty queue")

        item = self._storage[self._head]
        self._head += 1
        self._size -= 1

        # After dequeueing MAX_GARBAGE_ITEMS elements,
        # clean the front of the list. This operation
        # is O(N), where N is the number of items in the
        # queue.
        if self._head == MAX_GARBAGE_ITEMS:
            self._storage = self._storage[self._head:]
            self._head = 0

        return item

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self.size == 0
