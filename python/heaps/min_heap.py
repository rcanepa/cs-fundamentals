def _get_parent_index(child_index):
    if child_index == 0:
        return None
    return (child_index - 1) // 2


def _get_left_child_index(parent_index):
    return parent_index * 2 + 1


def _get_right_child_index(child_index):
    return child_index * 2 + 2


def _check_min_heap_invariant(min_heap):
    if min_heap.size == 0:
        return True

    storage = min_heap._storage

    def _check_index_invariant(index):
        parent_index = index
        child_index = _get_left_child_index(parent_index)

        if child_index < min_heap.size:
            if storage[parent_index] <= storage[child_index]:
                _check_index_invariant(child_index)
            else:
                raise Exception(
                    "Left child ({child}) is smaller than its parent ({parent}) [{storage}]!".format(
                        child=storage[child_index],
                        parent=storage[parent_index],
                        storage=storage
                    ))

        child_index += 1

        if child_index < min_heap.size:
            if storage[parent_index] <= storage[child_index]:
                _check_index_invariant(child_index)
            else:
                raise Exception(
                    "Right child ({child}) is smaller than its parent ({parent})!".format(
                        child=storage[child_index],
                        parent=storage[parent_index]
                    ))

        return True

    return _check_index_invariant(0)


class MinHeap(object):
    def __init__(self, initialization_list=None):
        self._storage = []
        initialization_list = initialization_list or []
        for value in initialization_list:
            self.insert(value)

    def __str__(self):
        return str(self._storage)

    def insert(self, value):
        """Insert in the heap and return the heap.

        The value is appended at the end of the list, and then
        it's 'bubbled up' until it reach its final position."""
        self._storage.append(value)
        current_index = len(self._storage) - 1
        parent_index = _get_parent_index(current_index)

        # Bubble up value.
        while self._is_index_valid(parent_index) and self._is_less(current_index, parent_index):
            self._swap(parent_index, current_index)
            current_index = parent_index
            parent_index = _get_parent_index(current_index)

        return self

    def remove(self):
        """Remove the min value of the heap and return it.

        After the top value is removed, the last value of the list
        is put on its position. Then, the value at the top is pushed down
        until it finds its final position."""
        if self.size == 0:
            return None

        # Swap last element with the top.
        self._swap(0, self.size - 1)
        removed = self._storage.pop()

        parent_index = 0
        child_index = _get_left_child_index(parent_index)

        while child_index < self.size:
            if self._is_index_valid(_get_right_child_index(parent_index)) \
                    and (self._is_gte(child_index, parent_index)
                         or self._is_less(child_index + 1, child_index)):
                child_index += 1

            if self._is_less(child_index, parent_index):
                self._swap(child_index, parent_index)
                parent_index = child_index
                child_index = _get_left_child_index(parent_index)
            else:
                break

        return removed

    def peek(self):
        return self._storage[0] if self.size > 0 else None

    @property
    def size(self):
        return len(self._storage)

    def _swap(self, origin, source):
        self._storage[origin], self._storage[source] = self._storage[source], self._storage[origin]

    def _is_less(self, index1, index2):
        if index1 >= self.size or index2 >= self.size:
            raise Exception(
                "Trying to access an invalid index on the list. "
                "Index1: {}, index2: {}, list size: {}.".format(
                    index1,
                    index2,
                    self.size
                )
            )

        return self._storage[index1] < self._storage[index2]

    def _is_index_valid(self, index):
        return False if index is None or index >= self.size else True

    def _is_gte(self, index1, index2):
        if index1 >= self.size or index2 >= self.size:
            raise Exception(
                "Trying to access an invalid index on the list. "
                "Index1: {}, index2: {}, list size: {}.".format(
                    index1,
                    index2,
                    self.size
                )
            )

        return self._storage[index1] >= self._storage[index2]


if __name__ == '__main__':
    heap = MinHeap([89, 82, -20, 200, 100, 1, 20])
    ordered_list = []
    while heap.size > 0:
        removed = heap.remove()
        ordered_list.append(removed)
