import unittest
from trees.rbtree import LLRBT, RED, BLACK
from utils.arrays import create_random_array


class RedBlackBSTreeTest(unittest.TestCase):
    def test_initialization_list(self):
        initialization_list = [100, 20, 200, 400]
        tree = LLRBT(initialization_list)
        self.assertEqual(tree.size, len(initialization_list))

    def test_bst_size(self):
        tree = LLRBT()
        self.assertEqual(tree.size, 0)
        tree.insert(100)
        self.assertEqual(tree.size, 1)
        tree.insert(200)
        tree.insert(50)
        self.assertEqual(tree.size, 3)
        tree.remove_min()
        self.assertEqual(tree.size, 2)

    def test_does_not_insert_repeated_values(self):
        tree = LLRBT()
        tree.insert(100)
        tree.insert(100)
        self.assertEqual(tree.size, 1)

    def test_insert_preserves_left_leaning_props(self):
        """
        http://algs4.cs.princeton.edu/33balanced/images/redblack-construction.png
        This image contains a visual representation of Red Black BST
        constructed with the keys used in these tests.
        The first assertion handle the left column Tree example and
        the second one, handle the right column Tree example.
        """

        # Example number 1
        tree = LLRBT(["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"])
        values = []
        for node in tree.pre_order_traversal():
            values.append((node.value, node.color))
        self.assertEqual(values, [("M", BLACK),
                                  ("E", BLACK),
                                  ("C", BLACK),
                                  ("A", RED),
                                  ("L", BLACK),
                                  ("H", RED),
                                  ("R", BLACK),
                                  ("P", BLACK),
                                  ("X", BLACK),
                                  ("S", RED)])

        # Example number 2 (keys are inserted in order)
        tree = LLRBT(["A", "C", "E", "H", "L", "M", "P", "R", "S", "X"])
        values = []
        for node in tree.pre_order_traversal():
            values.append((node.value, node.color))
        self.assertEqual(values, [("H", BLACK),
                                  ("C", BLACK),
                                  ("A", BLACK),
                                  ("E", BLACK),
                                  ("R", BLACK),
                                  ("M", RED),
                                  ("L", BLACK),
                                  ("P", BLACK),
                                  ("X", BLACK),
                                  ("S", RED)])

    def test_inserts_return_boolean_result(self):
        tree = LLRBT()
        self.assertTrue(tree.insert(100))
        self.assertFalse(tree.insert(100))

    def test_remove_min_preserves_llrbt_invariant(self):
        tree = LLRBT(["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"])
        """Initial tree (! = RED).
                        M
                E               R
             C     L         P     X
          !A    !H              !S
        """
        # Assert deletion of the smallest key and size of the tree
        self.assertEqual(tree.size, 10)
        self.assertTrue(tree.remove_min())
        self.assertEqual(tree.size, 9)
        self.assertFalse(tree.contains("A"))

        # Assert the tree has the correct shape
        values = []
        for node in tree.pre_order_traversal():
            values.append((node.value, node.color))

        """Representation after a delete_min operation (! = RED).
                        M
                E               R
             C     L         P     X
                !H              !S
        """
        self.assertEqual(values, [("M", BLACK),
                                  ("E", BLACK),
                                  ("C", BLACK),
                                  ("L", BLACK),
                                  ("H", RED),
                                  ("R", BLACK),
                                  ("P", BLACK),
                                  ("X", BLACK),
                                  ("S", RED)])

        # Assert deletion of the smallest key and size of the tree
        tree.remove_min()
        self.assertEqual(tree.size, 8)
        self.assertFalse(tree.contains("C"))

        # Assert the tree has the correct shape
        values = []
        for node in tree.pre_order_traversal():
            values.append((node.value, node.color))

        """Representation after two delete_min operations (! = RED).
                        M
                H               R
             E     L         P     X
                                !S
        """
        self.assertEqual(values, [("M", BLACK),
                                  ("H", BLACK),
                                  ("E", BLACK),
                                  ("L", BLACK),
                                  ("R", BLACK),
                                  ("P", BLACK),
                                  ("X", BLACK),
                                  ("S", RED)])

    def test_remove_max_preserves_llrbt_invariant(self):
        tree = LLRBT(["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"])
        """Initial tree (! = RED).
                        M
                E               R
             C     L         P     X
          !A    !H              !S
        """
        # Assert deletion of the greatest key and size of the tree
        self.assertEqual(tree.size, 10)
        self.assertTrue(tree.remove_max())
        self.assertEqual(tree.size, 9)
        self.assertFalse(tree.contains("X"))

        # Assert the tree has the correct shape
        values = []
        for node in tree.pre_order_traversal():
            values.append((node.value, node.color))

        """Representation after a delete_max operation (! = RED).
                        M
                E               R
             C     L         P     S
          !A    !H
        """
        self.assertEqual(values, [("M", BLACK),
                                  ("E", BLACK),
                                  ("C", BLACK),
                                  ("A", RED),
                                  ("L", BLACK),
                                  ("H", RED),
                                  ("R", BLACK),
                                  ("P", BLACK),
                                  ("S", BLACK)])

        # Assert deletion of the greatest key and size of the tree
        tree.remove_max()
        self.assertEqual(tree.size, 8)
        self.assertFalse(tree.contains("S"))

        # Assert the tree has the correct shape
        values = []
        for node in tree.pre_order_traversal():
            values.append((node.value, node.color))

        """Representation after two delete_max operations (! = RED).
                        M
               !E               R
             C     L         !P
          !A    !H
        """
        self.assertEqual(values, [("M", BLACK),
                                  ("E", RED),
                                  ("C", BLACK),
                                  ("A", RED),
                                  ("L", BLACK),
                                  ("H", RED),
                                  ("R", BLACK),
                                  ("P", RED)])

    def test_removes_return_boolean_result(self):
        tree = LLRBT([100, 75, 125])
        self.assertTrue(tree.remove(100))
        self.assertFalse(tree.remove(100))

    def test_removing_root_promotes_successor(self):
        tree = LLRBT([100, 75, 50, 95, 125, 150, 110])
        tree.remove(100)
        root = next(tree.pre_order_traversal())
        self.assertEqual(root.value, 110)

    def test_removing_min_until_empty(self):
        initialization_list = [100, 75, 125, -30, 150, 40, 20, 130]
        tree = LLRBT(initialization_list)
        removed_values = []
        while tree.size > 0:
            min_value = tree.min()
            removed_values.append(min_value)
            tree.remove(min_value)
        self.assertEqual(removed_values, sorted(initialization_list))

    def test_contains_value(self):
        tree = LLRBT([100, 75, 125])
        self.assertTrue(tree.contains(100))
        self.assertFalse(tree.contains(200))

    def test_min_value(self):
        tree = LLRBT([100, 75, 125, 150, -40])
        self.assertEqual(tree.min(), -40)

    def test_max_value(self):
        tree = LLRBT([100, 75, 125, 150, 40])
        self.assertEqual(tree.max(), 150)

    def test_in_order_traversal_return_values_increasing_order(self):
        initialization_list = ["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"]
        tree = LLRBT(initialization_list)
        values = []
        for v in tree.in_order_traversal():
            values.append(v.value)
        self.assertEqual(values, sorted(initialization_list))

    def test_integrity(self):
        initialization_list = create_random_array(1000)
        tree = LLRBT(initialization_list)

        # Delete 500 items
        for idx, n in enumerate(initialization_list[:800]):
            if n % 3 == 0:
                tree.remove_min()
            elif n % 3 == 1:
                tree.remove_max()
            else:
                tree.remove(initialization_list[idx])

        # If it raises an IntegrityError
        integrity_result = tree.check_integrity()
        self.assertGreater(integrity_result, 0)

    def test_select(self):
        tree = LLRBT([70, 50, 200, 30, 60, 55, 100, 300, 80, 150])
        self.assertEqual(tree.select(0), 30)
        self.assertEqual(tree.select(1), 50)
        self.assertEqual(tree.select(2), 55)
        self.assertEqual(tree.select(3), 60)
        self.assertEqual(tree.select(4), 70)
        self.assertEqual(tree.select(8), 200)
        self.assertEqual(tree.select(9), 300)

    def test_rank(self):
        tree = LLRBT([70, 50, 200, 30, 60, 55, 100, 300, 80, 150])
        self.assertEqual(tree.rank(30), 0)
        self.assertEqual(tree.rank(50), 1)
        self.assertEqual(tree.rank(55), 2)
        self.assertEqual(tree.rank(60), 3)
        self.assertEqual(tree.rank(70), 4)
        self.assertEqual(tree.rank(200), 8)
        self.assertEqual(tree.rank(300), 9)

    def test_select_rank_are_inverses(self):
        tree = LLRBT([70, 50, 200, 30, 60, 55, 100, 300, 80, 150])
        self.assertEqual(tree.select(tree.rank(30)), 30)
        self.assertEqual(tree.select(tree.rank(50)), 50)
        self.assertEqual(tree.select(tree.rank(55)), 55)
        self.assertEqual(tree.select(tree.rank(60)), 60)
        self.assertEqual(tree.select(tree.rank(70)), 70)
        self.assertEqual(tree.select(tree.rank(200)), 200)
        self.assertEqual(tree.select(tree.rank(300)), 300)

    def test_floor(self):
        tree = LLRBT([100, 75, 125, 150, 40])
        self.assertTrue(tree.floor(100), 100)
        self.assertTrue(tree.floor(75), 75)
        self.assertTrue(tree.floor(125), 125)
        self.assertTrue(tree.floor(80), 75)
        self.assertTrue(tree.floor(130), 125)
        self.assertTrue(tree.floor(1000), 150)
        self.assertIsNone(tree.floor(30))

    def test_ceiling(self):
        tree = LLRBT([100, 75, 125, 150, 40])
        self.assertTrue(tree.ceiling(100), 100)
        self.assertTrue(tree.ceiling(75), 75)
        self.assertTrue(tree.ceiling(125), 125)
        self.assertTrue(tree.ceiling(101), 125)
        self.assertTrue(tree.ceiling(0), 40)
        self.assertIsNone(tree.ceiling(1000))


if __name__ == '__main__':
    unittest.main()
