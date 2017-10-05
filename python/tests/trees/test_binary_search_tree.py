import unittest
from trees.binary_search_tree import BSTree
from utils.arrays import create_random_array


class BSTreeTest(unittest.TestCase):
    def test_initialization_list(self):
        initialization_list = [100, 20, 200, 400]
        tree = BSTree(initialization_list)
        self.assertEqual(tree.size, len(initialization_list))

    def test_bst_size(self):
        tree = BSTree()
        self.assertEqual(tree.size, 0)
        tree.insert(100)
        self.assertEqual(tree.size, 1)
        tree.insert(200)
        tree.insert(50)
        self.assertEqual(tree.size, 3)
        tree.remove(100)
        self.assertEqual(tree.size, 2)

    def test_does_not_insert_repeated_values(self):
        tree = BSTree()
        tree.insert(100)
        tree.insert(100)
        self.assertEqual(tree.size, 1)

    def test_inserts_return_boolean_result(self):
        tree = BSTree()
        self.assertTrue(tree.insert(100))
        self.assertFalse(tree.insert(100))

    def test_removes_return_boolean_result(self):
        tree = BSTree([100, 75, 125])
        self.assertTrue(tree.remove(100))
        self.assertFalse(tree.remove(100))

    def test_removing_root_promotes_successor(self):
        tree = BSTree([100, 75, 50, 95, 125, 150, 110])
        tree.remove(100)
        root = next(tree.pre_order_traversal())
        self.assertEqual(root.value, 110)

    def test_removing_min_until_empty(self):
        initialization_list = [100, 75, 125, -30, 150, 40, 20, 130]
        tree = BSTree(initialization_list)
        removed_values = []
        while tree.size > 0:
            min_value = tree.min()
            removed_values.append(min_value)
            tree.remove(min_value)
        self.assertEqual(removed_values, sorted(initialization_list))

    def test_contains_value(self):
        tree = BSTree([100, 75, 125])
        self.assertTrue(tree.contains(100))
        self.assertFalse(tree.contains(200))

    def test_min_value(self):
        tree = BSTree([100, 75, 125, 150, -40])
        self.assertEqual(tree.min(), -40)

    def test_max_value(self):
        tree = BSTree([100, 75, 125, 150, 40])
        self.assertEqual(tree.max(), 150)

    def test_in_order_traversal_return_values_increasing_order(self):
        initialization_list = [100, 75, 125, -30, 150, 40, 20, 130]
        tree = BSTree(initialization_list)
        values = []
        for node in tree.in_order_traversal():
            values.append(node.value)
        self.assertEqual(values, sorted(initialization_list))

    def test_preserve_binary_search_invariant(self):
        initialization_list = create_random_array(500)
        tree = BSTree(initialization_list)
        self.assertTrue(tree._validate_bstree())

    def test_select(self):
        tree = BSTree([70, 50, 200, 30, 60, 55, 100, 300, 80, 150])
        self.assertEqual(tree.select(0), 30)
        self.assertEqual(tree.select(1), 50)
        self.assertEqual(tree.select(2), 55)
        self.assertEqual(tree.select(3), 60)
        self.assertEqual(tree.select(4), 70)
        self.assertEqual(tree.select(8), 200)
        self.assertEqual(tree.select(9), 300)

    def test_rank(self):
        tree = BSTree([70, 50, 200, 30, 60, 55, 100, 300, 80, 150])
        self.assertEqual(tree.rank(30), 0)
        self.assertEqual(tree.rank(50), 1)
        self.assertEqual(tree.rank(55), 2)
        self.assertEqual(tree.rank(60), 3)
        self.assertEqual(tree.rank(70), 4)
        self.assertEqual(tree.rank(200), 8)
        self.assertEqual(tree.rank(300), 9)

    def test_select_rank_are_inverses(self):
        tree = BSTree([70, 50, 200, 30, 60, 55, 100, 300, 80, 150])
        self.assertEqual(tree.select(tree.rank(30)), 30)
        self.assertEqual(tree.select(tree.rank(50)), 50)
        self.assertEqual(tree.select(tree.rank(55)), 55)
        self.assertEqual(tree.select(tree.rank(60)), 60)
        self.assertEqual(tree.select(tree.rank(70)), 70)
        self.assertEqual(tree.select(tree.rank(200)), 200)
        self.assertEqual(tree.select(tree.rank(300)), 300)

    def test_floor(self):
        tree = BSTree([100, 75, 125, 150, 40])
        self.assertTrue(tree.floor(100), 100)
        self.assertTrue(tree.floor(75), 75)
        self.assertTrue(tree.floor(125), 125)
        self.assertTrue(tree.floor(80), 75)
        self.assertTrue(tree.floor(130), 125)
        self.assertTrue(tree.floor(1000), 150)
        self.assertIsNone(tree.floor(30))

    def test_ceiling(self):
        tree = BSTree([100, 75, 125, 150, 40])
        self.assertTrue(tree.ceiling(100), 100)
        self.assertTrue(tree.ceiling(75), 75)
        self.assertTrue(tree.ceiling(125), 125)
        self.assertTrue(tree.ceiling(101), 125)
        self.assertTrue(tree.ceiling(0), 40)
        self.assertIsNone(tree.ceiling(1000))


if __name__ == '__main__':
    unittest.main()
