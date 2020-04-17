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


def find_largest(root_node):
    # set the current_node to the root_node
    current_node = root_node
    # while there is a current_node
    while current_node:
        # if current_node does not have a right child node
        if current_node.right is None:
            # return current_node's value
            return current_node.value
        # set current_node to current_node's right child node
        current_node = current_node.right


def find_second_largest(root_node):
    # Perform a biased DFT
    # keep going down to the right child node until
    # there is no right child node anymore
    # at that point return the last node parent node

    # if the root_node is empty or does not have any child nodes
    if (root_node.value is None) or (root_node.right is None and root_node.left is None):
        # raise exception
        raise ValueError("Root node cannot be empty or be a single node")
    # if there is a left subtree without a right
        # return the largest value from the left subtree
    # initialize the current_node to the root_node
    current_node = root_node
    previous_node = None
    # loop while current_node
    while current_node:
        # if the current_node does not have a right child node
        if current_node.right is None:
            # if previous_node has a left child node
                # return the largest value from the left subtree
            # return the current_node's value
            return previous_node.value
        # set current_node to the current_node's right child node
        previous_node = current_node
        current_node = current_node.right
