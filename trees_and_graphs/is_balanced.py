def is_balanced(tree_root):
    # initialize stack to empty list
    # initialize depths to empty list
    # push node and value onto stack as a tuple
    # while stack is not empty
        # pop the node and depth from stack
        # if current node does not have a left and right child
        # that is, the node is a leaf node
            # push depth onto the depths list
            # if depths is longer that two or absolute difference between
            # the two depths is greater than one
                # return False
        # if there is a left child
            # push the left node and its depth plus one onto the stack
        # if there is a right child
            # push the right node and its depth plus one onto the stack
    # return True
    pass
