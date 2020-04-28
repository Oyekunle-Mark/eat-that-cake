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
    nodes_visited = set()
    # set current to first_node
    current = first_node
    # loop while current is not None
    while current:
        # check if current is in nodes_visited
        if current in nodes_visited:
            # return True
            return True
        # add current to nodes_visited
        nodes_visited.add(current)
        # set current to current's next
        current = current.next
    # return False
    return False


def contains_cycle_optimize(first_node):
    pass
