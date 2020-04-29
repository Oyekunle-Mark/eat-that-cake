def kth_to_last_node(k, head):
    # this can be done is O(1) time and space
    # the approach will be to keep track of the node that was encountered
    # two nodes ago as we loop through the linked list
    # every node from the kth node onward, we set the kth to the last node
    # to the next node
    # initialize count to zero
    # initialize kth_to_last to the head
    # initialize current to the head
    # loop through all the nodes
        # increment count by one
        # set current to the next node
        # check if count is greater than k
            # set kth_to_last to the next node after it.
    # if count is less than k
        # raise an exception
    # return kth_to_last
    pass
