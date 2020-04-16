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


def is_binary_search_tree(root):
    # check if the root is an empty node
        # return True
    # create a stack
    # push root onto the stack
    # loop while stack is not empty
        # pop node from the stack
        # if node has a left child
            # if value of left child is greater than value of node
                # return False
            # push node onto the stack
        # if node has a right child
            # if value of right child is greater than value of node
                # return False
            # push node onto the stack
    # return True
    pass
