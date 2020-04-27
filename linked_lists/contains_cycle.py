"""
class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None
"""


def contains_cycle(first_node):
    # the plan would be to iterate through the linked list
    # in one pass and add the nodes to a set as they are visited
    # when a node is found in the set already, return False

    # initialize nodes_visited to an empty set
    # set current to first_node
    # loop while current is not None
        # check if current is in nodes_visited
            # return False
        # add current to nodes_visited
        # set current to current's next
    # return False
    pass
