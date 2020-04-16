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
    if root.value is None:
        # return True
        return True
    # create a stack
    stack = []
    # push root onto the stack
    stack.append(root)
    # loop while stack is not empty
    while len(stack) > 0:
        # pop node from the stack
        node = stack.pop()
        # if node has a left child
        if node.left is not None:
            # if value of left child is greater than value of node
            # of node value if greater than the root node value
            if node.left.value > node.value or node.left.value > root.value:
                # return False
                return False
            # push node onto the stack
            stack.append(node.left)
        # if node has a right child
        if node.right is not None:
            # if value of right child is less than value of node
            # or node value if less than the root node value
            if node.right.value < node.value or node.right.value < root.value:
                # return False
                return False
            # push node onto the stack
            stack.append(node.right)
    # return True
    return True
