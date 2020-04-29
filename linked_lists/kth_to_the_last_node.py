def kth_to_last_node(k, head):
    # this can be done is O(1) time and space
    # the approach will be to keep track of the node that was encountered
    # two nodes ago as we loop through the linked list
    # every node from the kth node onward, we set the kth to the last node
    # to the next node
    # initialize count to zero
    count = 0
    # initialize kth_to_last to the head
    kth_to_last = head
    # initialize current to the head
    current = head
    # loop through all the nodes
    while current:
        # increment count by one
        count += 1
        # set current to the next node
        current = current.next
        # check if count is greater than k
        if count > k:
            # set kth_to_last to the next node after it.
            kth_to_last = kth_to_last.next
    # if count is less than k
    if k == 0 or count < k:
        # raise an exception
        raise Exception("K cannot be zero or greater than Linked List length")
    # return kth_to_last
    return kth_to_last
