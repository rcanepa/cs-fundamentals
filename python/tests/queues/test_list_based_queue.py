import unittest
from queues.list_based_queue import Queue


class QueueTest(unittest.TestCase):
    def test_added_items_can_be_retrieved_in_correct_order(self):
        q = Queue()
        self.assertEqual(q.size, 0)
        q.enqueue(100)
        self.assertEqual(q.size, 1)
        q.enqueue(300)
        q.enqueue(20)
        q.enqueue(400)
        self.assertEqual(q.size, 4)
        self.assertEqual(q.dequeue(), 100)
        self.assertEqual(q.size, 3)
        self.assertEqual(q.dequeue(), 300)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 20)
        self.assertEqual(q.dequeue(), 400)
        self.assertEqual(q.size, 0)
        self.assertTrue(q.is_empty())

    def test_enqueueing_none_raises(self):
        q = Queue()
        self.assertRaises(Exception, lambda: q.dequeue())

    def test_dequeueing_on_empty_queue_raises(self):
        q = Queue()
        self.assertRaises(Exception, lambda: q.enqueue())
