class BinaryTree:
    """
    Class represent binary tree
    """
    def __init__(self, value):
        """
        Contructor of BinaryTree class
        :param value:
        """
        self.value = value
        self.left = None
        self.right = None


def left_leaves_sum(root: BinaryTree, is_left: bool = False):
    """
    Method that calculate sum of left leaves in binary tree
    :param root:
    :param is_left:
    :return: sum
    """
    if root is None:
        return 0

    if root.left is None and root.right is None and is_left:
        return root.value

    return left_leaves_sum(root.left, True) + left_leaves_sum(root.right, False)
