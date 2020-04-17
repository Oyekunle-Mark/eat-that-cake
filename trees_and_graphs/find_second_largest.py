"""
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
"""


def find_second_largest(root_node):
    # Perform a biased DFT
    # keep going down to the right child node until
    # there is no right child node anymore
    # at that point return the last node parent node
    pass
