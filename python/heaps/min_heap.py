def _get_parent_index(child_index):
    if child_index == 0:
        return None
    return (child_index - 1) // 2


def _get_left_child_index(parent_index):
    return parent_index * 2 + 1


def _get_right_child_index(child_index):
    return child_index * 2 + 2


class MinHeap(object):
    def __init__(self, initialization_list=None):
        self._storage = []
        initialization_list = initialization_list or []
        for value in initialization_list:
            self.insert(value)

    def __str__(self):
        return str(self._storage)

    def insert(self, value):
        self._storage.append(value)
        current_index = len(self._storage) - 1
        parent_index = _get_parent_index(current_index)
        while isinstance(parent_index, int) and self._storage[current_index] < self._storage[parent_index]:
            print("Replacing", self._storage[current_index], "with", self._storage[parent_index])
            self._storage[parent_index], self._storage[current_index] = self._storage[current_index], self._storage[parent_index]
            current_index = parent_index
            parent_index = _get_parent_index(current_index)
        return self

    def remove(self):
        pass

    def peek(self):
        pass


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(100)\
        .insert(200)\
        .insert(10)\
        .insert(500)\
        .insert(3)\
        .insert(30)\
        .insert(-3)\
        .insert(-10)
    print(heap)