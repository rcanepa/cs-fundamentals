"""Implement a Queue with two Stacks as the storage.

Time Complexity: O(1) for size, is_empty and enqueue. However, the TC of dequeue
can vary depending on whether the dequeue stack is empty or not. If the dequeue
empty is empty, then the TC will be O(N). If not, the TC will be O(1).
Space Complexity: O(N), where N is the number of elements inside the queue.
"""


class Queue(object):
    def __init__(self):
        self._enqueue_stack = []
        self._dequeue_stack = []
        self._size = 0

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, item):
        self._enqueue_stack.append(item)
        self._size += 1

    def dequeue(self):
        if not self._dequeue_stack and not self._enqueue_stack:
            raise Exception("you cannot dequeue from an empty queue")

        if len(self._dequeue_stack) == 0:
            while len(self._enqueue_stack) > 0:
                self._dequeue_stack.append(self._enqueue_stack.pop())

        self._size -= 1
        return self._dequeue_stack.pop()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(100)
    q.enqueue(20)
    q.enqueue(3000)
    q.enqueue(4)

    assert q.size == 4
    assert q.dequeue() == 100
    assert q.size == 3
    assert q.dequeue() == 20
    assert q.size == 2
    assert q.dequeue() == 3000
    assert q.size == 1
    q.enqueue(55)
    assert q.is_empty() is False
    assert q.size == 2
    assert q.dequeue() == 4
    assert q.size == 1
    q.enqueue(57)
    q.enqueue(58)
    assert q.size == 3
    assert q.dequeue() == 55
    assert q.dequeue() == 57
    assert q.size == 1
    assert q.dequeue() == 58
    assert q.size == 0
    assert q.is_empty()
