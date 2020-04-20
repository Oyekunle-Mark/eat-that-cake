# use the deque class from the collections module
from collections import deque


def get_path(graph, start_node, end_node):
    # initialize queue to an instance of deque class
    # initialize visited to an empty set
    # enqueue the start_node node as a list into the queue
    # loop while queue is not empty
        # dequeue the path from the queue
        # get the last_node from the path
        # if the last_node is equivalent to the end_node
            # return the path
        # if the last_node has not been visited
            # add it to the visited
            # for every node connected to last_node
                # initialize new_path to a copy of path
                # append node to new_path
                # enqueue new_path into the queue
    pass
