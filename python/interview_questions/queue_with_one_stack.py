"""Implement a Queue with just one Stack."""


class Queue(object):
    def __init__(self):
        self._storage = []

    @property
    def size(self):
        return len(self._storage)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        self._storage.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("you cannot dequeue from an empty queue")

        def _dequeue():
            if self.size == 1:
                return self._storage.pop()

            current_element = self._storage.pop()
            result = _dequeue()
            self._storage.append(current_element)
            return result

        return _dequeue()


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
    assert q.is_empty() is False
    assert q.dequeue() == 4
    assert q.size == 0
    assert q.is_empty()

