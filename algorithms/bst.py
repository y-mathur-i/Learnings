"""Module for binary search tree
"""


class TreeNode:
    """Node with val attr and left and right child
    """
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


class BST:
    """Binary search tree
        where nodes with value less than parent are on left
        and equal or greater than are on right.
    """
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        """Method to insert value in tree
        """
        curr = self.root
        if self.root is None:
            self.root = TreeNode(val=value)
        else:
            while True:
                if curr.val > value:
                    if curr.left is None:
                        curr.left = TreeNode(val=value)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = TreeNode(val=value)
                        break
                    curr = curr.right
        return

    def find(self, value: int) -> bool:
        """Method to find node in BST
        """
        curr = self.root
        while curr is not None:
            if curr.val < value:
                curr = curr.right
            elif curr.val > value:
                curr = curr.left
            else:
                return True
        return False


if __name__ == "__main__":
    bst = BST()
    vals = [5, 3, 6]
    for val in vals:
        bst.insert(val)
        assert bst.find(val)
    assert not bst.find(10)
