import unittest
from lab import BinaryTree, leftLeavesSum


class TestBinaryTreeLeftLeavesSum(unittest.TestCase):
    def setUp(self):
        self.root1 = BinaryTree(1)
        self.root1.left = BinaryTree(2)
        self.root1.right = BinaryTree(3)
        self.root1.right.left = BinaryTree(8)
        self.root1.left.left = BinaryTree(4)
        self.root1.left.right = BinaryTree(5)
        self.root1.left.left.left = BinaryTree(7)

        self.root2 = BinaryTree(10)
        self.root2.left = BinaryTree(20)
        self.root2.right = BinaryTree(30)
        self.root2.right.left = BinaryTree(40)
        self.root2.left.left = BinaryTree(50)
        self.root2.left.right = BinaryTree(60)
        self.root2.left.left.left = BinaryTree(70)

        self.root3 = BinaryTree(100)
        self.root3.left = BinaryTree(200)
        self.root3.right = BinaryTree(300)
        self.root3.right.left = BinaryTree(400)
        self.root3.left.left = BinaryTree(500)
        self.root3.left.right = BinaryTree(600)
        self.root3.left.left.left = BinaryTree(700)

    def test_leftLeavesSum_root(self):
        result = leftLeavesSum(self.root1)
        self.assertEqual(result, 15)

    def test_leftLeavesSum_with_isleft_true(self):
        result = leftLeavesSum(self.root2)
        self.assertEqual(result, 110)

    def test_leftLeavesSum_with_isleft_false(self):
        result = leftLeavesSum(self.root3)
        self.assertEqual(result, 1100)

    def test_leftLeavesSum_empty_tree(self):
        result = leftLeavesSum(None)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
