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
    # an optimized solution for space would be to have two runners
    # a fast runner runs at twice the speed of the slow runner
    # if fast runner catches up with slow runner at any point,
    # we can say we have a loop. But if fast runner ends the iteration
    # we know there is no loop

    # initialize fast_runner and slow_runner to the first_node
    slow_runner = first_node
    fast_runner = first_node
    # loop while slow_runner has a next and fast_runner has a next next
    while slow_runner.next and fast_runner.next.next:
        # set slow_runner to the next node
        slow_runner = slow_runner.next
        # set fast_runner to the next two nodes
        fast_runner = fast_runner.next.next
        # check if fast_runner and slow_runner are in the same position
        if fast_runner == slow_runner:
            # return True
            return True
    # return False
    return False
