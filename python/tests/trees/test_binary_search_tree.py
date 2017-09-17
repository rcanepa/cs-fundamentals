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
        self.assertEqual(root, 110)

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
        for v in tree.in_order_traversal():
            values.append(v)
        self.assertEqual(values, sorted(initialization_list))

    def test_preserve_binary_search_invariant(self):
        initialization_list = create_random_array(500)
        tree = BSTree(initialization_list)
        self.assertTrue(tree._validate_bstree())


if __name__ == '__main__':
    unittest.main()
