import unittest

from avl_node import AVLNode, insert, min_value_node, max_value_node, get_balance, sum_keys


class TestAVLNode(unittest.TestCase):
    def test_initialization(self):
        node = AVLNode(10)
        self.assertEqual(node.key, 10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        self.assertEqual(node.height, 1)

    def test_insert_left(self):
        root = AVLNode(10)
        root.left = AVLNode(5)
        self.assertEqual(root.left.key, 5)
        self.assertEqual(root.left.height, 1)

    def test_insert_right(self):
        root = AVLNode(10)
        root.right = AVLNode(15)
        self.assertEqual(root.right.key, 15)
        self.assertEqual(root.right.height, 1)

    def test_height_update(self):
        root = None
        keys = [10, 5, 15]
        for key in keys:
            root = insert(root, key)
        self.assertEqual(root.height, 2)

    def test_balance_factor(self):
        root = None
        keys = [10, 5, 15]
        for key in keys:
            root = insert(root, key)
        self.assertEqual(get_balance(root), 0)

    def test_find_min(self):
        root = None
        keys = [10, 5, 2]
        for key in keys:
            root = insert(root, key)
        self.assertEqual(min_value_node(root).key, 2)

    def test_find_max(self):
        root = None
        keys = [10, 15, 20]
        for key in keys:
            root = insert(root, key)
        self.assertEqual(max_value_node(root).key, 20)

    def test_complex_tree_find_min(self):
        root = None
        keys = [10, 5, 15, 2, 7, 12, 20, 1, 8]
        for key in keys:
            root = insert(root, key)
        self.assertEqual(min_value_node(root).key, 1)

    def test_complex_tree_find_max(self):
        root = None
        keys = [10, 5, 15, 2, 7, 12, 20, 25, 8]
        for key in keys:
            root = insert(root, key)
        self.assertEqual(max_value_node(root).key, 25)

    def test_sum_keys(self):
        root = None
        keys = [10, 5, 15, 2, 7, 12, 20, 1, 8]
        for key in keys:
            root = insert(root, key)
        self.assertEqual(sum_keys(root), sum(keys))

if __name__ == "__main__":
    unittest.main()
