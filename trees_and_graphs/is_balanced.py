def is_balanced(tree_root):
    # initialize stack to empty list
    stack = []
    # initialize depths to empty list
    depths = []
    # push node and depth as a zero onto stack as a tuple
    stack.append((tree_root, 0))
    # while stack is not empty
    while len(stack):
        # pop the node and depth from stack
        node, depth = stack.pop()
        # if current node does not have a left and right child
        # that is, the node is a leaf node
        if node.left is None and node.right is None:
            # push depth onto the depths list
            depths.append(depth)
            # if depths is longer that two or absolute difference between
            # the two depths is greater than one
            if len(depths) > 2 or (len(depths) > 1 and abs(depths[0] - depths[1]) > 1):
                # return False
                return False
        # if there is a left child
        if node.left is not None:
            # push the left node and its depth plus one onto the stack
            stack.append((node.left, 1 + depth))
        # if there is a right child
        if node.right is not None:
            # push the right node and its depth plus one onto the stack
            stack.append((node.right, 1 + depth))
    # return True
    return True
