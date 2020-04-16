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
    if root.value is None:
        # return True
        return True
    # create a stack to hold the at tuple of the node, the lower_bound and upper_bound
    # push the root, negative infinity as lower bound
    # and positive infinity as upper bound
    stack = []
    stack.append((root, -float('inf'), float('inf')))
    # loop while stack is not empty
    while len(stack) > 0:
        # pop the node, lower_bound and upper_bound from the stack
        node, lower_bound, upper_bound = stack.pop()
        # check if node's value is less than or equal to the lower bound
        # or greater than or equal to the upper bound
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            # return False
            return False
        # if there is a left child
        if node.left is not None:
            # push it onto the stack with negative infinity as lower bound
            # and node value as upper bound
            stack.append((node.left, lower_bound, node.value))
        # if there is a right child
        if node.right is not None:
            # push it onto the stack with positive infinity as upper bound
            # and node value as lower bound
            stack.append((node.right, node.value, upper_bound))
    # return True
    return True
