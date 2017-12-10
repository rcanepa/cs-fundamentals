class DoubleLinkedList(object):
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.previous = None
            self.next = None

        def __repr__(self):
            return "Node[{}]".format(value)

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self.size == 0

    def push_front(self, value):
        new_node = Node(value)
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
        self._size += 1
        return new_node

    def push_back(self, value):
        new_node = Node(value)
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.previous = self._tail
            self._tail = new_node
        self._size += 1
        return new_node

    def pop_front(self):
        if self._size == 0:
            raise Exception(
                "you cannot pop from an empty list"
            )
        ret = self._tail.value
        self._tail = self._tail.previous
        self._tail.next = None
        self._size -= 1
        return ret

    def pop_back(self):
        if self._size == 0:
            raise Exception(
                "you cannot pop from an empty list"
            )
        ret = self._head.value
        self._head = self._head.next
        self._tail.previous = None
        self._size -= 1
        return ret
