from io import StringIO
import unittest
from unittest.mock import patch
from data_structures.binary_tree import *


"""
      3
   /     \
  2       4
 / \     / \
6   0   1   5
"""

root = TreeNode(3)
root.left = TreeNode(2); root.right = TreeNode(4)
root.left.left = TreeNode(6); root.left.right = TreeNode(0)
root.right.left = TreeNode(1); root.right.right = TreeNode(5)


class TestURLPrint(unittest.TestCase):

    def test_pre_order(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pre_order(root)
            self.assertEqual(fake_out.getvalue(), '3 2 6 0 4 1 5 ')

    def test_in_order(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            in_order(root)
            self.assertEqual(fake_out.getvalue(), '6 2 0 3 1 4 5 ')

    def test_post_order(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            post_order(root)
            self.assertEqual(fake_out.getvalue(), '6 0 2 1 5 4 3 ')

    def test_pre_order_iterative(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pre_order_iterative(root)
            self.assertEqual(fake_out.getvalue(), '3 2 6 0 4 1 5 ')

    def test_level_order(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            level_order(root)
            self.assertEqual(fake_out.getvalue(), '3 2 4 6 0 1 5 ')


if __name__ == '__main__':
    unittest.main()
