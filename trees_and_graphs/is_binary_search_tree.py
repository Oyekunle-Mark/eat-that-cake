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
    # if the root node is empty
        # return True
    # create a stack to hold the at tuple of the node, the lower_bound and upper_bound
    # push the root, negative infinity as lower bound
    # and positive infinity as upper bound
    # loop while stack is not empty
        # pop the node, lower_bound and upper_bound from the stack
        # check if node's value is less than or equal to the lower bound
        # or greater than or equal to the upper bound
            # return False
        # if there is a left child
            # push it onto the stack with negative infinity as lower bound
            # and node value as upper bound
        # if there is a right child
            # push it onto the stack with positive infinity as upper bound
            # and node value as lower bound
    # return True
    pass
