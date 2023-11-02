class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def leftLeavesSum(root: BinaryTree, isleft: bool = False):
    if root is None:
        return 0

    if root.left is None and root.right is None and isleft:
        return root.value

    return leftLeavesSum(root.left, True) + leftLeavesSum(root.right, False)
