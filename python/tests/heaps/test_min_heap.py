import unittest
from heaps.min_heap import MinHeap, _check_min_heap_invariant
from utils.arrays import create_random_array


class MinHeapTest(unittest.TestCase):
    def test_initialization_list(self):
        initialization_list = [100, 200, -1, 50, 90, 20, -30, 900]
        heap = MinHeap(initialization_list)
        self.assertEqual(heap.size, len(initialization_list))

    def test_insert_preserves_min_heap_property(self):
        heap = MinHeap()
        heap.insert(10)
        self.assertEqual(heap.peek(), 10)
        self.assertTrue(_check_min_heap_invariant(heap))
        heap.insert(-1)
        self.assertEqual(heap.peek(), -1)
        self.assertTrue(_check_min_heap_invariant(heap))
        heap.insert(-100)
        self.assertEqual(heap.peek(), -100)
        self.assertTrue(_check_min_heap_invariant(heap))
        heap.insert(100)
        self.assertEqual(heap.peek(), -100)
        self.assertTrue(_check_min_heap_invariant(heap))
        heap.insert(10)
        self.assertEqual(heap.peek(), -100)
        self.assertTrue(_check_min_heap_invariant(heap))
        heap.insert(-200)
        self.assertEqual(heap.peek(), -200)
        self.assertTrue(_check_min_heap_invariant(heap))
        heap.insert(-20)
        self.assertEqual(heap.peek(), -200)
        self.assertTrue(_check_min_heap_invariant(heap))
        heap.insert(400)
        self.assertEqual(heap.peek(), -200)
        self.assertTrue(_check_min_heap_invariant(heap))

    def test_remove_preserves_min_heap_property(self):
        initialization_list = [42, 78, 21, 78, 66, 66, 100, 200, -1, 50, 90, 20, -30, 900]
        heap = MinHeap(initialization_list)
        self.assertEqual(heap.size, len(initialization_list))
        self.assertEqual(heap.remove(), -30)
        self.assertTrue(_check_min_heap_invariant(heap))
        self.assertEqual(heap.size, len(initialization_list) - 1)
        self.assertEqual(heap.peek(), -1)
        self.assertEqual(heap.remove(), -1)
        self.assertTrue(_check_min_heap_invariant(heap))
        self.assertEqual(heap.size, len(initialization_list) - 2)
        self.assertEqual(heap.peek(), 20)

    def test_return_an_increasing_order_sequence(self):
        random_data = create_random_array(300)
        heap = MinHeap(random_data)
        ordered_list = []
        while heap.size > 0:
            removed = heap.remove()
            ordered_list.append(removed)
        self.assertEqual(ordered_list, sorted(random_data))

